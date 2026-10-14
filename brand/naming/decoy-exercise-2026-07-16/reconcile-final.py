from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent


def norm(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_text = "".join(
        char for char in decomposed if not unicodedata.combining(char)
    ).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", "", ascii_text.lower())


def read(name: str) -> list[dict[str, str]]:
    with (HERE / name).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def short_note(value: str) -> str:
    words = re.sub(r"[,;:]", "", value).strip().rstrip(".").split()
    if len(words) < 3:
        words.extend(["master", "brand", "potential"][: 3 - len(words)])
    return " ".join(words[:12])


def main() -> None:
    pool_rows = read("reviewed-pool-screen.csv")
    pool = {norm(row["Name"]): row for row in pool_rows}
    shortlist = read("independent-shortlist.csv")
    champions = read("champion-list.csv")
    audit = read("adversarial-cuts.csv")

    cut = {norm(row["Name"]): row["Reason"] for row in audit if row["Severity"] == "CUT"}
    demote = {norm(row["Name"]): row["Reason"] for row in audit if row["Severity"] == "DEMOTE"}
    champion = {
        norm(row["Name"]): {
            "rank": int(row["ChampionRank"]),
            "reason": row["ChampionReason"],
        }
        for row in champions
    }
    draft = {
        norm(row["Name"]): {
            "rank": int(row["DraftRank"]),
            "reason": row["ShortlistReason"],
        }
        for row in shortlist
    }

    candidates = [row for row in shortlist if norm(row["Name"]) not in cut]
    if len(candidates) != 258:
        raise ValueError(f"Expected 258 shortlist rows after CUT exclusions; found {len(candidates)}")

    screen_penalty = {
        "PROVISIONAL PASS": 0.0,
        "YELLOW - DEAD EXACT": 0.25,
        "YELLOW - LIVE NEAR": 0.4,
        "AMBER - LIVE EXACT": 0.7,
        "AMBER - LIVE NEAR / RELEVANT": 0.9,
    }

    def keep_score(row: dict[str, str]) -> float:
        key = norm(row["Name"])
        source = pool[key]
        value = float(source["Score"]) * 10
        value -= screen_penalty[source["Decision"]] * 4
        value += max(0, 3.0 - draft[key]["rank"] / 100)
        if key in champion:
            value += 10 + max(0, 4.0 - champion[key]["rank"] / 25)
        if key in demote:
            value -= 5
        risk = source["Risk"].lower()
        if any(term in risk for term in ("campaign", "generic", "meaning stretch", "abstract")):
            value -= 1.25
        return value

    working = candidates[:]
    removed: list[dict[str, str]] = []
    while len(working) > 250:
        world_counts = Counter(pool[norm(row["Name"])]["World"] for row in working)
        decoy_counts = Counter(pool[norm(row["Name"])]["DecoyBrief"] for row in working)
        eligible = []
        for row in working:
            key = norm(row["Name"])
            source = pool[key]
            if key in champion:
                continue
            if world_counts[source["World"]] <= 35:
                continue
            if decoy_counts[source["DecoyBrief"]] <= 25:
                continue
            eligible.append(row)
        if not eligible:
            raise RuntimeError("Balance constraints left no eligible final removal")
        weakest = min(eligible, key=lambda row: (keep_score(row), -draft[norm(row["Name"])]["rank"]))
        working.remove(weakest)
        removed.append(weakest)

    provisional_champions = sorted(
        (
            row
            for row in working
            if norm(row["Name"]) in champion
            and pool[norm(row["Name"])]["Decision"] == "PROVISIONAL PASS"
        ),
        key=lambda row: champion[norm(row["Name"])]["rank"],
    )
    caution_champions = sorted(
        (
            row
            for row in working
            if norm(row["Name"]) in champion
            and pool[norm(row["Name"])]["Decision"] != "PROVISIONAL PASS"
        ),
        key=lambda row: champion[norm(row["Name"])]["rank"],
    )
    nonchampions = sorted(
        (row for row in working if norm(row["Name"]) not in champion),
        key=lambda row: (
            -float(pool[norm(row["Name"])]["Score"]),
            screen_penalty[pool[norm(row["Name"])]["Decision"]],
            draft[norm(row["Name"])]["rank"],
        ),
    )

    # Keep top 30 entirely provisional, then restore remaining champion ordering.
    top = provisional_champions[:30]
    used = {norm(row["Name"]) for row in top}
    rest = sorted(
        [row for row in working if norm(row["Name"]) not in used],
        key=lambda row: (
            0 if norm(row["Name"]) in champion else 1,
            champion.get(norm(row["Name"]), {"rank": 10_000})["rank"],
            -float(pool[norm(row["Name"])]["Score"]),
            screen_penalty[pool[norm(row["Name"])]["Decision"]],
            draft[norm(row["Name"])]["rank"],
        ),
    )
    ordered = top + rest
    if len(ordered) != 250 or len({norm(row["Name"]) for row in ordered}) != 250:
        raise ValueError("Final ordering is not 250 unique rows")

    output_rows = []
    for rank, row in enumerate(ordered, start=1):
        key = norm(row["Name"])
        reason = champion[key]["reason"] if key in champion else draft[key]["reason"]
        output_rows.append(
            {
                "Rank": rank,
                "Name": pool[key]["Name"],
                "FinalNote": short_note(reason),
            }
        )
    with (HERE / "final-selection.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Rank", "Name", "FinalNote"])
        writer.writeheader()
        writer.writerows(output_rows)

    selected_keys = {norm(row["Name"]) for row in output_rows}
    selected_sources = [pool[key] for key in selected_keys]
    summary = {
        "candidate_start": len(candidates),
        "final_count": len(output_rows),
        "removed_final_eight": [pool[norm(row["Name"])]["Name"] for row in removed],
        "champion_survivors": sum(key in champion for key in selected_keys),
        "demote_survivors": sum(key in demote for key in selected_keys),
        "world_counts": dict(Counter(row["World"] for row in selected_sources)),
        "decoy_counts": dict(Counter(row["DecoyBrief"] for row in selected_sources)),
        "decision_counts": dict(Counter(row["Decision"] for row in selected_sources)),
        "top_30_all_provisional": all(
            pool[norm(row["Name"])]["Decision"] == "PROVISIONAL PASS" for row in output_rows[:30]
        ),
        "red_count": sum(row["Decision"].startswith("RED") for row in selected_sources),
        "cut_count": sum(key in cut for key in selected_keys),
    }
    (HERE / "final-reconcile-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
