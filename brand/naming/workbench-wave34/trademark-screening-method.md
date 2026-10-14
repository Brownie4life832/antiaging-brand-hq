# Basic trademark and live-market knockout method

> **Status:** Method validated on 2026-07-16 with one current candidate and one known positive control. The full external batch is waiting for explicit user approval to transmit the private candidate list to the USPTO and search engines. This is a screening exercise, not legal clearance or a legal opinion.

## Input integrity

- Current delivered input: **500 names** across `net-new-250-2026-07-16.md` and `net-new-250-wave2-2026-07-16.md`.
- Validation on 2026-07-16: **500 table rows, 500 exact-unique names, 500 normalized-unique names**.
- Retained exclusion baseline before wave 3: **2,595 normalized names** — 2,095 historical candidates plus the two delivered 250-name waves. The wave-2 report's own generation baseline was 2,345 because it was checked against the historical 2,095 plus wave 1.
- Normalization for internal deduplication: lowercase; strip punctuation, whitespace, apostrophes, and diacritics; retain letters and numbers.

## Scope and decision rule

This pass is designed only to remove immediate, obvious problems. It must not be described as clearance or availability.

- **RED — obvious knockout:** live exact or highly similar federal mark for cosmetics/skincare; active exact-name cosmetics/skincare brand or product; or a dominant coined element already used for closely related goods.
- **AMBER — counsel review:** live exact mark in a coordinated beauty, health, retail, or scientific class; close sight/sound/meaning conflict; active adjacent-category use; dead federal record with evidence of continuing market use; or a common/descriptive expression with weak-mark risk.
- **PROVISIONAL PASS:** no obvious issue surfaced in this limited pass. This does not imply registrability or freedom to use.

USPTO explains that marks need not be identical: similarity in sound, appearance, meaning, or commercial impression can matter when the goods or services are related. It also says a comprehensive search includes federal records, state databases, and the internet. Sources: [Federal trademark searching](https://www.uspto.gov/trademarks/search/federal-trademark-searching), [Likelihood of confusion](https://www.uspto.gov/trademarks/search/likelihood-confusion), and [Why search for similar trademarks?](https://www.uspto.gov/trademarks/basics/why-search-similar-trademarks).

## Layer 1 — official USPTO federal knockout

### 1A. Exact live wordmark batch

Use the public search service behind the official [USPTO Trademark Search](https://tmsearch.uspto.gov/search/search-information):

`POST https://tmsearch.uspto.gov/prod-v1-0-0/tmsearch`

Run names sequentially in modest chunks (20 in the validated script) using the official full-mark field `FM` plus `LD:true`. For each name, include joined, spaced, and hyphenated forms when relevant. The script adaptively splits any chunk whose result set reaches the 100-record response ceiling. Retrieve at least serial number (`id`), wordmark, live status, international classes, goods/services, owner, registration number, and filing/registration dates. Do **not** initially filter to Class 003, because USPTO warns that narrowing by class can miss related goods and services.

Treat this as a one-time, low-volume knockout, not a crawler or a bulk-data feed. Pause between requests, stop on rate-limit or challenge responses, and never parallelize requests against the service. USPTO's [website terms](https://www.uspto.gov/terms-use-uspto-websites) warn that its online database interfaces are not intended for bulk downloads and that unusually high automated access may be blocked. Repeated or production-scale work should use the metered TSDR API or official bulk-data products instead; USPTO documents those options on its [Trademark bulk data](https://www.uspto.gov/trademarks/apply/check-status-view-documents/trademark-bulk-data) page.

Minimal official field-tag query shape before it is wrapped in the request payload:

```text
(FM:"candidate one" OR FM:"candidateone" OR FM:"candidate two") AND LD:true
```

The request uses the same `query_string` syntax as the official Trademark Search interface, requests at most 100 records per call, and maps returned full marks back to the normalized candidate register.

Classify live exact hits by commercial proximity:

- Primary danger: **IC 003** cosmetics and cleaning preparations.
- Coordinated classes identified by USPTO for IC 003: **IC 005, 021, 035, 042, and 044**.
- Also manually inspect IC 010 when the record involves dermatology, aesthetic devices, or skin treatment.

Official class source: [Using coordinated classes in your federal trademark search](https://www.uspto.gov/trademarks/search/using-coordinated-classes-your-federal-trademark-search).

### 1B. Simple similarity expansion

For every name, run the official UI combined-mark query for the exact phrase (`CM:"candidate"`). For coined or compact names, also check:

- joined and spaced forms;
- hyphenated and unhyphenated forms;
- obvious singular/plural;
- one likely phonetic spelling;
- dominant uncommon word without generic terms such as `skin`, `face`, `beauty`, `formula`, `lab`, `co`, or `club`.

Focus first on live records. Keep relevant dead records as AMBER when ordinary-web evidence suggests continued use. USPTO calls exact-wording search a knockout but expressly says not to stop there.

## Layer 2 — ordinary web and category use

Run one quoted web query per candidate, dated and logged:

`"CANDIDATE" (skincare OR "skin care" OR cosmetics OR beauty OR serum OR moisturizer)`

If no useful result appears and the name is coined or one word, run a second query:

`"CANDIDATE" (brand OR shop OR serum OR cream)`

Inspect only enough to establish an immediate issue:

- official brand/product page;
- major retailer product page;
- active social/profile evidence tied to skincare or cosmetics;
- credible business directory or press coverage;
- TSDR record for any surfaced serial number.

Do not treat a search-results snippet alone as decisive when the underlying page cannot be verified. Record the exact-use wording, market, and source URL.

## Layer 3 — consolidation

Maintain one row per candidate with these fields:

`set`, `row`, `name`, `score`, `query_date`, `federal_status`, `matched_mark`, `serial_or_registration`, `classes`, `goods_or_use`, `web_status`, `web_entity`, `source_url`, `decision`, `confidence`, `notes`.

Deduplicate federal hits by serial number. Preserve every obvious RED and AMBER record; for provisional passes, preserve the query date and note that no obvious result surfaced.

## Validated pilot

- **Pretty Rational** — official exact live-wordmark query returned zero results on 2026-07-16. This is only a federal exact-match provisional pass; similarity and common-law checks remain pending.
- **AGE SMART** — positive control returned live Reg. **3742282**, Serial **77766067**, covering non-medicated skincare in IC 003 and medicated skincare in IC 005. This confirms the query retrieves an obvious, known category conflict.
- Local comparison of the current 500 against 67 retained competitor profiles produced **zero exact normalized matches**. Three substring alerts were reviewed (`Judge for Yourself` / `Ourself`, `See for Yourself` / `Ourself`, and `Skin Not Shame` / `SKINN`) and are not exact-name collisions; they still remain eligible for later similarity review.

Pilot rows are in `trademark-pilot-findings.csv`.

## Important limitation and handoff

The full 500/1,000-name batch requires sending the private candidate names to external search services. The managed environment blocked that disclosure until the user explicitly approves it after being informed of the risk. Do not bypass the block with another endpoint, browser automation, or smaller batches. Once approval is given, run Layers 1–3 and append results to the final 1,000-name screening table.
