# Repository Summary

A complete account of what this repository is, what it contains, how it is built, what the
data guarantees are, and what the training records actually look like. Every example below
is copied verbatim out of the shipped build in `data/`.

---

## 1. What the repository is

**One deliverable:** an instruction-response dataset of **7,200 examples** that teaches a
fiction-writing model *internalized writer thinking* — the decisions a writer makes while
generating, not post-hoc critique. It is designed to accompany pretraining on a corpus of
high-quality novels, so the supervision is about **craft procedure**, never about prose.

The reasoning covers the whole process, and each stage teaches the craft of that stage:

| Stage | Records | Deliverable the reasoning produces | Native libraries (65% of the stage) |
|---|---|---|---|
| `ideation` | 900 | a premise with an engine, the promise it makes, and the choice that tests it | `idea_generation`, `idea_shaping` |
| `outline` | 1,260 | a plan whose chapters have functions, positions, and prices | `outline_design`, `arc_mapping`, `scene_planning` |
| `drafting` | 4,320 | the decisions the specific chapter is written from | the eighteen drafting craft libraries |
| `revision` | 720 | a diagnosis and the order of passes that will fix it | `revision_craft`, `revision_diagnosis` |

Two hard content rules apply to every record:

1. **No prose, ever.** No illustrative passage, no sample line, no quoted dialogue, no
   "for example". The validator machine-checks this (no double quotes, no curly quotes, no
   exemplification phrases anywhere in the 7,200 responses).
2. **The outline is inference-time context.** At inference the caller supplies the novel
   outline being drafted; the shipped records contain no outline text and no outline
   metadata, so the model learns the reasoning rather than a particular story.

---

## 2. Repository map

| Path | What it is |
|---|---|
| `README.md` | the public description of the dataset, its guarantees, and how to regenerate it |
| `data/dataset.jsonl` | **the shipped dataset** — 7,200 records, shuffled |
| `data/transition_examples.jsonl` | 3,600 transition records (planning → writing handoff) |
| `data/pure_reasoning_examples.jsonl` | 1,800 arc-level reasoning records |
| `data/negative_examples.jsonl` | 1,800 forward-oriented trap records |
| `data/manifest.json` | seed, counts, and per-stage / depth / difficulty / strategy / category / lens / rule coverage |
| `data/README.md` | data dictionary and coverage notes |
| `docs/REPO_SUMMARY.md` | this document |
| `docs/IMPROVEMENTS.md` | the research-backed account of what was improved and why |
| `generator/build_dataset.py` | the assembler: composes instructions and responses, applies depth tiers and strategies, writes the datasets and manifest |
| `generator/stages.py` | the four process stages: instruction frames, tails, openers, context lines, stage routing (`ALLOWED_CATEGORIES`, `NATIVE_CATEGORIES`, `NATIVE_SHARE`), lens affinity |
| `generator/categories/` | **25 authored craft libraries** — the paragraph banks every response is composed from |
| `generator/rules.py` | the 260-rule craft registry; every authored paragraph encodes rules from it, every record is tagged with them |
| `generator/strategies.py` | 9 reusable reasoning moves (route comparison, backward reasoning, cost ledger, pre-mortem, constraints as conditions, weakest link, reader model, ordering by consequence, verification) |
| `generator/lenses.py`, `lenses_a.py`, `lenses_b.py` | the 17 cross-cutting lens pools (POV, concrete, character, scene, pacing, emotion, dialogue, humor, action, worldbuilding, continuity, plan obedience, reader trust, metaphor, prose, AI-pattern avoidance, style) |
| `generator/lenses_stage.py` | **planning-height lens banks**: the same lens keys reasoned at book level rather than scene level, used by ideation, outline and revision |
| `generator/situations.py` | outline conditioning (rendering the outline slice, the situation paragraph, the commitment paragraph) for the optional `--with-outlines` mode |
| `generator/outlines/` | the authored outline bank: **36 novels × 10 chapters** across 6 genre clusters, used only in `--with-outlines` mode |
| `generator/common.py` | shared helpers (deterministic distribution, sentence utilities, rule routing) |
| `validation/validate_dataset.py` | the contract: structure, type ratios, stage routing, coverage floors, balance, marker discipline, no-prose scan, word bands, uniqueness, strategy/lens/depth consistency |
| `training/convert_for_training.py` | converter to ChatML SFT rows with the system prompt and the stage brief |
| `.github/workflows/`, `scripts/lovable-coder/` | tooling scaffolding from the repository template, unrelated to the dataset |

