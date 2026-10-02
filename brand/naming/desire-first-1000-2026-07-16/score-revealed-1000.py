from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE / "blind-1000.csv"
OUTPUT = HERE / "scored-1000.csv"

DIRECTION_DESIRE = {
    "The Invented House": 8.5,
    "The Pure Sound Lab": 8.2,
    "The Beautiful Object": 8.0,
    "The Magnetic Character": 7.7,
    "The Private World": 8.0,
    "The Cultural Mononym": 8.2,
    "Beautiful Mischief": 7.9,
    "Sensory Motion": 7.9,
    "Technical Elegance": 7.4,
    "Deep Time": 7.8,
}

COINED_METHODS = {
    "Eponym / curated mononym",
    "Morpheme engine",
    "World-language-shaped coinage",
    "Sound-first curated coinage",
    "Sound-first coinage",
    "Structural symmetry",
    "Deconstruct / reconstruct",
    "Invented place name",
    "Movement reconstruction",
    "Technical morpheme engine",
}

NEGATIVE_TOKENS = {
    "casket": 1.8, "wrong": 0.8, "disorder": 0.7, "vice": 0.5, "riot": 0.4,
    "trouble": 0.35, "scandal": 0.4, "alibi": 0.35, "excuse": 0.4,
    "vanity": 0.3, "elder": 0.45, "old": 0.8, "noise": 0.35,
}
GENERIC_WORDS = {
    "frame", "mirror", "vessel", "token", "album", "letter", "screen", "lens", "prism",
    "author", "citizen", "natural", "realist", "editor", "mentor", "friend", "expert",
    "house", "room", "studio", "gallery", "salon", "phase", "lumen", "axis", "vector",
    "record", "return", "duration", "interval", "sequence", "legacy", "heirloom",
}
CAMPAIGN_STARTS = {
    "the", "your", "good", "fine", "dear", "more", "not", "no", "why", "what", "by",
}


def clamp(value: float, low: float = 5.0, high: float = 9.7) -> float:
    return max(low, min(high, value))


def read_rows() -> list[dict[str, str]]:
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def pronunciation_penalty(name: str, method: str) -> float:
    norm = re.sub(r"[^a-z]", "", name.lower())
    value = 0.0
    if re.search(r"[bcdfghjklmnpqrstvwxyz]{3}", norm):
        value += 0.8
    if re.search(r"(oror|onon|inin|elel|enen|erer|rnr|vlr|vrn)", norm):
        value += 0.8
    if method in COINED_METHODS and len(norm) > 9:
        value += (len(norm) - 9) * 0.18
    if norm.endswith(("elal", "oral", "onel", "inor")):
        value += 0.5
    return value


def semantic_penalty(name: str) -> float:
    words = {re.sub(r"[^a-z]", "", word.lower()) for word in name.split()}
    return sum(penalty for word, penalty in NEGATIVE_TOKENS.items() if word in words)


