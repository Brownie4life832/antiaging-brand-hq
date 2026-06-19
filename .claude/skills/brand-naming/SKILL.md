---
name: brand-naming
description: >-
  Run a brand- or product-naming exercise the David Placek / Lexicon Branding way
  (Pentium, PowerBook, BlackBerry, Swiffer, Sonos, Azure, Vercel, Windsurf,
  Impossible Burger). Use when the user wants to name (or rename) a brand,
  company, product, or feature; generate name candidates; build a naming brief;
  or screen/choose a name. Triggers on "name the brand", "brand name ideas",
  "help me name", "naming exercise", "come up with names", "rename".
---

# Brand naming — the Placek / Lexicon method

> Source: David Placek, founder of Lexicon Branding (4,000+ naming projects). Full
> digest with the A–Z sound-symbolism chart and the brand-story case file:
> [`reference/placek-method.md`](reference/placek-method.md).

## The philosophy in five lines

1. **Nothing you build is used more often or for longer than the name.** It compounds. Get it *right*, not just *good*.
2. A right name does three jobs: **gets attention → holds it (processing fluency) → surprises** (not comfortable, not popular, not descriptive).
3. Aim for **"surprisingly familiar"**: easy enough for the lazy brain to process, odd enough to make it stop.
4. **Don't describe the product — start a story.** Don't make a statement. (Swiffer ≠ "ReadyMop"; Azure ≠ "CloudPro".)
5. **"There is no power in comfort."** If the team is comfortable, you don't have the name yet. Look for **polarization** — argument is a sign of strength.

## The three phases

Placek's process is **Identify → Invent → Implement.** Run them in order.

---

### Phase 1 — IDENTIFY (the brief)

Forget the word. Start with **behavior and experience**, not "positioning / mission / values."

**Run the Diamond exercise** (his one universal exercise). Draw a diamond; answer the four points — and spend most time on the last:

- **▲ WIN** — how do *we* define winning here? (Get specific; everyone in the room answers differently — surface that.)
- **◄ What we HAVE to win** — assets/strengths already in hand.
- **► What we NEED to win** — gaps to close (talent, proof, trust… and "the right name").
- **▼ What we have to SAY to win** — *the engine of the name.* What must the market understand/feel? Push into **metaphor, behavior, experience**.

Then map the **landscape**: list competitors' names + the language they all use. You don't yet know where you're going, but you know **you're not going there** (the "sea of sameness").

Output a **creative framework** — a *window* to search through (not a narrow objectives list). It should open up breadth: different experiences, personalities, sound textures.

> This repo's filled-in example: [`/brand/naming/creative-brief.md`](../../../brand/naming/creative-brief.md).

---

### Phase 2 — INVENT (generate — a lot)

**Quantity leads to quality.** 200 names is not enough — get to **1,000–1,500+** ideas and *directions*. Most will be "trash"; that's the job. **Suspend judgment. Speculate, don't evaluate** ("what could this name *do* for us?").

**Work in small teams, never big brainstorms.** Brainstorms die from peer pressure and premature evaluation. Use **two- or three-person teams** (or, solo, run yourself through several distinct briefings).

**The three-teams trick (the most powerful move):** give each team a *different* briefing so they escape the category's clichés.
- **Team 1** knows the real assignment in full.
- **Team 2** is *disguised* — same emotional brief, but told they're naming something adjacent (a fragrance, a car, a material, a retreat).
- **Team 3** is *off-category* entirely (name a bicycle, a wine, a watch).
> Most winning names come from Teams 2 and 3 — Windsurf came from "list everything about dynamic flow/sport," not from "name an AI IDE."

**Make the intangible tangible.** If the product is abstract (software, "code"), force it into a physical world (flow → wind/surf) and name *that*.

**Go treasure hunting** ("Ship of Gold" — map the whole sea, then dive). Mine databases:
Latin & Greek roots · Greek/Roman/Norse/etc. mythology · the periodic table · minerals & gems · constellations & light phenomena · botanicals · world languages · expressions/idioms · adjacent fields (flip through hunting/flying magazines and steal words). **Force synchronicity** — connect two unrelated fields.

**Engineer sound symbolism** (every letter has a feeling — full chart in the reference):
- **V** = most *alive / vibrant* (Vercel, Corvette, Viagra) · **B** = *reliable* (BlackBerry) · **S / Z / V** = *noisy*, a strong signal that cuts through (Sonos, Azure) · **X** = *fast, crisp, innovative* · **P / T / K** (plosives) = *sharp, energetic, precise* · soft **L / M / N** + long round vowels = *calm, smooth, soothing*.
- **Front vowels** (ee, i) feel *small/light/fast*; **back vowels** (o, u, ah) feel *large/round/substantial*.
- **Compounds multiply** associations — PowerBook, BlackBerry, Windsurf: 1+1 = 3.
- **Coinage** works when built from familiar units (ver+cel, son+os, pent+ium); palindromes are a bonus (Sonos).

---

### Phase 3 — IMPLEMENT (screen & choose)

From thousands, sift to ~10–15, clear trademark, then present.

**Screening rubric** (a right name clears all of these):
- **Original in the category** · **processing-fluent** (easy to say/spell) · **surprising/not descriptive** · **sound-symbolically apt** · **headroom** across the range · **distinctive** vs. the landscape · **clearable** (trademark; domain is *secondary* — a prefix/suffix or `.ai`/`.co` is fine, don't over-pay for the exact `.com`).

**Don't trust "I'll know it when I see it"** — you almost never will; the bold, right name feels uncomfortable first.

**Two field drills to evaluate without bias:**
1. To colleagues: not "what do you think of this name?" but **"what could this name *do* for us?"**
2. To friends: **"A new competitor just launched, they're called ____ — what do you think?"** You learn what the name *does*, not their taste. The signal you want: *"I don't know much about them, but they're not like the other guys."*

**Use polarization as a compass.** A name half the team loves and half resists usually has energy (Andy Grove chose "Pentium" over "ProChip" *because* it polarized). Comfortable = not there yet.

**Build prototypes** for the finalists — name on a cap/tube, a mock headline/ad — so deciders see the *experience*, not a word on a list. Arm your champion with the rationale to sell it upward.

---

## How to run it here

- **Solo / fast (founder mode):** do the Diamond (Phase 1), then generate across several self-briefings until you pass ~1,000 ideas; suspend judgment; screen with the rubric + the two drills; choose by polarization.
- **At scale (this repo):** the workflow `placek-naming-exercise` runs ~13 generation "teams" (insider + disguised + database) → screen → adversarially verify → curated 100. Re-run it with a new `creative-brief.md` to regenerate.

## Output format

Deliver candidates as a tagged, scored list — for each: **name · what it could do (rationale) · positioning lane it serves · sound-symbolism note · type** (real-word/compound/coined/classical/foreign) · **boldness** · any risk. Surface a short **bold/polarizing shortlist** separately — those are the ones to fight for.
