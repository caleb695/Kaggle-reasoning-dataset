"""Shared infrastructure for the writer-craft reasoning dataset generator.

Design constraints enforced across the whole dataset:
- Responses are purely structural and conceptual. No illustrative prose anywhere.
- Transition examples end with exactly one voice-neutral handoff marker.
- Negative examples are forward-oriented: trap -> damage -> replacement reasoning.
"""

TRANSITION_LINE = "Given the above, the scene begins."

TYPES = ("transition", "reasoning", "negative")

TYPE_RATIOS = {"transition": 0.50, "reasoning": 0.25, "negative": 0.25}

# Openers for instructions (the writer-model is addressed in second person).
INTROS = [
    "You are writing a novel.",
    "You are at work on a novel.",
    "You are drafting a novel.",
    "You are deep inside a novel you are writing.",
]

PLANNING_INTROS = [
    "You are planning a novel.",
    "You are architecting a novel before drafting begins.",
    "You are mapping out a novel you are about to write.",
    "You are standing at the start of a novel, deciding how it will be built.",
]

# Instruction tails for transition examples: they ask for complete reasoning,
# then a direct handoff into writing. They never quote the marker itself.
TRANSITION_TAILS = [
    "Work through the structural problem completely, then move straight into writing the scene.",
    "Reason your way through it in full, then begin the scene.",
    "Settle every decision the problem turns on, then carry them onto the page as you start the scene.",
    "Think the problem through to the end of the reasoning, then let the scene take over.",
    "Work out exactly how the scene must be built, then start writing it.",
    "Do the structural thinking first; when nothing is left to decide, begin the scene.",
    "Resolve the craft question in your head, then write into the scene without further commentary.",
    "Plan until the path is firm, then cross from planning into the scene itself.",
    "Think it all the way through, then make the move from reasoning to writing in a single step.",
    "Handle the structural decisions here; once the reasoning is complete, the scene begins.",
    "Work through the problem until you know precisely what the scene must do, then commit to the page.",
    "Finish the thinking first. When the decisions are made, begin.",
]

# Instruction tails for pure reasoning examples: architecture-level thinking,
# no drafting, no handoff.
REASONING_TAILS = [
    "Lay out the structural thinking you will carry into the draft.",
    "Work the problem at the level of architecture, so drafting stands on decisions rather than habits.",
    "Build the framework now, before any drafting begins.",
    "Set out how you will think about this across the whole arc.",
    "Map the structure and the tradeoffs, and settle the principles you will write from.",
    "Reason through the interactions at stake and end with the rules you will follow.",
    "Think it through as planning: what must be true, in what order, and why.",
    "Give the structural reasoning only; the drafting will come later.",
    "Set the load-bearing decisions down in full, so the draft has something solid to stand on.",
    "Reason through the whole problem at the planning level and stop when the structure is decided.",
]

# Instruction tails for negative examples: forward-oriented, framing the trap
# as a live pull to reason past while generating.
NEGATIVE_TAILS = [
    "Reason through why this pull would undermine the story, and how you will think past it as you generate.",
    "Treat the trap as a temptation you are feeling right now; work past it and decide what you will do instead.",
    "Think past the weak shape before it reaches the page: why it fails, and what replaces it in your planning.",
    "Examine the pull, understand the damage it would do downstream, and set the corrective reasoning you will follow while writing.",
    "The slide is happening in your planning right now. Refuse it with reasons, and settle the replacement pattern.",
    "Work out why the easy shape would cost the story, then build the habit of thought that avoids it from here on.",
    "Face the trap as a forward-looking hazard: name it, reject it on structural grounds, and choose the stronger path you will draft from.",
    "Do not merely flag the problem; reason your way past it and end with the decisions you will carry into the writing.",
]


def pick(rng, seq):
    return seq[rng.randrange(len(seq))]


def ordered_subset(rng, keys, k):
    """A random subset of `keys` of size k, preserving the given order."""
    chosen = rng.sample(list(keys), k)
    return [key for key in keys if key in chosen]


def distribute(count, items, rng):
    """Split `count` across `items` as evenly as possible; returns [(item, n)]."""
    base = count // len(items)
    extra = count - base * len(items)
    order = list(items)
    rng.shuffle(order)
    pairs = []
    for i, item in enumerate(order):
        pairs.append((item, base + (1 if i < extra else 0)))
    return pairs


def join_paragraphs(paragraphs):
    return "\n\n".join(p.strip() for p in paragraphs)


def build_instruction(rng, intro_bank, frame, context, stage, tail):
    parts = [pick(rng, intro_bank), frame, context]
    if stage:
        parts.append("You are in " + stage + ".")
    parts.append(tail)
    return " ".join(p.strip() for p in parts if p and p.strip())


def make_record(rec_id, rec_type, category, subcategory, instruction, response):
    return {
        "id": rec_id,
        "type": rec_type,
        "category": category,
        "subcategory": subcategory,
        "instruction": instruction,
        "response": response,
    }
