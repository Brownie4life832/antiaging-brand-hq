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
import sys
import datetime
import shutil
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
ING = ROOT / "research" / "ingredients"
DEVICES = ROOT / "research" / "devices"
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
# Primary grade = the first/leading A–F token in a cell; en-dash "–" is a range
# separator (e.g. "C–D"), NOT a minus, so it is not captured as a sign.
GRADE_SEARCH = re.compile(r"([ABCDF])\s*([+\-−])?")
MD_BOLD = re.compile(r"\*\*(.+?)\*\*")
MD_LINK = re.compile(r"\[(.+?)\]\([^)]*\)")


def norm_grade(g):
    return g.replace("−", "-").replace("–", "-").replace("*", "").strip()


def strip_md(s):
    s = MD_BOLD.sub(r"\1", s)
    s = MD_LINK.sub(r"\1", s)
    return s.replace("`", "").strip()


def primary_grade(cell):
    m = GRADE_SEARCH.search(cell or "")
    if not m:
        return "—"
    return norm_grade(m.group(1) + (m.group(2) or ""))


def call_bucket(cell):
    # Priority: best available brand-adjacency wins (a row may carry several).
    if "✅" in cell:
        return "build"
    if "🤝" in cell:
        return "partner"
    if "📚" in cell:
        return "educate"
    if "❌" in cell:
        return "avoid"
    return "other"


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


def target_slug(path_prefix, stem, source_is_device):
    """Resolve an intra-doc .md link to a fragment slug. Device fragments are
    namespaced 'dev__<stem>' so device dossiers don't collide with ingredient
    dossiers of the same name (exosomes, polynucleotides-pdrn) or the shared
    _EVIDENCE-MATRIX. Folder-aware so device→ingredient links still resolve."""
    folder = (path_prefix or "").rstrip("/").split("/")[-1]
    if folder == "devices":
        return "dev__" + stem
    if folder == "":  # bare link → relative to the source doc's own folder
        return ("dev__" + stem) if source_is_device else stem
    return stem  # explicit non-device folder (ingredients/competitors/…)


def md_to_html(text, source_is_device=False):
    def repl(m):
        return f'href="javascript:void(0)" data-doc="{target_slug(m.group(1), m.group(2), source_is_device)}"'
    return LINK_RE.sub(repl, markdown.markdown(text, extensions=MD_EXT))


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


def parse_devices_matrix():
    """research/devices/_EVIDENCE-MATRIX.md columns:
    # | Modality(link) | Category | Clinic/best grade | At-home grade | Regulatory | Brand call | Note"""
    meta = {}
    f = DEVICES / "_EVIDENCE-MATRIX.md"
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
        pg = primary_grade(cols[3])
        meta[slug] = {"name": name, "category": cols[2],
                      "clinicGrade": strip_md(cols[3]), "homeGrade": strip_md(cols[4]),
                      "primaryGrade": pg, "gradeRank": grade_rank(pg), "gradeBucket": grade_bucket(pg),
                      "reg": strip_md(cols[5]), "call": strip_md(cols[6]),
                      "callBucket": call_bucket(cols[6]), "note": strip_md(cols[7])}
    return meta


def collect(folder, extra_skip=()):
    if not folder.exists():
        return []
    return [p for p in sorted(folder.glob("*.md"))
            if not p.name.startswith("_") and p.stem.lower() != "readme" and p.stem not in extra_skip]


