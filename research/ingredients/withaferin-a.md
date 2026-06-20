# Ingredient: Withaferin A (Ashwagandha) (INCI: there is **no** "Withaferin A" cosmetic INCI — see §1)

**Researched:** 2026-06-19 · **Status:** ⬜ considering / ⬜ shortlisted / ☑ rejected (as an isolate) / ⬜ in a product
**Class:** Senotherapeutics & senolytics · **Slug:** `withaferin-a`

> Exhaustive literature review. Brutally honest on evidence quality. **Read this caveat first, because it
> inverts the usual senolytic story:** Withaferin A (WA) is a potent, *reactive* anticancer/anti-fibrotic
> drug molecule, not a gentle botanical antioxidant. Its single best-characterized skin-relevant action is
> that it **DECREASES type-I collagen synthesis** (it is being developed as an *anti-fibrotic*) — the exact
> opposite of what an anti-wrinkle "build collagen" cream wants. Its senolytic/longevity reputation rests on
> an **AI screen + fruit-fly lifespan + cancer-cell senescence-induction** data, much of which is actually
> about WA's *sister* withanolide (withanone), not WA itself. The **one human topical RCT that exists is for
> whole ashwagandha-root extract (KSM-66, 5% withanolides) — NOT isolated Withaferin A** — and it is
> industry-supported with physician-visual scoring. There is **zero human topical evidence for purified
> Withaferin A.** Treat "ashwagandha = anti-aging skincare hero" as a conflation of (a) a calming botanical
> root extract and (b) a cytotoxic drug molecule, marketed as if they were the same thing. They are not.

---

## 1. Identity

- **Common name:** Withaferin A (WA, WFA). The lead/most-studied member of the **withanolide** class — naturally occurring **C28 steroidal lactones** (ergostane-type). It is the headline bioactive of **Ashwagandha** (*Withania somnifera*; "Indian winter cherry"/"Indian ginseng"), also found in *Acnistus arborescens* and other Solanaceae. [1][2]
- **Chemistry:** molecular formula **C₂₈H₃₈O₆**, **MW ≈ 470.6 g/mol**, **CAS 5119-48-2**, PubChem CID 265237. IUPAC: (22R)-4β,27-dihydroxy-5,6β:22,26-diepoxy-5β-ergosta-2,24-diene-1,26-dione. [1][2]
- **Reactivity (this is the whole story for safety/stability):** WA is a **highly reactive electrophile** with **three Michael-acceptor / reactive sites** — the α,β-unsaturated ketone in the A-ring (the key nucleophile-trapping C3), the **5,6-β-epoxide** in the B-ring, and the **unsaturated δ-lactone** side chain. [1][2] It covalently modifies cysteine thiols on protein targets. This is *why* it works (covalent target engagement) and *why* it is cytotoxic and hard to formulate (it reacts with everything).
- **Solubility:** essentially **water-insoluble**; soluble in DMSO/ethanol/methanol — a poorly-soluble, lipophilic small molecule. [10] (Wikipedia/supplier data; precise logP not consistently reported — [partly unverified].)
- **Where it is in the plant matters:** **Withaferin A concentrates in the LEAVES**, not the roots. [1] Most "ashwagandha" supplements and the cosmetic RCT below use **ROOT** extract (standardized to total *withanolides*, of which WA is a minor fraction), so "ashwagandha extract" ≠ "withaferin A."
- **Key forms / what you'd actually buy:**
  - **Purified Withaferin A** (≥95–98%) — a research/pharma chemical, sold by Sigma, Abcam, Santa Cruz, MedChemExpress etc. **Not a registered cosmetic ingredient.**
  - **Withania somnifera root extract** — INCI **WITHANIA SOMNIFERA ROOT EXTRACT** (CAS 90147-43-6; CosIng function: *skin conditioning*); also **WITHANIA SOMNIFERA LEAF/ROOT EXTRACT** and **…EXTRACT**. These are the legitimate **cosmetic** ingredients (~0.1% market prevalence), standardized to *total withanolides* (commonly ~2.5–5%), of which WA is one. [11]
  - **Branded standardized roots:** **KSM-66®** (Ixoreal; root, ~5% withanolides) and **Sensoril®** (root+leaf, higher withanolide load) — the supplement/cosmetic-grade materials.
- **Nomenclature caution (critical):** **do not equate "Withaferin A" with "ashwagandha root extract."** And do not conflate WA with **withanone** or **withanolide A** — different molecules with different (sometimes opposite) safety and senescence profiles (see §4, §7). Much "ashwagandha is a senolytic" writing silently swaps between them.

---

## 2. Class & mechanism

WA is filed under **senotherapeutics/senolytics**, but its pharmacology is far broader and more aggressive than a typical "antioxidant flavonoid." It is best understood as a **multi-target covalent drug** that the longevity field has *flagged* (largely via in-silico screening) as a possible geroprotector.

**Validated molecular targets / mechanisms:**

- **Vimentin disruption (its signature, and the double-edged one for skin).** WA binds and covalently modifies a conserved cysteine (C328) in the vimentin rod-2B domain, collapsing the intermediate-filament network at **0.5–1.5 µM**. [3] Because vimentin **stabilizes type-I collagen mRNA** (LARP6-dependent), disrupting it **shortens collagen mRNA half-life and lowers collagen output** — see §3/§4. This is *anti-fibrotic* pharmacology. [3]
- **NF-κB inhibition via covalent IKKβ blockade.** WA alkylates **Cys179 in IKKβ**, preventing IκBα degradation and NF-κB nuclear translocation; it also inhibits the 20S proteasome's chymotrypsin-like activity. Net effect: strong suppression of NF-κB-driven inflammation (TNF-α, IL-6, COX-2, MMPs). [6][7] This is the basis of its **anti-inflammatory / anti-SASP** claims.
- **Hsp90 inhibition & proteostasis.** WA binds Hsp90, destabilizing client oncoproteins — part of its anticancer profile (and a flag that it is a real cytotoxic agent, not a cosmetic conditioner). [2]
- **TGF-β/Smad suppression.** WA inhibits TGF-β1-induced phosphorylation of TGF-βRI and Smad3, blocking pro-fibrotic collagen-gene transcription. [3] Again: **anti-collagen**, by design.
- **Pigmentation pathway shutdown.** WA blocks **c-KIT autophosphorylation** (stem-cell-factor signaling) and the **endothelin-1 → Raf-1/MEK/ERK/MITF/CREB** cascade in melanocytes, suppressing tyrosinase/TRP1/DCT/PMEL17 and melanin. [8][9] A genuine multi-node anti-melanogenic mechanism (in vitro).
- **Senescence — and here the data get slippery.** WA was tagged a **rapamycin/metformin mimetic & candidate senolytic** by a deep-learning transcriptomic screen (Aliper/Zhavoronkov 2017, Insilico Medicine), not by direct senescence-clearance experiments. [12] In cancer cells, WA *analogues* (e.g. W-2b) **induce** premature senescence (Chk2/p21) — the opposite direction from a senolytic. [13] The actual "decelerates fibroblast senescence / lowers p21" data attributed to ashwagandha is for **withanone**, not WA. [14] So WA's "senolytic" filing is **mechanistically plausible but largely inferential** for WA specifically.

