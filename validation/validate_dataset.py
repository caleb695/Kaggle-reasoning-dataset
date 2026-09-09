"""Validate the generated dataset against its hard constraints.

Checks:
- Type ratios are 50/25/25 within tolerance.
- Transition responses end with exactly one handoff marker, as the final line.
- Reasoning and negative responses contain no marker.
- No double quotes and no prose-exemplar phrases anywhere (responses and instructions).
- All instructions and responses are globally unique.
- Every category is represented in every type; response lengths are sane.

Usage:
    python -m validation.validate_dataset data/dataset.jsonl
"""

import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generator.categories import CATEGORIES

EXPECTED_CATEGORIES = {c["id"] for c in CATEGORIES}

MARKER = "Given the above, the scene begins."

FORBIDDEN_SUBSTRINGS = [
    '"', "\u201c", "\u201d", "\u2018", "\u2019",
    "for example", "for instance", "such as", "e.g.", "i.e.",
    "might read", "would read", "could read", "as follows",
    "sample passage", "illustrative", "written out", "example passage",
]


def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)


def main(path):
    records = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    if not (2000 <= len(records) <= 3000):
        fail("dataset size %d outside target range 2000-3000" % len(records))

    type_counts = Counter(r["type"] for r in records)
    n = len(records)
    for rec_type, share in (("transition", 0.50), ("reasoning", 0.25), ("negative", 0.25)):
        got = type_counts.get(rec_type, 0) / n
        if abs(got - share) > 0.02:
            fail("ratio for %s is %.3f, expected %.2f +/- 0.02" % (rec_type, got, share))

    instructions = [r["instruction"] for r in records]
    responses = [r["response"] for r in records]
    if len(set(instructions)) != len(instructions):
        fail("duplicate instructions found")
    if len(set(responses)) != len(responses):
        fail("duplicate responses found")

    per_type_cat = defaultdict(set)
    for r in records:
        per_type_cat[r["type"]].add(r["category"])

    word_counts = []
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
        if r["type"] == "transition":
            if not resp.endswith(MARKER):
                fail("%s transition response does not end with the marker" % r["id"])
            if resp.count(MARKER) != 1:
                fail("%s transition response contains the marker more than once" % r["id"])
            body = resp[: -len(MARKER)].rstrip()
            if not body or len(body.split()) < 120:
                fail("%s transition response has too little reasoning before the marker" % r["id"])
        else:
            if MARKER in resp:
                fail("%s %s response contains the marker" % (r["id"], r["type"]))
        if words < 120:
            fail("%s response too short (%d words)" % (r["id"], words))
        if words > 900:
            fail("%s response too long (%d words)" % (r["id"], words))

    for rec_type in ("transition", "reasoning", "negative"):
        if len(per_type_cat[rec_type]) < 9:
            fail("type %s does not cover all nine categories" % rec_type)

    word_counts.sort()
    print("OK: %d records" % n)
    print("  types: %s" % dict(type_counts))
    print("  response words: min=%d median=%d max=%d"
          % (word_counts[0], word_counts[len(word_counts) // 2], word_counts[-1]))
    cats = Counter(r["category"] for r in records)
    print("  categories: %s" % dict(cats))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/dataset.jsonl")
