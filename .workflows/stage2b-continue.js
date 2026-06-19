export const meta = {
  name: 'stage2b-continue',
  description: 'Idempotent continuation of Stage 2 ingredient deep-research: researches ONLY ingredients still missing a dossier, then (optionally) synthesizes the evidence matrix. Model + synthesis are run-time configurable via args. Self-commits per wave. Safe to re-run.',
  phases: [
    { title: 'Load', detail: 'master index minus existing dossiers -> remaining list' },
    { title: 'Supporting', detail: 'remaining supporting-tier: review -> verify -> commit' },
    { title: 'Fringe', detail: 'remaining fringe-tier: review -> verify -> commit' },
    { title: 'Core', detail: 'any remaining core-tier: review -> verify -> commit' },
    { title: 'Synthesize', detail: 'evidence matrix + landmark papers (skipped if args.skipSynthesis)' },
  ],
}

const DIR = 'C:/Users/Hasan/Kintsugi_Anti_Aging'

// Run-time overrides via Workflow args: { model: 'sonnet'|'opus'|'haiku', verifyModel?, skipSynthesis: true }
const A = (args && typeof args === 'object') ? args : {}
const MODEL = A.model || undefined            // undefined => inherit session model
const VERIFY_MODEL = A.verifyModel || MODEL   // allow a different (stronger) verify tier
const SKIP_SYNTH = !!A.skipSynthesis

const LOAD_SCHEMA = {
  type: 'object',
  properties: {
    totalCount: { type: 'number' }, existingCount: { type: 'number' }, missingCount: { type: 'number' },
    missing: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, slug: { type: 'string' }, primaryClass: { type: 'string' }, relevance: { type: 'string' } }, required: ['name', 'slug', 'relevance'] } },
  },
  required: ['missing', 'missingCount'],
}
const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    slug: { type: 'string' }, fileWritten: { type: 'boolean' },
    topEvidenceTier: { type: 'string', enum: ['human-topical-RCT', 'human-topical-other', 'human-oral', 'animal', 'in-vitro', 'none'] },
    topicalViability: { type: 'string', enum: ['strong', 'moderate', 'weak', 'unknown'] },
    verdict: { type: 'string', enum: ['hero', 'supporting', 'conditional', 'skip'] },
    sourceCount: { type: 'number' },
  },
  required: ['slug', 'fileWritten', 'verdict'],
}
const VERIFY_SCHEMA = { type: 'object', properties: { slug: { type: 'string' }, evidenceGrade: { type: 'string', enum: ['A', 'B', 'C', 'D'] }, verified: { type: 'boolean' } }, required: ['slug', 'evidenceGrade'] }

function litReviewPrompt(ing) {
  return `Write an EXHAUSTIVE, citation-backed literature review on the skincare ingredient "${ing.name}" (slug: ${ing.slug}; class: ${ing.primaryClass || 'n/a'}) for an anti-aging / skin-longevity brand. Use the real current date.

Read first for format + claims discipline: ${DIR}/CLAUDE.md , ${DIR}/research/ingredients/_template.md , ${DIR}/brand/glossary.md .

Do DEEP web + literature research (multiple searches; pull PRIMARY sources — PubMed, peer-reviewed journals, systematic reviews, reputable derm references). Be exhaustive and brutally honest about evidence quality. Write the dossier to ${DIR}/research/ingredients/${ing.slug}.md with: 1) Identity (common name, INCI, forms); 2) Class & mechanism; 3) Hallmarks targeted (collagen/ECM loss, barrier decline, oxidative stress, glycation/AGEs, cellular senescence, mitochondrial decline, inflammaging, photoaging, pigmentation/tone, microbiome, hydration); 4) **Evidence review by tier** — in-vitro -> animal -> human ORAL -> human TOPICAL (RCT vs lower), citing MANY real studies (authors/year + link/DOI) with sample sizes/limitations, explicit about what's proven for TOPICAL human use vs borrowed from other formats; 5) Topical bioavailability; 6) Formulation (conc, pH, stability, pairings, sensory); 7) Safety (irritation, sun, pregnancy, sensitization, sourcing); 8) Regulatory & claims (cosmetic vs drug per CLAUDE.md); 9) Sourcing & cost; 10) Hype vs evidence; 11) Verdict for the brand (hero/supporting/conditional/skip + reasoning + longevity note); 12) Sources (numbered, linked).

Cite ONLY real sources; mark "[unverified]" if you cannot confirm one. Do NOT run git. Return the structured summary.`
}
function verifyPrompt(ing) {
  return `Adversarially verify the dossier at ${DIR}/research/ingredients/${ing.slug}.md for "${ing.name}". Read the file. For each headline claim check: (a) is the evidence HUMAN and TOPICAL, or borrowed from in-vitro/animal/oral? (b) are cited studies real and do they say what's claimed? (c) industry-funded or tiny? Append a section "## Evidence verification (adversarial)" with an overall grade (A=strong human-topical RCT; B=moderate human-topical; C=weak/indirect; D=unproven topically/hype), main caveats, and claims to soften; edit any overstated claim in the dossier to be defensible. Do NOT run git. Return the verdict.`
}
function commitPrompt(wave) {
  return `Commit the brand research repo. Run exactly:\ngit -C "${DIR}" add -A\ngit -C "${DIR}" commit -m "Stage 2 (cont.): ${wave}"\ngit -C "${DIR}" push\nThe repo is gh-authenticated. If nothing to commit, report that. Report the outcome.`
}

