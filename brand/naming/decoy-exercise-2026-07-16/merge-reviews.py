from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
WORLDS = {
    "Earned Confidence",
    "The Long View",
    "The Living Standard",
    "Beauty for Skeptics",
    "On Your Terms",
    "Performance Without Theater",
}


def normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_text = "".join(
        char for char in decomposed if not unicodedata.combining(char)
    ).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", "", ascii_text.lower())


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    merged: list[dict[str, object]] = []
    seen: set[str] = set()
    for label in ("a", "b", "c"):
        chunk_path = HERE / f"review-chunk-{label}.csv"
        review_path = HERE / f"review-{label}.csv"
        chunk = {normalize(row["Name"]): row for row in read_csv(chunk_path)}
        review = read_csv(review_path)
        if not 80 <= len(review) <= 180:
            raise ValueError(f"Expected 80-180 retained rows in {review_path.name}; found {len(review)}")
        local_seen: set[str] = set()
        for row in review:
            name = row.get("Name", "").strip()
            norm = normalize(name)
            if norm not in chunk:
                raise ValueError(f"Review {label} contains name outside its chunk: {name}")
            if norm in local_seen or norm in seen:
                raise ValueError(f"Duplicate reviewed name: {name}")
            local_seen.add(norm)
            seen.add(norm)
            try:
                score = round(float(row.get("Score", "")), 1)
            except ValueError as exc:
                raise ValueError(f"Invalid score for {name}: {row.get('Score')}") from exc
            if not 8.0 <= score <= 10.0:
                raise ValueError(f"Out-of-range score for {name}: {score}")
            world = row.get("World", "").strip()
            if world not in WORLDS:
                raise ValueError(f"Invalid world for {name}: {world}")
            source = chunk[norm]
            merged.append(
                {
                    "Name": source["Name"],
                    "Score": f"{score:.1f}",
                    "World": world,
                    "Hook": row.get("Hook", "").strip(),
                    "Risk": row.get("Risk", "").strip(),
                    "Method": source["Method"],
                    "DecoyBrief": source["DecoyBrief"],
                    "SourceFile": source["SourceFile"],
                    "Normalized": norm,
                    "Reviewer": label.upper(),
                }
            )

    merged.sort(key=lambda row: (-float(row["Score"]), str(row["Name"]).lower()))
    fields = [
        "Name",
        "Score",
        "World",
        "Hook",
        "Risk",
        "Method",
        "DecoyBrief",
        "SourceFile",
        "Normalized",
        "Reviewer",
    ]
    write_csv(HERE / "reviewed-pool.csv", merged, fields)
    summary = {
        "reviewed_survivors": len(merged),
        "reviewer_counts": dict(Counter(str(row["Reviewer"]) for row in merged)),
        "world_counts": dict(Counter(str(row["World"]) for row in merged)),
        "decoy_counts": dict(Counter(str(row["DecoyBrief"]) for row in merged)),
        "method_counts": dict(Counter(str(row["Method"]) for row in merged)),
        "score_counts": dict(Counter(str(row["Score"]) for row in merged)),
    }
    (HERE / "review-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
