# Dataset files

Instruction–response pairs that teach a fiction-writing model internalized, generative
writer-craft reasoning about a novel it is about to draft. Every request carries an
outline of the book (or of the specific chapter) as context; every response is purely
structural and conceptual craft reasoning — zero prose, zero exemplification.

## Files

| File | Records | Contents |
|---|---|---|
| `dataset.jsonl` | 6,400 | all examples, shuffled |
| `transition_examples.jsonl` | 3,200 | 50% — chapter-conditioned reasoning that ends with the handoff line `Given the above, the scene begins.` |
| `pure_reasoning_examples.jsonl` | 1,600 | 25% — whole-book (arc-level) structural craft reasoning, no handoff |
| `negative_examples.jsonl` | 1,600 | 25% — structural traps framed as live pulls to reason past while writing, no handoff |
| `manifest.json` | — | seed, counts, per-category, per-outline and per-rule coverage |

## Schema (one JSON object per line)

```json
{
  "id": "t-tension-1646",
  "type": "transition | reasoning | negative",
  "category": "tension",
  "subcategory": "post_twist_reset",
  "instruction": "outline context + the writing situation",
  "response": "pure structural/conceptual craft reasoning",
  "outline_id": "the_long_shift",
  "chapter": 5,
  "craft_pressure": "emotion",
  "lenses": ["emotion", "continuity"],
  "rules": [111, 176, 177, 259]
}
```

- `instruction` embeds the outline: title, form and genre, POV and distance, premise, world
  rules, the cast in play with wants, flaws, secrets and knowledge, open threads with their
  setup and payoff chapters, and then either the chapter's obligations, beats, entry and
  exit state and craft pressure, or the whole-book planning scope for `reasoning` records.
- `response` opens by reading the outline as structural obligations, works the craft
  problem, adds one to three cross-cutting lens paragraphs, and closes with the decisions
  to carry into the draft.
- `transition` responses end with exactly one handoff line and nothing after it;
  `reasoning` and `negative` responses end when the reasoning is complete.
- `chapter` and `craft_pressure` are `null` for `reasoning` records: they are planned at the
  level of the whole book rather than of one chapter.
- `lenses` names the craft dimensions the record reasons through (the first is the lead
  lens, and for chapter-bound records the chapter's own craft pressure is always among
  them). `rules` lists the 260-rule registry ids the record's category encodes.
- No double quotes, no curly quotes, no illustrative prose, and no exemplification phrases
  appear in any instruction or response (machine-checked by `validation/validate_dataset.py`).

## Categories (18, about 355 examples each)

`plot_architecture`, `conflict_escalation`, `character_decisions`,
`information_management`, `scene_construction`, `chapter_arcs`, `setup_payoff`,
`tension`, `momentum`, `epic_scale`, `pov_perception`, `concrete_grounding`,
`prose_discipline`, `metaphor_imagery`, `emotion_craft`, `dialogue_voice`,
`action_physicality`, `continuity_outline`.

## Outline bank

36 standalone novel outlines across fantasy, horror, science fiction, crime,
literary/historical, romance, survival, young adult, dystopian, workplace and western
forms. Each outline carries a fixed 10-chapter spine with per-chapter function, required
beats, entry state, exit state and a craft-pressure tag, so every chapter request is
concrete: 360 chapter contexts in total, each used 128–210 times across the dataset.

## Quick load in a Kaggle notebook

```python
import pandas as pd

df = pd.read_json("/kaggle/input/<dataset-slug>/data/dataset.jsonl", lines=True)
print(df["type"].value_counts())
print(df[df.category == "dialogue_voice"].iloc[0]["instruction"].split("\n")[0])
print(df[df.type == "transition"].iloc[0]["response"][-40:])
```

## Source & regeneration

Generated deterministically from the authored craft libraries, the 36-outline bank and the
17 lens pools in the source repository:

```
python -m generator.build_dataset --size 6400 --seed 20260924
python -m validation.validate_dataset data/dataset.jsonl
```

Regenerating with a new seed or size (2,000–20,000 supported; the shipped dataset is
6,400) yields another valid sample of the same content system. License: CC0 1.0 (see
LICENSE at the repository root).
