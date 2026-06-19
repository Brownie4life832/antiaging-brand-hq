# Ingredient: NR (Nicotinamide Riboside) (INCI: Niacinamide Riboside Chloride)

**Researched:** 2026-06-19 · **Status:** ⬜ considering / ⬜ shortlisted / ⬜ rejected / ⬜ in a product
**Slug:** nicotinamide-riboside · **Class:** Antioxidants (NAD+ precursor / redox metabolism)

> **Reading note.** NR is the third member of the NAD+ precursor family, sitting alongside **niacinamide** (the proven cosmetic workhorse) and **NMN** (the trendy story molecule). All three feed the same NAD+ salvage pathway, and the skincare marketing groups them under one "recharge your skin's NAD+ / cellular energy" narrative. This dossier covers NR specifically and keeps a hard line between what is proven, and *for which format (oral vs topical) and species*. NR is genuinely interesting because, unlike NMN, it has **real human oral RCTs** — but almost none of them measure skin, and there is **no published human topical RCT** for an NR cosmetic. See the companion file [`nad-niacinamide-longevity.md`](nad-niacinamide-longevity.md) for the full family context; this file does not repeat the niacinamide evidence in depth.

---

## 0. The honest punchline (read this first)

- **NR's human evidence is its differentiator — but it's the wrong kind for us.** NR has ~25 published human clinical trials (more than NMN), and they reliably show **oral NR raises blood NAD+** (and, in a few studies, muscle NAD+) in a dose-dependent way. That is real and well-replicated.
- **But almost none of that is dermatological, and none of it is topical.** The human NR trials measure blood NAD+, blood pressure, metabolic markers, Parkinson's, etc. The only human NR data with a *skin* endpoint is the **Werner syndrome** trial (n=9 rare-disease patients, oral, healing of pathological skin ulcers) and one **oral combination supplement** trial in aged Asian women (NR was bundled with grape-seed/rosehip/vitamins, so NR's solo contribution can't be isolated). **There is no published human topical NR RCT** showing visible wrinkle/tone/barrier benefit from an NR cosmetic.
- **A leading critical review is blunt:** "oral nicotinamide riboside supplementation has displayed few clinically relevant effects, and there is an unfortunate tendency in the literature to exaggerate the importance and robustness of reported findings" (Kim et al., *Science Advances* 2023 [1]). That is the NR community's own assessment of the *oral* data — the topical case is weaker still.
- **Formulation is a real problem.** NR chloride is hygroscopic, light/air/humidity-sensitive, and base-catalysed-hydrolyses in water — degrading into... **nicotinamide** (Campbell et al. 2019 [2]). So a water-based "NR serum" partly converts into the cheap, proven vitamin anyway.
- **IP is a real problem.** NR (as Niagen) is heavily patent-protected by ChromaDex (patents from Dartmouth/Cornell/Washington University), including a **topical-skin composition patent** [3]. Freedom-to-operate is a live commercial constraint.
- **Net:** NR is a credible NAD+ precursor with better human (oral) data than NMN, but for a *topical cosmetic* the proof is **borrowed** (from oral systemic trials and from cultured cells), the molecule is **unstable in water**, and it's **encumbered by IP**. Treat it like NMN: an optional, honest "story garnish" on a niacinamide base — not a hero, and never claimed to raise skin NAD+.

---

## 1. Identity

| Field | Detail |
|---|---|
| **Common name** | NR — Nicotinamide Riboside (β-nicotinamide riboside) |
| **Cosmetic form / INCI** | **Niacinamide Riboside Chloride** (the chloride salt is the stable, supplied form). Sometimes listed as "Nicotinamide Riboside Chloride." Verify exact INCI on the supplied raw material. |
| **CAS** | Nicotinamide riboside chloride **23111-00-4**; free NR base **1341-23-7** |
| **Trade name** | **NIAGEN®** (ChromaDex) is the dominant commercial NR chloride; consumer brand TRU NIAGEN. Generic cosmetic-grade NR chloride also offered by Asian suppliers (e.g. Suzhou Greenway, Huilin) — IP status varies, see §9. |
| **Family relationship** | NR → (via NR kinases, **NRK1/NRK2**) → **NMN** → (via NMNAT) → **NAD+**. NR is one step "upstream" of NMN, two steps from NAD+. It is a phosphate-free **nucleoside** (smaller/less charged than phosphorylated NMN). |
| **Reduced / derivative forms** | NRH (dihydro-NR) and lipophilic esters (e.g. NR trioleate chloride) are emerging to solve NR's water-instability — research-stage, not cosmetically established. |

**Why the smaller-molecule argument matters:** NR is a non-phosphorylated nucleoside, so it is *smaller and less charged* than NMN (a phosphorylated nucleotide) and far smaller/more stable than NAD+ itself (large, charged, very unstable). This is the headline pro-NR formulation argument — "the precursor that actually penetrates." It is plausible but, for skin, unproven in vivo (see §5).

---

## 2. Class & mechanism

**Class:** NAD+ metabolism / cellular-energy & redox active. Filed under Antioxidants per the taxonomy, though the mechanism is broader than free-radical scavenging.

**The mechanistic thesis (shared with the NAD+ family):**
- **NAD+** is a coenzyme central to mitochondrial ATP production, DNA repair, and as the obligate substrate for **sirtuins** (SIRT1–7) and **PARPs** (DNA-repair enzymes).
- **NAD+ declines with age** in tissues including skin; the decline is a proposed driver of mitochondrial dysfunction, impaired DNA repair, and senescence.
- **Intervention logic:** supply NR → cells import it via **equilibrative nucleoside transporters (ENT1/2/4)** (Kropotov et al. 2021 [4]) → NRK enzymes phosphorylate it → raise intracellular NAD+ → re-fuel sirtuins/PARPs/mitochondria.