def write_fragment(path, docs_index, source_is_device=False):
    """Render one md file to docs/<slug>.html; register in docs_index. Returns (slug, name).
    Device docs get a 'dev__' slug prefix to avoid cross-folder slug collisions."""
    text = path.read_text(encoding="utf-8", errors="replace")
    slug = ("dev__" + path.stem) if source_is_device else path.stem
    name = title_of(text, path.stem)
    (DOCS / f"{slug}.html").write_text(md_to_html(text, source_is_device), encoding="utf-8")
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

    # devices & procedures — research, shareable like ingredients (included in both modes).
    dmatrix = parse_devices_matrix()
    devices = []
    for p in collect(DEVICES, extra_skip=("_template",)):
        slug, name = write_fragment(p, docs_index, source_is_device=True)
        m = dmatrix.get(p.stem, {})
        devices.append({"slug": slug, "name": m.get("name", name),
                        "category": m.get("category", "—"), "clinicGrade": m.get("clinicGrade", "—"),
                        "homeGrade": m.get("homeGrade", "—"), "primaryGrade": m.get("primaryGrade", "—"),
                        "gradeRank": m.get("gradeRank", 99), "gradeBucket": m.get("gradeBucket", "unknown"),
                        "reg": m.get("reg", "—"), "call": m.get("call", "—"),
                        "callBucket": m.get("callBucket", "other"), "note": m.get("note", "")})
        if p.stem in dmatrix:
            docs_index[slug]["name"] = dmatrix[p.stem]["name"]
    devices.sort(key=lambda r: (r["gradeRank"], r["name"].lower()))

    def listing(paths):
        out = []
        for p in paths:
            slug, name = write_fragment(p, docs_index)
            out.append({"slug": slug, "name": name})
        return sorted(out, key=lambda r: r["name"].lower())

    # --public builds an ingredients-only site safe to publish (no competitor/market/strategy).
    public = "--public" in sys.argv
    if public:
        competitors, market, strategy = [], [], []
    else:
        competitors = listing(collect(COMP, extra_skip=("_template",)))
        market = listing(collect(MARKET) + collect(TRENDS))
        strat_order = [COMP / "_competitive-landscape.md", COMP / "_opportunities-whitespace.md",
                       ING / "_EVIDENCE-MATRIX.md", DEVICES / "_EVIDENCE-MATRIX.md",
                       SCIENCE / "landmark-papers.md",
                       PRODUCTS / "what-to-make-recommendation.md", PRODUCTS / "roadmap.md",
                       BRAND / "positioning.md", BRAND / "brand-identity.md"]
        strategy = []
        for p in [x for x in strat_order if x.exists()]:
            slug, name = write_fragment(p, docs_index, source_is_device=(p.parent == DEVICES))
            strategy.append({"slug": slug, "name": name})

    dist, buckets, viable_strong = {}, {"strong": 0, "moderate": 0, "weak": 0, "unknown": 0}, 0
    for r in ingredients:
        dist[r["grade"]] = dist.get(r["grade"], 0) + 1
        buckets[r["gradeBucket"]] = buckets.get(r["gradeBucket"], 0) + 1
        if r["gradeBucket"] == "strong" and not r["viabilityShort"].lower().startswith("not viable"):
            viable_strong += 1

    data = {"generatedAt": datetime.date.today().isoformat(),
            "counts": {"ingredients": len(ingredients), "devices": len(devices),
                       "competitors": len(competitors), "market": len(market), "strategy": len(strategy),
                       "strong": buckets["strong"], "moderate": buckets["moderate"],
                       "weak": buckets["weak"], "viableStrong": viable_strong},
            "gradeDist": dist, "ingredients": ingredients, "devices": devices,
            "competitors": competitors, "market": market, "strategy": strategy,
            "docsIndex": docs_index, "public": public}
    (SITE / "data.js").write_text("window.DATA = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    kb = (SITE / "data.js").stat().st_size / 1024
    print(f"Wrote data.js ({kb:.0f} KB) + {len(docs_index)} fragments in site/docs/  [mode: {'PUBLIC research-only' if public else 'FULL'}]")
    print(f"  ingredients={len(ingredients)} devices={len(devices)} competitors={len(competitors)} market/trends={len(market)} strategy={len(strategy)}")
    print(f"  grades: strong(A/B)={buckets['strong']} (cosmetic-viable {viable_strong}) moderate(C)={buckets['moderate']} weak(D/F)={buckets['weak']} unknown={buckets['unknown']}")


if __name__ == "__main__":
    main()
