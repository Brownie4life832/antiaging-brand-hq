from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

import pandas as pd


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
SCREEN_MODULE = NAMING_DIR / "workbench-wave34" / "screen-uspto-local.py"
INPUT = HERE / "reviewed-pool.csv"
OUTPUT = HERE / "reviewed-pool-screen.csv"
HITS_OUTPUT = HERE / "reviewed-pool-screen-hits.csv"
SUMMARY_OUTPUT = HERE / "reviewed-pool-screen-summary.json"


def load_screen_module():
    spec = importlib.util.spec_from_file_location("uspto_screen", SCREEN_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SCREEN_MODULE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    screen = load_screen_module()
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    if not source_rows:
        raise ValueError("Reviewed pool is empty")

    candidate_rows = []
    for index, row in enumerate(source_rows):
        candidate_rows.append(
            {
                "candidate_id": index,
                "wave": 5,
                "wave_number": index + 1,
                "name": row["Name"],
                "score": float(row["Score"]),
                "norm": screen.normalize_name(row["Name"]),
            }
        )
    candidates = pd.DataFrame(candidate_rows)
    if candidates["norm"].duplicated().any():
        raise ValueError("Normalized duplicates found in reviewed pool")

    search_keys = screen.build_search_keys(candidates)
    status_lookup = screen.load_status_lookup()
    hits = screen.query_hits(candidates, search_keys, status_lookup)
    results = screen.build_results(candidates, hits)

    by_name = {row["Name"]: row for row in source_rows}
    enriched_rows = []
    for row in results.to_dict(orient="records"):
        source = by_name[row["name"]]
        enriched_rows.append(
            {
                "Name": row["name"],
                "Score": f"{float(row['score']):.1f}",
                "World": source["World"],
                "Hook": source["Hook"],
                "Risk": source["Risk"],
                "Method": source["Method"],
                "DecoyBrief": source["DecoyBrief"],
                "SourceFile": source["SourceFile"],
                "Reviewer": source["Reviewer"],
                "Decision": row["decision"],
                "DecisionReason": row["reason"],
                "LiveExact": int(row["live_exact_count"]),
                "LiveNear1": int(row["live_near_count"]),
                "DeadOrUnknownExact": int(row["dead_or_unknown_exact_count"]),
                "AllHitCount": int(row["all_hit_count"]),
                "RepresentativeHits": row["representative_hits"],
                "Normalized": screen.normalize_name(row["name"]),
            }
        )

    output_fields = list(enriched_rows[0])
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields)
        writer.writeheader()
        writer.writerows(enriched_rows)
    hits.to_csv(HITS_OUTPUT, index=False, encoding="utf-8-sig")

    counts = results["decision"].value_counts().to_dict()
    summary = {
        "candidate_count": len(enriched_rows),
        "search_key_count": len(search_keys),
        "matched_case_record_count": len(hits),
        "decision_counts": {key: int(value) for key, value in counts.items()},
        "corpus_distinct_serials": 14_180_757,
        "corpus_latest_source_date": "2026-07-06",
        "relevant_classes": sorted(screen.RELEVANT_CLASSES),
    }
    SUMMARY_OUTPUT.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
