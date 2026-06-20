# Research Explorer (site)

An offline, interactive HTML view of the brand's research base — generated from the Markdown in [`../research/`](../research/) (plus key product/brand strategy docs).

## View it

The dossiers are fetched at runtime, so **serve the folder** (don't just double-click `index.html` — Chrome blocks `file://` fetches):

```bash
python -m http.server 8765 --directory site
# then open http://localhost:8765
```

Or host the `site/` folder on any static host (e.g. GitHub Pages).

## What's inside

- **Ingredients** — all ingredient dossiers in a sortable/filterable table (search, grade buckets, class, verdict) with a dashboard (evidence-grade distribution) and a click-to-read dossier reader.
- **Competitors / Market & Trends / Strategy** — searchable lists → the same reader.
- Grades reflect the **topical, leave-on, anti-aging** claim: **A/B** = solid human-topical evidence · **C** = weak/indirect · **D/F** = unproven topically. Verdicts: ✅ shortlist · ⚠️ conditional · ❌ skip.

## Rebuild after research changes

```bash
python site/build.py
```

This regenerates `data.js` (lightweight index) and the per-dossier fragments in `site/docs/`. Requires the `markdown` package (`pip install markdown`).

## Notes

- `data.js` and `docs/` are **generated** — commit them so the site is hostable out-of-the-box, or add them to `.gitignore` and build on demand if the churn bothers you.
- Styling is intentionally **neutral** — the brand's visual identity is still an open decision.