**Net cell-level story (honest version):** WA is a covalent, multi-target inhibitor that **quiets NF-κB inflammation, blocks melanogenesis, disrupts vimentin, and lowers collagen/TGF-β signaling**, and is *computationally predicted* to act senolytically/geroprotectively. Most of this is anticancer/anti-fibrotic biology repurposed onto a skin-aging narrative — and one core action (collagen suppression) actively cuts against dermal anti-aging.

---

## 3. Hallmarks of skin aging targeted

| Hallmark | Targeted? | Basis / honest caveat |
|---|---|---|
| **Inflammaging** | ✅ (mechanistic/in-vitro) | Strong covalent NF-κB/IKKβ inhibition; ↓IL-6, ↓MMP-9 in human dermal fibroblasts in vitro [6][7][5]; oral ↓CRP/IL-6/TNF-α for *ashwagandha* in humans [14] |
| **Cellular senescence** | ⚠️ (inferred / wrong-compound) | WA = AI-predicted senolytic/metformin-mimetic [12]; but direct senescence-deceleration data are for **withanone** [14], and WA *analogues* **induce** senescence in cancer cells [13]. No senescence-clearance shown in human skin. |
| **Oxidative stress** | ⚠️ (indirect) | Ashwagandha ↑Nrf2/SOD, ↓MDA (mostly oral/systemic) [14]; WA itself is a *reactive electrophile*, so "antioxidant" is via Nrf2 induction, not radical scavenging — and high doses are *pro*-oxidant/cytotoxic |
| **Collagen / ECM loss** | ❌ **Counterproductive** | WA **reduces** type-I collagen: ↓collagen α1(I)/α2(I) mRNA half-life ~3–4×, ↓protein 2–4× in fibroblasts at 0.5–1.5 µM [3]; ↓TGF-β/Smad3 [3]. This is *anti-fibrotic* — the wrong direction for building dermal collagen. |
| **Pigmentation / tone** | ✅ (in-vitro, mechanistically strong) | Blocks c-KIT & endothelin-1 melanogenesis; ↓tyrosinase/TRP1/DCT/PMEL17/melanin in human melanocytes + epidermal equivalents [8][9]. No isolated-WA human in-vivo proof. |
| **Photoaging** | ⚠️ (indirect/in-vitro) | WA blocks UVB-driven keratinocyte→melanocyte cytokine crosstalk (ET-1, IL-1α, IL-6/8, GM-CSF) [9]; anti-MMP-9 in vitro [5]. Whole-root-extract human photoaging RCT exists [4] but is not WA. |
| **Barrier decline** | ⚠️ (extract only) | KSM-66 root-extract lotion ↓TEWL 15% vs placebo in humans [4] — extract, not WA; no WA-specific barrier data |
| **Hydration** | ⚠️ (extract only) | Same root-extract RCT: +20.7% corneometer hydration vs placebo [4]; no WA-specific data |
| **Mitochondrial decline** | ⚠️ (asserted, weak) | Reviews assert mito support via Nrf2; "no independent mitochondrial outcome studies" cited [14] |
| **Glycation / AGEs** | ❌ | No meaningful WA-specific anti-glycation evidence located [unverified] |
| **Microbiome** | ❌ | No meaningful evidence |

---

## 4. Evidence review by tier  ← core of this dossier

**Overarching honesty flag.** The evidence pyramid here is *upside-down* relative to the marketing. The deep, high-quality data are **anticancer and anti-fibrotic** (i.e. reasons to be *cautious*). The skin-aging data are: (a) genuinely strong **in-vitro pigmentation** mechanism for WA; (b) **anti-collagen** in-vitro/animal data for WA (a red flag); (c) **one human topical RCT — but for whole root extract, not WA**; and (d) an in-vitro-only topical liposomal WA formulation. **No human topical study of purified Withaferin A exists** (2026-06). Keep the tiers — and the "WA vs whole-extract" distinction — strictly separate.

### Tier 1 — In-vitro (cells)

**Challa, Bargagna-Mohan, Mohan et al. (2012), *PLOS ONE* — the collagen-reduction paper. [3]**  *(Most decision-relevant study in this whole dossier.)*
- In **human lung, skin, and cardiac fibroblasts**, WA disrupted vimentin filaments at **0.5–1.5 µM**.
- **Reduced collagen α1(I) mRNA half-life ~3-fold (to ~8 h) and α2(I) ~4-fold (to ~6 h);** lowered collagen **protein 2–3× (lung fibroblasts), up to 4× (scleroderma fibroblasts).**
- Mechanism: vimentin disruption (destabilizing collagen mRNA) **plus** inhibition of **TGF-β1→TGF-βRI→Smad3** signaling.
- **Interpretation for us:** this is a deliberate **anti-fibrotic** mechanism. For an anti-wrinkle product whose thesis is preserving/supporting dermal collagen, an active that *demonstrably reduces collagen synthesis at low µM* is a direct conflict — not a benefit.

