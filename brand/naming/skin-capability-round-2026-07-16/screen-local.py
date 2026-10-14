from __future__ import annotations

import csv
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
SCREEN_HELPER = NAMING_DIR / "workbench-wave34" / "screen-uspto-local.py"
INPUT = HERE / "screening-slate.csv"
VENDOR = Path(r"C:\tmp\duckdb_vendor")


def load_helper():
    sys.path.insert(0, str(VENDOR))
    spec = importlib.util.spec_from_file_location("screen_helper", SCREEN_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SCREEN_HELPER}")
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper


def main() -> None:
    helper = load_helper()
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        source = list(csv.DictReader(handle))

    import pandas as pd

    candidates = pd.DataFrame(
        [
            {
                "candidate_id": index,
                "wave": row["World"],
                "wave_number": int(row["WorldRank"]),
                "name": row["Name"],
                "score": 0.0,
                "norm": helper.normalize_name(row["Name"]),
            }
            for index, row in enumerate(source)
        ]
    )
    if candidates["norm"].duplicated().any():
        raise ValueError("Normalized duplicate in screening slate")

    search_keys = helper.build_search_keys(candidates)
    status_lookup = helper.load_status_lookup()
    hits = helper.query_hits(candidates, search_keys, status_lookup)
    results = helper.build_results(candidates, hits)
    results.rename(columns={"wave": "world", "wave_number": "world_rank"}, inplace=True)
    results.to_csv(HERE / "local-federal-results.csv", index=False, encoding="utf-8-sig")
    hits.to_csv(HERE / "local-federal-hits.csv", index=False, encoding="utf-8-sig")

    summary = {
        "candidate_count": len(results),
        "search_key_count": len(search_keys),
        "matched_case_record_count": len(hits),
        "decision_counts": results["decision"].value_counts().to_dict(),
        "corpus_latest_source_date": "2026-07-06",
        "relevant_classes": sorted(helper.RELEVANT_CLASSES),
    }
    (HERE / "local-federal-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
