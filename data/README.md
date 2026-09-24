# Dataset files

Instruction–response pairs that teach a fiction-writing model internalized, generative
writer-craft reasoning across the whole process of writing a novel: developing an idea,
designing its architecture, drafting a chapter of it against an outline, and revising it.
Every response is purely structural and conceptual — zero prose, zero exemplification.

At inference the caller supplies the novel outline being drafted along with a situation
prompt; the outline is request-time input and is not part of these records, so the training
data stays reasoning-only.

## Files

| File | Records | Contents |
|---|---|---|
| `dataset.jsonl` | 7,200 | all examples, shuffled |
| `transition_examples.jsonl` | 3,600 | 50% — chapter craft reasoning that ends with the handoff line `Given the above, the scene begins.` |
| `pure_reasoning_examples.jsonl` | 1,800 | 25% — structural craft reasoning, no handoff |
| `negative_examples.jsonl` | 1,800 | 25% — structural traps framed as live pulls to reason past while generating |
| `manifest.json` | — | seed, counts, stage / depth / difficulty / strategy / category / lens / rule coverage |

## Schema (one JSON object per line)

```json
{
  "id": "n-tension-0180",
  "type": "transition | reasoning | negative",
  "stage": "ideation | outline | drafting | revision",
  "category": "tension",
  "subcategory": "post_twist_reset",
  "instruction": "stage frame + the writing situation and the craft problem + the no-prose contract",
  "response": "pure structural/conceptual craft reasoning",
  "depth": "terse | standard | deep",
  "difficulty": "foundational | intermediate | advanced",
  "lenses": ["continuity", "emotion"],
  "strategies": ["pre_mortem", "reader_model"],
  "rules": [111, 176, 177, 259]
}
```

- `stage` places the reasoning in the writing process, and each stage reasons only with the
  libraries that belong to its own work: brainstorming (`idea_generation`, `idea_shaping`),
  outlining (`outline_design`, `arc_mapping`, `scene_planning` plus the structural libraries),
  writing (the eighteen craft libraries), revision (`revision_craft`, `revision_diagnosis`).
  Brainstorming and revision use nothing else. `transition` records exist only at `drafting`,
  where writing follows, and the reasoning in every stage is written in the voice of that
  activity rather than in the voice of a process.
- `depth` controls the trace's size and demand: terse settles one decision (190–343 words),
  standard settles several with one named strategy (245–506 words), deep carries
  interacting decisions plus a check (281–625 words). `difficulty` follows the tier.
- `strategies` names the reusable reasoning moves used in the response: `two_routes`,
  `backward`, `cost_ledger`, `pre_mortem`, `constraints_as_conditions`, `weakest_link`,
  `reader_model`, `ordering`, `verify`.
- `lenses` names the craft dimensions the record reasons through, in canonical paragraph
  order; `rules` lists the 260-rule registry ids the record's category encodes.
- `transition` responses end with exactly one handoff line and nothing after it;
  `reasoning` and `negative` responses end when the reasoning is complete.
- No double quotes, no curly quotes, no illustrative prose, and no exemplification phrases
  appear in any instruction or response (machine-checked by `validation/validate_dataset.py`).

## Coverage

**Stages:** `ideation` 900, `outline` 1,260, `drafting` 4,320, `revision` 720.

**Depths:** `terse` 1,573, `standard` 3,771, `deep` 1,856.

**Categories (25, roughly 290 examples each):** the eighteen drafting libraries
(`plot_architecture`, `conflict_escalation`, `character_decisions`,
`information_management`, `scene_construction`, `chapter_arcs`, `setup_payoff`, `tension`,
`momentum`, `epic_scale`, `pov_perception`, `concrete_grounding`, `prose_discipline`,
`metaphor_imagery`, `emotion_craft`, `dialogue_voice`, `action_physicality`,
`continuity_outline`) plus seven stage-native libraries: `idea_generation` and
`idea_shaping` for brainstorming, `outline_design`, `arc_mapping` and `scene_planning` for
outlining, `revision_craft` and `revision_diagnosis` for revision. Each stage reasons only
with the libraries that belong to it, and its own libraries carry 65% of its records.

## Quick load in a Kaggle notebook

```python
import pandas as pd

df = pd.read_json("/kaggle/input/<dataset-slug>/data/dataset.jsonl", lines=True)
print(df["type"].value_counts())
print(df.groupby(["stage", "type"]).size())
print(df[df.stage == "ideation"].iloc[0]["instruction"])
print(df[df.type == "transition"].iloc[0]["response"][-40:])
```

## Source & regeneration

Generated deterministically from the authored craft libraries, the four process stages,
the nine reasoning strategies, and the 17 lens pools in the source repository:

```
python -m generator.build_dataset --size 7200 --seed 20260924
python -m validation.validate_dataset data/dataset.jsonl
```

Regenerating with a new seed or size (200–20,000 supported; the shipped dataset is 7,200)
yields another valid sample of the same content system. License: CC0 1.0 (see LICENSE at
the repository root). The reasoning behind the current build, with examples, is documented
in `docs/IMPROVEMENTS.md`.
