# Dataset files

Instruction–response pairs that teach a fiction-writing model internalized, generative
writer-craft reasoning: the structural thinking to do before writing, not post-hoc
analysis. This is a reasoning dataset — every response is purely structural and
conceptual, with zero prose and zero exemplification.

At inference the caller supplies the novel outline being drafted along with a situation
prompt; the outline is request-time input and is not part of these records, so the training
data stays reasoning-only.

## Files

| File | Records | Contents |
|---|---|---|
| `dataset.jsonl` | 6,400 | all examples, shuffled |
| `transition_examples.jsonl` | 3,200 | 50% — reasoning that ends with the handoff line `Given the above, the scene begins.` |
| `pure_reasoning_examples.jsonl` | 1,600 | 25% — arc-level structural craft reasoning, no handoff |
| `negative_examples.jsonl` | 1,600 | 25% — structural traps framed as live pulls to reason past while writing, no handoff |
| `manifest.json` | — | seed, counts, per-category, per-lens and per-rule coverage |

## Schema (one JSON object per line)

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

- `instruction` is a second-person writing situation: the frame of the moment, the craft
  problem (or trap, or arc-level question), where in the work the writer is, and the push to
  reason it through in full. At inference the outline being drafted is prepended to an
  instruction of this shape.
- `response` opens on the craft problem, works it through the category's reasoning, adds one
  to three cross-cutting lens paragraphs, and closes on what to carry into the writing.
- `transition` responses end with exactly one handoff line and nothing after it;
  `reasoning` and `negative` responses end when the reasoning is complete.
- `lenses` names the craft dimensions the record reasons through, in canonical paragraph
  order; `rules` lists the 260-rule registry ids the record's category encodes.
- No double quotes, no curly quotes, no illustrative prose, and no exemplification phrases
  appear in any instruction or response (machine-checked by `validation/validate_dataset.py`).

## Categories (18, about 355 examples each)

`plot_architecture`, `conflict_escalation`, `character_decisions`,
`information_management`, `scene_construction`, `chapter_arcs`, `setup_payoff`,
`tension`, `momentum`, `epic_scale`, `pov_perception`, `concrete_grounding`,
`prose_discipline`, `metaphor_imagery`, `emotion_craft`, `dialogue_voice`,
`action_physicality`, `continuity_outline`.

## Quick load in a Kaggle notebook

```python
import pandas as pd

df = pd.read_json("/kaggle/input/<dataset-slug>/data/dataset.jsonl", lines=True)
print(df["type"].value_counts())
print(df[df.category == "dialogue_voice"].iloc[0]["instruction"])
print(df[df.type == "transition"].iloc[0]["response"][-40:])
```

## Source & regeneration

Generated deterministically from the authored craft libraries and the 17 lens pools in the
source repository:

```
python -m generator.build_dataset --size 6400 --seed 20260924
python -m validation.validate_dataset data/dataset.jsonl
```

Regenerating with a new seed or size (2,000–20,000 supported; the shipped dataset is
6,400) yields another valid sample of the same content system. License: CC0 1.0 (see
LICENSE at the repository root).
