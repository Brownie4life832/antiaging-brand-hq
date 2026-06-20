# Ingredient: BCL-2 / BCL-xL Inhibitor Senolytics — Navitoclax (ABT-263), ABT-737, A1331852, A1155463 (INCI: **none — not cosmetic ingredients**)

**Researched:** 2026-06-19 · **Status:** ⬜ considering / ⬜ shortlisted / ☑ rejected / ⬜ in a product
**Class:** Senotherapeutics & senolytics (BH3-mimetic apoptosis inducers) · **Slug:** `bcl-inhibitor-senolytics`

> Exhaustive literature review. **Brutally honest headline up front:** these are **investigational anti-cancer
> drugs**, not cosmetic ingredients. Navitoclax is an unapproved oncology agent with a real, dose-limiting
> bleeding toxicity (thrombocytopenia). ABT-737, A1331852, and A1155463 are **lab reagents only** — never tested
> in humans for anything. Every "rejuvenates aged skin" headline traces to **rodent or mouse-grafted-human-skin
> experiments using injected or DMSO-driven drug**, not a cosmetic. There is **zero** legitimate human topical
> cosmetic evidence, **zero** INCI registration, and using any of them in a consumer skincare product would be
> selling an unapproved drug. This dossier exists to document *why this class is a hard skip for a cosmetic
> brand* and to map what the senescence biology does (and doesn't) support.

---

## 1. Identity

This "ingredient" is actually a **family of BH3-mimetic small molecules** that inhibit anti-apoptotic BCL-2-family proteins. They are pharmaceutical compounds, not cosmetic actives.

| Compound | Aliases | Target selectivity | Status |
|---|---|---|---|
| **Navitoclax** | ABT-263 | BCL-2, BCL-xL, BCL-w (pan, oral) | Investigational oncology drug; **not FDA-approved** [11][12] |
| **ABT-737** | — | BCL-2, BCL-xL, BCL-w (pan, IV/IP only; poor oral bioavailability/solubility) | Lab reagent / tool compound [1][6] |
| **A1331852** | — | **BCL-xL-selective** | Lab reagent only [3] |
| **A1155463** | — | **BCL-xL-selective** | Lab reagent only [3] |

- **Common name:** "BCL-2/BCL-xL inhibitor senolytics," "BH3 mimetics," sometimes lumped under "first-generation senolytics" (alongside the dasatinib + quercetin combo, which works by a different route).
- **INCI:** **None.** None of these molecules has an INCI name, a cosmetic registration, or a CAS listing as a cosmetic ingredient. Navitoclax CAS 923564-51-6 is registered as a **pharmaceutical API**. This single fact mostly settles the brand question (see §8, §11).
- **Forms / derivatives in development (all pharma, all to *reduce* navitoclax's platelet toxicity):**
  - **DT2216** — a BCL-xL **PROTAC degrader** (uses VHL E3 ligase, which platelets barely express → platelet-sparing). In a first-in-human Phase 1 oncology trial. [9][10]
  - **Nav-Gal** — galacto-conjugated navitoclax prodrug, cleaved selectively by senescent cells' high lysosomal β-galactosidase, sparing platelets. [7] (Preclinical.)
  - **PZ15227** — BCL-xL PROTAC, senolytic without thrombocytopenia in mice. [7]
  - These are **oncology/gerotherapeutic R&D**, not cosmetic raw materials.

**Nomenclature caution:** Do not confuse with **venetoclax (ABT-199)**, the FDA-approved, BCL-2-*selective*, platelet-sparing leukemia drug — it is generally **not** senolytic against most senescent cell types (senescence resistance leans on BCL-xL, which venetoclax doesn't hit). And do not confuse this pharmaceutical class with **botanical "senolytics"** like fisetin/quercetin (separate dossiers) or the **senomorphic peptide OS-01** ([`senolytics-os01-peptide.md`](senolytics-os01-peptide.md)) — those are at least plausibly cosmetic; these are not.

---

## 2. Class & mechanism

These are genuine **senolytics** — they selectively *kill* senescent ("zombie") cells, as opposed to **senomorphics** (e.g., OS-01) that merely quiet the senescent phenotype. This is the strongest mechanistic story in the senescence field, and the mechanism is well understood:

- **The "primed for death" biology.** Senescent cells are under chronic apoptotic stress from their own SASP and DNA damage, yet they survive by **upregulating anti-apoptotic BCL-2-family proteins** (BCL-2, BCL-xL, BCL-w) — these are part of the "senescent cell anti-apoptotic pathways" (SCAPs). The cells are simultaneously primed to die (high pro-apoptotic BAX/BAK, BH3-only proteins) yet held alive by these guardians. [4][6]
- **BH3-mimetic action.** Navitoclax/ABT-737 occupy the hydrophobic BH3-binding groove of BCL-2/BCL-xL/BCL-w, **displacing pro-apoptotic effectors (BAX/BAK)** → mitochondrial outer-membrane permeabilization → cytochrome-c release → caspase cascade → apoptosis. In senescent cells, which are perched on the edge, this tips them over; healthy cells, less dependent on these guardians, largely survive. [2][6]
- **BCL-xL is the key node in many senescent cells.** That's why **BCL-xL-selective** A1331852/A1155463 are senolytic in endothelial cells and fibroblasts — and why **BCL-2-selective venetoclax is largely *not* senolytic.** [3][6]
- **Cell-type specificity (a crucial nuance, not a footnote).** These drugs are **not universal senolytics.** They efficiently kill senescent endothelial cells (HUVECs), senescent lung fibroblasts (IMR90, WI-38) and mouse embryonic fibroblasts — "more than 60% of senescent WI-38, IMR-90, HUVECs, and MEFs in 72 h" — but **do NOT kill senescent human primary preadipocytes.** [2][3][6] Senescence survival programs differ by cell lineage; no single senolytic clears them all. For skin, the relevant fact is that **dermal fibroblasts and endothelial cells are sensitive** — the right targets for skin aging.

**Net cell-level story:** remove the BCL-xL "survival shield" → senescent dermal fibroblasts/endothelial cells undergo apoptosis → fewer SASP-secreting cells → less local inflammation, less MMP-driven collagen breakdown → (in mouse/grafted-skin models) measurably more collagen and better wound healing. The biology is real; the *delivery as a cosmetic* is the problem.

---

## 3. Hallmarks of skin aging targeted

| Hallmark | Targeted? | Basis / honest caveat |
|---|---|---|
| **Cellular senescence** | ✅ Primary | Direct, validated senolysis of senescent fibroblasts/endothelium [2][3][6]; the single best-evidenced mechanism in the field |
| **Inflammaging** | ✅ | Killing SASP-secreting cells lowers IL-6, IL-1α, CXCL8 etc. in models [4][13] |
| **Collagen / ECM loss** | ✅ (model only) | ~30% ↑ collagen density and ↓ MMPs in mouse-grafted aged *human* skin after injected navitoclax [8] |
| **Photoaging** | ⚠️ Plausible | ABT-263/ABT-737 reduce UV-induced senescent fibroblasts, ↓IL-6, ↓MMP-1 in vitro [13]; no human topical photoaging endpoint |
| **Barrier decline** | ⚠️ Indirect | Better wound healing/epidermal regeneration in mice [5]; no direct human TEWL/barrier data |
| **Hair-follicle / regeneration** | ⚠️ (model) | ABT-737 ↑ hair-follicle stem-cell proliferation in mouse epidermis [1] |
| **Oxidative stress** | ❌ Not direct | Not an antioxidant; only indirect via removing ROS-generating senescent cells |
| **Mitochondrial decline** | ⚠️ Mechanistic | Acts *on* mitochondrial apoptosis machinery; not a "mito support" actor in the cosmetic sense |
| **Glycation / AGEs** | ❌ | No evidence |
| **Pigmentation / tone** | ❌ | No direct evidence (senescent melanocytes exist but not targeted in these studies) |
| **Hydration** | ❌ | No evidence |
| **Microbiome** | ❌ | No evidence |

**Honest framing:** the mechanism maps beautifully onto the *theory* of skin longevity (clear the zombie cells, restore the dermis). The hallmark column looks strong, but **almost every ✅/⚠️ rests on animal or ex-grafted-tissue data with non-cosmetic delivery.**

---

## 4. Evidence review by tier ← core of this dossier

**Overarching honesty flag:** there is a **complete absence of human topical cosmetic evidence.** The human data that exist are **oncology safety/efficacy trials of oral navitoclax for cancer** (which establish toxicity, not skin benefit) and **mouse experiments — including a mouse model carrying grafted aged human skin — using injected or DMSO-dissolved drug.** Nothing here is a cosmetic, and nothing has been tested as one in people.

### Tier 1 — In-vitro & ex-vivo (deepest, most consistent evidence)

**Zhu et al. (2016), *Aging Cell* — "Identification of a novel senolytic agent, navitoclax (ABT-263), targeting the Bcl-2 family of anti-apoptotic factors."** [2]
- Foundational paper establishing navitoclax as senolytic. Kills senescent HUVECs, IMR90 & WI-38 fibroblasts, MEFs (>60% in 72 h) by inducing apoptosis; **does NOT kill senescent human preadipocytes** — first clear demonstration of cell-type-specific senolysis. Mechanism mapped to BCL-2 / BCL-xL / BCL-w dependence.
- **Limitation:** in-vitro; flagged platelet/neutrophil toxicity risk as the translational hurdle.

**Zhu et al. (2017), *Aging (Albany NY)* — "New agents that target senescent cells: the flavone, fisetin, and the BCL-XL inhibitors, A1331852 and A1155463."** [3]
- Introduced the **BCL-xL-selective** senolytics A1331852 & A1155463. Senolytic in senescent **HUVECs and IMR90 fibroblasts**, **not** in preadipocytes. Argued these are better translational candidates than navitoclax because BCL-xL-selectivity should cause **less BCL-2-mediated neutropenia** — though BCL-xL inhibition still drives platelet toxicity.
- **Limitation:** in-vitro reagents; never advanced to humans.

**Saleh et al. (2020), *Molecular Oncology*** [14] — mechanistic confirmation that ABT-263 clears therapy-induced senescent tumour cells via **interference with the BCL-xL–BAX interaction.** Supports mechanism; oncology context.

**Photoaging / dermal fibroblast in-vitro work** [13] — in UV/UVB-induced senescent human dermal fibroblast models, ABT-263 and ABT-737 reduced senescent-cell burden, lowered SASP factors (IL-6) and decreased MMP-1, with relative preservation of collagen. This is the most skin-relevant in-vitro signal, but it is cell-culture only.

**Bottom line, Tier 1:** robust, reproducible, mechanism-anchored. These compounds genuinely kill senescent dermal fibroblasts and endothelial cells in a dish. This is real science — it just lives in cell culture.

### Tier 2 — Animal (the bulk of the "rejuvenation" headlines)

**Chang et al. (2016), *Nature Medicine* — "Clearance of senescent cells by ABT263 rejuvenates aged hematopoietic stem cells in mice."** [4]
- Seminal in-vivo senolytic paper. Oral **navitoclax (gavage) cleared senescent cells in irradiated/aged mice**, rejuvenating hematopoietic and muscle stem cells. Established navitoclax as a systemic senolytic in vivo. **Not skin; systemic dosing.**

**Yosef et al. (2016), *Nature Communications* — "Directed elimination of senescent cells by inhibition of BCL-W and BCL-XL."** [1] *(Most skin-relevant animal study.)*
- Joint BCL-W/BCL-XL inhibition (siRNA or **ABT-737**) selectively apoptoses senescent cells. **In a transgenic mouse (K5-rtTA/tet-p14^ARF) where p53-driven senescence is induced in the basal epidermis,** ABT-737 (**75 mg/kg intraperitoneal, 2–4 days**) **dramatically reduced epidermal SA-β-gal+ senescent cells** and **increased proliferating hair-follicle bulge stem cells (CD34+/CD49f^high).**
- **Limitation:** transgenic/artificial senescence, **IP injection**, not topical, not natural aging.

**Takaya, Ishii, Asou, Kishi (2023), *Rejuvenation Research* — "Navitoclax (ABT-263) Rejuvenates Human Skin by Eliminating Senescent Dermal Fibroblasts in a Mouse/Human Chimeric Model."** [8] *(The headline "rejuvenates HUMAN skin" study — read the fine print.)*
- **Model:** aged **human** skin grafts (male donors **78–91 yr**) transplanted onto nude mice. Drug given as **intraperitoneal injection, 50 mg/kg/day** — **NOT topical.**
- **Results:** **~60% reduction** in senescent-cell stain; **~30% increase in collagen density**; reduced SASP gene activity (MMPs, IL-1α).
- **Limitation (authors' own):** systemic injection, not a cream; they explicitly raise whether topical delivery "such as a skin cream" could work — i.e., topical was *not* tested here. This is the study most often mis-cited as proof a topical product works. It is not.

**Shvedova et al. (2024), *Aging (Albany NY)* — "Topical ABT-263 treatment reduces aged skin senescence and improves subsequent wound healing."** [5] *(The only genuinely TOPICAL study — and it's in mice.)*
- **Model:** C57BL/6 mice, **24-month-old aged** vs 2-month young; **n = 5/group** (5–8/timepoint for wounds).
- **Dosing:** **5 µM ABT-263 dissolved in DMSO**, applied to dorsal skin **5 consecutive days** (DMSO = vehicle control). **DMSO is doing real penetration work** (a strong solvent/penetration enhancer, not a cosmetically benign vehicle).
- **Senescence:** significant ↓ p16 & p21 gene expression and ↓ p21+/SA-β-gal+ cells in aged skin vs DMSO; **no effect in young skin** (consistent with senolysis being burden-dependent).
- **Wound healing:** wounds made 5 days post-treatment; **33% of ABT-263 mice fully healed by day 18 vs 0% DMSO; 80% vs 56.3% by day 24** (~1.4×). RNA-seq showed upregulation of hemostasis, inflammation, proliferation, angiogenesis, collagen synthesis, ECM organization.
- **Notable safety signal even topically:** **transient inflammation with increased F4/80+ macrophage infiltration** in dermis (authors frame the inflammation as ultimately pro-healing — but it is an irritation/inflammation signal). Reported **no significant change in serum platelets** after 5 days topical (suggesting limited systemic absorption at this dose).
- **Limitations (authors' own):** mouse, tiny n, short term, results "differ somewhat from other studies" depending on age/delivery/timepoints; preliminary; DMSO vehicle.
- **Conflicts:** authors declare none; NIH/NIA-funded (R03AG067983, K76AG083300) — i.e., academic, not industry-cosmetic.

**Counter-evidence — same drug, *harmful* in another tissue.** Sharma et al. (2020), *Frontiers in Cell & Dev. Biology* [15]: in aged mice, systemic navitoclax (50 mg/kg/day, 2 wks) **reduced senescent-cell burden but caused trabecular bone loss** (−60.1% bone-volume-fraction in females, −45.6% males) and **impaired osteoblast mineralization** (−88%/−83%). A vivid reminder that "clear senescent cells" is **not uniformly beneficial** — off-target/on-target harms are real.

### Tier 3 — Human, ORAL (exists — but it is *oncology toxicity* data, not skin)

There **is** substantial human data on **oral navitoclax** — entirely in **cancer trials**, and it is mostly a **safety/toxicity** record, not a longevity benefit:
- **Roberts et al. (2012), *J Clin Oncol*** — Phase 1 in relapsed/refractory CLL; **thrombocytopenia was the dose-limiting toxicity.** [16]
- **Phase 2a lymphoid-malignancy study (2020)** — grade 3/4 **thrombocytopenia 38.5%, neutropenia 30.8%**; required a 7-day lead-in dose titration to manage platelet drop. [17]
- **Myelofibrosis program (navitoclax + ruxolitinib, 2022–2025)** — ongoing; **navitoclax remains investigational and unapproved** as of 2025. [11][12]
- **DT2216 (BCL-xL PROTAC) first-in-human Phase 1 (2025)** — designed specifically to *reduce* the platelet toxicity that limits navitoclax. [9][10]

**What the human-oral record proves for skincare:** essentially nothing positive — and it proves the **central safety problem** (systemic BCL-xL inhibition kills platelets → bleeding risk). It is "borrowed" only as a *caution*, not as a benefit.

### Tier 4 — Human, TOPICAL

**None. Zero.** There is **no** human topical study — not an RCT, not a pilot, not a case series — of navitoclax, ABT-737, A1331852, or A1155463 applied to human skin as a cosmetic or otherwise. The "human skin" data (Takaya [8]) used **injected drug on grafted tissue in mice.** The only topical study (Shvedova [5]) is **in mice with a DMSO vehicle.**

**What is actually proven for TOPICAL human use:** **nothing.** Any product or copy implying a topical BCL-inhibitor "clears senescent cells in your skin" or "rejuvenates skin" is **borrowing from mouse and grafted-tissue data with injected/DMSO-delivered pharmaceutical drug**, and is making a drug claim about an unapproved drug.

---

## 5. Topical bioavailability / penetration

- **Navitoclax is a large, lipophilic molecule (~974 Da)** — far above the ~500 Da "rule-of-500" for easy stratum-corneum passage, and poorly water-soluble. ABT-737 has notoriously poor solubility/oral bioavailability (the very reason oral ABT-263 was developed). [6] These are not molecules that diffuse readily into living dermis from a normal cosmetic emulsion.
- The single topical study achieved penetration **only by dissolving the drug in DMSO** [5] — a potent penetration enhancer that itself causes stinging/irritation and is not used at functional penetration-enhancing levels in mainstream cosmetics. Remove DMSO and the delivery case largely collapses.
- **No published human skin PK/penetration data** for any of these compounds.
- **The delivery paradox:** you need the drug to reach senescent dermal fibroblasts/endothelium (deep dermis) at a senolytic concentration, but *not* systemically (to avoid platelet toxicity). Threading that needle is an open pharmaceutical-delivery problem, not something solved by a cosmetic base.

---

## 6. Formulation

**Not formulable as a cosmetic** — included only to document why.
- **Use level / concentration:** undefined for cosmetics; the topical mouse study used **5 µM in DMSO** [5]. There is no established safe cosmetic concentration because it is not a cosmetic ingredient.
- **pH / stability:** pharmaceutical-grade handling; lipophilic, poorly water-soluble; would demand solvents/penetration enhancers (DMSO-like) that are themselves problematic in a consumer product.
- **Pairings:** N/A — this is a controlled investigational drug, not something to "pair with niacinamide."
- **Sensory:** the only working vehicle (DMSO) is an irritant with a characteristic odor/aftertaste-on-skin; the topical study itself recorded transient inflammation and macrophage infiltration. [5]
- **Practical reality:** any legitimate skin development of this class (e.g., a senolytic topical for dermatoporosis or wound healing) would proceed as a **prescription drug** through clinical trials, **not** as a cosmetic.

---

## 7. Safety

- **Systemic toxicity (the headline risk):** **thrombocytopenia** — navitoclax/BCL-xL inhibition directly kills platelets (platelets depend on BCL-xL for survival). This is the **dose-limiting toxicity in every oral human trial** [16][17] and the entire reason for the platelet-sparing redesigns (venetoclax, DT2216, Nav-Gal). Also **neutropenia** with pan-BCL-2 inhibition. [17]
- **Topical systemic-exposure question:** the mouse topical study reported **no serum-platelet change after 5 days** [5] — encouraging that low-dose topical may limit systemic exposure, **but** this is mouse, 5 days, n=5, with no human confirmation. Scaling concentration/area for human use could plausibly cross into systemic exposure.
- **Local irritation/inflammation:** even topically, ABT-263 caused **transient inflammation and macrophage infiltration** in mouse dermis [5]; DMSO vehicle adds its own irritation.
- **On-target collateral harm:** clearing senescent cells is **not universally good** — systemic navitoclax caused **bone loss and impaired osteoblast function** in aged mice [15]. Senescent cells have legitimate roles (wound healing, fibrosis limitation, tumour suppression); indiscriminate killing has trade-offs.
- **Sensitization / HRIPT:** none performed — never tested as a cosmetic.
- **Pregnancy/breastfeeding:** **contraindicated by default.** A pro-apoptotic, cytotoxic, genotoxic-adjacent anti-cancer drug must be treated as unsafe in pregnancy. Do not use, do not market.
- **Sourcing:** sold as a **research chemical / pharmaceutical API** ("for research use only," not for human application) by reagent suppliers — buying it for a consumer product would be both a regulatory and ethical violation.

---

## 8. Regulatory & claims (per CLAUDE.md guardrails)

**This is the decisive section.** Under US FDA, a product's *intended use* and *ingredients* determine its category, and these compounds fail the cosmetic test on every axis:

1. **It is a drug, not a cosmetic, by composition.** Navitoclax is an **investigational new drug** (active in oncology INDs/trials) and is **not FDA-approved for any use** [11][12]. ABT-737/A1331852/A1155463 are **research reagents.** None has an INCI name or cosmetic regulatory clearance in the US, EU, or anywhere. Putting an unapproved drug in a cosmetic makes the product an **unapproved new drug + adulterated/misbranded cosmetic** — a serious FDA violation, not a labeling nuance.
2. **The mechanism is inherently a "drug" claim.** "Kills/clears senescent cells," "induces apoptosis," "rejuvenates skin," "increases collagen," "improves wound healing" are all **structure/function or disease claims** with no OTC monograph — automatically drug territory. There is no compliant cosmetic way to describe what this molecule does, because what it does *is* pharmacology.
3. **No defensible cosmetic claim exists** because there is no human topical cosmetic evidence to substantiate any claim, and the only honest mechanistic description is a drug action.

- ✅ **Safe cosmetic language:** **none applies** — there is no cosmetic use to describe.
- ⚠️ **Forbidden:** "senolytic," "clears zombie/senescent cells," "rejuvenates skin," "boosts collagen," "heals wounds," "reverses skin aging," or naming navitoclax/ABT-263/ABT-737 on a product. Each is an unapproved-drug claim about an unapproved drug.
- **Educational use only:** the brand may *reference this science* in editorial/explainer content ("the cutting edge of senescence research includes BCL-xL senolytics, currently studied as drugs, not skincare") — clearly framed as **investigational pharmacology, not our product.** This is the only legitimate brand touchpoint.

See [`../../brand/glossary.md`](../../brand/glossary.md) claim cheat-sheet and the claims guardrail in [`../../CLAUDE.md`](../../CLAUDE.md).

---

## 9. Sourcing & cost

- **Availability:** sold only as **research-use-only reagents** (e.g., MedChemExpress, Selleck, Cayman) or as **pharmaceutical API** under controlled supply. **Not** available as a cosmetic raw material with a CoA for skin use, an INCI, or supplier safety data appropriate for consumer leave-on products.
- **Cost:** research-reagent pricing is high per mg, but cost is irrelevant — the compound **cannot be lawfully or ethically used in a consumer cosmetic.**
- **Supply/ethics:** procuring an investigational anti-cancer drug to formulate into a face cream is a non-starter for a credible brand; it would also fail any responsible-sourcing, insurance, and retailer-compliance review.

---

## 10. Hype vs. evidence

| Marketing claim (seen in longevity/press coverage) | Reality |
|---|---|
| "Navitoclax rejuvenates aged human skin" | True **only** in a mouse carrying grafted human skin, with **injected** drug (50 mg/kg IP), not topical, not a cosmetic. [8] |
| "Topical senolytic clears your skin's zombie cells" | Shown **in mice**, with the drug dissolved in **DMSO**, n=5, 5 days. [5] No human topical data exist. |
| "Senolytics are the future of anti-aging skincare" | The *category* is promising; **these specific molecules are drugs** with a dose-limiting bleeding toxicity, not skincare actives. |
| "+30% collagen, −60% senescent cells" | Real numbers — from **injected drug on grafted tissue in mice.** [8] Not transferable to a cosmetic cream. |
| "Proven and safe" | Navitoclax is **unapproved**, causes **thrombocytopenia** in humans [16][17], and caused **bone loss** in aged mice [15]. Not safe to self-administer. |
| "You can buy it as an ingredient" | It's a **research chemical / unapproved drug**, not a cosmetic ingredient — using it in product is illegal. |

Independent expert framing converges on: BCL-2/BCL-xL senolytics are the **most mechanistically validated senolytics**, but their future in skin is as **physician-supervised drugs** (for indications like dermatoporosis, wound healing, fibrosis), pursued via clinical trials — **not** as OTC cosmetics. The genuinely interesting science is being used to sell a fantasy product.

---

## 11. Verdict for the brand

❌ **SKIP — hard skip. This is a class to *understand and reference*, never to *formulate*.**

- **Why skip (non-negotiable):** these are **unapproved investigational drugs / lab reagents**, not cosmetic ingredients. No INCI, no cosmetic regulatory status, a real human dose-limiting toxicity (thrombocytopenia), documented off-target harm (bone loss), and **zero human topical cosmetic evidence.** Using any of them would mean selling an adulterated cosmetic / unapproved drug — fatal to a credibility-first brand and a serious legal exposure. This is the cleanest "no" in the senolytics space.
- **Why it's still worth a dossier:** BCL-xL senolytics are the **scientific gold standard for the senolytic mechanism** (genuine apoptosis of senescent dermal fibroblasts/endothelium, validated across many models). They are the benchmark against which *cosmetically viable* senotherapeutics (peptides like OS-01, botanicals like fisetin/quercetin, senomorphics) should be honestly compared — usually showing those gentler options are far less potent senolytics but far more appropriate for a cream.
- **Longevity relevance:** **High in the science, zero in the bottle.** The senescence-clearance thesis is the most compelling story in skin longevity, and this class proves the mechanism — which makes it powerful **editorial/educational** material (explaining *why* the brand pursues gentle, evidence-based senotherapeutics) without ever appearing in a formula.
- **Strategic alternative:** if the brand wants a "senescence" angle, build it on **(a)** a senomorphic/senotherapeutic peptide with a cosmetic INCI and at least some human topical data (OS-01/Decapeptide-52 — conditional, see its dossier), and/or **(b)** botanical senotherapeutics (fisetin, quercetin), all framed with honest "supports/visibly" cosmetic language. Reference BCL-xL senolytics only as the *research frontier* the brand respects but does not (and cannot) sell.

Log in [`../../ideas/not-considering.md`](../../ideas/not-considering.md) with reason: **"Unapproved investigational anti-cancer drugs / research reagents — no INCI, no cosmetic status, dose-limiting human toxicity, zero human topical cosmetic evidence; illegal to formulate. Keep as science reference / benchmark only."**

---

## 12. Sources

1. Yosef R, Pilpel N, Tokarsky-Amiel R, et al. (2016). "Directed elimination of senescent cells by inhibition of BCL-W and BCL-XL." *Nature Communications* 7:11190. (ABT-737; in-vivo epidermal senescence clearance + hair-follicle stem-cell proliferation.) https://www.nature.com/articles/ncomms11190 · PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC4823827
2. Zhu Y, Tchkonia T, Fuhrmann-Stroissnigg H, et al. (2016). "Identification of a novel senolytic agent, navitoclax, targeting the Bcl-2 family of anti-apoptotic factors." *Aging Cell* 15(3):428–435. (Navitoclax senolytic; cell-type specificity; preadipocytes resistant.) https://onlinelibrary.wiley.com/doi/full/10.1111/acel.12445
3. Zhu Y, Doornebal EJ, Pirtskhalava T, et al. (2017). "New agents that target senescent cells: the flavone, fisetin, and the BCL-XL inhibitors, A1331852 and A1155463." *Aging (Albany NY)* 9(3):955–963. https://www.aging-us.com/article/101202/text · PubMed: https://pubmed.ncbi.nlm.nih.gov/28273655/
4. Chang J, Wang Y, Shao L, et al. (2016). "Clearance of senescent cells by ABT263 rejuvenates aged hematopoietic stem cells in mice." *Nature Medicine* 22(1):78–83. https://www.nature.com/articles/nm.4010
5. Shvedova M, et al. (2024). "Topical ABT-263 treatment reduces aged skin senescence and improves subsequent wound healing." *Aging (Albany NY)* 16. (Mouse; 5 µM ABT-263 in DMSO; the only topical study.) https://www.aging-us.com/article/206165/text · PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11810067/ · preprint: https://www.biorxiv.org/content/10.1101/2024.08.19.608670
6. Kirkland JL, Tchkonia T, et al. — review: "Senescent Cell Depletion Through Targeting BCL-Family Proteins and Mitochondria." *Frontiers in Physiology* (2020) 11:593630. (Mechanism, cell-type specificity, toxicity, redesigns.) https://www.frontiersin.org/articles/10.3389/fphys.2020.593630/full
7. González-Gualda E, et al. (2020). "Galacto-conjugation of Navitoclax as an efficient strategy to increase senolytic specificity and reduce platelet toxicity" (Nav-Gal). *Aging Cell* 19(4):e13142. https://onlinelibrary.wiley.com/doi/10.1111/acel.13142
8. Takaya K, Ishii T, Asou T, Kishi K (2023). "Navitoclax (ABT-263) Rejuvenates Human Skin by Eliminating Senescent Dermal Fibroblasts in a Mouse/Human Chimeric Model." *Rejuvenation Research* 26(1):9–20. (Aged human skin grafts, donors 78–91; **IP injection 50 mg/kg/day**; ~30% ↑collagen, ~60% ↓senescent stain.) https://www.liebertpub.com/doi/10.1089/rej.2022.0048 · summary: https://www.nad.com/news/navitoclax-rejuvenates-aged-human-skin
9. Khan S, Zhang X, Lv D, et al. (2019). "A selective BCL-XL PROTAC degrader achieves safe and potent antitumor activity" (DT2216). *Nature Medicine* 25:1938–1947. https://www.nature.com/articles/s41591-019-0668-z
10. First-in-human Phase 1 study of DT2216, a selective BCL-xL degrader (2025). *Journal of Hematology & Oncology* 18. https://link.springer.com/article/10.1186/s13045-025-01753-8 · PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12613848/
11. ASCO/AbbVie myelofibrosis program — "Addition of Navitoclax to Ongoing Ruxolitinib Therapy…" *Journal of Clinical Oncology* (2022) & Blood Neoplasia (2024). (Navitoclax remains investigational/unapproved.) https://ascopubs.org/doi/10.1200/JCO.21.02188
12. ClinicalTrials.gov — Navitoclax + ruxolitinib in myelofibrosis (NCT04472598). (Investigational status.) https://clinicaltrials.gov/study/NCT04472598
13. Review of dermal fibroblast senescence & senotherapeutics (2024–2025) — ABT-263/ABT-737 reduce UV-induced senescent fibroblasts, ↓IL-6, ↓MMP-1 in vitro. *(PMC review)* https://pmc.ncbi.nlm.nih.gov/articles/PMC12213903/
14. Saleh T, Bloukh S, et al. (2020). "Clearance of therapy-induced senescent tumor cells by the senolytic ABT-263 via interference with BCL-XL–BAX interaction." *Molecular Oncology* 14(10):2504–2519. https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.12761 · PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7530780/
15. Sharma AK, Roberts RL, et al. (2020). "The Senolytic Drug Navitoclax (ABT-263) Causes Trabecular Bone Loss and Impaired Osteoprogenitor Function in Aged Mice." *Frontiers in Cell & Developmental Biology* 8:354. (On-target harm: −60.1%/−45.6% bone-volume-fraction.) https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2020.00354/full · PubMed: https://pubmed.ncbi.nlm.nih.gov/32509782/
16. Roberts AW, Seymour JF, Brown JR, et al. (2012). "Substantial susceptibility of chronic lymphocytic leukemia to BCL2 inhibition: results of a phase I study of navitoclax in patients with relapsed or refractory disease." *J Clin Oncol* 30(5):488–496. (Thrombocytopenia = dose-limiting toxicity.) https://pubmed.ncbi.nlm.nih.gov/22184378/
17. "Safety and efficacy of navitoclax, a BCL-2 and BCL-XL inhibitor, in patients with relapsed or refractory lymphoid malignancies: results from a phase 2a study." *Leukemia & Lymphoma* (2020). (Grade 3/4 thrombocytopenia 38.5%, neutropenia 30.8%; 7-day lead-in titration.) https://www.tandfonline.com/doi/full/10.1080/10428194.2020.1845332

---

## Evidence verification (adversarial)

_Verified 2026-06-19 by independent re-reading/cross-checking of primary sources: Yosef 2016 Nat Commun [1]; Zhu 2016 Aging Cell [2] & Zhu 2017 Aging [3]; Chang 2016 Nat Med [4]; Shvedova 2024 Aging [5] (full PMC extraction); Takaya 2023 Rejuv Res [8]; Sharma 2020 Front Cell Dev Biol [15]; navitoclax oncology toxicity trials [16][17]; FDA-status/clinical-trial records [11][12]. Goal: catch any benefit quietly borrowed from animal/injected/oncology data and presented as topical-cosmetic proof, and confirm the regulatory "drug not cosmetic" conclusion. **Re-audited 2026-06-19 (second, independent adversarial pass): every headline number below was re-traced to its primary source and matches — see "What re-verification confirmed."**_

### Overall evidence grade for TOPICAL COSMETIC use: **D** (unproven topically / hype from a cosmetic standpoint — no human topical cosmetic evidence of any kind exists).

Mechanistic/animal grade for the senolytic *mechanism* (i.e., the pharmacology, not cosmetic use): **A–B** — strong and reproducible across many independent labs, but **pharmacological, delivered by injection or DMSO, never as a cosmetic.** The two grades must not be conflated: the mechanism being A-grade does **not** lift the cosmetic grade above D, because the cosmetic-relevant question (does a topically applied cosmetic do anything in human skin?) has zero supporting evidence.

- **Mechanism (A-grade, verified):** BCL-2/BCL-xL/BCL-w inhibition → apoptosis of senescent cells is well-established and reproducible across many independent labs [1][2][3][4][6][14]. Cell-type specificity (kills senescent HUVECs/IMR90 fibroblasts, **not** preadipocytes) confirmed in [2][3]. Accurately represented.
- **Animal skin data (B-grade, verified, correctly caveated):** Yosef epidermal clearance + hair-follicle stem-cell proliferation used **IP ABT-737 75 mg/kg** in a transgenic mouse [1]. Takaya "human skin" was **grafted tissue on mice with IP navitoclax 50 mg/kg/day** [8] — the dossier correctly flags this is NOT topical and is the most-misrepresented study. Shvedova topical study is **mouse + DMSO, n=5** [5] — numbers (5 µM, p16/p21 ↓, 33%/0% and 80%/56.3% wound healing, F4/80 macrophage infiltration, no serum-platelet change) extracted directly and accurately.
- **Human data reality (verified):** all human data are **oral navitoclax oncology trials** whose dominant finding is **dose-limiting thrombocytopenia** [16][17]; navitoclax is **unapproved** [11][12]. **No human topical study of any kind exists** — confirmed by multiple searches. The dossier does not borrow any oncology benefit as a skin benefit; it uses the human record only as a safety caution, which is correct.
- **Counter-evidence included (good hygiene):** Sharma 2020 bone-loss harm [15] is real and correctly used to puncture "senolytic = uniformly good."

### What re-verification confirmed (second pass, 2026-06-19)
Every load-bearing number was independently re-traced to the primary source and matches the dossier:
- **Shvedova 2024 [5]** (full PMC text): C57BL/6, 24-mo aged vs 2-mo young; **n = 5–8/timepoint**; **5 µM ABT-263 in DMSO, 5 consecutive days**; wound healing **33% vs 0% by day 18** and **80% vs 56.3% by day 24**; **F4/80+ macrophage** infiltration in papillary + reticular dermis; **no significant serum-platelet change**; NIA-funded (Boston University), **no conflicts declared.** All correct. *(One detail the dossier omits and the source actually states: ABT-263-treated aged mice also showed **elevated neutrophils** vs DMSO — a second local inflammatory/immune signal alongside the macrophages, reinforcing the "irritation/inflammation even topically" point, not contradicting anything.)*
- **Takaya 2023 [8]:** grafted aged **human** skin (donors **78–91 yr**) on nude mice; drug **IP, 50 mg/kg/day — not topical**; ~60% ↓ senescent stain, ~30% ↑ collagen. Correct; the "rejuvenates HUMAN skin" framing is appropriately defused.
- **Zhu 2016 [2] / Zhu 2017 [3]:** senolytic in HUVECs/IMR90/WI-38/MEFs, **not** preadipocytes; BCL-2/BCL-xL/BCL-w upregulation drives the specificity. Correct.
- **Yosef 2016 [1]:** ABT-737 (and BCL-W/BCL-XL siRNA) in K5-rtTA/tet-p14ARF transgenic mice cleared epidermal senescent cells and ↑ hair-follicle stem-cell proliferation; delivery **IP, not topical.** Correct.
- **Sharma 2020 [15]:** 24-mo aged mice, navitoclax **50 mg/kg/day × 2 wks**; **−60.1% (F) / −45.6% (M)** trabecular bone-volume-fraction; impaired osteoblast mineralization **−88% (F) / −83% (M)**. Correct — note these mineralization figures are stated in the verdict but not in §4; both are real and on-target-harm, not typos.
- **Human oncology toxicity [16][17]:** Roberts 2012 — thrombocytopenia (via BCL-xL) = dose-limiting toxicity, confirmed. Phase 2a — **grade 3/4 thrombocytopenia 38.5%, neutropenia 30.8%**, with a **7-day, 150-mg lead-in** before 250 mg, confirmed verbatim.
- **Regulatory status [11][12]:** navitoclax remains **investigational / not FDA-approved** as of 2025 (TRANSFORM-1 Phase 3 read out but no approval); the other three compounds are research reagents with no INCI. Confirmed.

### Load-bearing caveats
1. **Not a cosmetic ingredient — full stop.** No INCI, no cosmetic regulatory status; navitoclax is an unapproved investigational drug, the others are reagents. This is the decisive, verified fact.
2. **All "skin rejuvenation" data are animal/grafted-tissue with injected or DMSO-delivered drug.** Human topical cosmetic evidence = nil.
3. **Real human toxicity (thrombocytopenia) + animal off-target harm (bone loss).** Safety is not benign.
4. **Delivery depends on DMSO** in the only topical study — not a cosmetically realistic vehicle.

### Bottom line
**Grade: D for topical-cosmetic use (unproven topically / hype), A–B for the underlying senolytic mechanism (pharmacology, not cosmetic).** The dossier does **not** overstate anything — if anything it correctly downgrades a class that press/longevity coverage hypes, and it never borrows an animal/injected/oncology benefit and re-sells it as topical-cosmetic proof. Across two independent adversarial passes, **no claim required softening and no citation required correction**; all studies are real and all headline numbers trace to their primary sources. The only additions on re-audit were clarifying ones (an A–D grade per the verification rubric; the explicit "no human topical cosmetic evidence" statement; the elevated-neutrophil detail from Shvedova that further supports the existing irritation caveat). For a **cosmetic brand** the verdict is an unambiguous, well-evidenced **SKIP** — keep as a science benchmark/reference, never as a formulation ingredient.
