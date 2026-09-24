# Writer-Craft Reasoning Dataset

An instruction-response dataset of **6,400 examples** that teaches a fiction-writing model
*internalized writer thinking*: how to construct plot, escalate conflict, make character
decisions, manage narrative information, pace scenes and chapters, plant and pay off
long-range setups, hold tension, sustain momentum, and control point of view, prose
surface, imagery, emotion, dialogue, action, worldbuilding, humor, continuity and style —
as generative, forward-looking reasoning performed *while writing*, not as post-hoc
analysis.

This is a **reasoning dataset**. The responses contain the structural craft reasoning the
model should produce before it writes: decisions, costs, staging, and what a scene owes the
book. There is zero prose — no illustrative passages, no sample lines, no written-out
examples anywhere in the responses.

At inference the model is handed the novel outline it is about to draft, along with a
situation prompt like the ones in this dataset, and it reasons before writing. That outline
is supplied by the caller at request time; it is deliberately **not** part of these records,
so the dataset stays pure reasoning supervision and the trained behavior does not depend on
any particular outline, chapter, or story.

Designed to accompany pretraining on a corpus of high-quality novels.

---

## The three example types

| Type | Share | Count | Ends with |
|---|---|---|---|
| `transition` | 50% | 3,200 | the single handoff line `Given the above, the scene begins.` |
| `reasoning` | 25% | 1,600 | nothing — the response ends when the reasoning is complete |
| `negative` | 25% | 1,600 | nothing — ends on the replacement decisions |

**Transition examples** (the dominant training signal) take one specific craft problem,
work through it with complete reasoning, and end with exactly one voice-neutral, structural
sentence: `Given the above, the scene begins.` Nothing follows it. The reasoning is always
thorough enough that the handoff feels earned — the model sees planning lead directly into
execution, across every category of craft problem.

**Pure reasoning examples** are architecture-level: arc shape, the schedule of setups and
payoffs, cost distribution, knowledge arcs, relief economics, how craft problems interact
across chapters. No handoff line.

**Negative examples** frame structural traps as *live pulls to reason past while
generating* — always forward-oriented: here is the temptation as it presents itself while
drafting, here is the damage it would do downstream, here is the replacement reasoning and
the decisions to carry into the writing. Never backward-looking diagnosis.

## Craft categories (18)

Each category module is an authored library of forward-looking craft paragraphs, and each
maps onto the 260-rule craft registry in `generator/rules.py` (rule ids follow the
original numbering, 1–260).

| Category | Craft domain | Rule ids |
|---|---|---|
| `plot_architecture` | plot construction and architecture | 104, 178, 179, 224-226 |
| `conflict_escalation` | escalation across scenes and arcs | 103, 123, 133, 134 |
| `character_decisions` | decision making and motivation | 151-167 |
| `information_management` | reader/character knowledge asymmetry | 9, 148-150, 186-196, 257 |
| `scene_construction` | scene-level pacing and multi-purpose construction | 100-102, 105-107, 109, 110, 112, 114, 115 |
| `chapter_arcs` | chapter-level arc structure | 113, 180, 181 |
| `setup_payoff` | long-range setup and payoff | 182-185 |
| `tension` | tension maintenance | 111, 176, 177, 259 |
| `momentum` | narrative momentum | 108, 116, 117 |
| `epic_scale` | worldbuilding pressure, magic as a priced economy, prophecy vs. agency, sprawl control, series architecture | 137-147 |
| `pov_perception` | point of view, interiority, what a character perceives and misreads | 1-8, 10-13, 17, 18 |
| `concrete_grounding` | the concrete before the abstract | 19-22, 24, 25, 27, 248-250 |
| `prose_discipline` | prose style, rhythm, restraint, machine-prose avoidance, style consistency | 16, 26, 28-46, 197-213, 241-247, 253, 255, 260 |
| `metaphor_imagery` | metaphor, imagery and symbol discipline | 38, 47-57 |
| `emotion_craft` | emotional individuation, timing and gradient | 14, 15, 23, 58-75, 251 |
| `dialogue_voice` | dialogue, subtext, register and humor | 76-99, 168-175, 252 |
| `action_physicality` | action, combat legibility, physical cost | 118-122, 124-132, 135, 136 |
| `continuity_outline` | continuity across a novel and obedience to its plan | 214-223, 227-240, 254, 256, 258 |