**Melanogenesis (Imokawa group and collaborators).** [8][9]
- WA **abolished stem-cell-factor (SCF)-stimulated pigmentation of human epidermal equivalents** by blocking **c-KIT autophosphorylation** → ↓Shc/Raf-1/MEK/ERK/MITF/CREB → ↓tyrosinase/TRP1/DCT/PMEL17/melanin. [8]
- In keratinocyte↔melanocyte co-culture, WA (with astaxanthin) attenuated **UVB-induced endothelin-1** secretion and downstream **Raf-1/MEK/ERK/MITF/CREB**, plus ↓IL-1α, IL-6/8, GM-CSF; post-UVB WA blunted tyrosinase upregulation. [9]
- Genuinely **multi-node anti-melanogenic** — but **cell/3D-equivalent only**, no isolated-WA human in-vivo proof.

**NF-κB / anti-inflammatory cell biology.** WA covalently inhibits **IKKβ (Cys179)** and the 20S proteasome, suppressing NF-κB and its downstream cytokines/MMPs. [6][7] This underpins the anti-inflammatory and "anti-SASP" rationale, but it is generic anti-NF-κB pharmacology, demonstrated mostly in non-skin and cancer/endothelial cells.

**Withaferin A-loaded liposomal gel (Marwah et al., 2025, *Br. J. Biomed. Sci.*).** [5] — *the only "topical WA for skin" study, and it is in-vitro only.*
- Liposomes: size **~117–122 nm**, PDI ~0.15, **entrapment ~70–73%**, near-neutral zeta. WA loaded at 1 mg/mL (WA-L) and 5 mg/mL (WA-H).
- TNF-α-stimulated **HDFa**: **IL-6** 40.1→**14.3 (WA-L)/10.4 (WA-H) pg/mL**; **MMP-9** 408.8→**243/195 pg/mL**. Similar IL-6 drop in HUVECs.
- **No Franz-cell/ex-vivo skin permeation** (a permeable-insert release model only); authors flag ex-vivo/in-vivo permeation as *future work*.
- **Cytotoxicity:** good viability only at **≤1 µM**; **reduced viability at 5 µM** — a narrow safety window.
- **Bottom line:** confirms WA can be encapsulated and quiets inflammatory cytokines in skin cells, but it is **in-vitro, narrow-margin, no penetration data, no efficacy endpoint.**

**Bottom line, Tier 1:** WA is a real, potent in-vitro **anti-inflammatory and anti-melanogenic** agent — and an equally real **anti-collagen** agent. The cell data are internally consistent and pharmacologically credible; they just don't all point toward "anti-aging."

### Tier 2 — Animal

- **Anti-fibrosis (collagen ↓), mouse.** In the same Challa 2012 work, **WA 4 mg/kg/day × 2 wk i.p. reduced isoproterenol-induced myocardial fibrosis ~50%** [3] — in-vivo confirmation that WA's systemic action is **collagen-lowering/anti-fibrotic.**
- **Geroprotection, *Drosophila* (Koval/Moskalev et al., 2021, *Aging*).** [15] WA in food at 1/10/100 µM; **median lifespan +7.7% (10 µM) and +9.6% (100 µM) in MALES only; max lifespan +11.1%;** **no effect in females.** Modulated PrxV, Gadd45, Hsp68/83, Ku80. Authors note a **"multidirectional" effect** — *reduced* stress resistance at some doses/ages (a trade-off, not clean protection). Invertebrate, sex-specific, narrow.
- **Other model-organism lifespan:** review-level reports of *C. elegans* mean lifespan **~+20%** for ashwagandha (extract, not isolated WA); **no direct mouse lifespan-extension data** for WA — only disease-model improvements. [14]
- **Oral PK/safety, mice.** Oral WA is **poorly bioavailable** (low %, rapid metabolism); sub-acute oral dosing tolerated to high mg/kg in some reports. [16] *(Primary PK page was CAPTCHA-blocked on fetch; figures from secondary safety reviews — treat exact numbers as [partly unverified].)*
- **No animal topical skin-aging study of WA located.**

**Bottom line, Tier 2:** the strongest in-vivo WA effect relevant to skin is **collagen reduction (anti-fibrosis)**. The "lifespan" data are fruit-fly, male-only, modest, and trade-off-laden. Nothing topical, nothing skin-aging.

### Tier 3 — Human, ORAL (ashwagandha; essentially none for isolated WA)

- Robust human RCT literature exists for **oral ashwagandha root extract** (stress/cortisol, sleep, strength, and **systemic anti-inflammatory markers: ↓CRP >30%, ↓IL-6/TNF-α**, ↑SOD, ↓MDA). [14] These are **whole-extract** trials, **not Withaferin A**, and **none has a skin-aging endpoint.**
- **No human oral trial of purified Withaferin A** with any skin outcome located. (Isolated WA has been explored in early oncology contexts, not dermatology/cosmetics.)

**Bottom line, Tier 3:** humans tolerate oral *ashwagandha* and show systemic anti-inflammatory/antioxidant shifts — but this is the *extract*, not WA, and there is **no oral-→-skin-aging evidence.**

### Tier 4 — Human, TOPICAL

**The single human topical RCT is for whole root extract, NOT Withaferin A — and it is the source of every viral "ashwagandha reduces wrinkles 55%" figure.**

**Narra, Naik, Ghatge (2023), *Cureus* — 8% ashwagandha-root-extract lotion, photoaged facial skin. [4]**
- **Design:** randomized, double-blind, placebo-controlled; **N=56 randomized (53 evaluable: 27 active / 26 placebo)**; **60 days**; single site (Hyderabad).
- **Active = 8% KSM-66® *root* extract standardized to 5% withanolides** — **a whole extract, not isolated WA** (WA is a minor component, and concentrates in *leaves* anyway). [4][1]
- **Results vs placebo (statistically significant unless noted):** physician total score −74.7% vs −48.7% (p<0.0001); **wrinkles −55.9% vs −24.1% (p=0.006)**; pores −66.5% vs −42.3% (p=0.023); brightness/tone −77.0% vs −47.7% (p=0.005); pigmentation −80.6% vs −60.3% (p=0.009); **TEWL −15.1% vs −8.3% (p<0.0001)**; **corneometer hydration +20.7% vs +9.5% (p<0.0001)**; **elasticity (R2) +16.3% vs +3.7% (p<0.0001)**; **melanin index −2.8% vs −1.8% (p=0.969, NOT significant).**
- **Honest caveats:**
  1. **It's the extract, not WA** — you cannot cite this for "Withaferin A."
  2. **Industry-supported:** investigational product supplied by **Ixoreal Biomed** (the maker of KSM-66); "no competing interests" declared, but the sponsor stake is obvious.
  3. The big percentages are largely **physician *visual-scoring* deltas** (subjective grading), not all instrumental — the dramatic "wrinkles/pores/pigmentation −55–80%" are score reductions; only TEWL/hydration/elasticity are instrument-measured.
  4. **N small (53), young cohort (under ~40), 60 days, single site.**
  5. Notably, the **instrumental melanin index change was NOT significant** — despite WA's strong *in-vitro* anti-melanogenic mechanism — a useful real-world reality check.
