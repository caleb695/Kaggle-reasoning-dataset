"""Compose the writer-craft reasoning dataset.

Usage (from the repository root):
    python -m generator.build_dataset --size 6400 --seed 20260924

Every record is a writing situation and the structural craft reasoning it
requires: decisions made while writing rather than post-hoc correction. The
reasoning is the whole of the training signal, and responses contain no prose.

At inference the model is also handed the novel outline it is about to draft.
That outline is supplied by the caller at request time and is deliberately not
part of these records, so the dataset stays a pure reasoning dataset and the
trained behavior does not depend on any particular outline text.

Optional: `--with-outlines` conditions each record on one chapter of the
authored outline bank in generator/outlines, for experiments that need the
outline in the training request itself.

Outputs JSONL files under data/. Fully deterministic for a given seed.
"""

import argparse
import json
import os
import random
from collections import Counter

from generator.categories import CATEGORIES
from generator.common import (
    NEGATIVE_TAILS,
    PLANNING_INTROS,
    REASONING_TAILS,
    TRANSITION_LINE,
    TRANSITION_TAILS,
    TYPE_RATIOS,
    join_paragraphs,
    make_record,
    ordered_subset,
    pick,
)
from generator.lenses import CATEGORY_LENSES, LENSES, LENS_ORDER, PRESSURE_LENS, TYPE_LENSES
from generator.rules import RULES, rules_for_category

TYPE_PREFIX = {"transition": "t", "reasoning": "r", "negative": "n"}

INSTRUCTION_FRAMES = {
    "transition": (
        "You are drafting the scene this problem is standing in the way of.",
        "You are writing the scene in front of you, and the problem below has to be settled before the first line.",
        "You are at the desk with the scene ahead of you and the problem below still open.",
        "You are inside the chapter where this problem has just surfaced.",
    ),
    "reasoning": (
        "You are planning the novel, and the question below concerns the book's architecture rather than one scene.",
        "You are working at the level of the whole book, deciding structure before any chapter is drafted.",
        "You are architecting the novel; the decisions at stake govern the entire arc rather than a single chapter.",
        "You are in planning, settling the book's structural approach.",
    ),
    "negative": (
        "You are drafting, and the pull described below is active in the writing right now.",
        "You are inside the chapter, and the temptation below is the one the draft keeps offering.",
        "You are at the page where the weak shape below is currently the easiest available move.",
        "You are writing and you can feel the pull described below starting to operate.",
    ),
}


def build_instruction(rng, rec_type, cat, item, ctx=None):
    """The request: the writing situation and the craft problem it raises.

    With `ctx` (an outline and chapter, used only by the optional outline mode)
    the request also carries the outline slice.
    """
    parts = []
    if ctx is not None:
        from generator.situations import render_outline_block

        outline, chapter = ctx
        heading = ("Novel outline:" if chapter is None
                   else "Novel outline for the chapter you are about to write:")
        parts.extend([heading, render_outline_block(outline, chapter), ""])
    parts.append(pick(rng, INSTRUCTION_FRAMES[rec_type]))
    if rec_type == "transition":
        parts.append(pick(rng, item["frames"]))
        parts.append(item["context"])
        parts.append("You are in " + pick(rng, item["stages"]) + ".")
        parts.append(pick(rng, TRANSITION_TAILS))
    elif rec_type == "reasoning":
        parts.append(pick(rng, item["frames"]))
        parts.append(item["question"])
        parts.append(pick(rng, PLANNING_INTROS))
        parts.append(pick(rng, REASONING_TAILS))
    else:
        parts.append(pick(rng, item["frames"]))
        parts.append(item["slide"])
        parts.append("You are in " + pick(rng, item["stages"]) + ".")
        parts.append(pick(rng, NEGATIVE_TAILS))
    return "\n".join(p for p in parts if p is not None)


