from __future__ import annotations

import csv
import importlib.util
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
HISTORY_HELPER = NAMING_DIR / "decoy-exercise-2026-07-16" / "build-decoy-pool.py"
RAW = HERE / "raw-pool.csv"
OUTPUT = HERE / "blind-1000.csv"
REJECTIONS = HERE / "blind-pool-rejections.csv"

ALLOCATIONS = {
    "The Invented House": 160,
    "The Pure Sound Lab": 160,
    "The Beautiful Object": 110,
    "The Magnetic Character": 100,
    "The Private World": 90,
    "The Cultural Mononym": 100,
    "Beautiful Mischief": 90,
    "Sensory Motion": 80,
    "Technical Elegance": 60,
    "Deep Time": 50,
}

METHOD_BASE = {
    "Eponym / curated mononym": 9.0,
    "Morpheme engine": 6.4,
    "World-language-shaped coinage": 6.2,
    "Sound-first curated coinage": 9.0,
    "Sound-first coinage": 6.8,
    "Structural symmetry": 6.6,
    "Deconstruct / reconstruct": 6.5,
    "Real-word object metaphor": 7.3,
    "Compound 1+1=3": 6.8,
    "Real-word eponym": 7.0,
    "Archetypal compound": 6.4,
    "Character proposition": 6.5,
    "Real-word place metaphor": 7.0,
    "Place compound": 6.7,
    "Invented place name": 7.1,
    "Far-field real-word raid": 7.5,
    "Contradictory compound": 7.0,
    "Audacity / proposition": 7.4,
    "Action and sensory metaphor": 7.0,
    "Movement reconstruction": 6.4,
    "Sensory compound": 6.7,
    "Technical source raid": 6.8,
    "Technical morpheme engine": 6.1,
    "Deep-time metaphor and future reframe": 6.9,
}

