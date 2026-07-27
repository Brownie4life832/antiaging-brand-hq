from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent

BLIND_FILES = [
    ("blind-standards.csv", 400),
    ("blind-performance.csv", 400),
    ("blind-control.csv", 400),
    ("blind-longview.csv", 350),
    ("blind-skeptic.csv", 350),
    ("blind-fewerbetter.csv", 350),
]

EXCLUDED_HISTORY_PARTS = {
    HERE.name.lower(),
    "basic-trademark-knockout-1000-2026-07-16.md",
    "trademark-screening-hits.csv",
    "trademark-screening-results.csv",
    "trademark-screening-summary.json",
    "trademark-pilot-findings.csv",
}


def normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_text = "".join(
        char for char in decomposed if not unicodedata.combining(char)
    ).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", "", ascii_text.lower())


def clean_candidate(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("**", "").replace("`", "").strip()
    value = re.sub(r"\s+", " ", value)
    return value.strip(" \t|–—-:;,.\"")


def plausible_name(value: str) -> bool:
    if not value or len(value) > 60 or len(value) < 2:
        return False
    if value.count(" ") > 7:
        return False
    lowered = value.lower()
    blocked = (
        "score",
        "method",
        "territory",
        "rationale",
        "decision",
        "candidate",
        "provisional pass",
        "live exact",
        "live near",
        "dead exact",
        "representative federal",
        "creative framework",
    )
    if any(token in lowered for token in blocked):
        return False
    if value.startswith(("#", ">", "|---")):
        return False
    if re.fullmatch(r"[\d\W_]+", value):
        return False
    return bool(re.search(r"[A-Za-z]", value))


def explicit_name_field(value: str) -> bool:
    """Use a looser gate when a source explicitly labels a column Name."""
    return bool(value and 2 <= len(value) <= 80 and re.search(r"[A-Za-z]", value))


def historical_csv_names(path: Path) -> set[str]:
    names: set[str] = set()
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames:
                return names
            by_lower = {field.lower().strip(): field for field in reader.fieldnames}
            name_field = next(
                (by_lower[key] for key in ("name", "candidate", "brand name") if key in by_lower),
                None,
            )
            if not name_field:
                return names
            for row in reader:
                value = clean_candidate(row.get(name_field, ""))
                if explicit_name_field(value):
                    names.add(value)
    except (UnicodeDecodeError, csv.Error):
        pass
    return names


def historical_text_names(path: Path) -> set[str]:
    names: set[str] = set()
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except UnicodeDecodeError:
        return names

    active_name_column: int | None = None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            active_name_column = None
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [clean_candidate(cell) for cell in stripped.strip("|").split("|")]
            header_indexes = [
                index for index, cell in enumerate(cells) if cell.lower() in {"name", "candidate", "brand name"}
            ]
            if header_indexes:
                active_name_column = header_indexes[0]
                continue
            if active_name_column is not None and active_name_column < len(cells):
                value = cells[active_name_column]
                if explicit_name_field(value):
                    names.add(value)
                continue

        patterns = [
            r"^\s*\d+[.)]\s+\*\*(.+?)\*\*(?:\s|$)",
            r"^\s*[-*+]\s+\*\*(.+?)\*\*(?:\s|$)",
            r"^\s*\d+[.)]\s+([^—–|]{2,60}?)(?:\s+[—–|]|$)",
        ]
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                value = clean_candidate(match.group(1))
                if plausible_name(value):
                    names.add(value)
                break

        if path.suffix.lower() == ".txt" and not re.search(r"[:,]", stripped):
            value = clean_candidate(re.sub(r"^\s*\d+[.)]\s*", "", stripped))
            if plausible_name(value):
                names.add(value)

    return names


def build_historical_index() -> tuple[dict[str, str], Counter]:
    indexed: dict[str, str] = {}
    source_counts: Counter = Counter()
    for path in NAMING_DIR.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".csv", ".txt"}:
            continue
        relative = path.relative_to(NAMING_DIR)
        lowered_parts = {part.lower() for part in relative.parts}
        if lowered_parts & EXCLUDED_HISTORY_PARTS:
            continue
        if path.suffix.lower() == ".csv":
            values = historical_csv_names(path)
        else:
            values = historical_text_names(path)
        for value in values:
            norm = normalize(value)
            if norm and norm not in indexed:
                indexed[norm] = f"{relative.as_posix()} :: {value}"
                source_counts[relative.as_posix()] += 1
    return indexed, source_counts


def read_blind_pool() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for filename, expected_count in BLIND_FILES:
        path = HERE / filename
        if not path.exists():
            raise FileNotFoundError(f"Missing blind pool: {path}")
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            source_rows = list(csv.DictReader(handle))
        if len(source_rows) != expected_count:
            raise ValueError(f"Expected {expected_count} rows in {filename}; found {len(source_rows)}")
        seen: set[str] = set()
        for row in source_rows:
            name = clean_candidate(row.get("Name", ""))
            norm = normalize(name)
            if not norm:
                raise ValueError(f"Empty normalized name in {filename}: {row}")
            if norm in seen:
                raise ValueError(f"Normalized duplicate inside {filename}: {name}")
            seen.add(norm)
            rows.append(
                {
                    "Name": name,
                    "Method": clean_candidate(row.get("Method", "")),
                    "DecoyBrief": clean_candidate(row.get("DecoyBrief", "")),
                    "SourceFile": filename,
                    "Normalized": norm,
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    history, history_source_counts = build_historical_index()
    raw_rows = read_blind_pool()

    survivors: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []
    blind_seen: dict[str, str] = {}
    for row in raw_rows:
        norm = row["Normalized"]
        if norm in history:
            rejected.append({**row, "RejectReason": "historical exact", "Collision": history[norm]})
            continue
        if norm in blind_seen:
            rejected.append(
                {
                    **row,
                    "RejectReason": "blind-pool duplicate",
                    "Collision": blind_seen[norm],
                }
            )
            continue
        blind_seen[norm] = row["Name"]
        survivors.append(row)

    fields = ["Name", "Method", "DecoyBrief", "SourceFile", "Normalized"]
    write_csv(HERE / "blind-pool-deduped.csv", survivors, fields)
    write_csv(
        HERE / "blind-pool-rejections.csv",
        rejected,
        fields + ["RejectReason", "Collision"],
    )

    chunks = [[], [], []]
    source_cursors: Counter = Counter()
    for row in survivors:
        source = row["SourceFile"]
        target = source_cursors[source] % 3
        source_cursors[source] += 1
        chunks[target].append(row)
    for label, rows in zip(("a", "b", "c"), chunks):
        write_csv(HERE / f"review-chunk-{label}.csv", rows, fields)

    summary = {
        "raw_blind_rows": len(raw_rows),
        "historical_normalized_index": len(history),
        "historical_exact_rejections": sum(r["RejectReason"] == "historical exact" for r in rejected),
        "blind_duplicate_rejections": sum(r["RejectReason"] == "blind-pool duplicate" for r in rejected),
        "deduped_survivors": len(survivors),
        "review_chunk_counts": {label: len(rows) for label, rows in zip(("a", "b", "c"), chunks)},
        "blind_source_counts": dict(Counter(row["SourceFile"] for row in raw_rows)),
        "survivor_source_counts": dict(Counter(row["SourceFile"] for row in survivors)),
        "largest_historical_sources": history_source_counts.most_common(15),
    }
    (HERE / "pool-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
