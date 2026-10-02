import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read_csv(filename):
    with (ROOT / filename).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


screened = read_csv("screened-1000.csv")
final50 = read_csv("finalists-50.csv")
final20 = final50[:20]
market100 = read_csv("marketplace-search-results.csv")
with (ROOT / "raw-generation-audit.json").open(encoding="utf-8") as f:
    raw_audit = json.load(f)
with (ROOT / "blind-pool-audit.json").open(encoding="utf-8") as f:
    blind_audit = json.load(f)

screen_priority = {
    "PROVISIONAL PASS": 0,
    "YELLOW - DEAD EXACT": 1,
    "YELLOW - LIVE NEAR": 2,
    "AMBER - LIVE NEAR / RELEVANT": 3,
    "AMBER - LIVE EXACT": 4,
    "RED - LIVE EXACT / RELEVANT": 5,
}
ranked = sorted(
    screened,
    key=lambda r: (
        screen_priority.get(r["TrademarkDecision"], 9),
        -float(r["CreativeScore"]),
        r["Name"].casefold(),
    ),
)
rank_fields = ["ScreenAwareRank"] + list(ranked[0].keys())
with (ROOT / "all-1000-screen-aware-ranked.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rank_fields)
    writer.writeheader()
    for rank, row in enumerate(ranked, 1):
        writer.writerow({"ScreenAwareRank": rank, **row})


def short_federal(value):
    return {
        "PROVISIONAL PASS": "Pass*",
        "YELLOW - DEAD EXACT": "Yellow: dead exact",
        "YELLOW - LIVE NEAR": "Yellow: live near",
        "AMBER - LIVE NEAR / RELEVANT": "Amber: near/relevant",
        "AMBER - LIVE EXACT": "Amber: live exact",
        "RED - LIVE EXACT / RELEVANT": "Red: remove",
    }.get(value, value)


def short_market(value):
    return {
        "PROVISIONAL - NO OBVIOUS EXACT": "No obvious exact*",
        "CAUTION - ACTIVE OTHER USE": "Other active use",
        "CAUTION - TRADEMARK/PRODUCT": "TM/product caution",
        "REMOVE - DIRECT BEAUTY/HEALTH": "Direct conflict: remove",
    }.get(value, value)


screen_counts = Counter(r["TrademarkDecision"] for r in screened)
market_counts = Counter(r["MarketplaceDecision"] for r in market100)
direction_counts = Counter(r["Direction"] for r in screened)

methods = [
    "Intangible-to-tangible",
    "Benefit ladder",
    "Future reframe",
    "Anti-descriptor",
    "Win-by-contrast",
    "Audacity / worldview",
    "Deconstruct / reconstruct",
    "Portmanteau",
    "Morpheme engine",
    "Scientific borrowing",
    "Sound-first coinage",
    "Structural / orthographic devices",
    "Compounds",
    "Real-word metaphor / eponym",
    "World-language hunt",
    "Far-field source raids",
    "Decoy briefs",
]

lines = []
lines.append("# Desire-first anti-aging brand naming run")
lines.append("")
lines.append("**Completed:** July 16, 2026")
lines.append("")
lines.append("## The outcome")
lines.append("")
lines.append(
    f"This run produced **{raw_audit['raw_unique_count']:,} normalized-unique raw candidates**, "
    f"then selected exactly **1,000 project-fresh names** across ten blind briefs. "
    "Skincare was revealed only after the names were formed. All 1,000 were creatively scored and screened against a local USPTO-derived federal corpus; the strongest 100 non-red candidates then received one exact-name web search apiece."
)
lines.append("")
lines.append("The practical handoff is:")
lines.append("")
lines.append("- `finalists-20.csv`: the most interesting conversation set")
lines.append("- `finalists-50.csv`: the broader curated finalist set")
lines.append("- `marketplace-search-results.csv`: the 100 exact-name web checks and evidence links")
lines.append("- `top-200-non-red.csv`: the non-red consideration pool")
lines.append("- `all-1000-screen-aware-ranked.csv`: every rated name, with federal screen evidence")
lines.append("")
lines.append("## The 20 to discuss first")
lines.append("")
lines.append("| Rank | Name | Rating | World | Federal screen | Exact-name web scan |")
lines.append("|---:|---|---:|---|---|---|")
for row in final20:
    lines.append(
        f"| {row['FinalRank']} | **{row['Name']}** | {row['CuratorScore']} | {row['Direction'].replace('The ', '')} | "
        f"{short_federal(row['TrademarkDecision'])} | {short_market(row['MarketplaceDecision'])} |"
    )
lines.append("")
lines.append("### Cleanest early slate")
lines.append("")
clean = [
    r for r in final50
    if r["TrademarkDecision"] == "PROVISIONAL PASS"
    and r["MarketplaceDecision"] == "PROVISIONAL - NO OBVIOUS EXACT"
]
lines.append(", ".join(f"**{r['Name']}**" for r in clean[:12]) + ".")
lines.append("")
lines.append("This is the lowest-friction starting slate from the current quick screens—not a legal clearance conclusion.")
lines.append("")
lines.append("## Why these worlds are genuinely different")
lines.append("")
lines.append("| World | Names | What it is trying to make people desire |")
lines.append("|---|---:|---|")
world_desire = {
    "The Invented House": "160 | The authority and magnetism of an established house, without a fake founder story",
    "The Pure Sound Lab": "160 | A beautiful verbal object with almost no inherited meaning",
    "The Beautiful Object": "110 | A modern heirloom: tactile, collectible, and display-worthy",
    "The Magnetic Character": "100 | A person-like presence customers want to trust and know",
    "The Private World": "90 | Entry into a secluded room, estate, or private atmosphere",
    "The Cultural Mononym": "100 | An unexpected existing word capable of becoming culturally ownable",
    "Beautiful Mischief": "90 | Self-possession, wit, and controlled rule-breaking",
    "Sensory Motion": "80 | The felt pleasure of gesture, rhythm, and movement",
    "Technical Elegance": "60 | Precision made desirable, with the laboratory left in the story rather than the name",
    "Deep Time": "50 | Depth, accumulation, and becoming more compelling through continued existence",
}
for direction, detail in world_desire.items():
    count, desire = detail.split(" | ", 1)
    lines.append(f"| {direction} | {count} | {desire} |")
lines.append("")
lines.append("## The Placek-style method stack")
lines.append("")
lines.append("All seventeen moves were distributed across the ten worlds rather than applied as one homogeneous word blender:")
lines.append("")
for i, method in enumerate(methods, 1):
    lines.append(f"{i}. {method}")
lines.append("")
lines.append("The key process intervention was the **decoy brief**: generators were naming fashion houses, private rooms, heirlooms, characters, gestures, instruments, and cultural objects—not skincare. Only after the 1,000-name set existed did the review ask whether a name could credibly carry high-performance skincare, confidence, age-positive control, and responsive expertise.")
lines.append("")
lines.append("## Funnel and screening results")
lines.append("")
lines.append(f"- Historical/conversation collision index: **{blind_audit['historical_index_count']:,} names**")
lines.append(f"- Raw normalized-unique pool: **{raw_audit['raw_unique_count']:,} names**")
lines.append("- Final blind pool: **1,000 names**, with the exact direction allocations above")
lines.append("- Post-reveal creative ratings: six criteria per name—desire, distinctiveness, fluency, stretch, bottle presence, and story ignition")
lines.append("- Federal knockout labels:")
for key in [
    "PROVISIONAL PASS",
    "YELLOW - DEAD EXACT",
    "YELLOW - LIVE NEAR",
    "AMBER - LIVE NEAR / RELEVANT",
    "AMBER - LIVE EXACT",
    "RED - LIVE EXACT / RELEVANT",
]:
    lines.append(f"  - {key}: **{screen_counts[key]}**")
lines.append("- Exact-name marketplace/web scan over the strongest 100 non-red names:")
for key in [
    "PROVISIONAL - NO OBVIOUS EXACT",
    "CAUTION - ACTIVE OTHER USE",
    "CAUTION - TRADEMARK/PRODUCT",
    "REMOVE - DIRECT BEAUTY/HEALTH",
]:
    lines.append(f"  - {key}: **{market_counts[key]}**")
lines.append("")
lines.append("## Reading the labels correctly")
lines.append("")
lines.append("- **Red / direct conflict** means eliminate from this working set.")
lines.append("- **Amber or trademark/product caution** means visible relevant risk; counsel should inspect it before enthusiasm grows.")
lines.append("- **Yellow or active other use** means a collision exists but was not an obvious same-category knockout in this basic screen.")
lines.append("- **Provisional pass / no obvious exact** means only that this limited screen did not expose an immediate issue. It does not establish availability, registrability, priority, common-law freedom, domain availability, or international clearance.")
lines.append("")
lines.append("## My read")
lines.append("")
lines.append("The most productive new territories are **Cultural Mononym** and **Beautiful Mischief**. Ricercar, Partimento, Fascicle, Better Trouble, Velvet Diversion, Polite Mischief, and Tender Detour feel less like skincare naming exercises and more like brands with an independent point of view. The strongest conventional-house options are Anvorel, Calvere, Corvenne, Brivune, Ferrore, and Elvenne; they are easier to merchandise but less conceptually surprising.")
lines.append("")
lines.append("## Legal caveat")
lines.append("")
lines.append("This is a preliminary naming screen, not legal advice or trademark clearance. Before adoption, trademark counsel should run a comprehensive search covering federal and state records, common-law use, phonetic and conceptual similarity, relevant goods/services, domains and social handles, and priority markets outside the United States.")

(ROOT / "FINAL-REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

print({
    "ranked_1000": len(ranked),
    "final50": len(final50),
    "final20": len(final20),
    "clean_early_slate": [r["Name"] for r in clean[:12]],
    "screen_counts": dict(screen_counts),
    "market_counts": dict(market_counts),
    "direction_counts": dict(direction_counts),
})
