from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULTS = HERE / "top-500-trademark-results.csv"
GEN_AUDIT = HERE / "generation-rating-audit.json"
TM_AUDIT = HERE / "top-500-trademark-summary.json"

DISCUSSION = [
    (1, "Nextkeeping", "A compact long-term-care idea with a clear keeping/next tension."),
    (2, "Yearproof", "Turns longevity into a bold durability standard; warranty overtones remain."),
    (3, "Onwardly", "Optimistic continuation in a clean adverb form; the one-edit Class 005 hit needs counsel."),
    (4, "Added Time", "A familiar expression that makes continued improvement tangible, though protection may be narrow."),
    (5, "Showthrough", "Transparency with a material/visual meaning; slightly industrial but unusually ownable in tone."),
    (6, "Undisguised", "Direct openness and natural-face relevance; already appears as ordinary beauty copy."),
    (7, "Ingredient Ledger", "Makes disclosure operational and distinctive, but may fit a system better than the house."),
    (8, "Viewing Port", "A concrete device for seeing inside; crisp but technical."),
    (9, "Recognizably", "Names continuity of identity instead of youth; long but semantically exact."),
    (10, "Original Negative", "Photography term with a productive anti-correction second meaning."),
    (11, "Candid Standard", "Combines unperformed appearance with a higher standard; somewhat editorial."),
    (12, "Same Person", "Human and emotionally immediate, but common language and likely narrow protection."),
    (13, "Adaptive Practice", "The clearest non-gym expression of progressive skin capability."),
    (14, "Gentle Load", "A useful training contradiction: enough input to adapt without punishment."),
    (15, "Rangekind", "A compact capability coinage with a human tone; interpretation is not immediate."),
    (16, "Motor Pattern", "Authentic training language with strong form, but body-performance associations dominate."),
    (17, "Visible Gain", "Direct performance language that survives the federal screen but is close to a claim."),
    (18, "Change Register", "A technical record of improvement; intelligent but not emotionally warm."),
    (19, "Understated Result", "A premium performance contradiction, though phrase-like."),
    (20, "By Degrees", "Gradual visible improvement in a familiar idiom; dead exact federal history exists."),
    (21, "Living Buffer", "Makes resilience active and biological without literal armor language."),
    (22, "Allostasis", "Authentic adaptive-regulation term with strong science; explanation dependence is high."),
    (23, "Adaptive Range", "Functional and clear, but closer to a platform or regimen than a masterbrand."),
    (24, "Tolerance Window", "Authentic capacity language with a strong story; medical/technical tone remains."),
    (25, "Shown Work", "Compact proof idea with less classroom syntax than Show Your Work."),
    (26, "Witnessed", "Evidence as something observed; live one-edit and dead exact records require review."),
    (27, "Verify First", "Clear operating stance, but it behaves more like a principle than a house name."),
    (28, "Claim Accounted", "Every promise has support; grammatically tense and campaign-like."),
    (29, "Understandably", "Warm, human comprehension without teacher language; category signal is weak."),
    (30, "Plainly Advanced", "Combines accessibility and sophistication in a productive contradiction."),
    (31, "Beginner Expert", "Customer agency through a bold contradiction; can sound like an education product."),
    (32, "Knowhow Club", "Community and practical knowledge in one structure; less premium and likely weak protection."),
]

MARKETPLACE_NOTES = {
    "Nextkeeping": "No exact operating beauty identity surfaced in a targeted current search.",
    "Showthrough": "No exact operating beauty identity surfaced in a targeted current search.",
    "Recognizably": "No exact source identity surfaced; ordinary beauty/editorial use of the word exists.",
    "Undisguised": "Ordinary beauty copy exists, including transparency/natural-face positioning; no exact source identity surfaced.",
    "Adaptive Practice": "Used descriptively in current skincare editorial language; no exact source identity surfaced.",
    "Living Buffer": "No exact operating beauty identity surfaced in a targeted current search.",
    "Visible Gain": "No exact operating beauty identity surfaced in a targeted current search.",
    "Change Register": "No exact operating beauty identity surfaced in a targeted current search.",
    "Shown Work": "No exact operating beauty identity surfaced in a targeted current search.",
    "Understandably": "No exact operating beauty identity surfaced; it remains an ordinary adverb.",
    "Original Features": "Used descriptively in beauty testing/editorial material; not advanced to the discussion set.",
    "Response Reserve": "Retired after current search: AMOREPACIFIC sells Time Response Skin Reserve products.",
}


