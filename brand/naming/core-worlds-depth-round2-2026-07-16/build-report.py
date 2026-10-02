from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULTS = HERE / "top-500-trademark-results.csv"
AUDIT = HERE / "generation-rating-audit.json"
DISCUSSION = HERE / "discussion-set-32.csv"
REPORT = HERE / "FINAL-REPORT.md"


SELECTED = [
    ("Continuous Form", "ADVANCE", "A composed, premium way to hold continuity and physical form in one name; it can stretch from preservation to capability without saying anti-aging."),
    ("Durable Present", "ADVANCE", "Turns longevity away from forever and toward remaining fully in the present; intelligent, optimistic, and less claim-like."),
    ("Present Continuous", "ADVANCE", "A familiar grammatical form becomes an elegant model of ongoing change; editorial rather than medical."),
    ("Return Again", "REACTION TEST", "Warm, circular continuation with ritual potential; the redundancy is either memorable or irritating, which makes it worth founder testing."),
    ("Inspectably", "ADVANCE", "A strange but legible adverb that makes openness an operating behavior, not a clean-beauty adjective."),
    ("Uncurtained", "ADVANCE", "Human, visual transparency with no compliance language; slightly literary and unusually tactile."),
    ("Visible Join", "REACTION TEST", "Says the construction is allowed to show, a strong metaphor for formula and sourcing transparency; feels design-led."),
    ("Source Open", "REACTION TEST", "Puts provenance before polish in a compact reversal; technical syntax may be a feature or a flaw."),
    ("Stillself", "HOLD — MARKET USE", "The cleanest expression of identity continuity in the round, but fresh exact marketplace use means it is not presently clean enough to advance without counsel."),
    ("In Full Face", "ADVANCE", "Reclaims a makeup expression to mean fully oneself and fully visible; category-relevant with productive tension."),
    ("Feature Signature", "ADVANCE", "Treats recognizable features as a personal signature instead of defects; premium and extensible, though two-word."),
    ("Portrait Continuity", "REACTION TEST", "Precisely names recognizable identity through time; more editorial platform than compact mark, but strategically exact."),
    ("Well Practiced", "ADVANCE", "Makes results the product of an intelligent repeatable practice; mature, calm, and non-gym."),
    ("Skillful Skin", "REACTION TEST", "A direct capability reframe with alliteration; clear enough to teach the world, but close to a positioning line."),
    ("Coachmark", "REACTION TEST", "Compact coaching language with a useful mark/result echo; also an established UX term, which adds technical baggage."),
    ("Gentle Progression", "REACTION TEST", "The best contradiction inside training: increase capacity without punishment; more regimen or method than masterbrand."),
    ("Understated Output", "ADVANCE", "A premium performance contradiction—quiet tone, observable result; strongest as a sophisticated efficacy brand."),
    ("Plain Result", "REACTION TEST", "Refreshingly anti-hype and easy to understand; its plainness may also make it hard to own."),
    ("Notice Mark", "REACTION TEST", "Compresses visible change into a crisp constructed form; meaning needs a beat but the shape feels like a mark."),
    ("Result Window", "PLATFORM CANDIDATE", "A concrete place where progress becomes visible; better for a measurement system or content property than a house."),
    ("Adaptive Margin", "ADVANCE", "Names the extra capacity to handle variability, an excellent scientific story with less fortress language."),
    ("Elastic Reserve", "REACTION TEST", "Communicates give plus stored capacity; credible and tactile, though it may sound like a technology platform."),
    ("Controlled Give", "ADVANCE", "A productive barrier contradiction: strength that yields intelligently rather than hardening."),
    ("Response Margin", "PLATFORM CANDIDATE", "Authentic control-system language for skin headroom; strategically rich but technical for a masterbrand."),
    ("Factchecked", "REACTION TEST", "A familiar proof behavior in a compact form; current journalism meaning may overpower beauty and narrow protection."),
    ("Error Bar", "ADVANCE", "Evidence with honesty built in: proof that includes uncertainty. Distinctive worldview, though deliberately cerebral."),
    ("Measured Doubt", "REACTION TEST", "An excellent evidence contradiction that rejects false certainty; likely stronger as a principle or campaign."),
    ("Open Assay", "REACTION TEST", "Makes product testing visible and inspectable; attractive scientific form, more lab/platform than lifestyle."),
    ("Knowingly", "HOLD — RELATED FILING", "Warm agency in a real adverb, but KNOWINGLY HEALTHY has a current relevant filing and broader uses make the territory less clean."),
    ("Sense First", "ADVANCE", "Puts customer judgment before authority in a short, human stance; can also imply sensoriality in beauty."),
    ("Question Ready", "REACTION TEST", "Frames informed customers as prepared to challenge claims; energetic but more attitude than luxury."),
    ("Clearheaded Beauty", "REACTION TEST", "The strategy is immediately legible and culturally useful; likely a positioning line or editorial property rather than a strong mark."),
]


