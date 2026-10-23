from __future__ import annotations

import bisect
import csv
import json
import math
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE / "master-universe.csv"
OUTPUT = HERE / "all-names-cohesive-ratings.csv"
ABOVE_EIGHT = HERE / "names-above-8.csv"
SUMMARY = HERE / "rating-summary.json"


DIRECT_TERMS = {
    "straight", "plain", "frank", "clear", "direct", "outright", "honest",
    "true", "actual", "real", "candid", "open", "known", "shown", "sure",
    "exact", "visible", "unhidden", "unredacted", "unabridged", "plainspoken",
}
EVIDENCE_TERMS = {
    "fact", "proof", "check", "claim", "source", "evidence", "reason",
    "standard", "measure", "account", "record", "ledger", "formula", "study",
    "tested", "test", "data", "math", "receipts", "rationale", "verified",
    "citation", "cited", "documented", "review", "examiner", "finding",
}
ACCOUNTABILITY_TERMS = {
    "stand", "back", "mean", "promise", "promised", "word", "deed", "writing",
    "written", "say", "said", "show", "tell", "terms", "answer", "kept",
    "accountable", "behind", "required", "earned", "enough", "own", "consent",
}
TRANSPARENCY_TERMS = {
    "inside", "disclosure", "visible", "view", "daylight", "light", "see",
    "shown", "show", "unhidden", "unredacted", "unabridged", "exposed",
    "spelled", "plain", "open", "full", "nothing", "mystery", "asterisk",
    "footnote", "fineprint", "smallprint", "coverstory", "uncovered",
}
SKIN_TERMS = {
    "skin", "face", "derm", "barrier", "bare", "layer", "surface", "cell",
    "ceramide", "lipid", "serum", "complexion", "epiderm", "cutaneous",
}
CAPABILITY_TERMS = {
    "strong", "strength", "hold", "keep", "stand", "steady", "last", "lasting",
    "durable", "living", "capable", "resilient", "resilience", "renew", "mend",
    "repair", "time", "long", "abide", "bearing", "support", "foundation",
    "fortify", "stamina", "mettle", "ballast", "endure", "intact",
}
HYPE_TERMS = {
    "antiaging", "antiage", "youth", "young", "ageless", "wrinkle", "miracle",
    "magic", "botox", "erase", "reverse", "reversal", "fountain", "flawless",
    "perfect", "perfection", "immortal", "foreveryoung", "timelessbeauty",
}
FAUX_LUXURY_TERMS = {
    "luxe", "luxury", "royal", "regal", "diamond", "platinum", "opulent",
    "couture", "velvet", "cashmere", "goddess", "divine", "elite",
}
GENERIC_WORDS = {
    "actual", "standard", "direct", "clear", "proof", "skin", "face", "real",
    "true", "choice", "context", "practical", "measure", "claim", "trace",
    "touch", "only", "here", "will", "match", "adjust", "responsive", "care",
    "beauty", "health", "wellness", "formula", "review", "evidence", "reason",
}
CONVERSATIONAL_STARTS = {
    "no", "we", "you", "your", "our", "show", "tell", "say", "ask", "stand",
    "put", "make", "take", "see", "look", "mean", "does", "do", "dont",
    "with", "without", "in", "as", "by", "all", "nothing", "sure", "plain",
}
SLOGAN_PRONOUNS = {"we", "you", "your", "our", "us", "it", "yourself"}
COINED_CONTEXT = {"coin", "coined", "coinage", "portmanteau", "morpheme", "periodic"}
STRONG_CONTEXT = {"compound", "insider", "real-word", "real word", "phrase", "contradiction"}

ATTITUDE_PHRASES = {
    "sureenough", "enoughsaid", "wemeanit", "standbyit", "as promised".replace(" ", ""),
    "sayitplain", "sayitplainly", "putplainly", "plaintosee", "nomystery",
    "noasterisk", "nofootnote", "nofineprint", "nosmallprint", "nopretense",
    "notheater", "showthework", "showyourwork", "showyoursources", "inwriting",
    "spelledout", "full disclosure".replace(" ", ""), "plainspoken",
}
THESIS_PHRASES = {
    "nomystery", "noasterisk", "nofootnote", "nofineprint", "nosmallprint",
    "showthework", "showyourwork", "showyoursources", "showtheformula",
    "inwriting", "allinwriting", "spelledout", "fullyspelled", "plaintosee",
    "putplainly", "sayitplain", "sayitplainly", "fulldisclosure", "openformula",
    "donttakeourword", "claimlessshowmore", "skinwithoutsecrets",
}