- **Adverse events:** mild local reactions (irritation/erythema/swelling) in 4 active / 5 placebo, all self-resolving.

**What is actually proven for TOPICAL human use of WITHAFERIN A:** **nothing.** The human topical data are for a **standardized root extract**; the only WA-specific topical work is **in-vitro liposomal** [5]. Bridging "ashwagandha root lotion improved photoaged skin scores" to "Withaferin A is an effective topical anti-aging active" is **two inferences stacked** (extract→isolate, and visual-score→real effect).

---

## 5. Topical bioavailability / penetration

- **Poorly water-soluble, lipophilic, chemically reactive/unstable** — a hard delivery trio. Reviews of WA dermatology explicitly cite **"poor aqueous solubility, chemical instability, and insufficient skin permeability"** as the blockers. [5]
- **MW ~470 Da** is just under the rule-of-500, so size is borderline-OK; the limiters are **solubility, reactivity (it covalently consumes itself), and stability.**
- The only published WA skin-delivery work is **liposomal encapsulation** (~120 nm, ~70% entrapment) — and even that paper provides **no actual skin-permeation/retention data** (release-through-membrane only) and flags ex-vivo permeation as unfinished. [5]
- **Implication:** a naked-WA serum would likely deliver little intact active, react with formula components, and have a **very narrow cytotoxicity window** (in-vitro cell margin ≤1 µM [5]). Any credible topical WA needs encapsulation **and** a dose low enough to avoid the cytotoxic range — which also means low enough that efficacy is unproven. The **whole-root-extract** route sidesteps this by delivering a low-WA, multi-component botanical (and that is what the human RCT actually used).

---

## 6. Formulation

- **Effective concentration (isolated WA): unknown and risky.** In-vitro bioactivity is **~0.1–1.5 µM** (anti-inflammatory/anti-melanogenic), but **cytotoxicity appears by ~5 µM** [5][3] — a *narrow* window. There is **no established cosmetic use level** for purified WA. For the **extract**, the human data point is **8% root extract (≈5% withanolides)** [4].
- **pH / stability — the hard part:** WA's **epoxide + two Michael-acceptor enones** make it reactive toward nucleophiles, thiols, amines, and prone to degradation; expect sensitivity to pH extremes, heat, light, and nucleophilic excipients. Anhydrous/encapsulated, antioxidant-protected, opaque/airless packaging is the only sane approach for an isolate. (For root extract, standard botanical-extract stability rules apply.)
- **Pairings (if pursuing the *extract* as a soothing/tone actor):**
  - **Niacinamide** — complementary tone/barrier, well-tolerated. See [`niacinamide.md`](niacinamide.md).
  - **Centella / panthenol / beta-glucan** — soothing co-actives matching the "calm/adaptogen" story. [`centella-asiatica.md`](centella-asiatica.md), [`panthenol.md`](panthenol.md), [`beta-glucan.md`](beta-glucan.md).
  - **Brightening actives** — if leaning on the (in-vitro) anti-melanogenesis angle, pair with evidenced brighteners rather than relying on WA. [`brightening-peptides.md`](brightening-peptides.md), [`licorice-extract.md`](licorice-extract.md).
- **Conflicts:** **do not pair an anti-collagen actor with your collagen-support hero** — co-formulating WA with retinoids/peptides/GHK-Cu whose pitch is *supporting* collagen is self-contradicting (WA *lowers* collagen synthesis [3]). Avoid high-nucleophile systems that will quench the reactive WA.
- **Sensory:** root extract is a typical brown-ish botanical (can tint/odor at higher %); isolate would be a low-% encapsulated active driven by the base.

---

## 7. Safety

- **WA is a cytotoxic drug molecule, not a benign cosmetic conditioner.** It is an active **anticancer agent** (apoptosis induction across many cancer lines) and a **reactive electrophile**; a 2025 paper title bluntly notes **"Withaferin-A kills neuronal cells,"** an off-target cytotoxicity flag. [17] Its in-vitro cell-viability window is narrow (≤1 µM safe, cytotoxic ~5 µM [5]). This is the central safety problem with the **isolate**.
- **Hepatotoxicity (the ashwagandha-category risk).** There are **documented case reports of ashwagandha-associated liver injury** (NIH LiverTox; multiple case series), generally mild-moderate, self-limited on discontinuation, often confounded by polypharmacy/contamination — **mostly an oral-supplement concern.** Mechanistically, **withanone** (not WA) is the chief hepatotoxicity suspect (DNA-adduct-forming electrophile). [18] Relevant here mainly as brand/category reputational risk and a reason to control the actual withanolide profile of any extract.
- **Pregnancy/breastfeeding — explicit contraindication.** Ashwagandha is **traditionally an abortifacient / uterine stimulant** and is widely advised **against in pregnancy.** Do **not** market any WA/ashwagandha product as pregnancy-safe; flag avoid-in-pregnancy. [14][18]
- **Topical irritation/sensitization:** in the root-extract RCT, mild local reactions occurred at similar rates to placebo (4 vs 5) [4] — i.e. the *extract* lotion was reasonably tolerated. **No HRIPT/patch data for purified WA**; given its reactivity and electrophilicity, **sensitization potential is plausible and unproven** for the isolate.
- **Sun sensitivity:** not a photosensitizer/exfoliant; if anything its anti-melanogenic/anti-inflammatory actions are protective in vitro. Does not replace SPF — see [`sunscreen-photoprotection.md`](sunscreen-photoprotection.md).
- **Sourcing/quality:** botanical provenance and **standardized, characterized withanolide profile** (WA vs withanone vs withanolide A) matter for both efficacy *and* safety; demand heavy-metal/pesticide and withanolide-assay specs.

