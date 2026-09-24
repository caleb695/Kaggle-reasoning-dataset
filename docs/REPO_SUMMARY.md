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

| Stage | Records | The work the examples teach | Libraries it reasons with |
|---|---|---|---|
| `ideation` | 900 | **brainstorming**: finding an idea that makes a story, with someone to follow, something they want badly, and trouble that will not let them have it | `idea_generation`, `idea_shaping` |
| `outline` | 1,260 | **outlining**: building the story so it works, deciding what happens, why it happens, and what it costs | `outline_design`, `arc_mapping`, `scene_planning` (65%) plus the structural libraries |
| `drafting` | 4,320 | **writing**: how the chapter in front of you gets written, inside the outline you were given | the eighteen writing craft libraries |
| `revision` | 720 | **revising**: what to change, what to keep, and the order to work in | `revision_craft`, `revision_diagnosis` |

Brainstorming and revision reason with nothing but their own libraries: a brainstorming request that talks about thread schedules is an outlining request, and a revision request that plans an arc is planning rather than repair. Outlining keeps the structural libraries beside its own, and writing draws on the whole craft library, because that is where all of it converges.

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
response words: min=190 p50=347 max=585
  instruction words: min=56 p50=113 max=169
OK: 7200 records
  types: {'negative': 1800, 'reasoning': 1800, 'transition': 3600}
  stages: {'ideation': 900, 'outline': 1260, 'drafting': 4320, 'revision': 720}
  stage x type: {'drafting/negative': 360, 'drafting/reasoning': 360, 'drafting/transition': 3600, 'ideation/negative': 450, 'ideation/reasoning': 450, 'outline/negative': 630, 'outline/reasoning': 630, 'revision/negative': 360, 'revision/reasoning': 360}
  categories: 25, each used only at the stages it applies to
  stage ideation  libraries=2, own-library share=1.00
  stage outline   libraries=12, own-library share=0.65
  stage drafting  libraries=18, own-library share=0.00
  stage revision  libraries=2, own-library share=1.00
  rules exercised: 260 of 260
  strategies: {'verify': 1653, 'cost_ledger': 694, 'weakest_link': 694, 'constraints_as_conditions': 692, 'pre_mortem': 687, 'reader_model': 681, 'backward': 526, 'two_routes': 524, 'ordering': 517}
  lenses: 17 distinct; leads balanced 169-780
