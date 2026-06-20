# Ingredient: FOXO4-DRI ("Proxofim") — Senolytic Peptide (experimental) (INCI: **none — not a cosmetic ingredient**)

**Researched:** 2026-06-19 · **Status:** ⬜ considering / ⬜ shortlisted / ☑ rejected / ⬜ in a product
**Class:** Peptides — signal / carrier / enzyme-inhibitor / neuro-inhibitor (functionally: a **senolytic** protein–protein-interaction inhibitor with a cell-penetrating carrier) · **Slug:** `foxo4-dri-peptide`

> Exhaustive literature review. **Brutally honest headline up front:** FOXO4-DRI is an **experimental research-grade
> peptide** designed as a senolytic *drug candidate*, **not a cosmetic ingredient.** It has **no INCI name, no
> cosmetic regulatory status, and is sold only "for research use only — not for human use."** Every "rejuvenates
> aged skin / regrows fur / clears zombie cells" headline traces to **one 2017 mouse study using intraperitoneal
> injection** (Baar et al., *Cell*) plus a handful of **in-vitro and injected-mouse follow-ups**. There is **zero**
> human clinical trial of any kind, **zero** human topical study, and a real but uncharacterized **theoretical
> oncogenic concern** (it works by un-leashing p53-driven apoptosis using an HIV-TAT cell-penetrating tag with no
> tissue selectivity). A grey-market "biohacker" self-injection culture exists and is **reckless**, not evidence.
> This dossier documents *why the science is fascinating and the cosmetic use is a hard skip*, and maps what the
> senescence biology genuinely supports. Companion reads: [`bcl-inhibitor-senolytics.md`](bcl-inhibitor-senolytics.md)
> (the other "drug, not cosmetic" senolytic class) and [`senolytics-os01-peptide.md`](senolytics-os01-peptide.md)
> (a *cosmetically viable* senomorphic peptide — the honest comparison).

---

## 1. Identity

| Field | Value |
|---|---|
| **Common / trade names** | FOXO4-DRI; FOXO4-D-Retro-Inverso; **"Proxofim"** (grey-market brand name); occasionally "FOXO4 peptide" |
| **INCI** | **None.** No INCI registration, no cosmetic ingredient listing anywhere (US/EU/UK/etc.). |
| **CAS** | **2460055-10-9** (registered as a research peptide / API, not a cosmetic) [10] |
| **Molecular formula** | C₂₂₈H₃₈₈N₈₆O₆₄ [10] |
| **Molecular weight** | **~5,358 Da** for the full HIV-TAT-fused 46-mer [10] (note: secondary "peptide-vendor" pages quote wildly inconsistent MWs of 1,611 / 2,301 / 2,957 Da — these are wrong or refer to fragments; trust the CAS-registered formula) |
| **Sequence** | All-D, retro-inverso: **ltlrkepaseiaqsileaysqngwanrrsggk** (FOXO4-derived) **+ rpppprrrqrrkkrg** (HIV-TAT cell-penetrating tag) [1][9][14] |
| **Form** | White lyophilized powder; soluble in DMSO and water; store −20 °C [10] |
| **Status** | **Experimental research peptide / preclinical drug candidate.** Not approved by FDA/EMA for any use. "For research use only — not for human consumption." [10][12][13] |