Each rule is routed to exactly one category module, so the eighteen modules between them
encode all 260 rules of the craft guide. Cross-cutting coverage on top of that is carried
by the seventeen lens pools described below, and every record lists both the rules of its
category and the lenses it was reasoned through.

## How a record is composed

1. **Craft item** — a problem, a trap, or an arc-level theme is drawn from the category
   library.
2. **Instruction** — a second-person writing situation: the frame of the moment, the
   problem itself (what the book is doing and why it resists easy handling), where in the
   work the writer is, and the instruction to reason it through in full.
3. **Response** — the craft item's opening paragraph, two or three of the category's craft
   paragraphs, one to three cross-cutting **lens** paragraphs (17 lens pools spanning POV,
   concrete grounding, character, scene, pacing, emotion, dialogue, humor, action,
   worldbuilding, continuity, plan obedience, reader trust, metaphor, prose, AI-pattern
   avoidance and style consistency), and the item's closing paragraph, with the handoff
   line appended for transition examples.

Lens choice is balanced across the dataset: every lens leads its share of records and
appears in many more.

At inference the caller prepends the outline being drafted to an instruction of this shape;
the outline text itself never appears in the training records.

## Data format

JSONL. One record per line:

```json
{
  "id": "t-dialogue_voice-0550",
  "type": "transition | reasoning | negative",
  "category": "dialogue_voice",
  "subcategory": "humor_placement",
  "instruction": "the writing situation and the craft problem",
  "response": "pure structural/conceptual craft reasoning",
  "lenses": ["dialogue", "humor", "character"],
  "rules": [76, 78, 80, 168, 169, 252]
}
```

- `lenses` names the craft dimensions the record reasons through, in canonical paragraph
  order.
- `rules` lists the registry rules the record's category encodes, so a training run can
  balance, weight or ablate signal per rule without re-deriving the mapping.

Files:

- `data/dataset.jsonl` — all 6,400 records, shuffled
- `data/transition_examples.jsonl` — 3,200 transition examples
- `data/pure_reasoning_examples.jsonl` — 1,600 pure reasoning examples
- `data/negative_examples.jsonl` — 1,600 negative examples
- `data/manifest.json` — seed, counts, per-category, per-lens and per-rule coverage

## Guarantees (enforced by the validator)

- Type ratios 50/25/25 within ±2 points; all 18 categories present in every type with
  balanced per-category counts.
- Transition responses end with exactly one occurrence of the marker, as the final line,
  with substantial reasoning before it; no other type contains the marker or the phrase.
- No double quotes, no curly quotes, and no exemplification phrases (`for example`,
  `such as`, `might read`, and similar) anywhere — the no-prose rule is machine-checked,
  not aspirational.
- All 6,400 instructions and all 6,400 responses are globally unique.
- Every rule in the 260-rule registry is exercised; lenses and rule references are valid
  on every record; responses sit inside a sane length band (180–900 words).

Run the validator:

```bash
python -m validation.validate_dataset data/dataset.jsonl
```

## Regenerating

The dataset is generated from authored libraries of craft-reasoning paragraphs and 17 lens
pools, deterministically composed per seed:

```bash
python -m generator.build_dataset --size 6400 --seed 20260924
```

`--size` may be any value in the 2000–20000 supported range (the shipped dataset is 6,400,
inside the 6,000–8,000 target band the validator enforces by default); a different seed
yields a different, equally valid sample of the combination space. Outputs are written to
`data/`.