---

## 8. Regulatory & claims (per CLAUDE.md guardrails)

**Two different regulatory objects — keep them apart:**
1. **Withania somnifera root (or leaf/root) extract** — a recognized **cosmetic ingredient** (CosIng; *skin conditioning*). [11] Usable in cosmetics.
2. **Purified "Withaferin A"** — **not** an established cosmetic INCI; it is a pharmacological/research chemical with **anticancer/anti-fibrotic** activity. Building a face product around the isolate invites both **regulatory** (drug-like molecule) and **claims** scrutiny.

**The claims line (US FDA):** intended use decides cosmetic vs drug. Structure/function claims ("removes senescent cells," "rebuilds collagen," "anti-fibrotic," "reverses aging") make it a **drug**; there is no OTC anti-aging monograph.

- ✅ **Safer cosmetic language (for the *extract*):** "soothing adaptogenic botanical," "helps calm the look of stressed skin," "supports a more even-looking tone," "helps visibly improve the appearance of photo-aged skin," "antioxidant-supporting botanical."
- ⚠️ **Risky / drug-like — avoid or legal-review:**
  - "**senolytic / clears senescent cells**" — for WA this is **AI-predicted, not demonstrated** (and the senescence-*deceleration* data are for *withanone*) → unsupported + structure/function.
  - "**boosts/rebuilds collagen**" — **directly contradicted by the evidence**: WA *reduces* collagen synthesis [3]. This would be a *false* claim, not just a risky one.
  - "**reduces wrinkles 55% / clinically proven anti-aging**" — borrows a **whole-root-extract, industry-supported, visual-score** RCT [4] and silently attributes it to "Withaferin A." Misleading substantiation.
  - "**metformin/rapamycin for your skin / longevity molecule**" — borrows an *in-silico* prediction [12] and fruit-fly data [15]; drug-mimetic framing.
- **"Adaptogen"** is a marketing/traditional term, not an evidenced cosmetic mechanism — use lightly and never as a structure/function claim.
- **EU/UK:** WITHANIA SOMNIFERA ROOT EXTRACT is in CosIng; claims must meet the EU Cosmetics Claims Regulation (evidential support, no misleading "biological age" promises). Purified WA's cytotoxic profile would warrant a careful safety dossier.

See [`../../brand/glossary.md`](../../brand/glossary.md) claim cheat-sheet.

---

## 9. Sourcing & cost

- **Withania somnifera root extract** is **cheap, abundant, and commoditized** (huge ayurvedic/nutraceutical supply chain; branded KSM-66/Sensoril add cost + standardization + a clinical paper). **Low–mid cost tier** as a cosmetic botanical.
- **Purified Withaferin A** is a **research/pharma chemical** — expensive per gram, sold in mg–g lots by reagent suppliers; **not produced at cosmetic scale or grade**, and not a registered cosmetic ingredient. Going this route means custom sourcing, an encapsulation system, and a safety dossier — **high cost and complexity for unproven topical benefit.**
- **IP:** WA itself is a natural molecule; specific **anti-fibrotic / senolytic / "withaferin compositions for prevention of aging" uses and delivery systems carry patents** — FTO review needed if leaning on a WA mechanism claim. Branded *extracts* (KSM-66/Sensoril) are trademarked, licensable inputs.
- **Quality spec:** standardize on **assayed withanolide profile** (WA %, withanone %), heavy metals, pesticides, and botanical authentication.

---

## 10. Hype vs. evidence

| Marketing claim | Reality |
|---|---|
| "Ashwagandha / Withaferin A — senolytic skin-longevity active" | WA is an **AI-predicted** senolytic/metformin-mimetic [12]; direct senescence-*deceleration* data are for **withanone**, not WA [14]; WA analogues actually **induce** senescence in cancer cells [13]. **Not demonstrated in human skin.** |
| "Boosts collagen / firms by building collagen" | **False for WA** — it *reduces* type-I collagen mRNA/protein and blocks TGF-β/Smad; it's an **anti-fibrotic** [3]. The opposite of the claim. |
| "Clinically proven to reduce wrinkles 55% / hydrate / firm" | That RCT used **8% whole ROOT extract (KSM-66, 5% withanolides), not Withaferin A**, was **industry-supported**, and the headline numbers are **physician visual scores** [4]. Real but mis-attributed if pinned on "Withaferin A." |
| "Brightens / fades pigmentation" | Strong **in-vitro** anti-melanogenic mechanism (c-KIT/ET-1) [8][9] — but the human RCT's **instrumental melanin change was NOT significant** [4]. Mechanism ≫ human proof. |
| "Calming adaptogen that soothes stressed skin" | Best-supported angle: real NF-κB/IL-6 suppression in vitro [5][6] + decent tolerability of the *extract* lotion [4]. Defensible as a **soothing botanical** (cosmetic language). |
| "Longevity molecule that extends lifespan" | Lifespan data are **fruit-fly, males only, +8–10%, with trade-offs** [15]; *C. elegans* ~+20% is **extract** [14]; **no mouse/human lifespan data for WA.** |
| "Natural and gentle" | WA is a **reactive, cytotoxic anticancer/anti-fibrotic drug molecule** (kills neurons [17]; narrow cell-viability window [5]) — "natural" ≠ "gentle." |

**Independent reality:** *Ashwagandha root extract* is a legitimate, low-risk **soothing/antioxidant cosmetic botanical** with one supportive (if industry-tinged) human topical RCT. **Withaferin A the isolate** is a different thing entirely — a potent covalent drug whose best-characterized skin action (**collagen reduction**) is *anti-*aging-cream, whose senolytic billing is **predictive not proven**, and which has **no human topical evidence and a narrow safety margin.** The marketing fuses the two; the evidence says don't.

---

## 11. Verdict for the brand

❌ **Skip Withaferin A as an isolate / hero. ⚠️ The whole *Withania somnifera* root extract is a legitimate but minor *supporting* (soothing/tone) botanical — not a longevity hero, and never a "collagen" claim.**