def choose_lenses(rng, cat, rec_type, lens_use, quota, lead=None):
    """The record's cross-cutting lenses, balanced across the whole dataset.

    The lead lens comes from the category's own lens preferences (or, in
    outline mode, from the chapter's craft pressure), chosen so every lens in
    the registry leads its share of the dataset. `lens_use` counts lead
    assignments only.
    """
    candidates = []
    for lens in ([lead] if lead else []) + list(CATEGORY_LENSES[cat["id"]]) + list(TYPE_LENSES[rec_type]):
        if lens and lens not in candidates:
            candidates.append(lens)
    weight = {lens: 1.0 for lens in candidates}
    if lead:
        weight[lead] = 2.0
    else:
        weight[candidates[0]] = 1.6
    scored = sorted(
        candidates,
        key=lambda lens: (lens_use[lens] / weight[lens], candidates.index(lens)),
    )
    if lens_use[scored[0]] < quota and rng.random() < 0.85:
        chosen = [scored[0]]
    else:
        chosen = [pick(rng, scored[:2])]
    rest = [lens for lens in candidates if lens != chosen[0]]
    if rest:
        chosen.append(min(rest, key=lambda lens: lens_use[lens]))
    if rest and rng.random() < 0.7:
        extra = [lens for lens in rest if lens not in chosen]
        if extra:
            chosen.append(min(extra, key=lambda lens: lens_use[lens]))
    # In outline mode the chapter's own craft pressure always travels with the
    # record, whatever else was chosen.
    if lead and lead not in chosen:
        if len(chosen) > 1:
            chosen[1] = lead
        else:
            chosen.append(lead)
    lens_use.update(chosen[:1])
    return chosen[:1] + sorted(chosen[1:], key=LENS_ORDER.index)


def lens_paragraphs(rng, lenses):
    return [LENSES[lens][rng.randrange(len(LENSES[lens]))] for lens in lenses]


def tag_rules(cat, lenses):
    """The registry rules this record encodes.

    Normally the rules routed to the record's authored category. The two
    cross-cutting categories carry no rules of their own, so they fall back to
    the rules routed to the lead lens, which is what those records reason with.
    """
    rules = rules_for_category(cat["id"])
    if not rules:
        rules = [rid for rid, spec in RULES.items() if spec[2] == lenses[0]]
    return sorted(rules)


def build_transition(rng, cat, ctx, used_text, used_combo, lens_use, quota):
    problem = pick(rng, cat["problems"])
    move_keys = list(cat["moves"].keys())
    for _ in range(600):
        outline, chapter = ctx if ctx is not None else (None, None)
        k = rng.choice((2, 2, 3))
        keys = ordered_subset(rng, move_keys, min(k, len(move_keys)))
        move_paras = tuple((key, rng.randrange(len(cat["moves"][key]))) for key in keys)
        opener_i = rng.randrange(len(problem["openers"]))
        closer_i = rng.randrange(len(problem["closers"]))
        lead = PRESSURE_LENS[chapter["pressure"]] if chapter else None
        lenses = choose_lenses(rng, cat, "transition", lens_use, quota, lead=lead)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        combo = (
            problem["id"], problem["openers"][opener_i], move_paras, lens_paras, closer_i,
            outline["id"] if outline else None,
            chapter["n"] if chapter else None,
        )
        if combo in used_combo:
            continue
        paragraphs = []
        if ctx is not None:
            from generator.situations import situation_paragraph

            paragraphs.append(situation_paragraph(outline, chapter, rng, "transition"))
        paragraphs.append(problem["openers"][opener_i])
        paragraphs.extend(cat["moves"][key][idx] for key, idx in move_paras)
        paragraphs.extend(lens_paragraphs(rng, lenses))
        paragraphs.append(problem["closers"][closer_i])
        response = join_paragraphs(paragraphs) + "\n\n" + TRANSITION_LINE
        if response in used_text:
            continue
        instruction = build_instruction(rng, "transition", cat, problem, ctx)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "transition", cat["id"], problem["id"], instruction, response,
            lenses=list(lenses), rules=tag_rules(cat, lenses),
            **outline_fields(outline, chapter),
        )
    raise RuntimeError("Could not build a unique transition example for " + cat["id"])


