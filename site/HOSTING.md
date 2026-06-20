# Hosting the research explorer (private / gated)

The goal: a real URL you (and collaborators) can open, **not** world-public — so your competitor teardowns, white-space map, and product strategy stay confidential. The GitHub repo stays private.

This host serves the **full** explorer (run `python site/build.py` with **no** `--public` flag). Build deps: `requirements.txt` (just `markdown`). Build output: the `site/` folder.

> GitHub Pages is intentionally **not** used here — it's public-only (non-Enterprise). The `.github/workflows/pages.yml` workflow is **manual-only** (`workflow_dispatch`); run it by hand only if you ever decide to publish an *ingredients-only* build to public Pages.

---

## Option A — Cloudflare Pages + Access  *(recommended: free, truly gated, native Python build)*

**1. Deploy**
1. [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers & Pages** → **Create** → **Pages** → **Connect to Git** → authorize and pick `Brownie4life832/antiaging-brand-hq` (private is fine).
2. Build settings:
   - **Build command:** `pip install -r requirements.txt && python site/build.py`
   - **Build output directory:** `site`
   - **Environment variable:** `PYTHON_VERSION = 3.12`
3. Save & Deploy → you get a `https://<project>.pages.dev` URL.

**2. Gate it (Cloudflare Access — free up to 50 users)**
1. In the dashboard → **Zero Trust** → **Access** → **Applications** → **Add an application** → **Self-hosted**.
2. Domain: your `*.pages.dev` URL.
3. Policy: **Allow** → include **Emails** = your email(s). (Login is email one-time-code; no password to manage.)
4. Save. Now the site requires sign-in — nobody else can read it.

Pushes to `main` auto-rebuild and redeploy (so the daily Trend Radar keeps it fresh).

---

## Option B — Vercel  *(easiest UI; gating = "Vercel Authentication", free on Hobby)*

1. [vercel.com/new](https://vercel.com/new) → import `antiaging-brand-hq` (private OK). `vercel.json` in the repo already sets the build command + output dir.
   - If the build can't find Python, set Project → Settings → **Environment Variables**, or use Option A.
2. Gate it: Project → **Settings → Deployment Protection → Vercel Authentication → Standard Protection (All Deployments)**. This restricts the site to members of your Vercel account. *(Password Protection is a paid add-on; Vercel Authentication is free.)*

---

## Option C — No host build (direct upload of the prebuilt folder)

If a host's Python build is fussy, build locally and upload the static output — no host build needed:

```bash
python site/build.py            # full site -> site/data.js + site/docs/
npx wrangler pages deploy site  # Cloudflare  (then add Access as above)
# or:  npx vercel deploy site --prod   (then enable Vercel Authentication)
```

Re-run after research changes to refresh.

---

## Notes
- Whichever you pick, **add the access policy before sharing the URL** — until gated, a `.pages.dev` / `.vercel.app` URL is publicly reachable by anyone who has it.
- `data.js` and `site/docs/` are generated (git-ignored); the host's build command regenerates them, or Option C uploads your local build.
