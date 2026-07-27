# Master naming ranking and staged trademark screen

**Prepared:** July 16, 2026  
**Decision rule:** rank the entire accumulated name universe first; run the federal knockout only on names scoring **above 8.0**.

## Outcome

- **13,548** archived candidate rows were consolidated from eleven naming pools.
- Normalization and deduplication produced **13,271 unique names**.
- Every unique name received one cohesive creative score and master rank.
- **397 names** scored above 8.0, representing the top **2.99%** of the universe.
- Those 397 names received the automated federal knockout.
- **222** received a **PROVISIONAL PASS** in that narrow screen.
- **175** surfaced a federal exact or near-match issue and should be reviewed before advancing.
- Fourteen previously selected names had also received a broader manual research pass; **six** are currently preliminary green at that deeper layer.

## Current six with both a strong creative score and a broader preliminary green signal

| Master rank | Name | Score | Current readout |
|---:|---|---:|---|
| 4 | No Mystery | 9.67 | Broader federal pass; descriptive category use may limit strength |
| 13 | Plain to See | 9.57 | Broader federal pass; ordinary/descriptive phrase strength needs review |
| 18 | Sure Enough | 9.52 | Broader federal pass; only an unrelated SHO'NUFF popcorn result surfaced |
| 19 | In Writing | 9.51 | Broader federal pass; ordinary-phrase strength needs review |
| 83 | Spelled Out | 8.95 | Broader federal pass; ordinary-phrase strength needs review |
| 205 | With Reason | 8.59 | Broader federal pass; ordinary-phrase strength needs review |

These are **not legally cleared names**. They are the cleanest names among the small subset already examined beyond exact/edit-distance-one matching.

The top creative name overall is **Say It Plain** at 9.70. It passed the basic automated federal knockout but has not yet received a broader manual/common-law search. **Sure Enough** remains the strongest previously researched expression of the conversational confidence and attitude that made StraightUp compelling.

## Important overrides from the deeper pass

The automated screen is deliberately narrow. It can produce a basic pass even when broader research finds a concern. The output files therefore contain separate `deeper_screen_status`, `deeper_screen_note`, and `decision_readout` fields.

Examples:

- **No Asterisk**: broader ASTERISK-family federal records surfaced, including Classes 010 and 035/042.
- **Put Plainly**: PLAINLY EARTH is live in Class 003.
- **Stand By It**: STAND BY / STANDBY phrase-family records surfaced in relevant classes.
- **Plain Proof**: active exact PlainProof common-law use was found in health analytics.
- **No Footnote / No Footnotes**, **No Small Print**, and **Show the Work**: category or commercial phrase use was found and should be resolved before advancement.

## Cohesive rating model

Every name was rescored under the same positioning: evidence-led anti-aging skincare with the directness, confidence, transparency, and spoken attitude of StraightUp.

| Component | Weight |
|---|---:|
| StraightUp-like attitude | 24% |
| Brand thesis fit | 24% |
| Verbal strength | 13% |
| Distinctiveness proxy | 13% |
| Product-system fit | 10% |
| Story and campaign headroom | 8% |
| Cross-round source quality | 8% |

Prior scores were treated as light supporting evidence, not as the controlling grade. Penalties were applied for names previously marked CUT/HOLD, awkward or mechanical constructions, meaning stretch, and poor verbal usability. The >8.0 threshold was calibrated to isolate approximately the top 3% for legal screening.

### Rating tiers

- **9.0–10.0 — A+ / exceptional:** strongest creative territory; requires legal and real-world validation.
- **8.01–8.99 — A / priority:** worthy of the staged trademark screen.
- **7.0–8.0 — B / credible to strong:** useful longlist or future exploration territory; not screened in this decision cohort.
- **Below 7.0:** insufficient strategic, verbal, or distinctive strength for this brief.

Automated scoring creates consistency across a massive pool; it does not replace founder judgment. Close scores should be treated as bands, not false precision.

## Federal screen scope and legal limits

The automated knockout used normalized exact and edit-distance-one matching against a local U.S. federal trademark corpus current through **July 6, 2026**, emphasizing relevant Classes 003, 005, 010, 021, 035, and 044.

This is a triage screen, not a legal clearance opinion. The USPTO explains that likelihood of confusion can arise from similarity in sound, appearance, meaning, or overall commercial impression—not only identical wording. It also recommends a comprehensive clearance search that includes federal records, state databases, and internet/common-law use. See the USPTO guidance on [likelihood of confusion](https://www.uspto.gov/trademarks/search/likelihood-confusion), [comprehensive clearance searching](https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks), and [federal trademark searching](https://www.uspto.gov/trademarks/search/federal-trademark-searching).

Accordingly:

- `PROVISIONAL PASS` means no disqualifying result appeared in the narrow automated federal test.
- `PRELIMINARY GREEN — broader federal pass` means broader federal research also found no relevant conflict, but common-law, state, domain, social, marketplace, and counsel review remain outstanding.
- RED, AMBER, and YELLOW results are investigation flags, not automatic legal conclusions.

## Deliverable guide

- `MASTER-13271-RATED.csv` — the authoritative master list: all unique names, scores, ranks, source provenance, and staged-screen status.
- `TOP-397-ABOVE-8-SCREENED.csv` — the complete >8.0 decision cohort with federal results.
- `ABOVE-8-PRELIMINARY-FEDERAL-PASSES.csv` — the 222 narrow automated passes; deeper-screen fields identify known exceptions.
- `KNOWN-DEEP-SCREEN-RESULTS.csv` — the fourteen names with existing broader research notes.
- `rating-summary.json` and `screened-ranking-summary.json` — machine-readable audit totals.

## Recommended next decision

Do not manually search all 222 preliminary passes at equal depth. First select roughly **20–30 names** from the >8.0 cohort based on founder reaction, pronunciation, packaging fit, and appetite for descriptive versus distinctive naming. Then run comprehensive federal, state, common-law, domain, social-handle, and international-market screening on that reduced group before counsel makes the final clearance call.
