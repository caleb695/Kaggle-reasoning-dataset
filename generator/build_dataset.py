"""Compose the writer-craft reasoning dataset.

Usage (from the repository root):
    python -m generator.build_dataset --size 7200 --seed 20260924

Records cover the whole process of writing a novel, not only the drafting moment:

    ideation  ->  brainstorming: finding an idea that makes a story
    outline   ->  outlining: building a story that works, from first page to last
    drafting  ->  writing: how the chapter in front of you gets written
    revision  ->  revising: what to change, what to keep, and what to do first

Three record types:

    transition  50%  chapter craft reasoning that hands off into writing, ending
                     with the single line Given the above, the scene begins.
                     Drafting stage only, because that is where writing follows.
    reasoning   25%  structural reasoning that ends when the decisions are made
    negative    25%  forward-oriented traps reasoned past while generating

Quality controls baked into the composition:

  * depth tiers (terse / standard / deep) so traces are not uniformly long, which
    is how reasoning data teaches verbosity rather than judgement
  * reasoning strategies (two-routes, backward, cost ledger, pre-mortem,
    constraint conditions, weakest link, reader model, ordering, verify) tagged
    per record, because strategy diversity transfers better than topic diversity
  * difficulty tiers, with advanced records combining more interacting decisions
  * stage-native craft libraries loaded at their own stage, so ideation reasons
    about ideas, outlining about structure, and revision about repair
  * unique instruction and response text, balanced lens coverage, and an
    explicit no-prose contract in every instruction

At inference the caller supplies the novel outline being drafted. That outline is
deliberately not part of these records: the dataset is reasoning supervision, and
the trained behavior does not depend on any particular story.

Optional: `--with-outlines` conditions each record on one chapter of the authored
outline bank in generator/outlines, for experiments that need outline text in the
training request itself.

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
    REASONING_TAILS,
    TRANSITION_LINE,
    TRANSITION_TAILS,
    TYPE_RATIOS,
    join_paragraphs,
    make_record,
    ordered_subset,
    pick,
)
from generator import stages as ST
from generator.lenses import CATEGORY_LENSES, LENSES, LENS_ORDER, PRESSURE_LENS, TYPE_LENSES
from generator.lenses_stage import STAGE_LENSES, lens_bank
from generator.rules import RULES, rules_for_category
from generator.strategies import STRATEGIES, TYPE_STRATEGIES

TYPE_PREFIX = {"transition": "t", "reasoning": "r", "negative": "n"}

DRAFTING_ONLY = "drafting"

# Stage mix for the reasoning and negative slices. Transition records are all
# drafting, since the handoff line exists to separate planning from writing.
STAGE_MIX = {
    "reasoning": (("outline", 0.35), ("ideation", 0.25), ("drafting", 0.20), ("revision", 0.20)),
    "negative": (("outline", 0.35), ("ideation", 0.25), ("drafting", 0.20), ("revision", 0.20)),
    "transition": (("drafting", 1.0),),
}

DEPTHS = (("terse", 0.30), ("standard", 0.45), ("deep", 0.25))

CATEGORY_BY_ID = {cat["id"]: cat for cat in CATEGORIES}


def weighted_choice(rng, pairs):
    total = sum(weight for _, weight in pairs)
    target = rng.random() * total
    upto = 0.0
    for item, weight in pairs:
        upto += weight
        if target <= upto:
            return item
    return pairs[-1][0]


# ---------------------------------------------------------------------------
# Instructions
# ---------------------------------------------------------------------------


def build_instruction(rng, rec_type, stage, cat, item, ctx=None):
    """The request: stage frame, the craft problem, the deliverable, the contract."""
    parts = []
    if ctx is not None:
        from generator.situations import render_outline_block

        outline, chapter = ctx
        heading = ("Novel outline:" if chapter is None
                   else "Novel outline for the chapter you are about to write:")
        parts.extend([heading, render_outline_block(outline, chapter), ""])
    parts.append(pick(rng, ST.FRAMES[stage][rec_type]))
    parts.append(pick(rng, item["frames"]))
    if rec_type == "transition":
        parts.append(item["context"])
        parts.append("You are in " + pick(rng, item["stages"]) + ".")
    elif rec_type == "reasoning":
        parts.append(item["question"])
    else:
        parts.append(item["slide"])
        parts.append("You are in " + pick(rng, item["stages"]) + ".")
    if rng.random() < 0.6:
        parts.append(pick(rng, ST.CONTEXT_LINES[stage]))
    parts.append(pick(rng, ST.TAILS[stage][rec_type]))
    if rng.random() < 0.5:
        parts.append(ST.deliverable_line(stage))
    parts.append(pick(rng, ST.CONTRACTS))
    return "\n".join(p for p in parts if p)


# ---------------------------------------------------------------------------
# Lenses, strategies, depth
# ---------------------------------------------------------------------------


def choose_lenses(rng, cat, rec_type, stage, lens_use, quota, lead=None,
                  max_lenses=3):
    """The record's craft lenses, balanced across the dataset.

    The lead lens comes from the stage's affinity, the chapter's craft pressure
    in outline mode, the category's preferences, or the record type, chosen so
    every lens in the registry leads its share of the dataset. `lens_use` counts
    lead assignments only.
    """
    permitted = set(STAGE_LENSES[stage])
    candidates = []
    ordering = ([lead] if lead else []) + list(ST.LENS_AFFINITY[stage]) \
        + list(CATEGORY_LENSES[cat["id"]]) + list(TYPE_LENSES[rec_type])
    for lens in ordering:
        if lens and lens not in candidates and lens in permitted:
            candidates.append(lens)
    if not candidates:
        # Defensive: a stage always reasons with a lens of its own, and an
        # outline-mode craft pressure is always honoured even when the stage's
        # own sets do not list it.
        candidates = ([lead] if lead else []) + list(STAGE_LENSES[stage])
    weight = {lens: 1.0 for lens in candidates}
    weight[candidates[0]] = 1.6 if not lead else 2.0
    scored = sorted(candidates, key=lambda lens: (lens_use[lens] / weight[lens],
                                                  candidates.index(lens)))
    if lens_use[scored[0]] < quota and rng.random() < 0.85:
        chosen = [scored[0]]
    else:
        chosen = [pick(rng, scored[:2])]
    rest = [lens for lens in candidates if lens != chosen[0]]
    if rest:
        chosen.append(min(rest, key=lambda lens: lens_use[lens]))
    if rest and rng.random() < 0.6:
        extra = [lens for lens in rest if lens not in chosen]
        if extra:
            chosen.append(min(extra, key=lambda lens: lens_use[lens]))
    if lead and lead not in chosen:
        if len(chosen) > 1:
            chosen[1] = lead
        else:
            chosen.append(lead)
    if max_lenses == 1:
        # A terse trace reasons through one dimension. In outline mode that has to
        # be the chapter's own craft pressure, so the lead lens wins.
        chosen = [lead] if lead else chosen[:1]
    lens_use.update(chosen[:1])
    return chosen[:1] + sorted(chosen[1:], key=LENS_ORDER.index)


def choose_strategies(rng, rec_type, depth, strategy_use):
    """How many reasoning strategies to include, and which."""
    if depth == "terse":
        # A terse trace settles one decision; the strategy layer is what makes
        # standard and deep traces longer, so it is not used here.
        return []
    count = 1 if depth != "deep" else rng.choice((1, 2))
    pool = [s for s in TYPE_STRATEGIES[rec_type]]
    # Prefer strategies that are under-used so far, with the verification check
    # appearing in roughly a quarter of records.
    pool.sort(key=lambda name: strategy_use[name])
    chosen = []
    if rng.random() < 0.28 and "verify" in pool:
        chosen.append("verify")
    for name in pool:
        if len(chosen) >= count:
            break
        if name not in chosen:
            chosen.append(name)
    strategy_use.update(chosen)
    return chosen


def depth_for(rng, strategy_count):
    """Paragraph-count decisions that follow from the depth tier."""
    depth = weighted_choice(rng, DEPTHS)
    return depth


DIFFICULTY_BY_DEPTH = {"terse": "foundational", "standard": "intermediate",
                       "deep": "advanced"}


def difficulty_for(depth):
    """Difficulty tier, tracked so a training run can sample across the range.

    Depth is what varies the demand: a terse trace settles one decision, a
    standard trace settles several, and a deep trace carries interacting
    decisions plus a strategy and a check.
    """
    return DIFFICULTY_BY_DEPTH[depth]


def lens_paragraphs(rng, lenses, stage):
    """Lens paragraphs at the height of the stage being reasoned about."""
    banks = {lens: lens_bank(stage, lens, LENSES[lens]) for lens in lenses}
    return [banks[lens][rng.randrange(len(banks[lens]))] for lens in lenses]


def strategy_paragraphs(rng, names):
    return [STRATEGIES[name]["paragraphs"][rng.randrange(len(STRATEGIES[name]["paragraphs"]))]
            for name in names]


def tag_rules(cat, lenses):
    """The registry rules this record encodes.

    Normally the rules routed to the record's authored category. Categories that
    carry no rules of their own fall back to the rules routed to the lead lens,
    which is what those records reason with.
    """
    rules = rules_for_category(cat["id"])
    if not rules:
        rules = [rid for rid, spec in RULES.items() if spec[2] == lenses[0]]
    return sorted(rules)


def outline_fields(outline, chapter):
    """Outline metadata, written only when the optional outline mode is on."""
    if outline is None:
        return {}
    fields = {"outline_id": outline["id"], "chapter": chapter["n"] if chapter else None}
    if chapter is not None:
        fields["craft_pressure"] = chapter["pressure"]
    return fields


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------


def build_transition(rng, cat, stage, ctx, used_text, used_combo, lens_use, quota,
                     strategy_use):
    problem = pick(rng, cat["problems"])
    move_keys = list(cat["moves"].keys())
    pad = 0
    for _ in range(900):
        outline, chapter = ctx if ctx is not None else (None, None)
        depth = weighted_choice(rng, DEPTHS)
        if pad >= 2:
            depth = "deep"
        elif pad == 1:
            depth = "standard"
        move_count = {"terse": 1, "standard": 2, "deep": 3}[depth] + pad
        keys = ordered_subset(rng, move_keys, min(move_count, len(move_keys)))
        move_paras = tuple((key, rng.randrange(len(cat["moves"][key]))) for key in keys)
        opener_i = rng.randrange(len(problem["openers"]))
        closer_i = rng.randrange(len(problem["closers"]))
        lead = PRESSURE_LENS[chapter["pressure"]] if chapter else None
        lenses = choose_lenses(rng, cat, "transition", stage, lens_use, quota, lead=lead,
                               max_lenses=1 if depth == "terse" else 3)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        strategies = choose_strategies(rng, "transition", depth, strategy_use)
        strategy_paras = tuple(rng.randrange(len(STRATEGIES[name]["paragraphs"]))
                               for name in strategies)
        combo = (
            problem["id"], problem["openers"][opener_i], move_paras, lens_paras,
            strategy_paras, closer_i, outline["id"] if outline else None,
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
        paragraphs.extend(strategy_paragraphs(rng, strategies))
        paragraphs.extend(lens_paragraphs(rng, lenses, stage))
        paragraphs.append(problem["closers"][closer_i])
        response = join_paragraphs(paragraphs) + "\n\n" + TRANSITION_LINE
        minimum = {"terse": 190, "standard": 245, "deep": 285}[depth]
        if len(response.split()) < minimum and pad < 3:
            pad += 1
            continue
        if response in used_text:
            continue
        instruction = build_instruction(rng, "transition", stage, cat, problem, ctx)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "transition", cat["id"], problem["id"], instruction, response,
            stage=stage, depth=depth,
            difficulty=difficulty_for(depth),
            lenses=list(lenses), strategies=list(strategies),
            rules=tag_rules(cat, lenses), **outline_fields(outline, chapter),
        )
    raise RuntimeError("Could not build a unique transition example for " + cat["id"])


def build_reasoning(rng, cat, stage, ctx, used_text, used_combo, lens_use, quota,
                    strategy_use):
    theme = pick(rng, cat["themes"])
    middles = theme["middles"]
    pad = 0
    for _ in range(900):
        outline, chapter = ctx if ctx is not None else (None, None)
        depth = weighted_choice(rng, DEPTHS)
        if pad >= 2:
            depth = "deep"
        elif pad == 1:
            depth = "standard"
        keep_count = min(len(middles), {"terse": 1, "standard": 2, "deep": 3}[depth] + pad)
        keep = sorted(rng.sample(range(len(middles)), keep_count))
        opener_i = rng.randrange(len(theme["openers"]))
        closer_i = rng.randrange(len(theme["closers"]))
        principle_i = rng.randrange(len(cat["principles"]))
        lenses = choose_lenses(rng, cat, "reasoning", stage, lens_use, quota,
                               max_lenses=1 if depth == "terse" else 3)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        strategies = choose_strategies(rng, "reasoning", depth, strategy_use)
        strategy_paras = tuple(rng.randrange(len(STRATEGIES[name]["paragraphs"]))
                               for name in strategies)
        combo = (
            theme["id"], opener_i, tuple(keep), principle_i, closer_i, lens_paras,
            strategy_paras, outline["id"] if outline else None,
        )
        if combo in used_combo:
            continue
        paragraphs = []
        if ctx is not None:
            from generator.situations import situation_paragraph

            paragraphs.append(situation_paragraph(outline, chapter, rng, "reasoning"))
        paragraphs.append(pick(rng, ST.OPENERS[stage]["reasoning"]))
        paragraphs.append(theme["openers"][opener_i])
        paragraphs.extend(middles[i] for i in keep)
        paragraphs.append(cat["principles"][principle_i])
        paragraphs.extend(strategy_paragraphs(rng, strategies))
        paragraphs.extend(lens_paragraphs(rng, lenses, stage))
        paragraphs.append(theme["closers"][closer_i])
        response = join_paragraphs(paragraphs)
        minimum = {"terse": 190, "standard": 245, "deep": 285}[depth]
        if len(response.split()) < minimum and pad < 3:
            pad += 1
            continue
        if response in used_text:
            continue
        instruction = build_instruction(rng, "reasoning", stage, cat, theme, ctx)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "reasoning", cat["id"], theme["id"], instruction, response,
            stage=stage, depth=depth,
            difficulty=difficulty_for(depth),
            lenses=list(lenses), strategies=list(strategies),
            rules=tag_rules(cat, lenses), **outline_fields(outline, None),
        )
    raise RuntimeError("Could not build a unique reasoning example for " + cat["id"])


def build_negative(rng, cat, stage, ctx, used_text, used_combo, lens_use, quota,
                   strategy_use):
    trap = pick(rng, cat["traps"])
    pad = 0
    for _ in range(900):
        outline, chapter = ctx if ctx is not None else (None, None)
        depth = weighted_choice(rng, DEPTHS)
        if pad >= 2:
            depth = "deep"
        elif pad == 1:
            depth = "standard"
        opener_i = rng.randrange(len(trap["openers"]))
        closer_i = rng.randrange(len(trap["closers"]))
        discipline_i = rng.randrange(len(cat["discipline"]))
        lead = PRESSURE_LENS[chapter["pressure"]] if chapter else None
        lenses = choose_lenses(rng, cat, "negative", stage, lens_use, quota, lead=lead,
                               max_lenses=1 if depth == "terse" else 3)
        if pad:
            extra = [lens for lens in list(CATEGORY_LENSES[cat["id"]]) + list(ST.LENS_AFFINITY[stage])
                     if lens not in lenses]
            lenses = lenses + extra[:pad]
            lenses = lenses[:3]
            lenses = lenses[:1] + sorted(lenses[1:], key=LENS_ORDER.index)
        lens_paras = tuple(rng.randrange(len(LENSES[lens])) for lens in lenses)
        strategies = choose_strategies(rng, "negative", depth, strategy_use)
        strategy_paras = tuple(rng.randrange(len(STRATEGIES[name]["paragraphs"]))
                               for name in strategies)
        combo = (
            trap["id"], opener_i, discipline_i, closer_i, lens_paras, strategy_paras,
            outline["id"] if outline else None, chapter["n"] if chapter else None,
        )
        if combo in used_combo:
            continue
        paragraphs = []
        if ctx is not None:
            from generator.situations import situation_paragraph

            paragraphs.append(situation_paragraph(outline, chapter, rng, "negative"))
        paragraphs.append(pick(rng, ST.OPENERS[stage]["negative"]))
        paragraphs.append(trap["openers"][opener_i])
        paragraphs.append(trap["damage"])
        paragraphs.append(cat["discipline"][discipline_i])
        paragraphs.append(trap["reason_past"])
        paragraphs.extend(strategy_paragraphs(rng, strategies))
        paragraphs.extend(lens_paragraphs(rng, lenses, stage))
        paragraphs.append(trap["closers"][closer_i])
        response = join_paragraphs(paragraphs)
        minimum = {"terse": 190, "standard": 245, "deep": 285}[depth]
        if len(response.split()) < minimum and pad < 3:
            pad += 1
            continue
        if response in used_text:
            continue
        instruction = build_instruction(rng, "negative", stage, cat, trap, ctx)
        if instruction in used_text:
            continue
        used_combo.add(combo)
        used_text.add(response)
        used_text.add(instruction)
        return make_record(
            None, "negative", cat["id"], trap["id"], instruction, response,
            stage=stage, depth=depth,
            difficulty=difficulty_for(depth),
            lenses=list(lenses), strategies=list(strategies),
            rules=tag_rules(cat, lenses), **outline_fields(outline, chapter),
        )
    raise RuntimeError("Could not build a unique negative example for " + cat["id"])


BUILDERS = {
    "transition": build_transition,
    "reasoning": build_reasoning,
    "negative": build_negative,
}


# ---------------------------------------------------------------------------
# Distribution
# ---------------------------------------------------------------------------


def distribute(count, items, rng):
    base = count // len(items)
    extra = count - base * len(items)
    order = list(items)
    rng.shuffle(order)
    pairs = [(item, base + (1 if i < extra else 0)) for i, item in enumerate(order)]
    return pairs


def stage_counts(rec_type, total):
    """Split a type's records across stages."""
    counts = []
    assigned = 0
    mix = STAGE_MIX[rec_type]
    for i, (stage, share) in enumerate(mix):
        n = total - assigned if i == len(mix) - 1 else int(round(total * share))
        assigned += n
        counts.append((stage, n))
    return counts


