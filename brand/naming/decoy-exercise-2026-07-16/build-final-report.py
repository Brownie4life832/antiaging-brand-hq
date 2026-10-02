from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
FINAL_SELECTION = HERE / "final-selection.csv"
SCREENED_POOL = HERE / "reviewed-pool-screen.csv"
OUTPUT_CSV = HERE / "decoy-final-250.csv"
OUTPUT_REPORT = HERE.parent / "decoy-250-2026-07-16.md"


def normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_text = "".join(
        char for char in decomposed if not unicodedata.combining(char)
    ).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", "", ascii_text.lower())


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def md(value: object) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def counts_line(counter: Counter) -> str:
    return "; ".join(f"{md(key)} {value}" for key, value in counter.most_common())


def main() -> None:
    pool_rows = read_csv(SCREENED_POOL)
    pool = {normalize(row["Name"]): row for row in pool_rows}
    selection = read_csv(FINAL_SELECTION)
    if len(selection) != 250:
        raise ValueError(f"Expected 250 final selections; found {len(selection)}")

    final_rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for expected_rank, selected in enumerate(selection, start=1):
        rank = int(selected.get("Rank", "0"))
        if rank != expected_rank:
            raise ValueError(f"Expected rank {expected_rank}; found {rank}")
        norm = normalize(selected.get("Name", ""))
        if norm not in pool:
            raise ValueError(f"Final name not present in screened pool: {selected.get('Name')}")
        if norm in seen:
            raise ValueError(f"Duplicate final name: {selected.get('Name')}")
        seen.add(norm)
        source = pool[norm]
        final_rows.append(
            {
                "Rank": str(rank),
                "Name": source["Name"],
                "Score": source["Score"],
                "World": source["World"],
                "Hook": source["Hook"],
                "FinalNote": selected.get("FinalNote", "").strip(),
                "Risk": source["Risk"],
                "Method": source["Method"],
                "DecoyBrief": source["DecoyBrief"],
                "Decision": source["Decision"],
                "DecisionReason": source["DecisionReason"],
                "LiveExact": source["LiveExact"],
                "LiveNear1": source["LiveNear1"],
                "DeadOrUnknownExact": source["DeadOrUnknownExact"],
                "RepresentativeHits": source["RepresentativeHits"],
                "Normalized": norm,
            }
        )

    fields = list(final_rows[0])
    with OUTPUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(final_rows)

    pool_audit = json.loads((HERE / "pool-audit.json").read_text(encoding="utf-8"))
    review_audit = json.loads((HERE / "review-audit.json").read_text(encoding="utf-8"))
    screen_audit = json.loads((HERE / "reviewed-pool-screen-summary.json").read_text(encoding="utf-8"))
    world_counts = Counter(row["World"] for row in final_rows)
    decoy_counts = Counter(row["DecoyBrief"] for row in final_rows)
    method_counts = Counter(row["Method"] for row in final_rows)
    decision_counts = Counter(row["Decision"] for row in final_rows)

    lines = [
        "# 250 net-new skincare master-brand names from the blind decoy exercise",
        "",
        "> These names were generated without revealing the skincare category, deduplicated against the project's broad historical corpus, reviewed only after the category reveal, and then compared mechanically with a local USPTO-derived federal corpus. Creative scores and knockout labels are not legal clearance opinions.",
        "",
        "## What was different this time",
        "",
        "Six off-category briefs were used to escape the naming language already overrepresented in the project: a living professional standard, a three-model performance company, a calm decision tool, a long-view cultural membership, an entertaining skeptic, and a radically focused essentials company. The teams generated names blind. Only after generation and exact historical deduplication did reviewers learn that the real category was skincare.",
        "",
        "The reveal tested each name against three confidence layers—confidence in the product, confidence in yourself and aging, and confidence in your own decisions—and six strategic worlds: Earned Confidence, The Long View, The Living Standard, Beauty for Skeptics, On Your Terms, and Performance Without Theater.",
        "",
        "## Funnel",
        "",
        f"- Blind names generated: **{pool_audit['raw_blind_rows']:,}**",
        f"- Historical normalized name index: **{pool_audit['historical_normalized_index']:,}**",
        f"- Historical exact collisions removed: **{pool_audit['historical_exact_rejections']:,}**",
        f"- Blind-pool duplicates removed: **{pool_audit['blind_duplicate_rejections']:,}**",
        f"- Net-new names category-reviewed: **{pool_audit['deduped_survivors']:,}**",
        f"- Reveal-review survivors rated 8.0+: **{review_audit['reviewed_survivors']:,}**",
        f"- USPTO-derived records compared: **{screen_audit['corpus_distinct_serials']:,} distinct serials**, source records through **{screen_audit['corpus_latest_source_date']}**",
        f"- Final curated set: **{len(final_rows):,}**",
        "",
        "## Final-set balance",
        "",
        f"- Strategic worlds: {counts_line(world_counts)}",
        f"- Blind source briefs: {counts_line(decoy_counts)}",
        f"- Creative construction methods: {counts_line(method_counts)}",
        f"- Mechanical screen labels: {counts_line(decision_counts)}",
        "",
        "## Top 30",
        "",
        "| Rank | Name | Score | World | Why it survived | Knockout label |",
        "|---:|---|---:|---|---|---|",
    ]
    for row in final_rows[:30]:
        lines.append(
            f"| {row['Rank']} | {md(row['Name'])} | {float(row['Score']):.1f} | {md(row['World'])} | {md(row['FinalNote'] or row['Hook'])} | {md(row['Decision'])} |"
        )

    lines.extend(
        [
            "",
            "## All 250",
            "",
            "| Rank | Name | Score | World | Blind brief | Method | Naming story | Knockout label |",
            "|---:|---|---:|---|---|---|---|---|",
        ]
    )
    for row in final_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["Rank"],
                    md(row["Name"]),
                    f"{float(row['Score']):.1f}",
                    md(row["World"]),
                    md(row["DecoyBrief"]),
                    md(row["Method"]),
                    md(row["Hook"]),
                    md(row["Decision"]),
                ]
            )
            + " |"
        )

    issue_rows = [
        row
        for row in final_rows
        if row["Decision"] != "PROVISIONAL PASS" and row["RepresentativeHits"]
    ]
    lines.extend(
        [
            "",
            "## Mechanical knockout issues retained for visibility",
            "",
            "The final creative set prioritizes names that survived the basic screen. Any non-pass retained below remains a creative option only and should not advance without a closer search. A dead federal record can coexist with common-law use.",
            "",
            "| Name | Label | Reason | Representative federal records |",
            "|---|---|---|---|",
        ]
    )
    for row in issue_rows:
        lines.append(
            f"| {md(row['Name'])} | {md(row['Decision'])} | {md(row['DecisionReason'])} | {md(row['RepresentativeHits'])} |"
        )

    lines.extend(
        [
            "",
            "## What the screen does and does not mean",
            "",
            "Exact normalized identity ignored case, spaces, punctuation, apostrophes, and diacritics. Compact names 5–18 characters long also received a one-character insertion, deletion, substitution, and adjacent-transposition check. Relevant active classes were 003, 005, 010, 021, 035, and 044.",
            "",
            "This is a narrow, non-legal knockout—not clearance. It does not fully evaluate phonetic, semantic, or commercial-impression similarity; common-law and state use; domains and handles; foreign registers; ownership strategy; or likelihood of confusion. Before adopting a finalist, trademark counsel should run a comprehensive search and the live register should be checked again immediately before filing.",
            "",
        ]
    )
    OUTPUT_REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(
        json.dumps(
            {
                "final_count": len(final_rows),
                "output_csv": str(OUTPUT_CSV),
                "output_report": str(OUTPUT_REPORT),
                "world_counts": dict(world_counts),
                "decision_counts": dict(decision_counts),
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
