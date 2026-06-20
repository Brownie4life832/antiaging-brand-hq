# Master Ingredient Index — Anti-Aging / Skin-Longevity Taxonomy

**Compiled:** 2026-06-19 · **Status:** working master list (open to edits)

This is the consolidated, de-duplicated master index for the Kintsugi anti-aging / skin-longevity
ingredient taxonomy. It was built by merging **14 raw class lists**. An ingredient that appeared in
several class lists is kept **once**, assigned a single **primaryClass**, and its cross-listing noted
in the row (see the "Also listed in" column).

**This file is the input list for the per-ingredient deep-research run.** It is intentionally broad
(it includes fringe, experimental, and pharma-adjacent actives for completeness). The list is **open
to edits, additions, re-tiering, and pruning before that run** — nothing here is final.

---

## Count summary

- **Total unique ingredients:** 232
- **By relevance tier:**
  - Core: 55
  - Supporting: 96
  - Fringe: 81
- **Dossiers written:** **271 of 272** taxonomy rows now have a dossier (flagged `Dossier? = ✅`) — i.e. **the deep-research run is effectively complete**. The lone remaining `❌` is `selenium` (no dossier yet). Two rows are cross-listed and share one dossier each (`nad-niacinamide-longevity`, `senolytics-os01-peptide`); on disk this is **269 unique dossier files**. For the consolidated, strongest-evidence-first synthesis of every dossier (evidence grade, top tier, topical viability, verdict), see **[`_EVIDENCE-MATRIX.md`](_EVIDENCE-MATRIX.md)**; for the pivotal papers by hallmark, see **[`../science/landmark-papers.md`](../science/landmark-papers.md)**.

> Note on counting: where a class list bundled several near-identical molecules under one umbrella row
> (e.g. "Acetyl Tetrapeptide / Oligopeptide multi-peptide complexes"), that umbrella is counted as one
> entry. Salt/ester families that the source lists already split out (e.g. the vitamin C derivatives,
> the named ceramides) are kept split.

---

## Hallmarks of skin aging (framework used)

Every ingredient is mapped to one or more of the following eleven hallmarks. This is the controlled
vocabulary used throughout the table.

| Hallmark | Short definition |
|---|---|
| **collagen/ECM loss** | Decline and disorganization of dermal collagen, elastin, and the extracellular matrix → wrinkles, laxity, thinning. |
| **barrier decline** | Weakening of the stratum-corneum lipid barrier and corneocyte cohesion → sensitivity, roughness. |
| **oxidative stress** | Accumulation of reactive oxygen/nitrogen species (UV, pollution, metabolism) that damage lipids, proteins, and DNA. |
| **glycation/AGEs** | Sugar-driven cross-linking of collagen/elastin into advanced glycation end-products → stiffness, yellowing. |
| **cellular senescence** | Build-up of "zombie" cells that stop dividing but secrete a pro-aging SASP signature. |
| **mitochondrial decline** | Falling ATP output, mitophagy, and NAD+ with age → low cellular energy and dullness. |
| **inflammaging** | Chronic low-grade inflammation that accelerates matrix breakdown and senescence. |
| **photoaging** | UV-driven aging: wrinkles, mottled pigment, elastosis, DNA damage. |
| **pigmentation/tone** | Uneven melanin, dark spots, sallowness, loss of radiance. |
| **microbiome** | Health/diversity of the skin's microbial ecosystem and its barrier/immune crosstalk. |
| **hydration/water-loss** | NMF and water-binding capacity vs. trans-epidermal water loss (TEWL). |

---

## How to read the table

- **Ingredient** — consolidated common name.
- **INCI** — representative INCI / regulatory name (drugs noted as such).
- **Hallmark(s)** — targeted hallmarks from the framework above.
- **Relevance** — core / supporting / fringe (longevity relevance for the brand).
- **Dossier?** — ✅ a dossier already exists (by meaning), ❌ not yet.
- **Also listed in** — other class lists this ingredient appeared in (cross-listing note); blank if only one.
- **Slug** — kebab-case filename for the future dossier.

---

## 1. Retinoids & retinoid alternatives

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Retinol / Retinaldehyde / Encapsulated retinol (family) | Retinol; Retinal; encapsulated systems | collagen/ECM loss · photoaging · pigmentation/tone · cellular senescence · barrier decline · microbiome | core | ✅ | — | retinoids |
| Tretinoin (all-trans retinoic acid) | Tretinoin (drug) | collagen/ECM loss · photoaging · pigmentation/tone · cellular senescence | core | ✅ (context within retinoids) | — | tretinoin |
| Tazarotene | Tazarotene (drug) | collagen/ECM loss · photoaging · pigmentation/tone | core | ✅ | — | tazarotene |
| Adapalene | Adapalene (drug) | collagen/ECM loss · photoaging · inflammaging · pigmentation/tone | supporting | ✅ | — | adapalene |
| Trifarotene | Trifarotene (drug) | collagen/ECM loss · photoaging | fringe | ✅ | — | trifarotene |
| Alitretinoin (9-cis RA) | Alitretinoin (drug) | collagen/ECM loss · inflammaging | fringe | ✅ | — | alitretinoin |
| Isotretinoin (13-cis RA) | Isotretinoin (drug) | photoaging · inflammaging | fringe | ✅ | — | isotretinoin |
| Hydroxypinacolone Retinoate (HPR) | Hydroxypinacolone Retinoate | collagen/ECM loss · photoaging · pigmentation/tone · barrier decline | core | ✅ | own active-molecule dossier; trade blend in granactive-retinoid | hydroxypinacolone-retinoate |
| Granactive Retinoid | Dimethyl Isosorbide (and) HPR | collagen/ECM loss · photoaging · pigmentation/tone | core | ✅ | — | granactive-retinoid |
| Retinyl Retinoate | Retinyl Retinoate | collagen/ECM loss · photoaging · pigmentation/tone · barrier decline | core | ✅ | — | retinyl-retinoate |
| Retinyl Palmitate | Retinyl Palmitate | photoaging · oxidative stress · barrier decline | supporting | ✅ | — | retinyl-palmitate |
| Retinyl Propionate | Retinyl Propionate | photoaging · collagen/ECM loss · barrier decline | supporting | ✅ | — | retinyl-propionate |
| Retinyl Acetate | Retinyl Acetate | photoaging · oxidative stress (weak/borrowed) | supporting | ✅ | skip-as-hero / minor supporting only — no stand-alone topical RCT; weakest ester; EU-capped | retinyl-acetate |
| Retinyl Linoleate | Retinyl Linoleate | barrier decline · photoaging · hydration/water-loss | supporting | ✅ | — | retinyl-linoleate |
| Minor retinyl esters (Lactate, Oleate, Stearate, Butyrate, Hexanoate/Caprylate/Heptanoate, Sunflowerseedate) | various Retinyl esters | photoaging · barrier decline · hydration/water-loss | fringe | ✅ | — | minor-retinyl-esters |
| Retinyl Ascorbate | Retinyl Ascorbate | oxidative stress · photoaging · pigmentation/tone · collagen/ECM loss | fringe | ✅ | vitamin C–retinoid conjugate | retinyl-ascorbate |
| Beta-Carotene (provitamin A) | Beta-Carotene | oxidative stress · photoaging | fringe | ✅ | Antioxidants; Botanicals | beta-carotene |
| Bakuchiol | Bakuchiol (Psoralea Corylifolia Seed Ext.) | collagen/ECM loss · photoaging · pigmentation/tone · oxidative stress · inflammaging · barrier decline | core | ✅ | Botanicals; Sunscreen/photoprotection | bakuchiol |
| Bidens Pilosa extract (Bio-Retinol) | Bidens Pilosa Extract | collagen/ECM loss · pigmentation/tone · photoaging | supporting | ✅ | — | bidens-pilosa-bio-retinol |
| Revinage (Bidens + plant oils) | Bidens Pilosa Ext. (+ plant oils) | collagen/ECM loss · photoaging · barrier decline · pigmentation/tone | supporting | ✅ | — | revinage |
| Moth Bean extract | Vigna Aconitifolia Seed Extract | collagen/ECM loss · hydration/water-loss · photoaging | supporting | ✅ | — | moth-bean-extract |
| Rambutan extract | Nephelium Lappaceum Peel/Leaf/Seed Extract | oxidative stress · collagen/ECM loss · pigmentation/tone · cellular senescence · hydration/water-loss | supporting (conditional) | ✅ | — | rambutan-extract |
| Rosehip seed oil | Rosa Canina / Rubiginosa Seed Oil | barrier decline · hydration/water-loss · oxidative stress (photoaging/pigment weak/borrowed) | supporting | ✅ | Botanicals | rosehip-seed-oil |
| Sea buckthorn oil | Hippophae Rhamnoides Oil | oxidative stress · barrier decline · photoaging · hydration/water-loss | supporting | ✅ | Botanicals (listed core there) | sea-buckthorn-oil |
| Carrot seed extract / oil | Daucus Carota Sativa Seed Oil/Ext. | oxidative stress · photoaging · pigmentation/tone | fringe | ✅ | Botanicals | carrot-seed-extract |
| Buddleja extract | Buddleja Davidii Extract | oxidative stress · photoaging · inflammaging | fringe | ✅ | — | buddleja-extract |

