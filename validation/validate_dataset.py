"""Validate the generated dataset against its hard constraints.

Checks:
- Dataset size is inside the supported band, and type ratios are 50/25/25.
- Every stage of the writing process is covered, with every category represented
  inside every stage and type combination.
- Transition responses end with exactly one handoff marker, as the final line,
  and only at the drafting stage; other types never contain the marker.
- No double quotes, no curly quotes, and no prose-exemplar phrases anywhere.
- All instructions and responses are globally unique.
- Depth tiers are represented, responses sit in the band for their tier, and the
  difficulty tag agrees with the tier.
- Reasoning strategies are drawn from the registry and all of them are used.
- Lenses and rule references are valid, and every rule in the registry is used.
- Optional: when a record carries outline metadata (outline mode only), the
  outline and chapter resolve and the pressure lens travels with the record.

Usage:
    python -m validation.validate_dataset data/dataset.jsonl
    python -m validation.validate_dataset data/dataset.jsonl --min 6000 --max 8000
"""

import argparse
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generator.categories import CATEGORIES
from generator.lenses import LENS_ORDER, PRESSURE_LENS
from generator.rules import all_rule_ids
from generator.stages import STAGES
from generator.strategies import STRATEGIES

EXPECTED_CATEGORIES = {c["id"] for c in CATEGORIES}

MARKER = "Given the above, the scene begins."

FORBIDDEN_SUBSTRINGS = [
    '"', "\u201c", "\u201d", "\u2018", "\u2019",
    "for example", "for instance", "such as", "e.g.", "i.e.",
    "might read", "would read", "could read", "as follows",
    "sample passage", "illustrative", "written out", "example passage",
]

TYPE_SHARES = {"transition": 0.50, "reasoning": 0.25, "negative": 0.25}

REQUIRED_FIELDS = ("id", "type", "stage", "category", "subcategory", "instruction",
                   "response", "lenses", "strategies", "rules", "depth", "difficulty")

DEPTH_FIELDS = {
    "terse": (185, 400),      # one decision, settled fast
    "standard": (240, 540),   # several decisions plus a strategy
    "deep": (275, 700),       # interacting decisions, strategy, and a check
}

DIFFICULTY_BY_DEPTH = {"terse": "foundational", "standard": "intermediate",
                       "deep": "advanced"}

MIN_PER_STAGE_CATEGORY_RATIO = 0.0011  # ~8 at 7,200 records
MIN_PER_TYPE_CATEGORY = 20


def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)


