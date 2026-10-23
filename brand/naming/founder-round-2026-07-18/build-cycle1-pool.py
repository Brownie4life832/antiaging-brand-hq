from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
MASTER = NAMING_DIR / "master-cohesive-rating-2026-07-16" / "MASTER-13271-RATED.csv"
LABS = {
    "A — category idea with voltage": HERE / "cycle1-lab-a-category-voltage.txt",
    "B — legible invention": HERE / "cycle1-lab-b-legible-invention.txt",
    "C — charged familiar metaphor": HERE / "cycle1-lab-c-charged-metaphor.txt",
}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]", "", value.lower())


def read_names(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    raw_rows: list[dict[str, object]] = []
    occurrence_map: dict[str, list[dict[str, object]]] = defaultdict(list)

    for approach, path in LABS.items():
        for lab_order, name in enumerate(read_names(path), start=1):
            row = {
                "approach": approach,
                "lab_order": lab_order,
                "name": name,
                "normalized": normalize(name),
            }
            raw_rows.append(row)
            occurrence_map[str(row["normalized"])].append(row)

    unique_rows: list[dict[str, object]] = []
    duplicate_rows: list[dict[str, object]] = []
    for row in raw_rows:
        norm = str(row["normalized"])
        occurrences = occurrence_map[norm]
        if row is occurrences[0]:
            unique_rows.append(
                {
                    **row,
                    "new_pool_occurrences": len(occurrences),
                    "all_approaches": " | ".join(
                        dict.fromkeys(str(item["approach"]) for item in occurrences)
                    ),
                }
            )
        else:
            duplicate_rows.append(
                {
                    **row,
                    "first_approach": occurrences[0]["approach"],
                    "first_name": occurrences[0]["name"],
                }
            )

    with MASTER.open("r", encoding="utf-8-sig", newline="") as handle:
        master_rows = list(csv.DictReader(handle))
    historical = {row["normalized"]: row for row in master_rows}

    history_rows: list[dict[str, object]] = []
    for row in unique_rows:
        old = historical.get(str(row["normalized"]))
        row["historical_repeat"] = "YES" if old else ""
        if old:
            history_rows.append(
                {
                    "name": row["name"],
                    "approach": row["approach"],
                    "historical_name": old["name"],
                    "historical_sources": old["sources"],
                    "historical_master_rank": old["master_rank"],
                }
            )

    def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    write_csv(
        HERE / "cycle1-pool.csv",
        unique_rows,
        [
            "approach",
            "lab_order",
            "name",
            "normalized",
            "new_pool_occurrences",
            "all_approaches",
            "historical_repeat",
        ],
    )
    write_csv(
        HERE / "cycle1-internal-duplicates.csv",
        duplicate_rows,
        ["approach", "lab_order", "name", "normalized", "first_approach", "first_name"],
    )
    write_csv(
        HERE / "cycle1-history-matches.csv",
        history_rows,
        ["name", "approach", "historical_name", "historical_sources", "historical_master_rank"],
    )

    summary = {
        "raw_count": len(raw_rows),
        "unique_normalized_count": len(unique_rows),
        "internal_duplicate_rows": len(duplicate_rows),
        "historical_repeat_count": len(history_rows),
        "approach_raw_counts": {
            approach: len(read_names(path)) for approach, path in LABS.items()
        },
    }
    (HERE / "cycle1-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
