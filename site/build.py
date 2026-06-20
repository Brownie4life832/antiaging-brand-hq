#!/usr/bin/env python3
"""Build the research explorer site.

Parses research/ingredients/_EVIDENCE-MATRIX.md for per-ingredient metadata and
renders every research markdown file to HTML. Emits:
  - site/data.js   : lightweight index (table metadata + doc index) — loads instantly
  - site/docs/<slug>.html : one rendered fragment per dossier, fetched lazily on click

Serve the site/ folder (any static server, the preview, or GitHub Pages) — the
dossier fragments are fetched at runtime, so double-clicking index.html via file://
in Chrome will show the table but block the dossier fetches.

Run:  python site/build.py
"""
import json
import re
import datetime
import shutil
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
ING = ROOT / "research" / "ingredients"
COMP = ROOT / "research" / "competitors"
MARKET = ROOT / "research" / "market"
TRENDS = ROOT / "research" / "trends"
SCIENCE = ROOT / "research" / "science"
PRODUCTS = ROOT / "products"
BRAND = ROOT / "brand"
SITE = ROOT / "site"
DOCS = SITE / "docs"

MD_EXT = ["tables", "fenced_code", "sane_lists"]
LINK_RE = re.compile(r'href="([^"]*?/)?([^"/]+?)\.md(#[^"]*)?"')
H1_RE = re.compile(r'^#\s+(.+)$')
CELL_LINK = re.compile(r'\[(.+?)\]\(([^)]+?)\.md[^)]*\)')
NUM_RE = re.compile(r'^\d+$')

GRADE_RANK = {"A": 0, "A-": 1, "B+": 2, "B": 3, "B-": 4, "C+": 5, "C": 6,
              "C-": 7, "D+": 8, "D": 9, "D-": 10, "F": 11}
VERDICT = {"✅": "shortlist", "⚠️": "conditional", "❌": "skip"}


def norm_grade(g):
    return g.replace("−", "-").replace("*", "").strip()


def grade_rank(g):
    return GRADE_RANK.get(norm_grade(g), 99)


def grade_bucket(g):
    n = norm_grade(g)
    if n[:1] in ("A", "B"):
        return "strong"
    if n[:1] == "C":
        return "moderate"
    if n[:1] in ("D", "F"):
        return "weak"
    return "unknown"


def md_to_html(text):
    return LINK_RE.sub(lambda m: f'href="javascript:void(0)" data-doc="{m.group(2)}"',
                       markdown.markdown(text, extensions=MD_EXT))


def title_of(text, fallback):
    for line in text.splitlines():
        m = H1_RE.match(line.strip())
        if m:
            return m.group(1).strip()
    return fallback


def parse_matrix():
    meta = {}
    f = ING / "_EVIDENCE-MATRIX.md"
    if not f.exists():
        return meta
    for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if len(cols) < 8 or not NUM_RE.match(cols[0]):
            continue
        m = CELL_LINK.search(cols[1])
        if not m:
            continue
        name, slug = m.group(1), m.group(2)
        g = norm_grade(cols[6])
        verd = cols[7].strip()
        meta[slug] = {"name": name, "cls": cols[2], "relevance": cols[3], "tier": cols[4],
                      "viability": cols[5], "viabilityShort": cols[5].split("(")[0].strip(),
                      "grade": g, "gradeRank": grade_rank(g), "gradeBucket": grade_bucket(g),
                      "verdict": verd, "verdictLabel": VERDICT.get(verd, verd)}
    return meta


def collect(folder, extra_skip=()):
    if not folder.exists():
        return []
    return [p for p in sorted(folder.glob("*.md"))
            if not p.name.startswith("_") and p.stem.lower() != "readme" and p.stem not in extra_skip]


def write_fragment(path, docs_index):
    """Render one md file to docs/<slug>.html; register in docs_index. Returns (slug, name)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    slug = path.stem
    name = title_of(text, slug)
    (DOCS / f"{slug}.html").write_text(md_to_html(text), encoding="utf-8")
    docs_index[slug] = {"name": name, "file": f"docs/{slug}.html"}
    return slug, name


def main():
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True, exist_ok=True)

    matrix = parse_matrix()
    docs_index = {}

    ingredients = []
    for p in collect(ING, extra_skip=("_template",)):
        slug, name = write_fragment(p, docs_index)
        m = matrix.get(slug, {})
        ingredients.append({"slug": slug, "name": m.get("name", name),
                            "cls": m.get("cls", "—"), "relevance": m.get("relevance", "—"),
                            "tier": m.get("tier", "—"), "viabilityShort": m.get("viabilityShort", "—"),
                            "grade": m.get("grade", "—"), "gradeRank": m.get("gradeRank", 99),
                            "gradeBucket": m.get("gradeBucket", "unknown"),
                            "verdictLabel": m.get("verdictLabel", "—"), "verdict": m.get("verdict", "—")})
        if slug in matrix:
            docs_index[slug]["name"] = matrix[slug]["name"]
    ingredients.sort(key=lambda r: (r["gradeRank"], r["name"].lower()))

    def listing(paths):
        out = []
        for p in paths:
            slug, name = write_fragment(p, docs_index)
            out.append({"slug": slug, "name": name})
        return sorted(out, key=lambda r: r["name"].lower())

    competitors = listing(collect(COMP, extra_skip=("_template",)))
    market = listing(collect(MARKET) + collect(TRENDS))
    strat_order = [COMP / "_competitive-landscape.md", COMP / "_opportunities-whitespace.md",
                   ING / "_EVIDENCE-MATRIX.md", SCIENCE / "landmark-papers.md",
                   PRODUCTS / "what-to-make-recommendation.md", PRODUCTS / "roadmap.md",
                   BRAND / "positioning.md", BRAND / "brand-identity.md"]
    strategy = []
    for p in [x for x in strat_order if x.exists()]:
        slug, name = write_fragment(p, docs_index)
        strategy.append({"slug": slug, "name": name})

    dist, buckets, viable_strong = {}, {"strong": 0, "moderate": 0, "weak": 0, "unknown": 0}, 0
    for r in ingredients:
        dist[r["grade"]] = dist.get(r["grade"], 0) + 1
        buckets[r["gradeBucket"]] = buckets.get(r["gradeBucket"], 0) + 1
        if r["gradeBucket"] == "strong" and not r["viabilityShort"].lower().startswith("not viable"):
            viable_strong += 1

    data = {"generatedAt": datetime.date.today().isoformat(),
            "counts": {"ingredients": len(ingredients), "competitors": len(competitors),
                       "market": len(market), "strategy": len(strategy),
                       "strong": buckets["strong"], "moderate": buckets["moderate"],
                       "weak": buckets["weak"], "viableStrong": viable_strong},
            "gradeDist": dist, "ingredients": ingredients, "competitors": competitors,
            "market": market, "strategy": strategy, "docsIndex": docs_index}
    (SITE / "data.js").write_text("window.DATA = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    kb = (SITE / "data.js").stat().st_size / 1024
    print(f"Wrote data.js ({kb:.0f} KB) + {len(docs_index)} fragments in site/docs/")
    print(f"  ingredients={len(ingredients)} competitors={len(competitors)} market/trends={len(market)} strategy={len(strategy)}")
    print(f"  grades: strong(A/B)={buckets['strong']} (cosmetic-viable {viable_strong}) moderate(C)={buckets['moderate']} weak(D/F)={buckets['weak']} unknown={buckets['unknown']}")


if __name__ == "__main__":
    main()