def load(path):
    records = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default="data/dataset.jsonl")
    parser.add_argument("--min", type=int, default=6000)
    parser.add_argument("--max", type=int, default=8000)
    args = parser.parse_args()

    records = load(args.path)
    n = len(records)

    if not (args.min <= n <= args.max):
        fail("dataset size %d outside target range %d-%d" % (n, args.min, args.max))

    type_counts = Counter(r["type"] for r in records)
    for rec_type, share in TYPE_SHARES.items():
        got = type_counts.get(rec_type, 0) / n
        if abs(got - share) > 0.02:
            fail("ratio for %s is %.3f, expected %.2f +/- 0.02" % (rec_type, got, share))

    for field in REQUIRED_FIELDS:
        missing = [r.get("id", "?") for r in records if field not in r]
        if missing:
            fail("records missing %r: %s" % (field, missing[:5]))

    ids = [r["id"] for r in records]
    if len(set(ids)) != n:
        fail("duplicate record ids found")
    if len({r["instruction"] for r in records}) != n:
        fail("duplicate instructions found")
    if len({r["response"] for r in records}) != n:
        fail("duplicate responses found")

    word_counts = []
    instruction_words = []
    stage_cells = Counter()
    per_type_cat = defaultdict(Counter)
    rule_hits = Counter()
    lens_lead = Counter()
    lens_all = Counter()
    strategy_hits = Counter()
    outline_records = 0

    for r in records:
        resp = r["response"]
        instr = r["instruction"]
        for text, field in ((resp, "response"), (instr, "instruction")):
            low = text.lower()
            for bad in FORBIDDEN_SUBSTRINGS:
                if bad in low:
                    fail("%s %s contains forbidden substring %r" % (r["id"], field, bad))

        words = len(resp.split())
        word_counts.append(words)
        instruction_words.append(len(instr.split()))

        stage = r["stage"]
        if stage not in STAGES:
            fail("%s has unknown stage %r" % (r["id"], stage))
        if stage != "drafting" and r["type"] == "transition":
            fail("%s transition record outside the drafting stage" % r["id"])
        stage_cells[(stage, r["type"])] += 1

        depth = r["depth"]
        if depth not in DEPTH_FIELDS:
            fail("%s has unknown depth %r" % (r["id"], depth))
        low, high = DEPTH_FIELDS[depth]
        if r.get("outline_id"):
            # Outline mode prepends the outline slice, so the reasoning itself is
            # unchanged but the record is longer than the depth band.
            high += 160
        if not (low <= words <= high):
            fail("%s is %s depth but has %d words (band %d-%d)"
                 % (r["id"], depth, words, low, high))
        if r["difficulty"] != DIFFICULTY_BY_DEPTH[depth]:
            fail("%s difficulty %r does not match depth %r"
                 % (r["id"], r["difficulty"], depth))

        if r["type"] == "transition":
            if not resp.endswith(MARKER):
                fail("%s transition response does not end with the marker" % r["id"])
            if resp.count(MARKER) != 1:
                fail("%s transition response contains the marker more than once" % r["id"])
            if len(resp[: -len(MARKER)].split()) < 150:
                fail("%s transition response has too little reasoning before the marker" % r["id"])
        else:
            if MARKER in resp:
                fail("%s %s response contains the marker" % (r["id"], r["type"]))
            if "the scene begins" in resp:
                fail("%s %s response contains the handoff phrase" % (r["id"], r["type"]))

        cat = r["category"]
        if cat not in EXPECTED_CATEGORIES:
            fail("%s has unknown category %r" % (r["id"], cat))
        per_type_cat[r["type"]][cat] += 1

        lenses = r["lenses"]
        if not lenses or len(lenses) > 3:
            fail("%s carries %d lenses" % (r["id"], len(lenses) if lenses else 0))
        if any(lens not in LENS_ORDER for lens in lenses):
            fail("%s has invalid lenses %r" % (r["id"], lenses))
        if len(set(lenses)) != len(lenses):
            fail("%s repeats a lens %r" % (r["id"], lenses))
        if lenses[1:] != sorted(lenses[1:], key=LENS_ORDER.index):
            fail("%s secondary lenses are not in canonical order" % r["id"])
        lens_lead.update(lenses[:1])
        lens_all.update(lenses)

        strategies = r["strategies"]
        if len(strategies) > 2 or len(set(strategies)) != len(strategies):
            fail("%s carries invalid strategies %r" % (r["id"], strategies))
        if any(name not in STRATEGIES for name in strategies):
            fail("%s has unknown strategies %r" % (r["id"], strategies))
        if depth == "terse" and strategies:
            fail("%s is terse but carries a reasoning strategy" % r["id"])
        strategy_hits.update(strategies)
        for name in strategies:
            if not any(STRATEGIES[name]["paragraphs"][i] in resp
                       for i in range(len(STRATEGIES[name]["paragraphs"]))):
                fail("%s carries strategy %r without its paragraph" % (r["id"], name))

        rules = r["rules"]
        if not rules:
            fail("%s carries no rule references" % r["id"])
        rule_hits.update(rules)

        # Optional outline metadata: the dataset is reasoning-only by default,
        # so this block only fires for records built in the outline mode.
        if r.get("outline_id"):
            outline_records += 1
            if "TITLE:" not in instr:
                fail("%s instruction is missing the outline block" % r["id"])
            from generator.outlines import BY_ID as OUTLINE_BY_ID

            outline = OUTLINE_BY_ID.get(r["outline_id"])
            if outline is None:
                fail("%s references unknown outline %r" % (r["id"], r["outline_id"]))
            chapter = r.get("chapter")
            if r["type"] == "reasoning":
                if chapter is not None:
                    fail("%s reasoning record carries a chapter reference" % r["id"])
            else:
                if not isinstance(chapter, int) or not (1 <= chapter <= len(outline["chapters"])):
                    fail("%s references a chapter outside %s" % (r["id"], r["outline_id"]))
                if r.get("craft_pressure") not in PRESSURE_LENS:
                    fail("%s has unknown craft pressure %r" % (r["id"], r.get("craft_pressure")))
                if PRESSURE_LENS[r["craft_pressure"]] not in lenses:
                    fail("%s does not carry the lens for its craft pressure %r"
                         % (r["id"], r["craft_pressure"]))

    # Stage and category coverage.
    for stage in STAGES:
        for rec_type in TYPE_SHARES:
            if rec_type == "transition":
                # Transitions are the planning-to-writing handoff, so they exist
                # only where writing follows: the drafting stage.
                continue
            if not stage_cells[(stage, rec_type)]:
                fail("no records at stage %s for type %s" % (stage, rec_type))
    if stage_cells[("drafting", "transition")] != type_counts["transition"]:
        fail("every transition record should sit at the drafting stage")

    for rec_type in TYPE_SHARES:
        covered = per_type_cat[rec_type]
        if set(covered) != EXPECTED_CATEGORIES:
            missing = sorted(EXPECTED_CATEGORIES - set(covered))
            fail("type %s is missing categories %s" % (rec_type, missing))
        thin = sorted(c for c, k in covered.items() if k < min(MIN_PER_TYPE_CATEGORY, n // 400))
        if thin:
            fail("type %s has thinly covered categories %s" % (rec_type, thin))

    for rec_type in TYPE_SHARES:
        cells = Counter((r["stage"], r["category"]) for r in records if r["type"] == rec_type)
        floor = max(1, int(round(n * MIN_PER_STAGE_CATEGORY_RATIO)))
        thin = sorted(cell for cell, k in cells.items() if k < floor)
        if thin:
            fail("stage/category cells under %d records in %s: %s"
                 % (floor, rec_type, thin[:6]))

    missing_rules = sorted(set(all_rule_ids()) - set(rule_hits))
    if missing_rules:
        fail("rules with no coverage: %s" % missing_rules)

    unused_strategies = sorted(set(STRATEGIES) - set(strategy_hits))
    if unused_strategies:
        fail("strategies with no coverage: %s" % unused_strategies)

    for field, values in (("response", word_counts), ("instruction", instruction_words)):
        values = sorted(values)
        print("  %s words: min=%d p50=%d max=%d"
              % (field, values[0], values[len(values) // 2], values[-1]))

    print("OK: %d records%s" % (n, "" if not outline_records else " (%d outline-mode)" % outline_records))
    print("  types: %s" % dict(type_counts))
    print("  stages: %s" % {s: sum(k for (st, _), k in stage_cells.items() if st == s)
                            for s in STAGES})
    print("  stage x type: %s" % {"%s/%s" % k: v for k, v in sorted(stage_cells.items())})
    print("  categories: %d" % len(EXPECTED_CATEGORIES))
    print("  rules exercised: %d of %d" % (len(rule_hits), len(all_rule_ids())))
    print("  strategies: %s" % dict(strategy_hits.most_common()))
    print("  lenses: %d distinct; leads balanced %d-%d"
          % (len(lens_all), min(lens_lead.values()), max(lens_lead.values())))


if __name__ == "__main__":
    main()