Line counts: ~11,200 lines of generator + validation + training code; 45 MB of shipped
data.

---

## 3. How the dataset is built

The generator composes each record deterministically from authored banks, seeded once
(`--seed 20260924` for the shipped build), so a rebuild is reproducible.

**Composition pipeline per record:**

1. **Routing.** The record's stage is drawn from the type's stage distribution (transitions
   exist only at `drafting`). The stage then draws its category plan: 65% from its own
   libraries, the remainder from the libraries that also apply at that stage
   (`ALLOWED_CATEGORIES`). The validator fails the build if any record reasons about a
   library outside its stage — a brainstorming record about sentence rhythm, an outlining
   record about a character's hands.
2. **Craft item.** A problem, a trap, or an arc-level theme is drawn from the category
   library, with its opener and closer paragraphs.
3. **Lenses.** The record's lead lens comes from the stage's lens affinity plus the
   category's preferences; one to three lenses are used, and the lens paragraphs come from
   the **stage-height bank** (planning stages reason about character and pacing at book
   level; drafting reasons at scene level).
4. **Strategy.** Standard and deep traces carry one to three named reasoning strategies
   (terse traces carry none, by design).
5. **Depth tier.** Terse = one decision; standard = several decisions plus a strategy;
   deep = interacting decisions, a strategy, and a check. The response is padded until it
   meets the tier's minimum, and depth is upgraded if padding is heavy.
6. **Assembly.** Instruction = frame + craft problem + position in the work + instruction
   tail. Response = opener + craft paragraphs + lens paragraphs + strategy paragraphs +
   closer, then the handoff line for transitions.