def build_reasoning(rng, cat, ctx, used_text, used_combo, lens_use, quota):
    theme = pick(rng, cat["themes"])
    middles = theme["middles"]
    take = max(2, len(middles) - 1) if len(middles) > 2 else len(middles)
    for _ in range(600):
        outline, chapter = ctx if ctx is not None else (None, None)
        opener_i = rng.randrange(len(theme["openers"]))
        closer_i = rng.randrange(len(theme["closers"]))
        principle_i = rng.randrange(len(cat["principles"]))
        keep = sorted(rng.sample(range(len(middles)), min(take, len(middles))))
        lenses = choose_lenses(rng, cat, "reasoning", lens_use, quota)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        combo = (
            theme["id"], opener_i, tuple(keep), principle_i, closer_i, lens_paras,
            outline["id"] if outline else None,
        )
        if combo in used_combo:
            continue
        paragraphs = []
        if ctx is not None:
            from generator.situations import situation_paragraph

            paragraphs.append(situation_paragraph(outline, chapter, rng, "reasoning"))
        paragraphs.append(theme["openers"][opener_i])
        paragraphs.extend(middles[i] for i in keep)
        paragraphs.append(cat["principles"][principle_i])
        paragraphs.extend(lens_paragraphs(rng, lenses))
        paragraphs.append(theme["closers"][closer_i])
        response = join_paragraphs(paragraphs)
        if response in used_text:
            continue
        instruction = build_instruction(rng, "reasoning", cat, theme, ctx)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "reasoning", cat["id"], theme["id"], instruction, response,
            lenses=list(lenses), rules=tag_rules(cat, lenses),
            **outline_fields(outline, None),
        )
    raise RuntimeError("Could not build a unique reasoning example for " + cat["id"])


def build_negative(rng, cat, ctx, used_text, used_combo, lens_use, quota):
    trap = pick(rng, cat["traps"])
    for _ in range(600):
        outline, chapter = ctx if ctx is not None else (None, None)
        opener_i = rng.randrange(len(trap["openers"]))
        closer_i = rng.randrange(len(trap["closers"]))
        discipline_i = rng.randrange(len(cat["discipline"]))
        lead = PRESSURE_LENS[chapter["pressure"]] if chapter else None
        lenses = choose_lenses(rng, cat, "negative", lens_use, quota, lead=lead)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        combo = (
            trap["id"], opener_i, discipline_i, closer_i, lens_paras,
            outline["id"] if outline else None,
            chapter["n"] if chapter else None,
        )
        if combo in used_combo:
            continue
        paragraphs = []
        if ctx is not None:
            from generator.situations import situation_paragraph

            paragraphs.append(situation_paragraph(outline, chapter, rng, "negative"))
        paragraphs.append(trap["openers"][opener_i])
        paragraphs.append(trap["damage"])
        paragraphs.append(cat["discipline"][discipline_i])
        paragraphs.append(trap["reason_past"])
        paragraphs.extend(lens_paragraphs(rng, lenses))
        paragraphs.append(trap["closers"][closer_i])
        response = join_paragraphs(paragraphs)
        if response in used_text:
            continue
        instruction = build_instruction(rng, "negative", cat, trap, ctx)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "negative", cat["id"], trap["id"], instruction, response,
            lenses=list(lenses), rules=tag_rules(cat, lenses),
            **outline_fields(outline, chapter),
        )
    raise RuntimeError("Could not build a unique negative example for " + cat["id"])


def outline_fields(outline, chapter):
    """Outline metadata, written only when the optional outline mode is on."""
    if outline is None:
        return {}
    fields = {"outline_id": outline["id"], "chapter": chapter["n"] if chapter else None}
    if chapter is not None:
        fields["craft_pressure"] = chapter["pressure"]
    return fields


BUILDERS = {
    "transition": build_transition,
    "reasoning": build_reasoning,
    "negative": build_negative,
}


def context_pools(with_outlines):
    """The chapter-context pools for the optional outline mode."""
    if not with_outlines:
        return None
    from generator.outlines import OUTLINES

    everything = [(o, ch) for o in OUTLINES for ch in o["chapters"]]
    aligned = {}
    for cat in CATEGORIES:
        prefs = set(CATEGORY_LENSES[cat["id"]])
        pool = [(o, ch) for o, ch in everything if PRESSURE_LENS[ch["pressure"]] in prefs]
        aligned[cat["id"]] = pool or everything
    return everything, aligned


def pick_context(rng, cat, pools, align_rate=0.75):
    if pools is None:
        return None
    everything, aligned = pools
    pool = aligned[cat["id"]] if rng.random() < align_rate else everything
    return pick(rng, pool)


def distribute(count, items, rng):
    base = count // len(items)
    extra = count - base * len(items)
    order = list(items)
    rng.shuffle(order)
    pairs = []
    for i, item in enumerate(order):
        pairs.append((item, base + (1 if i < extra else 0)))
    return pairs