def stage_category_count(stage, total, rng):
    """How many records each category contributes inside one stage.

    Each stage reasons with its own libraries: the stage-native ones carry the
    majority of its records, and the rest come from the categories that also
    apply at that stage (for outlining, the structural libraries; for revision,
    the repair, scene and continuity libraries).
    """
    counts = Counter()
    allowed = list(ST.ALLOWED_CATEGORIES[stage])
    native = [c for c in ST.NATIVE_CATEGORIES[stage] if c in allowed]
    general = [CATEGORY_BY_ID[c] for c in allowed if c not in native]
    share = ST.NATIVE_SHARE[stage]
    if native and (not general or share >= 1.0):
        for cat, n in distribute(total, [CATEGORY_BY_ID[c] for c in native], rng):
            counts[cat["id"]] += n
        return counts
    if native:
        native_total = int(round(total * share))
        for cat, n in distribute(native_total, [CATEGORY_BY_ID[c] for c in native], rng):
            counts[cat["id"]] += n
        general_total = total - native_total
    else:
        general_total = total
    if general and general_total:
        for cat, n in distribute(general_total, general, rng):
            counts[cat["id"]] += n
    return counts


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
    strategy_use = Counter()
    quota = max(1, int(size / len(LENS_ORDER)))
    records = {t: [] for t in counts}
    counters = {t: 0 for t in counts}

    for rec_type, total in counts.items():
        for stage, stage_total in stage_counts(rec_type, total):
            plan = stage_category_count(stage, stage_total, rng)
            for cat_id, n in distribute_stage_plan(plan, stage_total, rng):
                cat = CATEGORY_BY_ID[cat_id]
                for _ in range(n):
                    ctx = pick_context(rng, cat, pools)
                    rec = BUILDERS[rec_type](rng, cat, stage, ctx, used_text,
                                             used_combo[rec_type], lens_use, quota,
                                             strategy_use)
                    counters[rec_type] += 1
                    rec["id"] = "%s-%s-%04d" % (TYPE_PREFIX[rec_type], cat_id,
                                                counters[rec_type])
                    records[rec_type].append(rec)

    return records, counts


