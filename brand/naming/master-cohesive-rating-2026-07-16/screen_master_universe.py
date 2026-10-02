from __future__ import annotations

import csv
import importlib.util
import json
import math
import sys
from pathlib import Path

import duckdb
import pandas as pd


HERE = Path(__file__).resolve().parent
NAMING = HERE.parent
SCREEN_PATH = NAMING / "workbench-wave34" / "screen-uspto-local.py"
INPUT = HERE / "master-universe.csv"
RESULTS = HERE / "master-federal-screen.csv"
HITS = HERE / "master-federal-hits.csv"
SUMMARY = HERE / "master-federal-summary.json"
CHUNK_SIZE = 500
CACHE_DB = Path(r"C:\tmp\uspto_tm_screen\normalized_marks_cache.duckdb")


def load_screen_module():
    spec = importlib.util.spec_from_file_location("master_local_tm_screen", SCREEN_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SCREEN_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def ensure_marks_cache(connection: duckdb.DuckDBPyConnection, screen) -> None:
    existing = connection.execute(
        """
        SELECT count(*)
        FROM information_schema.tables
        WHERE table_name = 'marks'
        """
    ).fetchone()[0]
    if existing:
        count = connection.execute("SELECT count(*) FROM marks").fetchone()[0]
        if count >= 14_000_000:
            print(f"using normalized mark cache: records={count}", flush=True)
            return
        connection.execute("DROP TABLE marks")

    status_lookup = screen.load_status_lookup()
    connection.register("status_frame", status_lookup)
    case_paths = ", ".join(f"'{path.as_posix()}'" for path in screen.CASE_FILES)
    print("building normalized 14.18M-record mark cache", flush=True)
    connection.execute(
        f"""
        CREATE TABLE marks AS
        SELECT
            cases.serial_no,
            cases.registration_no,
            cases.mark_id_char,
            cases.filing_dt,
            cases.status_cd,
            lower(
                regexp_replace(
                    strip_accents(cases.mark_id_char),
                    '[^A-Za-z0-9]',
                    '',
                    'g'
                )
            ) AS mark_norm,
            status.description AS status_description,
            status.live_dead_indicator,
            starts_with(status.live_dead_indicator, 'Live') AS is_live
        FROM read_parquet([{case_paths}]) AS cases
        LEFT JOIN status_frame AS status
            ON cases.status_cd = status.code
        WHERE cases.mark_id_char IS NOT NULL
        """
    )
    print("indexing normalized mark cache", flush=True)
    connection.execute("CREATE INDEX marks_norm_idx ON marks(mark_norm)")
    connection.execute("ANALYZE marks")
    connection.unregister("status_frame")
    count = connection.execute("SELECT count(*) FROM marks").fetchone()[0]
    print(f"normalized mark cache ready: records={count}", flush=True)


def query_chunk_cached(
    connection: duckdb.DuckDBPyConnection, search_keys: pd.DataFrame
) -> pd.DataFrame:
    connection.register("search_key_frame", search_keys)
    hits = connection.execute(
        """
        SELECT * EXCLUDE (preference)
        FROM (
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
                marks.status_description,
                marks.live_dead_indicator,
                marks.is_live,
                row_number() OVER (
                    PARTITION BY keys.candidate_id, marks.serial_no
                    ORDER BY keys.distance, keys.hit_type
                ) AS preference
            FROM marks
            INNER JOIN search_key_frame AS keys
                ON marks.mark_norm = keys.norm_key
            WHERE marks.mark_norm <> ''
        )
        WHERE preference = 1
        ORDER BY candidate_id, distance, is_live DESC, filing_dt DESC, serial_no
        """
    ).fetchdf()
    connection.unregister("search_key_frame")
    return hits


def attach_active_classes(
    connection: duckdb.DuckDBPyConnection,
    hits: pd.DataFrame,
    screen,
) -> pd.DataFrame:
    if hits.empty:
        hits["active_classes"] = ""
        hits["has_relevant_class"] = False
        return hits

    matched = hits[["serial_no"]].drop_duplicates()
    connection.register("matched_serial_frame", matched)
    relevant_sql = ", ".join(
        f"'{code}'" for code in sorted(screen.RELEVANT_CLASSES)
    )
    classes = connection.execute(
        f"""
        SELECT
            classification.serial_no,
            string_agg(
                DISTINCT intl.intl_class_cd,
                ',' ORDER BY intl.intl_class_cd
            ) AS active_classes,
            bool_or(intl.intl_class_cd IN ({relevant_sql})) AS has_relevant_class
        FROM read_parquet('{screen.CLASSIFICATION_FILE.as_posix()}') AS classification
        INNER JOIN matched_serial_frame AS matched
            ON classification.serial_no = matched.serial_no
        LEFT JOIN read_parquet('{screen.INTL_CLASS_FILE.as_posix()}') AS intl
            ON classification.serial_no = intl.serial_no
            AND classification.class_seq = intl.class_seq
        WHERE classification.class_status_cd = '6'
        GROUP BY classification.serial_no
        """
    ).fetchdf()
    connection.unregister("matched_serial_frame")
    merged = hits.merge(classes, how="left", on="serial_no")
    merged["active_classes"] = merged["active_classes"].fillna("")
    merged["has_relevant_class"] = merged["has_relevant_class"].fillna(False)
    return merged


def main() -> None:
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))

    candidates = pd.DataFrame(
        {
            "candidate_id": range(len(source_rows)),
            "wave": [1] * len(source_rows),
            "wave_number": range(1, len(source_rows) + 1),
            "name": [row["name"] for row in source_rows],
            "score": [0.0] * len(source_rows),
            "norm": [row["normalized"] for row in source_rows],
        }
    )

    screen = load_screen_module()
    connection = duckdb.connect(str(CACHE_DB))
    connection.execute("PRAGMA threads=4")
    ensure_marks_cache(connection, screen)
    result_frames: list[pd.DataFrame] = []
    hit_frames: list[pd.DataFrame] = []
    total_search_keys = 0
    chunk_count = math.ceil(len(candidates) / CHUNK_SIZE)

    for chunk_index, start in enumerate(range(0, len(candidates), CHUNK_SIZE), 1):
        chunk = candidates.iloc[start : start + CHUNK_SIZE].copy()
        search_keys = screen.build_search_keys(chunk)
        total_search_keys += len(search_keys)
        hits = query_chunk_cached(connection, search_keys)
        if not hits.empty:
            hit_frames.append(hits)
        print(
            f"chunk {chunk_index}/{chunk_count}: candidates={len(chunk)} "
            f"keys={len(search_keys)} hits={len(hits)}",
            flush=True,
        )

    all_hits = (
        pd.concat(hit_frames, ignore_index=True)
        if hit_frames
        else pd.DataFrame()
    )
    print("attaching active international classes", flush=True)
    all_hits = attach_active_classes(connection, all_hits, screen)
    connection.close()
    all_results = screen.build_results(candidates, all_hits)
    all_results.to_csv(RESULTS, index=False, encoding="utf-8-sig")
    all_hits.to_csv(HITS, index=False, encoding="utf-8-sig")

    summary = {
        "candidate_count": len(candidates),
        "chunk_size": CHUNK_SIZE,
        "chunk_count": chunk_count,
        "search_key_count": total_search_keys,
        "matched_case_record_count": len(all_hits),
        "decision_counts": {
            key: int(value)
            for key, value in all_results["decision"].value_counts().to_dict().items()
        },
        "corpus_distinct_serials": 14_180_757,
        "corpus_latest_source_date": "2026-07-06",
        "relevant_classes": sorted(screen.RELEVANT_CLASSES),
        "scope": "Normalized exact plus edit-distance-one U.S. federal knockout screen; preliminary and non-legal.",
    }
    SUMMARY.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