SOURCE_PRIORS = {
    "Legacy Curated 106": 8.2,
    "Final Blind Pool": 7.5,
    "Legacy Top 500": 7.3,
    "Net-New Federal 1000": 7.0,
    "Desire First 1000": 7.0,
    "Decoy Review": 6.8,
    "Core Worlds Round 1": 6.7,
    "Core Worlds Round 2": 6.7,
    "StraightUp Exploration": 6.6,
    "Skin Capability": 6.3,
    "Legacy First-Pass 100": 6.2,
}


def clamp(value: float, low: float = 0.0, high: float = 10.0) -> float:
    return max(low, min(high, value))


def tokenize(name: str) -> list[str]:
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    return [token.lower() for token in re.findall(r"[A-Za-z0-9]+", spaced)]


def contains_term(words: list[str], normalized: str, term: str) -> bool:
    if term in words:
        return True
    return len(term) >= 4 and term in normalized


def count_hits(words: list[str], normalized: str, terms: set[str]) -> int:
    return sum(1 for term in terms if contains_term(words, normalized, term))


def source_quality(row: dict[str, str], sorted_scores: list[float]) -> float:
    sources = [item.strip() for item in row["sources"].split(";") if item.strip()]
    prior = max((SOURCE_PRIORS.get(source, 5.8) for source in sources), default=5.8)
    if row["source_score_mean"]:
        score = float(row["source_score_mean"])
        left = bisect.bisect_left(sorted_scores, score)
        right = bisect.bisect_right(sorted_scores, score)
        percentile = ((left + right) / 2) / len(sorted_scores)
        calibrated = 4.8 + 4.6 * percentile
        prior = max(prior, calibrated)
    source_count = int(row["source_count"])
    if source_count >= 2:
        prior += 0.35
    if source_count >= 3:
        prior += 0.25
    return clamp(prior)


