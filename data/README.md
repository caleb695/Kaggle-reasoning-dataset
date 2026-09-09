# Dataset files

Instruction–response pairs that teach a fiction-writing model internalized,
generative writer-craft reasoning (plot architecture, conflict escalation,
character decisions, information management, scene and chapter construction,
long-range setup/payoff, tension, momentum, and epic-fantasy scale). All
responses are purely structural and conceptual — zero prose, zero exemplification.

## Files

| File | Records | Contents |
|---|---|---|
| `dataset.jsonl` | 2,400 | all examples, shuffled |
| `transition_examples.jsonl` | 1,200 | 50% — reasoning that ends with the handoff line `Given the above, the scene begins.` |
| `pure_reasoning_examples.jsonl` | 600 | 25% — arc-level structural craft reasoning, no handoff |
| `negative_examples.jsonl` | 600 | 25% — structural traps framed as live pulls to reason past while writing |
| `manifest.json` | — | seed, counts, per-category breakdown |

## Schema (one JSON object per line)

```json
{
  "id": "t-plo-0001",
  "type": "transition | reasoning | negative",
  "category": "plot_architecture",
  "subcategory": "point_of_attack",
  "instruction": "second-person writing situation + the structural task",
  "response": "pure structural/conceptual craft reasoning"
}
```

- `transition` responses end with exactly one handoff line and nothing after it.
- `reasoning` and `negative` responses end when the reasoning is complete.
- No double quotes, no illustrative prose, and no exemplification phrases appear
  in any instruction or response (machine-checked).

## Categories (10 × 240 examples each)

`plot_architecture`, `conflict_escalation`, `character_decisions`,
`information_management`, `scene_construction`, `chapter_arcs`, `setup_payoff`,
`tension`, `momentum`, `epic_scale` (worldbuilding pressure, magic as a priced
economy, prophecy vs. agency, sprawl control, series architecture).

## Quick load in a Kaggle notebook

```python
import pandas as pd

df = pd.read_json("/kaggle/input/<dataset-slug>/data/dataset.jsonl", lines=True)
print(df["type"].value_counts())
print(df[df.type == "transition"].iloc[0]["response"][-60:])
```

## Source & regeneration

Generated deterministically from the authored library in the source repository:

```
python -m generator.build_dataset --size 2400 --seed 20260909
```

Regenerating with a new seed or size (2000–3000) yields another valid sample of
the same content system. License: CC0 1.0 (see LICENSE at the repository root).