**NR-specific mechanistic points:**
- **NR uses a dedicated salvage route (NRK1/NRK2).** This is sometimes pitched as an advantage — NR can raise NAD+ via a pathway that doesn't depend on NAMPT (the rate-limiting salvage enzyme that is itself depleted/inhibited under UV stress). The keratinocyte data below supports this idea.
- **In UV-stressed keratinocytes, NR rescues the NAMPT-NAD+-SIRT1 axis.** Katayoshi et al. 2021 [5] showed UVA/UVB damage depletes NAD+ via PARP while NAMPT tries to resynthesize it; when NAMPT was inhibited, supplementing **NR (50 µM)** or NMN (100 µM) **rescued** the UV-induced survival/proliferation defect and restored SIRT1-mediated p53 deacetylation. This is the cleanest cell-level rationale for NR in a *photo-protection* skin story.
- **Crucial caveat (same as the whole family):** raising NAD+ is the *hypothesized* mechanism. It is **not established that topical NR raises NAD+ in living human skin**, and niacinamide — the closely related parent — has no confirmed single molecular target for its clinical effects (Boo 2021, in companion file). The benefit could come from NR itself, its conversion to nicotinamide, or general redox buffering — not necessarily NAD+ elevation in skin.

---

## 3. Hallmarks of skin aging targeted

| Hallmark | NR — what's actually shown, and in which format |
|---|---|
| Collagen / ECM loss | Wound-closure / fibroblast migration in vitro (NIH 3T3, patent data [3]); preserved collagen in NMN photoaging mouse models (family read-across, not NR-specific) — **no human topical data** |
| Barrier decline | Supplier in-vitro claims of ↑barrier integrity at ≥2.5% [6] (vendor data, not peer-reviewed); strong barrier data exists for *niacinamide* (the degradant), not NR per se |
| Oxidative stress | Cytoprotection vs H₂O₂ in A431 epidermoid cells (2–38% at 0.2–5 mM, patent data [3]); ENT-mediated uptake supports intracellular antioxidant role [4] |
| Glycation / AGEs | Not a documented NR-specific effect |
| Cellular senescence | Plausible via NAD+/SIRT1; NR rescues UV-stress phenotypes in keratinocytes [5]; senolytic/anti-senescence data stronger for NMN/NAD+ in the family — **not shown in human skin** |
| Mitochondrial decline | **Core claimed mechanism**; oral NR boosts mitochondrial markers in human muscle (twin study [7]) — systemic, not skin |
| Inflammaging | Oral NR lowered some circulating inflammatory cytokines in human trials [8]; ↓TNF-α/IL-6 in NMN UV mouse models (family) — not demonstrated in human skin topically |
| Photoaging | NR rescues UV-damaged keratinocytes in vitro [5]; reduces UV-induced DNA dimers (CPDs) 32–50% in cells (patent [3]) — **no human topical RCT** |
| Pigmentation / tone | Improvement reported in the *oral combination* supplement trial [9] (confounded by other actives); pigment mechanism is well-evidenced for **niacinamide**, not NR |
| Microbiome | Not established for skin; oral NR altered gut microbiota in a twin study [7] (systemic, not relevant to topical) |
| Hydration / TEWL | Improved in the oral combination trial [9] (confounded); supplier claims ↑moisture at ≥1.5% [6] (vendor, not peer-reviewed); robust topical hydration data belongs to *niacinamide* |

**Read:** Across the hallmarks, NR's signal is real at the **cell** level and at the **systemic (oral)** level, but the **human topical skin** column is essentially empty of independent RCT evidence.

---

## 4. Evidence review by tier (the core of this dossier)

> Tiers, weakest-to-strongest *format* within the longevity story: **in-vitro → animal → human ORAL → human TOPICAL (RCT vs lower)**. For each claim I flag whether the benefit is **proven for topical human use** or **borrowed** from another format/species.

### TIER A — In-vitro (cell / biochemistry)

**A1. NR rescues UV-damaged human keratinocytes (the best skin-cell rationale).**
- Katayoshi T, Nakajo T, Tsuji-Naito K. "Restoring NAD+ by NAMPT is essential for the SIRT1/p53-mediated survival of UVA- and UVB-irradiated epidermal keratinocytes." *J Photochem Photobiol B* 2021;221:112238. [5]
- **Design:** human epidermal keratinocytes, UVA/UVB ± NAMPT inhibitor; rescue with NR (50 µM) or NMN (100 µM).
- **Findings:** UV depletes NAD+ via PARP; NAMPT resynthesis is required for SIRT1-mediated p53 deacetylation and cell survival; **NR supplementation rescued** the survival/proliferation defect when NAMPT was blocked.
- **Limitation:** cultured keratinocytes bathed in NR at defined µM — not skin under a cream. Mechanistic support, not efficacy.

**A2. NR enters human cells via ENT transporters.**
- Kropotov A, et al. "Equilibrative Nucleoside Transporters Mediate the Import of Nicotinamide Riboside and Nicotinic Acid Riboside into Human Cells." *Int J Mol Sci* 2021;22(3):1391. [4]
- **Findings:** ENT1/ENT2/ENT4 (not concentrative CNTs) mediate NR uptake in HEK293; ENT1/2 are expressed in most tissues, supporting plausible skin-cell uptake.
- **Limitation:** kidney-derived cells; establishes a transport route, not skin efficacy.