def component_scores(row: dict[str, str], sorted_scores: list[float]) -> dict[str, float | str]:
    name = row["name"]
    normalized = row["normalized"]
    words = tokenize(name)
    word_count = len(words)
    char_count = len(normalized)
    context = row["source_contexts"].lower()
    context_penalty = 0.0
    if "cut" in context:
        context_penalty += 1.35
    if "hold" in context:
        context_penalty += 0.35
    if "mechanical construction" in context:
        context_penalty += 0.9
    if "meaning stretch" in context:
        context_penalty += 0.55
    if "awkward" in context or "unclear" in context:
        context_penalty += 0.55

    direct = count_hits(words, normalized, DIRECT_TERMS)
    evidence = count_hits(words, normalized, EVIDENCE_TERMS)
    accountability = count_hits(words, normalized, ACCOUNTABILITY_TERMS)
    transparency = count_hits(words, normalized, TRANSPARENCY_TERMS)
    skin = count_hits(words, normalized, SKIN_TERMS)
    capability = count_hits(words, normalized, CAPABILITY_TERMS)
    hype = count_hits(words, normalized, HYPE_TERMS)
    faux_luxury = count_hits(words, normalized, FAUX_LUXURY_TERMS)
    first = words[0] if words else ""

    prior = source_quality(row, sorted_scores)

    attitude = 4.1
    attitude += min(2.4, direct * 0.75 + accountability * 0.55)
    if 2 <= word_count <= 4 and first in CONVERSATIONAL_STARTS:
        attitude += 1.25
    if first in {"no", "dont", "nothing", "without"}:
        attitude += 0.7
    if first == "no" and 2 <= word_count <= 3:
        attitude += 0.8
    if normalized in ATTITUDE_PHRASES:
        attitude += 1.2
    if word_count == 1 and direct:
        attitude += 0.4
    if word_count >= 5:
        attitude -= 1.1
    if faux_luxury:
        attitude -= min(1.6, faux_luxury * 0.8)
    if normalized.endswith(("ara", "oria", "ique", "elle")) and not direct:
        attitude -= 0.5
    attitude -= context_penalty * 0.45
    attitude = clamp(attitude)

    thesis = 3.7
    thesis += min(3.3, evidence * 0.85 + transparency * 0.65)
    thesis += min(1.7, accountability * 0.45 + direct * 0.35)
    thesis += min(0.9, capability * 0.3)
    if normalized in THESIS_PHRASES:
        thesis += 1.8
    if first == "no" and transparency:
        thesis += 1.25
    if normalized in {"sureenough", "enoughsaid", "wemeanit", "standbyit", "aspromised"}:
        thesis += 0.7
    thesis -= min(3.2, hype * 1.15)
    thesis -= min(1.4, faux_luxury * 0.55)
    thesis = clamp(thesis)

    verbal = 5.3
    if 1 <= word_count <= 3:
        verbal += 1.3
    elif word_count == 4:
        verbal += 0.5
    else:
        verbal -= 0.8
    if 5 <= char_count <= 16:
        verbal += 1.0
    elif char_count <= 22:
        verbal += 0.3
    else:
        verbal -= min(1.8, (char_count - 22) * 0.1)
    vowel_count = sum(1 for char in normalized if char in "aeiouy")
    vowel_ratio = vowel_count / char_count if char_count else 0
    if 0.30 <= vowel_ratio <= 0.62:
        verbal += 0.5
    elif vowel_ratio < 0.22:
        verbal -= 1.0
    if re.search(r"(.)\1\1", normalized):
        verbal -= 0.6
    if any(char.isdigit() for char in normalized):
        verbal -= 0.7
    verbal = clamp(verbal)

    distinctive = 5.0
    if any(term in context for term in COINED_CONTEXT):
        distinctive += 1.0
    if any(term in context for term in STRONG_CONTEXT):
        distinctive += 0.55
    if word_count == 1 and 6 <= char_count <= 12 and not direct and not skin:
        distinctive += 0.7
    if word_count == 2 and char_count <= 20:
        distinctive += 0.65
    if word_count == 1 and first in GENERIC_WORDS:
        distinctive -= 1.7
    if skin and word_count <= 2:
        distinctive -= 0.45
    if evidence + direct + transparency >= 2 and word_count <= 4:
        distinctive += 0.4
    if word_count >= 5:
        distinctive -= 0.8
    distinctive = clamp(distinctive)

    product_fit = 5.0
    product_fit += min(2.0, skin * 1.15)
    if 1 <= word_count <= 3 and char_count <= 18:
        product_fit += 1.2
    if direct + capability:
        product_fit += min(0.9, (direct + capability) * 0.25)
    if word_count >= 5:
        product_fit -= 1.5
    if len(set(words) & SLOGAN_PRONOUNS) >= 2:
        product_fit -= 0.7
    if hype:
        product_fit -= min(1.8, hype * 0.7)
    product_fit -= context_penalty * 0.85
    product_fit = clamp(product_fit)

    headroom = 5.5
    if 1 <= word_count <= 2 and not hype:
        headroom += 1.1
    if direct + accountability + capability:
        headroom += min(1.1, (direct + accountability + capability) * 0.25)
    if word_count >= 5:
        headroom -= 1.5
    if skin and (evidence + transparency + accountability == 0):
        headroom -= 0.6
    if hype:
        headroom -= min(1.7, hype * 0.7)
    headroom -= context_penalty * 0.6
    headroom = clamp(headroom)

    raw = (
        prior * 0.08
        + attitude * 0.24
        + thesis * 0.24
        + verbal * 0.13
        + distinctive * 0.13
        + product_fit * 0.10
        + headroom * 0.08
    )

    strengths: list[str] = []
    risks: list[str] = []
    if attitude >= 7.5:
        strengths.append("StraightUp-like attitude")
    if thesis >= 7.5:
        strengths.append("evidence/transparency fit")
    if skin:
        strengths.append("immediate category cue")
    if verbal >= 7.5:
        strengths.append("strong verbal usability")
    if distinctive >= 7.2:
        strengths.append("distinctive form")
    if hype:
        risks.append("age-panic or overclaim language")
    if faux_luxury:
        risks.append("faux-luxury signal")
    if word_count >= 5:
        risks.append("long/slogan-like")
    if distinctive < 5.0:
        risks.append("weak inherent distinctiveness")
    if product_fit < 5.5:
        risks.append("awkward masterbrand/product syntax")

    return {
        "source_quality": round(prior, 2),
        "straightup_attitude": round(attitude, 2),
        "brand_thesis_fit": round(thesis, 2),
        "verbal_strength": round(verbal, 2),
        "distinctiveness_proxy": round(distinctive, 2),
        "product_system_fit": round(product_fit, 2),
        "story_headroom": round(headroom, 2),
        "raw_composite": round(raw, 5),
        "strengths": "; ".join(strengths) if strengths else "general brand usability",
        "risks": "; ".join(risks) if risks else "no major creative penalty in rubric",
    }