BLOCKED_WORDS = {
    "skin", "skincare", "age", "aging", "anti", "proof", "truth", "science", "lab",
    "formula", "clinical", "derm", "clear", "open", "standard", "method", "confidence",
    "glow", "soft", "silk", "flow", "renew", "timeless", "forever", "longevity",
}
BLOCKED_SUBSTRINGS = ("skincare", "antiaging", "pharma", "derma", "biohack")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_history() -> tuple[dict[str, str], dict[str, int]]:
    spec = importlib.util.spec_from_file_location("history_helper", HISTORY_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {HISTORY_HELPER}")
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    helper.EXCLUDED_HISTORY_PARTS.add(HERE.name.lower())
    history, source_counts = helper.build_historical_index()

    # The earlier blind workbench was intentionally excluded by its own helper.
    # Add every explicit Name column from that package because the user received
    # a link to the broader pool and may have inspected it.
    old_decoy = NAMING_DIR / "decoy-exercise-2026-07-16"
    for path in old_decoy.glob("*.csv"):
        try:
            for row in read_csv(path):
                name = (row.get("Name") or row.get("name") or "").strip()
                norm = helper.normalize(name)
                if norm and norm not in history:
                    history[norm] = f"{path.relative_to(NAMING_DIR).as_posix()} :: {name}"
        except (UnicodeDecodeError, csv.Error):
            continue

    seen_path = HERE / "seen-in-conversation.txt"
    for name in seen_path.read_text(encoding="utf-8").splitlines():
        name = name.strip()
        norm = helper.normalize(name)
        if norm:
            history[norm] = f"conversation probe :: {name}"
    return history, dict(source_counts)


def gate_reason(row: dict[str, str], history: dict[str, str]) -> str | None:
    name = row["Name"].strip()
    norm = row["Normalized"]
    if norm in history:
        return "historical exact"
    words = {re.sub(r"[^a-z]", "", word.lower()) for word in name.split()}
    if words & BLOCKED_WORDS:
        return "prohibited category/cliche word"
    if any(value in norm for value in BLOCKED_SUBSTRINGS):
        return "prohibited category substring"
    if re.search(r"[^A-Za-zÀ-ÿ' -]", name):
        return "unsupported orthography"
    if re.search(r"[bcdfghjklmnpqrstvwxyz]{4,}", norm):
        return "four-consonant cluster"
    if re.search(r"([a-z])\1\1", norm):
        return "triple repeated letter"
    return None


def structural_score(row: dict[str, str]) -> float:
    name = row["Name"]
    norm = row["Normalized"]
    words = name.split()
    method = row["Method"]
    direction = row["Direction"]
    score = METHOD_BASE.get(method, 6.0)

    if len(words) == 1:
        score += 1.0
    elif len(words) == 2:
        score += 0.35
    else:
        score -= 0.8

    ideal = 7 if len(words) == 1 else 13
    score += max(-1.5, 1.5 - abs(len(norm) - ideal) * 0.22)

    vowels = sum(char in "aeiouy" for char in norm)
    ratio = vowels / max(1, len(norm))
    score += max(-1.2, 1.1 - abs(ratio - 0.42) * 8)
    if re.search(r"[bcdfghjklmnpqrstvwxyz]{3}", norm):
        score -= 0.8
    if re.search(r"(ae|eo|io|oa|ue)", norm):
        score += 0.15
    if norm.endswith(("ium", "ica", "ara", "oria", "avia")):
        score -= 1.0
    if norm.endswith(("en", "el", "in", "on", "or", "ren")):
        score += 0.35
    if any(chunk in norm for chunk in ("anal", "oral", "ova", "dick", "arse", "sore", "ill", "sick", "die")):
        score -= 2.0
    if any(chunk in norm for chunk in ("elle", "ella", "ora", "ara")) and direction in {
        "The Invented House", "The Pure Sound Lab"
    }:
        score -= 0.5

    if direction == "The Invented House" and method == "Eponym / curated mononym":
        score += 1.5
    if direction == "The Pure Sound Lab" and method == "Sound-first curated coinage":
        score += 1.5
    if direction == "The Cultural Mononym" and len(words) == 1 and 5 <= len(norm) <= 11:
        score += 1.0
    if direction == "Beautiful Mischief" and method == "Audacity / proposition" and len(words) <= 2:
        score += 0.7
    if direction == "The Beautiful Object" and method == "Real-word object metaphor":
        score += 0.6
    if direction == "The Private World" and method == "Invented place name":
        score += 0.7
    return round(score, 5)


def family_keys(row: dict[str, str]) -> tuple[str, ...]:
    norm = row["Normalized"]
    words = row["Name"].lower().split()
    if len(words) == 1:
        return (f"start:{norm[:3]}", f"end:{norm[-3:]}")
    return (f"first:{words[0]}", f"last:{words[-1]}")


def select_direction(rows: list[dict[str, str]], target: int) -> list[dict[str, str]]:
    ordered = sorted(rows, key=lambda row: (-float(row["StructuralScore"]), int(row["RawOrder"])))
    selected: list[dict[str, str]] = []
    selected_norms: set[str] = set()
    family_counts: Counter = Counter()
    method_counts: Counter = Counter()

    for family_limit, method_limit in ((8, math.ceil(target * 0.58)), (14, target), (10_000, target)):
        for row in ordered:
            if len(selected) >= target:
                break
            norm = row["Normalized"]
            if norm in selected_norms:
                continue
            keys = family_keys(row)
            if any(family_counts[key] >= family_limit for key in keys):
                continue
            if method_counts[row["Method"]] >= method_limit:
                continue
            selected.append(row)
            selected_norms.add(norm)
            for key in keys:
                family_counts[key] += 1
            method_counts[row["Method"]] += 1
        if len(selected) >= target:
            break
    if len(selected) != target:
        raise ValueError(f"Could select only {len(selected)} of {target}")
    return selected


def main() -> None:
    history, history_source_counts = load_history()
    raw = read_csv(RAW)
    gated_by_direction: dict[str, list[dict[str, str]]] = defaultdict(list)
    rejections: list[dict[str, str]] = []
    for row in raw:
        reason = gate_reason(row, history)
        if reason:
            rejections.append({**row, "RejectReason": reason, "Collision": history.get(row["Normalized"], "")})
            continue
        row["StructuralScore"] = f"{structural_score(row):.5f}"
        gated_by_direction[row["Direction"]].append(row)

    selected: list[dict[str, str]] = []
    for direction, target in ALLOCATIONS.items():
        available = gated_by_direction.get(direction, [])
        if len(available) < target:
            raise ValueError(f"{direction}: only {len(available)} gated candidates for target {target}")
        chosen = select_direction(available, target)
        for row in chosen:
            row["DirectionRank"] = str(len([x for x in selected if x["Direction"] == direction]) + 1)
        selected.extend(chosen)

    if len(selected) != 1000 or len({row["Normalized"] for row in selected}) != 1000:
        raise ValueError("Final blind pool is not exactly 1,000 normalized-unique names")

    output_fields = [
        "PoolNumber", "Name", "Direction", "DirectionRank", "Method", "SourceWorld",
        "RawOrder", "StructuralScore", "Normalized",
    ]
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields, extrasaction="ignore")
        writer.writeheader()
        for number, row in enumerate(selected, start=1):
            writer.writerow({"PoolNumber": number, **row})

    rejection_fields = list(raw[0]) + ["RejectReason", "Collision"]
    with REJECTIONS.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rejection_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rejections)

    summary = {
        "raw_unique_count": len(raw),
        "historical_index_count": len(history),
        "gated_count": sum(len(value) for value in gated_by_direction.values()),
        "rejection_count": len(rejections),
        "rejection_reasons": dict(Counter(row["RejectReason"] for row in rejections)),
        "available_by_direction": {key: len(value) for key, value in gated_by_direction.items()},
        "selected_count": len(selected),
        "selected_by_direction": dict(Counter(row["Direction"] for row in selected)),
        "selected_by_method": dict(Counter(row["Method"] for row in selected)),
        "largest_historical_sources": sorted(history_source_counts.items(), key=lambda item: item[1], reverse=True)[:15],
    }
    (HERE / "blind-pool-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