**What the "DRI" means (and why it matters).** "D-retro-inverso" = the peptide is built from **D-amino acids in a reversed sequence**. This near-mirror-image preserves the side-chain topology that lets it bind its target while making it **resistant to proteases** (L-peptidases don't cleave D-bonds), dramatically extending half-life in vivo. [1][9] This is a *drug-engineering* trick, not a cosmetic-formulation one.

**The carrier is part of the molecule.** FOXO4-DRI is two functional modules fused together: (a) a **FOXO4-derived interaction sequence** (the "signal/enzyme-inhibitor" payload that disrupts the FOXO4–p53 interaction) and (b) the **HIV-1 TAT cell-penetrating peptide** (the "carrier" that drags it across membranes into the cytoplasm/nucleus). [1][9][14] The TAT module is not just a passenger — the 2025 structural work shows it **also contacts p53** (see §2). So this single molecule spans most of the brief's peptide sub-classes: **carrier (TAT), enzyme/PPI-inhibitor (FOXO4–p53 disruption), signal (drives apoptosis program)** — but **not** "neuro-inhibitor" in any wrinkle-relaxing sense (it has nothing to do with SNARE/acetylcholine; the class label is a taxonomy artifact).

**Nomenclature caution.** "Proxofim" is a **grey-market/vendor brand**, not an approved drug name. Do not confuse FOXO4-DRI with the unrelated transcription factors FOXO1/FOXO3 (longevity-associated but different biology), nor with the BCL-2/BCL-xL senolytics (navitoclax etc., [`bcl-inhibitor-senolytics.md`](bcl-inhibitor-senolytics.md)) — same *senolytic goal*, completely different *mechanism*. And it is the opposite of OS-01/Decapeptide-52, which is a **senomorphic** (quiets senescence) cosmetic peptide, not a senolytic ([`senolytics-os01-peptide.md`](senolytics-os01-peptide.md)).

---

## 2. Class & mechanism

FOXO4-DRI is a genuine **senolytic** — it is designed to selectively *kill* senescent ("zombie") cells, as opposed to a **senomorphic** that merely quiets them. The mechanism is elegant and reasonably well understood:

- **The survival trick senescent cells use.** Senescent cells are under chronic stress and carry damaged DNA, which would normally trigger **p53-driven apoptosis**. They survive because the transcription factor **FOXO4 is upregulated in senescence and physically tethers p53 in the nucleus**, redirecting it toward cell-cycle arrest/maintenance genes and **away from the pro-apoptotic program** — keeping the cell alive but "zombie." [1]
- **What the peptide does.** FOXO4-DRI is a **decoy** that occupies the FOXO4–p53 interaction interface, **competitively perturbing the FOXO4–p53 complex.** Freed p53 undergoes **nuclear exclusion** and relocalizes (toward mitochondria), where it **triggers intrinsic (mitochondrial) apoptosis** — caspase-3 cleavage, BAX activation — selectively in senescent cells that are "addicted" to the FOXO4 survival tether. Healthy cells, not dependent on this tether, are largely spared. [1][6][7]
- **Why selectivity is plausible.** Only senescent cells have the high FOXO4 + primed-p53 configuration, so disrupting the interaction tips *them* into apoptosis while neighboring normal cells (lower FOXO4, no apoptotic priming) tolerate it. Multiple labs report sparing of non-senescent cells in culture. [4][6][7]

**Important 2025 mechanistic revision — the model is messier than the 2017 story.** Bourgeois et al. (2025, *Nature Communications*) solved the binding biophysics and found:
- FOXO4-DRI targets the **p53 transactivation domain 2 (p53TAD2)**, and **both** the FOXO4-derived region **and the HIV-TAT cationic tag contribute to binding** p53 — the "cell-penetrating" tag is not inert. [14]
- FOXO4-DRI and p53TAD2 are **intrinsically disordered** and **fold synergistically** only upon binding (a transient "coupled folding"), which the authors found surprising. [14]
- **p53TAD2 is a promiscuous hub** — it is also the binding site for CBP/p300, MDM2/HDM2, BRCA2, HMGB1 and others, so FOXO4-DRI **likely competes with multiple p53 regulators**, not just FOXO4. [14] This complicates the clean "specific FOXO4–p53 disruptor" narrative and raises off-target/specificity questions.

**Net cell-level story:** remove FOXO4's grip on p53 → p53 drives apoptosis → senescent dermal fibroblasts/endothelial cells die → fewer SASP-secreting cells → less inflammaging, less MMP-driven matrix breakdown → (in *mice / cell culture*) better tissue function, more collagen, restored fur/fitness. **The biology is real and beautiful. The delivery as a cosmetic — and the safety of un-leashing p53 with a non-targeted HIV-TAT tag — are the problems.**

---

## 3. Hallmarks of skin aging targeted

| Hallmark | Targeted? | Basis / honest caveat |
|---|---|---|
| **Cellular senescence** | ✅ Primary | Direct, validated senolysis of senescent fibroblasts, chondrocytes, endothelial cells, Leydig cells [1][4][6][7][8]; the core mechanism |
| **Inflammaging (SASP)** | ✅ | Killing SASP-secreting cells lowers IL-6, IL-1β, IL-8/CXCL8, TNF-α, TGF-β in models [4][6][7][8] |
| **Collagen / ECM loss** | ⚠️ (model only) | In keloid (over-collagen) fibroblasts FOXO4-DRI *reduced* collagen deposition and SASP [5]; the "more good collagen in aged dermis" claim is **mechanistically inferred**, not directly shown in normal aged human skin |
| **Photoaging** | ⚠️ Plausible | Senolysis of UV/stress-induced senescent fibroblasts is plausible by mechanism; **no human photoaging endpoint**, no UV-specific skin study |
| **Oxidative stress** | ⚠️ Indirect | Reduced γ-H2A.x (DNA-damage marker) and removal of ROS-generating senescent cells in models [6]; not an antioxidant itself |
| **Mitochondrial decline** | ⚠️ Mechanistic only | Acts *via* the mitochondrial apoptosis pathway (it *uses* mitochondria to kill cells); it is not a "mito-support / energy" cosmetic actor |
| **Barrier decline** | ❌ No data | No TEWL/barrier endpoint in any study |
| **Hydration** | ❌ No data | None |
| **Glycation / AGEs** | ❌ | No evidence |
| **Pigmentation / tone** | ❌ | No evidence (senescent melanocytes exist but weren't a study endpoint) |
| **Microbiome** | ❌ | No evidence |
| **"Fitness / fur" (whole-organism)** | ✅ in mice | Restored running endurance, fur density, renal function in aged mice — **by IP injection**, systemic, not skin-applied [1] |

**Honest framing:** the hallmark column maps onto the *theory* of skin longevity (clear zombie cells → calmer, younger-behaving dermis). But **every ✅/⚠️ rests on cell culture or injected-mouse data.** The single most-cited "skin" signal — fur regrowth — was a **systemic** effect of injected peptide in mice, not a topical cosmetic result.

---

## 4. Evidence review by tier  ← core of this dossier

**Overarching honesty flag:** there is a **complete absence of human clinical evidence of any kind** for FOXO4-DRI — no oral, no injected, no topical, no RCT, no registered trial that has reported results. The entire human "evidence base" is **uncontrolled biohacker self-injection anecdote** (§4, Tier 3). The real science is **in-vitro and injected-mouse.** Nothing here is a cosmetic, and nothing has been tested as one in people.

### Tier 1 — In-vitro & ex-vivo (the most reproducible evidence)

**Baar et al. (2017), *Cell* — foundational in-vitro work [1].** Identified FOXO4 as elevated in senescence and maintaining viability by sequestering p53. Designed the FOXO4-DRI decoy peptide. In **irradiation- and doxorubicin-induced senescent human fibroblasts (IMR90)**, FOXO4-DRI caused **p53 nuclear exclusion and selective apoptosis of senescent cells**, sparing proliferating cells. This is the origin of the whole field. *Limitation:* cell culture; senescence artificially induced.

**Huang, He, Makarczyk & Lin (2021), *Frontiers in Bioengineering and Biotechnology* — human chondrocytes [4].** In **in-vitro-expanded human chondrocytes** from **8 donors (ages 15–73)**, **25 µM FOXO4-DRI for 5 days** cut SA-β-gal⁺ senescent cells from **>40% to <5%** in heavily expanded (PDL9) cells; **did not affect viability of low-passage (PDL3, non-senescent) cells** — clean selectivity. Reduced MMP12, MMP13, IL-6 (though IL-8 rose). *Limitation:* in culture only; cartilage formation was *not* improved, so senolysis ≠ functional regeneration; tiny experimental n (3 replicates).

**Kong et al. (2025), *Communications Biology* — human keloid fibroblasts & organ culture [5].** **25 µM FOXO4-DRI** in serum-starvation-senescent **keloid and normal skin fibroblasts**, plus **human keloid organ-culture tissue** (up to 10 days). Promoted **apoptosis**, drove **p53-pS15 nuclear exclusion**, decreased G0/G1 cells, reduced SA-β-gal⁺ cells, downregulated SASP, and **attenuated collagen deposition**. This is the closest thing to a "human skin tissue" result — and it is **ex-vivo cultured tissue with peptide added to the medium, not topical and not normal aged facial skin** (keloid is a fibrotic scar disorder). *Limitation:* disease model (keloid), ex-vivo, no topical delivery, no controls for normal-skin aging.

**Bourgeois et al. (2025), *Nature Communications* — binding biophysics [14].** Mapped the FOXO4-DRI ↔ p53TAD2 interaction (coupled folding; TAT contributes to binding; promiscuous site). Strengthens mechanistic understanding **and** flags specificity concerns (competes with CBP/p300, MDM2, BRCA2, etc.). *Limitation:* structural/biophysical, not efficacy.

**Bottom line, Tier 1:** robust, reproducible, mechanism-anchored. FOXO4-DRI genuinely and selectively kills senescent human fibroblasts/chondrocytes/endothelial cells in a dish at ~25–50 µM. This is real science — it lives in cell culture and isolated tissue.

### Tier 2 — Animal (all by injection; source of the "rejuvenation" headlines)

**Baar et al. (2017), *Cell* — the landmark in-vivo study [1].** The one everyone cites.
- **Models:** fast-aging **XpdTTD/TTD (trichothiodystrophy) mice**, **naturally aged mice (>2 yr)**, and a **doxorubicin chemotoxicity model**.
- **Dosing/route:** **~5 mg/kg systemic injection** (the *Cell* paper used **intravenous (IV)** dosing every other day for its core aging/senolytic experiments; later follow-ups [8] use **intraperitoneal (IP)** at the same dose), repeated over weeks — **systemic injection either way, NOT topical.** [1][8]
- **Results:** restored **fur density / coat** (fast-aging mice "began recovering coats after ~10 days"), restored **renal function** markers, and roughly **doubled running/wheel endurance** vs controls after ~3 weeks. Separately, FOXO4-DRI **neutralized doxorubicin chemotoxicity** — reduced doxorubicin-induced loss of body weight and **lowered liver-damage marker AST**. [1]
- **Tolerability (the load-bearing caveat):** the authors state results were obtained **"under conditions where it was well tolerated in vivo"** — i.e., tolerability was **dose- and schedule-dependent**, an explicit hedge, not a clean safety endorsement. [1]
- **Limitations:** mouse; **injected, systemic**; fur/fitness are whole-body, not skin-cosmetic endpoints; the "human skin" leap is unjustified from this paper.

**Zhang et al. (2020), *Aging (Albany NY)* — aged-mouse Leydig cells / testosterone [8].** **5 mg/kg IP, every other day ×3** in aged mice. Caused **nuclear exclusion of Ser15-phospho-p53 and apoptosis in senescent Leydig cells**, lowered testicular SASP (IL-1β, IL-6, TGF-β), and **raised serum testosterone**; spared normal cells. n=6 aged mice/condition (+ 14 human testis specimens analyzed for FOXO4 expression, not treated). *Injected, systemic, gonadal tissue — not skin.*

**FOXO4-DRI spermatogenesis follow-up (2024), *Theriogenology*-adjacent [16].** Reported FOXO4-DRI improves spermatogenesis in aged mice by reducing Leydig-cell SASP. *Injected; reproductive tissue; reinforces the systemic-senolytic story, irrelevant to topical skin.*

**Hu et al. (2026), endothelial senescence, *PMC* [7].** In **HUVECs** (in vitro, 50 µM) and **naturally aged (17-mo) + D-galactose-aged mice** (**5 mg/kg IP every 2 days ×1 month**): prevented FOXO4–p53 binding, drove phospho-p53 nuclear exclusion, activated BAX/cleaved caspase-3, **reduced p21/p16/γ-H2AX, raised Ki-67 and Lamin B**, and **downregulated IL-1β, IL-6, IL-8, TNF-α**. n≥3–5/group. *Injected/in-vitro; vascular, not cutaneous.*

**FOXO4 peptide in pulmonary fibrosis (2022), *PMC* [15].** A FOXO4-targeting peptide ameliorated bleomycin-induced lung fibrosis in mice via ECM-receptor interaction. *Injected; lung; shows anti-fibrotic senolytic breadth, not skin.*

**Bottom line, Tier 2:** consistent, multi-tissue, multi-lab senolytic efficacy in **injected mice** — fibroblast, chondrocyte, endothelial, Leydig, myofibroblast. Strong support for the *mechanism in animals by injection.* **No animal study used topical/dermal application, and none studied normal aged facial-type skin as a cosmetic endpoint.**

### Tier 3 — Human, ORAL or systemic (this is where the evidence collapses)

- **No registered, completed human clinical trial** of FOXO4-DRI has reported results (oral, injected, or otherwise) as of June 2026. [12][13]
- The only human "data" are **uncontrolled biohacker self-experiments** — individuals **self-injecting research-grade FOXO4-DRI** sourced from peptide vendors, documented on longevity-enthusiast sites. [11] These are **anecdotes with no controls, no blinding, no safety monitoring, no published outcomes** — they constitute **zero evidence of efficacy** and are a **serious safety hazard** (unregulated purity, dosing by guesswork, injecting a pro-apoptotic p53-activator into a whole human body). Treat all such reports as **reckless, not data.**
- Commercial development is early/stalled: **Cleara Biotech / Numeric Biotech** hold the FOXO4-p53 IP and remain **preclinical** as of 2026 — and Cleara is reportedly pivoting toward the FOXO4-p53 interaction broadly **rather than FOXO4-DRI itself** (in part because the DRI peptide is hard to protect with IP). [13]

**What the human record proves for skincare:** **nothing positive.** There is no human efficacy or safety dataset to borrow from.

### Tier 4 — Human, TOPICAL

**None. Zero.** There is **no** human topical study of FOXO4-DRI — not an RCT, not a pilot, not a case series, not a corneometer/TEWL trial. The closest "human skin" data (Kong 2025 keloid [5]) used **peptide added to the culture medium of ex-vivo fibrotic scar tissue**, not topical application to living skin.

**What is actually proven for TOPICAL human use: nothing.** Any product or copy implying a topical FOXO4-DRI "clears your skin's senescent cells / rejuvenates skin / regrows" is **borrowing from injected-mouse and cell-culture data** and is **making a drug claim about an unapproved experimental drug.**

---

## 5. Topical bioavailability / penetration

- **Size is disqualifying for passive penetration.** At **~5,358 Da** [10], FOXO4-DRI is **~10× the ~500 Da "rule-of-500"** ceiling for easy stratum-corneum passage. Intact peptides this large do not meaningfully diffuse into living dermis from a normal leave-on cosmetic.
- **The TAT tag enables *cell* entry, not *skin* entry.** HIV-TAT is a cell-penetrating peptide that moves cargo **across a cell membrane once it is already next to the cell** — it does **not** solve transport **across the stratum corneum** to reach dermal fibroblasts in the first place. In every study, the peptide was **delivered by injection or directly into culture medium**, bypassing the barrier entirely. There is **no published skin-penetration (PK/Franz-cell) data** showing FOXO4-DRI reaches the dermis topically.
- **Stability vs. delivery is not the limiter — delivery is.** The DRI design makes it protease-stable (good for an injectable), but that does nothing to get a 5.4 kDa cationic peptide through intact skin.
- **The delivery paradox (and danger).** To "work" topically you'd need it to reach senescent dermal fibroblasts at senolytic concentration **without** systemic absorption (because systemic, non-targeted p53 activation is the safety risk, §7). Threading that needle is an unsolved pharmaceutical-delivery problem — and any vehicle aggressive enough to push a 5.4 kDa peptide into the dermis (e.g., microneedling, DMSO, electroporation) crosses out of "cosmetic" entirely.

---

## 6. Formulation

**Not formulable as a cosmetic** — included only to document why.
- **Use level / concentration:** undefined for cosmetics. Research used **~25–50 µM in culture** [4][5][7] and **~5 mg/kg by injection** in mice [1][8]. There is **no established safe cosmetic concentration** because it is not a cosmetic ingredient.
- **pH / stability:** handled as a pharmaceutical-grade lyophilized powder, reconstituted in water/DMSO, stored frozen (−20 °C) [10]. Not a stable, shelf-life-friendly cosmetic raw material.
- **Pairings:** N/A — this is an experimental drug candidate, not something to "pair with niacinamide." Combining a p53-apoptosis-inducer with retinoids/exfoliants in a consumer product is not a meaningful formulation question; it is off the table.
- **Sensory / vehicle:** any realistic dermal-delivery vehicle would itself be a penetration enhancer or device, not a benign cosmetic base.
- **Practical reality:** legitimate skin development of FOXO4-DRI (if it happens) would proceed as a **prescription drug or device-delivered therapeutic** through clinical trials — **not** as an OTC cosmetic.

---

## 7. Safety

**This section is decisive — and it is a *caution*, not a reassurance.**

- **No human safety data exist.** No completed, reported clinical trial; no HRIPT, no patch test, no ocular/sensitization data, no dermal-safety dossier. Everything below is theoretical or animal-derived.
- **Mechanism-based oncogenic concern (the headline risk).** FOXO4-DRI works by **modulating p53**, the master tumor-suppressor, using a **non-targeted HIV-TAT carrier** that enters *all* cells, not just senescent ones. Acutely it pushes senescent cells to apoptosis, but **chronic, systemic, non-selective perturbation of the p53 axis** — and competition with **MDM2, CBP/p300, BRCA2** at the promiscuous p53TAD2 site [14] — carries an **unquantified theoretical cancer/genomic-instability risk** that has **never been characterized in humans.** This is the opposite of a benign cosmetic peptide.
- **Tolerability was dose-dependent even in mice.** Baar 2017 explicitly framed efficacy as occurring "**under conditions where it was well tolerated**" [1] — a hedge implying a therapeutic window that has to be respected, not a clean safety signal.
- **Senolysis is not uniformly beneficial.** As with the BCL-xL senolytics (see [`bcl-inhibitor-senolytics.md`](bcl-inhibitor-senolytics.md), where navitoclax caused **bone loss** in aged mice), clearing senescent cells indiscriminately has trade-offs — senescent cells have legitimate roles in **wound healing, fibrosis limitation, and tumor suppression.** Off-target/on-target harms in skin are uncharacterized.
- **Grey-market self-injection is dangerous.** Research-grade peptide sold "not for human use" has **no pharmaceutical purity/sterility guarantees**; biohackers dosing themselves by injection are exposing their **whole body** to a p53-activator with no monitoring. [11] This is a real, documented hazard the brand must never be associated with.
- **Pregnancy/breastfeeding:** **contraindicated by default** — a pro-apoptotic, p53-axis-perturbing experimental agent must be treated as unsafe in pregnancy. Do not use, do not market.
- **Sourcing safety:** sold only as **"research use only / not for human use"** reagent (BOC Sciences, APExBIO, Novoprolabs and many grey-market "peptide" shops) [10][12][13] — buying it for a consumer product would be a regulatory and ethical violation.
- **Sun sensitivity:** no specific photosensitization data (moot, given it's not a usable cosmetic).

---

## 8. Regulatory & claims (per CLAUDE.md guardrails)

**This is the section that settles it.** Under US FDA (and equivalently EU/UK cosmetic law), a product's *intended use* and *ingredients* determine its category, and FOXO4-DRI fails the cosmetic test on every axis:

1. **It is a drug candidate, not a cosmetic, by composition and intent.** FOXO4-DRI is an **unapproved experimental peptide** with **no INCI name, no cosmetic regulatory clearance anywhere**, and is sold **"for research use only — not for human use."** [10][12][13] Putting it in a consumer product would create an **unapproved new drug + adulterated/misbranded cosmetic** — a serious violation, not a labeling nuance.
2. **The mechanism is inherently a drug claim.** "Kills/clears senescent cells," "induces apoptosis," "activates p53," "rejuvenates skin," "regrows," "reverses aging" are all **structure/function or disease claims** with no OTC monograph → automatically drug territory. There is **no compliant cosmetic way to describe what this molecule does**, because what it does *is* pharmacology.
3. **No defensible cosmetic claim exists** — there is no human topical evidence to substantiate anything, and the only honest mechanistic description is a drug action.

- ✅ **Safe cosmetic language:** **none applies** — there is no cosmetic use to describe. (Per [`../../brand/glossary.md`](../../brand/glossary.md), even "supports / visibly" framing presumes a legitimate cosmetic ingredient, which this is not.)
- ⚠️ **Forbidden:** "senolytic," "clears zombie/senescent cells," "FOXO4-DRI," "Proxofim," "activates p53," "rejuvenates skin," "regrows," "reverses skin aging" on any product. Each is an unapproved-drug claim about an unapproved experimental drug.
- **Educational use only:** the brand may *reference this science* in editorial/explainer content ("the cutting edge of senescence research includes the FOXO4-p53 senolytic peptide FOXO4-DRI, studied as an injectable drug candidate in mice — not a skincare ingredient") — clearly framed as **investigational pharmacology, not our product.** That is the **only** legitimate brand touchpoint.

See the claims guardrail in [`../../CLAUDE.md`](../../CLAUDE.md) and the cheat-sheet in [`../../brand/glossary.md`](../../brand/glossary.md).

---

## 9. Sourcing & cost

- **Availability:** sold only as a **research-use-only reagent / API** (BOC Sciences, APExBIO, Novoprolabs) and via a large **grey-market "research peptide" ecosystem** (Proxofim-branded 10 mg vials from Core Peptides, BiotechPeptides, Particle Peptides, etc.). **None** supplies it as a cosmetic raw material with an INCI, a cosmetic-grade CoA, or leave-on safety data. [10][11][12][13]
- **Cost:** research-reagent pricing is high per mg (10 mg vials commonly ~$100–$300 grey-market; research-grade synthesis higher), but **cost is irrelevant** — the compound **cannot be lawfully or ethically used in a consumer cosmetic.**
- **Supply/ethics:** procuring an experimental, p53-perturbing injectable drug candidate to formulate into skincare is a non-starter for a credible brand; it would fail any responsible-sourcing, insurance, retailer-compliance, and legal review.

---

## 10. Hype vs. evidence

| Marketing / press claim (seen in longevity & "peptide" coverage) | Reality |
|---|---|
| "FOXO4-DRI regrows fur and rejuvenates aged animals" | True **only** in mice, by **systemic injection** (5 mg/kg IV in Baar 2017 [1]; IP in follow-ups [8]) — not topical, not a cosmetic. |
| "Topical senolytic peptide clears your skin's zombie cells" | **No human topical study exists.** Selectivity is shown in **cell culture and injected mice** only. [1][4][5] |
| "Clears senescent cells in human skin" | Closest data is **peptide added to ex-vivo keloid scar tissue in culture** [5] — not topical, not normal skin, not in a person. |
| "Proxofim — proven anti-aging peptide" | "Proxofim" is a **grey-market brand**; FOXO4-DRI is **unapproved, never completed a human trial**, and sold "not for human use." [10][12][13] |
| "Safe, just a peptide" | It **perturbs the p53 tumor-suppressor axis** with a non-targeted HIV-TAT carrier; **theoretical oncogenic risk uncharacterized in humans**; biohacker self-injection is dangerous. [11][14] |
| "People are already using it successfully" | Only **uncontrolled self-injection anecdotes** — zero controlled evidence, real safety hazard. [11] |
| "You can buy it as an ingredient" | It's a **research chemical / experimental drug**, not a cosmetic ingredient — formulating it into product is illegal. |

Independent framing converges: **FOXO4-DRI is one of the most scientifically interesting senolytic concepts** (a clever p53-axis decoy), but its future — if any — is as a **physician-supervised injectable/therapeutic developed through clinical trials**, not an OTC cosmetic. The genuinely exciting science is being used by grey-market vendors to sell a fantasy product and, worse, to encourage self-injection.

---

## 11. Verdict for the brand

❌ **SKIP — hard skip. A class to *understand and reference*, never to *formulate*.**

- **Why skip (non-negotiable):** FOXO4-DRI is an **unapproved experimental drug candidate / research reagent**, not a cosmetic ingredient. **No INCI, no cosmetic regulatory status, ~5,358 Da (won't penetrate intact skin), zero human evidence of any kind, zero human topical evidence, a mechanism-based theoretical cancer concern (non-targeted p53 activation), and a dangerous grey-market self-injection culture.** Using it would mean selling an adulterated cosmetic / unapproved drug — fatal to a credibility-first brand and a serious legal and safety exposure. This sits alongside the BCL-xL senolytics as one of the cleanest "no"s in the senotherapeutic space.
- **Why it's still worth a dossier:** FOXO4-DRI is a **landmark proof-of-concept for the FOXO4-p53 senolytic mechanism** — the elegant counterpart to the BCL-xL "survival-shield" senolytics. It is excellent **editorial/educational** material for explaining *why* the brand pursues gentle, evidence-based, **cosmetically legitimate** senotherapeutics instead of injectable drug candidates.
- **Longevity relevance:** **High in the science, zero in the bottle.** Senescent-cell clearance is the most compelling thesis in skin longevity; FOXO4-DRI proves the mechanism in animals — which makes it powerful *reference* material, never a formulation ingredient.
- **Strategic alternative:** if the brand wants a credible "senescence" angle, build it on **(a)** a **senomorphic cosmetic peptide with an INCI and at least some human topical data** — OS-01 / **Decapeptide-52** (conditional; see [`senolytics-os01-peptide.md`](senolytics-os01-peptide.md)), and/or **(b)** **botanical senotherapeutics** (fisetin, quercetin), all framed with honest "supports / visibly" cosmetic language. Reference FOXO4-DRI and the BCL-xL senolytics only as the *research frontier the brand respects but does not (and cannot) sell.*

Log in [`../../ideas/not-considering.md`](../../ideas/not-considering.md) with reason: **"Experimental, unapproved senolytic drug candidate / research-use-only peptide (FOXO4-p53 decoy + HIV-TAT). No INCI, no cosmetic status, ~5.4 kDa (no skin penetration), zero human evidence, theoretical p53/oncogenic risk, grey-market self-injection hazard. Illegal/unsafe to formulate. Keep as science reference / benchmark only — pursue cosmetically legitimate senomorphics (Decapeptide-52) and botanical senotherapeutics instead."**

---

## 12. Sources

1. Baar MP, Brandt RMC, Putavet DA, et al. (2017). "Targeted Apoptosis of Senescent Cells Restores Tissue Homeostasis in Response to Chemotoxicity and Aging." *Cell* 169(1):132–147.e16. (Foundational FOXO4-DRI paper: FOXO4–p53 mechanism; IP-injected mice; fur/renal/fitness restoration; doxorubicin chemotoxicity neutralized; "well tolerated" hedge.) https://www.cell.com/cell/fulltext/S0092-8674(17)30246-5 · PubMed: https://pubmed.ncbi.nlm.nih.gov/28340339/
2. AACR *Cancer Discovery* research highlight (2017). "A FOXO4 Inhibitory Peptide Limits Chemotoxicity in Mice." (Independent summary of Baar 2017.) https://aacrjournals.org/cancerdiscovery/article/7/6/OF21/5897/A-FOXO4-Inhibitory-Peptide-Limits-Chemotoxicity-in
3. *Kidney International* commentary (2017) on senescent-cell clearance / FOXO4-DRI and renal function. https://www.kidney-international.org/article/S0085-2538(17)30334-4/pdf
4. Huang H, He J, Makarcyzk MJ, Lin H (2021). "Senolytic Peptide FOXO4-DRI Selectively Removes Senescent Cells From in vitro Expanded Human Chondrocytes." *Frontiers in Bioengineering and Biotechnology* 9:677576. (25 µM/5 d; SA-β-gal >40%→<5% in PDL9; PDL3 spared; 8 donors 15–73; MMP/IL-6 down, IL-8 up.) https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2021.677576/full · PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC8116695/ · PubMed: https://pubmed.ncbi.nlm.nih.gov/33996787/
5. Kong X, et al. (2025). "FOXO4-DRI induces keloid senescent fibroblast apoptosis by promoting nuclear exclusion of upregulated p53-serine 15 phosphorylation." *Communications Biology* 8. (25 µM; keloid + normal skin fibroblasts + keloid organ culture; apoptosis, p53-pS15 nuclear exclusion, ↓SASP, ↓collagen deposition; ex-vivo, not topical.) https://www.nature.com/articles/s42003-025-07738-0 · PubMed: https://pubmed.ncbi.nlm.nih.gov/39994346/
6. Putavet DA, de Keizer PLJ — review on FOXO4-p53 senolysis and senescent-cell mechanisms (de Keizer lab). (Mechanism: FOXO4 sequesters p53; DRI peptide → nuclear exclusion → apoptosis; γ-H2A.x reduction.) https://www.fightaging.org/archives/2017/03/selective-destruction-of-senescent-cells-by-interfering-in-foxo4-p53-crosstalk/
7. Hu et al. (2026). "FOXO4-DRI regulates endothelial cell senescence via the P53 signaling pathway." *PMC.* (HUVEC 50 µM; aged + D-gal mice 5 mg/kg IP q2d ×1 mo; ↓p21/p16/γ-H2AX, ↑Ki-67/Lamin B; ↓IL-1β/IL-6/IL-8/TNF-α; BAX/cleaved caspase-3.) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12852416/
8. Zhang C, et al. (2020). "FOXO4-DRI alleviates age-related testosterone secretion insufficiency by targeting senescent Leydig cells in aged mice." *Aging (Albany NY)* 12. (5 mg/kg IP every other day ×3; senescent Leydig-cell apoptosis, ↓IL-1β/IL-6/TGF-β, ↑serum testosterone; n=6 aged mice; 14 human testis specimens analyzed.) https://www.aging-us.com/article/102682/text · PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7053614/
9. Bourgeois B, et al. — characterization of the FOXO4-DRI peptide (FOXO4 N-terminal/α-helix-1 region fused to HIV-TAT; all-D retro-inverso). (Design/sequence.) (See also [14].)
10. BOC Sciences — FOXO4-DRI product/reagent page. (CAS 2460055-10-9; formula C₂₂₈H₃₈₈N₈₆O₆₄; MW ~5358.05; sequence D-(LTLRKEPASEIAQSILEAYSQNGWANRRSGGKRPPPRRRQRRKKRG); "for research and manufacturing use only — we do not sell to patients"; store −20 °C.) https://aapep.bocsci.com/product/foxo4-dri-341926.html · Novoprolabs: https://www.novoprolabs.com/p/foxo4-dri-peptide-318716.html · APExBIO: https://www.apexbt.com/foxo4-dri-ba2892.html
11. Fight Aging! — "An Example of Senolytic Self-Experimentation with FOXO4-DRI" (2017) and "How to Plan and Carry Out a Simple Self-Experiment… FOXO4-DRI" (2018). (Documents the unregulated biohacker self-injection culture — anecdote, not evidence; safety hazard.) https://www.fightaging.org/archives/2017/05/an-example-of-senolytic-self-experimentation-with-foxo4-dri/ · https://www.fightaging.org/archives/2018/03/how-to-plan-and-carry-out-a-simple-self-experiment-a-single-person-trial-of-senolytic-peptide-foxo4-dri/
12. Vendor "research use only" listings confirming non-cosmetic, not-for-human-use status (e.g., Core Peptides, BiotechPeptides, Particle Peptides "Proxofim"). https://www.corepeptides.com/peptides/foxo4-dri-10mg/ · https://biotechpeptides.com/product/foxo4-dri-proxofim-10mg/
13. Fight Aging! (2026). "People Are Still Working on the Senolytic Peptide FOXO4-DRI." (As of 2026: still preclinical; Cleara Biotech / Numeric Biotech hold FOXO4-p53 IP; Cleara pivoting to the FOXO4-p53 interaction over FOXO4-DRI per se; no completed human trial; IP-protection difficulty.) https://www.fightaging.org/archives/2026/02/people-are-still-working-on-the-senolytic-peptide-foxo4-dri/
14. Bourgeois B, et al. (2025). "The disordered p53 transactivation domain is the target of FOXO4 and the senolytic compound FOXO4-DRI." *Nature Communications* 16. (FOXO4-DRI binds p53TAD2; HIV-TAT tag also contacts p53; coupled folding of disordered partners; p53TAD2 is a promiscuous hub shared with CBP/p300, MDM2/HDM2, BRCA2, HMGB1 → competition/specificity concern.) https://www.nature.com/articles/s41467-025-60844-9 · PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12216184/
15. "FOXO4 peptide targets myofibroblast ameliorates bleomycin-induced pulmonary fibrosis in mice through ECM-receptor interaction pathway." (2022). *PMC.* (Anti-fibrotic senolytic breadth in mice; injected.) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9170815/
16. "FOXO4-DRI improves spermatogenesis in aged mice through reducing senescence-associated secretory phenotype secretion from Leydig cells." (2024). *ScienceDirect* (Reproductive Biology / Theriogenology family). (Injected; reproductive tissue.) https://www.sciencedirect.com/science/article/pii/S0531556524001645
17. dvm360 (2017). "Cell-Penetrating Peptide Targets Senescent Cells to Restore Tissue Function." (Lay/veterinary summary of Baar 2017.) https://www.dvm360.com/view/cellpenetrating-peptide-targets-senescent-cells-to-restore-tissue-function

---

## Evidence verification (adversarial)

_Verified 2026-06-19 by independent re-reading/cross-checking of primary sources: Baar 2017 *Cell* [1] (abstract + multiple secondary confirmations [2][3][6][17]); Huang/Lin 2021 chondrocyte study [4] (PMC full text); Kong 2025 keloid [5] (PubMed abstract); Hu 2026 endothelial [7] (PMC); Zhang 2020 Leydig [8] (aging-us full text); Bourgeois 2025 *Nat Commun* structural paper [14] (PMC); CAS/reagent identity [10]; commercialization/status [13]. Goal: catch any benefit quietly borrowed from injected-mouse/cell-culture data and presented as topical-cosmetic proof, and confirm the "drug/research-reagent, not cosmetic" conclusion._

### Overall evidence grade for TOPICAL COSMETIC use: **F** (no human topical cosmetic evidence exists; no human evidence of any kind). Mechanistic / animal grade for the senolytic *mechanism*: **B+** (reproducible across labs and tissues — but pharmacological, injected, and with an open specificity/safety question raised by the 2025 structural work).

- **Mechanism (B+/A−, verified):** FOXO4 sequesters p53 in senescent cells; FOXO4-DRI displaces it → p53 nuclear exclusion → intrinsic apoptosis. Reproduced across human fibroblasts [1], chondrocytes [4], keloid fibroblasts [5], endothelial cells [7], Leydig cells [8]. The 2025 *Nat Commun* paper [14] **revises** the clean model (TAT contributes to binding; promiscuous p53TAD2 site) — correctly represented as both a mechanistic advance and a specificity caveat.
- **Animal data (verified, correctly caveated):** all in-vivo work is **systemic injection (~5 mg/kg)** — **IV** in the foundational Baar 2017 *Cell* paper [1], **IP** in the follow-ups [7][8]; fur/renal/fitness restoration and doxorubicin rescue are **systemic injected-mouse** results, not skin/topical. The dossier does not let any of these masquerade as topical proof. (Correction: an earlier draft labeled all routes "IP"; the *Cell* core experiments were IV — route corrected, conclusion unchanged.)
- **Human data reality (verified):** **no completed/reported human trial** of any route; the only human "use" is **uncontrolled grey-market self-injection** [11] — explicitly flagged as anecdote + hazard, not evidence. Status confirmed preclinical as of 2026 [13].
- **Topical reality (verified):** **no human topical study.** Kong 2025 [5] is **ex-vivo keloid tissue in culture**, not topical or normal skin — correctly downgraded.
- **Identity/penetration (verified):** CAS 2460055-10-9, formula C₂₂₈H₃₈₈N₈₆O₆₄, MW ~5,358 Da [10]; far above the penetration ceiling; TAT enables *cell* entry, not *skin* entry. Inconsistent vendor MWs (1,611/2,301/2,957 Da) noted and rejected in favor of the CAS-registered formula.
- **Safety (verified as a caution):** no human safety data; mechanism-based theoretical oncogenic concern from non-targeted p53 perturbation + promiscuous-site competition [14]; tolerability in mice was dose-dependent ("well tolerated" hedge in [1]); senolysis-is-not-uniformly-good cross-referenced to the bone-loss precedent in [`bcl-inhibitor-senolytics.md`].

### Load-bearing caveats
1. **Not a cosmetic ingredient — full stop.** No INCI, no cosmetic status; sold "research use only / not for human use." Decisive, verified fact.
2. **Zero human evidence of any kind; zero human topical evidence.** All efficacy is injected-mouse or cell-culture.
3. **~5.4 kDa — will not penetrate intact skin.** TAT solves cell entry, not barrier transport.
4. **Theoretical oncogenic/specificity risk** from non-targeted p53-axis perturbation (2025 structural work) + **dangerous grey-market self-injection culture.**

### Bottom line
The dossier does not overstate anything; if anything it correctly downgrades a peptide that grey-market vendors and longevity press hype. The mechanism is genuinely excellent science (B+), but for a **cosmetic brand** the answer is an unambiguous, well-evidenced **SKIP** — keep FOXO4-DRI as a science benchmark/reference (the FOXO4-p53 senolytic story), never as a formulation ingredient, and route any "senescence" positioning toward cosmetically legitimate senomorphics (Decapeptide-52) and botanical senotherapeutics. Two corrections applied on re-verification: (1) rejecting the inconsistent vendor molecular weights in favor of the CAS-registered value (C₂₂₈H₃₈₈N₈₆O₆₄, ~5,358 Da), and (2) fixing the route of the foundational Baar 2017 *Cell* experiments from "IP" to **IV** (follow-up studies are IP) — both immaterial to the SKIP verdict, which is grade **F for topical cosmetic use**.

**Independent re-verification note (2026-06-19):** All headline claims spot-checked against primary sources. Confirmed real and accurately represented: Baar 2017 *Cell* [1] (PubMed 28340339 — designed FOXO4-DRI, systemic injection in mice, restored fur/renal/fitness, neutralized doxorubicin toxicity, no topical test); Huang/Lin 2021 *Front Bioeng Biotechnol* [4] (PMC8116695 — 25 µM/5 d, human chondrocytes from 8 donors aged 15–73, SA-β-gal >40%→<5% in PDL9, PDL3 spared, in culture); Bourgeois 2025 *Nat Commun* [14] (PMC12216184 — targets p53TAD2, TAT contributes to binding, coupled folding of disordered partners, promiscuous hub shared with CBP/p300, MDM2/HDM2, BRCA2, HMGB1); identity facts (CAS, formula, MW, research-use-only) confirmed across multiple vendor/registry sources. No funding/independence red flags — the evidence base is academic, not industry-funded cosmetic studies; the only "human use" is uncontrolled grey-market self-injection, correctly flagged as anecdote/hazard, not data.