def calibrated_score(percentile: float) -> float:
    # Anchored so >8.0 is intentionally selective: approximately the top 3%.
    points = [
        (0.00, 3.8),
        (0.10, 5.0),
        (0.40, 6.0),
        (0.70, 7.0),
        (0.97, 8.0),
        (0.995, 9.0),
        (1.00, 9.7),
    ]
    for (p0, s0), (p1, s1) in zip(points, points[1:]):
        if percentile <= p1:
            fraction = 0 if p1 == p0 else (percentile - p0) / (p1 - p0)
            return s0 + fraction * (s1 - s0)
    return 9.7


def tier(score: float) -> str:
    if score >= 9.0:
        return "A+ — exceptional"
    if score >= 8.5:
        return "A — priority"
    if score > 8.0:
        return "A- — serious contender"
    if score >= 7.5:
        return "B+ — strong longlist"
    if score >= 7.0:
        return "B — credible"
    if score >= 6.0:
        return "C — usable, not leading"
    return "D — cut"


def main() -> None:
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    score_values = sorted(
        float(row["source_score_mean"])
        for row in rows
        if row["source_score_mean"]
    )
    rated: list[dict[str, object]] = []
    for row in rows:
        components = component_scores(row, score_values)
        rated.append({**row, **components})

    rated.sort(
        key=lambda row: (
            -float(row["raw_composite"]),
            -int(row["source_count"]),
            str(row["name"]).lower(),
        )
    )
    count = len(rated)
    for index, row in enumerate(rated, 1):
        percentile = 1.0 - ((index - 1) / max(1, count - 1))
        score = round(calibrated_score(percentile), 2)
        row["master_rank"] = index
        row["cohesive_rating_10"] = score
        row["rating_tier"] = tier(score)
        row["trademark_screen_required"] = "YES" if score > 8.0 else "NO"

    ordered_fields = [
        "master_rank", "name", "cohesive_rating_10", "rating_tier",
        "trademark_screen_required", "straightup_attitude", "brand_thesis_fit",
        "verbal_strength", "distinctiveness_proxy", "product_system_fit",
        "story_headroom", "source_quality", "strengths", "risks",
        "source_count", "sources", "source_score_count", "source_score_mean", "source_score_max",
        "source_contexts", "normalized", "source_files", "raw_composite",
    ]
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ordered_fields)
        writer.writeheader()
        writer.writerows(rated)

    above = [row for row in rated if float(row["cohesive_rating_10"]) > 8.0]
    with ABOVE_EIGHT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ordered_fields)
        writer.writeheader()
        writer.writerows(above)

    summary = {
        "rated_name_count": count,
        "above_8_count": len(above),
        "above_8_share": round(len(above) / count, 4),
        "score_anchor": ">8.0 is calibrated to approximately the top 3% of the full pool",
        "rubric_weights": {
            "cross_round_source_quality": 0.08,
            "straightup_attitude": 0.24,
            "brand_thesis_fit": 0.24,
            "verbal_strength": 0.13,
            "distinctiveness_proxy": 0.13,
            "product_system_fit": 0.10,
            "story_headroom": 0.08,
        },
        "score_distribution": {
            "9_plus": sum(1 for row in rated if float(row["cohesive_rating_10"]) >= 9),
            "8_to_8_99": sum(1 for row in rated if 8 <= float(row["cohesive_rating_10"]) < 9),
            "7_to_7_99": sum(1 for row in rated if 7 <= float(row["cohesive_rating_10"]) < 8),
            "6_to_6_99": sum(1 for row in rated if 6 <= float(row["cohesive_rating_10"]) < 7),
            "below_6": sum(1 for row in rated if float(row["cohesive_rating_10"]) < 6),
        },
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print("\nTop 50:")
    for row in rated[:50]:
        print(
            f"{row['master_rank']:>4}  {row['cohesive_rating_10']:>4}  "
            f"{row['name']}"
        )


if __name__ == "__main__":
    main()