7. **Tagging.** `rules` (from the category's rule set plus the lead lens fallback),
   `strategies`, `lenses`, `depth`, `difficulty`, `subcategory`, and the record id
   (`t-`/`r-`/`n-<category>-NNNN`).

**Reproduce the shipped build:**

```bash
python -m generator.build_dataset --size 7200 --seed 20260924
python -m validation.validate_dataset data/dataset.jsonl
```

`--with-outlines` conditions each record on one chapter of the 36-outline bank, for
experiments that want the outline inside the request. The shipped dataset does not use it.

---

## 4. Verified coverage of the shipped build

```
OK: 7200 records
  types: {'transition': 3600, 'reasoning': 1800, 'negative': 1800}
  stages: {'ideation': 900, 'outline': 1260, 'drafting': 4320, 'revision': 720}
  categories: 25, each used only at the stages it applies to
  stage ideation  libraries=4,  own-library share=0.65
  stage outline   libraries=12, own-library share=0.65
  stage drafting  libraries=18, own-library share=0.00
  stage revision  libraries=9,  own-library share=0.65
  rules exercised: 260 of 260
  strategies: {'verify': 1611, 'cost_ledger': 684, 'constraints_as_conditions': 683,
               'reader_model': 682, 'weakest_link': 682, 'pre_mortem': 682,
               'backward': 503, 'two_routes': 503, 'ordering': 498}
  lenses: 17 distinct; leads balanced 199-772
```

- Depths: `standard` 3,747 · `deep` 1,853 · `terse` 1,600; difficulty follows depth
  (`intermediate` / `advanced` / `foundational`).
- Word bands in practice: terse 190–351, standard 248–498, deep 287–600; mean 355 words;
  2.55M response words total.
- 218 distinct subcategories; all 7,200 instructions and all 7,200 responses globally
  unique.
- Category sizes 234–448 (the two revision libraries and the eight narrow drafting
  libraries sit at the bottom of the range, the cross-cutting ones at the top).
- Stage-routing leak check: **zero** planning-stage records carry drafting-height lens text
  (the leak that existed in the earlier build).
- Marker discipline: exactly one `Given the above, the scene begins.` in each of the 3,600
  transitions, always the final line, never in a reasoning or negative record; no
  transition exists outside `drafting`; the shortest reasoning before the marker is 184
  words.

---

## 5. The record format

```json
{
  "id": "t-setup_payoff-0238",
  "type": "transition | reasoning | negative",
  "stage": "ideation | outline | drafting | revision",
  "category": "setup_payoff",
  "subcategory": "load_bearing_plant",
  "instruction": "the writing situation and the craft problem",
  "response": "pure structural/conceptual craft reasoning",
  "depth": "terse | standard | deep",
  "difficulty": "foundational | intermediate | advanced",
  "lenses": ["outline_obedience", "scene", "pacing"],
  "strategies": ["backward"],
  "rules": [182, 183, 184, 185]
}
```

`instruction` is a 5–8 line second-person writing situation; `response` is the reasoning.
`lenses` are listed in canonical paragraph order with the lead lens first. `rules` lets a
training run weight, balance or ablate signal per craft rule without re-deriving the
mapping.

**Training conversion:**

```bash
python -m training.convert_for_training --path data/dataset.jsonl --out training/formatted
```

writes `train.jsonl` plus per-type files (`sft_transition.jsonl`, `sft_reasoning.jsonl`,
`sft_negative.jsonl`), each row carrying `id / type / stage / category / depth /
difficulty / strategies / messages`, with a system prompt describing the structural
writing planner and a `STAGE_BRIEF` line for the record's stage.

---

## 6. Examples from the dataset

### 6.1 Transition — drafting, the dominant training signal

`t-scene_construction-0603`, terse, 205 words, category `scene_construction`, lead lens
`scene`, ends with the single handoff line.

**Instruction**

> You are writing the scene in front of you, and the problem below has to be settled before the first line.
> Your story's central tension is about to become face-to-face, and the scene must carry the accumulated weight.
> The confrontation must be built as a contest with moves, counters, and a value shift, so that the meeting changes the relationship's position rather than merely displaying it.
> You are in the approach to the climax.
> The outline you have been given fixes what this chapter must accomplish, so the reasoning works inside those obligations rather than renegotiating them.
> Think the problem through to the end of the reasoning, then let the scene take over.
> Reason about the craft and stop there, with no prose on the page.

**Response**

> Before drafting, fix the scene's turn: what is different between these two after the encounter that was not different before. A confession extracted, a threat made credible, an alliance revealed as betrayal, the turn is the scene's reason for existing, and every beat before it is built to make the turn cost something.
>
> Give the scene's opening beat a job beyond entry. The first exchange should either advance a live question from the previous scene or establish the scene's own pressure, ideally both, so the reader is inside motion from the first line. An opening beat spent on orientation is a tax collected at the moment of highest attention.
>
> Watch for stretches where the writing has drifted entirely into abstraction, where decisions, meanings, and emotional states are discussed without any material anchor. Break such stretches with the concrete, and keep the abstract passage short enough to stay a movement within the scene rather than the scene's mode.
>
> Fix the entry positions and the destabilizing move, then write toward the moment the map changes. The scene's value will be measured in what each party now knows about the other, and in what the reader has learned that neither would say.
>
> Given the above, the scene begins.

Note what the record is and is not: the instruction supplies the *situation*, the response
supplies *decisions* (the turn, the opening beat's job, the abstraction risk, the entry
positions), and the last line hands off to writing. Nothing after it.

### 6.2 Transition — deep, with a strategy and a backward chain

`t-setup_payoff-0238`, deep, 463 words, `setup_payoff`, `strategies: ["backward"]`.

Instruction excerpt:

> You are drafting the scene this problem is standing in the way of.
> Your plot's resolution requires something established long in advance, and the establishment must do its work without announcing itself.
> The load-bearing plant must be introduced inside a scene with its own business, given multiple natural touches, and kept proportionately staged so its later weight lands as recognition.
> You are in the first third of the book.
> Reason your way through it in full, then begin the scene.

Response excerpt:

> Decide what the plant does in its first scene besides waiting. The detail must earn its presence: it characterizes someone, it solves a small local problem, it establishes the world's texture. The payoff will borrow all of this accumulated normalcy, and the plant's weight at the end will be proportional to how completely it belonged at the start.
>
> Build the innocent reading to be complete and lived. Recontextualization only detonates when the first reading was fully trusted, so the planting scenes must work honestly with no shadow of the second meaning required.
>
> Balance the ledger between plot and feeling. Plants and payoffs in the material register, objects, skills, facts, are easier to manage but land lighter than those in the emotional register, promises, wounds, grudges, debts of love.
>
> Decide the end first and reason backward. Ask what has to be true at the last line for the unit to have done its job, then what has to be true one step before that, and continue until the reasoning reaches the opening.
>
> […]
>
> Fix the plant's local job in its introduction scene, then write the scene around that job. The detail will ride in on the scene's own attention, and the climax will collect something the reader has already owned for hundreds of pages.
>
> Given the above, the scene begins.

### 6.3 Pure reasoning — brainstorming (ideation)

`r-idea_generation-0698`, deep, 409 words, `strategies: ["weakest_link", "backward"]`.

Instruction:

> You are looking for the engine of a story rather than its subject.
> You are deciding what the book owes the reader from its first page.
> How should the promises an idea makes be decided, scheduled, and paid across the whole book?
> Reason about the premise's load-bearing parts and stop when the story's engine is identified.
> Deliverable: a premise with an engine, the promise it makes, and the choice that tests it.
> Keep the reasoning structural. Do not draft prose, quoted lines, or invented detail.

Response excerpt:

> An idea becomes a story when someone wants something that costs them, and something makes the wanting dangerous. Test the material against that shape: who wants what, why now, and what failure would mean for them.
>
> The promise ledger is the bridge between an idea and a structure. Reasoning at this level means deciding what the reader is owed, when the book intends to pay, and what the final payment will cost the protagonist rather than the author.
>
> Pay the smallest promise first and the largest last. Interest in a book is maintained by a sequence of settled debts, and the final settlement has to be the one the whole structure was built to make possible.
>
> Decide which promise the book will deliberately leave unsettled, and make that choice at the level of the idea. Ambiguity works as an ending when it is a decision the book has prepared for, and reads as evasion when it is the accident of an unplanned structure.
>
> Rank the decisions by how expensive they are to reverse later. Make the irreversible ones here, in the reasoning, and leave the cheap ones to be discovered while drafting.
>
> Work from the outcome the book needs at the far end of this material, and treat the reasoning as a path that must arrive there. Forward motion tends to lower stakes as it searches for what is dramatic; backward motion shows where the story has to be planted for the arrival to be earned.
>
> Treat withheld information as a debt with terms. The reader will carry an unanswered question across a long book only if the plan keeps showing that the question is live, and any question the plan forgets is experienced as an error rather than as a mystery.

This is the "how" the user asked for at brainstorming: not "brainstorm a premise" but the
moves that make an idea structural — the promise ledger, payment order, the deliberate
unsettled question, reversibility ranking, backward planting.

### 6.4 Pure reasoning — outlining

`r-outline_design-0035`, standard, 297 words, `strategies: ["ordering"]`.

Instruction:

> You are building the plan: the movements, the turns, the thread schedule, and the ending the book has to earn.
> You are designing a structure that has to argue with itself.
> How is a theme built into a novel's structure rather than stated in its text?
> Reason at the level of structure, and stop when the plan contains decisions rather than intentions.

Response excerpt:

> Deciding the architecture means deciding what the reader is waiting for at every point in the book. That is a scheduling problem: anticipation has to be created, maintained, and discharged, and every chapter does some of all three.
>
> A theme carried by structure is a pattern of pressure: the same test applied to different characters, the same mistake made at increasing cost, the counter-argument given its best scene. The plan embodies the question in what it makes people do.
>
> Give the counter-position its own scenes and its own competence. A theme tested only against weak opposition produces agreement, and agreement is where a novel's argument stops being dramatic.
>
> Make the resolution of the theme a decision rather than a conclusion. The final movement should force the protagonist to act on what they have learned, which is what converts a book's idea into its ending.
>
> Decide the sequence of work before deciding the content. Knowing that one choice forecloses another changes which choices are available, and reasoning out of order produces plans that cannot be executed in the order they were imagined.

### 6.5 Pure reasoning — scene planning at outline height

`r-scene_planning-0430`, deep, 422 words, `strategies: ["ordering", "two_routes"]`. This is
the library that answers "outlining must build books with good stories".

Instruction:

> You are designing the architecture, and the decisions at stake govern the whole book rather than one chapter.
> You are designing the physical facts of a scene that the story depends on.
> How is a major scene staged so that it turns the story rather than merely impressing the reader?
> Lay out the architecture and the tradeoffs, and end with the plan a chapter can be drafted from.

Response excerpt:

> An outline is a schedule of pressures rather than a list of events: decide where the book spends its setup, where it turns, and what each chapter is responsible for handing on.
>
> A staged scene is built from four decisions: the space and its constraints, the positions and capabilities of everyone present, the moment the terms change, and the bill that comes due afterward. Staging without a turn is a performance, and a turn without staging is an announcement.
>
> Establish capabilities before the scene depends on them. A resource that appears at the moment of need discounts every earlier difficulty, so the plan should place its introduction where the reader can verify it.
>
> Decide where the reader's attention should be at each stage of the scene. Attention is a budget: a staged scene works when the plan indicates what matters at the beginning, what changes at the turn, and what the reader should be looking at when it ends.
>
> Sequences have shape: one question, one crest, one entry state, one exit state.

### 6.6 Pure reasoning — revision

`r-revision_diagnosis-1578`, standard, 318 words, `strategies: ["ordering"]`.

Instruction:

> You have a drafted chapter that is not yet doing its job, and the revision decisions are ahead of you.
> You are reworking a draft that mostly works.
> How is a draft repaired so that the fixes do not damage what already works?
> Reason about the draft as a system, and settle what the revision is allowed to touch.

Response excerpt:

> A drafted chapter that is not working usually has one cause and several symptoms. Reasoning here means finding the cause, then deciding which changes are allowed to follow from it.
>
> Repair is bounded by two lists: what must change and what must survive. Writing both before opening the file is what keeps a structural repair from becoming a rewrite that loses the draft's best material and the writer's confidence along with it.
>
> Make one structural change at a time and re-read the chapters it touches before making the next. Parallel changes produce a manuscript whose parts no longer fit, which is a larger problem than the one the pass began with.
>
> Stop when the criteria are met rather than when the pages stop improving. Further passes at that point change the book rather than repairing it.
>
> Separate what has to be decided now from what can be decided in the draft. The reasoning should carry only the decisions that the writing cannot make for itself, because decisions deferred to drafting are usually the ones drafting is equipped to make.

### 6.7 Negative — brainstorming trap, forward-oriented

`n-idea_generation-0856`, deep, 389 words,
`strategies: ["constraints_as_conditions", "pre_mortem"]`.

Instruction:

> The idea keeps producing atmosphere and no decisions, and you are about to build on it anyway.
> Your planning keeps producing history, systems, and geography rather than events.
> The world is carrying the book. The setting is intricate and internally consistent, the exposition is already written in the notes, and the plot exists to tour it, so the reader is asked to admire a construction rather than follow a person under pressure.
> You are in the idea's development.
> Treat the material as a proposal that has to survive scrutiny before anything is built on it.
> Work past the weak shape and settle what the idea's engine will be before anything is outlined.

Response excerpt:

> This is a trap that is normally discovered in a finished draft, when the fix is a rewrite. Reasoning about it now, at the level of the idea, is the cheapest possible place to catch it.
>
> Reason past it by converting invention into pressure. Every element worth keeping should be able to answer what it makes difficult, expensive, or forbidden for the protagonist, and elements that cannot answer are background rather than story.
>
> Books built around their worlds produce readers who remember the setting and not the story, or who leave early because nothing has been demanded of anyone. Every chapter spent establishing the world is a chapter not spent creating anticipation, and no amount of internal consistency repairs a middle with no pressure in it.
>
> When the material is rich and the story is unclear, prefer narrowing. A smaller, more particular premise is easier to plan, easier to write, and easier to end well.
>
> Reason past it while planning by starting from a person under an obligation and letting the world surface only where it obstructs them. The invention then earns its place by making the story's problem harder, and the reader learns the world by watching someone struggle inside it.

The trap → downstream damage → replacement reasoning structure, with every sentence framed
"while planning" / "reason past it": forward-oriented, never a critique of pages already
written.

### 6.8 Negative — outlining trap

`n-scene_planning-0296`, terse, `scene_planning`.

Instruction excerpt:

> You are outlining, and the plan keeps resolving into a shape you have seen before.
> Your scene briefs specify what characters will say and where they will stand.
> The scene plan has become a transcript of the draft. Entrances, gestures, and exchanges are all fixed, so drafting turns into transcription, and the writing cannot respond to what the scene actually does, which is where a manuscript's best material usually comes from.
> You are in the scene brief's detail level.
> The plan is being made now, and the drafting stage will inherit whatever is decided here.

Response excerpt:

> A weak structure is usually a defensible idea applied too purely: the shape is recognisable, so it feels safe. The damage appears as a book that reads competently and moves nobody.
>
> Reason past it by asking, for each line of the brief, whether the drafting stage could decide it better with the scene in front of it. If it could, the line belongs to the drafting stage, and the plan keeps the obligations instead.
>
> Over-specified scene plans produce flat manuscripts. The writing has no decisions left, so the small inventions that make a scene feel inhabited never happen, and the revision stage has to create life inside a structure designed as a transcript of a scene that was never actually written well.

### 6.9 Negative — revision trap

`n-revision_craft-1774`, standard, `strategies: ["constraints_as_conditions"]`.

Instruction excerpt:

> You are reworking a chapter and the shortcut below would make the draft look finished sooner.
> The draft contains scenes you are defending because they were expensive to write.
> The revision is arranged around the material that should be removed. Scenes are given new functions, transitions are built to reach them, and explanations are added to justify them, so a fixable draft becomes a structure that has to be protected.

Response excerpt:

> The shortcut below produces a manuscript that passes a quick read and fails a slow one. It is refused here, at the level of cause, before the pass begins.
>
> The pull is the sunk cost of work already done, and the correction is a decision about function rather than about effort. Reason about what each scene contributes to the book's pressure and cut by that standard, not by how long it took.
>
> Manuscripts revised around their weakest material keep the faults and add explanations. The book becomes longer, its pressure dilutes across scenes that exist to justify other scenes, and the revision that would have fixed the structure in a week becomes a rewrite in a month.
>
> Reason past it by deciding the book's required material first, from the ending backward, and treating everything else as removable. Cuts made on structural grounds do not need defending, and they make every remaining scene stronger.

### 6.10 Same lens, two different heights

The cross-cutting lens banks exist in a scene-height version and a planning-height version.
Same lens key, `character`:

*Planning height (`lens_bank('ideation', 'character', …)`, used by ideation, outline and
revision):*

> Decide the cast's wants before the plot's needs. Every principal character should want
> something independently of the story's problem, because those independent wants are what
> supply collisions when the main pressure is briefly quiet.

*Drafting height (used at the drafting stage):*

> Decide what each character wants in this chapter, what they are willing to risk for it,
> and what they will not do even to succeed. The boundary is where the character is
> legible, and it is the part of the design most often left implicit.

That separation is what stops a brainstorming record from reasoning about a scene's beats
and stops an outline record from arriving with line-level lens text — the leak the
validator now checks for explicitly (zero occurrences in the shipped build).

### 6.11 Optional outline mode (not part of the shipped build)

With `--with-outlines`, the request carries one chapter of the authored outline bank and
the record gains `outline_id` / `chapter` fields. Verbatim fragment of such a request:

> Novel outline for the chapter you are about to write:
> TITLE: Bitterwater -- standalone, western, revenge and debt.
> POV AND DISTANCE: single close third, past tense, the tracker.
> PREMISE: A tracker carrying a dead man's debt returns to the town that issued it, and the three people who paid the bounty are the three who owe him the truth.
> …
> TARGET CHAPTER 7 OF 10 -- His name. Function: payoff of the tracker's warrant.
> REQUIRED BEATS: Rell finds the original warrant on file with the wrong man's name and his own added; he steals the sheet and does not destroy it.
> STATE ENTERING THE CHAPTER: council in three days, evidence in hand.
> STATE THE CHAPTER MUST HAND ON: he holds the proof of his own crime and another man's, and the deed to the water.
> CRAFT PRESSURE FOR THIS CHAPTER: how the chapter serves the plan's obligations.

The shipped dataset has none of this: `data/dataset.jsonl` records carry no outline text
and no outline fields.

---

## 7. Guarantees enforced by the validator

Run `python -m validation.validate_dataset data/dataset.jsonl`. It checks, and fails the
build on:

1. **Structure** — required fields, known stage, type, depth, difficulty, category;
   `difficulty` consistent with `depth`.
2. **Routing** — the record's category is allowed at its stage; each stage draws at least
   half its records from its own libraries; per-stage library balance within 1.9× (small
   groups skipped as rounding noise).
3. **Type ratios** — 50/25/25 within ±2 points; transitions only at `drafting`, and all of
   them there.
4. **Coverage** — every category used by a type's stages appears in that type; a floor of
   roughly 0.15% of the dataset per type-category and per stage-category cell.
5. **Marker discipline** — exactly one handoff line per transition, as the final line, with
   at least 150 words of reasoning before it; no marker in other types.
6. **No-prose scan** — no double quotes, no curly quotes, no exemplification phrases.
7. **Word bands** — per-depth minimum and maximum, including the outline-mode allowance.
8. **Uniqueness** — all instructions and all responses globally unique.
9. **Strategy and lens discipline** — terse records carry no strategy; a record's lens list
   is lead-first in canonical order; the record carries the lens for its stated craft
   pressure.
10. **Rule coverage** — all 260 rules exercised somewhere in the dataset.

---

## 8. Git state

```
5af4577  Tighten stage routing to stage-appropriate libraries and document the stage craft
543f508  Stage-locked story craft: brainstorming, outlining, writing, revision libraries
d2feac2  Improve dataset quality and cover the whole writing process (7,200 records)
```

Branch `arena/01a0d3cd-kaggle-reasoning-dataset`, pushed to `origin`. The shipped `data/`
matches the generator at `5af4577`: rebuild +
`python -m validation.validate_dataset data/dataset.jsonl` is green.