def distribute_stage_plan(plan, total, rng):
    """Flatten a per-category plan into (category, count) pairs, summing to total."""
    items = [(cat_id, n) for cat_id, n in plan.items() if n > 0]
    items.sort(key=lambda pair: (-pair[1], pair[0]))
    diff = total - sum(n for _, n in items)
    i = 0
    while diff != 0 and items:
        cat_id, n = items[i % len(items)]
        if diff > 0:
            items[i % len(items)] = (cat_id, n + 1)
            diff -= 1
        elif n > 1:
            items[i % len(items)] = (cat_id, n - 1)
            diff += 1
        i += 1
    rng.shuffle(items)
    return items


def write_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=7200)
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
    strategy_counts = Counter()
    for rec in all_records:
        rule_counts.update(rec["rules"])
        lens_counts.update(rec["lenses"])
        strategy_counts.update(rec["strategies"])

    manifest = {
        "seed": args.seed,
        "target_size": args.size,
        "counts": counts,
        "total": sum(counts.values()),
        "conditioning": "outline bank" if args.with_outlines else "none (reasoning only)",
        "per_stage": {
            stage: {
                rec_type: sum(1 for r in records[rec_type] if r["stage"] == stage)
                for rec_type in counts
            }
            for stage in ST.STAGES
        },
        "per_depth": dict(Counter(r["depth"] for r in all_records).most_common()),
        "per_difficulty": dict(Counter(r["difficulty"] for r in all_records).most_common()),
        "per_category": {
            cat["id"]: {
                rec_type: sum(1 for r in records[rec_type] if r["category"] == cat["id"])
                for rec_type in counts
            }
            for cat in CATEGORIES
        },
        "per_strategy": {name: strategy_counts.get(name, 0) for name in STRATEGIES},
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
    for stage in ST.STAGES:
        total = sum(manifest["per_stage"][stage].values())
        print("  %-11s %5d" % ("stage:" + stage, total))
    print("  depths:     %s" % manifest["per_depth"])
    print("  difficulty: %s" % manifest["per_difficulty"])
    missing = [str(k) for k in sorted(RULES) if rule_counts.get(k, 0) == 0]
    if missing:
        print("  rules with no coverage: %s" % ", ".join(missing))
    unused = [lens for lens in LENS_ORDER if lens_counts.get(lens, 0) == 0]
    if unused:
        print("  lenses with no coverage: %s" % ", ".join(unused))


if __name__ == "__main__":
    main()
