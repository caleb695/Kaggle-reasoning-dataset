# Dataset improvement report

This document records what was changed to make the dataset train better behavior, why
each change was made, and what it looks like in the data. It is written for whoever
maintains or retrains on this dataset.

Current build: **7,200 records**, seed `20260924`, shipped in `data/`. Stage coverage:
900 brainstorming, 1,260 outlining, 4,320 drafting, 720 revision, across 25 libraries.

---

## 1. What the research said, and what was done about it

| Finding | Source | Change made |
|---|---|---|
| Quality and reasoning depth beat volume; long shallow traces dilute the signal | NVIDIA, *Front-Loading Reasoning* (2025); *Awesome-Long-CoT* (2025) | Deep traces are a first-class tier, not an occasional long sample: every category can produce terse, standard, and deep records |
| Diversity should span prompt phrasing, difficulty, response length, and reasoning strategies rather than topics alone | *NaturalThoughts* (2025); SFT data guides (2025-2026) | Four independent axes added: stage, depth, difficulty, and reasoning strategy, each balanced and tagged |
| Reasoning-strategy diversity transfers better than topic diversity | *NaturalThoughts* (2025) | Nine named strategies authored as reusable reasoning moves and attached to a share of every record |
| Overly long reasoning traces accumulate noise and produce verbose inference | *CAC-CoT* (EMNLP 2025 Findings); LIMO, s1K | Depth tiers plus an explicit stop condition in the tails, and terse tiers that never carry a strategy paragraph |
| Verification steps inside traces improve outcomes | SFT CoT guides (2026) | A `verify` strategy that leaves a check the draft can run, present in about 22% of records |
| Framework-style questions plateau; rephrasing and de-clumping are needed | Synthetic-SFT guides (Toloka, 2024) | Instruction frames, tails, openers, and contracts all drawn from banks, with uniqueness enforced on instruction and response text |
| Apparent coverage is not coverage: a dataset can be large and homogeneous | SFT quality guides (2026) | New coverage axis (ideation, outline, revision) with a validator check that every stage x type slice exists and every category appears inside each one |

Earlier research that shaped the base build (next-chapter prediction with reasoning
traces, hierarchical planning traces, dynamic outlining, continuity ledgers) still
applies and is summarized in the repository README.

---

## 2. Process coverage: the four stages, each with its own craft

The dataset previously reasoned only about the drafting moment. It now covers the whole
process, and each stage teaches **the craft of that stage** rather than a process note
about it: brainstorming reasons about how to generate an engaging story, outlining reasons
about how to build a structure that holds, drafting reasons about how to write the chapter
against an outline, revision reasons about how to diagnose and repair what exists.

| Stage | Records | The work the examples teach | Libraries it reasons with |
|---|---|---|---|
| `ideation` | 900 | brainstorming: finding an idea that makes a story, with someone to follow, something they want badly, and trouble that will not let them have it | `idea_generation`, `idea_shaping` |
| `outline` | 1,260 | outlining: building the story so it works, deciding what happens, why it happens, and what it costs | `outline_design`, `arc_mapping`, `scene_planning` plus the structural libraries |
| `drafting` | 4,320 | writing: how the chapter in front of you gets written, inside the outline you were given | the eighteen writing craft libraries |
| `revision` | 720 | revising: what to change, what to keep, and the order to work in | `revision_craft`, `revision_diagnosis` |