```

- Depths: `standard` 3943 · `deep` 1823 · `terse` 1434; difficulty follows depth
  (`intermediate` / `advanced` / `foundational`).
- Word bands in practice: terse 190–339, standard 245–499, deep 285–585.

- 218 distinct subcategories; all 7,200 instructions and all 7,200 responses globally
  unique.
- Category sizes 240–450 across the 25 libraries.
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

### 6.1 Writing — transition, the dominant training signal

`t-scene_construction-0603` — drafting, transition, terse, 205 words, category `scene_construction`, lens(es) ['concrete'], strategies [].

The reasoning works through what the scene is for, then hands off in exactly one sentence with nothing after it.

**Instruction**

> You are at the desk with the scene ahead of you and the problem below still open.
> Your story's central tension is about to become face-to-face, and the scene must carry the accumulated weight.
> The confrontation must be built as a contest with moves, counters, and a value shift, so that the meeting changes the relationship's position rather than merely displaying it.
> You are in the approach to the climax.
> The outline you have been given fixes what this chapter must accomplish; the reasoning decides how it is written.
> Think the problem through to the end of the reasoning, then let the scene take over.
> Reason about the craft and stop there, with no prose on the page.

**Response**

> Before drafting, fix the scene's turn: what is different between these two after the encounter that was not different before. A confession extracted, a threat made credible, an alliance revealed as betrayal, the turn is the scene's reason for existing, and every beat before it is built to make the turn cost something.
>
> Give the scene's opening beat a job beyond entry. The first exchange should either advance a live question from the previous scene or establish the scene's own pressure, ideally both, so the reader is inside motion from the first line. An opening beat spent on orientation is a tax collected at the moment of highest attention.
>
> Watch for stretches where the writing has drifted entirely into abstraction, where decisions, meanings, and emotional states are discussed without any material anchor. Break such stretches with the concrete, and keep the abstract passage short enough to stay a movement within the scene rather than the scene's mode.
>
> Fix the entry positions and the destabilizing move, then write toward the moment the map changes. The scene's value will be measured in what each party now knows about the other, and
>
> […]

### 6.2 Writing — transition, deep

`t-chapter_arcs-2403` — drafting, transition, deep, 377 words, category `chapter_arcs`, lens(es) ['pacing', 'style_consistency'], strategies ['cost_ledger'].

A deep trace interacts several decisions, carries a named reasoning strategy, and still hands off in a single line.

**Instruction**

> You are at the desk with the scene ahead of you and the problem below still open.
> The climactic chapter must carry the story's accumulated pressure to its release, and its shape will decide how the release reads.
> The climactic chapter must be shaped to concentrate and release the book's pressure: the approach compressed, the collision in real time, and the immediate consequence granted full weight before the book's voice changes register.
> You are in the climax chapters.
> The chapter's obligations are set; what remains is how they reach the page.
> Resolve the craft question in your head, then write into the scene without further commentary.
> Deliverable: how this chapter gets written: what the scene does, whose eyes it is, and what the reader learns.
> Reason in structural and conceptual terms only; the prose comes after.

**Response**

> Before drafting the climax chapter, decide its internal sequence of peaks. A climax is rarely one note; it is a chain of escalations, each solution producing a worse problem, until the final choice. Plan the chain, with the false reliefs placed so the reader's hope is engaged and spent deliberately, and let the true peak be unmistakable.
>
> Keep the promise honest. A chapter that opens on one tension and spends its length on another has broken a small contract, and the habit erodes the reader's willingness to invest in openings at all. Decide the chapter's real subject before writing its first line, and let the first line be a faithful advertisement.
>
> Keep exits honest. A chapter that ends on manufactured peril, an unexplained sound, a stranger at the door, pays out in diminishing returns unless the peril was already in the story's system. Draw exit pressure from the established tensions, so the pull across the break is the story's own gravity.
>
> Design each chapter's interior shape deliberately: where it rises, where it rests, and where it crests. A chapter is a small arc with its own pressure curve, and the curve should be planned in
>
> […]

### 6.3 Brainstorming — pure reasoning

`r-idea_shaping-0968` — ideation, reasoning, standard, 374 words, category `idea_shaping`, lens(es) ['reader_trust', 'character', 'emotion'], strategies ['cost_ledger'].

The how of brainstorming: what makes a story engaging, and how that quality is built into the idea on purpose.

**Instruction**

> You have material you love and no trouble in it yet.
> You are trying to identify what makes a premise gripping rather than merely clever.
> What makes a story engaging, and how do you build that into an idea on purpose?
> The material is still soft; the reasoning should end with a story specific enough to follow.
> Work the idea until you can say what happens and why it matters, and stop there.
> Hold to craft reasoning alone; no written passages of any kind.

**Response**

> An idea becomes a story when someone wants something and cannot simply take it. The reasoning below looks for that want, the resistance to it, and the scenes it would produce.
>
> Engagement in a novel comes from three sources that can be designed: an unresolved question the reader wants answered, a person the reader wants to see succeed or fail, and a cost the reader can feel approaching. A premise that supplies all three produces momentum from the first chapter.
>
> Make the protagonist's want concrete enough to be pictured. Abstract goals produce abstract suspense: the reader waits for a resolution they cannot visualize, and nothing that happens feels like progress or setback.
>
> Give the opposition a plan of its own with a timetable. Antagonism that only reacts to the protagonist creates episodes; antagonism with its own schedule creates a clock, and a clock is what makes a middle feel inevitable.
>
> Choose an opening question the reader can repeat. If a reader cannot say what they are waiting to find out by the end of the first chapter, the hook has not been decided even if the scene is well built.
>
> Specific beats spectacular: stakes a r
>
> […]

### 6.4 Outlining — pure reasoning

`r-arc_mapping-0306` — outline, reasoning, standard, 247 words, category `arc_mapping`, lens(es) ['pacing', 'character'], strategies ['ordering'].

Outlining reasons about the story itself: what happens, why it happens next, and what it costs.

**Instruction**

> You are outlining the story: the idea is settled and now it has to work.
> You are designing several arcs at once and want them to reinforce each other.
> How do the parts of a story move together: what the protagonist wants, what opposes them, and what each of them learns?
> Reason about the story as a whole: what happens, why it happens next, and what it costs.
> Reason about the craft and stop there, with no prose on the page.

**Response**

> Outlining is where a story is made to work: causes, consequences, and an order that makes the ending necessary rather than convenient.
>
> The work at this level is alignment. Each movement should advance the plot and cost the character something, and each revelation should land where it changes a relationship as well as a fact, so a single scene does several jobs at once.
>
> Map what each principal character wants at the start and how it changes by the end. Wants that stay constant while the plot moves produce a cast that reads as scenery, and the plan should record the shifts.
>
> Schedule the resolution's requirements backward from the ending, so the last movement does not have to establish anything it needs. Everything the ending spends should have been placed before the midpoint where possible.
>
> Arcs are sequences of cost: each movement should take something the reader has watched the character accumulate.
>
> Decide the sequence of work before deciding the content. Knowing that one choice forecloses another changes which choices are available, and reasoning out of order produces plans that cannot be executed in the order they were imagin
>
> […]

### 6.5 Outlining — planning a scene that turns the story

`r-scene_planning-0480` — outline, reasoning, standard, 282 words, category `scene_planning`, lens(es) ['pacing', 'character', 'scene'], strategies ['ordering'].

Scene planning at outline height: what the scene is for, what changes inside it, and what it leaves behind.

**Instruction**

> You are building the order of events, and every part has to earn its place.
> You are designing the physical facts of a scene that the story depends on.
> How do you plan a big scene so that it turns the story instead of only being impressive?
> The idea is settled; what follows decides how it becomes a story.
> Decide the turns, the trouble, and the price, and stop when the story holds together.
> Keep the reasoning structural. Do not draft prose, quoted lines, or invented detail.

**Response**

> A story holds together when each thing that happens causes the next and costs somebody something. What follows arranges the material against that standard.
>
> A staged scene is built from four decisions: the space and its constraints, the positions and capabilities of everyone present, the moment the terms change, and the bill that comes due afterward. Staging without a turn is a performance, and a turn without staging is an announcement.
>
> Plan the space before the action: exits, obstacles, distances, and the two or three features that will decide the outcome. Every later convenience in a staged scene traces back to geography that was never decided.
>
> Establish capabilities before the scene depends on them. A resource that appears at the moment of need discounts every earlier difficulty, so the plan should place its introduction where the reader can verify it.
>
> Sequences have shape: one question, one crest, one entry state, one exit state.
>
> Order the decisions by consequence: the structural choice first, the scene-level choices that follow from it second, and the local choices last. Reversing that order is how drafts end up polished in
>
> […]

### 6.6 Writing — pure reasoning, at the desk

`r-epic_scale-1151` — drafting, reasoning, terse, 239 words, category `epic_scale`, lens(es) ['outline_obedience'], strategies [].

A drafting record reasons about how the chapter gets written rather than about the shape of the book.

**Instruction**

> You are inside the draft, and the way this is written decides whether the chapter works.
> You are planning a fantasy series whose volumes must function as one long structure, and the series-level promise system needs design.
> Plan the series architecture: which promises each volume makes and keeps, what is held in reserve across volumes, and how the whole escalates toward the series climax.
> The outline you have been given fixes what this chapter must accomplish; the reasoning decides how it is written.
> Work out how the chapter handles this in the writing, and stop once it is decided.
> Structure and concept only: no prose is to be written as part of the reasoning.

**Response**

> The decision below is a writing decision: what the chapter shows, whose eyes it is, and what the reader learns from it.
>
> A series is a promise ledger kept across years of the reader's life: each volume takes deposits, pays some debts on its own behalf, and holds the deeper reserves for the end. Design the ledger before drafting the next volume, and know at every point which promises are book-scoped and which are series-scoped, because confusing the two is how series sag.
>
> Assign each volume its own complete contract: question, opposition, climax, and change, deliverable within its covers. Then assign it its series duty: which long promises advance, which reserves deepen without being spent, and which new long promises it opens for the volumes after. A volume that cannot state both duties will serve neither.
>
> Magic means what it costs: limits generate plot, prices generate meaning, and spectacle without a bill is noise that depreciates with every repetition.
>
> Keep the ledger of obligations current as the chapter is drafted: threads opened and not yet closed, clues and the explanations they point toward, questions the book has asked t
>
> […]

### 6.7 Revision — pure reasoning

`r-revision_craft-1638` — revision, reasoning, terse, 190 words, category `revision_craft`, lens(es) ['ai_patterns'], strategies [].

Revision reasons about repair: what is wrong, why it is wrong, and what to do first.

**Instruction**

> You are reading back through the manuscript, deciding what to change.
> You are planning a revision pass across an entire manuscript.
> How do you revise a whole manuscript in an order that does not force you to redo the same work?
> Everything on the page is material; the reasoning decides what survives.
> Reason to the cause of the problem and the change that removes it.
> Deliverable: what to change, what to keep, and the order to work in.
> Structure and concept only: no prose is to be written as part of the reasoning.

**Response**

> What follows is the repair: what is wrong, why it is wrong, and what to do first.
>
> Treat the manuscript as a system of dependencies: chapters depend on earlier plants, characters depend on earlier knowledge, and the ending depends on everything the middle paid for. Revision has to work on the dependencies rather than on the chapters, which means it starts with the map and not the pages.
>
> Decide which chapters the revision is allowed to restructure and which are fixed points. Marking the fixed points prevents the pass from expanding indefinitely, and it also shows which structural change would require the fewest other repairs.
>
> Structure, then scene, then continuity, then line, with each pass finished before the next begins.
>
> Vary paragraph rhythm and sentence construction across the chapter, and vary names against pronouns. Repetition of a character's name where a pronoun would sound natural, and repetition of a sentence shape across consecutive paragraphs, both read as machinery once the reader's ear has been caught.
>
> Commit to revision by dependency rather than by chapter: structural decisions first, continuity after, line last, a
>
> […]

### 6.8 Brainstorming — a trap reasoned past while generating

`n-idea_generation-0708` — ideation, negative, deep, 310 words, category `idea_generation`, lens(es) ['character', 'emotion'], strategies ['reader_model'].

Trap, then the damage it would do to the story, then the replacement thinking. Nothing is diagnosed after the fact.

**Instruction**

> You are developing an idea that is all situation and no want.
> The premise is built around a conclusion you want the reader to reach.
> The theme is fixed and the characters are arranged to illustrate it. Opposition exists to be wrong, the middle repeats the argument in different registers, and the ending confirms what the first chapter already stated, so the reader is given an answer that was never in doubt.
> You are in the first structural pass.
> Everything here is still open, so the work is generation rather than repair.
> Work past the comfort and get to the want, the obstacle, and the stakes.
> Deliverable: an idea that makes you need to know what happens next: a person to follow, something they want badly, and trouble that will not let them have it.
> Reasoning only. The output is decisions, costs, and staging, not prose.

**Response**

> Ideas that cannot produce trouble feel generous while they are being developed, and their cost appears only when the book has to make something happen.
>
> Convert the conclusion into a question the book will test, and give the strongest counter-position to someone sympathetic. The story then has somewhere to go, because a question can be probed while an answer can only be restated.
>
> Message-driven books read as arguments and are judged as arguments, which means the reader evaluates whether they agree rather than whether the story moved them. The characters become instruments, the middle becomes repetition, and the ending cannot surprise because it was decided before the situation existed.
>
> Decide the promise and the price before the plot. Structure derived from a promise has a reason for every movement, and structure derived from events has to justify itself later.
>
> Reason past it by giving the opposition its best case and letting the protagonist be wrong in the first movement. A theme survives testing and dies of agreement, so the planning decision is to make the book an inquiry with consequences rather than a demonstration.
>
> Decide 
>
> […]

### 6.9 Outlining — a trap reasoned past

`n-outline_design-0296` — outline, negative, standard, 306 words, category `outline_design`, lens(es) ['pacing', 'worldbuilding'], strategies ['reader_model'].

The outline-shaped version of the same discipline: name the pull, price it, commit to the replacement.

**Instruction**

> You are outlining, and the plan keeps becoming a list of things that could happen in any order.
> You are about to draft from a sequence rather than from a design.
> The outline reads as a schedule of incidents, each one clear and none of them connected by pressure. Events arrive, the protagonist responds, and the next event is queued, so the plan contains activity without escalation and each chapter competes with the last rather than building on it.
> You are in the review of the plan before drafting.
> The idea is settled; what follows decides how it becomes a story.
> Identify what the weak shape would cost the story, and decide what the outline does instead.
> Deliverable: a story that works from the first page to the last: what happens, why it happens, and what it costs.
> Hold to craft reasoning alone; no written passages of any kind.

**Response**

> The pull below produces an outline that reads as complete and behaves as empty, which is why it is worth naming while the plan is still easy to change.
>
> The pull is toward incident, because incidents are easy to imagine and changes of condition require decisions. Reason past it by rewriting each outline line as a change: what is true after this chapter that was not true before, and what does that make possible or impossible.
>
> Books drafted from event lists have middles that sag and endings that arrive rather than land. Each chapter has to justify itself with a bigger incident because nothing has accumulated, escalation becomes a matter of volume, and the final movement has to be louder than everything before it in order to feel like an ending at all.
>
> Every structural decision should be expressed as a change of condition, a cost, or a position in the schedule. Structure that cannot be described that way is decoration.
>
> Reason past it while outlining by writing each chapter's obligation as a change of state and each movement's turn as a loss. The plan then carries pressure rather than activity, and the drafting stage inherits decisio
>
> […]

### 6.10 Revision — a trap reasoned past

`n-revision_craft-1722` — revision, negative, deep, 295 words, category `revision_craft`, lens(es) ['style_consistency', 'ai_patterns'], strategies ['reader_model'].

The revision temptation is the one that makes a draft look finished sooner; the reasoning refuses it before the pass starts.

**Instruction**

> You are in the pass where the temptation below is strongest, because the prose is already readable.
> The draft reads well and does not work.
> The pages are being polished because polishing is pleasant and immediately measurable. Sentences improve, the chapter reads more smoothly, and the structural fault remains underneath, now harder to see because the surface is convincing.
> You are in the review of the chapter's function.
> The manuscript is movable, so the order of the work matters as much as the changes.
> Name the shortcut, see what it would leave in the book, and choose the correction that costs something.
> Deliverable: what to change, what to keep, and the order to work in.
> Reason in structural and conceptual terms only; the prose comes after.

**Response**

> The shortcut below trades the book's problem for the writer's comfort. The reasoning works past it to the change the draft actually needs.
>
> The pull is toward the sentences, and the correction is to decide the chapter's function and structure first. Reason at the level of what the chapter must change and how that change is staged before any line is touched.
>
> Polishing before structural repair produces manuscripts that read better than they are, which makes the real problems harder for the writer to see and easier for a reader to feel without naming. The revision time is spent on pages that later get removed, and the structural fault is still present at the end of the pass.
>
> Run passes in order and finish each one. Structure, then scene, then continuity, then line.
>
> Reason past it by fixing the pass order: structure, then scene, then continuity, then line. Each pass is finished before the next begins, and the line pass is the last work the chapter receives.
>
> Reason from the reader's model rather than the plan's: what they know, what they expect to happen next, and what they would conclude from this as staged. The gap between the plan
>
> […]

### 6.11 The same lens at two heights

Cross-cutting lens paragraphs are drawn at the height of the stage's work, so a brainstorming record does not receive scene-level advice and an outlining record does not receive line-level advice. Same lens key, `character`:

*Brainstorming height (`IDEATION_LENSES`, used at ideation):*

> Choose the person the premise damages most. Whoever has the least ability to walk away will generate the most story, and whoever is most capable will generate the least pressure.

*Outlining height (`OUTLINE_LENSES`, used at outline):*

> Decide what each principal character wants independently of the main problem, because those wants are what collide when the plot is briefly quiet.

*Writing height (`LENSES`, used at drafting and revision):*

> Decide what each character wants in this chapter, what they are willing to risk for it, and what they will not do even to succeed. The boundary is where the character is legible, and it is the part of the design most often left implicit, which is why so many characters read as capable of anything.

### 6.12 Optional outline mode (not part of the shipped build)

With `--with-outlines`, the request carries one chapter of the authored outline bank and the record gains `outline_id` / `chapter` fields. Verbatim fragment of such a request:

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

The shipped dataset has none of this: `data/dataset.jsonl` records carry no outline text and no outline fields. In outline mode the entity that supplies the outline is the caller, and the reasoning learns to work inside it.

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

---

## 9. Rules: the 260-rule registry, with worked examples

The craft rules the dataset is built on live in `generator/rules.py` (rule numbering follows
the original craft guide, 1–260, grouped into eighteen groups such as POV, prose, emotion,
dialogue, scene, pacing, reader trust, AI-pattern avoidance, plot and outline obedience,
continuity and the overarching rules). Every authored paragraph in the 28 libraries encodes
one or more of those rules, and **every record is tagged with the rules its reasoning
implements**, so the supervision can be weighted, balanced or ablated rule by rule.

The generative libraries — brainstorming, outlining, revision and the three genres — carry
explicit rule sets too (`GENERATIVE_RULES`), so the rules are applied while brainstorming,
outlining and writing rather than only in the writing libraries:

| Library set | Rules carried |
|---|---|
| `idea_generation` | 26 rules (character, plot, worldbuilding, reader trust, overarching) |
| `idea_shaping` | 28 rules |
| `outline_design` | 42 rules |
| `arc_mapping` | 39 rules |
| `scene_planning` | 32 rules |
| `revision_craft` / `revision_diagnosis` | 41 / 51 rules |
| `genre_epic_fantasy` / `genre_scifi` / `genre_thriller` | 45 / 41 / 41 rules |

Coverage in the shipped build, enforced by the validator:

| Measure | Value |
|---|---|
| rules in the registry | 260 |
| rules with worked examples | 260 |
| examples per rule (min / median / max) | 210 / 572 / 3279 |
| rules exercised at more than one record type | 260 |
| rules exercised while brainstorming, outlining or writing | 260 |

Two worked examples, one rule each, with the record that implements it:

**Rule 59 (`dont_name_emotions`)** — examples include `t-emotion_craft-2201`, which opens by
reading the chapter's job and the people in the scene, then reasons:

> Decide where the feeling goes rather than when it ends. It can be postponed by obligation,
> converted into efficiency, hidden behind a practical problem, or saved for a character who
> is not present. Every one of those options lets the plot continue while keeping the emotion
> alive, and the release, when it comes, will be an event rather than a summary.

**Rule 151 (`personalities_not_roles`)** — 2,151 examples across brainstorming, outlining and
writing, e.g. `r-idea_shaping-0750` (brainstorming) and `n-character_decisions-1373`
(writing). The ideation example reasons about casting by what a person will not give up,
which is the rule applied at the idea stage rather than at the page.

`docs/RULE_COVERAGE.md` lists all 260 rules with their group, the number of examples, the
stages and types they are exercised in, and example record ids to open.

## 10. Reasoning first about the task and the story

Every record now begins with that opening reasoning, before any craft decision, and the
validator fails the build if a record is missing it:

| Stage | Task/story reading | What it teaches the model to do first |
|---|---|---|
| writing | `task`, `story_so_far`, `characters`, `what_happens`, `emotion_line` | read what the chapter is supposed to be: its function, its beats, the state it hands on; recall what the earlier chapters established and who knows what; reconstruct what each character wants and feels on entry; decide what happens and in what order |
| outlining | `story`, `artifact`, `chapters`, `characters` | reason about the story itself (want, obstacle, escalation, shape) and about the outline's own deliverable: a chapter-by-chapter summary, short character descriptions, plot, conflict, and notes |
| brainstorming | `story`, `artifact` | reason about the story the idea would become before judging the idea: who it happens to, what they want, what it costs, and what brainstorming has to produce before it is finished |
| revision | `draft_state`, `repair` | read the draft as the reader meets it, and decide what the pass is for before changing anything |

Coverage: 4,320 writing records open with the chapter's task; 2,160 outlining records open
with story reasoning and 2,160 with the outline deliverable; 2,160 brainstorming records open
with story reasoning; 720 revision records open with the draft's state. `story_so_far`
(1,081), `characters` (1,034), `what_happens` (1,081) and `emotion_line` (1,096) recur across
the writing records.

A worked example — `t-emotion_craft-0281`, writing, transition:

**Instruction**

> You are at the desk with the scene ahead of you and the problem below still open.
> Your characters recover from major events within a page.
> Emotional states must be delayed, stored, or displaced; immediate resolution destroys both the character's credibility and the plot's sense of consequence.
> You are in the scene following a loss.
> Reason your way through it in full, then begin the scene.

**Response (opening)**

> Establish the boundaries of the chapter first: what it must accomplish, what it must not resolve yet, and what the reader has to be able to do afterwards that they could not do before.
>
> Reconstruct the people before staging them. For everyone in the scene: what they want in this conversation or confrontation, what they are carrying in from earlier chapters, what they believe about the situation, and what they are wrong about.

…and then the craft reasoning, ending with the single handoff line.

## 11. Genres: epic fantasy, science fiction, thriller

Three genre libraries teach how to write each genre and what a story in it looks like, as
structure rather than as prose. Each genre is a registry entry in `generator/genres.py`
(promise, story shape, and an instruction frame) plus a library in
`generator/categories/`:

| Genre | Promise | What a story in it looks like | Library craft |
|---|---|---|---|
| **Epic fantasy** | a large world with power in it, followed through people who pay for using it | a world whose powers are priced, a protagonist drawn in against preference, allies whose interests diverge, an ending that costs something unrecoverable | priced power; world with consequence; protagonist against preference; alliance and fracture; scale management; prophecy and agency |
| **Science fiction** | one change to the world, followed all the way to what it does to people | one speculative change worked out honestly, an ordinary want made expensive by it, an opposing interest that benefits from the old order, an ending that answers the question the premise raised | one change extrapolated; idea dramatized; scale from the personal; competence and cost; society as argument; question answered |
| **Thriller** | a competent person under a clock, with something worse behind every answer | danger that advances on its own schedule, an antagonist already ahead, information that is dangerous to hold, escalation where every answer widens the problem, a confrontation forced by the protagonist's choice | clock and pressure; antagonist ahead; information asymmetry; escalating cost; competence and flaw; personal stakes |

Each genre also carries its own traps (lore openings, chosen-one defaults, quest itineraries;
exposition lectures, present-day-with-gadgets, scale inflation; rescue-dependent protagonists,
information dumps, false escalation), discipline checks, an arc-level theme and principles.

Sizing: **1,104 examples** — 368 epic fantasy, 367 science fiction, 369 thriller — spread
across brainstorming (270), outlining (316) and writing (518), shipped both inside the main
dataset and separately as `data/genre_examples.jsonl`, which is the smaller genre dataset.
Genre records carry `genre`, and the instruction leads with the genre's frame and story
shape, for example:

> You are building the order of events, and every part has to earn its place.
> The book is a thriller: something in the story advances without the protagonist, the antagonist has a schedule of their own, and each solution the protagonist reaches makes the situation worse rather than safer.
> …
> A thriller story puts a protagonist with something to lose into a situation where the danger advances on its own schedule…

### 11.1 A genre example, verbatim — `r-genre_epic_fantasy-0117`

**Instruction (excerpt)**

> You are at the desk with the chapter's requirements in front of you, working out how to write it.
> The book is epic fantasy: the world's powers cost something to use, the scale is carried by consequences that land on specific people, and the protagonist's involvement comes from an obligation rather than a destiny.

**Response (excerpt)**

> Read the request before deciding anything about the writing. What the chapter has to accomplish, where it sits in the book, what it must leave true when it ends, and what the reader is supposed to have learned by the last page of it.
>
> Plan the emotional line of the chapter the way the other obligations are planned: what the reader should feel on entry, what the scene does to that feeling, and what they should be left carrying into the next chapter.
>
> The genre promises bigness felt personally. That promise is kept by architecture rather than by description: the world's rules create costs, the costs create choices, the choices create the escalation, and the escalation is paid by a small, specific cast.