- **Why the isolate is a skip:** (1) its best-evidenced skin action is **reducing collagen synthesis** [3] — it is literally an anti-fibrotic, which **contradicts** a barrier-repair/firming anti-aging thesis; (2) its senolytic/longevity reputation is **AI-predicted + fruit-fly + wrong-compound (withanone)** — **not** demonstrated senescence clearance in skin [12][14][15]; (3) it is a **reactive, cytotoxic** molecule with a **narrow safety window** and off-target toxicity [5][17]; (4) **no human topical WA evidence exists**; (5) it is hard to formulate (reactive, insoluble, unstable) and not a registered cosmetic ingredient. The risk/benefit is upside-down for a credibility-first brand.
- **Where the *extract* could play (conditional, minor):** as a **soothing, antioxidant-supporting "adaptogen" botanical** with a **plausible tone/brightening** story (in-vitro) and **one human RCT** behind a *root-extract* lotion [4]. That is a **supporting** role at most — calm/comfort/tone — with strictly cosmetic language ("soothes the look of stressed skin," "supports even-looking tone"), never collagen/senolytic/anti-aging-structure claims.
- **Longevity relevance:** **High in narrative buzz, low in defensible topical substance, and partly self-contradicting.** "Ashwagandha senolytic" sounds perfect for a skin-longevity brand, but the honest read is that the *molecule* cited (WA) doesn't do what the marketing implies (and does the opposite for collagen), while the *thing with human data* (root extract) is a soothing botanical. For a brand built on **claims honesty**, leaning on "Withaferin A senolytic" would be exactly the kind of borrowed/inverted claim we exist to avoid.
- **Gating conditions if the *extract* is ever used:** (1) frame as **soothing/tone botanical**, not anti-aging hero; (2) use a **standardized, assayed** extract with a controlled withanolide profile (watch withanone for liver-safety optics); (3) **avoid-in-pregnancy** flag; (4) **never** co-message with a "build collagen" hero or use the word "senolytic"/"Withaferin A clinically proven."

Log in [`../../ideas/not-considering.md`](../../ideas/not-considering.md) (Withaferin A isolate) and, if pursued, the extract in [`../../ideas/considering.md`](../../ideas/considering.md) as a supporting botanical.

---

## 12. Sources