Stage routing is enforced rather than suggested: `generator/stages.py` holds
`ALLOWED_CATEGORIES` and `NATIVE_SHARE` per stage, and the validator fails the build if a
record reasons about a library outside its stage (a brainstorming request about sentence
rhythm, an outlining request about a character's hands). Brainstorming and revision reason
with nothing but their own libraries; outlining keeps the structural libraries alongside
its own; writing draws on all of them, because that is where the craft converges.

The stage voice is enforced too. Instruction frames, tails, response openers, context lines,
and the lens paragraphs are written as the activity itself: brainstorming frames sit in the
moment an idea is being found, outlining frames sit above the story deciding what happens
and why, writing frames sit at the desk with the chapter's requirements in front of them,
and revision frames sit in front of a draft that is not working yet. The planning lens pools
in `generator/lenses_stage.py` are authored per activity, so a brainstorming record reasons
about what makes a story engaging rather than about scene construction. Each stage also has its own instruction frames, tails,
context lines, and response openers, and `generator/lenses_stage.py` gives the cross-cutting
lens dimensions a planning-height paragraph bank, so ideation and outlining reason about
character, pacing, and continuity at the level of the book rather than the level of a scene.

What each stage's craft actually covers:

- **Brainstorming (`ideation`)** — what makes a story engaging and how to build it on
  purpose; premise engines and the demand a premise creates;
  protagonist choice by damage rather than capability; wants and needs; conflict generation
  from opposition with a legitimate claim, structural obstacles, and mutual exclusivity;
  stakes built as a ladder of currencies with something the protagonist cannot replace;
  hooks and opening promises; tone as contract; ending direction and its price; theme
  stated as a question with a live counter-position; pitch compression as a diagnostic;
  generating and selecting among candidate versions; capacity checks for novel length.
- **Outlining (`outline`)** — movements defined by changes of condition; chapter functions;
  thread schedules with setup and payoff positions; escalation ladders that charge rather
  than threaten; ending-first design and the conditions the ending requires; protagonist,
  antagonist, relationship, knowledge and stakes arcs and their alignment; act breaks and
  the midpoint reversal; climax design as a decision with a price; mystery trails and
  misdirection; scene purpose, turns, entry and exit; sequences with a question and a
  crest; set-piece staging with a cost and a consequence; scene budgets and ordering.
- **Drafting (`drafting`)** — the eighteen craft libraries: scene construction, POV and
  perception, concrete grounding, prose discipline, metaphor and imagery, emotion, dialogue,
  action, worldbuilding, characterization, humor, pacing, reader trust, AI-pattern
  avoidance, plan obedience, continuity, tension, momentum.
- **Revision (`revision`)** — repair: cause before symptom; scene and chapter audits; cut, merge,
  relocate, strengthen; pass order; repairing slow openings, sagging middles, flat endings,
  confusing sequences, unlikeable or undriven protagonists, missing motivation, and
  overwritten drafts; protecting the material that carries voice; criteria for stopping.

Drafting stays dominant, as requested. Transition records exist only at the drafting
stage, because the handoff line separates planning from writing and there is no writing
to begin at the other stages.

Three new authored craft libraries carry the stage-native reasoning, alongside the 18
existing ones (21 categories total):

The seven stage-native libraries, with the traps that give the negative records their
content:

| Library | Stage | Craft | Traps |
|---|---|---|---|
| `idea_generation` | ideation | premise engines, forced choices, collisions, theme as question, idea tests, promise ledgers | genre-as-idea, theme-as-message, world-as-substitute |
| `idea_shaping` | ideation | protagonist choice, want/need, conflict generation, stakes ladders, hooks, tone, ending direction, pitch, candidate selection | premise-love, twist-before-story, borrowed stakes, theme debate, indecisive protagonist |
| `outline_design` | outline | movements, chapter functions, thread schedules, escalation ladders, ending-first design, subplot convergence, pressure contour | event-list outline, options kept open, outline dictating prose |
| `arc_mapping` | outline | protagonist, antagonist, relationship, knowledge and stakes arcs, act breaks, climax, mystery, resolution | arc as announcement, escalation by inflation, twist as substitute |
| `scene_planning` | outline | scene purpose, turns, entry and exit, sequences, set pieces, ordering, scene budgets | beat sheet as script, scenes added for length, reveal before setup |
| `revision_craft` | revision | cause before symptom, cut first, protect what works, pass order, continuity after change | polish before repair, patch and keep, the infinite final pass |
| `revision_diagnosis` | revision | symptom-to-cause mapping, scene and chapter audits, pacing, character, clarity and ending repair, line pass | explaining to repair, cutting the wrong thing, smoothing voice |

Each library carries several moves (families of craft paragraphs), four to seven problems
with openers and closers, three to five traps with damage and replacement reasoning, three
discipline checks, two arc-level themes, and three principles, in the same schema as the
existing libraries, so every stage can produce reasoning, negative, and transition records.

---

## 3. Reasoning strategies

Nine strategies are authored as generic reasoning moves and attached to a share of
records (`strategies` field), so the traces teach procedure rather than phrasing:

`two_routes` (compare options, choose on stated grounds), `backward` (reason from the
ending), `cost_ledger` (price every decision), `pre_mortem` (assume the failure, find
where it shows), `constraints_as_conditions`, `weakest_link`, `reader_model`,
`ordering`, `verify` (leave a check the draft can run).

Counts in the shipped build: `verify` 1,607; the remaining eight between 498 and 687
each. Terse records carry none, standard records one, deep records one or two.

---

## 4. Depth, difficulty, and length control

| Depth | Records | Response words | Structure |
|---|---|---|---|
| `terse` | 1,573 | 190-343 | one decision, one lens, no strategy |
| `standard` | 3,771 | 245-506 | several decisions, a strategy, two or three lenses |
| `deep` | 1,856 | 281-625 | interacting decisions, a strategy, a check, three lenses |

The difficulty tag follows the tier (`foundational`, `intermediate`, `advanced`), and the
validator enforces that the response length sits inside the band for its tier. This is
the anti-verbosity control: a model trained only on long traces learns to be long.

---

## 5. Prompts

Instructions are assembled from banks so no two are identical, and they now state the
work explicitly:

1. **Stage frame** — where the writer is standing (5 variants per stage and type).
2. **Craft item** — the problem, trap, or arc-level question.
3. **Stage context line** — how the reasoning relates to the material, and at the
   drafting stage, the fact that the caller's outline fixes the chapter's obligations.
4. **Tail** — what the reasoning has to produce, drawn from eight variants per stage and
   type.
5. **Deliverable line** — the artefact the reasoning should end with (50% of records).
6. **Contract** — one of six phrasings of the no-prose rule, in every instruction.

Instruction length is 63-170 words (median 110), and every instruction is unique.

---

## 6. What the validator now enforces

- 7,200 records inside the 6,000-8,000 band, 50/25/25 by type.
- Every stage x type slice non-empty; every category present in every type; every
  stage x category cell inside each type above a floor; transitions all at drafting.
- Exactly one handoff line, final line, only in transition records, with at least 150
  words of reasoning before it; no other record contains the marker or the phrase.
- No double quotes, no curly quotes, no exemplification phrases anywhere.
- Global uniqueness of ids, instructions, and responses.
- Depth in range for its tier, difficulty consistent with depth, strategies drawn from
  the registry with their paragraph actually present in the response, no strategies on
  terse records, all nine strategies used.
- Valid lenses, canonical order after the lead lens, all 260 rules exercised.
- Optional outline-mode checks (outline and chapter resolve, pressure lens present) that
  fire only when outline metadata exists.

---

## 7. Examples from the shipped data

### Ideation, pure reasoning

Record `r-idea_generation-*`, stage `ideation`, depth `standard`.

> **Instruction** — You are testing an idea against the question of whether it can carry a
> novel. / Your premise is vivid and nothing has been asked of anyone yet. / A premise
> without pressure is a setting, and a setting cannot generate a middle. / You are in the
> idea's first statement. / Nothing is fixed yet; the value of this reasoning is in the
> decisions it makes rather than the options it lists. / Work the material until it has an
> engine that generates events, and say what tests it. / Deliverable: a premise with an
> engine, the promise it makes, and the choice that tests it. / Reason in structural and
> conceptual terms only; do not write any prose.

> **Response (opening)** — An idea becomes a story when someone wants something that costs
> them, and something makes the wanting dangerous. Test the material against that shape:
> who wants what, why now, and what failure would mean for them.
>
> … then the library's reasoning (charging the premise a running cost, turning concept into
> pressure, giving the opposition its best case), a `cost_ledger` paragraph, two lens
> paragraphs, and a commitment: *Commit to a premise with a built-in demand: one person,
> one obligation, one cost that grows with time.*

