# Writer-Craft Reasoning Dataset

An instruction-response dataset of **2,400 examples** that teaches a fiction-writing model
*internalized writer thinking*: how to construct plot, escalate conflict, make character
decisions, manage narrative information, pace scenes and chapters, plant and pay off
long-range setups, hold tension, and sustain momentum — as generative, forward-looking
reasoning performed *while writing*, not as post-hoc analysis.

All responses are **purely structural and conceptual**: craft reasoning about how and why
narrative choices work. There is zero prose — no illustrative passages, no sample lines,
no written-out examples anywhere in the responses.

Designed to accompany pretraining on a corpus of high-quality novels; the core craft
framing is deliberately genre- and voice-neutral, with a dedicated category for the
scale-specific problems of **epic fantasy** (worldbuilding pressure, magic economies,
prophecy vs. agency, sprawl control, series architecture).

---

## The three example types

| Type | Share | Count | Ends with |
|---|---|---|---|
| `transition` | 50% | 1,200 | the single handoff line `Given the above, the scene begins.` |
| `reasoning` | 25% | 600 | nothing — the response ends when the reasoning is complete |
| `negative` | 25% | 600 | nothing — ends on the replacement decisions |

**Transition examples** (the dominant training signal) each take one specific craft
problem, work through it with complete reasoning, and then end with exactly one
voice-neutral, structural sentence: `Given the above, the scene begins.` Nothing follows
it. The reasoning is always thorough enough that the handoff feels earned — the model
sees planning lead directly into execution, across every category of craft problem.

**Pure reasoning examples** build deeper, architecture-level craft knowledge: arc shape,
long-range loop inventory, knowledge arcs, relief economics, drive across acts. No
transition sentence.

**Negative examples** frame structural traps as *live pulls to reason past while
generating* — always forward-oriented: here is the temptation, here is the damage it
would do downstream, here is the replacement reasoning and the decisions to carry into
the writing. Never backward-looking diagnosis.

## Craft categories (9)

1. `plot_architecture` — plot construction and architecture
2. `conflict_escalation` — escalation across scenes and arcs
3. `character_decisions` — decision making and motivation
4. `information_management` — reader/character knowledge asymmetry
5. `scene_construction` — scene-level pacing and multi-purpose construction
6. `chapter_arcs` — chapter-level arc structure
7. `setup_payoff` — long-range setup and payoff
8. `tension` — tension maintenance
9. `momentum` — narrative momentum

Each category contributes examples of all three types (45 distinct craft problems, 45
traps, and 18 arc-level reasoning themes across the dataset).

## Data format

JSONL. One record per line:

```json
{
  "id": "t-plo-0001",
  "type": "transition | reasoning | negative",
  "category": "plot_architecture",
  "subcategory": "point_of_attack",
  "instruction": "...",
  "response": "..."
}
```

Files:

- `data/dataset.jsonl` — all 2,400 records, shuffled
- `data/transition_examples.jsonl` — 1,200 transition examples
- `data/pure_reasoning_examples.jsonl` — 600 pure reasoning examples
- `data/negative_examples.jsonl` — 600 negative examples
- `data/manifest.json` — seed, counts, per-category breakdown

## Guarantees (enforced by the validator)

- Type ratios 50/25/25 within ±2 points; every category present in every type.
- Transition responses end with exactly one occurrence of the marker, as the final line,
  with substantial reasoning before it; no other type contains the marker.
- No double quotes and no exemplification phrases (`for example`, `such as`, `might
  read`, and similar) anywhere — the no-prose rule is machine-checked, not aspirational.
- All 2,400 instructions and all 2,400 responses are globally unique; no example shares
  its full paragraph combination with another.

Run the validator:

```bash
python -m validation.validate_dataset data/dataset.jsonl
```

## Regenerating

The dataset is generated from an authored library of craft-reasoning paragraphs,
deterministically composed per seed:

```bash
python -m generator.build_dataset --size 2400 --seed 20260909
```

`--size` may be any value in the 2000–3000 target range; a different seed yields a
different (equally valid) sample of the combination space. Outputs are written to
`data/`.

## Repository layout

```
generator/
  common.py              shared infrastructure: marker, instruction banks, helpers
  build_dataset.py       deterministic composition engine (CLI above)
  categories/            nine authored craft libraries (moves, problems, traps, themes)
validation/
  validate_dataset.py    machine-checks every hard constraint
data/                    generated dataset (JSONL + manifest)
```
