# Website

The brand's home on the web. Right now this folder holds the **plan**; the site **code** (or Shopify theme) lands here when we build.

## Platform decision *(open)*

| Option | Best when | Notes |
|---|---|---|
| **Shopify** ⭐ | DTC commerce-first, fast to market | We have Shopify tools wired in (store previews, products, collections, discounts, analytics). Strong default for selling skincare. |
| **Headless (Hydrogen / Next.js + Shopify)** | We want a custom, design-forward site with Shopify commerce | More build effort; maximum design control for the wabi-sabi aesthetic. |
| **Custom (Next.js + Stripe)** | Content-led, commerce secondary | More control, more to maintain; rebuilds commerce Shopify gives free. |

**Working lean:** start on **Shopify** to sell fast, invest in custom/headless design later if the brand aesthetic demands it. Decide in [`../decisions/decision-log.md`](../decisions/decision-log.md).

## First-version sitemap *(draft)*

- **Home** — the kintsugi story + hero product
- **Shop** — product listing
- **Product pages** — benefit + science + ritual
- **Our story / philosophy** — the reframe of aging (this is our moat)
- **Ingredients / science** — credibility hub (pulls from [`../research/`](../research/))
- **Journal/blog** — SEO + education
- **About / contact / FAQ**

## When we build

- Use the **Shopify MCP** to spin up store previews from a description, then build out products/collections.
- Use **Figma** for design and **Canva** for supporting creative.
- Run **`/seo-audit`** to shape the content/keyword architecture.
- Keep large binaries out of git (see [`../.gitignore`](../.gitignore)); source design lives in Figma.

## Open questions
- [ ] Pick the platform.
- [ ] Secure the domain (run a domain availability check on Kintsugi variants).
- [ ] Lock the v1 sitemap.