async function runTier(title, items) {
  if (!items.length) { log(`${title}: nothing remaining, skipping`); return [] }
  phase(title)
  log(`${title}: ${items.length} remaining ingredients (model=${MODEL || 'inherited'})`)
  const res = await pipeline(
    items,
    (ing) => agent(litReviewPrompt(ing), { label: `review:${ing.slug}`, phase: title, schema: REVIEW_SCHEMA, agentType: 'general-purpose', model: MODEL }),
    (rev, ing) => agent(verifyPrompt(ing), { label: `verify:${ing.slug}`, phase: title, schema: VERIFY_SCHEMA, agentType: 'general-purpose', model: VERIFY_MODEL, effort: 'high' }).then(v => ({ ing, rev, v }))
  )
  const ok = res.filter(Boolean)
  await agent(commitPrompt(`${title}-tier remaining dossiers (${ok.length}, model=${MODEL || 'inherited'})`), { label: `commit:${title}`, phase: title, agentType: 'general-purpose', model: MODEL })
  return ok
}

phase('Load')
const loaded = await agent(
  `Determine which ingredient dossiers still need to be written.\n1. Read ${DIR}/research/ingredients/_MASTER-INDEX.md and extract the full ingredient list: name, slug (Slug column), primaryClass, relevance.\n2. List the existing dossier files in ${DIR}/research/ingredients/ (use Glob "${DIR}/research/ingredients/*.md"). Ignore files whose name starts with "_".\n3. Return ONLY the ingredients whose slug does NOT already have a matching <slug>.md file — these still need research. Include name, slug, primaryClass, relevance, plus totalCount, existingCount, missingCount.`,
  { label: 'load:remaining', phase: 'Load', schema: LOAD_SCHEMA, agentType: 'general-purpose', model: MODEL }
)
const MISSING = (loaded && loaded.missing) ? loaded.missing : []
log(`Remaining to research: ${MISSING.length} (existing: ${loaded ? loaded.existingCount : '?'}, total: ${loaded ? loaded.totalCount : '?'})`)

const r1 = await runTier('Supporting', MISSING.filter(i => i.relevance === 'supporting'))
const r2 = await runTier('Fringe', MISSING.filter(i => i.relevance === 'fringe'))
const r3 = await runTier('Core', MISSING.filter(i => i.relevance === 'core'))
const r4 = await runTier('Other', MISSING.filter(i => !['supporting', 'fringe', 'core'].includes(i.relevance)))
const researched = r1.length + r2.length + r3.length + r4.length

if (SKIP_SYNTH) {
  log('Dossier writing complete for this run. PAUSING before synthesis (skipSynthesis=true) — evidence matrix not built.')
} else {
  phase('Synthesize')
  await agent(
    `All ingredient dossiers should now exist in ${DIR}/research/ingredients/ (excluding files starting with "_"). Build the synthesis by reading from disk:\n1. Glob ${DIR}/research/ingredients/*.md and, for each dossier, extract name, class, the adversarial evidence grade (A-D from the "## Evidence verification (adversarial)" section), top evidence tier, topical viability, and verdict. Use Grep to pull these efficiently.\n2. Write ${DIR}/research/ingredients/_EVIDENCE-MATRIX.md: a master table (Ingredient | Class | Relevance | Top evidence tier | Topical viability | Evidence grade | Verdict) sorted strongest-evidence first; plus a "Best-evidence shortlist" (A/B) and a "Hype watch" (D). Note the dossier count.\n3. Write ${DIR}/research/science/landmark-papers.md: landmark/pivotal papers + key reviews grouped by hallmark of skin aging, from the dossiers' sources.\n4. Update the "Dossier?" flags in ${DIR}/research/ingredients/_MASTER-INDEX.md to done for every ingredient that now has a dossier.\nDo NOT run git yet. Report how many dossiers you covered.`,
    { label: 'synthesize:matrix', phase: 'Synthesize', agentType: 'general-purpose', model: MODEL }
  )
  await agent(commitPrompt('evidence matrix, landmark papers, master-index update'), { label: 'commit:final', phase: 'Synthesize', agentType: 'general-purpose', model: MODEL })
}

return {
  model: MODEL || 'inherited',
  remainingAtStart: MISSING.length,
  researchedThisRun: researched,
  bySupporting: r1.length, byFringe: r2.length, byCore: r3.length, byOther: r4.length,
  synthesis: SKIP_SYNTH ? 'paused (skipped)' : 'done',
}
