from __future__ import annotations

import csv
import json
import re
import unicodedata
from pathlib import Path


HERE = Path(__file__).resolve().parent
RATINGS = HERE / "all-names-cohesive-ratings.csv"
FEDERAL = HERE / "master-federal-screen.csv"
MASTER_OUTPUT = HERE / "MASTER-13271-RATED.csv"
SCREENED_OUTPUT = HERE / "TOP-397-ABOVE-8-SCREENED.csv"
PASS_OUTPUT = HERE / "ABOVE-8-PRELIMINARY-FEDERAL-PASSES.csv"
DEEP_OUTPUT = HERE / "KNOWN-DEEP-SCREEN-RESULTS.csv"
SUMMARY = HERE / "screened-ranking-summary.json"


# A small number of names were researched beyond the automated exact/edit-1
# knockout.  These notes prevent a basic federal pass from being read as a
# broader clearance opinion.  All other names remain explicitly unreviewed at
# the deeper-search layer.
DEEP_SCREEN_NOTES = {
    "noasterisk": (
        "AMBER — broader federal component conflicts",
        "Live ASTERISK-family records surfaced, including Classes 010 and 035/042.",
    ),
    "standbyit": (
        "AMBER — broader federal phrase-family conflicts",
        "STAND BY / STANDBY records surfaced in relevant classes, including WE STAND BY OUR PRODUCTS in Classes 003/005/010.",
    ),
    "putplainly": (
        "AMBER — broader federal dominant-word conflict",
        "PLAINLY EARTH is live in Class 003, creating a material category/dominant-word issue.",
    ),
    "plainproof": (
        "RED — active exact common-law use found",
        "An active PlainProof health-analytics business was found outside the federal exact-mark knockout.",
    ),
    "nofootnote": (
        "AMBER — beauty-category phrase use found",
        "INIKA Organic has used 'no footnotes, no asterisks' descriptively in beauty copy.",
    ),
    "nofootnotes": (
        "AMBER — beauty-category phrase use found",
        "INIKA Organic has used 'no footnotes, no asterisks' descriptively in beauty copy.",
    ),
    "nosmallprint": (
        "AMBER — skincare-category phrase use found",
        "Made Simple Skincare has used the phrase descriptively; strength and common-law context need review.",
    ),
    "showthework": (
        "AMBER — common/category phrase use found",
        "The phrase appears in category and explanatory copy; exclusivity and common-law use need review.",
    ),
    "sureenough": (
        "PRELIMINARY GREEN — broader federal pass",
        "No broader relevant federal conflict surfaced; one unrelated SHO'NUFF popcorn record appeared.",
    ),
    "nomystery": (
        "PRELIMINARY GREEN — broader federal pass",
        "No broader relevant federal conflict surfaced, though the phrase is used descriptively in skincare/wellness copy.",
    ),
    "plaintosee": (
        "PRELIMINARY GREEN — broader federal pass",
        "No broader relevant federal conflict surfaced; ordinary/descriptive phrase strength still needs counsel review.",
    ),
    "inwriting": (
        "PRELIMINARY GREEN — broader federal pass",
        "No broader relevant federal conflict surfaced; ordinary-phrase strength still needs counsel review.",
    ),
    "spelledout": (
        "PRELIMINARY GREEN — broader federal pass",
        "No broader relevant federal conflict surfaced; ordinary-phrase strength still needs counsel review.",
    ),
    "withreason": (
        "PRELIMINARY GREEN — broader federal pass",
        "No broader relevant federal conflict surfaced; ordinary-phrase strength still needs counsel review.",
    ),
}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.lower())


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    ratings = read_rows(RATINGS)
    federal = read_rows(FEDERAL)
    federal_by_norm = {normalize(row["name"]): row for row in federal}

    federal_fields = [
        "federal_screen_scope",
        "federal_decision",
        "federal_reason",
        "live_exact_count",
        "live_near_count",
        "dead_or_unknown_exact_count",
        "all_hit_count",
        "representative_hits",
        "deeper_screen_status",
        "deeper_screen_note",
        "decision_readout",
    ]
    output_rows: list[dict[str, object]] = []
    screened_rows: list[dict[str, object]] = []
    pass_rows: list[dict[str, object]] = []

    for rating in ratings:
        score = float(rating["cohesive_rating_10"])
        row: dict[str, object] = dict(rating)
        if score > 8.0:
            hit = federal_by_norm.get(rating["normalized"])
            if hit is None:
                raise RuntimeError(f"Missing federal result for {rating['name']}")
            row.update(
                {
                    "federal_screen_scope": "U.S. normalized exact + edit-distance-one; local corpus through 2026-07-06",
                    "federal_decision": hit["decision"],
                    "federal_reason": hit["reason"],
                    "live_exact_count": hit["live_exact_count"],
                    "live_near_count": hit["live_near_count"],
                    "dead_or_unknown_exact_count": hit["dead_or_unknown_exact_count"],
                    "all_hit_count": hit["all_hit_count"],
                    "representative_hits": hit["representative_hits"],
                }
            )
            deep_status, deep_note = DEEP_SCREEN_NOTES.get(
                rating["normalized"],
                (
                    "NOT DEEP-SCREENED",
                    "Only the automated federal exact/edit-distance-one knockout has been completed.",
                ),
            )
            row["deeper_screen_status"] = deep_status
            row["deeper_screen_note"] = deep_note
            if deep_status.startswith("RED") or deep_status.startswith("AMBER"):
                row["decision_readout"] = "DO NOT TREAT AS CLEAR; resolve the identified issue before advancing"
            elif deep_status.startswith("PRELIMINARY GREEN"):
                row["decision_readout"] = "ADVANCEABLE TO COMPREHENSIVE COUNSEL SEARCH; not legally cleared"
            elif hit["decision"] == "PROVISIONAL PASS":
                row["decision_readout"] = "BASIC FEDERAL PASS ONLY; deeper search still required"
            else:
                row["decision_readout"] = "FEDERAL KNOCKOUT ISSUE; review before advancing"
            screened_rows.append(row)
            if hit["decision"] == "PROVISIONAL PASS":
                pass_rows.append(row)
        else:
            row.update(
                {
                    "federal_screen_scope": "Not included in >8.0 screening cohort",
                    "federal_decision": "NOT SCREENED IN DECISION COHORT",
                    "federal_reason": "Creative rating did not exceed 8.0",
                    "live_exact_count": "",
                    "live_near_count": "",
                    "dead_or_unknown_exact_count": "",
                    "all_hit_count": "",
                    "representative_hits": "",
                    "deeper_screen_status": "NOT PERFORMED",
                    "deeper_screen_note": "Creative rating did not exceed 8.0.",
                    "decision_readout": "CREATIVE REVIEW ONLY",
                }
            )
        output_rows.append(row)

    fields = list(ratings[0].keys()) + federal_fields
    write_rows(MASTER_OUTPUT, output_rows, fields)
    write_rows(SCREENED_OUTPUT, screened_rows, fields)
    write_rows(PASS_OUTPUT, pass_rows, fields)
    deep_rows = [
        row for row in screened_rows if row["deeper_screen_status"] != "NOT DEEP-SCREENED"
    ]
    write_rows(DEEP_OUTPUT, deep_rows, fields)

    decisions: dict[str, int] = {}
    for row in screened_rows:
        decision = str(row["federal_decision"])
        decisions[decision] = decisions.get(decision, 0) + 1

    summary = {
        "total_rated_names": len(ratings),
        "creative_score_threshold": "> 8.0",
        "screened_cohort_count": len(screened_rows),
        "preliminary_federal_pass_count": len(pass_rows),
        "known_deeper_screen_count": len(deep_rows),
        "known_deeper_green_count": sum(
            str(row["deeper_screen_status"]).startswith("PRELIMINARY GREEN")
            for row in deep_rows
        ),
        "screened_decision_counts": dict(
            sorted(decisions.items(), key=lambda item: (-item[1], item[0]))
        ),
        "legal_status": "Preliminary federal knockout only; not final trademark clearance.",
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print("\nTop 30 preliminary federal passes:")
    for row in pass_rows[:30]:
        print(
            f"{int(row['master_rank']):>4}  {float(row['cohesive_rating_10']):>4.2f}  "
            f"{row['name']}"
        )


if __name__ == "__main__":
    main()
