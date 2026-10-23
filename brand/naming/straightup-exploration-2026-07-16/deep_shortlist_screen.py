from __future__ import annotations

import csv
import json
import re
import unicodedata
from pathlib import Path

import duckdb
import pandas as pd


HERE = Path(__file__).resolve().parent
DATA_DIR = Path(r"C:\tmp\uspto_tm_screen")
CASE_FILES = [
    DATA_DIR / "case_file_0.parquet",
    DATA_DIR / "case_file_1.parquet",
]
CLASSIFICATION_FILE = DATA_DIR / "classification.parquet"
INTL_CLASS_FILE = DATA_DIR / "intl_class.parquet"
STATUS_FILE = DATA_DIR / "status_codes.csv"

HITS_PATH = HERE / "deep-federal-hits.csv"
SUMMARY_PATH = HERE / "deep-federal-summary.csv"
META_PATH = HERE / "deep-federal-meta.json"

RELEVANT_CLASSES = {"003", "005", "010", "021", "035", "044"}

# These patterns deliberately go beyond exact identity and edit distance one.
# They probe dominant matter, obvious collapsed phrases, and practical phonetic
# spellings that could create a similar commercial impression.
PATTERNS = {
    "Hide Nothing": [
        ("phrase-family", "hidenothing"),
        ("reversal", "nothinghidden"),
    ],
    "As Shown": [
        ("phrase-family", "asshown"),
        ("phrase-family", "shownas"),
    ],
    "No Asterisk": [
        ("dominant", "asterisk"),
        ("phonetic", "asterix"),
    ],
    "Stand By It": [
        ("phrase-family", "standby"),
        ("phrase-family", "standwithit"),
    ],
    "Sure Enough": [
        ("phonetic", "shonuff"),
        ("phonetic", "shonuf"),
        ("phonetic", "shoenough"),
        ("phonetic", "sureenuff"),
        ("phonetic", "surenough"),
        ("phonetic", "shurenough"),
    ],
    "We Mean It": [
        ("phrase-family", "wemeanit"),
        ("dominant", "meanit"),
    ],
    "Spelled Out": [
        ("phrase-family", "spelledout"),
        ("phrase-family", "spellitout"),
        ("phrase-family", "spellout"),
    ],
    "In Writing": [
        ("phrase-family", "inwriting"),
        ("phrase-family", "allinwriting"),
    ],
    "Put Plainly": [
        ("dominant", "plainly"),
        ("phrase-family", "putplain"),
    ],
    "Plain to See": [
        ("phrase-family", "plaintosee"),
        ("phrase-family", "plainsee"),
        ("phrase-family", "plain2see"),
    ],
    "Show the Work": [
        ("phrase-family", "showthework"),
        ("phrase-family", "showyourwork"),
        ("reversal", "workshown"),
    ],
    "With Reason": [
        ("phrase-family", "withreason"),
        ("reversal", "reasonwith"),
    ],
    "Made Plain": [
        ("phrase-family", "madeplain"),
        ("reversal", "plainmade"),
    ],
    "Proof Required": [
        ("phrase-family", "proofrequired"),
        ("reversal", "requiredproof"),
        ("dominant", "proof"),
    ],
    "Word Kept": [
        ("phrase-family", "wordkept"),
        ("reversal", "keptword"),
        ("phrase-family", "keepyourword"),
    ],
    "Word and Deed": [
        ("phrase-family", "wordanddeed"),
        ("plural", "wordsanddeeds"),
        ("phrase-family", "worddeed"),
    ],
    "No Mystery": [
        ("phrase-family", "nomystery"),
        ("phrase-family", "mysteryfree"),
    ],
    "In Full View": [
        ("phrase-family", "infullview"),
        ("dominant", "fullview"),
    ],
    "No Footnote": [
        ("phrase-family", "nofootnote"),
        ("plural", "nofootnotes"),
        ("phrase-family", "footnotefree"),
        ("dominant", "footnote"),
    ],
    "No Theater": [
        ("phrase-family", "notheater"),
        ("british-spelling", "notheatre"),
        ("phrase-family", "theaterfree"),
        ("phrase-family", "theatrefree"),
    ],
    "More Than Talk": [
        ("phrase-family", "morethantalk"),
        ("phrase-family", "beyondtalk"),
    ],
    "No Blind Faith": [
        ("phrase-family", "noblindfaith"),
        ("dominant", "blindfaith"),
    ],
    "In Daylight": [
        ("phrase-family", "indaylight"),
        ("dominant", "daylight"),
    ],
    "All Adds Up": [
        ("phrase-family", "alladdsup"),
        ("phrase-family", "italladdsup"),
        ("dominant", "addsup"),
    ],
    "Does What It Says": [
        ("phrase-family", "doeswhatitsays"),
        ("phrase-family", "dowhatitsays"),
        ("phrase-family", "whatitsays"),
    ],
}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.lower())


def load_status_lookup() -> pd.DataFrame:
    with STATUS_FILE.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    frame = pd.DataFrame(rows)
    frame["code"] = frame["code"].astype(str).str.zfill(3)
    return frame[frame["live_dead_indicator"].str.startswith("Live", na=False)].copy()


