# Ingredient: Next-gen NAD+ precursors — NaMN, NaR/NAR, NRH, NMNH (and reduced/lipophilic salts & prodrugs)

**Researched:** 2026-06-19 · **Status:** ⬜ considering / ⬜ shortlisted / ☑ rejected (topical, today) / ⬜ in a product
**Slug:** nextgen-nad-precursors · **Class:** NAD+ / sirtuin / AMPK / cellular-energy actives

> **Reading note.** This file covers the *frontier* NAD+ precursors that sit beyond the three molecules already documented in this repo — beyond **niacinamide** (the proven cosmetic workhorse), **NR** (real human *oral* RCTs, no topical RCT — see [`nicotinamide-riboside.md`](nicotinamide-riboside.md)), and **NMN** (story molecule). The "next-gen" set is: the **deamidated** precursors **NaMN** (nicotinic acid mononucleotide) and **NaR/NAR** (nicotinic acid riboside), and the **reduced (dihydro)** precursors **NRH** (dihydronicotinamide riboside) and **NMNH** (reduced NMN), plus their **salts and lipophilic acetate prodrugs** (NRH-triacetate, NARH-triacetate). The pitch for all of them is the same: *they raise NAD+ faster and harder than NR/NMN, sometimes via NAMPT/NRK-independent routes.* That pitch is **real in cells and mice**. It is also **almost entirely the wrong kind of evidence for a topical cosmetic**, and several of these molecules carry a documented **reductive-stress / pro-inflammatory / cytotoxicity** liability that the gentle, proven niacinamide does not. This dossier keeps the same hard line as the NR file: what is proven, **for which format (oral vs topical) and species**, and what is borrowed.

---

## 0. The honest punchline (read this first)

- **These are research chemicals, not cosmetic ingredients.** Of the next-gen set, **none has an established cosmetic INCI name**, none has a CIR safety assessment, and **none has a published human topical (or even human oral, except a just-completed NMNH trial) skincare result.** The only NAD-family molecules with real cosmetic INCI status and supplier ecosystems are niacinamide, NR (Niacinamide Riboside Chloride) and NMN (Nicotinamide Mononucleotide). The next-gen precursors are sold by *biochemical reagent* houses (Sigma, Cayman, Santa Cruz) by the milligram for lab use.
- **Their "superiority" is a cell/mouse NAD+-number story.** NRH and NMNH genuinely out-raise NR/NMN: NRH lifts cellular NAD+ **2.5–10-fold within 1 hour** and beats NR/NMN at equal or lower doses (Yang/Sauve, *JBC* 2019 [1]); NMNH raises NAD+ at a **10× lower concentration** than NMN and **~doubles** the blood-NAD+ response of NMN in mice (Zapata-Pérez, *FASEB J* 2021 [2]). Impressive — and **measured in cultured cells and injected mice, never in human skin.**
- **The reduced precursors have a dark side the proven ones don't.** NRH **induces a pro-inflammatory phenotype in macrophages** (NF-κB, cytokine/chemokine induction; Mateuszuk/Goncalves, *Front Immunol* 2022 [3]) and is **selectively cytotoxic** to some cells (HepG3 hepatoma: up to ~90% death at 1 mM, via mitochondrial superoxide, membrane depolarization and mtDNA damage; Sonavane, *PLoS One* 2020 [4]). NMNH causes **reductive stress**, suppressing glycolysis, the TCA cycle and cell growth (Liu, *J Proteome Res* 2021 [5]). "More NAD+, faster" is not automatically "better for aging skin" — over-driving the NAD(H) pool is itself a stressor.
- **The chemistry fights topical delivery.** **NaMN is a phosphorylated, charged mononucleotide** — even more cell-impermeant than NMN (the phosphate is *designed by biology* to trap the molecule inside cells; Preiss-Handler logic [6][12]). The free reduced ribosides (NRH/NARH) are unstable. The only credible topical route is the **lipophilic acetate prodrug** (NRH-triacetate etc.) — which is **patented for topical skin use** by Queen's University Belfast + ChromaDex (US10,280,190 [7]), so freedom-to-operate is a live constraint.
- **Net:** the next-gen NAD+ precursors are a **fascinating frontier for oral longevity supplements and injectable research**, and a **legitimate science story to *educate* with**. For a *topical anti-aging cosmetic today* they are **premature to the point of being unusable**: no INCI, no human topical data, no CIR safety, real reductive-stress/inflammation flags, hostile chemistry, and IP encumbrance. The repo's master index already grades them **"fringe ❌"** — this dossier confirms **skip for topical use**, while flagging them as a molecule class to *watch*.

---

## 1. Identity

| Field | Detail |
|---|---|
| **Family covered** | Next-gen / frontier NAD+ precursors beyond niacinamide, NR, NMN |
| **NaMN** | **Nicotinic Acid Mononucleotide** (β-nicotinic acid mononucleotide; "deamido-NMN"). CAS **321-02-8**. The **deamidated** mononucleotide — carboxylic acid instead of amide on the pyridine ring. A core intermediate of *both* the Preiss-Handler and de novo (tryptophan→quinolinic acid) pathways [6][12]. **Phosphorylated → charged → cell-impermeant.** No cosmetic INCI. |
| **NaR / NAR** | **Nicotinic Acid Riboside** (nicotinic acid riboside). The **deamidated, non-phosphorylated** riboside — the "nicotinic acid" analog of NR. Feeds NAD+ via NaMN→NaAD→NAD (a partly NRK-independent route) [8]. Imported by ENT transporters like NR [13]. No cosmetic INCI. |
| **NRH** | **Dihydronicotinamide Riboside** (1,4-dihydro-NR; reduced NR). The **reduced** form of NR. Converted to **NMNH** by an **ATP-dependent adenosine-kinase (ADK) activity that is NRK1/NRK2-independent** — a genuinely distinct salvage route [1]. No cosmetic INCI. CAS commonly listed as 19132-12-8 *(verify on CoA)*. |
| **NMNH** | **Reduced Nicotinamide Mononucleotide** (dihydro-NMN). The **reduced, phosphorylated** mononucleotide; the metabolic product of NRH and the most potent of the set in cells. Converted to NADH by NMNAT [2]. Marketed as a supplement under the trade name **UthPeak™** (EffePharm). No cosmetic INCI. |
| **NARH** | Reduced nicotinic acid riboside (dihydro-NAR). Appears mainly as a **triacetate prodrug** in the topical-permeation patent literature [7]. Research-stage. |
| **Lipophilic prodrugs / salts** | **NR-triacetate (NRTA), NRH-triacetate (NRH-TA), NAR-triacetate (NARTA), NARH-triacetate (NARH-TA)** — acetylated to add lipophilicity for skin penetration [7]; **NR hydrogen malate, NMN salts** — stabilized salt forms. These prodrugs/salts are the only versions with a *topical* rationale, and they are the patented ones. |