MARKET_NOTES = {
    "Stillself": "Exact StillSelf Etsy shop active in 2026; small/non-beauty use, but a current common-law flag.",
    "In Full Face": "Full face is ordinary makeup language; the phrase carries useful category tension but likely narrower exclusivity.",
    "Coachmark": "Coach mark is established UX/onboarding terminology; no obvious beauty operator surfaced in the targeted check.",
    "Factchecked": "Ordinary journalism and verification language; federal pass does not make it inherently distinctive.",
    "Knowingly": "KNOWINGLY HEALTHY has a 2025 filing in Classes 005 and 044; counsel should assess scope before any advance.",
}


PRESSURE_SHORTLIST = [
    "Continuous Form",
    "Inspectably",
    "In Full Face",
    "Durable Present",
    "Well Practiced",
    "Feature Signature",
    "Uncurtained",
    "Controlled Give",
    "Understated Output",
    "Adaptive Margin",
    "Error Bar",
    "Sense First",
]


WORLD_ORDER = [
    "Time and Skin Longevity",
    "Nothing Hidden and Transparency",
    "Bare Face and Recognizable Self",
    "Skin Capability and Training",
    "Visible Performance",
    "Barrier Strength and Adaptive Capacity",
    "Evidence and Proof",
    "Better Informed and Customer Agency",
]


WORLD_READ = {
    "Bare Face and Recognizable Self": "Still the strongest masterbrand world. The second ring found identity-continuity forms that are emotionally specific without youth language.",
    "Time and Skin Longevity": "Still the deepest lexical world. Publishing and grammatical continuity improved the tone, but the territory remains crowded and many source terms are descriptive.",
    "Nothing Hidden and Transparency": "The largest round-two improvement. Inspection, open construction, and visible joins feel more distinctive than labels, ledgers, or generic clarity.",
    "Skin Capability and Training": "Strategically strong when it sounds like practice, skill, and progression. Literal workout and coaching mechanics still skew toward program names.",
    "Barrier Strength and Adaptive Capacity": "Control-system margins and flexible response created a better story than armor. Many outputs still feel like technologies or product platforms.",
    "Visible Performance": "Commercially legible but structurally descriptive. Its best language pairs quiet tone with hard output rather than making louder claims.",
    "Evidence and Proof": "Produced sharp worldview language around uncertainty and reproducibility, but most forms remain cerebral, editorial, or lab-like.",
    "Better Informed and Customer Agency": "Useful for brand voice and education systems; still the weakest source of premium masterbrands. Sense First is the main exception worth pressure-testing.",
}


def md_table(headers: list[str], rows: list[list[object]]) -> str:
    output = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    output.extend("| " + " | ".join(str(value) for value in row) + " |" for row in rows)
    return "\n".join(output)