def read_rows() -> list[dict[str, str]]:
    with RESULTS.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def md(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def main() -> None:
    rows = read_rows()
    by_name = {row["Name"]: row for row in rows}
    missing = [name for _, name, _ in DISCUSSION if name not in by_name]
    if missing:
        raise ValueError(f"Discussion names missing from screened top 500: {missing}")

    finalists = []
    for order, name, reason in DISCUSSION:
        source = by_name[name]
        finalists.append(
            {
                "EditorialOrder": order,
                "Name": name,
                "World": source["World"],
                "CreativeRating": source["CreativeRating"],
                "ExerciseNumber": source["ExerciseNumber"],
                "Exercise": source["Exercise"],
                "Form": source["Form"],
                "TrademarkDecision": source["TrademarkDecision"],
                "RepresentativeHits": source["RepresentativeHits"],
                "EditorialReason": reason,
                "MarketplaceNote": MARKETPLACE_NOTES.get(name, "Not included in the targeted current-marketplace leader check."),
            }
        )
    with (HERE / "discussion-set-32.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(finalists[0]))
        writer.writeheader()
        writer.writerows(finalists)

    gen = json.loads(GEN_AUDIT.read_text(encoding="utf-8"))
    tm = json.loads(TM_AUDIT.read_text(encoding="utf-8"))

    world_decisions: dict[str, Counter] = defaultdict(Counter)
    for row in rows:
        world_decisions[row["World"]][row["TrademarkDecision"]] += 1

    world_order = [
        "Time and Skin Longevity",
        "Nothing Hidden and Transparency",
        "Bare Face and Recognizable Self",
        "Skin Capability and Training",
        "Visible Performance",
        "Barrier Strength and Adaptive Capacity",
        "Evidence and Proof",
        "Better Informed and Customer Agency",
    ]

    lines = [
        "# Core worlds depth round - final report",
        "",
        "**Completed:** July 16, 2026  ",
        "**Scope:** Eight core naming worlds, all 17 exercises, creative rating before availability, and a 500-name federal knockout screen.",
        "",
        "## Outcome",
        "",
        f"- Raw candidates: **{gen['raw_candidates']:,}**",
        f"- Historical project-name index: **{gen['historical_index_size']:,}** normalized names",
        f"- Historical exact rejections: **{gen['historical_rejections']:,}**",
        f"- Internal duplicate rejections: **{gen['internal_duplicate_rejections']:,}**",
        f"- Project-fresh rated survivors: **{gen['rated_survivors']:,}**",
        f"- Names selected for federal screening: **{tm['candidate_count']:,}**",
        f"- Federal search keys evaluated: **{tm['search_key_count']:,}**",
        f"- Matched federal case records: **{tm['matched_case_record_count']:,}**",
        "",
        "The top-500 screen uses a 40-name floor per world and then fills by global creative rating with a 90-name ceiling. This preserves the founder's request to test every core world while retaining the original overall rating on every row.",
        "",
        "## Federal knockout summary",
        "",
        "| Decision | Count |",
        "|---|---:|",
    ]
    decision_order = [
        "PROVISIONAL PASS",
        "YELLOW - DEAD EXACT",
        "YELLOW - LIVE NEAR",
        "AMBER - LIVE EXACT",
        "AMBER - LIVE NEAR / RELEVANT",
        "RED - LIVE EXACT / RELEVANT",
    ]
    for decision in decision_order:
        lines.append(f"| {decision} | {tm['decision_counts'].get(decision, 0):,} |")

    lines.extend(
        [
            "",
            "## Results by world",
            "",
            "| World | Screened | Pass | Yellow | Amber | Red |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for world in world_order:
        counts = world_decisions[world]
        screened = sum(counts.values())
        yellow = sum(value for key, value in counts.items() if key.startswith("YELLOW"))
        amber = sum(value for key, value in counts.items() if key.startswith("AMBER"))
        red = counts["RED - LIVE EXACT / RELEVANT"]
        lines.append(
            f"| {world} | {screened} | {counts['PROVISIONAL PASS']} | {yellow} | {amber} | {red} |"
        )

    lines.extend(
        [
            "",
            "## Human-edited discussion set",
            "",
            "These are not 32 recommendations and the ordering is not a declaration of a winner. They are the names that remain most useful for founder reaction after the creative and federal passes. The rating is structured triage, not consumer truth.",
            "",
            "| # | Name | World | Rating | Federal screen | Why it remains |",
            "|---:|---|---|---:|---|---|",
        ]
    )
    for item in finalists:
        lines.append(
            f"| {item['EditorialOrder']} | **{md(item['Name'])}** | {md(item['World'])} | {item['CreativeRating']} | {md(item['TrademarkDecision'])} | {md(item['EditorialReason'])} |"
        )

    lines.extend(
        [
            "",
            "## Editorial read by world",
            "",
            "1. **Bare Face / Recognizable Self** produced the most emotionally specific language. Its best names preserve identity rather than promise youth.",
            "2. **Time / Longevity** produced the greatest lexical depth and the most collisions. The territory remains strategically right but commercially crowded.",
            "3. **Nothing Hidden / Transparency** improved when it used material and optical language rather than documents, policies, or slogans.",
            "4. **Skin Capability / Training** works best through adaptation and form, not literal reps, sessions, or gym language.",
            "5. **Barrier / Adaptive Capacity** generated credible systems and scientific terms, but many feel more like technology platforms or product families than masterbrands.",
            "6. **Visible Performance** generated direct commercial language but also the highest risk of descriptiveness and claim-like names.",
            "7. **Evidence / Proof** remains strategically essential but still tends to create content, legal, and testing language rather than desire.",
            "8. **Better Informed / Customer Agency** remains the weakest masterbrand world. Its strongest outputs are useful for education systems and brand voice.",
            "",
            "## Important current-market findings",
            "",
            "- `Response Reserve` received a federal provisional pass but should be retired because AMOREPACIFIC currently sells `Time Response Skin Reserve` products.",
            "- `Adaptive Practice` appears descriptively in current skincare editorial language, which weakens proprietary character even without an exact source identity.",
            "- `Undisguised` appears as ordinary transparency and natural-face beauty copy; it is not clean proprietary territory merely because the federal exact screen passed.",
            "- `Recognizably` appears in current beauty editorial copy, but no exact operating source identity surfaced in the targeted check.",
            "",
            "## How to use the files",
            "",
            "- `deduped-rated-pool.csv`: all 4,166 fresh candidates with component ratings.",
            "- `top-500-rated.csv`: the balanced federal-screening set, preserving overall rank and selection basis.",
            "- `top-500-trademark-results.csv`: the full 500-name screen with representative records.",
            "- `top-500-trademark-hits.csv`: every matched federal case record used by the screen.",
            "- `discussion-set-32.csv`: the smaller human-edited set with reasons and marketplace notes.",
            "",
            "## Legal limits",
            "",
            "This is a preliminary knockout, not trademark clearance or legal advice. Exact normalized identity ignores case, spaces, punctuation, and diacritics. Compact names also received a one-character insertion, deletion, substitution, and adjacent-transposition pass. The corpus contains 14,180,757 distinct serials and source records through July 6, 2026; relevant classes were 003, 005, 010, 021, 035, and 044.",
            "",
            "A finalist still requires attorney-led searching for broader phonetic and conceptual similarity, related goods and services, current USPTO filings, state and common-law rights, domains, trade names, social handles, and international markets.",
            "",
        ]
    )
    (HERE / "FINAL-REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"discussion_names": len(finalists), "report": str(HERE / 'FINAL-REPORT.md')}, indent=2))


if __name__ == "__main__":
    main()

