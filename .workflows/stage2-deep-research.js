export const meta = {
  name: 'stage2-deep-research',
  description: 'Exhaustive cited literature review for every ingredient in the master index, adversarial evidence verification, and a synthesized evidence matrix. Runs by tier wave and self-commits after each wave.',
  phases: [
    { title: 'Load', detail: 'read master index -> full ingredient list' },
    { title: 'Core', detail: 'core tier: exhaustive lit review -> adversarial verify -> commit' },
    { title: 'Supporting', detail: 'supporting tier: review -> verify -> commit' },
    { title: 'Fringe', detail: 'fringe tier: review -> verify -> commit' },
    { title: 'Synthesize', detail: 'evidence matrix + landmark papers + master-index update + final commit' },
  ],
}

const DIR = 'C:/Users/Hasan/Kintsugi_Anti_Aging'

const LIST_SCHEMA = {
  type: 'object',
  properties: {
    ingredients: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' }, slug: { type: 'string' }, primaryClass: { type: 'string' },
          relevance: { type: 'string' }, hasDossier: { type: 'boolean' },
        },
        required: ['name', 'slug', 'relevance'],
      },
    },
  },
  required: ['ingredients'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    slug: { type: 'string' }, fileWritten: { type: 'boolean' },
    topEvidenceTier: { type: 'string', enum: ['human-topical-RCT', 'human-topical-other', 'human-oral', 'animal', 'in-vitro', 'none'] },
    topicalViability: { type: 'string', enum: ['strong', 'moderate', 'weak', 'unknown'] },
    verdict: { type: 'string', enum: ['hero', 'supporting', 'conditional', 'skip'] },
    sourceCount: { type: 'number' }, keyClaims: { type: 'array', items: { type: 'string' } },
  },
  required: ['slug', 'fileWritten', 'topEvidenceTier', 'verdict'],
}

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    slug: { type: 'string' }, evidenceGrade: { type: 'string', enum: ['A', 'B', 'C', 'D'] },
    verified: { type: 'boolean' }, majorIssues: { type: 'array', items: { type: 'string' } },
  },
  required: ['slug', 'evidenceGrade'],
}

function litReviewPrompt(ing) {
  return `You are writing an EXHAUSTIVE, citation-backed literature review on the skincare ingredient "${ing.name}" (slug: ${ing.slug}; class: ${ing.primaryClass || 'n/a'}) for an anti-aging / skin-longevity brand's research base. Use the real current date.

Read first for format + claims discipline:
- ${DIR}/CLAUDE.md
- ${DIR}/research/ingredients/_template.md
- ${DIR}/brand/glossary.md

Do DEEP web + literature research — multiple searches; pull PRIMARY sources (PubMed, peer-reviewed journals, systematic reviews, reputable dermatology references). Be exhaustive and brutally honest about evidence quality. Then write a thorough dossier to ${DIR}/research/ingredients/${ing.slug}.md ${ing.hasDossier ? '(a dossier already exists — UPGRADE it to this exhaustive standard, preserving anything still valid)' : ''} with:
1. Identity — common name, INCI, key forms/derivatives.
2. Class & mechanism — how it works at the skin/cell level.
3. Hallmarks targeted — which hallmark(s) of skin aging (collagen/ECM loss, barrier decline, oxidative stress, glycation/AGEs, cellular senescence, mitochondrial decline, inflammaging, photoaging, pigmentation/tone, microbiome, hydration/water-loss).
4. **Evidence review by tier (the core of this dossier)** — separate clearly: in-vitro -> animal -> human ORAL -> human TOPICAL (RCT vs lower). Cite MANY real studies (authors/year + link/DOI), with sample sizes and limitations. Make explicit which benefits are proven for TOPICAL human use vs. borrowed from another format.
5. Topical bioavailability / penetration.
6. Formulation — effective concentration, pH, stability, pairings/conflicts, sensory.
7. Safety — irritation, sun sensitivity, pregnancy, sensitization, sourcing/sustainability.
8. Regulatory & claims — cosmetic vs. drug line; what can/can't be claimed (per CLAUDE.md guardrails).
9. Sourcing & cost.
10. Hype vs. evidence — call out marketing overreach.
11. Verdict for the brand — hero / supporting / conditional / skip + one-line reasoning + longevity-relevance note.
12. Sources — numbered, with links.

Cite ONLY real sources; never invent citations — mark "[unverified]" if you cannot confirm one. Do NOT run git. Then return the structured summary.`
}

