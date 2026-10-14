from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

import duckdb
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
NAMING_DIR = SCRIPT_DIR.parent
DATA_DIR = Path(r"C:\tmp\uspto_tm_screen")

REPORTS = [
    (1, NAMING_DIR / "net-new-250-2026-07-16.md"),
    (2, NAMING_DIR / "net-new-250-wave2-2026-07-16.md"),
    (3, NAMING_DIR / "net-new-250-wave3-2026-07-16.md"),
    (4, NAMING_DIR / "net-new-250-wave4-2026-07-16.md"),
]

CASE_FILES = [
    DATA_DIR / "case_file_0.parquet",
    DATA_DIR / "case_file_1.parquet",
]
CLASSIFICATION_FILE = DATA_DIR / "classification.parquet"
INTL_CLASS_FILE = DATA_DIR / "intl_class.parquet"
STATUS_FILE = DATA_DIR / "status_codes.csv"

OUTPUT_REPORT = NAMING_DIR / "basic-trademark-knockout-1000-2026-07-16.md"
OUTPUT_RESULTS = SCRIPT_DIR / "trademark-screening-results.csv"
OUTPUT_HITS = SCRIPT_DIR / "trademark-screening-hits.csv"
OUTPUT_SUMMARY = SCRIPT_DIR / "trademark-screening-summary.json"

# Core skincare/cosmetics plus plausible adjacent launch/extension classes.
RELEVANT_CLASSES = {"003", "005", "010", "021", "035", "044"}

ROW_RE = re.compile(
    r"^\|\s*(?P<number>\d+)\s*\|\s*(?P<name>.*?)\s*\|\s*"
    r"(?P<score>\d+(?:\.\d+)?)\s*\|"
)