### Outline, pure reasoning

Record `r-outline_design-*`, stage `outline`, depth `deep`.

> **Instruction** — You are turning a decided premise into the structure of a novel before
> any drafting begins. / Your middle movement has chapters and no pressure. / Middles sag
> when the plan carries events without carrying escalating costs. / You are in the second
> movement's design. / … / Reason at the level of structure, and stop when the plan
> contains decisions rather than intentions. / Deliverable: a plan whose chapters have
> functions, positions, and prices.

> **Response (excerpt)** — Give the middle a question of its own rather than a continuation
> of the first act… Raise the price of the protagonist's method rather than the size of the
> threat… Decide the midpoint reversal exactly: the moment when the protagonist learns that
> their understanding of the situation was wrong in a way that makes the goal harder.

### Drafting, transition

Record `t-pov_perception-*`, stage `drafting`, depth `terse`, lenses `['pov']`.

> **Instruction** — Your protagonist is about to draw the wrong conclusion from accurate
> evidence. / A durable misreading must be earned from the character's existing beliefs and
> must produce consequences that look like consequences of the truth. / The outline you have
> been given fixes what this chapter must accomplish, so the reasoning works inside those
> obligations rather than renegotiating them. / Think the problem through to the end of the
> reasoning, then let the scene take over.

