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
from collections import Counter

# At inference the caller supplies the novel outline being drafted; the outline
# is not part of these records, so training stays pure reasoning supervision.
SYSTEM_PROMPT = (
    "You are a writing planner and reasoner working at any stage of a novel: brainstorming "
    "an idea, outlining the story, writing a chapter of it from an outline, or revising it. "
    "You reason before you write. At every stage you first read the task and reconstruct the "
    "story: what you have been asked to produce, what the earlier chapters have established, "
    "who the characters are and what they want, and what the story needs next. Then you reason "
    "about craft: premise and promise, the story's plot and conflict, structure and thread "
    "scheduling, point of view, scene construction, pacing, tension, emotion, dialogue, imagery, "
    "continuity, and how each chapter serves the plan of the novel. When a genre is involved you "
    "work inside that genre's promise and conventions. Your reasoning is structural and "
    "conceptual only. You never write prose, never quote lines, and never give illustrative "
    "passages. When you are about to write a chapter, you end your reasoning with the single "
    "line: Given the above, the scene begins."
)

STAGE_BRIEF = {
    "ideation": "Stage: brainstorming. Deliverable: an idea that makes a story, with someone to follow, something they want badly, and trouble that will not let them have it.",
    "outline": "Stage: outlining. Deliverable: a story that works from the first page to the last, told as chapter summaries, character notes, plot and conflict.",
    "drafting": "Stage: writing. Deliverable: how the chapter gets written, inside the outline you were given.",
    "revision": "Stage: revision. Deliverable: what to change, what to keep, and the order to work in.",
}

MARKER = "Given the above, the scene begins."


def render(record, drop_marker=False):
    response = record["response"]
    if drop_marker and record["type"] == "transition":
        response = response[: -len(MARKER)].rstrip()
    context = [
        "Type: %s" % record["type"],
        STAGE_BRIEF.get(record.get("stage", ""), ""),
        "Category: %s" % record["category"],
        "Craft dimension: %s" % record["subcategory"],
    ]
    context = [line for line in context if line]
    if record.get("outline_id"):
        if record.get("chapter") is not None:
            context.append("Outline: %s, chapter %s" % (record["outline_id"], record["chapter"]))
        else:
            context.append("Scope: the whole novel %s" % record["outline_id"])
    user = "\n".join(context) + "\n\n" + record["instruction"]
    return {
        "id": record["id"],
        "type": record["type"],
        "stage": record.get("stage"),
        "category": record["category"],
        "depth": record.get("depth"),
        "difficulty": record.get("difficulty"),
        "strategies": record.get("strategies", []),
        "genre": record.get("genre"),
        "task_reading": record.get("task_reading", []),
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
    all_rows = []
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
            all_rows.append(rendered)
            handle("train.jsonl").write(json.dumps(rendered, ensure_ascii=False) + "\n")
            handle("sft_%s.jsonl" % record["type"]).write(
                json.dumps(rendered, ensure_ascii=False) + "\n")

    for fh in handles.values():
        fh.close()

    stages = Counter(r["stage"] for r in all_rows)
    print("wrote %s" % args.out)
    print("  stages: %s" % dict(stages))
    for rec_type, count in counts.items():
        print("  %-11s %5d" % (rec_type, count))
    print("  total       %5d" % sum(counts.values()))


if __name__ == "__main__":
    main()
