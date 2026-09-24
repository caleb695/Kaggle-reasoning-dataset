"""Convert the dataset into training-ready formats.

The dataset is stored as flat instruction/response JSONL because that is the
most portable schema. Training pipelines usually want a chat format instead, so
this script renders each record as a system/user/assistant conversation.

Usage (from the repository root):
    python -m training.convert_for_training --out training/formatted
    python -m training.convert_for_training --types transition --drop-marker

Outputs:
    <out>/train.jsonl                records rendered as chat messages
    <out>/sft_transition.jsonl       planning-to-writing traces only
    <out>/sft_reasoning.jsonl        arc-level planning traces only
    <out>/sft_negative.jsonl         forward avoidance traces only
"""

import argparse
import json
import os

# At inference the caller supplies the novel outline being drafted; the outline
# is not part of these records, so training stays pure reasoning supervision.
SYSTEM_PROMPT = (
    "You are a structural writing planner. You reason about craft before drafting: "
    "point of view, scene construction, pacing, tension, emotion, dialogue, imagery, "
    "continuity, and how each chapter serves the plan of the novel. Your reasoning is "
    "structural and conceptual only. You never write prose, never quote lines, and "
    "never give illustrative passages. When you are writing a chapter, you end your "
    "reasoning with the single line: Given the above, the scene begins."
)

MARKER = "Given the above, the scene begins."


def render(record, drop_marker=False):
    response = record["response"]
    if drop_marker and record["type"] == "transition":
        response = response[: -len(MARKER)].rstrip()
    context = [
        "Type: %s" % record["type"],
        "Category: %s" % record["category"],
        "Craft dimension: %s" % record["subcategory"],
    ]
    if record.get("outline_id"):
        if record.get("chapter") is not None:
            context.append("Outline: %s, chapter %s" % (record["outline_id"], record["chapter"]))
        else:
            context.append("Scope: the whole novel %s" % record["outline_id"])
    user = "\n".join(context) + "\n\n" + record["instruction"]
    return {
        "id": record["id"],
        "type": record["type"],
        "category": record["category"],
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
            {"role": "assistant", "content": response},
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default="data/dataset.jsonl")
    parser.add_argument("--out", default="training/formatted")
    parser.add_argument("--types", nargs="*", default=None,
                        help="restrict to these record types")
    parser.add_argument("--drop-marker", action="store_true",
                        help="strip the handoff line from transition responses")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    wanted = set(args.types) if args.types else None
    counts = {"transition": 0, "reasoning": 0, "negative": 0}
    handles = {}

    def handle(name):
        if name not in handles:
            handles[name] = open(os.path.join(args.out, name), "w", encoding="utf-8")
        return handles[name]

    with open(args.path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if wanted and record["type"] not in wanted:
                continue
            rendered = render(record, drop_marker=args.drop_marker)
            counts[record["type"]] += 1
            handle("train.jsonl").write(json.dumps(rendered, ensure_ascii=False) + "\n")
            handle("sft_%s.jsonl" % record["type"]).write(
                json.dumps(rendered, ensure_ascii=False) + "\n")

    for fh in handles.values():
        fh.close()

    print("wrote %s" % args.out)
    for rec_type, count in counts.items():
        print("  %-11s %5d" % (rec_type, count))
    print("  total       %5d" % sum(counts.values()))


if __name__ == "__main__":
    main()