function verifyPrompt(ing) {
  return `Adversarially verify the dossier at ${DIR}/research/ingredients/${ing.slug}.md for "${ing.name}". Read the file. For each headline efficacy claim check: (a) is the evidence HUMAN and TOPICAL, or quietly borrowed from in-vitro/animal/oral data? (b) are the cited studies real and do they say what is claimed? (c) are key studies industry-funded or very small? Be skeptical and specific.

Then APPEND a section "## Evidence verification (adversarial)" to the file containing: an overall evidence grade (A = strong human-topical RCT evidence; B = moderate human-topical; C = weak/indirect; D = essentially unproven topically / hype), the main caveats, and a list of any claims that should be softened. Edit any overstated claim in the dossier itself to be defensible. Do NOT run git. Return the structured verdict.`
}

function commitPrompt(wave) {
  return `Commit the completed ${wave} work for the brand research repo. Run exactly:
git -C "${DIR}" add -A
git -C "${DIR}" commit -m "Stage 2 deep research: ${wave}"
git -C "${DIR}" push
The repo is authenticated via the gh CLI. If there is nothing to commit, just report that. Report the outcome (commit hash or 'nothing to commit').`
}

async function runTier(title, items) {
  if (!items.length) return []
  phase(title)
  log(`${title} tier: ${items.length} ingredients (exhaustive review -> verify)`)
  const res = await pipeline(
    items,
    (ing) => agent(litReviewPrompt(ing), { label: `review:${ing.slug}`, phase: title, schema: REVIEW_SCHEMA, agentType: 'general-purpose' }),
    (rev, ing) => agent(verifyPrompt(ing), { label: `verify:${ing.slug}`, phase: title, schema: VERIFY_SCHEMA, agentType: 'general-purpose' }).then(v => ({ ing, rev, v }))
  )
  const ok = res.filter(Boolean)
  await agent(commitPrompt(`${title}-tier ingredient literature reviews (${ok.length})`), { label: `commit:${title}`, phase: title, agentType: 'general-purpose' })
  log(`${title} tier done: ${ok.length}/${items.length} reviewed + committed`)
  return ok
}

// ---- Load the master list (self-loading: reads the committed index) ----
phase('Load')
const loaded = await agent(
  `Read ${DIR}/research/ingredients/_MASTER-INDEX.md and extract EVERY ingredient row from ALL class tables (there should be ~232). For each return: name, slug (from the Slug column), primaryClass, relevance (core/supporting/fringe), and hasDossier (the Dossier? column: a check mark -> true). Do not skip any rows.`,
  { label: 'load:master-index', phase: 'Load', schema: LIST_SCHEMA, agentType: 'general-purpose' }
)
const ALL = (loaded && loaded.ingredients) ? loaded.ingredients : []
log(`Loaded ${ALL.length} ingredients from the master index.`)

const core = ALL.filter(i => i.relevance === 'core')
const supporting = ALL.filter(i => i.relevance === 'supporting')
const fringe = ALL.filter(i => i.relevance === 'fringe')

// ---- Tier waves (each self-commits) ----
const r1 = await runTier('Core', core)
const r2 = await runTier('Supporting', supporting)
const r3 = await runTier('Fringe', fringe)
const all = [...r1, ...r2, ...r3]

// ---- Synthesis ----
phase('Synthesize')
const compact = JSON.stringify(all.map(x => ({
  slug: x.ing.slug, name: x.ing.name, class: x.ing.primaryClass, relevance: x.ing.relevance,
  grade: x.v ? x.v.evidenceGrade : null, tier: x.rev ? x.rev.topEvidenceTier : null,
  topical: x.rev ? x.rev.topicalViability : null, verdict: x.rev ? x.rev.verdict : null,
})))
await agent(
  `Using this verified ingredient dataset (${all.length} ingredients):\n${compact}\n\nWrite TWO files:\n1. ${DIR}/research/ingredients/_EVIDENCE-MATRIX.md — a master evidence matrix: a table of every ingredient with columns Ingredient | Class | Relevance | Top evidence tier | Topical viability | Evidence grade (A-D) | Verdict, sorted so the strongest-evidence actives surface first; plus a "Best-evidence shortlist" (grades A/B) and a "Hype watch" list (grade D).\n2. ${DIR}/research/science/landmark-papers.md — a curated list of the landmark/pivotal papers and key reviews per hallmark of skin aging, drawn from the dossiers' sources.\nAlso update the "Dossier?" flags in ${DIR}/research/ingredients/_MASTER-INDEX.md to a check mark for every ingredient now reviewed. Do NOT run git. Confirm when written.`,
  { label: 'synthesize:matrix', phase: 'Synthesize', agentType: 'general-purpose' }
)
await agent(commitPrompt('evidence matrix, landmark papers, master-index update'), { label: 'commit:final', phase: 'Synthesize', agentType: 'general-purpose' })

return { loaded: ALL.length, reviewed: all.length, core: r1.length, supporting: r2.length, fringe: r3.length }