def main() -> None:
    pattern_rows: list[dict[str, str]] = []
    for candidate, patterns in PATTERNS.items():
        candidate_norm = normalize(candidate)
        pattern_rows.append(
            {
                "candidate": candidate,
                "pattern_type": "exact",
                "pattern": candidate_norm,
                "match_mode": "exact",
            }
        )
        for pattern_type, pattern in patterns:
            pattern_rows.append(
                {
                    "candidate": candidate,
                    "pattern_type": pattern_type,
                    "pattern": normalize(pattern),
                    "match_mode": "contains",
                }
            )

    patterns = pd.DataFrame(pattern_rows).drop_duplicates()
    live_status = load_status_lookup()

    connection = duckdb.connect()
    connection.execute("PRAGMA threads=4")
    connection.register("pattern_frame", patterns)
    connection.register("live_status_frame", live_status)
    connection.execute("CREATE TEMP TABLE patterns AS SELECT * FROM pattern_frame")
    connection.execute("CREATE TEMP TABLE live_status AS SELECT * FROM live_status_frame")

    case_paths = ", ".join(f"'{path.as_posix()}'" for path in CASE_FILES)
    connection.execute(
        f"""
        CREATE TEMP TABLE pattern_hits AS
        WITH marks AS (
            SELECT
                serial_no,
                registration_no,
                mark_id_char,
                filing_dt,
                status_cd,
                lower(
                    regexp_replace(
                        strip_accents(mark_id_char),
                        '[^A-Za-z0-9]',
                        '',
                        'g'
                    )
                ) AS mark_norm
            FROM read_parquet([{case_paths}])
            WHERE mark_id_char IS NOT NULL
        )
        SELECT
            patterns.candidate,
            patterns.pattern_type,
            patterns.pattern,
            marks.serial_no,
            marks.registration_no,
            marks.mark_id_char,
            marks.mark_norm,
            marks.filing_dt,
            marks.status_cd
        FROM marks
        INNER JOIN live_status ON marks.status_cd = live_status.code
        INNER JOIN patterns
            ON (
                patterns.match_mode = 'exact'
                AND marks.mark_norm = patterns.pattern
            ) OR (
                patterns.match_mode = 'contains'
                AND contains(marks.mark_norm, patterns.pattern)
            )
        WHERE marks.mark_norm <> ''
        """
    )

    connection.execute(
        """
        CREATE TEMP TABLE matched_serials AS
        SELECT DISTINCT serial_no FROM pattern_hits
        """
    )
    relevant_sql = ", ".join(f"'{code}'" for code in sorted(RELEVANT_CLASSES))
    connection.execute(
        f"""
        CREATE TEMP TABLE active_classes AS
        SELECT
            classification.serial_no,
            string_agg(
                DISTINCT intl.intl_class_cd,
                ',' ORDER BY intl.intl_class_cd
            ) AS active_classes,
            bool_or(intl.intl_class_cd IN ({relevant_sql})) AS has_relevant_class
        FROM read_parquet('{CLASSIFICATION_FILE.as_posix()}') AS classification
        INNER JOIN matched_serials
            ON classification.serial_no = matched_serials.serial_no
        LEFT JOIN read_parquet('{INTL_CLASS_FILE.as_posix()}') AS intl
            ON classification.serial_no = intl.serial_no
            AND classification.class_seq = intl.class_seq
        WHERE classification.class_status_cd = '6'
        GROUP BY classification.serial_no
        """
    )

    hits = connection.execute(
        """
        SELECT
            pattern_hits.*,
            coalesce(active_classes.active_classes, '') AS active_classes
        FROM pattern_hits
        INNER JOIN active_classes USING (serial_no)
        WHERE active_classes.has_relevant_class
        ORDER BY candidate, pattern_type, filing_dt DESC, mark_id_char
        """
    ).fetchdf()
    connection.close()

    hits = hits.drop_duplicates(
        ["candidate", "pattern_type", "pattern", "serial_no"]
    )
    hits.to_csv(HITS_PATH, index=False, encoding="utf-8-sig")

    summary_rows: list[dict[str, object]] = []
    for candidate in PATTERNS:
        candidate_hits = hits[hits["candidate"] == candidate]
        exact = candidate_hits[candidate_hits["pattern_type"] == "exact"]
        broader = candidate_hits[candidate_hits["pattern_type"] != "exact"]
        representative = "; ".join(
            f"{row.mark_id_char} (SN {row.serial_no}; classes {row.active_classes}; via {row.pattern})"
            for row in broader.head(8).itertuples(index=False)
        )
        summary_rows.append(
            {
                "candidate": candidate,
                "live_relevant_exact_count": exact["serial_no"].nunique(),
                "live_relevant_broader_count": broader["serial_no"].nunique(),
                "representative_broader_hits": representative,
            }
        )

    summary = pd.DataFrame(summary_rows)
    summary.to_csv(SUMMARY_PATH, index=False, encoding="utf-8-sig")
    meta = {
        "candidate_count": len(PATTERNS),
        "pattern_count": len(patterns),
        "live_relevant_hit_rows": len(hits),
        "corpus_distinct_serials": 14_180_757,
        "corpus_latest_source_date": "2026-07-06",
        "relevant_classes": sorted(RELEVANT_CLASSES),
        "scope": "Live U.S. federal records matching exact, dominant, phrase-family, reversal, or listed phonetic patterns.",
    }
    META_PATH.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(summary.to_string(index=False))
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