def main() -> None:
    with RESULTS.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_name = {row["Name"]: row for row in rows}
    missing = [name for name, _, _ in SELECTED if name not in by_name]
    if missing:
        raise ValueError(f"Discussion names missing from screened file: {missing}")

    discussion_rows = []
    for rank, (name, editorial_status, why) in enumerate(SELECTED, start=1):
        row = by_name[name]
        discussion_rows.append(
            {
                "DiscussionRank": rank,
                "Name": name,
                "World": row["World"],
                "Exercise": row["Exercise"],
                "Form": row["Form"],
                "CreativeRating": row["CreativeRating"],
                "CreativeDecision": row["CreativeDecision"],
                "TrademarkDecision": row["TrademarkDecision"],
                "EditorialStatus": editorial_status,
                "WhyItRemains": why,
                "MarketplaceNote": MARKET_NOTES.get(name, "No obvious exact skincare operator surfaced in the limited targeted web check; this is not clearance."),
            }
        )

    with DISCUSSION.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(discussion_rows[0]))
        writer.writeheader()
        writer.writerows(discussion_rows)

    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    decision_counts = Counter(row["TrademarkDecision"] for row in rows)
    by_world = defaultdict(list)
    for row in rows:
        by_world[row["World"]].append(row)

    world_rows = []
    for world in WORLD_ORDER:
        group = by_world[world]
        world_rows.append(
            [
                world,
                len(group),
                sum(row["TrademarkDecision"] == "PROVISIONAL PASS" for row in group),
                sum(row["TrademarkDecision"].startswith("YELLOW") for row in group),
                sum(row["TrademarkDecision"].startswith("AMBER") for row in group),
                sum(row["TrademarkDecision"].startswith("RED") for row in group),
            ]
        )

    pressure_rows = []
    for rank, name in enumerate(PRESSURE_SHORTLIST, start=1):
        row = by_name[name]
        reason = next(reason for selected_name, _, reason in SELECTED if selected_name == name)
        pressure_rows.append([rank, f"**{name}**", row["World"], row["CreativeRating"], reason])

    discussion_table = []
    for item in discussion_rows:
        discussion_table.append(
            [
                item["DiscussionRank"],
                f"**{item['Name']}**",
                item["World"],
                item["CreativeRating"],
                item["EditorialStatus"],
                item["WhyItRemains"],
            ]
        )

    report = f"""# Core worlds depth round two — final report

**Completed:** July 16, 2026  
**Scope:** A fresh second ring across the same eight founder-approved worlds, all 17 Placek-style exercises, creative rating before availability, full-project deduplication, and a balanced 500-name federal knockout screen.

## Outcome

- Raw candidates: **{audit['raw_candidates']:,}**
- Exercise/world cells: **136**
- Historical project-name index: **{audit['historical_index_size']:,}** normalized names
- Historical exact rejections, including round one: **{audit['historical_rejections']:,}**
- Internal duplicate rejections: **{audit['internal_duplicate_rejections']:,}**
- Project-fresh rated survivors: **{audit['rated_survivors']:,}**
- Names selected for federal screening: **500**
- Federal search keys evaluated: **428,736**
- Matched federal case records: **3,809**

The generation sources were intentionally different from round one: serial publishing and service life; microscopy and open construction; portrait sittings and identity continuity; motor learning and practice design; metrology and inspection; feedback margins and headroom; reproducibility and uncertainty; and decision science and wayfinding.

## Federal knockout summary

{md_table(
    ["Decision", "Count"],
    [
        ["PROVISIONAL PASS", decision_counts["PROVISIONAL PASS"]],
        ["YELLOW - DEAD EXACT", decision_counts["YELLOW - DEAD EXACT"]],
        ["YELLOW - LIVE NEAR", decision_counts["YELLOW - LIVE NEAR"]],
        ["AMBER - LIVE EXACT", decision_counts["AMBER - LIVE EXACT"]],
        ["AMBER - LIVE NEAR / RELEVANT", decision_counts["AMBER - LIVE NEAR / RELEVANT"]],
        ["RED - LIVE EXACT / RELEVANT", decision_counts["RED - LIVE EXACT / RELEVANT"]],
    ],
)}

## Results by world

{md_table(["World", "Screened", "Pass", "Yellow", "Amber", "Red"], world_rows)}

## What changed versus round one

| Measure | Round one | Round two | Change |
|---|---:|---:|---:|
| Raw pool | 5,808 | 5,840 | +32 |
| Fresh rated survivors | 4,166 | 4,155 | -11 |
| Federal provisional passes | 204 | 340 | +136 |
| Provisional-pass rate | 40.8% | 68.0% | +27.2 points |
| Relevant live exact reds | 110 | 30 | -80 |

This is a real whitespace improvement, not proof that the round contains 340 good brands. The second-ring sources produced fewer direct collisions because they moved farther from obvious beauty vocabulary. They also produced more authentic phrases and technical terms, which can clear an exact screen while still being weak, descriptive, cold, or hard to protect. Human editing remains the decisive pass.

## Founder pressure-test shortlist

These are the 12 names I would actually put into the next founder reaction exercise. All 12 received federal provisional passes. The order is editorial, not a legal ranking.

{md_table(["#", "Name", "World", "Rating", "Why"], pressure_rows)}

## Human-edited discussion set

The 32-name set includes the pressure shortlist plus useful reaction tests, platform candidates, and two linguistically strong holds. It is deliberately not 32 recommendations.

{md_table(["#", "Name", "World", "Rating", "Editorial status", "Why it remains"], discussion_table)}

## Editorial ranking of the worlds after two deep rounds

1. **Bare Face / Recognizable Self** — {WORLD_READ['Bare Face and Recognizable Self']}
2. **Time / Skin Longevity** — {WORLD_READ['Time and Skin Longevity']}
3. **Nothing Hidden / Transparency** — {WORLD_READ['Nothing Hidden and Transparency']}
4. **Skin Capability / Training** — {WORLD_READ['Skin Capability and Training']}
5. **Barrier Strength / Adaptive Capacity** — {WORLD_READ['Barrier Strength and Adaptive Capacity']}
6. **Visible Performance** — {WORLD_READ['Visible Performance']}
7. **Evidence / Proof** — {WORLD_READ['Evidence and Proof']}
8. **Better Informed / Customer Agency** — {WORLD_READ['Better Informed and Customer Agency']}

## Current-market findings that change the edit

- **Stillself** is one of the best linguistic forms, but a [StillSelf Etsy shop](https://www.etsy.com/listing/4469105615/minimalist-office-wall-art-past-this) began operating in 2026. The use is small and outside beauty, but it is current exact use; hold for counsel rather than calling it clean.
- **Another Volume** should be retired from the discussion set because Essence sells [Another Volume Mascara… Just Better!](https://www.essence.eu/de-de/p/936011/another-volume-mascarajust-better), an exact phrase in cosmetics.
- **Choicecraft** should be retired: [ChoiceCraft](https://choicecraft.in/) currently operates a product-comparison platform, directly occupying the customer-decision meaning, and another current operator uses the same name for admissions strategy.
- **Living Range** should be retired as a masterbrand because [Living Range](https://livingrange.co.uk/) is an operating UK retailer, even though the goods are not skincare.
- **Knowingly** remains a hold because [KNOWINGLY HEALTHY](https://trademarks.justia.com/990/43/knowingly-99043770.html) has a current filing in Classes 005 and 044. That is not an exact identity, but it is close enough in relevant services to require counsel.
- **Residence Time** is authentic and federally clear in this exact screen, but current cosmetic technology already uses the phrase descriptively for how long ingredients remain on skin. It is better as source language than as a leading mark.
- **Coachmark** is established interface/onboarding terminology. It can still be an interesting brand metaphor, but it carries a software meaning that needs testing.

## Core conclusion

Round two did not overturn the world strategy. It strengthened it. The genuinely new seam is **continuity of form**: not agelessness, reversal, or preservation, but remaining recognizably oneself while still developing. That seam connects the three best worlds—Bare Face, Time, and Training—and is why **Continuous Form**, **In Full Face**, **Durable Present**, **Well Practiced**, and **Feature Signature** feel more promising than most isolated invented words.

The next productive move is not another 5,000-name round. It is a founder pressure test on the 12-name shortlist using positioning lines, package mockups, spoken introductions, and forced-choice reactions. If the founders reject the underlying forms—not just particular names—we will have learned which world or tone to eliminate before generating again.

## How to use the files

- `raw-pool.csv`: all 5,840 generated candidates across 136 cells.
- `deduped-rated-pool.csv`: all 4,155 project-fresh candidates with component ratings.
- `dedupe-rejections.csv`: every historical or internal collision and its reason.
- `top-500-rated.csv`: the balanced federal-screening set, preserving global and world ranks.
- `top-500-trademark-results.csv`: the full 500-name screen with decisions and representative records.
- `top-500-trademark-hits.csv`: all matched federal case records used by the screen.
- `discussion-set-32.csv`: the human-edited set with editorial status, rationale, and marketplace notes.

## Legal limits

This is a preliminary knockout, not trademark clearance or legal advice. Exact normalized identity ignores case, spaces, punctuation, and diacritics. Compact names also received a one-character insertion, deletion, substitution, and adjacent-transposition pass. The local corpus contains 14,180,757 distinct serials and source records through July 6, 2026; relevant classes were 003, 005, 010, 021, 035, and 044.

The screen can miss phonetic, conceptual, translated, common-law, newly filed, and related-goods conflicts. Any finalist still requires attorney-led clearance plus current state, domain, trade-name, social-handle, international, and marketplace searching.
"""
    REPORT.write_text(report, encoding="utf-8")
    print(json.dumps({"discussion_rows": len(discussion_rows), "report": str(REPORT)}, indent=2))


if __name__ == "__main__":
    main()