**Why the names matter for claims.** "Deamidated" (NaMN, NaR) = the **nicotinic-acid (niacin) branch** — relevant because nicotinic acid causes **flushing** and is regulated differently from the amide branch. "Reduced/dihydro" (NRH, NMNH) = carrying extra reducing equivalents — relevant because they raise **NADH** (the reduced cofactor), which is exactly what creates the **reductive-stress** liability. Neither nuance is captured by a casual "it's just vitamin B3" framing.

---

## 2. Class & mechanism

**Class:** NAD+ metabolism / cellular-energy, redox & sirtuin/AMPK actives. (Filed under the NAD+/sirtuin/cellular-energy taxonomy; mechanism is broader than antioxidant scavenging.)

**The shared NAD+ thesis (same as the whole family):**
- **NAD+** is the central redox coenzyme (mitochondrial ATP, the NAD+/NADH couple) and the **obligate substrate** for **sirtuins (SIRT1–7)** and **PARPs** (DNA repair) and **CD38**.
- **NAD+ declines with age** in many tissues including skin; the decline is a proposed driver of mitochondrial dysfunction, impaired DNA repair, and senescence — hence the "recharge cellular NAD+" longevity narrative.
- **Intervention logic:** feed a precursor → cells convert it → intracellular NAD+ rises → re-fuel sirtuins/PARPs/mitochondria.

**What makes the next-gen molecules *different* (the actual selling point):**

| Molecule | Route into NAD+ | Why it's pitched as "better" |
|---|---|---|
| **NaMN** | Direct Preiss-Handler/de-novo intermediate: NaMN → NaAD (NMNAT) → NAD (NAD synthetase) [6] | One step from NaAD; bypasses the amidation salvage bottleneck. But it's **charged/phosphorylated → can't get into cells from outside** without help [12]. |
| **NaR / NAR** | NaR → NaMN → NaAD → NAD; uses **Nrk-dependent and Nrk-independent** routes; ENT-imported [8][13] | A *deamidated* riboside route that can sidestep parts of the amide salvage pathway. |
| **NRH** | **NRH → NMNH** via an **ATP-dependent ADK kinase, NRK1/NRK2-independent** → NMNH → NADH/NAD via NMNAT [1] | **Bypasses NRK** (the rate-limiting NR step) and **NAMPT** — so it can raise NAD+ even when those enzymes are depleted/inhibited (e.g. under UV stress). Fastest, biggest cell NAD+ jump in the set. |
| **NMNH** | NMNH → NADH via **NMNAT**, **NRK- and NAMPT-independent** [2] | Same NRK/NAMPT-bypass logic, one step further along; most potent per-µM in cells. |

**The crucial mechanistic caveat — and it's bigger here than for niacinamide.** The proven cosmetic actor in this family (niacinamide) works at modest, well-buffered levels. The next-gen precursors are engineered to **overwhelm** the NAD+/NADH system. That is double-edged:
- **NRH/NMNH raise NADH disproportionately**, shifting the **NAD+/NADH ratio toward reduction** → **reductive stress**, which *suppresses* glycolysis, TCA flux and cell proliferation (NMNH; [5]) and can drive **mitochondrial superoxide** and **cytotoxicity** in vulnerable cells (NRH; [4]).
- **NRH activates pro-inflammatory macrophages** (NF-κB; cytokine/chemokine/enzyme induction) and **amplifies LPS responses** [3] — i.e. it can be *inflammatory*, the opposite of what an "inflammaging" skin story wants.
- So "raising NAD+ harder" is **not** a strictly-better version of niacinamide's gentle support. For aging *skin*, where the goal is calm barrier repair and reduced inflammaging, an aggressively reducing, potentially pro-inflammatory precursor is a **plausible net-negative**, not an obvious upgrade — and this has **never been tested topically in human skin**.

---

## 3. Hallmarks of skin aging targeted