**A3. NR patent in-vitro examples (ChromaDex topical patent).**
- Deren-Lewis A, Rhonemus T (assignee ChromaDex). EP3063163A1 / US10688118 / US11033568 "Nicotinamide riboside compositions for topical use in treating skin conditions." [3]
- **Example data (in-vitro only; NO human clinical data in the filing):**
  - A431 epidermoid cells: **2–38% cytoprotection** vs H₂O₂ at 0.2–5 mM NR.
  - UV-exposed cells: CPD DNA-damage markers reduced **32–50%**.
  - NIH 3T3 mouse fibroblasts: **46% scratch-wound gap closure** at 1 mM NR vs 20% control.
- **Limitation:** patent examples are self-generated, in-vitro, and a commercial document — useful as a directional signal, NOT independent efficacy evidence.

**A4. NR/NMN/NAD+ niche skin-cell work.** A liposomal NAD+ formulation showed anti-senescence effects in keratinocytes/endothelial cells (2025, family read-across) [10] — relevant to delivery rationale, not NR-specific efficacy.

### TIER B — Animal

> There is comparatively little **NR-specific topical** animal skin work; the strong UV-photoaging animal data in this family is for **NMN** (oral/IP in mice — see companion file). For NR, the animal evidence is mostly systemic.
- Trammell et al. 2016 [11] established **oral NR raises hepatic NAD+ in mice** with superior pharmacokinetics to nicotinamide/nicotinic acid — foundational for the family, systemic not cutaneous.
- **Honest gap:** I found **no robust, peer-reviewed topical-NR animal skin photoaging RCT** comparable to the NMN mouse studies. Any "NR protects skin in animals" claim should be checked against a real primary source before use.

### TIER C — Human ORAL (NR's strongest tier — but mostly non-skin)

> This is where NR genuinely out-evidences NMN. The data is real and replicated — but it measures **blood/tissue NAD+ and systemic endpoints, not skin appearance**. Classic "borrowed format."

**C1. First human PK trial — oral NR is bioavailable.**
- Trammell SAJ, et al. "Nicotinamide riboside is uniquely and orally bioavailable in mice and humans." *Nat Commun* 2016;7:12948; PMC5062546. [11]
- Single oral doses (100/300/1000 mg) **dose-dependently raised the blood NAD+ metabolome**; first human NR PK trial.

**C2. Conze/ChromaDex dose-ranging RCT — the cleanest oral NAD+ result.**
- Conze D, Brenner C, Kruger CL. "Safety and Metabolism of Long-term Administration of NIAGEN (Nicotinamide Riboside Chloride)..." *Sci Rep* 2019;9:9772; PMID 31278280; PMC6611812. [8]
- **Design:** randomized, double-blind, placebo-controlled; **n=140** healthy overweight adults (40–60 y); 100/300/1000 mg/day; 8 weeks.
- **Findings:** dose-dependent blood NAD+ rise by day 14 (**+22% / +51% / +142%**), sustained to day 56. **No flushing, no serious AEs**, AEs not different from placebo; did not raise LDL or dysregulate 1-carbon metabolism.
- **Limitations:** predominantly white middle-aged adults; **no skin endpoints**. **COI: ChromaDex-funded; authors are ChromaDex employees / IP holder.**

**C3. Martens RCT — NAD+ rise + cardiovascular signal.**
- Martens CR, et al. "Chronic nicotinamide riboside supplementation is well-tolerated and elevates NAD+ in healthy middle-aged and older adults." *Nat Commun* 2018;9:1286. [12]
- **Design:** 2×6-week randomized, double-blind, placebo-controlled **crossover**; **n=24** healthy adults 55–79; 1000 mg/day.
- **Findings:** NAD+ ~+60%; in a 13-person hypertensive subgroup, systolic BP ~−10 mmHg (exploratory). No serious AEs.
- **Limitations:** small n; cardiovascular finding exploratory/subgroup; **no skin endpoints.**

**C4. Other oral NR human trials (systemic, no skin).** Twin study showing ↑muscle mitochondrial biogenesis, satellite-cell differentiation, gut-microbiota shift (*Sci Adv* 2022 [7]); Parkinson's (NADPARK, NR-SAFE high-dose safety [13]); mild cognitive impairment; CKD; COVID recovery; PAD. **Tolerability is consistently good up to ~2000 mg/day.** None are dermatological.

**C5. The sobering critical review.**
- Kim LJ, et al. "What is really known about the effects of nicotinamide riboside supplementation in humans." *Sci Adv* 2023;9(29):eadi4862. [1]
- Reviewed the ~25 published human NR trials: **"oral nicotinamide riboside supplementation has displayed few clinically relevant effects, and there is an unfortunate tendency in the literature to exaggerate the importance and robustness of reported findings."**
- **Implication for us:** even NR's *best* (oral) human evidence is judged thin on clinical payoff. We should be doubly cautious extrapolating to a topical cosmetic.

### TIER D — Human (the skin tier)