1. PubChem / Wikipedia — Withaferin A chemical identity (C₂₈H₃₈O₆; MW 470.6; CAS 5119-48-2; steroidal lactone/withanolide; reactive A-ring enone + B-ring epoxide + unsaturated lactone; from *Withania somnifera* [conc. in leaves] & *Acnistus arborescens*). https://pubchem.ncbi.nlm.nih.gov/compound/265237 · https://en.wikipedia.org/wiki/Withaferin_A
2. ACS "Molecule of the Week — Withaferin A"; supplier monographs (Sigma 681535, Abcam ab120644, Santa Cruz). (Identity, reactivity, Hsp90/NF-κB targeting, anticancer profile.) https://www.acs.org/molecule-of-the-week/archive/w/withaferin-a.html · https://www.sigmaaldrich.com/US/en/product/mm/681535
3. Challa AA, Bargagna-Mohan P, Mohan R, et al. (2012). "Withaferin-A Reduces Type I Collagen Expression In Vitro and Inhibits Development of Myocardial Fibrosis In Vivo." *PLOS ONE* 7(8):e42989. (Vimentin disruption 0.5–1.5 µM in lung/skin/cardiac fibroblasts; ↓collagen α1(I)/α2(I) mRNA half-life ~3–4×; ↓protein 2–4×; ↓TGF-β/Smad3; **mouse 4 mg/kg/day i.p. × 2 wk → ↓myocardial fibrosis ~50%**. The collagen-reduction / anti-fibrotic paper.) DOI:10.1371/journal.pone.0042989 · https://pmc.ncbi.nlm.nih.gov/articles/PMC3416765/
4. Narra K, Naik SK, Ghatge AS (2023). "A Study of Efficacy and Safety of Ashwagandha (Withania somnifera) Lotion on Facial Skin in Photoaged Healthy Adults." *Cureus* 15(2):e34874. (RCT, N=56→53 evaluable, 60 d; **8% KSM-66 ROOT extract, 5% withanolides — NOT isolated WA**; wrinkles −55.9% vs −24.1%, TEWL −15.1% vs −8.3%, hydration +20.7% vs +9.5%, elasticity +16.3% vs +3.7% vs placebo; **melanin index NS**; **Ixoreal-supported**; mostly physician visual scoring.) https://pmc.ncbi.nlm.nih.gov/articles/PMC10017910/
5. Marwah M, et al. (2025). "Formulation and In Vitro Characterisation of Withaferin A-Loaded Liposomal Gels for the Topical Management of Chronic Inflammatory Skin Conditions." *British Journal of Biomedical Science* 82:14847. (Liposomes ~117–122 nm, ~70–73% entrapment; HDFa: IL-6 40.1→14.3/10.4, MMP-9 408.8→243/195 pg/mL; **in-vitro only, no skin-permeation data; cytotoxic ~5 µM, safe ≤1 µM**; notes WA's poor solubility/instability/permeability.) https://pmc.ncbi.nlm.nih.gov/articles/PMC12702788/
6. Heyninck K, Lahtela-Kakkonen M, Van der Veken P, Haegeman G, Vanden Berghe W (2014). "Withaferin A inhibits NF-κB activation by targeting cysteine 179 in IKKβ." *Biochem. Pharmacol.* (Covalent IKKβ-Cys179 alkylation → ↓NF-κB.) PMID 25159986 · https://pubmed.ncbi.nlm.nih.gov/25159986/
7. Tocris/MedChemExpress monographs — Withaferin A as NF-κB/IκB inhibitor and 20S-proteasome inhibitor; vimentin-targeting. https://www.tocris.com/products/withaferin-a_2816 · https://www.medchemexpress.com/Withaferin_A.html
8. Imokawa group (2014). "Withaferin A abolishes the stem cell factor-stimulated pigmentation of human epidermal equivalents by interrupting the auto-phosphorylation of c-KIT in human melanocytes." *Arch. Dermatol. Res.* 306(8):767–778. (↓c-KIT→Shc/Raf-1/MEK/ERK/MITF/CREB; ↓tyrosinase/TRP1/DCT/PMEL17/melanin; human melanocytes + 3D epidermal equivalents; in-vitro.) https://link.springer.com/article/10.1007/s00403-014-1518-y
9. (Imokawa group) "Astaxanthin and withaferin A block paracrine cytokine interactions between UVB-exposed human keratinocytes and human melanocytes via attenuation of endothelin-1 secretion and its downstream intracellular signaling." *Cytokine* (2015). (↓ET-1, IL-1α, IL-6/8, GM-CSF; ↓Raf-1/MEK/ERK/MITF/CREB; post-UVB ↓tyrosinase; co-culture in-vitro.) https://www.sciencedirect.com/science/article/abs/pii/S1043466615000654
10. Supplier/Wikipedia solubility & physicochemistry (water-insoluble; soluble DMSO/ethanol; reactive electrophile). https://en.wikipedia.org/wiki/Withaferin_A · https://www.abcam.com/en-us/products/biochemicals/withaferin-a-from-withania-somnifera-ab120644
11. CosIng / INCI Beauty / SpecialChem — WITHANIA SOMNIFERA ROOT EXTRACT (CAS 90147-43-6; function: skin conditioning; ~0.1% market prevalence); also WITHANIA SOMNIFERA LEAF/ROOT EXTRACT. https://incibeauty.com/en/ingredients/20313-withania-somnifera-root-extract · https://www.specialchem.com/cosmetics/inci-ingredients/withania-somnifera-root-extract
12. Aliper A, Jellen L, Cortese F, … Moskalev A, Zhavoronkov A (2017). "Towards natural mimetics of metformin and rapamycin." *Aging (Albany NY)* 9(11):2245–2268. (Deep-learning LINCS screen of >800 natural compounds; **withaferin A predicted as both a metformin- and rapamycin-mimetic** — an *in-silico* geroprotector prediction.) PMID 29165314 · https://pubmed.ncbi.nlm.nih.gov/29165314/
13. (Ring-A fused Withaferin A isoxazoline analogues) "Induction of Premature Senescence by W-2b in Proliferating Cancer Cells." *Sci. Rep.* (2017) 7:13854. (WA analogue **induces** Chk2/p21-dependent senescence in cancer cells — opposite of senolysis.) https://www.nature.com/articles/s41598-017-13664-x
14. Vittal M, Vinciguerra M (2025). "Enhancing healthspan with Ashwagandha (Withania somnifera): a comprehensive review of its multifaceted geroprotective benefits." *Biogerontology* 26(5):179. (Senescence deceleration / ↓p21 attributed to **withanone**, preclinical; Nrf2/SOD↑, MDA↓; ↓CRP>30%, ↓IL-6/TNF-α [clinical, extract]; telomerase +~45% in vitro; *C. elegans* lifespan ~+20% [extract]; cites the 8% topical RCT; no mouse WA lifespan data.) https://pmc.ncbi.nlm.nih.gov/articles/PMC12417257/
15. Koval L, Zemskaya N, Aliper A, Zhavoronkov A, Moskalev A (2021). "Evaluation of the geroprotective effects of withaferin A in Drosophila melanogaster." *Aging (Albany NY)* 13(2):1817–1841. (WA 1/10/100 µM in food; **median lifespan +7.7%/+9.6% MALES only; max +11.1%; no female effect; "multidirectional"/trade-off stress responses**; PrxV/Gadd45/Hsp/Ku80 modulation.) PMID 33498013 · https://www.aging-us.com/article/202572/text
16. "Safety, toxicity and pharmacokinetic assessment of oral Withaferin-A in mice" (2022/2023). (Oral WA poorly bioavailable; sub-acute tolerability reported — **exact PK figures [partly unverified]; source page CAPTCHA-blocked on fetch**.) https://pmc.ncbi.nlm.nih.gov/articles/PMC9742883/
17. "Withaferin-A kills neuronal cells: An off-putting facet of Withania somnifera as a neuroprotectant." (2025) *PubMed* 40695418. (Off-target neuronal cytotoxicity — flags that WA is a cytotoxic, not benign, molecule. Abstract via PubMed; full text not fetched.) https://pubmed.ncbi.nlm.nih.gov/40695418/
18. NIH LiverTox — "Ashwagandha"; plus safety reviews (Frontiers Nutrition 2025 meta-analysis; *Phytotherapy Research* 2025 adverse-effects reviews) and "DNA damage by Withanone as a potential cause of liver toxicity…" (*Curr. Res. Toxicol.* 2021). (Rare, mostly mild-moderate self-limited ashwagandha hepatotoxicity, **withanone**-implicated; pregnancy abortifacient caution.) https://www.ncbi.nlm.nih.gov/books/NBK548536/ · https://www.sciencedirect.com/science/article/pii/S2666027X21000074

---

## Evidence verification (adversarial)

**Verified:** 2026-06-19. Independent adversarial re-check of every headline claim against primary sources (PMC, PLOS ONE, *Aging*, *Cureus*, *Br. J. Biomed. Sci.*, PubMed, CosIng). Where a primary page was CAPTCHA/403-blocked it is flagged in-text and in the source list.

**Second-pass independent re-verification (2026-06-19):** the three load-bearing primary sources were re-fetched and re-confirmed from scratch by a separate adversarial pass: [3] Challa 2012 (vimentin collapse at ~1 µM; collagen α1(I) mRNA half-life cut 3× to ~8 h, α2(I) 4× to ~6 h; ↓protein 2–4×; mouse 4 mg/kg/day i.p. × 14 d → ~50% ↓ myocardial fibrosis, ~7%→~3.5%) — **WA is anti-fibrotic, confirmed**; [4] Narra 2023 (8% KSM-66 **root** extract, 5% withanolides, **not isolated WA**; wrinkles p=0.006, TEWL/hydration/elasticity p<0.0001, **melanin index NS p=0.969**; Ixoreal-supplied; N=56→53; 60 d; final cohort ~18–40) — **extract-not-WA, industry-supported, melanin-NS all confirmed**; [15] Koval 2021 (Drosophila median +7.7%/+9.6% at 10/100 µM, max +11.1%, **no female effect**, multidirectional stress-resistance trade-offs) — **male-only, modest, trade-off-laden, confirmed**. No discrepancies found; no overstated claim required softening (the dossier is, if anything, conservatively skeptical). The grade below stands on independent evidence, not the author's self-audit alone.

### Overall evidence grade for "does topical Withaferin A work as an anti-aging active?": **D / Skip-grade**

Split, because the conflation is the whole problem:

- **Withaferin A (isolate), topical human anti-aging efficacy:** **F/D** — *zero* human topical studies; the only topical WA work is in-vitro liposomal with no permeation/efficacy data. And its best in-vivo skin-relevant action (**collagen reduction**) points the *wrong way*.
- **Withaferin A mechanistic biology (anti-inflammatory, anti-melanogenic, anti-fibrotic):** **B** — robust, reproducible in-vitro/animal pharmacology (just not all pro-aging).
- **Ashwagandha ROOT EXTRACT, topical skin:** **C** — one real but small, industry-supported, visual-score-heavy human RCT [4].
- **Senolytic/longevity billing of WA:** **D** — AI-prediction [12] + fruit-fly (male-only) [15]; the senescence-deceleration data are for **withanone**, not WA [14].

### Citation audit — primary sources verified

| Ref | Claim as used | Verified? | Note |
|---|---|---|---|
| [3] Challa 2012, *PLOS ONE* | WA disrupts vimentin 0.5–1.5 µM; ↓collagen α1(I)/α2(I) mRNA half-life ~3–4×; ↓protein 2–4×; mouse 4 mg/kg ↓fibrosis ~50%; **reduces collagen** | ✅ Accurate | Direct fetch confirmed all figures. This is anti-fibrotic pharmacology — the dossier's central honesty point holds. |
| [4] Narra 2023, *Cureus* | 8% **KSM-66 root** extract (NOT WA); wrinkles −55.9% vs −24.1% (p=0.006); TEWL/hydration/elasticity sig; **melanin NS (p=0.969)**; Ixoreal-supported | ✅ Accurate | Direct fetch confirmed extract identity, all deltas/p-values, sponsor, and that melanin index was non-significant. Big % are largely physician visual scores. |
| [5] Marwah 2025, *Br. J. Biomed. Sci.* | Liposomes ~117–122 nm, ~70–73% entrapment; IL-6/MMP-9 drops in HDFa; **in-vitro only, no permeation; cytotoxic ~5 µM** | ✅ Accurate | Direct fetch confirmed numbers, the release-model (not Franz) caveat, and the narrow safety window. |
| [15] Koval 2021, *Aging* | WA Drosophila median +7.7/+9.6% **males only**, max +11.1%, **no female effect**, "multidirectional" trade-offs | ✅ Accurate | Direct fetch confirmed sex-specificity and trade-off framing. Invertebrate, modest. |
| [12] Aliper 2017, *Aging* | WA **AI-predicted** metformin+rapamycin mimetic (in-silico, not assay) | ✅ Accurate | Confirmed via abstract/secondary coverage; explicitly a deep-learning prediction. |
| [14] Vittal 2025, *Biogerontology* | senescence ↓p21 = **withanone** (not WA); ↓CRP>30% (extract, clinical); telomerase +45% in vitro; *C. elegans* +20% (extract) | ✅ Accurate | Direct fetch confirmed the compound attributions and evidence tiers. |
| [8][9] Imokawa melanogenesis | WA blocks c-KIT & ET-1 melanogenesis in human melanocytes/3D equivalents; in-vitro | ✅ Consistent | [8] via Springer landing + search; [9] (*Cytokine*) abstract only (publisher 403 on full text) — claims match abstract; in-vitro tier unaffected. |

Citations not independently full-text-fetched ([1][2][6][7][10][11][13][16][17][18]) are consistent with their descriptions and assigned tiers; [16] PK figures and [17] neurotoxicity detail are abstract/secondary only and flagged [partly unverified] in-text. None is used to support a human-topical anti-aging claim.

### Main caveats (the honest core)

1. **The isolate vs the extract are silently swapped in the market.** Every impressive *human* number is **whole root extract**; the molecule the class-name points to (**Withaferin A**) has **no human topical data**. The dossier keeps them separate; marketing usually does not.
2. **Withaferin A REDUCES collagen.** This is the most important, most counterintuitive fact: a well-replicated, in-vivo-confirmed **anti-fibrotic** action [3]. "Collagen-boosting ashwagandha" is contradicted by the primary literature.
3. **"Senolytic" is inferential for WA.** AI-prediction + fly data + a *different compound* (withanone) doing the senescence-decelerating. WA analogues even **induce** senescence in cancer cells [13]. No senescent-cell clearance shown in human skin.
4. **WA is a cytotoxic drug, not a gentle botanical.** Reactive electrophile, anticancer agent, narrow viability window (~5 µM cytotoxic [5]), kills neurons [17]. "Natural" is doing heavy lifting in the marketing.
5. **The human RCT is small, young-cohort, single-site, industry-supported, and mostly visual-scored** [4]; its instrumental **melanin index was non-significant**, undercutting the brightening claim despite a strong in-vitro mechanism.
6. **Pregnancy contraindication and category hepatotoxicity reports** (withanone-implicated) are real reputational/safety flags for an ashwagandha-forward product [18].
7. **Formulation is genuinely hard for the isolate** (insoluble, reactive, unstable, no penetration data even encapsulated) [5].

### Claims that must never appear as product copy

- "Withaferin A / ashwagandha **boosts/rebuilds collagen**" — **false** (WA lowers collagen [3]).
- "**Senolytic** / clears senescent skin cells" — unproven for WA; structure/function.
- "**Clinically proven** Withaferin A reduces wrinkles 55%" — that RCT is **root extract**, industry-supported, visual-scored [4]; mis-attribution.
- "**Metformin/rapamycin for your skin / longevity molecule**" — in-silico + fly only.
- "Natural and gentle anti-aging active" — WA is a cytotoxic anticancer/anti-fibrotic drug molecule.

**Defensible framing only (for the *extract*):** "soothing adaptogenic botanical," "helps calm the look of stressed skin," "supports an even-looking tone," "antioxidant-supporting" — strictly cosmetic, with no collagen/senolytic/longevity structure-function claims. **The isolate (Withaferin A) is a skip for this brand.**