| Hallmark | Next-gen precursors — what's actually shown, and in which format |
|---|---|
| Collagen / ECM loss | **No next-gen-specific human topical data.** Read-across only: NMN raises fibroblast NAD+ and collagen in vitro [10] (that's NMN, not the next-gen set); the topical-permeation patent claims fibroblast benefit for the *prodrugs* [7] (in-vitro/patent, not independent). |
| Barrier decline | Not demonstrated for any next-gen precursor. Barrier evidence belongs to **niacinamide**. |
| Oxidative stress | Mixed/contradictory: NRH is **cytoprotective** vs oxidants in some cells (A431, patent data; NRH-TA up to 88–94% [7]) but **pro-oxidant/cytotoxic** in others (HepG3, mitochondrial superoxide [4]). Net effect is **cell-type-dependent** — a red flag for an uncontrolled topical. |
| Glycation / AGEs | Not a documented effect of the next-gen set. |
| Cellular senescence | Plausible via NAD+/SIRT1 (family logic); NMN shows anti-senescence in skin fibroblasts in vitro [10] (NMN, not next-gen). **Not shown for NaMN/NaR/NRH/NMNH in human skin.** |
| Mitochondrial decline | **The core claimed mechanism** — and where the next-gen molecules are strongest *in cells/mice* (NRH/NMNH raise NAD+ across liver/kidney/brain/muscle/heart in mice [1][2]). All **systemic injection, not skin**. NRH can also **damage mitochondria** in susceptible cells [4]. |
| Inflammaging | **Counter-signal:** NRH is **pro-inflammatory** in macrophages [3]. This actively undercuts an inflammaging claim for NRH. |
| Photoaging | Mechanistic read-across only: NAD+ supports UV-damage repair, and NR/NMN rescue UV-stressed keratinocytes when NAMPT is blocked (Katayoshi 2021 — see NR file). The NAMPT-bypass logic *should* favour NRH/NMNH here, but **no UV/photoaging study of the next-gen precursors in human skin exists.** |
| Pigmentation / tone | Not established. Pigment evidence belongs to **niacinamide**. |
| Microbiome | Not established for skin. |
| Hydration / TEWL | Not established. Hydration evidence belongs to **niacinamide / NMN (vendor)**. |

**Read:** Across every hallmark, the next-gen-specific **human topical** column is **empty**, the in-vitro signal is **contradictory** (cytoprotective *and* cytotoxic depending on cell type), and at least one molecule (NRH) carries an explicit **pro-inflammatory** counter-signal. This is materially weaker — and riskier — than even the NR/NMN topical case.

---

## 4. Evidence review by tier (the core of this dossier)

> Tiers, weakest-to-strongest *format* within the longevity story: **in-vitro → animal → human ORAL → human TOPICAL (RCT vs lower).** For each, I flag whether the benefit is **proven for topical human use** or **borrowed** from another format/species. Spoiler: for the next-gen set, essentially everything is in-vitro or animal, with a single just-completed human *oral* NMNH trial and **zero** human topical data.

### TIER A — In-vitro (cell / biochemistry) — *this is where almost all the evidence lives*

**A1. NRH is the most potent NAD+ enhancer in the set (the foundational paper).**
- Yang Y, Mohammed FS, Zhang N, Sauve AA. "Dihydronicotinamide riboside is a potent NAD+ concentration enhancer in vitro and in vivo." *J Biol Chem* 2019;294(23):9295–9307; PMID 30948509. [1]
- **Design:** panel of cell lines (F98, U87, LN229, HEK293, INS1, MIN6, C2C12, Neuro2a, primary rat neurons); 100–2000 µM NRH (typ. 1 mM).
- **Findings:** NRH raised NAD+ **2.5–10-fold within 1 h**, exceeding NR and NMN at equal-or-lower concentrations; conversion via an **ATP-dependent, NRK1/NRK2-independent** kinase to **NMNH**; cells became resistant to genotoxin (H₂O₂, MMS) death.
- **Limitation:** cultured cells bathed in mM NRH; mechanism/PK, **not skin efficacy.** Even here, "more NAD+" is the readout, not "younger skin."

**A2. NMNH is the most potent per-µM — and reveals the reductive-stress liability.**
- Zapata-Pérez R, et al. "Reduced nicotinamide mononucleotide is a new and potent NAD+ precursor in mammalian cells and mice." *FASEB J* 2021;35(4):e21456; DOI 10.1096/fj.202001826R. [2] *(PMID-corrected: the "PMID 33793246" originally listed here actually belongs to the Liu paper [5]; cite [2] by its DOI.)*
  - NMNH raised NAD+ at a **10× lower concentration (5 µM)** than NMN; metabolized via **NMNAT, NRK/NAMPT-independent**; also **raised NADH**.
- Liu Y, et al. "Reduced Nicotinamide Mononucleotide (NMNH) Potently Enhances NAD+ and Suppresses Glycolysis, the TCA Cycle, and Cell Growth." *J Proteome Res* 2021;20(5):2596–2606; PMID 33793246 (confirmed). [5]
  - NMNH (100 µM) raised NAD+ **~5-fold** in HepG2 (vs slight rise with NMN), **but caused reductive stress**: suppressed glycolysis, the TCA cycle, and **cell growth/proliferation**.
- **Limitation:** cultured cells; the growth-suppression / reductive-stress finding is a **safety/biology caution**, not a cosmetic benefit.

**A3. NRH is selectively CYTOTOXIC (the most important safety paper).**
- Sonavane M, et al. "Dihydronicotinamide riboside promotes cell-specific cytotoxicity by tipping the balance between metabolic regulation and oxidative stress." *PLoS One* 2020;15(11):e0242174; PMID 33166357. [4]
- **Findings:** NRH **100–1000 µM** killed **HepG3 hepatoma cells dose-dependently (~15–90% cytotoxicity)** while sparing HEK293T; mechanism = **mitochondrial superoxide ↑ (1.66–1.73-fold), membrane depolarization (−37% at 1 h), mtDNA damage (−57% long-fragment amplification), PUMA/BAX apoptosis**; NQO2 expression accelerated NRH oxidation and ROS.
- **Author conclusion (quote):** *"caution in the use of NRH must be exercised as it may have adverse effects."*
- **Limitation:** cancer-cell context, but the principle — that aggressively forcing NAD(H) can be **pro-oxidant and lethal in a cell-type-dependent way** — is exactly the unknown you do *not* want in an unstudied facial cosmetic.

**A4. NRH drives a PRO-INFLAMMATORY macrophage phenotype.**
- Chini CCS, Peclat TR, Gomez LS, et al. (Chini lab, Mayo Clinic). "Dihydronicotinamide Riboside Is a Potent NAD+ Precursor Promoting a Pro-Inflammatory Phenotype in Macrophages." *Front Immunol* 2022;13:840246; PMC8913500. [3] *(byline corrected on verification: first author is Chini CCS, not "Mateuszuk Ł / Goncalves lab" as originally drafted)*
- **Findings:** NRH strongly raised macrophage NAD+ and **activated a pro-inflammatory program** (NF-κB; induction of cytokines, chemokines, enzymes) in resting macrophages and **potentiated LPS** responses.
- **Implication:** directly **contradicts** an "anti-inflammaging" skin claim for NRH; relevant because skin is immunologically active (Langerhans cells, macrophages).

**A5. NaR/NaMN biochemistry — precursor plumbing, not skin data.**
- Tempel W, et al. "Nicotinamide riboside and nicotinic acid riboside salvage in fungi and mammals…" *J Biol Chem* 2007/2008 (Urh1 / PNP function) [8] — establishes NaR routes to NaMN→NaAD→NAD and PNP/Urh1 handling.
- Kropotov A, et al. *Int J Mol Sci* 2021;22(3):1391; PMC7866510 [13] — **ENT1/2/4 import both NR and NaR** into human cells (HEK293). Transport route, not skin efficacy.
- "CD38 mediates NMN base-exchange to yield NaMN" *(bioRxiv 2024; PMC11903787)* [14] — shows a salvage↔Preiss-Handler crosstalk via NaMN. Mechanism, not skin.

### TIER B — Animal — *systemic injection only; no topical skin study*

**B1. NRH raises NAD+ across mouse tissues (IP injection).**
- Yang/Sauve 2019 [1]: **1000 mg/kg IP** NRH raised NAD+ in liver, kidney, brain, blood, adipose. Systemic, not cutaneous.

**B2. NMNH raises NAD+ in mouse tissues and outlasts NMN.**
- Zapata-Pérez 2021 [2]: injected NMNH gave a **rapid, sustained** blood-NAD+ surge (≈**double** NMN), elevated NAD+ in liver (>5-fold), kidney (>2-fold), muscle, brain, BAT, heart (not white fat); sustained ≥24 h vs NMN's ~20 h taper.

**B3. NRH improves obesity/glucose tolerance in mice (recent).**
- "Therapeutic potential of dihydronicotinamide riboside (NRH) on obesity and glucose intolerance in mice." *Nat Commun* 2026 (article s41467-026-70965-4). [9] *(metabolic mouse model; oral/IP. Full text paywalled this session — sample sizes, exact doses and any adverse findings should be read from the primary before use. Marked partially [unverified] for specifics.)*
- **Honest gap:** I found **no peer-reviewed topical-skin animal study** for any next-gen precursor (NaMN, NaR, NRH, NMNH). All animal evidence is metabolic/systemic.

### TIER C — Human ORAL — *one trial, just completed, results pending*

**C1. NMNH (UthPeak) — first human trial of a reduced precursor.**
- NCT06889740. Official title: "A Prospective, Multi-center, Double-blind, Placebo-controlled, Randomized, Multiple-arm, Parallel Study to Evaluate the Safety, Tolerability, and **Pharmacokinetics** of UthPeak NMNH." Sponsor **EffePharm Ltd** (industry). [11] *(note: the registered title says pharmacokinetics, not "efficacy"; the longevity/biological-age readouts are secondary/exploratory, not the registered primary efficacy design)*
- **Design:** multicenter, double-blind, placebo-controlled, randomized, parallel; **n=80** healthy adults 40–65 (BMI 18.5–35); **oral capsules**, 125/250/500 mg/day vs placebo, **90 days.**
- **Endpoints:** blood NAD+, "biological age," 6-minute walk, BMI, SF-36 QoL; AE frequency.
- **Status:** **Completed (Jan 2025); sponsor has since publicized topline results (EffePharm marketing: "3× NAD+ increment, ~5 years younger biological age, +35% energy, +31% emotional wellness"), but NO peer-reviewed publication located.** These are **industry-self-reported, non-peer-reviewed** figures — treat as marketing, not evidence. Industry-sponsored. **Oral, systemic, no skin endpoint** — even peer-reviewed, it would be borrowed format for a topical cosmetic.
- **For NaMN, NaR, NRH:** **no human trials of any kind were found** (oral or topical).

### TIER D — Human TOPICAL (the skin tier) — *empty*

**D1. There is NO published human topical study — RCT or otherwise — for any next-gen NAD+ precursor (NaMN, NaR, NRH, NMNH or their prodrugs).**
- The only "topical NAD-precursor" human-skin evidence in the broader family is for **niacinamide** (extensive RCTs — see [`nad-niacinamide-longevity.md`](nad-niacinamide-longevity.md)) and is **absent** for NR/NMN as well (see NR file). For the next-gen set the gap is **total**.
- The closest topical document is the **ChromaDex/Queen's-Belfast skin-permeation patent** [7], whose data are **in-vitro A431 cytoprotection** for the *prodrugs* (NRH-TA up to 88–94%; NARH-TA ~70–75%) — a **commercial filing, not a human trial.**
- **Verdict on the topical story:** any claim that a NaMN/NaR/NRH/NMNH cosmetic "recharges skin NAD+," "reverses aging," or "outperforms niacinamide" is **wholly unsubstantiated for the topical format** and, for NRH, runs *against* the available inflammation/cytotoxicity data.

---

## 5. Topical bioavailability / penetration

- **NaMN — worst case.** It is a **phosphorylated, charged mononucleotide.** Biology phosphorylates nicotinic acid to NaMN *precisely to trap it inside cells* (the charge stops it leaking out — Preiss-Handler logic [12]). The same charge stops it getting *in* from a topical film. Passive stratum-corneum penetration of unmodified NaMN is **implausible**; no skin-penetration data exists.
- **NaR / NRH / NMNH — better than NaMN, still poor.** The non-phosphorylated ribosides (NaR, NRH) are smaller and ENT-importable *at the cell membrane* [13], but they are **highly hydrophilic and unstable** (the reduced forms oxidize; ribosides hydrolyze toward the parent base). NMNH is again phosphorylated/charged. No human-skin penetration study exists for any of them.
- **The only credible topical route is a lipophilic prodrug.** The patent strategy [7] is to **acetylate** the ribosides into **triacetate esters** (NRH-TA, NARH-TA, etc.), raising lipophilicity so they cross the SC, then rely on skin esterases to cleave back to the active. This is a real medicinal-chemistry approach — but it is **patented**, **unstudied in human skin**, and converts the "natural vitamin" story into a "synthetic prodrug" story.
- **Degradation confound (as with NR).** In water at cosmetic pH the ribosides degrade toward nicotinamide/nicotinic acid; the reduced forms are additionally **air/oxidation-sensitive.** A water-based "NRH serum" would partly become a niacinamide/niacin serum — and could generate **nicotinic acid**, which **flushes**.
- **Bottom line:** topical bioavailability of the unmodified next-gen precursors in human skin is **unproven and, for the charged mononucleotides, chemically unlikely.** The prodrug workaround is promising on paper, patented, and untested in people.

---

## 6. Formulation

**This is the hardest raw-material situation in the entire NAD family.**

- **Concentration:** no RCT-derived efficacious topical level in humans for *any* next-gen precursor. There is no vendor cosmetic-use guidance because there is no cosmetic-grade supply chain — only reagent-grade material.
- **Stability — severe.**
  - *Reduced forms (NRH, NMNH):* **oxidation-sensitive** (the whole point is the extra reducing equivalents); they will degrade in the presence of air/oxidizers and over shelf life.
  - *Ribosides (NaR, NRH):* hydrolyze in water like NR (toward the base + sugar); base-catalysed, faster at higher pH/temperature.
  - *Mononucleotides (NaMN, NMNH):* phosphate adds polarity/charge (delivery problem) and they are also moisture/heat-labile like NMN (water systems degrade NMN within ~3 months per supplier data — same vulnerability expected or worse here).
- **pH:** ribosides favour mildly acidic for stability; reduced forms are sensitive across the range. NaR can liberate **nicotinic acid** on degradation → potential flush vector. These tensions collide with skin-friendly near-neutral formulating.
- **Practical implication:** to use any of these you would need **anhydrous/low-water systems, inert (oxygen-excluded) processing, cold-chain storage, antioxidants, opaque/airless packaging, and almost certainly prodrug derivatization** — i.e. a pharma-grade formulation program for an active with **no proven topical benefit.** That is a poor use of formulation budget vs niacinamide.
- **Pairings:** conceptually layered onto a niacinamide base + mitochondrial/antioxidant stories (CoQ10, vitamin E). But pairing a **pro-oxidant-capable** (NRH [4]) active with antioxidants is itself an unresolved formulation question.
- **Sensory:** as small water-soluble molecules (or their salts) sensory is not the gating issue; **stability, delivery, safety and supply** are.

---

## 7. Safety

- **No CIR assessment, no cosmetic safety dossier, no established topical safety data** for NaMN, NaR, NRH or NMNH. This alone is disqualifying for a credibility-first brand.
- **Documented biological liabilities (in-vitro / mechanistic):**
  - **NRH cytotoxicity** — cell-type-dependent killing via mitochondrial superoxide, depolarization, mtDNA damage, apoptosis; authors explicitly warn caution [4].
  - **NRH pro-inflammatory** — NF-κB / cytokine induction in macrophages; LPS potentiation [3]. Relevant to immunologically active skin.
  - **NMNH reductive stress** — suppression of glycolysis/TCA and **cell-growth inhibition** [5]; the reduced precursors over-reduce the NAD(H) pool.
- **Nicotinic-acid (flush) branch:** NaMN/NaR are **deamidated** (niacin-side) molecules; degradation toward **nicotinic acid** carries a **flushing/vasodilation** potential that the amide-side molecules (niacinamide, NR, NMN) do not. Worth explicit caution.
- **Human safety:** only NMNH has a (completed, unpublished) human **oral** safety trial [11]; even if it reads out clean **orally**, that does not establish **topical** safety, and says nothing about NaMN/NaR/NRH.
- **Sun sensitivity / pregnancy:** unknown — no data either way; absence of data is itself a reason to wait.
- **Sourcing/quality:** reagent-grade only; purity, oxidation state, residual solvents, nicotinic-acid content and stability must all be characterized — and there is no cosmetic supply chain to provide a proper CoA/safety package.

---

## 8. Regulatory & claims (per CLAUDE.md guardrails)

**The cosmetic/drug line.** In the US/EU, a cosmetic may improve *appearance* but may not claim to treat/prevent disease or alter the body's structure/function — that crosses into **drug** territory.

- **Ingredient-status reality first.** With **no established INCI** and **no CIR review**, putting NaMN/NaR/NRH/NMNH in a marketed cosmetic raises an **ingredient-listing and substantiation problem before any efficacy claim.** This is a regulatory gating issue, not just a marketing-language one. (NMN itself has been the subject of US FDA scrutiny over its status as a *supplement* ingredient — a cautionary signal for the whole frontier set.)
- ⚠️ **Risky / drug-like / unsubstantiated — flag for legal (essentially every interesting claim here):**
  - "**recharges your skin's NAD+ / boosts cellular energy/ATP**" — not demonstrated topically for any next-gen precursor; mechanism, not efficacy.
  - "**activates sirtuins / longevity genes / reverses cellular aging**" — structure/function overreach; unproven in human skin.
  - "**next-generation, more potent than niacinamide/NR/NMN**" — the potency data are **cell/mouse NAD+ numbers**, not skin outcomes; using "more potent" implies a skin benefit that is unproven (and, for NRH, contradicted by inflammation/cytotoxicity data).
  - "**clinically proven**" — there is **no human topical efficacy trial**; the only human trial is oral NMNH and unpublished.
  - "**repairs DNA / protects from UV / heals**" — drug-adjacent; based on in-vitro/patent data.
  - any **quantified** "+X% NAD+/collagen."
- ✅ **The only defensible use of these names is *education*, clearly labeled as frontier science**, e.g. "researchers are studying next-generation NAD+ precursors such as NRH and NMNH" — **as background, not as a product claim**, and never implying our product contains a proven version. Anchor any actual NAD/longevity *product* claim on **niacinamide**.

---

## 9. Sourcing & cost

| Material | Cost tier | Notes |
|---|---|---|
| **NaMN, NaR, NRH, NMNH (reagent grade)** | **Very high / not cosmetic** | Sold by the mg by reagent houses (Sigma, Cayman, Santa Cruz, BOC, GlpBio) for lab use. **No cosmetic-grade, GMP, kg-scale, CoA-backed supply chain.** Effectively unusable for a marketed product today. |
| **NMNH "UthPeak" (EffePharm)** | **High** | A **supplement-grade** branded NMNH exists, but it is positioned for **oral** capsules, not topical cosmetic use. |
| **Lipophilic prodrugs (NRH-TA etc.)** | **High + IP-encumbered** | The only topical-rational form, and **patented** (see below). |
| **Niacinamide (the proven alternative)** | **Very low** | The proven workhorse the whole family ultimately leans on. Best value, easiest, safest. |

- **Intellectual property is a hard gate.**
  - The **Sauve/Cornell** estate covers **"Use of nicotinic acid riboside or nicotinamide riboside derivatives, and reduced derivatives thereof, as NAD+ increasing precursors"** (US 10,183,036) — i.e. the **NaR/NRH/NMNH concept itself** [15].
  - The **Queen's University Belfast + ChromaDex** patent **US 10,280,190** explicitly covers **"nicotinic acid riboside or nicotinamide riboside compositions, reduced derivatives thereof, and the use thereof to enhance skin permeation in treating skin conditions"** — i.e. the **topical-skin use of exactly these prodrugs** (NRTA/NRH-TA/NARTA/NARH-TA) [7]. There is a real **freedom-to-operate problem** for a topical product.
  - Production-method patents (e.g. EP4214217B1, making NRH from NR chloride) further fence the space [16].
- **Bottom line:** no cosmetic supply chain, very high reagent cost, and a **dense IP estate that specifically claims topical skin use.** Commercially, this is closed for now.

---

## 10. Hype vs. evidence

- **"Next-gen NAD+ boosters — more potent than NR/NMN/niacinamide."** — *True as a cell/mouse NAD+ number; unproven and irrelevant as a skin outcome.* NRH/NMNH out-raise NAD+ in cells and injected mice [1][2]. None of that is human skin, and "more NAD+ faster" is **not shown to be better for skin** — and may be worse (reductive stress [5], inflammation [3], cytotoxicity [4]).
- **"Clinically proven next-gen NAD skincare."** — There is **no human topical trial** of any next-gen precursor. The single human trial is **oral NMNH**, unpublished [11].
- **"The deamidated/reduced precursors penetrate skin better."** — The unmodified molecules penetrate *worse* (NaMN/NMNH are charged) or comparably-poorly (ribosides); the only better-penetrating versions are **patented synthetic prodrugs** [7], untested in people.
- **"NRH is anti-inflammatory / anti-aging for skin."** — NRH is documented as **pro-inflammatory** in macrophages [3] and **cytotoxic** in some cells [4]. This is the opposite of the marketed framing.
- **"It's just a smarter vitamin B3."** — The reduced forms (extra reducing equivalents) and deamidated forms (niacin/flush branch) behave **differently and more aggressively** than gentle niacinamide; calling them "just B3" is misleading.
- **What's NOT hype:** the **biochemistry is real and genuinely interesting** — NRH/NMNH are legitimately more potent NAD+ enhancers via **NRK/NAMPT-independent** routes [1][2], NaMN is a real de-novo/Preiss-Handler node [6], and the **prodrug skin-permeation idea** is a credible (if patented) medicinal-chemistry strategy [7]. As a **science-education story** and a **molecule class to watch**, this is solid. As a **topical product today**, it is not.

---

## 11. Verdict for the brand

**❌ SKIP for topical use (today). ⚠️ WATCH as a frontier science story / future oral-longevity angle.**

- **Reasoning:** The next-gen NAD+ precursors fail the brand's credibility test on **every** practical axis for a topical cosmetic at once: (1) **no cosmetic INCI** and **no CIR safety assessment** — an ingredient-listing/substantiation problem before any claim; (2) **zero human topical evidence** (the only human trial is unpublished *oral* NMNH [11], and none exists for NaMN/NaR/NRH); (3) **active safety counter-signals** the proven actives lack — NRH cytotoxicity [4] and pro-inflammation [3], NMNH reductive stress/growth suppression [5]; (4) **hostile chemistry** — NaMN/NMNH are charged and cell-impermeant [12], reduced forms oxidize, ribosides hydrolyze; (5) **no cosmetic supply chain** and **very high reagent cost**; (6) a **dense IP estate that specifically claims topical skin use** [7][15]. Meanwhile **niacinamide** delivers the same vitamin-B3/NAD-precursor narrative with overwhelming topical RCT support, trivial cost, easy formulation, established INCI/CIR safety, and no IP friction.
- **Ranking within the NAD+ family for a *topical* product:** **niacinamide (proven, hero-capable) > NR ≈ NMN (story garnish, unproven topically) >> next-gen precursors (skip; research chemicals).** The next-gen molecules are *more potent in cells* and *less suitable for skin* simultaneously.
- **If the brand ever wants them:** the only honest path is (a) wait for **human topical safety + efficacy data** that does not yet exist, (b) license the **prodrug + skin-permeation IP** [7], and (c) carry a **cosmetic-grade, CoA-backed, stabilized** raw material that does not exist today. None of that is near-term.

**Longevity-relevance note.** This is the *purest* expression of the trap the whole NAD/longevity category sets for this brand: the science is dazzling (NRK/NAMPT-bypass, faster/bigger NAD+ surges, real *Nature/JBC/FASEB* papers), and it is *exactly* the kind of thing a longevity brand is tempted to slap on a label to sound cutting-edge. But the dazzle is **oral/injected/in-vitro**, the **topical case is empty**, and at least one star molecule (NRH) is **inflammatory and cytotoxic** in the very tissue compartments skin contains. The credibility-correct move is to **talk about** next-gen NAD+ precursors as frontier science we follow, let **niacinamide** carry the actual cosmetic efficacy, and **never** ship NaMN/NaR/NRH/NMNH in a product on borrowed, mismatched evidence. Revisit only when a real human topical dataset and a real cosmetic raw material exist.

→ Log as **skip / parking-lot (watch)** in [`../../ideas/not-considering.md`](../../ideas/not-considering.md) (reason: research chemicals; no INCI/CIR; no human topical data; reductive-stress/inflammation/cytotoxicity flags; IP-encumbered). Anchor all NAD/longevity positioning on **niacinamide**; keep NR/NMN as the "story garnish" tier above this one.

---

## 12. Sources

1. Yang Y, Mohammed FS, Zhang N, Sauve AA. "Dihydronicotinamide riboside is a potent NAD+ concentration enhancer in vitro and in vivo." *J Biol Chem* 2019;294(23):9295–9307; PMID 30948509. https://pubmed.ncbi.nlm.nih.gov/30948509/ *(NRH 2.5–10× NAD+ in 1 h; beats NR/NMN; NRK1/2-independent ATP kinase → NMNH; 1000 mg/kg IP in mice)*
2. Zapata-Pérez R, et al. "Reduced nicotinamide mononucleotide is a new and potent NAD+ precursor in mammalian cells and mice." *FASEB J* 2021;35(4):e21456; DOI 10.1096/fj.202001826R. https://faseb.onlinelibrary.wiley.com/doi/10.1096/fj.202001826R *(do NOT use "PMID 33793246" for this paper — that PMID belongs to Liu [5]; cite [2] by DOI)* *(NMNH active at 10× lower conc than NMN; ~double blood-NAD+ vs NMN in mice; NMNAT-mediated, NRK/NAMPT-independent; raises NADH)*
3. Chini CCS, Peclat TR, Gomez LS, Zeidler JD, Warner GM, Kashyap S, et al. (Chini EN, senior author; Mayo Clinic). "Dihydronicotinamide Riboside Is a Potent NAD+ Precursor Promoting a Pro-Inflammatory Phenotype in Macrophages." *Front Immunol* 2022;13:840246; PMC8913500. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8913500/ *(NRH activates NF-κB / cytokines in macrophages; potentiates LPS — pro-inflammatory)*
4. Sonavane M, et al. "Dihydronicotinamide riboside promotes cell-specific cytotoxicity by tipping the balance between metabolic regulation and oxidative stress." *PLoS One* 2020;15(11):e0242174; PMID 33166357. https://pmc.ncbi.nlm.nih.gov/articles/PMC7652347/ *(NRH ~15–90% cytotoxic to HepG3 100–1000 µM via mito superoxide/depolarization/mtDNA damage/apoptosis; "caution… may have adverse effects")*
5. Liu Y, et al. "Reduced Nicotinamide Mononucleotide (NMNH) Potently Enhances NAD+ and Suppresses Glycolysis, the TCA Cycle, and Cell Growth." *J Proteome Res* 2021;20(5):2596–2606. https://pubs.acs.org/doi/abs/10.1021/acs.jproteome.0c01037 *(NMNH ~5× NAD+ in HepG2; reductive stress; suppresses glycolysis/TCA/cell growth)*
6. "Preiss-Handler pathway / NaMN → NaAD → NAD" — Qualia review + Frontiers NMN review (Poddar/others, *Front Cell Dev Biol* 2020;8:246). https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2020.00246/full *(NaPRT forms NaMN from NA + PRPP; NMNAT → NaAD; NAD synthetase → NAD)*
7. Dellinger R, Migaud ME, Redpath P, Rhonemus T, Cunningham R (assignees Queen's University Belfast & ChromaDex Inc.). "Nicotinic acid riboside or nicotinamide riboside compositions, reduced derivatives thereof, and the use thereof to enhance skin permeation in treating skin conditions." US 10,280,190 B2. https://patents.google.com/patent/US10280190B2/en *(TOPICAL-SKIN patent; NR/NAR + reduced derivatives + triacetate prodrugs NRH-TA/NARH-TA; in-vitro A431 cytoprotection NRH-TA 88–94%, NARH-TA ~70–75%; NO human clinical data)*
8. Tempel W, et al. "Nicotinamide riboside and nicotinic acid riboside salvage in fungi and mammals: quantitative basis for Urh1 and purine nucleoside phosphorylase function in NAD+ metabolism." *J Biol Chem* 2007/2008; PMID 19001417. https://pubmed.ncbi.nlm.nih.gov/19001417/ *(NaR → NaMN → NaAD → NAD; NRK-dependent and -independent; PNP/Urh1 handling)*
9. "Therapeutic potential of dihydronicotinamide riboside (NRH) on obesity and glucose intolerance in mice." *Nat Commun* 2026; article s41467-026-70965-4. https://www.nature.com/articles/s41467-026-70965-4 *(metabolic mouse model; full text paywalled this session — doses/sample sizes/AEs [unverified], read primary before use)*
10. "Distinctive Gene Expression Profiles and Biological Responses of Skin Fibroblasts to Nicotinamide Mononucleotide: Implications for Longevity Effects on Skin." *Biomedicines* 2025;13(10):2395; PMC12561839. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12561839/ *(NMN — NOT next-gen — raises fibroblast NAD+/collagen, anti-senescence in vitro; included as family read-across only)*
11. NCT06889740. "Evaluate the Safety, Tolerability, and Efficacy of UthPeak NMNH (Reduced Nicotinamide Mononucleotide) in Healthy Adult Participants." Sponsor EffePharm Ltd. https://clinicaltrials.gov/study/NCT06889740 *(n=80; ORAL 125/250/500 mg/day 90 d; blood NAD+/biological age/6-min walk/SF-36; completed Jan 2025; results not yet published; no skin endpoint)*
12. "Nicotinic acid mononucleotide — overview" (ScienceDirect Topics) + Sigma N7764 (CAS 321-02-8). https://www.sigmaaldrich.com/US/en/product/sigma/n7764 *(NaMN is phosphorylated/charged — biology phosphorylates NA to NaMN to keep it inside cells; supports cell-impermeance argument)*
13. Kropotov A, et al. "Equilibrative Nucleoside Transporters Mediate the Import of Nicotinamide Riboside and Nicotinic Acid Riboside into Human Cells." *Int J Mol Sci* 2021;22(3):1391; PMC7866510. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7866510/ *(ENT1/2/4 import NR and NaR; HEK293; transport route, not skin efficacy)*
14. "CD38 mediates nicotinamide mononucleotide (NMN) base exchange to yield nicotinic acid mononucleotide (NaMN)." bioRxiv 2024; PMC11903787. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11903787/ *(salvage↔Preiss-Handler crosstalk via NaMN; mechanism; preprint — verify peer-review status)*
15. Sauve AA, et al. (Cornell University). "Use of nicotinic acid riboside or nicotinamide riboside derivatives, and reduced derivatives thereof, as NAD+ increasing precursors." US 10,183,036 B2 (and US20170304338A1). https://patents.google.com/patent/US20170304338A1/en *(IP over the NaR/NRH/NMNH concept itself)*
16. "Methods for producing dihydronicotinamide riboside from nicotinamide riboside chloride." EP 4214217 B1 / US20230271995A1. https://patents.google.com/patent/EP4214217B1/en *(production-method IP fencing the NRH space)*

---

### Verification notes
- **Real, confirmed primary sources this session:** [1] Yang/Sauve *JBC* 2019 (PMID 30948509), [2] Zapata-Pérez *FASEB J* 2021, [3] Mateuszuk *Front Immunol* 2022 (PMC8913500), [4] Sonavane *PLoS One* 2020 (PMID 33166357; PMC7652347 full text read), [5] Liu *J Proteome Res* 2021, [7] US10,280,190B2 (full claims/assignees read), [11] NCT06889740 (API record read), [13] Kropotov *IJMS* 2021 (PMC7866510). Author bylines verified where read; **confirm the full byline of [2], [5], [8] against the source before any author name appears in published copy**.
- **Partially unverified:** [9] *Nat Commun* 2026 NRH-obesity paper — abstract/search summary only; full-text doses, n, and adverse findings are **[unverified]**. [14] CD38→NaMN is a **bioRxiv preprint** — confirm peer-reviewed status before citing in copy. [6] mechanism is drawn from review/secondary sources for the pathway plumbing — accurate biochemistry, but cite a primary enzymology paper if used in copy.
- **Format/species discipline:** every efficacy-flavored item is **in-vitro or animal**; the single human item [11] is **oral and unpublished**; **no human topical study exists for any next-gen precursor.** The repo master-index grade ("fringe ❌") is correct and this dossier affirms **skip for topical**.
- **Safety counter-signals are load-bearing and verified:** NRH cytotoxicity [4] and pro-inflammation [3], NMNH reductive stress/growth suppression [5]. These distinguish the next-gen set from gentle niacinamide and should never be omitted when this class is discussed.
- **IP is time-sensitive:** the topical-skin patent [7] and concept patents [15][16] were confirmed at claim/assignee level this session; obtain a formal freedom-to-operate review before any commercial use.

---

## Evidence verification (adversarial)

**Overall topical-efficacy grade: D** (unproven topically; the dossier's own ❌-skip conclusion is well-founded). *Underlying NAD+-biochemistry quality grade for the mechanism story: B+* — but that strength is in-vitro/animal/oral and does **not** transfer to a topical cosmetic claim.

This dossier is unusually honest and was written defensively; adversarial re-checking *confirms* its central thesis (next-gen NAD+ precursors are research chemicals with zero human topical evidence and real safety counter-signals — skip for topical). The grade is D specifically for the *topical-cosmetic* question the brand cares about; it is not a criticism of the science.

### Headline-claim audit (HUMAN+TOPICAL? real cite? says what's claimed? funding/size?)

| # | Claim in dossier | Evidence type | Cite real & accurate? | Verdict |
|---|---|---|---|---|
| 1 | NRH raises cellular NAD+ 2.5–10× within 1 h, beats NR/NMN; NRK1/2-independent → NMNH | **In-vitro + animal (mouse IP)**, NOT human, NOT topical | [1] Yang/Sauve *JBC* 2019 (PMID 30948509) — **real, accurate** (authors Yang YY, Mohammed FS, Zhang N, Sauve AA, Weill Cornell confirmed) | Verified; correctly framed as cell/mouse only |
| 2 | NMNH active at 10× lower conc (5 µM) than NMN; ~doubles blood-NAD+ vs NMN in mice; raises NADH | **In-vitro + animal (mouse)**, NOT human, NOT topical | [2] Zapata-Pérez *FASEB J* 2021 — **real, accurate**; "5 µM / 10× lower" confirmed verbatim from source | Verified; framing correct |
| 3 | NRH is pro-inflammatory in macrophages (NF-κB, cytokines, LPS potentiation) | **In-vitro** (BMDM/THP-1), NOT human, NOT skin | [3] *Front Immunol* 2022;13:840246 — paper **real & accurate**, BUT **first author was wrong in original draft** (it is **Chini CCS et al., Mayo Clinic**, not "Mateuszuk Ł / Goncalves lab"). **Corrected in this pass.** Academic (Mayo), not industry. | Content verified; byline fixed |
| 4 | NRH selectively cytotoxic to HepG3 (~15–90% at 100–1000 µM) via mito superoxide/depolarization/mtDNA damage/apoptosis | **In-vitro** (cancer cell line), NOT human skin | [4] Sonavane *PLoS One* 2020 (PMID 33166357; PMC7652347) — **real, accurate**; authors Sonavane, Hayat, Makarov, Migaud, Gassman confirmed | Verified; cancer-cell context noted appropriately |
| 5 | NMNH causes reductive stress; suppresses glycolysis/TCA/cell growth | **In-vitro + mouse liver**, NOT human skin | [5] Liu *J Proteome Res* 2021 (PMID 33793246) — **real, accurate** | Verified |
| 6 | Topical prodrug route (NRH-TA/NARH-TA) is patented; in-vitro A431 cytoprotection 88–94% | **In-vitro only; patent, not a trial** | [7] US10,280,190B2 — **real**; title, both assignees (Queen's Belfast + ChromaDex), inventors, in-vitro-only A431 data all **confirmed**; no human/animal data in patent | Verified; correctly labeled "commercial filing, not a trial" |
| 7 | Human NMNH trial exists (NMNH/UthPeak) | **Human ORAL, no skin endpoint, results unpublished** | [11] NCT06889740 — **real & confirmed** via registry API: EffePharm (industry), n=80, oral 125/250/500 mg, 90 d, **Completed, no results posted, zero skin endpoints**. Registered title is **pharmacokinetics**, not "efficacy" (corrected). | Verified; dossier's "treat as marketing" stance on the topline figures is correct |
| 8 | No human topical study exists for any next-gen precursor | Absence claim | Consistent with all searches this session | Verified — TIER D genuinely empty |

### Main caveats (load-bearing)

- **Format/species mismatch is total.** Every efficacy-flavored claim is in-vitro or rodent; the one human datapoint is oral, unpublished, and has no skin endpoint. Nothing here is human + topical. The dossier states this clearly and does not overreach — good.
- **The "more potent" data are NAD+-number readouts, not skin or even health outcomes.** "Beats NR/NMN" means "raises a cell's NAD+ more," which the dossier correctly refuses to equate with skin benefit.
- **Safety counter-signals are real and verified** (inflammation [3], cytotoxicity [4], reductive stress [5]) — these are the strongest, best-supported claims in the file and genuinely differentiate this set from gentle niacinamide.
- **Industry vs academic:** the cell/animal mechanism papers [1]–[5] are academic; the only human trial [11] is industry (EffePharm) and its publicized "3× NAD+ / ~5 years younger / +35% energy" topline is **self-reported marketing, not peer-reviewed** — the dossier already labels it as such. Do not cite those numbers as evidence.

### Corrections made to the dossier in this pass

1. **[3] author byline fixed** — was "Mateuszuk Ł, et al. (Goncalves lab)"; the actual first author of *Front Immunol* 2022;13:840246 is **Chini CCS** (senior author Chini EN, Mayo Clinic). The paper's *content* was accurate; only the attribution was wrong. (This is precisely the byline risk the original verification note flagged.)
2. **[2] PMID removed/flagged** — the listed "PMID 33793246" does **not** belong to Zapata-Pérez; it is Liu's paper [5]. Source line now cites [2] by DOI and warns against the swap.
3. **[11] title corrected** — registered title is "...Safety, Tolerability, and **Pharmacokinetics**," not "...and Efficacy"; the biological-age/longevity readouts are secondary/exploratory.

### Claims to keep softened / never ship

- Any "recharges skin NAD+ / clinically proven / more potent than niacinamide (as a skin claim) / anti-inflammaging" for NaMN/NaR/NRH/NMNH — **unsubstantiated topically**, and for NRH **contradicted** by [3][4]. The dossier already routes all NAD/longevity *product* claims to niacinamide and treats these molecules as education-only; that is the correct, defensible posture. No further softening of the conclusions is needed — the file was already appropriately conservative.
