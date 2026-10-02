from __future__ import annotations

import csv
import importlib.util
import json
import re
import sys
import unicodedata
from pathlib import Path

import pandas as pd


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
SCREEN_PATH = NAMING_DIR / "workbench-wave34" / "screen-uspto-local.py"
DUCKDB_VENDOR = Path(r"C:\tmp\duckdb_vendor")
INPUTS = [
    HERE / "cycle2-semantic-hinges-96.csv",
    HERE / "cycle2-expansion-40.csv",
    HERE / "cycle2-final-focus-12.csv",
]
RESULTS = HERE / "cycle2-federal-screen.csv"
HITS = HERE / "cycle2-federal-hits.csv"
SUMMARY = HERE / "cycle2-federal-summary.json"


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.lower())


def load_screen_module():
    sys.path.insert(0, str(DUCKDB_VENDOR))
    spec = importlib.util.spec_from_file_location("cycle2_local_tm_screen", SCREEN_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SCREEN_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    rows: list[dict[str, str]] = []
    for input_path in INPUTS:
        with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows.extend(csv.DictReader(handle))

    normalized = [normalize(row["name"]) for row in rows]
    duplicates = sorted({item for item in normalized if normalized.count(item) > 1})
    if duplicates:
        raise ValueError(f"Normalized duplicates: {duplicates}")

    candidates = pd.DataFrame(
        {
            "candidate_id": range(len(rows)),
            "wave": [2] * len(rows),
            "wave_number": range(1, len(rows) + 1),
            "name": [row["name"] for row in rows],
            "score": [0.0] * len(rows),
            "norm": normalized,
        }
    )

    screen = load_screen_module()
    search_keys = screen.build_search_keys(candidates)
    status_lookup = screen.load_status_lookup()
    hits = screen.query_hits(candidates, search_keys, status_lookup)
    results = screen.build_results(candidates, hits)

    lane_by_name = {row["name"]: row["lane"] for row in rows}
    results.insert(1, "lane", results["name"].map(lane_by_name))
    results.to_csv(RESULTS, index=False, encoding="utf-8-sig")
    hits.to_csv(HITS, index=False, encoding="utf-8-sig")

    summary = {
        "candidate_count": len(candidates),
        "search_key_count": len(search_keys),
        "matched_case_record_count": len(hits),
        "decision_counts": {
            key: int(value)
            for key, value in results["decision"].value_counts().to_dict().items()
        },
        "corpus_latest_source_date": "2026-07-06",
        "relevant_classes": sorted(screen.RELEVANT_CLASSES),
        "scope": "Normalized exact plus edit-distance-one U.S. federal knockout only",
    }
    SUMMARY.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