The generator also carries an optional `--with-outlines` mode that conditions each record
on one chapter of the authored outline bank in `generator/outlines/` (36 novels × 10
chapters). It exists for experiments that need the outline inside the training request;
the shipped dataset does not use it.

## Training notes

The dataset is built for **reasoning-trace supervision** rather than for direct prose
generation:

- **Cold-start SFT** on the reasoning traces, with the chapter text withheld, so the model
  learns to plan before writing. The `reasoning` slice is the arc-level curriculum stage;
  `transition` records give the planning-to-writing handoff; `negative` records teach
  forward avoidance of named traps rather than post-hoc critique.
- **Prompt shape at inference.** Send the outline being drafted, then a situation prompt in
  the style of these instructions, and let the model produce the reasoning before the
  writing pass. Because the records contain no outline, the model learns the reasoning
  rather than the outline, and it transfers to any novel the caller supplies.
- **Keep supervision on the traces.** The responses contain no prose by design: pair them
  with a strong pretrained prose model, or with a separate fine-tune on the novels corpus,
  so the reasoning does not cannibalize style.
- **On-policy stage.** Once the model produces traces, score the *chapter* it writes
  afterwards (not the trace) and reinforce on that signal; the negative examples give the
  reward model concrete, already-named failure modes to rank against.
- **Rubric hooks.** `lenses` and `rules` are attached per record, so evaluation can be
  sliced by craft dimension and per-rule coverage can be checked against held-out chapters.
- **Do not sample the marker literally at inference** unless the writing pass follows in
  the same generation; the marker is a planning-to-writing cognitive handoff, not a
  stylistic flourish.

`training/convert_for_training.py` renders the dataset as chat-format SFT splits:

```bash
python -m training.convert_for_training --out training/formatted
```

## Publishing this repo as a Kaggle dataset

Kaggle can create a dataset directly from a GitHub repository: on
[kaggle.com/datasets/new](https://www.kaggle.com/datasets/new), pick the
**GitHub repository** source and paste this repo's URL. Kaggle downloads the
repo's **default branch** into its own storage. For that to work:

1. **The repo must be public.** Kaggle fetches the repository anonymously, so a
   private repo cannot be imported (GitHub -> repo Settings -> General -> Danger
   Zone -> Change visibility -> Public).
2. **The data must be on `main`** (the default branch). Kaggle does not offer a
   branch picker; it imports whatever `main` holds. Merge the PR carrying the
   dataset into `main` before creating the Kaggle dataset.
3. **License:** choose *CC0 1.0 / Public Domain* in Kaggle's dropdown to match
   the `LICENSE` file in this repo.

After creation you can enable **automatic interval updates** in the dataset's
Settings tab (or press Update manually), so the Kaggle dataset re-syncs whenever
`main` changes -- regenerate the data, push to `main`, and Kaggle picks it up.

The import mirrors the repository layout; the training files are under `data/`.
Inside a Kaggle notebook they land at:

```
/kaggle/input/<dataset-slug>/data/dataset.jsonl
```

## Repository layout

```
LICENSE                 CC0 1.0 public-domain dedication
generator/
  common.py             shared infrastructure: marker, instruction banks, helpers
  rules.py              260-rule craft registry (ids, groups, category and lens routing)
  lenses_a.py           lens pools: pov, concrete, prose, metaphor, emotion, dialogue, humor
  lenses_b.py           lens pools: action, worldbuilding, reader trust, continuity,
                        AI patterns, plan obedience, style consistency, pacing,
                        character, scene
  lenses.py             merged lens registry, paragraph order, category/type routing
  outlines/             optional: 36 authored novel outlines x 10 chapters (--with-outlines)
  situations.py         optional: outline conditioning used only by --with-outlines
  build_dataset.py      deterministic composition engine (CLI above)
  categories/           eighteen authored craft libraries (moves, problems, traps, themes)
validation/
  validate_dataset.py   machine-checks every hard constraint
training/
  convert_for_training.py  renders the JSONL as chat-format SFT files
data/                   generated dataset (JSONL + manifest + data/README)
```