def score_row(row: dict[str, str]) -> dict[str, object]:
    name = row["Name"]
    method = row["Method"]
    direction = row["Direction"]
    words = name.split()
    norm = row["Normalized"]
    structural = float(row["StructuralScore"])

    desire = DIRECTION_DESIRE[direction]
    distinctiveness = 8.7 if method in COINED_METHODS else 7.5
    if method in {"Far-field real-word raid", "Audacity / proposition", "Contradictory compound"}:
        distinctiveness += 0.5
    if len(words) == 1 and norm not in GENERIC_WORDS:
        distinctiveness += 0.35

    fluency = clamp(6.4 + (structural - 6.0) * 0.37, 5.5, 9.4)
    fluency -= pronunciation_penalty(name, method)

    stretch = 8.7 if len(words) == 1 else 7.8
    if len(words) == 3:
        stretch -= 1.0
    if direction in {"The Invented House", "The Pure Sound Lab", "The Cultural Mononym"}:
        stretch += 0.35
    if method in {"Character proposition", "Audacity / proposition"} and len(words) > 2:
        stretch -= 0.7

    bottle = 8.8 if len(words) == 1 and 5 <= len(norm) <= 9 else 7.8
    if len(words) == 2 and len(norm) <= 15:
        bottle += 0.45
    if len(norm) > 18:
        bottle -= 1.0
    if name.lower().split()[0] in CAMPAIGN_STARTS and len(words) > 1:
        bottle -= 0.35

    story = {
        "The Invented House": 8.5,
        "The Pure Sound Lab": 7.9,
        "The Beautiful Object": 8.2,
        "The Magnetic Character": 8.0,
        "The Private World": 8.1,
        "The Cultural Mononym": 8.2,
        "Beautiful Mischief": 8.3,
        "Sensory Motion": 7.9,
        "Technical Elegance": 7.7,
        "Deep Time": 8.0,
    }[direction]

    penalty = semantic_penalty(name)
    if name.lower() in GENERIC_WORDS:
        penalty += 0.65
    if method == "Technical morpheme engine":
        penalty += 0.35
    if method == "Morpheme engine" and pronunciation_penalty(name, method) > 0:
        penalty += 0.25

    creative = (
        desire * 0.22
        + distinctiveness * 0.20
        + fluency * 0.17
        + stretch * 0.16
        + bottle * 0.15
        + story * 0.10
        - penalty
    )
    creative = round(clamp(creative, 5.0, 9.6), 1)

    if method in COINED_METHODS:
        risk = "Pronunciation / invented word"
    elif name.lower() in GENERIC_WORDS or (len(words) == 1 and distinctiveness < 8.0):
        risk = "Generic real word"
    elif len(words) >= 3 or (words and words[0].lower() in CAMPAIGN_STARTS):
        risk = "Campaign-like"
    elif semantic_penalty(name):
        risk = "Negative semantic edge"
    else:
        risk = "Low creative risk"

    hook = {
        "The Invented House": f"{name} behaves like an established beauty house: desirable first and rigorous underneath.",
        "The Pure Sound Lab": f"{name} is a meaning-free verbal vessel that can accumulate authority, pleasure, and trust.",
        "The Beautiful Object": f"{name} makes the daily routine feel like owning and using a considered object.",
        "The Magnetic Character": f"{name} gives the brand a memorable social character: informed, self-possessed, and worth returning to.",
        "The Private World": f"{name} creates a private brand world where expertise feels intimate rather than clinical.",
        "The Cultural Mononym": f"{name} imports cultural texture into skincare without describing the category.",
        "Beautiful Mischief": f"{name} gives the brand enough wit and nerve to challenge beauty theater without becoming cynical.",
        "Sensory Motion": f"{name} makes performance feel tactile, rhythmic, and alive before any product claim is made.",
        "Technical Elegance": f"{name} borrows precision and discipline while keeping the brand desirable and human.",
        "Deep Time": f"{name} frames continued existence as accumulation and character rather than decline.",
    }[direction]

    review = "ADVANCE" if creative >= 8.2 else "HOLD" if creative >= 7.7 else "CUT"
    return {
        **row,
        "Desire": f"{clamp(desire - penalty * 0.25):.1f}",
        "Distinctiveness": f"{clamp(distinctiveness - penalty * 0.10):.1f}",
        "Fluency": f"{clamp(fluency):.1f}",
        "Stretch": f"{clamp(stretch):.1f}",
        "BottlePresence": f"{clamp(bottle):.1f}",
        "StoryIgnition": f"{clamp(story - penalty * 0.15):.1f}",
        "CreativeScore": f"{creative:.1f}",
        "RevealDecision": review,
        "Hook": hook,
        "CreativeRisk": risk,
    }


def main() -> None:
    rows = [score_row(row) for row in read_rows()]
    fields = list(rows[0])
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "candidate_count": len(rows),
        "reveal_decisions": dict(Counter(str(row["RevealDecision"]) for row in rows)),
        "score_counts": dict(Counter(str(row["CreativeScore"]) for row in rows)),
        "direction_average_scores": {
            direction: round(
                sum(float(row["CreativeScore"]) for row in rows if row["Direction"] == direction)
                / sum(row["Direction"] == direction for row in rows),
                2,
            )
            for direction in DIRECTION_DESIRE
        },
    }
    (HERE / "reveal-score-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
