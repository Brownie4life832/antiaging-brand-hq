from __future__ import annotations

import csv
import json
import re
import statistics
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAMING = HERE.parent
OUTPUT = HERE / "master-universe.csv"
SUMMARY = HERE / "master-universe-summary.json"


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.lower())


def clean_name(value: str) -> str:
    value = value.strip().strip("`*_ ")
    value = re.sub(r"\s+", " ", value)
    return value


def repair_mojibake(value: str) -> str:
    if not any(marker in value for marker in ("Ã", "â", "Â")):
        return value
    try:
        repaired = value.encode("latin-1").decode("utf-8")
        return repaired if repaired else value
    except (UnicodeEncodeError, UnicodeDecodeError):
        return value


def as_float(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


@dataclass
class Candidate:
    name: str
    norm: str
    sources: set[str] = field(default_factory=set)
    source_files: set[str] = field(default_factory=set)
    contexts: set[str] = field(default_factory=set)
    scores: list[float] = field(default_factory=list)


pool: dict[str, Candidate] = {}
source_row_counts: defaultdict[str, int] = defaultdict(int)


def add_candidate(
    name: str,
    source: str,
    source_file: str,
    score: float | None = None,
    context: str | None = None,
) -> None:
    name = clean_name(repair_mojibake(name))
    norm = normalize(name)
    if not name or not norm or len(name) > 80:
        return
    if norm not in pool:
        pool[norm] = Candidate(name=name, norm=norm)
    candidate = pool[norm]
    # Prefer the cleanest display spelling when duplicates differ only by mojibake.
    if sum(candidate.name.count(x) for x in ("Ã", "â", "Â")) > sum(
        name.count(x) for x in ("Ã", "â", "Â")
    ):
        candidate.name = name
    candidate.sources.add(source)
    candidate.source_files.add(source_file)
    if context:
        candidate.contexts.add(clean_name(context))
    if score is not None:
        candidate.scores.append(score)
    source_row_counts[source] += 1


def read_csv_source(
    rel_path: str,
    source: str,
    name_field: str,
    score_field: str | None = None,
    context_fields: tuple[str, ...] = (),
) -> None:
    path = NAMING / rel_path
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            context = " / ".join(
                value
                for field_name in context_fields
                if (value := (row.get(field_name) or "").strip())
            )
            add_candidate(
                row.get(name_field, ""),
                source,
                rel_path,
                as_float(row.get(score_field)) if score_field else None,
                context,
            )


read_csv_source(
    "core-worlds-depth-2026-07-16/deduped-rated-pool.csv",
    "Core Worlds Round 1",
    "Name",
    "CreativeRating",
    ("World", "Exercise", "Form", "CreativeDecision", "CreativeRisk"),
)
read_csv_source(
    "core-worlds-depth-round2-2026-07-16/deduped-rated-pool.csv",
    "Core Worlds Round 2",
    "Name",
    "CreativeRating",
    ("World", "Exercise", "Form", "CreativeDecision", "CreativeRisk"),
)
read_csv_source(
    "desire-first-1000-2026-07-16/screened-1000.csv",
    "Desire First 1000",
    "Name",
    "CreativeScore",
    ("Direction", "Method", "SourceWorld", "RevealDecision", "CreativeRisk"),
)
read_csv_source(
    "decoy-exercise-2026-07-16/reviewed-pool-screen.csv",
    "Decoy Review",
    "Name",
    "Score",
    ("World", "Hook", "Risk", "Method", "Reviewer"),
)
read_csv_source(
    "skin-capability-round-2026-07-16/deduped-pool.csv",
    "Skin Capability",
    "Name",
    None,
    ("World", "ExerciseName", "Form"),
)
read_csv_source(
    "straightup-exploration-2026-07-16/candidate-pool.csv",
    "StraightUp Exploration",
    "name",
    None,
    ("lane",),
)


def parse_basic_federal_report() -> None:
    rel_path = "basic-trademark-knockout-1000-2026-07-16.md"
    path = NAMING / rel_path
    pattern = re.compile(
        r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(\d+(?:\.\d+)?)\s*\|\s*(.*?)\s*\|"
    )
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        wave, number, name, score, _decision = match.groups()
        add_candidate(
            name,
            "Net-New Federal 1000",
            rel_path,
            float(score),
            f"Wave {wave} / #{number}",
        )


def parse_legacy_top500() -> None:
    rel_path = "name-longlist-top500-2026-06-19.md"
    path = NAMING / rel_path
    pattern = re.compile(
        r"^\|\s*\*\*(.*?)\*\*\s*\|\s*(\d+(?:\.\d+)?)\s*\|"
    )
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            add_candidate(
                match.group(1),
                "Legacy Top 500",
                rel_path,
                float(match.group(2)),
                "June 2026 legacy longlist",
            )


def parse_bold_table_first_column(rel_path: str, source: str) -> None:
    path = NAMING / rel_path
    pattern = re.compile(r"^\|\s*\*\*(.*?)\*\*\s*\|")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            name = match.group(1)
            if name.lower() not in {"name", "candidate", "strategy", "type"}:
                add_candidate(name, source, rel_path, None, "Curated legacy table")


def parse_final_blind_pool() -> None:
    rel_path = "final-exercise-2026-07-16/03-blind-pool.md"
    path = NAMING / rel_path
    pattern = re.compile(r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match and match.group(1).isdigit():
            add_candidate(
                match.group(2),
                "Final Blind Pool",
                rel_path,
                None,
                f"Blind pool #{match.group(1)}",
            )


parse_basic_federal_report()
parse_legacy_top500()
parse_bold_table_first_column(
    "name-candidates-v2-fullmethod-2026-06-19.md", "Legacy Curated 106"
)
parse_bold_table_first_column(
    "name-candidates-2026-06-19.md", "Legacy First-Pass 100"
)
parse_final_blind_pool()


rows: list[dict[str, object]] = []
for candidate in pool.values():
    mean_score = statistics.mean(candidate.scores) if candidate.scores else None
    max_score = max(candidate.scores) if candidate.scores else None
    rows.append(
        {
            "name": candidate.name,
            "normalized": candidate.norm,
            "source_count": len(candidate.sources),
            "sources": "; ".join(sorted(candidate.sources)),
            "source_files": "; ".join(sorted(candidate.source_files)),
            "source_contexts": "; ".join(sorted(candidate.contexts))[:2000],
            "source_score_count": len(candidate.scores),
            "source_score_mean": f"{mean_score:.3f}" if mean_score is not None else "",
            "source_score_max": f"{max_score:.3f}" if max_score is not None else "",
        }
    )

rows.sort(
    key=lambda row: (
        -int(row["source_count"]),
        -(float(row["source_score_max"]) if row["source_score_max"] != "" else -1),
        str(row["name"]).lower(),
    )
)

with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

summary = {
    "source_row_counts": dict(sorted(source_row_counts.items())),
    "input_row_count": sum(source_row_counts.values()),
    "unique_normalized_candidate_count": len(rows),
    "duplicate_rows_collapsed": sum(source_row_counts.values()) - len(rows),
    "candidates_with_any_source_score": sum(
        1 for row in rows if row["source_score_count"]
    ),
}
SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2))
