# CLAUDE.md — Operating manual for the Kintsugi brand hub

This file orients any Claude session working in this repository. Read it first.

## What this project is

This is the **headquarters for Kintsugi**, an anti-aging skincare brand being built from scratch by Hasan (who also runs Underdog Games). This is **not a software codebase** — it is a brand operations hub. The "product" is a brand: its identity, research, formulations, marketing, and eventually a storefront. Treat the Markdown files here as the brand's living memory.

The goal: **anything related to this brand should be answerable from this repo.** When you learn something new, write it down in the right place so the next session inherits it.

## The brand in one breath

**Kintsugi** takes its name from the Japanese art of mending broken pottery with gold — celebrating cracks and age rather than hiding them. The brand's working premise is a reframe of "anti-aging": from *fighting* and *erasing* age toward *repairing, renewing, and honoring* skin as it changes. Premium, science-backed, with a wabi-sabi / golden aesthetic. (Whether to call it "anti-aging" vs. "pro-aging / graceful aging" is an open positioning question — see [`brand/positioning.md`](brand/positioning.md).)

Full detail: [`brand/brand-identity.md`](brand/brand-identity.md).

## Repo map

```
brand/        Identity, positioning, voice & tone, visual identity, glossary
research/     ingredients/ market/ competitors/ science/ trends/  (the evidence base)
products/     roadmap + concepts/ + formulations/
marketing/    copy/ ads/ campaigns/ social/ email/
website/      plan now; site code later
ideas/        considering.md, not-considering.md, parking-lot.md
decisions/    decision-log.md
```

## How to work here

- **Ground every answer in the files.** If the user asks about the brand, read the relevant file(s) before answering. Don't invent brand facts — if something isn't decided, say so and offer to decide it.
- **Write decisions down.** When the user settles something, record it in [`decisions/decision-log.md`](decisions/decision-log.md) and update the affected file(s).
- **Keep "considering" vs "not considering" current.** The user specifically wants Claude to always know what's on and off the table. When an idea is raised, log it in [`ideas/`](ideas/). When one is killed, move it to [`not-considering.md`](ideas/not-considering.md) **with the reason**.
- **Use the templates.** New ingredient research → copy `research/ingredients/_template.md`. New product → copy `products/concepts/_template.md`.
- **Cite sources in research.** Skincare/ingredient claims must be evidence-based. Link sources. Flag marketing claims that would need substantiation or legal review (cosmetic vs. drug claims matter — see note below).
- **Dates are absolute.** Today's date is provided each session; write real dates (e.g. "2026-06-18"), never "today".

## Capabilities available in this environment

Lean on these rather than doing everything by hand:

- **Deep research** (`/deep-research` skill) — multi-source, fact-checked ingredient/market/competitor reports. Ideal for the `research/` folder.
- **Marketing skills** — `campaign-plan`, `content-creation` / `draft-content`, `email-sequence`, `seo-audit`, `brand-review`, `competitive-brief`.
- **Brand voice skills** — `generate-guidelines`, `enforce-voice` (apply our voice to any content).
- **Design skills** — `design-critique`, `ux-copy`, plus **Figma** and **Canva** MCP tools for visuals/ads, and image generation.
- **Shopify MCP** — for when we build the storefront (create store previews, products, collections, discounts, analytics).
- **Domain tools** — check/suggest domain availability for the brand.
- **Web search / fetch** — for anything time-sensitive.

When a task fits one of these, prefer it over freehand.

## Important guardrails for a skincare brand

- **Claims discipline.** In most markets, cosmetics may not claim to treat/prevent disease or alter structure/function of the body without crossing into "drug" territory (e.g. US FDA). Words like "anti-aging," "repairs," "boosts collagen" carry regulatory weight. Draft boldly, but flag claims that likely need substantiation or legal review. Track this in research/science.
- **No medical advice.** We can educate about ingredients; we don't diagnose or prescribe.
- **Evidence over hype.** This brand's credibility depends on real science. Prefer cited, peer-reviewed sources for ingredient efficacy.

## Conventions

- Markdown for everything. One topic per file. Descriptive `kebab-case.md` names.
- Each major folder has a `README.md` index — keep it updated when you add files.
- Commit messages: short, present-tense, describe the brand change ("Add niacinamide ingredient research", "Refine voice & tone toward warmer register").