**D1. Human ORAL with a real skin endpoint — Werner syndrome (rare, pathological).**
- Shoji S, et al. "Nicotinamide Riboside Supplementation Benefits in Patients With Werner Syndrome..." *Aging Cell* 2025; PMID 40459998; PMC12341770. [14]
- **Design:** double-blind randomized **crossover** placebo-controlled; **n=9** randomized (Werner = premature-aging genetic disorder); 1000 mg/day; 26 weeks/arm.
- **Findings:** plasma NAD+ ↑ (p=0.045); **skin ulcer size significantly decreased** during NR (−0.88 cm² vs +0.71 cm² placebo, p=0.01); arterial stiffness (CAVI) improved; heel-pad-thinning trend toward preservation. No serious AEs.
- **Limitations:** tiny n; **rare-disease, pathological wound-healing context — NOT cosmetic facial aging**; oral not topical; no washout. Real, but not transferable to a "smoother skin" cosmetic claim.

**D2. Human ORAL combination supplement with cosmetic skin endpoints — confounded.**
- "Skin-Condition-Improving Effects of Nicotinamide Riboside Contained Supplement: A Randomized Clinical Trial in Naturally Aged Asian Women." *Curr Dev Nutr* 2024;8(7); article S2475-2991(24)00161-6. [9]
- **Design:** randomized clinical trial; **n=35** Asian women 30–45 with dermatologist-assessed facial concerns; **28 days**; oral. *(Published in a journal supplement; verify whether it is a full peer-reviewed article vs. a conference-abstract record before citing it as a definitive RCT.)*
- **Intervention:** NR **bundled with grape-seed extract, rosehip extract and vitamins** — NOT NR alone.
- **Findings:** significant improvement vs baseline in moisture, brightening/whitening, spot-fading, firmness by day 14 (p<0.001); smoothness/anti-wrinkle by day 28.
- **Limitations:** **NR's solo contribution cannot be isolated** (multi-ingredient); oral not topical; short; small; appears industry-associated. Useful for a "longevity-supplement" story, not as topical-NR proof.

**D3. Human TOPICAL NR — the gap.**
- **No published, peer-reviewed human topical RCT** was found demonstrating that an **NR cosmetic** visibly reduces wrinkles, evens tone, repairs barrier, or measurably raises skin NAD+ in living people. The supporting topical data is the **ChromaDex patent's in-vitro examples** [3] and the keratinocyte mechanism paper [5] — neither is a human topical efficacy trial.
- Registered exploratory work exists (e.g. a topical NR + pterostilbene + silibinin cream for radiation dermatitis; a psoriasis NR pilot) but these are disease-context and/or unpublished, not cosmetic anti-aging RCTs.
- **Verdict on the topical story:** the NAD+ mechanism is real biology and NR is a credible, ENT-importable precursor; but **topical human proof for NR is absent**. Any "topical NR recharges your skin's NAD+ / reverses aging" claim is currently **unsubstantiated for that format**.

---

## 5. Topical bioavailability / penetration

- **The pro-NR argument:** NR is a non-phosphorylated **nucleoside** — smaller and less charged than NMN (phosphorylated) and far smaller/more stable than NAD+. So of the three "trendy" precursors it is the most *theoretically* penetrable, and cells import it via **ENT transporters** [4]. This is the strongest formulation rationale for choosing NR over NMN/NAD+.
- **The reality check:** "smaller than NAD+" is a low bar. NR is still **highly hydrophilic (log P ≈ −6.25)** and very water-soluble [2] — properties that favour *solubility* but **work against passive stratum-corneum penetration** (the SC is lipophilic). There is **no published human-skin penetration study for NR**. The only direct family penetration signal is the NMN **Strat-M artificial-membrane** study (companion file) — a synthetic surrogate, not human skin.
- **The degradation confound:** in water at cosmetic pH, NR chloride hydrolyses to **nicotinamide** [2]. So part of any in-use "NR" effect is likely delivered by niacinamide — which *does* penetrate well and *is* proven. A "premium NR serum" may, over shelf life, become a more expensive niacinamide serum.
- **Bottom line:** plausible intracellular uptake *if* it reaches viable epidermis, but the in-vivo skin penetration of topically-applied NR in humans is **unproven**, and instability undercuts the delivered dose.

---

## 6. Formulation

**This is where NR gets hard — and where it differs sharply from niacinamide.**

- **Concentration:** no RCT-derived efficacious topical level in humans. Vendor/supplier guidance suggests ≥1.5% for moisture and ≥2.5% for barrier claims [6] (in-house data, not peer-reviewed). Cosmetic use levels are vendor-driven, not evidence-derived.
- **Stability — the central problem.** NR chloride is **highly hygroscopic** (raw powder turns sticky in seconds-to-minutes at ambient humidity), and **light/air/humidity-sensitive**. In solution it undergoes **base-catalysed hydrolysis to nicotinamide + ribose**; degradation roughly **doubles per +10 °C** and **doubles from pH 5.0 → 7.4** (Campbell et al. 2019 [2]). It cannot be used in high-water-activity systems without protection — hence research into lipophilic derivatives (NR trioleate chloride) and stabilized salts (NR hydrogen malate).
- **pH:** more stable in mildly acidic conditions; degrades faster as pH rises toward neutral/basic. This collides with skin-friendly near-neutral formulating and with co-formulating alongside niacinamide (best near pH 5–7). A genuine formulation tension.
- **Practical implications for a real product:** anhydrous or low-water systems, low-temperature processing and storage, opaque/airless packaging, antioxidants, and possibly encapsulation/derivatization. This is a meaningfully harder (and costlier) raw material to formulate well than niacinamide, HA, or peptides.
- **Pairings:** conceptually layered onto a niacinamide base and mitochondrial/antioxidant stories (CoQ10, vitamin E). Avoid high-pH, high-water, high-heat systems.
- **Sensory:** as a salt it's water-soluble and (well-purified) low-odour, but the formulation constraints above dominate the practical picture.

