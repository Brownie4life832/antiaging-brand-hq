from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE / "screened-1000.csv"
TOP200 = HERE / "top-200-non-red.csv"
TOP100 = HERE / "top-100-marketplace-input.csv"

SCREEN_POINTS = {
    "PROVISIONAL PASS": 2.8,
    "YELLOW - DEAD EXACT": 1.9,
    "YELLOW - LIVE NEAR": 1.5,
    "AMBER - LIVE EXACT": 0.75,
    "AMBER - LIVE NEAR / RELEVANT": 0.35,
}

UGLY_CHUNKS = (
    "datum", "toler", "phaseor", "phasein", "glue", "gloaz", "gliot", "doad",
    "workwork", "markmark", "kindkind", "elal", "oror", "onon", "inin",
)
DERIVATIVE_ENDINGS = ("made", "wise", "work", "mark", "kind", "form", "house")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def curation_score(row: dict[str, str]) -> float:
    name = row["Name"]
    norm = row["Normalized"]
    value = float(row["CreativeScore"]) + SCREEN_POINTS[row["TrademarkDecision"]]
    if row["RevealDecision"] == "ADVANCE":
        value += 0.5
    if len(name.split()) == 1:
        value += 0.4
    if row["Direction"] in {"The Invented House", "The Pure Sound Lab", "The Cultural Mononym"}:
        value += 0.3
    if any(chunk in norm for chunk in UGLY_CHUNKS):
        value -= 2.5
    if norm.endswith(DERIVATIVE_ENDINGS):
        value -= 0.85
    if row["Method"] in {"Technical morpheme engine", "Archetypal compound"}:
        value -= 0.55
    if len(name.split()) >= 3:
        value -= 0.8
    return round(value, 4)


def family_keys(name: str) -> tuple[str, ...]:
    norm = re.sub(r"[^a-z]", "", name.lower())
    words = name.lower().split()
    if len(words) == 1:
        return (f"start:{norm[:3]}", f"end:{norm[-3:]}")
    return (f"first:{words[0]}", f"last:{words[-1]}")


def main() -> None:
    rows = read_csv(INPUT)
    by_name = {row["Name"]: row for row in rows}
    champion_names = [
        line.strip()
        for line in (HERE / "champion-seeds.txt").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if len(champion_names) != 100 or len(set(champion_names)) != 100:
        raise ValueError("Champion seed file must contain exactly 100 unique names")
    for name in champion_names:
        if name not in by_name:
            raise ValueError(f"Champion is outside the 1,000-name pool: {name}")
        if by_name[name]["TrademarkDecision"].startswith("RED"):
            raise ValueError(f"Champion has red screen decision: {name}")

    top100_rows = []
    for rank, name in enumerate(champion_names, start=1):
        top100_rows.append({"ChampionSeedOrder": rank, **by_name[name]})

    non_red = [row for row in rows if not row["TrademarkDecision"].startswith("RED")]
    ordered = sorted(non_red, key=lambda row: (-curation_score(row), int(row["PoolNumber"])))
    selected = [by_name[name] for name in champion_names]
    selected_names = set(champion_names)
    family_counts: Counter = Counter()
    direction_counts: Counter = Counter(row["Direction"] for row in selected)
    for row in selected:
        for key in family_keys(row["Name"]):
            family_counts[key] += 1

    for family_limit in (9, 15, 10_000):
        for row in ordered:
            if len(selected) >= 200:
                break
            if row["Name"] in selected_names:
                continue
            keys = family_keys(row["Name"])
            if any(family_counts[key] >= family_limit for key in keys):
                continue
            if direction_counts[row["Direction"]] >= 45:
                continue
            selected.append(row)
            selected_names.add(row["Name"])
            for key in keys:
                family_counts[key] += 1
            direction_counts[row["Direction"]] += 1
        if len(selected) >= 200:
            break
    if len(selected) != 200:
        raise ValueError(f"Top 200 contains {len(selected)} rows")

    selected.sort(
        key=lambda row: (
            0 if row["Name"] in champion_names else 1,
            champion_names.index(row["Name"]) if row["Name"] in champion_names else 10_000,
            -curation_score(row),
        )
    )
    top200_rows = [
        {"Top200Rank": rank, "CurationScore": f"{curation_score(row):.4f}", **row}
        for rank, row in enumerate(selected, start=1)
    ]

    for path, output_rows in ((TOP100, top100_rows), (TOP200, top200_rows)):
        fields = list(output_rows[0])
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(output_rows)

    summary = {
        "top100_count": len(top100_rows),
        "top200_count": len(top200_rows),
        "top100_direction_counts": dict(Counter(row["Direction"] for row in top100_rows)),
        "top100_decision_counts": dict(Counter(row["TrademarkDecision"] for row in top100_rows)),
        "top200_direction_counts": dict(Counter(row["Direction"] for row in top200_rows)),
        "top200_decision_counts": dict(Counter(row["TrademarkDecision"] for row in top200_rows)),
    }
    (HERE / "curation-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
