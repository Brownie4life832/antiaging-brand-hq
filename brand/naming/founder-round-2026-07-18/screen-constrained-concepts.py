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
RUN_PREFIX = sys.argv[1] if len(sys.argv) > 1 else "20-constrained-concept"
INPUT = HERE / f"{RUN_PREFIX}-slate.csv"
RESULTS = HERE / f"{RUN_PREFIX}-federal-screen.csv"
HITS = HERE / f"{RUN_PREFIX}-federal-hits.csv"
SUMMARY = HERE / f"{RUN_PREFIX}-federal-summary.json"


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.lower())


def load_screen_module():
    sys.path.insert(0, str(DUCKDB_VENDOR))
    spec = importlib.util.spec_from_file_location(
        "constrained_concept_local_tm_screen", SCREEN_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SCREEN_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    candidates = pd.DataFrame(
        {
            "candidate_id": range(len(rows)),
            "wave": [1] * len(rows),
            "wave_number": range(1, len(rows) + 1),
            "name": [row["name"] for row in rows],
            "score": [0.0] * len(rows),
            "norm": [normalize(row["name"]) for row in rows],
        }
    )

    screen = load_screen_module()
    search_keys = screen.build_search_keys(candidates)
    status_lookup = screen.load_status_lookup()
    hits = screen.query_hits(candidates, search_keys, status_lookup)
    results = screen.build_results(candidates, hits)

    mechanism_by_name = {row["name"]: row["mechanism"] for row in rows}
    results.insert(1, "mechanism", results["name"].map(mechanism_by_name))
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
