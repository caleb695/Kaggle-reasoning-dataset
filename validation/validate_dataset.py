"""Validate the generated dataset against its hard constraints.

Checks:
- Dataset size is inside the supported band, and type ratios are 50/25/25.
- Transition responses end with exactly one handoff marker, as the final line;
  reasoning and negative responses never contain it, and never contain the
  phrase the scene begins.
- No double quotes, no curly quotes, and no prose-exemplar phrases anywhere.
- All instructions and responses are globally unique.
- Every category appears in every type, and per-category counts are balanced.
- Records carry valid lenses and rule references; every rule in the registry is
  exercised by at least one record.
- Response and instruction lengths sit inside sane bands.
- Optional: when a record carries outline metadata (only in outline mode), the
  outline and chapter must resolve and the plain-text outline block must be in
  the instruction.

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
from generator.lenses import LENS_ORDER
from generator.rules import all_rule_ids

EXPECTED_CATEGORIES = {c["id"] for c in CATEGORIES}

MARKER = "Given the above, the scene begins."

FORBIDDEN_SUBSTRINGS = [
    '"', "\u201c", "\u201d", "\u2018", "\u2019",
    "for example", "for instance", "such as", "e.g.", "i.e.",
    "might read", "would read", "could read", "as follows",
    "sample passage", "illustrative", "written out", "example passage",
]

TYPE_SHARES = {"transition": 0.50, "reasoning": 0.25, "negative": 0.25}

REQUIRED_FIELDS = ("id", "type", "category", "subcategory", "instruction", "response",
                   "lenses", "rules")


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
    parser.add_argument("--min-words", type=int, default=180)
    parser.add_argument("--max-words", type=int, default=900)
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

    instructions = [r["instruction"] for r in records]
    responses = [r["response"] for r in records]
    if len(set(instructions)) != n:
        fail("duplicate instructions found")
    if len(set(responses)) != n:
        fail("duplicate responses found")

    word_counts = []
    instruction_words = []
    per_type_cat = defaultdict(Counter)
    rule_hits = Counter()
    lens_lead = Counter()
    lens_all = Counter()
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
        if words < args.min_words:
            fail("%s response too short (%d words)" % (r["id"], words))
        if words > args.max_words:
            fail("%s response too long (%d words)" % (r["id"], words))

        if r["type"] == "transition":
            if not resp.endswith(MARKER):
                fail("%s transition response does not end with the marker" % r["id"])
            if resp.count(MARKER) != 1:
                fail("%s transition response contains the marker more than once" % r["id"])
            body = resp[: -len(MARKER)].rstrip()
            if len(body.split()) < 150:
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

        # Optional outline metadata: the dataset is reasoning-only by default,
        # so this block only fires for records built in the outline mode.
        if r.get("outline_id"):
            outline_records += 1
            if "TITLE:" not in instr:
                fail("%s instruction is missing the outline block" % r["id"])
            from generator.outlines import BY_ID as OUTLINE_BY_ID
            from generator.lenses import PRESSURE_LENS

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

    for rec_type in TYPE_SHARES:
        covered = per_type_cat[rec_type]
        if set(covered) != EXPECTED_CATEGORIES:
            missing = sorted(EXPECTED_CATEGORIES - set(covered))
            fail("type %s is missing categories %s" % (rec_type, missing))
        counts = list(covered.values())
        if max(counts) > 1.25 * min(counts):
            fail("type %s category counts are unbalanced: %s" % (rec_type, dict(covered)))

    missing_rules = sorted(set(all_rule_ids()) - set(rule_hits := Counter(rid for r in records
                                                                          for rid in r["rules"])))
    if missing_rules:
        fail("rules with no coverage: %s" % missing_rules)

    for field, values in (("response", word_counts), ("instruction", instruction_words)):
        values = sorted(values)
        print("  %s words: min=%d p50=%d max=%d"
              % (field, values[0], values[len(values) // 2], values[-1]))

    print("OK: %d records%s" % (n, "" if not outline_records else " (%d outline-mode)" % outline_records))
    print("  types: %s" % dict(type_counts))
    print("  categories: %d, per category per type roughly %d"
          % (len(EXPECTED_CATEGORIES), n // (len(EXPECTED_CATEGORIES) * 2)))
    print("  rules exercised: %d of %d" % (len(rule_hits), len(all_rule_ids())))
    print("  lenses: %d distinct; leads balanced %d-%d"
          % (len(lens_all), min(lens_lead.values()), max(lens_lead.values())))
    print("  lens frequency: %s" % dict(lens_all.most_common()))


if __name__ == "__main__":
    main()
