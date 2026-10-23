from __future__ import annotations

import csv
import importlib.util
import json
import sys
from pathlib import Path


VENDOR = Path(r"C:\tmp\duckdb_vendor")
if VENDOR.exists():
    sys.path.insert(0, str(VENDOR))

import pandas as pd


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
SCREEN_MODULE = NAMING_DIR / "workbench-wave34" / "screen-uspto-local.py"
INPUT = HERE / "top-500-rated.csv"
OUTPUT = HERE / "top-500-trademark-results.csv"
HITS_OUTPUT = HERE / "top-500-trademark-hits.csv"
SUMMARY_OUTPUT = HERE / "top-500-trademark-summary.json"


def load_screen_module():
    spec = importlib.util.spec_from_file_location("uspto_screen_round2", SCREEN_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SCREEN_MODULE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    screen = load_screen_module()
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    if len(source_rows) != 500:
        raise ValueError(f"Expected 500 source rows; found {len(source_rows)}")

    candidate_rows = []
    for index, row in enumerate(source_rows):
        candidate_rows.append(
            {
                "candidate_id": index,
                "wave": int(row["WorldRank"]),
                "wave_number": int(row["Top500Rank"]),
                "name": row["Name"],
                "score": float(row["CreativeRating"]),
                "norm": screen.normalize_name(row["Name"]),
            }
        )
    candidates = pd.DataFrame(candidate_rows)
    if candidates["norm"].duplicated().any():
        raise ValueError("Normalized duplicates found in top 500")

    search_keys = screen.build_search_keys(candidates)
    status_lookup = screen.load_status_lookup()
    hits = screen.query_hits(candidates, search_keys, status_lookup)
    results = screen.build_results(candidates, hits)

    by_name = {row["Name"]: row for row in source_rows}
    enriched = []
    for result in results.to_dict(orient="records"):
        source = by_name[result["name"]]
        enriched.append(
            {
                **source,
                "TrademarkDecision": result["decision"],
                "TrademarkReason": result["reason"],
                "LiveExact": int(result["live_exact_count"]),
                "LiveNear1": int(result["live_near_count"]),
                "DeadOrUnknownExact": int(result["dead_or_unknown_exact_count"]),
                "AllHitCount": int(result["all_hit_count"]),
                "RepresentativeHits": result["representative_hits"],
            }
        )

    fields = list(enriched[0])
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(enriched)
    hits.to_csv(HITS_OUTPUT, index=False, encoding="utf-8-sig")

    counts = results["decision"].value_counts().to_dict()
    summary = {
        "candidate_count": len(enriched),
        "search_key_count": len(search_keys),
        "matched_case_record_count": len(hits),
        "decision_counts": {key: int(value) for key, value in counts.items()},
        "corpus_distinct_serials": 14_180_757,
        "corpus_latest_source_date": "2026-07-06",
        "relevant_classes": sorted(screen.RELEVANT_CLASSES),
        "limits": "Exact normalized identity plus edit-distance-one for compact names; preliminary federal knockout only.",
    }
    SUMMARY_OUTPUT.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