def normalize_name(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_text = "".join(
        ch for ch in decomposed if not unicodedata.combining(ch)
    ).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", "", ascii_text.lower())


def read_candidates() -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    candidate_id = 0
    for wave, report_path in REPORTS:
        found: list[dict[str, object]] = []
        for line in report_path.read_text(encoding="utf-8").splitlines():
            match = ROW_RE.match(line)
            if not match:
                continue
            number = int(match.group("number"))
            if not 1 <= number <= 250:
                continue
            name = match.group("name").strip()
            score = float(match.group("score"))
            found.append(
                {
                    "candidate_id": candidate_id,
                    "wave": wave,
                    "wave_number": number,
                    "name": name,
                    "score": score,
                    "norm": normalize_name(name),
                }
            )
            candidate_id += 1
        if len(found) != 250:
            raise ValueError(f"Expected 250 rows in {report_path}, found {len(found)}")
        rows.extend(found)

    frame = pd.DataFrame(rows)
    if len(frame) != 1000:
        raise ValueError(f"Expected 1,000 total candidates, found {len(frame)}")
    if frame["norm"].duplicated().any():
        duplicates = frame.loc[frame["norm"].duplicated(False), ["name", "norm"]]
        raise ValueError(f"Normalized candidate duplicates found:\n{duplicates}")
    return frame


def edit_one_variants(value: str) -> dict[str, str]:
    """Return practical edit-distance-one variants for compact names.

    Full near-variant generation is deliberately limited to names 5-18
    characters long. Longer proposition names are screened by exact normalized
    identity; this keeps the basic pass focused and avoids noisy phrase typos.
    """
    if not 5 <= len(value) <= 18:
        return {}

    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    variants: dict[str, str] = {}

    for index in range(len(value)):
        variants[value[:index] + value[index + 1 :]] = "deletion"

    for index in range(len(value) - 1):
        if value[index] != value[index + 1]:
            variant = (
                value[:index]
                + value[index + 1]
                + value[index]
                + value[index + 2 :]
            )
            variants[variant] = "transposition"

    for index, original in enumerate(value):
        for char in alphabet:
            if char != original:
                variants[value[:index] + char + value[index + 1 :]] = "substitution"

    for index in range(len(value) + 1):
        for char in alphabet:
            variants[value[:index] + char + value[index:]] = "insertion"

    variants.pop(value, None)
    return variants


def build_search_keys(candidates: pd.DataFrame) -> pd.DataFrame:
    rows: list[tuple[int, str, str, int]] = []
    for candidate in candidates.itertuples(index=False):
        rows.append((candidate.candidate_id, candidate.norm, "EXACT", 0))
        for variant, variant_type in edit_one_variants(candidate.norm).items():
            rows.append(
                (
                    candidate.candidate_id,
                    variant,
                    f"NEAR_1_{variant_type.upper()}",
                    1,
                )
            )
    frame = pd.DataFrame(
        rows, columns=["candidate_id", "norm_key", "hit_type", "distance"]
    )
    frame = frame.drop_duplicates(["candidate_id", "norm_key"], keep="first")
    return frame


def load_status_lookup() -> pd.DataFrame:
    with STATUS_FILE.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    frame = pd.DataFrame(rows)
    frame["code"] = frame["code"].astype(str).str.zfill(3)
    return frame


def query_hits(
    candidates: pd.DataFrame, search_keys: pd.DataFrame, status_lookup: pd.DataFrame
) -> pd.DataFrame:
    connection = duckdb.connect()
    connection.execute("PRAGMA threads=4")
    connection.register("candidate_frame", candidates)
    connection.register("search_key_frame", search_keys)
    connection.register("status_frame", status_lookup)
    connection.execute("CREATE TEMP TABLE candidates AS SELECT * FROM candidate_frame")
    connection.execute("CREATE TEMP TABLE search_keys AS SELECT * FROM search_key_frame")
    connection.execute("CREATE TEMP TABLE status_lookup AS SELECT * FROM status_frame")

    case_paths = ", ".join(f"'{path.as_posix()}'" for path in CASE_FILES)
    connection.execute(
        f"""
        CREATE TEMP TABLE hits_raw AS
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
        ), joined AS (
            SELECT
                keys.candidate_id,
                keys.hit_type,
                keys.distance,
                marks.serial_no,
                marks.registration_no,
                marks.mark_id_char,
                marks.filing_dt,
                marks.status_cd,
                marks.mark_norm,
                status.description AS status_description,
                status.live_dead_indicator,
                starts_with(status.live_dead_indicator, 'Live') AS is_live
            FROM marks
            INNER JOIN search_keys AS keys
                ON marks.mark_norm = keys.norm_key
            LEFT JOIN status_lookup AS status
                ON marks.status_cd = status.code
            WHERE marks.mark_norm <> ''
        )
        SELECT * EXCLUDE (preference)
        FROM (
            SELECT
                joined.*,
                row_number() OVER (
                    PARTITION BY candidate_id, serial_no
                    ORDER BY distance, hit_type
                ) AS preference
            FROM joined
        )
        WHERE preference = 1
        """
    )

    connection.execute(
        """
        CREATE TEMP TABLE matched_serials AS
        SELECT DISTINCT serial_no FROM hits_raw
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
            hits_raw.*,
            coalesce(active_classes.active_classes, '') AS active_classes,
            coalesce(active_classes.has_relevant_class, false) AS has_relevant_class
        FROM hits_raw
        LEFT JOIN active_classes USING (serial_no)
        ORDER BY candidate_id, distance, is_live DESC, filing_dt DESC, serial_no
        """
    ).fetchdf()
    connection.close()
    return hits


def classify_candidate(candidate_hits: pd.DataFrame) -> tuple[str, str]:
    if candidate_hits.empty:
        return "PROVISIONAL PASS", "No exact or edit-distance-one federal record found"

    exact = candidate_hits[candidate_hits["distance"] == 0]
    near = candidate_hits[candidate_hits["distance"] == 1]
    live_exact = exact[exact["is_live"] == True]  # noqa: E712
    live_near = near[near["is_live"] == True]  # noqa: E712

    if (live_exact["has_relevant_class"] == True).any():  # noqa: E712
        return "RED - LIVE EXACT / RELEVANT", "Exact live hit in a relevant active class"
    if not live_exact.empty:
        return "AMBER - LIVE EXACT", "Exact live hit; active classes appear outside core set or are missing"
    if (live_near["has_relevant_class"] == True).any():  # noqa: E712
        return "AMBER - LIVE NEAR / RELEVANT", "One-edit live hit in a relevant active class"
    if not live_near.empty:
        return "YELLOW - LIVE NEAR", "One-edit live hit outside the core active-class set"
    if not exact.empty:
        return "YELLOW - DEAD EXACT", "Exact federal record exists but is coded dead/unknown"
    return "PROVISIONAL PASS", "Only dead/unknown one-edit records found"


def representative_hits(candidate_hits: pd.DataFrame, limit: int = 3) -> str:
    if candidate_hits.empty:
        return ""

    def display_rank(row: pd.Series) -> int:
        is_live = bool(row["is_live"])
        is_relevant = bool(row["has_relevant_class"])
        is_exact = int(row["distance"]) == 0
        if is_live and is_exact and is_relevant:
            return 0
        if is_live and is_exact:
            return 1
        if is_live and is_relevant:
            return 2
        if is_live:
            return 3
        if is_exact:
            return 4
        return 5

    ordered = candidate_hits.assign(
        display_rank=candidate_hits.apply(display_rank, axis=1)
    ).sort_values(
        ["display_rank", "filing_dt"],
        ascending=[True, False],
    )
    samples: list[str] = []
    for hit in ordered.head(limit).itertuples(index=False):
        match_kind = "exact" if hit.distance == 0 else "near-1"
        lifecycle = "live" if bool(hit.is_live) else "dead/unknown"
        reg = f"; RN {hit.registration_no}" if pd.notna(hit.registration_no) else ""
        classes = f"; classes {hit.active_classes}" if hit.active_classes else ""
        samples.append(
            f'{hit.mark_id_char} (SN {hit.serial_no}{reg}; {lifecycle}; {match_kind}{classes})'
        )
    return "; ".join(samples)


def build_results(candidates: pd.DataFrame, hits: pd.DataFrame) -> pd.DataFrame:
    grouped = {key: group.copy() for key, group in hits.groupby("candidate_id")}
    result_rows: list[dict[str, object]] = []
    for candidate in candidates.itertuples(index=False):
        candidate_hits = grouped.get(candidate.candidate_id, hits.iloc[0:0])
        decision, reason = classify_candidate(candidate_hits)
        exact = candidate_hits[candidate_hits["distance"] == 0]
        near = candidate_hits[candidate_hits["distance"] == 1]
        live_exact = exact[exact["is_live"] == True]  # noqa: E712
        live_near = near[near["is_live"] == True]  # noqa: E712
        result_rows.append(
            {
                "candidate_id": candidate.candidate_id,
                "wave": candidate.wave,
                "wave_number": candidate.wave_number,
                "name": candidate.name,
                "score": candidate.score,
                "decision": decision,
                "reason": reason,
                "live_exact_count": len(live_exact),
                "live_near_count": len(live_near),
                "dead_or_unknown_exact_count": len(exact) - len(live_exact),
                "all_hit_count": len(candidate_hits),
                "representative_hits": representative_hits(candidate_hits),
            }
        )
    return pd.DataFrame(result_rows)


def markdown_escape(value: object) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_report(results: pd.DataFrame, hits: pd.DataFrame, key_count: int) -> None:
    decision_order = [
        "RED - LIVE EXACT / RELEVANT",
        "AMBER - LIVE EXACT",
        "AMBER - LIVE NEAR / RELEVANT",
        "YELLOW - LIVE NEAR",
        "YELLOW - DEAD EXACT",
        "PROVISIONAL PASS",
    ]
    counts = results["decision"].value_counts().to_dict()

    lines = [
        "# Basic U.S. trademark knockout screen - 1,000 names",
        "",
        "> **Purpose:** A basic, non-legal knockout pass for immediate federal-record issues. It is not a comprehensive clearance opinion and does not cover common-law use, state marks, domains, social handles, foreign registers, trade names, phonetic/conceptual similarity beyond the simple one-edit rule, or legal likelihood-of-confusion analysis.",
        ">",
        "> **Data:** Local comparison against a public mirror of USPTO government-work case files. The downloaded corpus contains 14,180,757 distinct serials and source records through **July 6, 2026**. Candidate names never left the workspace during this comparison.",
        ">",
        "> **Matching:** Exact normalized identity ignores case, spacing, punctuation, apostrophes, and diacritics. Names 5-18 compact characters long also received a one-character insertion, deletion, substitution, or adjacent-transposition pass. Live/dead labels come from the corpus's USPTO status-code lookup. Active international classes come from class rows coded `6` (active). Relevant classes used here: **003, 005, 010, 021, 035, 044**.",
        "",
        "## Summary",
        "",
        f"- Candidates screened: **{len(results):,}**",
        f"- Search keys evaluated locally: **{key_count:,}**",
        f"- Matched federal case records retained: **{len(hits):,}**",
    ]
    for decision in decision_order:
        lines.append(f"- {decision}: **{counts.get(decision, 0):,}**")

    top_passes = (
        results[results["decision"] == "PROVISIONAL PASS"]
        .sort_values(
            ["score", "wave", "wave_number"], ascending=[False, True, True]
        )
        .head(25)
    )
    lines.extend(
        [
            "",
            "## Highest-rated provisional passes",
            "",
            "These are the strongest creative scores among names with no issue under this narrow mechanical rule. They are **not cleared names**.",
            "",
            "| Name | Score | Wave | # |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in top_passes.itertuples(index=False):
        lines.append(
            f"| {markdown_escape(row.name)} | {row.score:.1f} | {row.wave} | {row.wave_number} |"
        )

    lines.extend(
        [
            "",
            "### How to use the decisions",
            "",
            "- **RED:** Remove from the working pool unless counsel sees a compelling reason not to; this is an exact live hit in an active core/adjacent class.",
            "- **AMBER:** Do not advance without a closer manual review; the screen found either an exact live mark or a one-edit live relevant-class mark.",
            "- **YELLOW:** Keep only with caution. The hit is less direct, in another class, or dead at the federal level; dead registrations can still coexist with common-law use.",
            "- **PROVISIONAL PASS:** No issue under this narrow rule. It is not an availability finding.",
            "",
            "## Full 1,000-name register",
            "",
            "| Wave | # | Name | Creative score | Decision | Live exact | Live near-1 | Dead/unknown exact | Representative federal records |",
            "|---:|---:|---|---:|---|---:|---:|---:|---|",
        ]
    )
    for row in results.itertuples(index=False):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.wave),
                    str(row.wave_number),
                    markdown_escape(row.name),
                    f"{row.score:.1f}",
                    markdown_escape(row.decision),
                    str(row.live_exact_count),
                    str(row.live_near_count),
                    str(row.dead_or_unknown_exact_count),
                    markdown_escape(row.representative_hits),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Limits and next step",
            "",
            "This pass is intentionally conservative and mechanical. Before choosing a finalist, have U.S. trademark counsel run a full clearance search covering similar spellings/sounds/meanings, related goods and services, common-law use, state records, and marketplace evidence. Recheck live USPTO records immediately before filing because new applications arrive continuously.",
            "",
        ]
    )
    OUTPUT_REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    required = CASE_FILES + [CLASSIFICATION_FILE, INTL_CLASS_FILE, STATUS_FILE]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing local corpus files: " + ", ".join(missing))

    candidates = read_candidates()
    search_keys = build_search_keys(candidates)
    status_lookup = load_status_lookup()
    hits = query_hits(candidates, search_keys, status_lookup)
    results = build_results(candidates, hits)

    results.to_csv(OUTPUT_RESULTS, index=False, encoding="utf-8-sig")
    hits.to_csv(OUTPUT_HITS, index=False, encoding="utf-8-sig")
    write_report(results, hits, len(search_keys))

    summary = {
        "candidate_count": int(len(results)),
        "search_key_count": int(len(search_keys)),
        "matched_case_record_count": int(len(hits)),
        "decision_counts": {
            key: int(value)
            for key, value in results["decision"].value_counts().to_dict().items()
        },
        "corpus_distinct_serials": 14_180_757,
        "corpus_latest_source_date": "2026-07-06",
        "relevant_classes": sorted(RELEVANT_CLASSES),
        "outputs": {
            "report": str(OUTPUT_REPORT),
            "results_csv": str(OUTPUT_RESULTS),
            "hits_csv": str(OUTPUT_HITS),
        },
    }
    OUTPUT_SUMMARY.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