> **Response (closing)** — Write the chapter as if the misreading were correct: describe
> through it, decide through it, and let every consequence proceed as though it were true.
> The reader will register the error without being told, and the correction, when it arrives
> chapters later, will be a turn rather than a clarification.
>
> Given the above, the scene begins.

### Revision, negative

Record `n-tension-*`, stage `revision`, depth `deep`, strategies `['pre_mortem', 'reader_model']`.

> **Instruction** — You are in revision, where the damage described below is usually
> introduced. / You notice the book's tension economy is running a deficit: questions
> answered steadily, new ones opened rarely… The pull is toward resolution, because paying
> off questions feels like progress. / Reason past the pull before starting the pass, and
> decide what the revision will actually do.

> **Response (excerpt)** — The stack is emptying, and the single remaining question cannot
> carry the book alone. Restore the deposit habit: every scene that answers a question must
> open or sharpen another… Refuse the deficit spending. Install the next layer of questions
> before the current ones close.

---

## 8. How to regenerate

```bash
python -m generator.build_dataset --size 7200 --seed 20260924
python -m validation.validate_dataset data/dataset.jsonl
python -m training.convert_for_training --out training/formatted
```

The build is deterministic per seed. `--size` may be anything from 200 to 20,000; the
validator's default band is the 6,000-8,000 target.

---

## 8. This round: rules with examples, task-first reasoning, and genres

Three gaps were closed and verified against the shipped build.

**Rules, with worked examples for each.** The seven generative libraries and the three genre
libraries previously carried no rules of their own, so brainstorming, outlining and revision
records fell back on a single lens for their rule tags. They now carry explicit rule sets
(`GENERATIVE_RULES` in `generator/rules.py`), which means the craft rules are exercised while
brainstorming, outlining and writing rather than only in the writing libraries. The build emits
`data/rule_index.json` (every rule with its group, lens, example counts and example record ids
per stage and type) and `docs/RULE_COVERAGE.md` renders all 260 rules with their examples. The
validator now enforces a floor of examples per rule, requires every rule in more than one record
type, and requires every rule to appear while brainstorming, outlining or writing.

**Reasoning first about the task and the story.** `generator/task_reading.py` adds the opening
reasoning to every record: writing records read the chapter's task (function, beats, state to
hand on), reconstruct the story so far from the earlier chapters, reconstruct the characters and
what they carry into the scene, decide what happens in what order, and plan the chapter's
emotional line; outlining records reason about the story (want, obstacle, escalation, shape) and
about the outline's own deliverable (chapter-by-chapter summaries, character notes, plot,
conflict, notes); brainstorming records reason about the story the idea would become; revision
records read the draft as the reader meets it. Records carry `task_reading`, and the validator
requires the stage's mandatory kinds.

**Genre craft.** `generator/genres.py` plus three libraries (`genre_epic_fantasy`,
`genre_scifi`, `genre_thriller`) teach how to write each genre and what a story in it looks
like. Each genre has a promise, a structural story shape, moves, problems, three traps,
discipline checks, a theme and principles. 1,104 of the 7,200 records reason inside a genre
(368 / 367 / 369), across brainstorming, outlining and writing, shipped both in the main dataset
and as `data/genre_examples.jsonl`. Every genre record declares `genre`, and its instruction
leads with the genre's frame and story shape.

Resulting build: 7,200 records, 28 libraries, 260 rules exercised, 1,104 genre examples, every
record opening with task and story reasoning. Validator: green.