## 2. Peptides — signal, carrier, enzyme-inhibitor, neuro-inhibitor

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Signal/matrikine peptides (Matrixyl family: Pal-Pentapeptide-4, Matrixyl 3000, Synthe'6, Syn-Coll, etc.) | Palmitoyl Pentapeptide-4; Palmitoyl Tripeptide-1; Palmitoyl Tetrapeptide-7; Palmitoyl Tripeptide-38; Palmitoyl Tripeptide-5 | collagen/ECM loss · inflammaging · hydration/water-loss · photoaging | core | ✅ | Experimental/frontier | peptides |
| Copper Tripeptide-1 (GHK-Cu) & Tripeptide-1 (GHK) | Copper Tripeptide-1; Tripeptide-1 | collagen/ECM loss · oxidative stress · inflammaging · photoaging · barrier decline | core | ✅ | Senotherapeutics; Growth factors; Anti-glycation; Experimental | copper-peptides-ghk-cu |
| OS-01 / Peptide 14 (senotherapeutic) | Decapeptide-52 / sh-Decapeptide-7 (proprietary) | cellular senescence · inflammaging · barrier decline · collagen/ECM loss · photoaging | core | ✅ | Senotherapeutics; NAD/AMPK; Experimental | senolytics-os01-peptide |
| Carnosine (& N-Acetyl Carnosine) | Carnosine; Acetyl Carnosine | glycation/AGEs · oxidative stress · collagen/ECM loss · cellular senescence | core | ✅ | Antioxidants; NAD/sirtuin; Anti-glycation; Sunscreen; Experimental | carnosine |
| Hexapeptide-11 (Peptamide-6) | Hexapeptide-11 | cellular senescence · oxidative stress · collagen/ECM loss | core | ✅ | — | hexapeptide-11 |
| Trifluoroacetyl Tripeptide-2 (Progeline) | Trifluoroacetyl Tripeptide-2 | cellular senescence · collagen/ECM loss | core | ✅ | NAD/sirtuin | progeline-tfa-tripeptide-2 |
| Argireline-class neuro-peptides (Acetyl Hexapeptide-8/-3, SNAP-8, Acetyl Hexapeptide-30) | Acetyl Hexapeptide-8; Acetyl Octapeptide-3 | photoaging · collagen/ECM loss | core | ✅ | — | argireline-neuropeptides |
| Other neuro-inhibitor peptides (Leuphasyl, Syn-Ake, Vialox, Tripeptide-3) | Pentapeptide-18; Dipeptide Diaminobutyroyl Benzylamide Diacetate; Pentapeptide-3 | photoaging · pigmentation/tone | supporting | ✅ | — | neuro-inhibitor-peptides |
| Firming/density matrikines (Acetyl Tetrapeptide-9/-11/-2/-3, Dermican, Syniorage, Decapeptide-12-firming, Tripeptide-10 Citrulline, Tetrapeptide-21, Hexapeptide-9/-12) | various Acetyl Tetrapeptides; Tripeptide-10 Citrulline; Tetrapeptide-21 | collagen/ECM loss · barrier decline · hydration/water-loss | supporting | ✅ | — | firming-matrikine-peptides |
| Soothing / anti-redness peptides (Acetyl Tetrapeptide-15, Acetyl Tetrapeptide-40, Acetyl Dipeptide-1 Cetyl Ester, Hexapeptide-14, Palmitoyl Tripeptide-8) | Acetyl Tetrapeptide-15; Acetyl Dipeptide-1 Cetyl Ester | inflammaging · barrier decline · pigmentation/tone | supporting | ✅ | Anti-glycation | soothing-peptides |
| Hydration/aquaporin peptides (Acetyl Hexapeptide-20/-37 Diffuporine, Acetyl Heptapeptide-9) | Acetyl Hexapeptide-37; Acetyl Hexapeptide-20 | hydration/water-loss · barrier decline | conditional | ✅ | — | aquaporin-hydration-peptides |
| Brightening peptides (Decapeptide-12/Lumixyl, Nonapeptide-1, Oligopeptide-68/-34/-51, Tetrapeptide-30, Acetyl Glycyl Beta-Alanine, PKEK, Pentapeptide-18) | Decapeptide-12; Nonapeptide-1; Oligopeptide-68; Tetrapeptide-30 | pigmentation/tone · photoaging · inflammaging | supporting | ✅ | — | brightening-peptides |
| Microbiome/defensin peptides (Acetyl Dipeptide-3 Aminohexanoate Bodyfensine, Acetyl Heptapeptide-4 Fensebiome) | Acetyl Dipeptide-3 Aminohexanoate; Acetyl Heptapeptide-4 | microbiome · barrier decline · inflammaging | supporting | ✅ | — | microbiome-defensin-peptides |
| Juveleven (Acetyl Hexapeptide-51 Amide) | Acetyl Hexapeptide-51 Amide | cellular senescence · oxidative stress | supporting | ✅ | Senotherapeutics; DNA-repair enzymes; Sunscreen | juveleven-hexapeptide-51 |
| Eyeseryl / eye-contour peptides (Acetyl Tetrapeptide-5, Dipeptide-2, Eyeliss complex) | Acetyl Tetrapeptide-5; Dipeptide-2 | glycation/AGEs · inflammaging · hydration/water-loss · collagen/ECM loss | supporting | ✅ | — | eye-contour-peptides |
| DEJ / junction peptides (Syn-Hycan, Palmitoyl Tetrapeptide-10, Acetyl Octapeptide-17 Amide/mini-EGF) | Palmitoyl Dipeptide-5 Diaminobutyroyl Hydroxythreonine; Palmitoyl Tetrapeptide-10 | collagen/ECM loss · barrier decline | supporting | ✅ | — | dej-junction-peptides |
| Nrf2 / antioxidant peptides (Acetyl sh-Heptapeptide-1 P7, Acetyl Tripeptide-30 Citrulline) | Acetyl sh-Heptapeptide-1; Acetyl Tripeptide-30 Citrulline | oxidative stress · photoaging · collagen/ECM loss | supporting | ✅ | — | nrf2-antioxidant-peptides |
| Thymosin-β4 fragment peptide (Acetyl sh-Pentapeptide-1) | Acetyl sh-Pentapeptide-1 | collagen/ECM loss · inflammaging | supporting | ✅ | Growth factors (TB4) | thymosin-b4-peptide |
| Plant/protein peptides (Soybean, Silk/Sericin, Rice, Hydrolyzed Collagen) | Glycine Soja Peptide; Hydrolyzed Silk; Oryza Sativa Peptide; Hydrolyzed Collagen | oxidative stress · photoaging · collagen/ECM loss · hydration/water-loss · pigmentation/tone | supporting | ✅ | Anti-glycation (collagen tripeptides) | plant-protein-peptides |
| Volumizing/adipo peptides (Adifyline, Silusyne) | Acetyl Hexapeptide-38; Acetyl Hexapeptide-39 | collagen/ECM loss | fringe | ✅ | — | adipo-volumizing-peptides |
| Misc/long-tail biomimetic peptides (Acetyl Cyclohexapeptide-34, Tetrapeptide-26, Heptapeptide-15 Palmitate, Tripeptide-29/-32/-2, Acetyl Tetrapeptide-17/-22, Pentapeptide-4, Hexapeptide-48 HCl, Elaidoyl Tripeptide-37, Tripeptide-38) | various | collagen/ECM loss · inflammaging · oxidative stress | fringe | ✅ | — | misc-biomimetic-peptides |
| K-beauty recombinant multi-peptide blends (Tripeptide-46/Hexapeptide-40/Oligopeptide-96 etc., sh-Polypeptide-121, Oligopeptide-29) | Tripeptide-46; sh-Polypeptide-121; Oligopeptide-29 | collagen/ECM loss · barrier decline | fringe | ✅ | Growth factors | kbeauty-multipeptide-blends |
| Spider-silk biomimetic peptides | sr-Polypeptide-3 / Tetrapeptide-39 blends | collagen/ECM loss · barrier decline | fringe | ✅ | — | spider-silk-peptides |
| Mitochondrial-targeted peptides (SS-31/Elamipretide, Humanin/MOTS-c) | Elamipretide (investigational) | mitochondrial decline · oxidative stress · cellular senescence | fringe | ✅ | Autophagy/mitochondrial | mitochondrial-peptides-ss31 |
| FOXO4-DRI (senolytic peptide, experimental) | research-stage | cellular senescence | fringe | ✅ | — | foxo4-dri-peptide |
| Bioactive Peptide SA1-III (KP1) | proprietary | collagen/ECM loss | fringe | ✅ | — | peptide-sa1-iii-kp1 |

## 3. Antioxidants (vitamin C/E, ferulic, CoQ10, idebenone, glutathione, etc.)

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Vitamin C (L-ascorbic acid + derivatives family) | Ascorbic Acid; SAP; MAP; Ascorbyl Glucoside; 3-O-Ethyl Ascorbic Acid; THD Ascorbate; ATIP; etc. | oxidative stress · collagen/ECM loss · photoaging · pigmentation/tone · glycation/AGEs | core | ✅ | Sunscreen/photoprotection | vitamin-c |
| Vitamin E / Tocopherols (Tocopherol, Tocopheryl Acetate, Tocotrienols, etc.) | Tocopherol; Tocopheryl Acetate; Tocotrienols | oxidative stress · barrier decline · photoaging · hydration/water-loss | core | ✅ | Barrier lipids; Sunscreen | vitamin-e-tocopherols |
| Ferulic Acid (+ Ethyl Ferulate) | Ferulic Acid | oxidative stress · photoaging · collagen/ECM loss · glycation/AGEs | core | ✅ | Botanicals; Anti-glycation; Sunscreen | ferulic-acid |
| Coenzyme Q10 / Ubiquinone (+ Ubiquinol) | Ubiquinone; Ubiquinol | mitochondrial decline · oxidative stress · photoaging · collagen/ECM loss | core | ✅ | NAD/sirtuin; Autophagy/mitochondrial; Experimental | coenzyme-q10 |
| Idebenone | Idebenone / Hydroxydecyl Ubiquinone | oxidative stress · mitochondrial decline · photoaging · collagen/ECM loss · glycation/AGEs | core | ✅ | NAD/sirtuin; Autophagy/mitochondrial; Anti-glycation; Experimental | idebenone |
| Alpha-Lipoic Acid (+ DHLA) | Thioctic Acid; Dihydrolipoic Acid | oxidative stress · mitochondrial decline · photoaging · glycation/AGEs · inflammaging | core | ✅ | NAD/sirtuin; Autophagy/mitochondrial; Anti-glycation | alpha-lipoic-acid |
| Glutathione (+ GSSG, S-Acetyl, NAC, cysteine forms) | Glutathione; Acetyl Cysteine | oxidative stress · pigmentation/tone · inflammaging · cellular senescence · glycation/AGEs | core | ✅ | Anti-glycation; Experimental | glutathione |
| Ergothioneine | Ergothioneine | oxidative stress · mitochondrial decline · photoaging · inflammaging · cellular senescence · pigmentation/tone | core | ✅ | Autophagy/mitochondrial; Hydration; Anti-glycation; Sunscreen; Experimental | ergothioneine |
| Astaxanthin | Astaxanthin / Haematococcus Pluvialis Ext. | oxidative stress · photoaging · inflammaging · collagen/ECM loss · hydration/water-loss | core | ✅ | Botanicals; Anti-glycation; Sunscreen | astaxanthin |
| Niacinamide | Niacinamide | mitochondrial decline · barrier decline · oxidative stress · pigmentation/tone · inflammaging · hydration/water-loss · glycation/AGEs · photoaging | core | ✅ | NAD/sirtuin; Autophagy; Anti-glycation; Sunscreen; Experimental | niacinamide |
| Phloretin | Phloretin | oxidative stress · pigmentation/tone · photoaging | supporting | ✅ | Botanicals | phloretin |
| Hydroxytyrosol | Hydroxytyrosol | oxidative stress · photoaging · inflammaging · mitochondrial decline | supporting | ✅ | Botanicals | hydroxytyrosol |
| Tetrahydrocurcumin | Tetrahydrocurcumin | oxidative stress · inflammaging · pigmentation/tone · glycation/AGEs | supporting | ✅ | NAD/sirtuin; Botanicals; Sunscreen | tetrahydrocurcumin |
| Acetyl Zingerone | Acetyl Zingerone | oxidative stress · photoaging · pigmentation/tone · collagen/ECM loss | supporting | ✅ | — | acetyl-zingerone |
| Hexylresorcinol | Hexylresorcinol | oxidative stress · pigmentation/tone | supporting | ✅ | — | hexylresorcinol |
| MitoQ (Mitoquinol mesylate) | Mitoquinol Mesylate | mitochondrial decline · oxidative stress · cellular senescence | supporting | ✅ | Autophagy/mitochondrial; Experimental | mitoq |
| PQQ (Pyrroloquinoline Quinone) | PQQ Disodium Salt | mitochondrial decline · oxidative stress · cellular senescence | supporting | ✅ | NAD/sirtuin; Autophagy/mitochondrial | pqq |
| Antioxidant enzymes (SOD, Catalase, Glutathione Peroxidase, EUK-134) | Superoxide Dismutase; Catalase; EUK-134 | oxidative stress · inflammaging · photoaging | supporting | ✅ | — | antioxidant-enzymes |
| Lipochroman / Dimethylmethoxy Chromanol | Dimethylmethoxy Chromanol | oxidative stress · glycation/AGEs · photoaging · collagen/ECM loss | supporting | ✅ | — | lipochroman |
| Melatonin | Melatonin | oxidative stress · photoaging · mitochondrial decline · barrier decline · cellular senescence | supporting | ✅ | Autophagy/mitochondrial | melatonin |
| Carnosine relatives (Carcinine/Alistin, Anserine, Homocarnosine) | Carcinine HCl; Anserine | glycation/AGEs · oxidative stress | supporting | ✅ | Anti-glycation; Botanicals; Experimental | carcinine-alistin |
| Spermidine | Spermidine | cellular senescence · oxidative stress · mitochondrial decline · collagen/ECM loss · hydration/water-loss · inflammaging | supporting | ✅ | NAD/sirtuin; Senotherapeutics; Autophagy; Anti-glycation; Botanicals; Experimental | spermidine |
| NMN (Nicotinamide Mononucleotide) | Nicotinamide Mononucleotide | mitochondrial decline · cellular senescence · oxidative stress · collagen/ECM loss · photoaging · hydration/water-loss | supporting | ✅ (within NAD longevity) | Antioxidants; NAD/sirtuin; Autophagy; Experimental | nad-niacinamide-longevity |
| NR (Nicotinamide Riboside) | Nicotinamide Riboside Chloride | mitochondrial decline · cellular senescence · oxidative stress · barrier decline · photoaging | supporting | ✅ (within NAD longevity) | NAD/sirtuin; Autophagy; Experimental | nicotinamide-riboside |
| Taurine (+ Hypotaurine) | Taurine; Hypotaurine | oxidative stress · hydration/water-loss · inflammaging · cellular senescence | supporting | ✅ | Anti-glycation; Experimental | taurine |
| Creatine | Creatine | mitochondrial decline · oxidative stress · collagen/ECM loss | supporting | ✅ | NAD/sirtuin; Autophagy/mitochondrial | creatine |
| Carotenoids (Beta-Carotene, Lycopene, Lutein, Zeaxanthin, Fucoxanthin) | Beta-Carotene; Lycopene; Lutein; Zeaxanthin; Fucoxanthin | oxidative stress · photoaging · pigmentation/tone | supporting | ✅ | Retinoids; Botanicals; Sunscreen | dietary-carotenoids |
| Potassium Ascorbyl Tocopheryl Phosphate (EPC) | Potassium Ascorbyl Tocopheryl Phosphate | oxidative stress · barrier decline · photoaging · pigmentation/tone | supporting | ✅ | Antioxidants (vitamin C/E) | ascorbyl-tocopheryl-phosphate |
| Formula-stabilizer antioxidants (BHT, BHA, Propyl Gallate, TBHQ, Disodium EDTA) | BHT; BHA; Propyl Gallate; t-Butyl Hydroquinone; Disodium EDTA | oxidative stress | fringe | ✅ | — | formula-stabilizer-antioxidants |
| Endogenous niche antioxidants (Bilirubin/Biliverdin, Uric Acid) | Bilirubin; (urate) | oxidative stress | fringe | ✅ | — | endogenous-antioxidants |
| Caffeic & gallic phenolics (CAPE/Caffeic Acid, Gallic Acid) | Caffeic Acid; Gallic Acid | oxidative stress · pigmentation/tone · inflammaging | fringe | ✅ | Autophagy; Botanicals; Anti-glycation; Sunscreen | caffeic-gallic-phenolics |
| Cannabidiol (CBD) | Cannabidiol | oxidative stress · inflammaging · barrier decline | fringe | ✅ | Experimental | cannabidiol |
| Selenium / Sodium Selenite / Selenomethionine | Sodium Selenite | oxidative stress · photoaging | fringe | ❌ | — | selenium |
| Edaravone | Edaravone | oxidative stress · pigmentation/tone | fringe | ✅ | — | edaravone |
| Ebselen | Ebselen | oxidative stress · inflammaging | fringe | ✅ | — | ebselen |

## 4. NAD+ / sirtuin / AMPK / cellular-energy actives

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| NAD+ longevity complex (Niacinamide as NAD precursor + NMN/NR/NAD context) | Niacinamide; NMN; Nicotinamide Riboside; NAD | mitochondrial decline · cellular senescence · oxidative stress · barrier decline · pigmentation/tone | core | ✅ | Antioxidants; Autophagy; Experimental | nad-niacinamide-longevity |
| NADH (reduced NAD) | NADH | mitochondrial decline · oxidative stress | supporting | ✅ | — | nadh |
| Niacin (Nicotinic Acid) + esters (Myristyl Nicotinate, Tocopheryl Nicotinate) | Niacin; Myristyl Nicotinate; Tocopheryl Nicotinate | barrier decline · photoaging · oxidative stress · collagen/ECM loss · hydration/water-loss | supporting | ✅ | Antioxidants | niacin-esters |
| Next-gen NAD precursors (NaMN, NAR, NRH, NaMN salts) | Nicotinic Acid Mononucleotide; Nicotinic Acid Riboside | mitochondrial decline · oxidative stress · barrier decline | fringe | ✅ | — | nextgen-nad-precursors |
| Resveratrol | Resveratrol | oxidative stress · collagen/ECM loss · photoaging · cellular senescence · pigmentation/tone · inflammaging · glycation/AGEs | core | ✅ | Senotherapeutics; Autophagy; Botanicals; Anti-glycation; Sunscreen; Experimental | polyphenols-resveratrol |
| Resveratrol analogs (Pterostilbene, Oxyresveratrol, Acetyl/Hydroxy-resveratrol, Resveratryl Triacetate, Piceatannol, Rhapontigenin) | Pterostilbene; Oxyresveratrol; Resveratryl Triacetate | oxidative stress · cellular senescence · collagen/ECM loss · photoaging · pigmentation/tone · glycation/AGEs | supporting | ✅ | Senotherapeutics; Autophagy; Botanicals; Anti-glycation | resveratrol-analogs |
| Fisetin | Fisetin | cellular senescence · inflammaging · oxidative stress · photoaging | core | ✅ | Senotherapeutics; Autophagy; Botanicals; Experimental | fisetin |
| Quercetin | Quercetin | oxidative stress · cellular senescence · inflammaging · photoaging · mitochondrial decline · glycation/AGEs | core | ✅ | Senotherapeutics; Autophagy; Botanicals; Anti-glycation; Experimental | quercetin |
| Apigenin (CD38 inhibitor) | Apigenin | oxidative stress · inflammaging · mitochondrial decline · cellular senescence · collagen/ECM loss | supporting | ✅ | Senotherapeutics; Botanicals; Anti-glycation; Experimental | apigenin |
| Enoxolone (18β-Glycyrrhetinic Acid, CD38 inhibitor) | Glycyrrhetinic Acid / Enoxolone | inflammaging · oxidative stress · barrier decline · mitochondrial decline | supporting | ✅ | Botanicals (licorice) | enoxolone |
| Kaempferol | Kaempferol | oxidative stress · inflammaging · photoaging · cellular senescence · mitochondrial decline | supporting | ✅ | Senotherapeutics; Autophagy; Botanicals; Anti-glycation | kaempferol |
| Honokiol / Magnolol (SIRT3) | Honokiol; Magnolol | mitochondrial decline · oxidative stress · inflammaging · barrier decline | supporting | ✅ | — | honokiol-magnolol |
| EGCG / Green tea polyphenols | Epigallocatechin Gallate; Camellia Sinensis Leaf Ext. | oxidative stress · photoaging · inflammaging · collagen/ECM loss · cellular senescence · mitochondrial decline · glycation/AGEs | supporting | ✅ | Senotherapeutics; Autophagy; Botanicals; Anti-glycation; Sunscreen | green-tea-egcg |
| Genistein / soy isoflavones (+ Daidzein, Equol) | Genistein; Glycine Soja Extract; Equol; Daidzein | collagen/ECM loss · oxidative stress · photoaging · pigmentation/tone · cellular senescence | supporting | ✅ | Botanicals; Experimental | soy-isoflavones |
| Berberine | Berberine | inflammaging · oxidative stress · mitochondrial decline · cellular senescence · glycation/AGEs | supporting | ✅ | Senotherapeutics; Autophagy | berberine |
| Curcumin | Curcumin / Curcuma Longa Root Ext. | inflammaging · oxidative stress · pigmentation/tone · glycation/AGEs · cellular senescence | supporting | ✅ | Senotherapeutics; Botanicals; Anti-glycation | curcumin |
| Metformin (topical) | Metformin HCl | cellular senescence · inflammaging · collagen/ECM loss · photoaging · mitochondrial decline · glycation/AGEs · oxidative stress | supporting | ✅ | Autophagy; Experimental | topical-metformin |
| Yeast/biotech sirtuin-inducing ferments (Kluyveromyces, SIRT6-activating peptides, Surfactin) | Kluyveromyces Extract; Surfactin | cellular senescence · collagen/ECM loss · oxidative stress · microbiome · photoaging · inflammaging | supporting | ✅ | Experimental | sirtuin-ferments-peptides |
| Grape cane / vine-shoot extract (resveratrol + viniferins) | Vitis Vinifera Cane Extract | oxidative stress · pigmentation/tone · collagen/ECM loss · photoaging | supporting | ✅ | — | grape-cane-extract |
| Black ginger methoxyflavones (Kaempferia parviflora) | Kaempferia Parviflora Root Extract | oxidative stress · cellular senescence · collagen/ECM loss | fringe | ✅ | — | black-ginger-methoxyflavones |
| STAC-class polyphenols (Butein, Myricetin, Delphinidin, Cichoric Acid) | Butein; Myricetin; Chicoric Acid | oxidative stress · collagen/ECM loss · pigmentation/tone · cellular senescence | fringe | ✅ | — | stac-polyphenols |
| Guggulsterone (Commiphora mukul) | Commiphora Mukul Resin Extract | inflammaging · oxidative stress · mitochondrial decline | fringe | ✅ | — | guggulsterone |
| AICAR (Acadesine) | AICA Ribonucleotide | photoaging · mitochondrial decline · oxidative stress | fringe | ✅ | — | aicar-acadesine |
| Synthetic STACs (SRT1720, SRT2104, SRT3025) | investigational | cellular senescence · inflammaging · mitochondrial decline · collagen/ECM loss · oxidative stress | fringe | ✅ | Experimental | synthetic-stacs |
| Acetyl-L-Carnitine / L-Carnitine | Acetyl Carnitine; Carnitine | mitochondrial decline · oxidative stress · glycation/AGEs | supporting | ✅ | Autophagy/mitochondrial; Anti-glycation | acetyl-l-carnitine |

## 5. Senotherapeutics & senolytics

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Senolytics & OS-01 senotherapeutic peptide (class overview) | (see OS-01; Fisetin; Quercetin) | cellular senescence · inflammaging · oxidative stress · collagen/ECM loss | core | ✅ | Peptides; NAD/AMPK; Experimental | senolytics-os01-peptide |
| Eterwell Youth (alpine willowherb) | Epilobium Fleischeri Leaf/Stem Extract | cellular senescence · inflammaging · collagen/ECM loss · photoaging · microbiome | core | ✅ | — | eterwell-youth-epilobium |
| Celyscence (milk thistle senolytic) | Silybum Marianum Extract blend | cellular senescence · inflammaging · oxidative stress · collagen/ECM loss | core | ✅ | — | celyscence-milk-thistle |
| Altheostem (hollyhock stem cell) | Althaea Rosea Flower Cell Culture Extract | cellular senescence · collagen/ECM loss · inflammaging | core | ✅ | — | altheostem-hollyhock |
| SenoCellTec (alpine rose + apple stem cell) | Malus Domestica Fruit Cell Culture Ext. + Vitis Vinifera Fruit Cell Ext. + Rhododendron Ferrugineum Ext. | cellular senescence · collagen/ECM loss · oxidative stress · inflammaging | core | ✅ | Botanicals (alpine rose) | senocelltec |
| Alpine Rose extract (Rhododendron ferrugineum) | Rhododendron Ferrugineum Leaf Cell Culture Ext. | cellular senescence · oxidative stress · inflammaging · barrier decline | supporting | ✅ | Botanicals | alpine-rose-extract |
| Isatis tinctoria (Woad) extract | Isatis Tinctoria Leaf Extract | cellular senescence · inflammaging · oxidative stress | supporting | ✅ | — | isatis-tinctoria |
| Procyanidin C1 (PCC1) | Procyanidin C1 (grape seed fraction) | cellular senescence · oxidative stress · inflammaging · photoaging | supporting | ✅ | Experimental | procyanidin-c1 |
| Piperlongumine | Piperlongumine (Piper Longum Fruit Ext.) | cellular senescence · oxidative stress · inflammaging | supporting | ✅ | — | piperlongumine |
| Silymarin / Silibinin (milk thistle) | Silybum Marianum Extract; Silybin | oxidative stress · cellular senescence · inflammaging · photoaging · collagen/ECM loss · glycation/AGEs | supporting | ✅ | Botanicals; Anti-glycation; Sunscreen | silymarin-silibinin |
| Luteolin | Luteolin | cellular senescence · inflammaging · oxidative stress · photoaging · glycation/AGEs | supporting | ✅ | Botanicals; Anti-glycation | luteolin |
| Licochalcone A | Licochalcone A (Glycyrrhiza Inflata Ext.) | inflammaging · oxidative stress · cellular senescence · pigmentation/tone | supporting | ✅ | Botanicals | licochalcone-a |
| Ginsenoside Rg3 / Rh2 / Rb1 | Ginsenoside Rg3 (Panax Ginseng Ext.) | cellular senescence · inflammaging · oxidative stress · collagen/ECM loss | supporting | ✅ | Botanicals (ginseng) | ginsenosides |
| Fucoidan | Fucoidan (Fucus Vesiculosus Ext.) | cellular senescence · oxidative stress · collagen/ECM loss · hydration/water-loss · photoaging · inflammaging | fringe | ✅ | Autophagy/mitochondrial | fucoidan |
| Araliadiol | Araliadiol (Centella/Aralia) | cellular senescence · inflammaging · collagen/ECM loss | fringe | ✅ | — | araliadiol |
| Haritaki (Terminalia chebula) extract | Terminalia Chebula Fruit Extract | cellular senescence · inflammaging · oxidative stress · glycation/AGEs | fringe | ✅ | — | terminalia-chebula |
| Withaferin A (Ashwagandha) | Withania Somnifera Root Extract | cellular senescence · inflammaging · oxidative stress | fringe | ✅ | Botanicals (ashwagandha) | withaferin-a |
| Rapamycin (Sirolimus) / rapalogs | Sirolimus; Everolimus | cellular senescence · inflammaging · photoaging · collagen/ECM loss · mitochondrial decline | core | ✅ | Autophagy; Experimental | topical-rapamycin |
| Dasatinib (D+Q reference) | Dasatinib (drug) | cellular senescence · inflammaging | fringe | ✅ | Experimental | dasatinib |
| BCL-2/BCL-xL inhibitor senolytics (Navitoclax/ABT-263, ABT-737, A1331852, A1155463) | Navitoclax; A1331852 (research) | cellular senescence · inflammaging | fringe | ✅ | Experimental | bcl-inhibitor-senolytics |

## 6. Autophagy & mitochondrial-targeted actives

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Urolithin A (Mitopure) | Urolithin A | mitochondrial decline · collagen/ECM loss · photoaging · oxidative stress · barrier decline · hydration/water-loss · cellular senescence · inflammaging | core | ✅ | Senotherapeutics; Botanicals; Experimental | urolithin-a |
| Trehalose | Trehalose | mitochondrial decline · glycation/AGEs · hydration/water-loss · photoaging · oxidative stress · cellular senescence | core | ✅ | Hydration; Anti-glycation | trehalose |
| SkQ1 (Visomitin) | SkQ1 (plastoquinone-TPP) | mitochondrial decline · oxidative stress · inflammaging · photoaging | core | ✅ | — | skq1-visomitin |
| Mito-targeted research antioxidants (MitoTEMPO, MitoVitE, SkQR1) | MitoTEMPO; MitoVitE; SkQR1 | mitochondrial decline · oxidative stress | fringe | ✅ | — | mito-targeted-research-antioxidants |
| Urolithin B | Urolithin B | mitochondrial decline · oxidative stress | fringe | ✅ | — | urolithin-b |
| Ellagic acid | Ellagic Acid | oxidative stress · glycation/AGEs · pigmentation/tone · photoaging · mitochondrial decline · collagen/ECM loss | supporting | ✅ | Botanicals | ellagic-acid |
| Pomegranate extract / ellagitannins | Punica Granatum Fruit Extract | oxidative stress · photoaging · mitochondrial decline · glycation/AGEs · collagen/ECM loss · inflammaging | core | ✅ | Botanicals; Anti-glycation | pomegranate-extract |
| Tomatidine | Tomatidine | mitochondrial decline · oxidative stress · cellular senescence | fringe | ✅ | — | tomatidine |
| Camellia japonica flower extract + Hyperoside | Camellia Japonica Flower Extract; Hyperoside | mitochondrial decline · cellular senescence · oxidative stress · photoaging | supporting | ✅ | — | camellia-japonica-hyperoside |
| Caffeine | Caffeine | oxidative stress · mitochondrial decline · photoaging | fringe | ✅ | — | caffeine |
| Citrus bergamia (bergamot) extract | Citrus Aurantium Bergamia Fruit Extract | oxidative stress · mitochondrial decline · inflammaging | fringe | ✅ | — | bergamot-extract |
| Sulforaphane / broccoli sprout (Nrf2) | Sulforaphane; Brassica Oleracea Italica Sprout Ext. | oxidative stress · photoaging · inflammaging · mitochondrial decline | fringe | ✅ | Sunscreen | sulforaphane |
| Eugenol (spermidine co-active) | Eugenol | inflammaging · oxidative stress · mitochondrial decline | fringe | ✅ | — | eugenol |
| Spermine | Spermine | mitochondrial decline · barrier decline · oxidative stress | fringe | ✅ | — | spermine |
| Calcium Alpha-Ketoglutarate (Ca-AKG) | Calcium Alpha-Ketoglutarate | mitochondrial decline · hydration/water-loss · collagen/ECM loss · oxidative stress | supporting | ✅ | Experimental | calcium-akg |
| Galactomyces / Saccharomyces (Pitera) ferment filtrate | Galactomyces Ferment Filtrate; Saccharomyces Ferment Filtrate | oxidative stress · barrier decline · inflammaging · hydration/water-loss · microbiome · pigmentation/tone | supporting | ✅ | Hydration; Botanicals; Experimental (⚠️ **misfiled here** — dossier finds NO autophagy/mitochondrial evidence; mechanism is AHR/NRF2 antioxidant + barrier postbiotic; reclassify) | yeast-ferment-filtrates |

## 7. Hydroxy acids & chemical exfoliants

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Alpha-hydroxy acids (Glycolic, Lactic + salts) | Glycolic Acid; Lactic Acid; Sodium/Ammonium Lactate | collagen/ECM loss · photoaging · hydration/water-loss · pigmentation/tone · barrier decline | core | ✅ | Hydration (lactate) | alpha-hydroxy-acids |
| Mandelic acid | Mandelic Acid | pigmentation/tone · photoaging · inflammaging · collagen/ECM loss | core | ✅ | — | mandelic-acid |
| Salicylic acid (BHA) + derivatives (Betaine Salicylate, Hydroxyethyl Salicylate, Willow Bark) | Salicylic Acid; Betaine Salicylate; Salix Alba Bark Ext. | inflammaging · barrier decline · photoaging · pigmentation/tone · microbiome | core | ✅ | — | salicylic-acid-bha |
| LHA (Capryloyl Salicylic Acid) | Capryloyl Salicylic Acid | photoaging · barrier decline · inflammaging · pigmentation/tone | core | ✅ | — | lha-capryloyl-salicylic-acid |
| Azelaic acid (+ Potassium Azeloyl Diglycinate) | Azelaic Acid; Potassium Azeloyl Diglycinate | pigmentation/tone · inflammaging · oxidative stress · photoaging · microbiome | core | ✅ | — | azelaic-acid |
| PHAs / bionic acids (Gluconolactone, Lactobionic, Maltobionic, Gluconic, Galactose) | Gluconolactone; Lactobionic Acid; Maltobionic Acid | hydration/water-loss · oxidative stress · barrier decline · photoaging · glycation/AGEs · collagen/ECM loss | core | ✅ | Hydration | pha-bionic-acids |
| Secondary AHAs (Malic, Tartaric, Citric) | Malic Acid; Tartaric Acid; Citric Acid | photoaging · hydration/water-loss · oxidative stress · pigmentation/tone | supporting | ✅ | — | secondary-ahas |
| Pyruvic acid | Pyruvic Acid | photoaging · collagen/ECM loss · pigmentation/tone · inflammaging | supporting (conditional) | ✅ | conditional / professional-peel only — human RCTs are for 35–50% in-clinic peels (acne, melasma); anti-aging data uncontrolled; skip as leave-on hero, default to lactic acid | pyruvic-acid |
| Phytic acid | Phytic Acid | oxidative stress · pigmentation/tone · glycation/AGEs | supporting | ✅ | supporting/multifunctional — best, most defensible role is a biodegradable EDTA-alternative **chelator/antioxidant**; gentle exfoliant/brightener but ALL human efficacy is combination-peel data (loses head-to-head when isolated); ~660 Da/highly charged → poor dermal penetration; no glycation/AGEs skin evidence found despite hallmark tag; not a hero | phytic-acid |
| Shikimic acid | Shikimic Acid | oxidative stress · pigmentation/tone · microbiome | fringe | ✅ | — | shikimic-acid |
| Niche/long-tail acids (Glucoheptonolactone, Tropic Acid, neutralized glycolate salts) | Glucoheptonolactone; Tropic Acid; Ammonium Glycolate | hydration/water-loss · photoaging · oxidative stress | fringe | ✅ | — | niche-hydroxy-acids |

## 8. Barrier lipids & skin-identical actives

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Ceramides (full skin-identical spectrum NP/AP/EOP/NS/EOS + pseudo-ceramides + glucosylceramides) | Ceramide NP/AP/EOP/NS/EOS; Glucosylceramides; pseudo-ceramides | barrier decline · hydration/water-loss · photoaging · inflammaging · microbiome | core | ✅ | Autophagy (ceramide signaling) | ceramides |
| Cholesterol (+ cholesteryl esters) | Cholesterol; Cholesteryl Esters | barrier decline · hydration/water-loss | core | ✅ | — | cholesterol |
| Phytosterols (Beta-Sitosterol, Phytosteryl Macadamiate, Lanosterol, Ergosterol) | Phytosterols; Beta-Sitosterol | barrier decline · oxidative stress · inflammaging · collagen/ECM loss · hydration/water-loss | supporting | ✅ | — | phytosterols |
| Free fatty acids (Linoleic, Linolenic, Oleic, Palmitic, Stearic, Behenic, Lignoceric) | Linoleic Acid; Stearic Acid; Behenic Acid | barrier decline · hydration/water-loss · inflammaging | core | ✅ | — | free-fatty-acids |
| Squalane (+ Squalene) | Squalane; Squalene | hydration/water-loss · barrier decline · oxidative stress | core | ✅ | — | squalane |
| Phytosphingosine & sphingoid bases (Phytosphingosine, Sphingosine, Sphinganine, Salicyloyl Phytosphingosine, S1P) | Phytosphingosine; Sphingosine; Salicyloyl Phytosphingosine | barrier decline · inflammaging · microbiome · hydration/water-loss · photoaging · collagen/ECM loss · cellular senescence | core | ✅ | — | phytosphingosine-sphingoids |
| Ceramide-cholesterol-FFA physiological triad (3:1:1) | Ceramides + Cholesterol + Fatty Acids | barrier decline · hydration/water-loss · photoaging | core | ✅ | (overlaps ceramides) | barrier-lipid-triad |
| Skin-surface-lipid mimetics (L22-type, Jojoba esters) | Jojoba Esters; Phytosteryl Macadamiate complex | barrier decline · hydration/water-loss · oxidative stress | supporting | ✅ | — | skin-surface-lipid-mimetics |
| Botanical glucosylceramide sources (Rice, Wheat, Konjac, fermented ceramides) | Oryza/Triticum/Amorphophallus Glucosylceramides | barrier decline · hydration/water-loss · microbiome · inflammaging | supporting | ✅ | — | botanical-glucosylceramides |

## 9. Humectants & hydration actives

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Hyaluronic acid (all MW grades + salts/derivatives) | Hyaluronic Acid; Sodium Hyaluronate; Hydrolyzed HA; HA Crosspolymer | hydration/water-loss · barrier decline · collagen/ECM loss · photoaging · inflammaging | core | ✅ | — | hyaluronic-acid |
| Glycerin (glycerol) | Glycerin | hydration/water-loss · barrier decline | core | ✅ | — | glycerin |
| Panthenol (Provitamin B5) | Panthenol | hydration/water-loss · barrier decline · inflammaging | core | ✅ | — | panthenol |
| Urea (+ Hydroxyethyl Urea) | Urea; Hydroxyethyl Urea | hydration/water-loss · barrier decline | core | ✅ | — | urea |
| NMF complex (Sodium PCA, PCA salts, amino-acid blend, Sodium Lactate) | Sodium PCA; Arginine PCA; NMF amino acids | hydration/water-loss · barrier decline | core | ✅ | — | nmf-complex |
| Polyglutamic Acid (PGA) | Polyglutamic Acid / Sodium Polyglutamate | hydration/water-loss · barrier decline · collagen/ECM loss | core | ✅ | — | polyglutamic-acid |
| Beta-Glucan | Beta-Glucan | hydration/water-loss · collagen/ECM loss · barrier decline · inflammaging | core | ✅ | Botanicals (oat) | beta-glucan |
| Ectoin (+ Hydroxyectoine) | Ectoin; Hydroxyectoine | hydration/water-loss · oxidative stress · photoaging · inflammaging · barrier decline | core | ✅ | Antioxidants; Sunscreen; Experimental | ectoin |
| Betaine (Trimethylglycine) | Betaine | hydration/water-loss · barrier decline | supporting | ✅ | — | betaine |
| Saccharide Isomerate (Pentavitin) | Saccharide Isomerate | hydration/water-loss · barrier decline | supporting | ✅ | — | saccharide-isomerate |
| Snow Mushroom / Tremella extract | Tremella Fuciformis Extract | hydration/water-loss · oxidative stress · barrier decline | supporting | ✅ | Botanicals | tremella-snow-mushroom |
| Biosaccharide Gum-1 (Fucogel) | Biosaccharide Gum-1 | hydration/water-loss · barrier decline · inflammaging | supporting | ✅ | — | biosaccharide-gum-1 |
| Sugar-alcohol humectants (Sorbitol, Xylitol, Maltitol, Mannitol, Aquaxyl) | Sorbitol; Xylitol; Xylitylglucoside | hydration/water-loss · barrier decline · microbiome · oxidative stress | supporting | ✅ | — | sugar-alcohol-humectants |
| Glycols (Propanediol, Butylene/Pentylene/Propylene/Hexylene Glycol, Polyglycerins) | Propanediol; Butylene Glycol; Polyglycerin-3 | hydration/water-loss | fringe | ✅ | — | glycol-humectants |
| Glyceryl Glucoside (Glycoin) | Glyceryl Glucoside | hydration/water-loss · oxidative stress · barrier decline | supporting | ✅ | — | glyceryl-glucoside |
| Aquaporin-modulating actives (Imperata Cylindrica etc.) | Imperata Cylindrica Root Extract | hydration/water-loss · barrier decline | fringe | ✅ | — | aquaporin-actives |
| Allantoin | Allantoin | barrier decline · inflammaging · hydration/water-loss | supporting | ✅ | Botanicals (comfrey) | allantoin |
| Inositol | Inositol | hydration/water-loss · barrier decline | fringe | ✅ | — | inositol |
| Glycogen / Glycan humectants (Glycogen, Fructan/Levan) | Glycogen; Fructan | hydration/water-loss · barrier decline · collagen/ECM loss | fringe | ✅ | — | glycan-humectants |
| Prebiotic sugars (Inulin, FOS, Alpha-Glucan Oligosaccharide) | Inulin; Fructooligosaccharides; Alpha-Glucan Oligosaccharide | microbiome · hydration/water-loss | supporting | ✅ | Experimental | prebiotic-sugars |
| Honey / honey extract | Honey / Mel | hydration/water-loss · oxidative stress · microbiome | fringe | ✅ | — | honey-extract |
| Sodium Chondroitin Sulfate | Sodium Chondroitin Sulfate | hydration/water-loss · collagen/ECM loss | supporting | ✅ | — | chondroitin-sulfate |
| Marine/ferment exopolysaccharides (Algae Ext., Pseudoalteromonas/Antarcticine, Sphingomonas Ferment) | Algae Extract; Pseudoalteromonas Ferment Extract | hydration/water-loss · collagen/ECM loss · barrier decline · oxidative stress · inflammaging | supporting | ✅ | — | marine-ferment-exopolysaccharides |
| Resurrection plant extracts (Haberlea, Myrothamnus) | Haberlea Rhodopensis Ext.; Myrothamnus Flabellifolia Ext. | hydration/water-loss · oxidative stress · cellular senescence · mitochondrial decline | fringe | ✅ | — | resurrection-plant-extracts |

## 10. Growth factors, cytokines, exosomes, conditioned media & regenerative

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Recombinant growth factors (EGF, bFGF/FGF-2, aFGF, KGF, IGF-1, TGF-β1, PDGF, VEGF, HGF, CTGF, etc.) | sh-Oligopeptide-1/-2; sh-Polypeptide-1/-9/-11; etc. | collagen/ECM loss · barrier decline · photoaging · inflammaging · mitochondrial decline | core | ✅ | Peptides; Experimental | growth-factors |
| Exosomes (MSC/ADSC/iPSC/platelet/milk/plant exosomes) | Human/Adipose/iPSC Exosomes; plant callus exosomes | collagen/ECM loss · cellular senescence · inflammaging · oxidative stress · photoaging · pigmentation/tone · hydration/water-loss | core | ✅ | Experimental | exosomes |
| Conditioned media / secretomes (fibroblast TNS, ADSC-CM, MSC-CM, cord-lining PTT-6, bone-marrow) | Human Fibroblast/Adipose/Umbilical Conditioned Media | collagen/ECM loss · photoaging · barrier decline · oxidative stress · cellular senescence · inflammaging | core | ✅ | — | conditioned-media-secretomes |
| Defensins (LGR6+ stem-cell activators) | sh-Polypeptide (Defensin) complex | cellular senescence · barrier decline · collagen/ECM loss | core | ✅ | — | defensins |
| PDRN / Polynucleotides (salmon DNA, PN-HPT, salmon roe DNA) | Sodium DNA; Sodium Polynucleotide | collagen/ECM loss · inflammaging · barrier decline · hydration/water-loss · pigmentation/tone | core | ✅ | Experimental | polynucleotides-pdrn |
| Cytokines in conditioned-media complexes (IL-6, IL-8, G-CSF, NGF, HB-EGF) | (within conditioned media) | inflammaging · collagen/ECM loss · barrier decline | fringe | ✅ | — | cytokine-complexes |
| Bio-placenta GF complex (recombinant) | sh-Oligopeptide/sh-Polypeptide blend | collagen/ECM loss · photoaging · barrier decline | supporting | ✅ | — | bio-placenta-gf-complex |
| Placenta extracts (human/animal) | Placental Protein / Extract | inflammaging · collagen/ECM loss · pigmentation/tone · hydration/water-loss | fringe | ✅ | — | placenta-extracts |
| Bovine colostrum / colostrum GFs | Colostrum / Hydrolyzed Colostrum | barrier decline · collagen/ECM loss · inflammaging | supporting | ✅ | — | bovine-colostrum |
| Platelet lysate (PRP-derived topical) | Platelet Lysate / Plasma Proteins | collagen/ECM loss · inflammaging · photoaging | supporting | ✅ | — | platelet-lysate |
| Snail Secretion Filtrate (snail mucin) | Snail Secretion Filtrate | barrier decline · hydration/water-loss · collagen/ECM loss · photoaging | supporting | ✅ | — | snail-secretion-filtrate |
| Sea cucumber / marine secretome extracts | Holothuria Extract | collagen/ECM loss · inflammaging | fringe | ✅ | — | marine-secretome-extracts |
| Thymosin Beta-4 (TB4 / TB-500) | sh-Oligopeptide (Thymosin β4) | collagen/ECM loss · inflammaging | fringe | ✅ | Peptides | thymosin-beta-4 |
| Recombinant human collagen (rh-collagen) | sh-Polypeptide (recombinant collagen) | collagen/ECM loss · hydration/water-loss · barrier decline | supporting | ✅ | — | recombinant-human-collagen |
| Postbiotic ferment lysates near-exosome (Lactobacillus/Bifida Ferment Lysate) | Lactobacillus/Bifida Ferment Lysate | microbiome · barrier decline · photoaging · oxidative stress · inflammaging · hydration/water-loss | supporting | ✅ | Botanicals; Experimental | postbiotic-ferment-lysates |

## 11. Botanicals & plant bioactives

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Centella asiatica (cica) + triterpenes (Madecassoside, Asiaticoside, Asiatic/Madecassic acid, TECA) | Centella Asiatica Extract; Madecassoside; Asiaticoside | collagen/ECM loss · barrier decline · inflammaging · oxidative stress · photoaging | core | ✅ | Senotherapeutics (araliadiol) | centella-asiatica |
| Licorice root + actives (Glabridin, Dipotassium Glycyrrhizate, Licochalcone A) | Glycyrrhiza Glabra Root Extract; Glabridin | pigmentation/tone · inflammaging · oxidative stress · barrier decline | core | ✅ | NAD/AMPK (enoxolone); Senotherapeutics | licorice-extract |
| Ginseng (Panax, red/fermented) + ginsenosides | Panax Ginseng Root Extract | collagen/ECM loss · oxidative stress · pigmentation/tone · inflammaging · cellular senescence | core | ✅ | Senotherapeutics (ginsenosides); Growth factors (exosomes) | ginseng-extract |
| Soy / soybean extract & isoflavones | Glycine Soja Extract | collagen/ECM loss · pigmentation/tone · hydration/water-loss · oxidative stress · photoaging | core | ✅ | NAD/AMPK; Experimental | soy-extract |
| Edelweiss extract (+ stem cell) | Leontopodium Alpinum Extract / Callus Culture Ext. | oxidative stress · photoaging · collagen/ECM loss · cellular senescence | core | ✅ | Growth factors (exosomes) | edelweiss-extract |
| Rosemary + actives (Carnosic/Rosmarinic acid) | Rosmarinus Officinalis Leaf Extract | oxidative stress · glycation/AGEs · inflammaging · photoaging | supporting | ✅ | Anti-glycation; Sunscreen | rosemary-extract |
| Berry extracts (Blueberry/Bilberry, Maqui, Cranberry, Goji) | Vaccinium spp.; Aristotelia Chilensis; Lycium Barbarum | oxidative stress · glycation/AGEs · photoaging · collagen/ECM loss · inflammaging · hydration/water-loss | supporting | ✅ | Botanicals; Anti-glycation; Sunscreen/photoprotection; Experimental | anti-age-berry-extracts |
| Grape seed / Pine bark proanthocyanidins (OPCs/Pycnogenol) | Vitis Vinifera Seed Extract; Pinus Pinaster Bark Extract | oxidative stress · collagen/ECM loss · photoaging · glycation/AGEs | core | ✅ | Anti-glycation | grape-seed-pine-bark-opcs |
| Plant stem cell extracts (Apple/PhytoCellTec, Grape Solar Vitis, Argan) | Malus Domestica / Vitis Vinifera Cell Culture Ext.; Argania Spinosa | cellular senescence · collagen/ECM loss · oxidative stress · photoaging · barrier decline · hydration/water-loss | supporting | ✅ | — | plant-stem-cell-extracts |
| K-beauty soothing herbs (Mugwort/Artemisia, Houttuynia, Lotus, Perilla) | Artemisia Vulgaris Ext.; Houttuynia Cordata Ext. | inflammaging · barrier decline · oxidative stress · microbiome · pigmentation/tone | supporting | ✅ | Anti-glycation (houttuynia) | kbeauty-soothing-herbs |
| Rice / rice bran extract + ferment | Oryza Sativa Extract; Rice Ferment Filtrate | oxidative stress · pigmentation/tone · barrier decline · hydration/water-loss · microbiome | supporting | ✅ | Hydration | rice-extract |
| Microalgae extracts (Spirulina, Chlorella, plankton) | Spirulina Platensis Ext.; Chlorella Vulgaris Ext. | oxidative stress · collagen/ECM loss · inflammaging · cellular senescence · barrier decline | supporting | ✅ | Anti-glycation (chlorella); Sunscreen (spirulina) | microalgae-extracts |
| Adaptogen mushrooms (Reishi, Chaga, Cordyceps) | Ganoderma Lucidum Ext.; Inonotus Obliquus Ext. | inflammaging · oxidative stress · barrier decline | supporting | ✅ | — | adaptogen-mushrooms |
| Adaptogen herbs (Ashwagandha, Schisandra, Rhodiola/Salidroside) | Withania Somnifera Ext.; Rhodiola Rosea Ext.; Salidroside | oxidative stress · cellular senescence · inflammaging · collagen/ECM loss | fringe | ✅ | Senotherapeutics (withaferin) | adaptogen-herbs |
| Olive leaf/fruit polyphenols (Oleuropein, Hydroxytyrosol) | Olea Europaea Leaf Extract | oxidative stress · inflammaging · photoaging · mitochondrial decline · glycation/AGEs | supporting | ✅ | Antioxidants (hydroxytyrosol); Anti-glycation | olive-polyphenols |
| Turmeric / curcuminoids | Curcuma Longa Root Extract; Tetrahydrocurcumin | oxidative stress · inflammaging · pigmentation/tone · glycation/AGEs | supporting | ✅ | NAD/AMPK; Senotherapeutics; Antioxidants | turmeric-curcuminoids |
| Camellia / tsubaki seed oil | Camellia Japonica Seed Oil | hydration/water-loss · barrier decline · oxidative stress | supporting | ✅ | — | camellia-seed-oil |
| Sea fennel (Crithmum maritimum) extract | Crithmum Maritimum Extract | collagen/ECM loss · oxidative stress · photoaging | supporting | ✅ | — | sea-fennel-extract |
| Antioxidant oils (Marula, Moringa, Prickly Pear, Argan) | Sclerocarya Birrea Seed Oil; Moringa Oleifera Seed Oil | barrier decline · hydration/water-loss · oxidative stress · inflammaging | supporting | ✅ | Anti-glycation (argan) | antioxidant-plant-oils |
| Flavonoid actives (Baicalin/Baicalein, Ginkgo, Rutin, Hesperidin, Naringenin) | Scutellaria Baicalensis Ext.; Ginkgo Biloba Ext.; Rutin | collagen/ECM loss · oxidative stress · photoaging · inflammaging · barrier decline · cellular senescence | supporting | ✅ | Anti-glycation | misc-flavonoids |
| Soothing botanicals (Aloe, Chamomile/Bisabolol, Calendula, Witch Hazel, Comfrey/Allantoin) | Aloe Barbadensis Ext.; Bisabolol; Calendula Officinalis Ext. | inflammaging · barrier decline · oxidative stress · hydration/water-loss | supporting | ✅ | Sunscreen (bisabolol); Hydration (allantoin) | soothing-botanicals |
| Coffee / green coffee (Chlorogenic acid, caffeine) | Coffea Arabica Seed Extract; Chlorogenic Acid | oxidative stress · photoaging · inflammaging · glycation/AGEs | supporting | ✅ | Anti-glycation | coffee-extract |
| Tannins / gallotannins (Tannic Acid, gallnut, mastic) | Tannic Acid; Pistacia Lentiscus Extract | oxidative stress · collagen/ECM loss · inflammaging | fringe | ✅ | — | tannins |
| Vitamin-C botanicals (Kakadu Plum, Amla, Yuzu, Tomato/Lycopene) | Terminalia Ferdinandiana Ext.; Phyllanthus Emblica Ext.; Citrus Junos Ext. | oxidative stress · pigmentation/tone · photoaging · glycation/AGEs · collagen/ECM loss | supporting | ✅ | Anti-glycation (amla) | vitamin-c-botanicals |
| Extreme-environment botanicals (Snow Lotus, Helichrysum/Immortelle, Cistus, Sage) | Saussurea Involucrata Ext.; Helichrysum Italicum Ext.; Cistus Ladaniferus Ext. | oxidative stress · photoaging · inflammaging · cellular senescence · glycation/AGEs · collagen/ECM loss | fringe | ✅ | Senotherapeutics (cistus); Anti-glycation (sage) | extreme-environment-botanicals |
| Bamboo silica | Bambusa Vulgaris Extract | collagen/ECM loss · hydration/water-loss | fringe | ✅ | — | bamboo-silica |
| Mangosteen / alpha-mangostin | Garcinia Mangostana Peel Extract | oxidative stress · inflammaging · glycation/AGEs | fringe | ✅ | — | mangosteen-extract |
| Japanese knotweed (resveratrol source) | Polygonum Cuspidatum Root Extract | oxidative stress · inflammaging | supporting | ✅ | NAD/AMPK | japanese-knotweed |

## 12. Anti-glycation & related

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Branded anti-glycation actives (NAHP/Glycostop, Collrepair DG, Aldenine, Preventhelia, Amadorine, Antiglyskin, Glistin, Ameliox, Aglycal) | various branded blends | glycation/AGEs · collagen/ECM loss · oxidative stress · photoaging · mitochondrial decline | core | ✅ | — | branded-anti-glycation-actives |
| Aminoguanidine | Aminoguanidine (Pimagedine) | glycation/AGEs | fringe | ✅ | Experimental | aminoguanidine |
| AGE crosslink breakers (Alagebrium/ALT-711, phenacylthiazolium salts) | Alagebrium chloride | glycation/AGEs · collagen/ECM loss | fringe | ✅ | — | age-crosslink-breakers |
| B-vitamin anti-glycation agents (Pyridoxamine, P5P/Pyridoxine, Benfotiamine, Thiamine) | Pyridoxamine; Benfotiamine; Thiamine HCl | glycation/AGEs · oxidative stress | supporting | ✅ | — | b-vitamin-anti-glycation |
| Dihydromyricetin (Ampelopsin, RAGE antagonist) | Dihydromyricetin | glycation/AGEs · cellular senescence · collagen/ECM loss · photoaging | supporting | ✅ | — | dihydromyricetin |
| Salvianolic acid B / Danshen (Salvia miltiorrhiza) | Salvia Miltiorrhiza Root Extract; Salvianolic Acid B | glycation/AGEs · collagen/ECM loss · oxidative stress | supporting | ✅ | (Collrepair DG component) | salvianolic-acid-b |
| Anti-glycation phenolic acids (Methyl Gallate, Vanillic, Chlorogenic) | Methyl Gallate; Vanillic Acid | glycation/AGEs · collagen/ECM loss · oxidative stress | fringe | ✅ | — | anti-glycation-phenolic-acids |
| Plantamajoside (Plantago) | Plantamajoside | glycation/AGEs · inflammaging · oxidative stress | fringe | ✅ | — | plantamajoside |
| Botanical anti-AGE extracts (Cirsium japonicum, Akebia, Manilkara, Cecropia, Djulis, Sunflower sprout, Schizonepeta, Jasminum cell, Papaya, Lotus stamen, Black cumin, Hazelnut skin, Pholiota, Dunaliella, Parachlorella, Mycosporine-like AAs) | various plant/algae extracts | glycation/AGEs · oxidative stress · collagen/ECM loss · cellular senescence · photoaging · inflammaging | fringe | ✅ | Sunscreen (MAAs) | botanical-anti-age-extracts |
| N-Acetyl Hydroxyproline | Acetyl Hydroxyproline | glycation/AGEs · collagen/ECM loss | fringe | ✅ | — | acetyl-hydroxyproline |
| Carnosine zinc complex (Polaprezinc) | Zinc L-Carnosine | glycation/AGEs · barrier decline · oxidative stress | supporting | ✅ | — | zinc-carnosine-polaprezinc |
| Beta-alanine (carnosine precursor) | Beta-Alanine | glycation/AGEs | fringe | ✅ | — | beta-alanine |
| Thymoquinone (Nigella sativa) | Thymoquinone | glycation/AGEs · oxidative stress · inflammaging | fringe | ✅ | — | thymoquinone |
| C-Xyloside (C-glycoside) | Hydroxypropyl Tetrahydropyrantriol | collagen/ECM loss · glycation/AGEs · hydration/water-loss | supporting | ✅ | — | c-xyloside |
| Gold nanoparticles | Colloidal Gold | glycation/AGEs | fringe | ✅ | — | gold-nanoparticles |
| Acetyl Glutamine | Acetyl Glutamine | glycation/AGEs · barrier decline | fringe | ✅ | — | acetyl-glutamine |
| Fish collagen tripeptides (oral-adjacent) | Hydrolyzed Collagen | glycation/AGEs · collagen/ECM loss · oxidative stress | fringe | ✅ | Peptides | fish-collagen-tripeptides |

## 13. Sunscreen / photoprotection filters & adjuncts

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Sunscreen / photoprotection (filter system overview) | (organic + mineral filters) | photoaging · collagen/ECM loss · oxidative stress · pigmentation/tone · barrier decline | core | ✅ | — | sunscreen-photoprotection |
| Avobenzone (UVA1) | Butyl Methoxydibenzoylmethane | photoaging · collagen/ECM loss · oxidative stress · pigmentation/tone | core | ✅ | — | avobenzone |
| Next-gen broad-spectrum organic filters (Bemotrizinol/Tinosorb S, Bisoctrizole/Tinosorb M, Tinosorb A2B, DHHB/Uvinul A Plus, EHT/Uvinul T 150, Mexoryl SX/XL/400, TriAsorB) | Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine; Methylene Bis-Benzotriazolyl Tetramethylbutylphenol; Diethylamino Hydroxybenzoyl Hexyl Benzoate; etc. | photoaging · collagen/ECM loss · oxidative stress · pigmentation/tone | core | ✅ | bemotrizinol now US-GRASE (≤6%, 2026-06-09) — first new US filter since 1999 | next-gen-uv-filters |
| Legacy UVB organic filters (Octinoxate, Homosalate, Octisalate, Octocrylene, Ensulizole, Amiloxate, Iscotrizinol, Polysilicone-15, Neo Heliopan AP) | Ethylhexyl Methoxycinnamate; Homosalate; Ethylhexyl Salicylate; Octocrylene | photoaging · oxidative stress | supporting | ✅ | — | legacy-uvb-filters |
| Benzophenone filters (Oxybenzone, Sulisobenzone, BP-5, Dioxybenzone) | Benzophenone-3/-4/-5/-8 | photoaging · oxidative stress | supporting | ✅ | — | benzophenone-filters |
| Deprecated/niche filters (PABA, Padimate O, PEG-25 PABA, Cinoxate, Trolamine Salicylate, Meradimate, camphor derivatives) | PABA; Ethylhexyl Dimethyl PABA; 4-Methylbenzylidene Camphor | photoaging | fringe | ✅ | — | deprecated-uv-filters |
| Zinc Oxide (incl. nano) | Zinc Oxide | photoaging · barrier decline · oxidative stress · inflammaging · pigmentation/tone | core | ✅ | — | zinc-oxide |
| Titanium Dioxide (incl. nano) | Titanium Dioxide | photoaging · barrier decline · oxidative stress | core | ✅ | — | titanium-dioxide |
| DNA-repair enzymes (Photolyase, T4 Endonuclease V/Micrococcus Lysate, OGG1/Arabidopsis, UV endonuclease) | Plankton Extract (Photolyase); Micrococcus Lysate; Arabidopsis Thaliana Extract | photoaging · cellular senescence · oxidative stress · mitochondrial decline | core | ✅ | — | dna-repair-enzymes |
| Polypodium Leucotomos Extract (Fernblock) | Polypodium Leucotomos Leaf Extract | photoaging · oxidative stress · collagen/ECM loss · inflammaging · pigmentation/tone | core | ✅ | — | polypodium-leucotomos |
| Mycosporine-like amino acids (MAAs) | Porphyra Umbilicalis Extract | photoaging · oxidative stress · collagen/ECM loss · glycation/AGEs | supporting | ✅ | Anti-glycation | mycosporine-amino-acids |
| Photoprotective adjunct: Oxothiazolidine (Procysteine) | Oxothiazolidine Carboxylic Acid | oxidative stress · photoaging | fringe | ✅ | — | oxothiazolidine |
| Afamelanotide | Afamelanotide (drug) | photoaging · pigmentation/tone · oxidative stress | fringe | ✅ | — | afamelanotide |

## 14. Experimental / frontier & pharma-adjacent longevity actives

| Ingredient | INCI | Hallmark(s) | Relevance | Dossier? | Also listed in | Slug |
|---|---|---|---|---|---|---|
| Topical estrogens & estrogen-receptor activators (Estriol, Estradiol, MEP/Emepelle) | Estriol; Estradiol; Methyl Estradiolpropanoate | collagen/ECM loss · hydration/water-loss · barrier decline · photoaging · pigmentation/tone | core | ✅ | — | topical-estrogens-mep |
| Epitalon (Epithalon) | Ala-Glu-Asp-Gly tetrapeptide | cellular senescence · oxidative stress | fringe | ✅ | — | epitalon |
| Progerin-inhibitor complex | proprietary (no standard INCI) | cellular senescence · collagen/ECM loss | fringe | ✅ | — | progerin-inhibitor-complex |
| Live/topical probiotics (Lactobacillus, L. reuteri/rhamnosus, Nitrosomonas eutropha AOB) | Lactobacillus / Nitrosomonas Eutropha (live) | microbiome · barrier decline · inflammaging | fringe | ✅ | — | live-topical-probiotics |
| Microbiome postbiotics & ferments (Bifida/Lactobacillus/Lactococcus Ferment Lysate, L. plantarum, EPI-7, Vitreoscilla, Galactomyces, Saccharomyces) | Bifida Ferment Lysate; Lactobacillus Plantarum Ferment; Epidermidibacterium Keratini Ferment; Vitreoscilla Ferment | microbiome · barrier decline · inflammaging · photoaging · hydration/water-loss · collagen/ECM loss · oxidative stress | core | ✅ | Botanicals; Autophagy; Growth factors | microbiome-postbiotics |
| Cannabinoids (CBD, CBG) | Cannabidiol; Cannabigerol | inflammaging · oxidative stress · barrier decline · microbiome | supporting | ✅ | Antioxidants | cannabinoids |
| Reprogramming / klotho-mimetic frontier actives (Yamanaka-factor concepts, metadichol/policosanol) | experimental (mRNA/peptide/nano) | cellular senescence · collagen/ECM loss · mitochondrial decline | fringe | ✅ | — | reprogramming-klotho-actives |

---

## Cross-listing summary (high-overlap multi-class ingredients)

These ingredients recurred across many class lists; their consolidated home (primaryClass) is shown,
with the deep-research run expected to cover their multi-pathway behavior:

- **Carnosine** → Peptides (also Antioxidants, NAD/sirtuin, Anti-glycation, Sunscreen, Experimental)
- **Resveratrol** → NAD/sirtuin (also Senotherapeutics, Autophagy, Botanicals, Anti-glycation, Sunscreen, Experimental) — has dossier
- **Spermidine** → Antioxidants (also NAD/sirtuin, Senotherapeutics, Autophagy, Anti-glycation, Botanicals, Experimental) — has dossier
- **Niacinamide / NAD precursors** → NAD longevity (also Antioxidants, Autophagy, Anti-glycation, Sunscreen, Experimental) — has dossier(s)
- **Ergothioneine** → Antioxidants (also Autophagy, Hydration, Anti-glycation, Sunscreen, Experimental) — has dossier
- **Fisetin / Quercetin / EGCG / Apigenin / Kaempferol** → NAD/sirtuin (also Senotherapeutics, Autophagy, Botanicals, Anti-glycation)
- **GHK-Cu / copper peptides** → Peptides (also Senotherapeutics, Growth factors, Anti-glycation, Experimental) — has dossier
- **OS-01 / Peptide 14** → Senotherapeutics (also Peptides, NAD/AMPK, Experimental) — has dossier
- **Urolithin A / Trehalose / CoQ10 / Idebenone / Alpha-Lipoic Acid** → Autophagy/mitochondrial & Antioxidants overlap
- **Ectoin** → Hydration (also Antioxidants, Sunscreen, Experimental) — has dossier
- **Ceramides** → Barrier lipids (also Autophagy) — has dossier
- **Bakuchiol** → Retinoids (also Botanicals, Sunscreen) — has dossier