---

## 7. Safety

- **Oral human safety is well established.** Multiple RCTs show NR well-tolerated to **~1000–2000 mg/day**; consistently **no flushing** (a key differentiator from niacin/nicotinic acid), no serious AEs, AEs comparable to placebo (Conze 2019 [8]; Martens 2018 [12]; NR-SAFE high-dose Parkinson's [13]). FDA NDI-acknowledged and GRAS as a vitamin-B3 source [15].
- **Topical safety:** thin formal data, but as a vitamin-B3 nucleoside that largely converts to nicotinamide (which is CIR-assessed as non-irritant/non-sensitizer/non-photosensitizer at cosmetic levels), low intrinsic irritancy is expected. Conservative use levels and patch-test logic apply; demand supplier safety/irritation data and a CoA.
- **Sun sensitivity:** none expected (mechanism is the opposite — NAD+ supports UV-damage repair; cf. keratinocyte rescue [5]). Compatible in daytime products. Do **not**, however, imply sun-protection/photoprotection as a *cosmetic efficacy claim* (see §8).
- **Pregnancy:** vitamin-B3 family is generally low-concern topically; no specific contraindication flag, but defer to medical advice and avoid disease claims.
- **Sourcing/quality:** NR chloride is typically made by chemical/enzymatic synthesis or fermentation. Quality varies widely with the supplement boom; the hygroscopicity/instability means **degradation to nicotinamide and impurity profile must be verified** — demand CoA (purity, nicotinamide content, moisture, stability data).

---

## 8. Regulatory & claims (per CLAUDE.md guardrails)

**The cosmetic/drug line.** In the US/EU, cosmetics may improve *appearance* but may not claim to treat/prevent disease or alter the body's structure/function — that crosses into **drug** territory.

- ✅ **Safe cosmetic language:** "formulated with nicotinamide riboside, an **NAD-supporting** form of vitamin B3," "supports the skin's natural energy and renewal processes," "helps skin look healthier and more resilient," "antioxidant support." Keep these as *support/appearance* language tied to the vitamin-B3 family.
- ⚠️ **Risky / drug-like / unsubstantiated — flag for legal:**
  - "**recharges your skin's NAD+**" / "**boosts cellular energy/ATP in skin**" — NAD+ elevation is **not demonstrated for topical NR** in human skin; mechanism, not efficacy.
  - "**activates sirtuins / longevity genes in your skin**" — not shown in human skin in vivo.
  - "**reverses cellular aging / reverses wrinkles**" — structure/function overreach.
  - "**repairs DNA / protects against UV damage / heals wounds**" — the DNA-repair, UV-rescue and wound-closure data are **in-vitro / patent / rare-disease (Werner ulcers)**; "heals," "repairs," "protects from UV" are **drug-adjacent** and not supportable as cosmetic claims.
  - "**clinically proven**" — there is **no human topical NR efficacy RCT**; the human data is oral and largely non-skin. Using "clinical" for a topical NR product would be misleading.
  - any **quantified** "boosts NAD+/collagen by X%" without our own substantiation.
- **Key compliance nuance:** NR's genuine human wins are **oral and systemic** (and one rare-disease wound study). They must never be implied to apply to a topical facial cosmetic. Keep oral findings clearly labeled as oral, and as *education*, not product efficacy.

---

## 9. Sourcing & cost

| Material | Cost tier | Notes |
|---|---|---|
| **NR chloride (Niagen-grade)** | **High** | ChromaDex NIAGEN is the benchmark; pharma-grade NR chloride has traded ~$1,000+/kg. Premium price for **unproven topical efficacy** and a **hard-to-formulate** active. |
| **Generic NR chloride** | **Mid–high** | Asian suppliers offer cheaper material, but quality/purity/stability vary and **IP/freedom-to-operate is the gating issue** (see below). |
| **Niacinamide (the degradant / proven alternative)** | **Very low** | The proven workhorse and the thing NR partly turns into. Best value in the category. |

- **Intellectual property is a live constraint.** NR (Niagen) is protected by a **dense ChromaDex patent estate** (licensed from Dartmouth, Cornell, Washington University), including a **topical-skin composition patent** [3]. Patent validity has been litigated/contested at the USPTO with mixed outcomes [16]. **Practical rule: do not assume freedom-to-operate** for a topical NR product — legal review of the IP landscape is mandatory before formulating or marketing.
- **Regulatory status:** FDA **NDI-acknowledged (2015/2016)** and **GRAS** as a source of vitamin B3 (GRN 635) [15]; **EFSA** has assessed NR as safe for food use [17]. These are *food/supplement* clearances; cosmetic use rides on general cosmetic-ingredient safety, not these specifically.

---

## 10. Hype vs. evidence

- **"NR penetrates better than NMN/NAD+ so it works topically."** — *Partly true on chemistry, unproven on outcome.* NR is smaller/less charged than NMN/NAD+, but it's still extremely hydrophilic and there is **no human-skin penetration or efficacy study**. "More penetrable than the worst option" ≠ effective.
- **"Clinically proven NAD+ skincare."** — The human NR "clinical" data is **oral** (blood NAD+, BP, metabolism) — not a topical skin RCT. Borrowed across format.
- **"NR is the proven NAD+ booster."** — True that **oral NR raises blood NAD+** robustly; but a leading review found **"few clinically relevant effects"** and warns of **"exaggeration"** in the NR literature [1]. The NAD+ number rises; the patient-relevant payoff is modest even orally.
- **"NR repairs DNA / protects skin from UV."** — Based on **in-vitro keratinocyte** [5] and **patent** [3] data, not human topical trials; and these are **drug-adjacent** claims regardless.
- **"Premium NR does what cheap niacinamide can't."** — Unproven topically; and NR **degrades into niacinamide** in water [2]. The proven actor in the family is the cheap one.
- **What's NOT hype:** NR is a real, ENT-importable NAD+ precursor with the **best human (oral) NAD+-elevation data** in the family and an excellent **oral safety/no-flush** profile; the UV-stress keratinocyte rescue mechanism [5] is a legitimate, on-trend *story*; the Werner ulcer-healing result [14] is real (in a rare disease, orally).

---

## 11. Verdict for the brand

**⚠️ CONDITIONAL / supporting "story" garnish — not a hero. Slightly weaker for us than niacinamide, and roughly on par with NMN, with extra formulation and IP friction.**

- **Reasoning:** NR's standout asset (real human oral RCTs) is the *wrong kind of evidence* for a topical cosmetic — it's systemic, largely non-skin, and judged thin even by NR's own reviewers [1]. For the topical format there is **no human efficacy RCT**, **no human-skin penetration data**, a **genuine instability problem** (hydrolyses to niacinamide [2]), a **high cost**, and a **dense IP estate with a topical-skin patent** [3][16]. Niacinamide delivers the same vitamin-B3 / NAD-precursor narrative with overwhelming topical RCT support, trivial cost, easy formulation, and no IP friction — and NR partly *becomes* niacinamide anyway.
- **If used at all:** treat NR like NMN — a small, optional narrative inclusion layered on a **niacinamide** base, formulated in a low-water/stabilized system, and described only as an **NAD-supporting vitamin-B3 derivative**. **Never** claim it raises skin NAD+, repairs DNA, protects from UV, or "reverses aging." Clear the IP first.
- **Ranking within the NAD+ family for a topical product:** **niacinamide (proven hero-capable) > NR ≈ NMN (story garnish) > NAD+ (least practical).** NR edges NMN on *human oral* pedigree and ENT-uptake logic, but loses ground on *topical formulation* (instability) and *IP* (Niagen patents).

**Longevity-relevance note:** NR is one of the cleanest molecules to *talk about* in a longevity/hallmarks-of-aging narrative (NAD+ decline, sirtuins, the famous human trials) — which is exactly the trap. Its credibility for the brand depends on keeping the NAD+/sirtuin mechanism as **education**, letting **niacinamide's** RCTs carry the actual cosmetic efficacy, and never letting NR's *oral, systemic, rare-disease* wins masquerade as topical-cosmetic proof. Over-claiming NR is precisely where the brand's core asset — credibility — would be spent.

→ Log as **conditional / parking-lot** alongside NMN in [`../../ideas/considering.md`](../../ideas/considering.md) (pending real human topical data + IP clearance); anchor any NAD/longevity positioning on **niacinamide**.

---

## 12. Sources

1. Kim LJ, et al. "What is really known about the effects of nicotinamide riboside supplementation in humans." *Sci Adv* 2023;9(29):eadi4862. https://www.science.org/doi/10.1126/sciadv.adi4862 *(critical review of ~25 human NR trials; "few clinically relevant effects… exaggeration" quote)*
2. Campbell MTD, Jones DS, Andrews GP, Li S. "Understanding the physicochemical properties and degradation kinetics of nicotinamide riboside, a promising vitamin B3 nutritional supplement." *Food Nutr Res* 2019;63; PMID 31807125; PMC6878970. https://pmc.ncbi.nlm.nih.gov/articles/PMC6878970/ *(hygroscopic; hydrolyses to nicotinamide; degradation doubles per +10 °C and pH 5→7.4)*
3. Deren-Lewis A, Rhonemus T (assignee ChromaDex Inc.). "Nicotinamide riboside compositions for topical use in treating skin conditions." EP3063163A1; US10688118; US11033568. https://patents.google.com/patent/EP3063163A1/en *(0.001–50% claimed; in-vitro A431 cytoprotection 2–38%, CPD reduction 32–50%, NIH 3T3 wound closure 46%; NO human clinical data)*
4. Kropotov A, et al. "Equilibrative Nucleoside Transporters Mediate the Import of Nicotinamide Riboside and Nicotinic Acid Riboside into Human Cells." *Int J Mol Sci* 2021;22(3):1391. https://pmc.ncbi.nlm.nih.gov/articles/PMC7866510/
5. Katayoshi T, Nakajo T, Tsuji-Naito K. "Restoring NAD+ by NAMPT is essential for the SIRT1/p53-mediated survival of UVA- and UVB-irradiated epidermal keratinocytes." *J Photochem Photobiol B* 2021;221:112238. https://www.sciencedirect.com/science/article/abs/pii/S1011134421001172 *(NR 50 µM rescues UV-damaged keratinocytes when NAMPT inhibited)*
6. Niacinamide Riboside Chloride (Suzhou Greenway Biotech) — UL Prospector cosmetic listing; supplier in-vitro claims (≥1.5% moisture, ≥2.5% barrier). https://www.ulprospector.com/en/eu/PersonalCare/Detail/134104/9705480/Niacinamide-Riboside-Chloride *(vendor data — NOT peer-reviewed; treat as marketing)*
7. "Nicotinamide riboside improves muscle mitochondrial biogenesis, satellite cell differentiation, and gut microbiota in a twin study." *Sci Adv* 2022;8(13):eadd5163. https://www.science.org/doi/10.1126/sciadv.add5163 *(oral, systemic)*
8. Conze D, Brenner C, Kruger CL. "Safety and Metabolism of Long-term Administration of NIAGEN (Nicotinamide Riboside Chloride) in a Randomized, Double-Blind, Placebo-controlled Clinical Trial of Healthy Overweight Adults." *Sci Rep* 2019;9:9772; PMID 31278280; PMC6611812. https://pmc.ncbi.nlm.nih.gov/articles/PMC6611812/ *(n=140; NAD+ +22/+51/+142%; no flushing; ChromaDex COI)*
9. "Skin-Condition-Improving Effects of Nicotinamide Riboside Contained Supplement: A Randomized Clinical Trial in Naturally Aged Asian Women." *Curr Dev Nutr* 2024;8(7); article S2475-2991(24)00161-6. https://cdn.nutrition.org/article/S2475-2991(24)00161-6/fulltext *(n=35; ORAL; NR bundled with grape-seed/rosehip/vitamins — NR solo effect not isolable)*
10. "A Liposomal Formulation Enhances the Anti-Senescence Properties of Nicotinamide Adenine-Dinucleotide (NAD+) in Endothelial Cells and Keratinocytes." 2025; PMC12468054. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12468054/ *(family read-across; delivery rationale)*
11. Trammell SAJ, et al. "Nicotinamide riboside is uniquely and orally bioavailable in mice and humans." *Nat Commun* 2016;7:12948; PMC5062546. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5062546/
12. Martens CR, et al. "Chronic nicotinamide riboside supplementation is well-tolerated and elevates NAD+ in healthy middle-aged and older adults." *Nat Commun* 2018;9:1286. https://www.nature.com/articles/s41467-018-03421-7 *(n=24 crossover; NAD+ ~+60%; exploratory BP signal)*
13. "NR-SAFE: a randomized, double-blind safety trial of high dose nicotinamide riboside in Parkinson's disease." *Nat Commun* 2023. https://www.nature.com/articles/s41467-023-43514-6 *(high-dose oral safety)*
14. Shoji S, et al. "Nicotinamide Riboside Supplementation Benefits in Patients With Werner Syndrome: A Double-Blind Randomized Crossover Placebo-Controlled Trial." *Aging Cell* 2025; PMID 40459998; PMC12341770. https://pmc.ncbi.nlm.nih.gov/articles/PMC12341770/ *(n=9; ORAL; skin-ulcer reduction p=0.01; rare disease, not cosmetic)*
15. FDA GRAS Notice GRN 000635 (nicotinamide riboside chloride, vitamin-B3 source) + ChromaDex NDI acknowledgements (2015/2016). https://www.fda.gov/food/gras-notice-inventory/agency-response-letter-gras-notice-no-grn-000635
16. "NR legal rumbles continue as USPTO board splits recent decisions on patent challenges." NutraIngredients, 2022 (NR/Niagen patent-validity litigation). https://www.nutraingredients.com/Article/2022/08/23/nr-legal-rumbles-continue-as-uspto-board-splits-recent-decisions-on-patent-challenges/ *(secondary/industry — for IP-landscape context only)*
17. "EFSA rules nicotinamide riboside is safe for consumption." Nutraceutical Business Review (reporting EFSA novel-food opinion). https://nutraceuticalbusinessreview.com/efsa-rules-nicotinamide-riboside-is-safe-for-consumption-157238 *(secondary; confirm against primary EFSA opinion before citing in copy)*

---

### Verification notes
- All numbered primary sources (1–5, 7–15) resolve to real PubMed/PMC/journal/USPTO/FDA records confirmed in this session; sample sizes, doses and percentages were read from the source or its abstract/full text.
- **Author bylines verified where shown**: Campbell et al. [2], Kropotov et al. [4], Katayoshi/Nakajo/Tsuji-Naito [5], Conze/Brenner/Kruger [8], Trammell et al. [11], Martens et al. [12], Shoji et al. [14]. The Kim et al. byline for [1] and the exact first-author of [9] should be confirmed against the source before any author name appears in published copy — **[author bylines for [1] and [9] not fully captured this session]**.
- Sources [6], [16], [17] are **vendor/industry/secondary** — use only to locate primaries or for IP/regulatory context, never as efficacy citations in marketing.
- **No human topical NR efficacy RCT was found** despite targeted searching; if one is published later, this verdict should be revisited. The topical efficacy data cited here is in-vitro [3][5] or patent-internal [3].
- IP status (§9) is time-sensitive and was confirmed at a high level only; obtain a formal freedom-to-operate review before commercial use.

---

## Evidence verification (adversarial)

_Independent re-check, 2026-06-19. Method: every load-bearing citation was searched against PubMed/PMC/journal/USPTO records; each was tested on three questions — (a) is the evidence HUMAN and TOPICAL, or borrowed from in-vitro/animal/oral? (b) is the cited study real and does it say what the dossier claims? (c) is it industry-funded or tiny?_

### Overall grade: **D** (for the topical-cosmetic claim) — *unproven topically; the supporting human data is real but oral/systemic, not skin-topical.*

This grade is **for the question the dossier itself frames**: does NR work as a *topical* anti-aging cosmetic? On that question the evidence is **D — unproven topically**. (If the question were instead "does *oral* NR raise blood NAD+ safely?", that sub-claim would grade **B–A**: real, replicated human RCTs. The dossier never conflates the two, which is its central strength.) The headline cosmetic proposition rests on in-vitro keratinocyte data [5], a ChromaDex patent's self-generated in-vitro examples [3], and read-across from oral/systemic and rare-disease trials — none of which is a human topical efficacy RCT.

### Citation-by-citation check (the load-bearing claims)

| # | Claim in dossier | Real? | Says what's claimed? | Format / species | Funding / size flag |
|---|---|---|---|---|---|
| [1] Kim, *Sci Adv* 2023 | "few clinically relevant effects… exaggeration" | ✅ verified | ✅ quote and "~25 trials" scope accurate | Critical **review** of *oral* human data | Independent; **this is the strongest caveat in the file and it checks out** |
| [2] Campbell, *Food Nutr Res* 2019 | NR hygroscopic; hydrolyses to nicotinamide | ✅ verified | ✅ base-catalysed hydrolysis to nicotinamide + sugar confirmed | Physicochemical (not skin) | Independent; legitimate formulation concern |
| [4] Kropotov, *IJMS* 2021 | NR imported via ENT1/2/4 | ✅ verified | ✅ — and notes imported NR is metabolized to nicotinamide (reinforces degradation point) | **In-vitro, HEK293 (kidney) cells** — not skin | Independent |
| [5] Katayoshi, *J Photochem Photobiol B* 2021 | NR rescues UV-stressed keratinocytes | ✅ verified | ✅ NR/NMN rescue UVA/B phenotypes when NAMPT inhibited | **In-vitro, cultured human keratinocytes** — mechanism, not efficacy | Independent (DHC Corp. lab) |
| [8] Conze, *Sci Rep* 2019 | n=140; NAD+ +22/+51/+142%; no flush | ✅ verified | ✅ all figures accurate | Human **ORAL**; **no skin endpoint** | **ChromaDex-funded / employee authors — dossier discloses this** |
| [9] Combination supplement, *Curr Dev Nutr* 2024 | n=35 aged Asian women, skin improvements | ✅ exists (DOI resolves) | ⚠️ real, but **NR bundled** with grape-seed/rosehip/vitamins; appears in a **journal supplement** — verify full-article vs. abstract status | Human **ORAL combination**; NR solo effect not isolable | Industry-associated; **confound already flagged** |
| [11/12] Trammell 2016 / Martens 2018 | oral NR bioavailable; NAD+ ↑; BP signal | ✅ verified | ✅ Martens n=24 crossover, BP framed as exploratory/future-direction (accurate) | Human **ORAL**; **no skin endpoint** | Trammell ties to ChromaDex ecosystem; Martens academic |
| [14] Shoji, *Aging Cell* 2025 | Werner syndrome n=9; skin-ulcer ↓ | ✅ verified | ✅ crossover, 1000 mg, 26 wk/arm, ulcer-area reduction, arterial-stiffness improvement | Human **ORAL**; **rare-disease pathological wound**, not cosmetic facial aging | Tiny (n=9); rare disease; **dossier flags non-transferability** |
| [3] ChromaDex topical patent | in-vitro cytoprotection / CPD / wound-closure % | ✅ patent family exists (US10688118 / US11033568) | ✅ in-vitro examples; **no human clinical data in filing** | **In-vitro + commercial document** | Self-generated by IP holder; **dossier states this** |

**Bottom line of the check:** I found **no overstated or fabricated citation**. Every primary source resolves to a real record and supports the claim attached to it. The dossier's discipline about *format and species provenance* is unusually rigorous — it never lets oral, systemic, in-vitro, or rare-disease data masquerade as topical-cosmetic proof.

### Main caveats (carry these forward)

1. **The entire topical case is borrowed or in-vitro.** There is no human topical NR efficacy RCT and no human-skin penetration study. Confirmed: §4 D3 and §5 are accurate.
2. **NR's best human data is ChromaDex-adjacent.** The cleanest oral NAD+ result [8] is ChromaDex-funded with employee authors; even NR's own community review [1] calls the oral literature exaggerated. Independent, non-industry topical evidence is essentially absent.
3. **The molecule degrades into the cheap proven alternative.** Two independent lines ([2] degradation, [4] intracellular metabolism) confirm NR → nicotinamide. A water-based "NR serum" is partly a niacinamide serum over shelf life.
4. **The skin-endpoint human data is rare-disease and confounded.** The only human study with a real skin endpoint is Werner-syndrome ulcer healing (n=9, pathological) [14]; the only cosmetic-endpoint human study is an oral *combination* supplement [9].

### Claims to keep soft (already handled, do not let drift back up)

- Never: "recharges skin's NAD+," "boosts cellular energy in skin," "activates sirtuins/longevity genes," "repairs DNA," "protects from UV," "clinically proven" (topical), or any quantified "+X% NAD+/collagen." All are mechanism/in-vitro/oral, not topical-human. §8 already polices these correctly.
- Keep "NR penetrates better than NMN/NAD+" as a *chemistry* statement only — outcome is unproven (§5, §10 already do this).

### Edits made to the dossier this pass

- §0 punchline: "raises blood/tissue NAD+" → "raises blood NAD+ (and, in a few studies, muscle NAD+)"; "~25+" → "~25" to match the Kim review's count.
- §4 D2: added a flag that the combination-supplement trial [9] appears in a journal supplement and its full-article-vs-abstract status should be verified before it is cited as a definitive RCT.

No claim required *correction* for overstatement — only these two precision tightenings. The dossier was already defensible.
