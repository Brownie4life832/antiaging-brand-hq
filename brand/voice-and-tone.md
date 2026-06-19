# Voice & Tone

> **Status:** Working draft v0.1 (2026-06-18) — **(name / story / positioning OPEN).** Voice cannot be finalized until positioning is chosen; the brand name and story are also undecided. Use the framework below to write copy in the interim, then run the `generate-guidelines` brand-voice skill against our best copy once positioning lands.

## Why this doc is a framework, not a finished voice

Voice is downstream of positioning, and positioning is still **open**. The same brand fact ("a barrier-repair cream backed by evidence") sounds very different depending on whether we lead with corrective results, science/longevity, clean/transparency, barrier health, or an age-positive stance. So this doc does two things:

1. **Name-agnostic basics** that hold true under *any* positioning (clarity, claims discipline). Use these now.
2. **A decision framework** that maps each candidate positioning to the voice it implies, so voice can be locked the moment positioning is.

Throughout, refer to the brand only as **"the brand"** or **[BRAND]**. Do not assume a name, story, or metaphor.

## Name-agnostic basics (true under any positioning)

These are non-negotiable regardless of which direction wins.

**Clarity**
- Write to be understood on first read. Plain language over jargon; explain a term the first time it appears.
- One idea per sentence; lead with the benefit, then the *why*.
- Name ingredients and say what they do, in concrete terms.

**Claims discipline**
- Say what's proven — and admit what isn't. Distinguish evidence levels.
- No drug-like or unsubstantiated claims ("cures," "erases wrinkles," "boosts collagen 300%"). See the claims guardrail in [`../CLAUDE.md`](../CLAUDE.md).
- Avoid hype words ("miracle," "revolutionary," "game-changer") and exclamation-point inflation under every positioning — they read as desperate and invite regulatory scrutiny.

**Reader respect**
- Speak *to* the reader as a peer ("you," "your skin"), not down to them.
- Don't manufacture insecurity to sell. (How far this goes depends on positioning — see below.)

**Consistency**
- Use terms the same way every time (see [`glossary.md`](glossary.md), which should be rebuilt once name/story/positioning are set — its current entries assume an abandoned story).

## Positioning options → voice implications

The founder is choosing among the directions below. Each is shown with the competitive crowding from the research and the voice it would imply. **None is the chosen direction.** The crowding notes describe the market, not us.

| Positioning option | Competitive landscape | Voice it implies |
|---|---|---|
| **Results / corrective ("fight aging")** | Crowded — most of the active/clinical category lives here. | Confident, precise, before/after-driven; performance language. Risk: claims overreach and sameness. |
| **Pro-aging / age-positive** | Relatively unoccupied — **an option with low competition.** | Warm, affirming, non-shaming; reframes aging as normal, not a defect. Risk: can read as soft if results aren't also evidenced. |
| **Science / longevity-led** | Growing and increasingly contested as "longevity" trends. | Rigorous, citation-forward, mechanism-explaining; teacherly. Risk: cold/clinical if unchecked. |
| **Clean / transparency-led** | Very crowded and somewhat commoditized. | Plain-spoken, ingredient-honest, "here's exactly what's in it." Risk: undifferentiated; "clean" fatigue. |
| **Barrier-health-led** | Less crowded than "clean" or "corrective"; aligns with the evidence-grounded product logic. | Calm, physiology-literate, practical; focuses on skin function over fear. Risk: niche unless made accessible. |

How to read this: pick the positioning first, then adopt the matching voice column. The pro-aging row's low competition is a *market observation*, not a recommendation.

## Tone shifts by context (apply after positioning is chosen)

These channel adjustments hold across positionings; calibrate their warmth/intensity to the chosen direction.

- **Product pages:** confident + precise. Lead with the benefit and the *why* (the science), in plain language.
- **Education / blog:** generous teacher. Demystify ingredients. Cite. No condescension.
- **Social:** a little more relaxed and human, still grounded and accurate.
- **Email:** personal and direct, like a note from a knowledgeable person.
- **Ads:** evocative + concrete. One idea, clearly. Never desperate.

## Language rules

**Do**
- Speak to the reader as a peer ("you," "your skin").
- Name ingredients and explain what they do.
- Say what's proven — and admit what isn't.
- Keep terminology consistent (see [`glossary.md`](glossary.md)).

**Don't**
- Make unsubstantiated or drug-like claims ("cures," "erases wrinkles," "boosts collagen 300%") — see claims guardrail in [`../CLAUDE.md`](../CLAUDE.md).
- Over-use exclamation points or hype words ("miracle," "revolutionary," "game-changer").
- Sound like every other clinical-white skincare brand.
- Lock in fear/shame *or* warmth as a blanket rule before positioning is decided — how much of either is appropriate depends on the chosen direction (e.g., a results/corrective stance tolerates more "fight" language; an age-positive stance forbids shame entirely).

## Signature words & phrases

**Open — do not finalize a lexicon yet.** The product-specific vocabulary depends on the (undecided) name, story, and positioning. Once those are set, build the signature lexicon in [`glossary.md`](glossary.md).

Candidate functional terms that are safe under most positionings (because they describe the product, not a metaphor): *barrier, ceramides, cholesterol, fatty acids, resilience, repair, renewal, hydration.* Validate against the chosen positioning before adopting.

Avoid (overused category clichés regardless of direction): "glow up," "turn back the clock," "ageless," "fountain of youth," "anti-wrinkle."

## Quick before/after (claims discipline, positioning-neutral)

The fix below corrects a hype/claims problem without committing to a story or positioning. Tune the framing to the chosen direction.

- ❌ "Erase years of wrinkles with our miracle anti-aging serum!"
- ✅ "A Renewal Serum built around a ceramide + cholesterol + fatty-acid barrier complex — formulated to help support your skin's barrier, with claims we can stand behind."

## Related

- Words & terms → [`glossary.md`](glossary.md) *(rebuild once name / story / positioning are set)*
- Apply this voice automatically → `enforce-voice` skill