def build_dataset(size, seed, with_outlines=False):
    rng = random.Random(seed)

    counts = {
        "transition": int(round(size * TYPE_RATIOS["transition"])),
        "reasoning": int(round(size * TYPE_RATIOS["reasoning"])),
    }
    counts["negative"] = size - counts["transition"] - counts["reasoning"]

    pools = context_pools(with_outlines)
    if with_outlines:
        from generator.outlines import validate_outlines

        validate_outlines()

    used_text = set()
    used_combo = {t: set() for t in counts}
    lens_use = Counter()
    quota = max(1, int(size / len(LENS_ORDER)))
    records = {t: [] for t in counts}
    counters = {t: 0 for t in counts}

    for rec_type, total in counts.items():
        for cat, n in distribute(total, CATEGORIES, rng):
            for _ in range(n):
                ctx = pick_context(rng, cat, pools)
                rec = BUILDERS[rec_type](rng, cat, ctx, used_text, used_combo[rec_type],
                                         lens_use, quota)
                counters[rec_type] += 1
                rec["id"] = "%s-%s-%04d" % (TYPE_PREFIX[rec_type], cat["id"], counters[rec_type])
                records[rec_type].append(rec)

    return records, counts


def write_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=6400)
    parser.add_argument("--seed", type=int, default=20260924)
    parser.add_argument("--outdir", type=str, default="data")
    parser.add_argument("--no-splits", action="store_true",
                        help="write only dataset.jsonl, not the per-type files")
    parser.add_argument("--with-outlines", action="store_true",
                        help="optional: condition every record on a chapter of the outline bank")
    args = parser.parse_args()

    if not (200 <= args.size <= 20000):
        raise SystemExit("size must be within the 200-20000 supported range")

    records, counts = build_dataset(args.size, args.seed, with_outlines=args.with_outlines)

    os.makedirs(args.outdir, exist_ok=True)
    all_records = []
    fnames = {
        "transition": "transition_examples.jsonl",
        "reasoning": "pure_reasoning_examples.jsonl",
        "negative": "negative_examples.jsonl",
    }
    for rec_type in ("transition", "reasoning", "negative"):
        recs = records[rec_type]
        all_records.extend(recs)
        if not args.no_splits:
            write_jsonl(os.path.join(args.outdir, fnames[rec_type]), recs)

    rng = random.Random(args.seed + 1)
    rng.shuffle(all_records)
    write_jsonl(os.path.join(args.outdir, "dataset.jsonl"), all_records)

    rule_counts = Counter()
    lens_counts = Counter()
    for rec in all_records:
        rule_counts.update(rec["rules"])
        lens_counts.update(rec["lenses"])

    manifest = {
        "seed": args.seed,
        "target_size": args.size,
        "counts": counts,
        "total": sum(counts.values()),
        "conditioning": "outline bank" if args.with_outlines else "none (reasoning only)",
        "per_category": {
            cat["id"]: {
                rec_type: sum(1 for r in records[rec_type] if r["category"] == cat["id"])
                for rec_type in counts
            }
            for cat in CATEGORIES
        },
        "per_lens": dict(lens_counts.most_common()),
        "per_rule": {str(k): rule_counts.get(k, 0) for k in sorted(RULES)},
    }
    if args.with_outlines:
        manifest["per_outline"] = dict(sorted(
            Counter(r["outline_id"] for r in all_records).items()))
    with open(os.path.join(args.outdir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)

    print("Built %d examples (seed %d, %s)"
          % (manifest["total"], args.seed, manifest["conditioning"]))
    for rec_type, n in counts.items():
        print("  %-11s %5d" % (rec_type, n))
    thin = [cat_id for cat_id, c in manifest["per_category"].items()
            if min(c.values()) < 10]
    if thin:
        print("  categories with thin coverage: %s" % ", ".join(thin))
    missing = [str(k) for k in sorted(RULES) if rule_counts.get(k, 0) == 0]
    if missing:
        print("  rules with no coverage: %s" % ", ".join(missing))
    unused = [lens for lens in LENS_ORDER if lens_counts.get(lens, 0) == 0]
    if unused:
        print("  lenses with no coverage: %s" % ", ".join(unused))


if __name__ == "__main__":
    main()
