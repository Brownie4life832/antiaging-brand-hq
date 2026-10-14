import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent

# Deliberate human curation after the blind creative score, federal knockout,
# and exact-name marketplace scan. Scores express naming potential, not legal certainty.
FINALISTS = [
    ("Ricercar", 9.3),
    ("Anvorel", 9.2),
    ("Calvere", 9.1),
    ("Corvenne", 9.0),
    ("Brivune", 9.0),
    ("Dorevan", 8.9),
    ("Elverin", 8.9),
    ("Ferrore", 8.8),
    ("Elvenne", 8.8),
    ("Partimento", 8.8),
    ("Hollismere", 8.7),
    ("Fascicle", 8.7),
    ("Better Trouble", 8.7),
    ("Velvet Diversion", 8.6),
    ("Polite Mischief", 8.6),
    ("Tender Detour", 8.6),
    ("Asterel", 8.5),
    ("Evrel", 8.5),
    ("Brevier", 8.5),
    ("Layerwork", 8.5),
    ("Toccata", 8.4),
    ("Contrarywise", 8.4),
    ("Attacca", 8.4),
    ("Ligature", 8.4),
    ("Winter Portico", 8.4),
    ("Abrin", 8.3),
    ("Uruva", 8.3),
    ("Alderen", 8.3),
    ("Alvarel", 8.3),
    ("Ravellen", 8.3),
    ("Ardelin", 8.2),
    ("Ciodor", 8.2),
    ("Navelin", 8.2),
    ("Cavrel", 8.2),
    ("Acroterion", 8.2),
    ("Ravenmere", 8.1),
    ("Quiet Landing", 8.1),
    ("Private Filigree", 8.1),
    ("Honest Exception", 8.1),
    ("Rare Behavior", 8.1),
    ("Rare Nerve", 8.0),
    ("Vivid Gesture", 8.0),
    ("True Tremor", 8.0),
    ("Henceforward", 8.0),
    ("Wild Armature", 8.0),
    ("Deep Calendar", 8.0),
    ("Supposedly", 8.0),
    ("Undulate", 8.0),
    ("Valewell", 8.0),
    ("Ambergate", 8.0),
]

CURATOR_RATIONALE = {
    "Ricercar": "A musical form whose name carries the idea of seeking: constant research expressed as culture, not laboratory language.",
    "Anvorel": "Immediate house-name authority; it can make rigorous skincare feel established, desirable, and expansive.",
    "Calvere": "Controlled, elegant, and intellectually cool; a strong vessel for confidence without youth language.",
    "Corvenne": "A darker couture cadence that feels decisive and memorable on a very simple bottle.",
    "Brivune": "Compact invented sound with energy and restraint; meaning can be built entirely around the brand's behavior.",
    "Dorevan": "Familiar enough to pronounce instantly, unfamiliar enough to feel like a founderless European house.",
    "Elverin": "Precise and stately rather than soft or spa-like; it gives technical credibility a human surface.",
    "Ferrore": "A strong, warm sound with a material undertone; confident without becoming aggressive or clinical.",
    "Elvenne": "Quietly feminine and high-finish without fragility, fantasy language, or explicit category cues.",
    "Partimento": "A musical method that turns a reliable foundation into fluent performance—an unusually apt story for the standard routine.",
    "Hollismere": "Creates a complete private world around the customer; expertise can feel intimate rather than institutional.",
    "Fascicle": "A small collected section or bundle; it can frame the line as a concise body of essential knowledge and products.",
    "Better Trouble": "Confident skepticism in two words: challenge beauty theater, keep the genuinely useful parts.",
    "Velvet Diversion": "Sensory pleasure collides with intelligent nonconformity; highly distinctive, editorial, and display-worthy.",
    "Polite Mischief": "The clearest expression of responsible rule-breaking: contrarian about claims, rigorous about products.",
    "Tender Detour": "An age-positive alternative path with warmth; it rejects correction language without rejecting performance.",
    "Asterel": "Poised, luminous house cadence with enough abstraction to support future research-led launches.",
    "Evrel": "Very short, fluent, and visually clean; a nearly empty vessel that can acquire trust through proof.",
    "Brevier": "Suggests a concise compendium: a small, edited routine containing only what earns its place.",
    "Layerwork": "Makes consistency and accumulation the hero—exactly the bridge between a standard routine and emerging technology.",
}


def index_csv(filename):
    with (ROOT / filename).open(encoding="utf-8-sig", newline="") as f:
        return {row["Name"]: row for row in csv.DictReader(f)}


creative = index_csv("top-100-marketplace-input.csv")
market = index_csv("marketplace-search-results.csv")

fields = [
    "FinalRank", "Name", "CuratorScore", "CuratorRationale", "Direction", "CreativeScore", "Hook",
    "TrademarkDecision", "TrademarkReason", "RepresentativeHits",
    "MarketplaceDecision", "MarketplaceReason", "TopExactSearchResult", "EvidenceURL",
]

rows = []
for rank, (name, score) in enumerate(FINALISTS, start=1):
    c = creative[name]
    m = market[name]
    rows.append({
        "FinalRank": rank,
        "Name": name,
        "CuratorScore": f"{score:.1f}",
        "CuratorRationale": CURATOR_RATIONALE.get(name, c["Hook"]),
        "Direction": c["Direction"],
        "CreativeScore": c["CreativeScore"],
        "Hook": c["Hook"],
        "TrademarkDecision": c["TrademarkDecision"],
        "TrademarkReason": c["TrademarkReason"],
        "RepresentativeHits": c["RepresentativeHits"],
        "MarketplaceDecision": m["MarketplaceDecision"],
        "MarketplaceReason": m["MarketplaceReason"],
        "TopExactSearchResult": m["TopExactSearchResult"],
        "EvidenceURL": m["EvidenceURL"],
    })

for filename, subset in (("finalists-50.csv", rows), ("finalists-20.csv", rows[:20])):
    with (ROOT / filename).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(subset)

print({
    "top50": len(rows),
    "top20": len(rows[:20]),
    "top20_directions": sorted({r["Direction"] for r in rows[:20]}),
    "top20_marketplace": {d: sum(r["MarketplaceDecision"] == d for r in rows[:20]) for d in sorted({r["MarketplaceDecision"] for r in rows[:20]})},
})
