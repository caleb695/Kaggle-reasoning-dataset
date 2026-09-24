"""Compose the outline-conditioned writer-craft reasoning dataset.

Usage (from the repository root):
    python -m generator.build_dataset --size 6000 --seed 20260924

Every record is conditioned on one chapter of one novel outline. The request
carries the outline slice (frame, cast, rules, threads, chapter obligations and
state) plus the craft problem; the response reasons that problem through to a
set of decisions, ending with the single handoff line for transition examples.
All responses are structural and conceptual. No prose.

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
from generator.outlines import OUTLINES, validate_outlines
from generator.rules import RULES, rules_for_category
from generator.situations import (
    commitment_paragraph,
    render_outline_block,
    situation_paragraph,
)

TYPE_PREFIX = {"transition": "t", "reasoning": "r", "negative": "n"}

INSTRUCTION_FRAMES = {
    "transition": (
        "You are drafting this chapter now, from the outline above, and nothing about the plan is open for renegotiation.",
        "You are writing this chapter of the novel described above, inside its plan and its established state.",
        "You are at the desk with this chapter ahead of you: the outline is fixed, the chapter position is fixed, and the writing starts from the reasoning.",
        "You are beginning this chapter of the outlined novel, carrying the story's accumulated state into the scene.",
    ),
    "reasoning": (
        "You are planning the novel described above, and the question below concerns the book's architecture rather than one scene.",
        "You are working at the level of the whole book described above, deciding structure before any chapter is drafted.",
        "You are architecting the novel above; the decisions at stake govern the entire arc rather than a single chapter.",
        "You are in planning, with the outline above as the working material, settling the book's structural approach.",
    ),
    "negative": (
        "You are drafting this chapter of the outlined novel, and the pull described below is active in the writing right now.",
        "You are inside this chapter of the novel above, and the temptation below is the one the draft keeps offering.",
        "You are at the page for this chapter, where the weak shape below is currently the easiest available move.",
        "You are writing this chapter from the outline above and can feel the pull described below starting to operate.",
    ),
}


def build_instruction(rng, rec_type, outline, chapter, cat, item):
    """The request: outline slice, chapter obligations, and the craft problem."""
    block = render_outline_block(outline, chapter)
    heading = ("Novel outline:" if chapter is None
               else "Novel outline for the chapter you are about to write:")
    parts = [heading, block, ""]
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


def chapter_pools(outline_pool):
    """All chapter contexts, plus per-category pools whose craft pressure matches."""
    every = [(o, ch) for o in outline_pool for ch in o["chapters"]]
    aligned = {}
    for cat in CATEGORIES:
        prefs = set(CATEGORY_LENSES[cat["id"]])
        pool = [(o, ch) for o, ch in every if PRESSURE_LENS[ch["pressure"]] in prefs]
        aligned[cat["id"]] = pool or every
    return every, aligned


def choose_outline_chapter(rng, cat, every, aligned, align_rate=0.75):
    pool = aligned[cat["id"]] if rng.random() < align_rate else every
    outline, chapter = pick(rng, pool)
    return outline, chapter


def planning_lenses(rng, cat, rec_type, lens_use, quota):
    """Lead lens plus a second lens for arc-level planning records."""
    candidates = []
    for lens in list(CATEGORY_LENSES[cat["id"]]) + list(TYPE_LENSES[rec_type]):
        if lens not in candidates:
            candidates.append(lens)
    weight = {lens: 1.0 for lens in candidates}
    weight[candidates[0]] = 1.6
    scored = sorted(
        candidates,
        key=lambda lens: (lens_use[lens] / weight[lens], candidates.index(lens)),
    )
    lead = scored[0] if rng.random() < 0.85 else pick(rng, scored[:2])
    lenses = [lead]
    rest = [lens for lens in candidates if lens != lead]
    if rest and rng.random() < 0.75:
        lenses.append(min(rest, key=lambda lens: lens_use[lens]))
    lens_use.update(lenses[:1])
    return lenses[:1] + sorted(lenses[1:], key=LENS_ORDER.index)


def lenses_for(rng, cat, chapter, rec_type, lens_use, quota):
    """Choose the record's lenses: a lead lens plus the chapter's pressure lens.

    `lens_use` counts lead assignments only, so each lens in the registry leads
    its share of the dataset over the course of a build.

    The lead lens comes from the chapter's craft pressure when that lens is
    still under its share of the dataset, otherwise from the category or the
    record type, so every lens in the registry stays exercised. The chapter's
    pressure lens is always carried among the record's lenses.
    """
    pressure_lens = PRESSURE_LENS[chapter["pressure"]]
    candidates = [pressure_lens]
    for lens in list(CATEGORY_LENSES[cat["id"]]) + list(TYPE_LENSES[rec_type]):
        if lens not in candidates:
            candidates.append(lens)
    # The chapter's own craft pressure carries double weight, so it leads
    # whenever its share of the dataset is not already far ahead.
    weight = {lens: 1.0 for lens in candidates}
    weight[pressure_lens] = 2.0
    scored = sorted(
        candidates,
        key=lambda lens: (lens_use[lens] / weight[lens], candidates.index(lens)),
    )
    lead = scored[0] if rng.random() < 0.85 else pick(rng, scored[:2])
    rest = [lens for lens in candidates if lens != lead]
    if lead != pressure_lens:
        lenses = [lead, pressure_lens]
        extra = [lens for lens in rest if lens != pressure_lens]
        if extra and rng.random() < 0.5:
            lenses.append(pick(rng, extra))
    else:
        lenses = [lead]
        if rest and rng.random() < 0.7:
            lenses.append(min(rest, key=lambda lens: lens_use[lens]))
    lens_use.update(lenses[:1])
    return lenses[:1] + sorted(lenses[1:], key=LENS_ORDER.index)


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


def build_transition(rng, cat, every, aligned, used_text, used_combo, lens_use, quota):
    problem = pick(rng, cat["problems"])
    move_keys = list(cat["moves"].keys())
    for _ in range(600):
        outline, chapter = choose_outline_chapter(rng, cat, every, aligned)
        k = rng.choice((2, 2, 3))
        keys = ordered_subset(rng, move_keys, min(k, len(move_keys)))
        move_paras = tuple((key, rng.randrange(len(cat["moves"][key]))) for key in keys)
        opener_i = rng.randrange(len(problem["openers"]))
        closer_i = rng.randrange(len(problem["closers"]))
        lenses = lenses_for(rng, cat, chapter, "transition", lens_use, quota)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        combo = (
            problem["id"], problem["openers"][opener_i], move_paras, lens_paras, closer_i,
            outline["id"], chapter["n"],
        )
        if combo in used_combo:
            continue
        paragraphs = [
            situation_paragraph(outline, chapter, rng, "transition"),
            problem["openers"][opener_i],
        ]
        paragraphs.extend(cat["moves"][key][idx] for key, idx in move_paras)
        paragraphs.append(problem["closers"][closer_i])
        paragraphs.extend(LENSES[lens][i] for lens, i in zip(lenses, lens_paras))
        paragraphs.append(commitment_paragraph(outline, chapter, rng, "transition"))
        response = join_paragraphs(paragraphs) + "\n\n" + TRANSITION_LINE
        if response in used_text:
            continue
        instruction = build_instruction(rng, "transition", outline, chapter, cat, problem)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "transition", cat["id"], problem["id"], instruction, response,
            outline_id=outline["id"], chapter=chapter["n"],
            craft_pressure=chapter["pressure"], lenses=list(lenses),
            rules=tag_rules(cat, lenses),
        )
    raise RuntimeError("Could not build a unique transition example for " + cat["id"])


def build_reasoning(rng, cat, every, aligned, used_text, used_combo, lens_use, quota):
    theme = pick(rng, cat["themes"])
    middles = theme["middles"]
    take = max(2, len(middles) - 1) if len(middles) > 2 else len(middles)
    outlines = [o for o, _ in every]
    for _ in range(600):
        outline = pick(rng, outlines)
        opener_i = rng.randrange(len(theme["openers"]))
        closer_i = rng.randrange(len(theme["closers"]))
        principle_i = rng.randrange(len(cat["principles"]))
        keep = sorted(rng.sample(range(len(middles)), min(take, len(middles))))
        lenses = planning_lenses(rng, cat, "reasoning", lens_use, quota)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        combo = (
            theme["id"], opener_i, tuple(keep), principle_i, closer_i, lens_paras,
            outline["id"],
        )
        if combo in used_combo:
            continue
        paragraphs = [
            situation_paragraph(outline, None, rng, "reasoning"),
            theme["openers"][opener_i],
        ]
        paragraphs.extend(middles[i] for i in keep)
        paragraphs.append(cat["principles"][principle_i])
        paragraphs.extend(LENSES[lens][i] for lens, i in zip(lenses, lens_paras))
        paragraphs.append(theme["closers"][closer_i])
        paragraphs.append(commitment_paragraph(outline, None, rng, "reasoning"))
        response = join_paragraphs(paragraphs)
        if response in used_text:
            continue
        instruction = build_instruction(rng, "reasoning", outline, None, cat, theme)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "reasoning", cat["id"], theme["id"], instruction, response,
            outline_id=outline["id"], chapter=None,
            craft_pressure=None, lenses=list(lenses),
            rules=tag_rules(cat, lenses),
        )
    raise RuntimeError("Could not build a unique reasoning example for " + cat["id"])


def build_negative(rng, cat, every, aligned, used_text, used_combo, lens_use, quota):
    trap = pick(rng, cat["traps"])
    for _ in range(600):
        outline, chapter = choose_outline_chapter(rng, cat, every, aligned)
        opener_i = rng.randrange(len(trap["openers"]))
        closer_i = rng.randrange(len(trap["closers"]))
        discipline_i = rng.randrange(len(cat["discipline"]))
        lenses = lenses_for(rng, cat, chapter, "negative", lens_use, quota)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        combo = (
            trap["id"], opener_i, discipline_i, closer_i, lens_paras,
            outline["id"], chapter["n"],
        )
        if combo in used_combo:
            continue
        paragraphs = [
            situation_paragraph(outline, chapter, rng, "negative"),
            trap["openers"][opener_i],
            trap["damage"],
            cat["discipline"][discipline_i],
            trap["reason_past"],
        ]
        paragraphs.extend(LENSES[lens][i] for lens, i in zip(lenses, lens_paras))
        paragraphs.append(trap["closers"][closer_i])
        paragraphs.append(commitment_paragraph(outline, chapter, rng, "negative"))
        response = join_paragraphs(paragraphs)
        if response in used_text:
            continue
        instruction = build_instruction(rng, "negative", outline, chapter, cat, trap)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "negative", cat["id"], trap["id"], instruction, response,
            outline_id=outline["id"], chapter=chapter["n"],
            craft_pressure=chapter["pressure"], lenses=list(lenses),
            rules=tag_rules(cat, lenses),
        )
    raise RuntimeError("Could not build a unique negative example for " + cat["id"])


BUILDERS = {
    "transition": build_transition,
    "reasoning": build_reasoning,
    "negative": build_negative,
}


def distribute(count, items, rng):
    base = count // len(items)
    extra = count - base * len(items)
    order = list(items)
    rng.shuffle(order)
    pairs = []
    for i, item in enumerate(order):
        pairs.append((item, base + (1 if i < extra else 0)))
    return pairs


def build_dataset(size, seed, outline_pool=None):
    rng = random.Random(seed)
    outline_pool = list(outline_pool or OUTLINES)
    counts = {
        "transition": int(round(size * TYPE_RATIOS["transition"])),
        "reasoning": int(round(size * TYPE_RATIOS["reasoning"])),
    }
    counts["negative"] = size - counts["transition"] - counts["reasoning"]

    every, aligned = chapter_pools(outline_pool)
    used_text = set()
    used_combo = {t: set() for t in counts}
    lens_use = Counter()
    quota = max(1, int(size / len(LENS_ORDER)))
    records = {t: [] for t in counts}
    counters = {t: 0 for t in counts}

    for rec_type, total in counts.items():
        per_cat = distribute(total, CATEGORIES, rng)
        for cat, n in per_cat:
            for _ in range(n):
                rec = BUILDERS[rec_type](rng, cat, every, aligned, used_text,
                                         used_combo[rec_type], lens_use, quota)
                counters[rec_type] += 1
                rec["id"] = "%s-%s-%04d" % (
                    TYPE_PREFIX[rec_type],
                    cat["id"],
                    counters[rec_type],
                )
                records[rec_type].append(rec)

    return records, counts


def write_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=6000)
    parser.add_argument("--seed", type=int, default=20260924)
    parser.add_argument("--outdir", type=str, default="data")
    parser.add_argument("--no-splits", action="store_true",
                        help="write only dataset.jsonl, not the per-type files")
    args = parser.parse_args()

    if not (200 <= args.size <= 20000):
        raise SystemExit("size must be within the 2000-20000 supported range")

    validate_outlines()
    records, counts = build_dataset(args.size, args.seed)

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
    for rec in all_records:
        rule_counts.update(rec["rules"])

    manifest = {
        "seed": args.seed,
        "target_size": args.size,
        "counts": counts,
        "total": sum(counts.values()),
        "conditioning": {
            "outlines": len(OUTLINES),
            "chapters": sum(len(o["chapters"]) for o in OUTLINES),
        },
        "per_category": {
            cat["id"]: {
                rec_type: sum(1 for r in records[rec_type] if r["category"] == cat["id"])
                for rec_type in counts
            }
            for cat in CATEGORIES
        },
        "per_outline": dict(sorted(Counter(r["outline_id"] for r in all_records).items())),
        "per_rule": {str(k): rule_counts.get(k, 0) for k in sorted(RULES)},
    }
    with open(os.path.join(args.outdir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)

    print("Built %d examples (seed %d, %d outlines / %d chapter contexts)"
          % (manifest["total"], args.seed, len(OUTLINES),
             sum(len(o["chapters"]) for o in OUTLINES)))
    for rec_type, n in counts.items():
        print("  %-11s %5d" % (rec_type, n))
    for cat_id, c in manifest["per_category"].items():
        print("  %-22s t=%d r=%d n=%d" % (cat_id, c["transition"], c["reasoning"], c["negative"]))
    unweighted = [str(k) for k in sorted(RULES) if rule_counts.get(k, 0) == 0]
    if unweighted:
        print("  rules with no coverage: %s" % ", ".join(unweighted))


if __name__ == "__main__":
    main()
