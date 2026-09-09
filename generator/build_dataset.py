"""Compose the writer-craft reasoning dataset from the authored content library.

Usage (from the repository root):
    python -m generator.build_dataset --size 2400 --seed 20260909

Outputs JSONL files under data/. Fully deterministic for a given seed.
"""

import argparse
import json
import os
import random

from generator.common import (
    NEGATIVE_TAILS,
    PLANNING_INTROS,
    REASONING_TAILS,
    INTROS,
    TRANSITION_LINE,
    TRANSITION_TAILS,
    TYPE_RATIOS,
    build_instruction,
    distribute,
    join_paragraphs,
    make_record,
    ordered_subset,
    pick,
)
from generator.categories import CATEGORIES


def build_transition(rng, cat, used_text, used_combo):
    """One transition example: problem opener -> ordered move paragraphs ->
    commitment closer -> the single handoff marker."""
    problem = pick(rng, cat["problems"])
    move_keys = list(cat["moves"].keys())
    for _ in range(400):
        opener_i = rng.randrange(len(problem["openers"]))
        closer_i = rng.randrange(len(problem["closers"]))
        k = rng.choice((3, 4)) if len(move_keys) >= 4 else len(move_keys)
        keys = ordered_subset(rng, move_keys, k)
        move_paras = tuple((key, rng.randrange(len(cat["moves"][key]))) for key in keys)
        combo = (problem["id"], opener_i, move_paras, closer_i)
        if combo in used_combo:
            continue
        paragraphs = [problem["openers"][opener_i]]
        paragraphs.extend(cat["moves"][key][idx] for key, idx in move_paras)
        paragraphs.append(problem["closers"][closer_i])
        response = join_paragraphs(paragraphs) + "\n\n" + TRANSITION_LINE
        if response in used_text:
            continue
        stage = pick(rng, problem["stages"])
        instruction = build_instruction(
            rng, INTROS, pick(rng, problem["frames"]), problem["context"], stage,
            pick(rng, TRANSITION_TAILS),
        )
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "transition", cat["id"], problem["id"], instruction, response
        )
    raise RuntimeError("Could not build a unique transition example for " + cat["id"])


def build_reasoning(rng, cat, used_text, used_combo):
    """One pure reasoning example: theme opener -> theme middles -> shared
    principle -> theme closer. No marker; ends when the reasoning ends."""
    theme = pick(rng, cat["themes"])
    middles = theme["middles"]
    take = len(middles) - 1 if len(middles) > 3 else len(middles)
    for _ in range(400):
        opener_i = rng.randrange(len(theme["openers"]))
        closer_i = rng.randrange(len(theme["closers"]))
        principle_i = rng.randrange(len(cat["principles"]))
        keep = sorted(rng.sample(range(len(middles)), take))
        combo = (theme["id"], opener_i, tuple(keep), principle_i, closer_i)
        if combo in used_combo:
            continue
        paragraphs = [theme["openers"][opener_i]]
        paragraphs.extend(middles[i] for i in keep)
        paragraphs.append(cat["principles"][principle_i])
        paragraphs.append(theme["closers"][closer_i])
        response = join_paragraphs(paragraphs)
        if response in used_text:
            continue
        instruction = build_instruction(
            rng, PLANNING_INTROS, pick(rng, theme["frames"]), theme["question"], None,
            pick(rng, REASONING_TAILS),
        )
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "reasoning", cat["id"], theme["id"], instruction, response
        )
    raise RuntimeError("Could not build a unique reasoning example for " + cat["id"])


def build_negative(rng, cat, used_text, used_combo):
    """One negative example: trap opener -> damage -> shared discipline check ->
    replacement reasoning -> commitment closer. Forward-oriented throughout."""
    trap = pick(rng, cat["traps"])
    for _ in range(400):
        opener_i = rng.randrange(len(trap["openers"]))
        closer_i = rng.randrange(len(trap["closers"]))
        discipline_i = rng.randrange(len(cat["discipline"]))
        combo = (trap["id"], opener_i, discipline_i, closer_i)
        if combo in used_combo:
            continue
        paragraphs = [
            trap["openers"][opener_i],
            trap["damage"],
            cat["discipline"][discipline_i],
            trap["reason_past"],
            trap["closers"][closer_i],
        ]
        response = join_paragraphs(paragraphs)
        if response in used_text:
            continue
        stage = pick(rng, trap["stages"])
        instruction = build_instruction(
            rng, INTROS, pick(rng, trap["frames"]), trap["slide"], stage,
            pick(rng, NEGATIVE_TAILS),
        )
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "negative", cat["id"], trap["id"], instruction, response
        )
    raise RuntimeError("Could not build a unique negative example for " + cat["id"])


BUILDERS = {
    "transition": build_transition,
    "reasoning": build_reasoning,
    "negative": build_negative,
}


def build_dataset(size, seed):
    rng = random.Random(seed)
    counts = {
        "transition": round(size * TYPE_RATIOS["transition"]),
        "reasoning": round(size * TYPE_RATIOS["reasoning"]),
    }
    counts["negative"] = size - counts["transition"] - counts["reasoning"]

    used_text = set()
    used_combo = {t: set() for t in counts}
    records = {t: [] for t in counts}
    counters = {t: 0 for t in counts}

    for rec_type, total in counts.items():
        per_cat = distribute(total, CATEGORIES, rng)
        for cat, n in per_cat:
            for _ in range(n):
                rec = BUILDERS[rec_type](rng, cat, used_text, used_combo[rec_type])
                counters[rec_type] += 1
                prefix = {"transition": "t", "reasoning": "r", "negative": "n"}[rec_type]
                rec["id"] = "%s-%s-%04d" % (
                    prefix, cat["id"][:3].replace("_", ""), counters[rec_type]
                )
                records[rec_type].append(rec)

    return records, counts


def write_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=2400)
    parser.add_argument("--seed", type=int, default=20260909)
    parser.add_argument("--outdir", type=str, default="data")
    args = parser.parse_args()

    if not (2000 <= args.size <= 3000):
        raise SystemExit("size must be within the 2000-3000 target range")

    records, counts = build_dataset(args.size, args.seed)

    os.makedirs(args.outdir, exist_ok=True)
    all_records = []
    for rec_type in ("transition", "reasoning", "negative"):
        recs = records[rec_type]
        all_records.extend(recs)
        fname = {
            "transition": "transition_examples.jsonl",
            "reasoning": "pure_reasoning_examples.jsonl",
            "negative": "negative_examples.jsonl",
        }[rec_type]
        write_jsonl(os.path.join(args.outdir, fname), recs)

    rng = random.Random(args.seed + 1)
    rng.shuffle(all_records)
    write_jsonl(os.path.join(args.outdir, "dataset.jsonl"), all_records)

    manifest = {
        "seed": args.seed,
        "target_size": args.size,
        "counts": counts,
        "total": sum(counts.values()),
        "per_category": {
            cat["id"]: {
                rec_type: sum(1 for r in records[rec_type] if r["category"] == cat["id"])
                for rec_type in counts
            }
            for cat in CATEGORIES

        },
    }
    with open(os.path.join(args.outdir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)

    print("Built %d examples (seed %d)" % (manifest["total"], args.seed))
    for rec_type, n in counts.items():
        print("  %-11s %5d" % (rec_type, n))
    for cat_id, c in manifest["per_category"].items():
        print("  %-24s t=%d r=%d n=%d" % (cat_id, c["transition"], c["reasoning"], c["negative"]))


if __name__ == "__main__":
    main()
