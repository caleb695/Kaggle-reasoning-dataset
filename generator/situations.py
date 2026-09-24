"""Outline conditioning.

Three jobs live here:

1. `render_outline_block` builds the compact outline slice that every request
   carries: the story's frame, the cast who are present, the open obligations
   that touch this chapter, and the chapter's required beats with the state it
   inherits and the state it must hand on.
2. `situation_paragraph` opens every response by reading that material as
   structural obligations, so the reasoning is anchored in the outline rather
   than floating free of it.
3. `commitment_paragraph` closes the response by converting the reasoning into
   the decisions to carry into the draft.

All generated text is structural and conceptual. No prose, no exemplification.
"""

PRESSURE_LABEL = {
    "pov": "whose perception carries the chapter",
    "concrete": "keeping the chapter physically grounded",
    "character": "what the chapter reveals through choice",
    "scene": "what the scene is for and when it enters and leaves",
    "pacing": "where the chapter sits on the book's intensity curve",
    "emotion": "how feeling is timed and individuated",
    "dialogue": "what speech is doing that narration cannot",
    "humor": "where levity comes from and what it costs",
    "action": "keeping the physical sequence legible and costly",
    "worldbuilding": "what the world's rules make possible or expensive",
    "continuity": "what the chapter inherits from the story's ledger",
    "outline": "how the chapter serves the plan's obligations",
    "trust": "what the reader is trusted to assemble alone",
    "metaphor": "where figurative language earns its place",
    "prose": "how the prose stays in service of the scene",
    "surface": "how the chapter avoids the familiar machine habits",
    "consistency": "how the chapter keeps the book's voice steady",
}


def _beats(chapter, limit=3):
    return [b.strip().rstrip(".") for b in chapter["beats"][:limit]]


def _join(items):
    items = [i for i in items if i]
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return items[0] + ", and " + items[1]
    return ", ".join(items[:-1]) + ", and " + items[-1]


def _cast_in_play(outline, chapter, limit=2):
    """The cast members this chapter's beats and state actually touch."""
    haystack = " ".join(
        [chapter["label"], chapter["function"], chapter["state_in"], chapter["state_out"]]
        + list(chapter["beats"])
    ).lower()
    named = [m for m in outline["cast"] if m["name"].split()[0].lower() in haystack]
    rest = [m for m in outline["cast"] if m not in named]
    return (named + rest)[:limit]


def _threads_in_play(outline, chapter, limit=2):
    n = chapter["n"]
    open_threads = [t for t in outline["threads"] if t["setup"] <= n <= t["payoff"]]
    rest = [t for t in outline["threads"] if t not in open_threads]
    return (open_threads + rest)[:limit]


def _clean(text):
    return text.strip().rstrip(".")


def render_outline_block(outline, chapter=None):
    """The context slice handed to the model with every request.

    With a chapter, the block is the drafting slice for that chapter. Without
    one, it is the whole-book view used for arc-level planning requests.
    """
    arc_mode = chapter is None
    cast = (outline["cast"] if arc_mode else _cast_in_play(outline, chapter))[:3]
    threads = outline["threads"] if arc_mode else _threads_in_play(outline, chapter, limit=1)
    numbers = [c["n"] for c in outline["chapters"]]
    cast_lines = []
    for m in cast:
        cast_lines.append(
            "%s, %s: wants %s; flaw, %s; secret, %s; knows, %s"
            % (m["name"], m["role"], _clean(m["want"]), _clean(m["flaw"]),
               _clean(m["secret"]), _clean(m["knows"]))
        )
    thread_lines = [
        "%s (opens chapter %s, pays off chapter %s): %s"
        % (t["name"], t["setup"], t["payoff"], _clean(t["carry"]))
        for t in threads
    ]
    lines = [
        "TITLE: %s -- %s, %s." % (outline["title"], outline["form"], outline["genre"]),
        "POV AND DISTANCE: %s." % outline["pov"],
        "PREMISE: %s" % _clean(outline["premise"]) + ".",
        "RULES OF THIS WORLD: %s." % "; ".join(_clean(r) for r in outline["rules"]),
        "CAST IN PLAY: %s." % " | ".join(cast_lines),
    ]
    lines.append("OPEN THREADS: %s." % "; ".join(thread_lines))
    if arc_mode:
        lines.append(
            "THREE-ACT ARC: %s | %s | %s"
            % (_clean(outline["act1"]), _clean(outline["act2"]), _clean(outline["act3"]))
        )
        lines.append("ENDING: %s." % _clean(outline["end"]))
        lines.append("PROMISES TO THE READER: %s." % "; ".join(_clean(p) for p in outline["promises"]))
        lines.append(
            "PLANNING SCOPE: the whole novel, chapters 1 to %s, planned before any chapter is drafted."
            % max(numbers)
        )
        return "\n".join(lines)
    lines.append(
        "TARGET CHAPTER %s OF %s -- %s. Function: %s."
        % (chapter["n"], max(numbers), chapter["label"], _clean(chapter["function"]))
    )
    lines.append("REQUIRED BEATS: %s." % "; ".join(_clean(b) for b in _beats(chapter)))
    lines.append("STATE ENTERING THE CHAPTER: %s." % _clean(chapter["state_in"]))
    lines.append("STATE THE CHAPTER MUST HAND ON: %s." % _clean(chapter["state_out"]))
    lines.append("CRAFT PRESSURE FOR THIS CHAPTER: %s." % PRESSURE_LABEL[chapter["pressure"]])
    return "\n".join(lines)


SITUATION_TEMPLATES = (
    "Chapter {n} of the outline carries {count} obligations at once, and they are these: {beats}. The chapter's entry state: {state_in}. Its exit state: {state_out}. That combination decides what the writing must do before it does anything else, and none of the obligations can be addressed outside the chapter's own pressure.",
    "The material in front of the draft is chapter {n}. Its stated function: {function}. It inherits this state: {state_in}. It owes the story this state: {state_out}. The chapter is not free to spend its length on atmosphere or on material the later chapters will need, because the obligations are structural before they are dramatic: {beats}.",
    "What chapter {n} must accomplish is already fixed: {beats}. The state entering the chapter: {state_in}. The state it must hand on: {state_out}. The reasoning below is not about whether those things happen but about the staging, the sequence, and the cost that make them happen as consequences rather than as announcements.",
    "The chapter in front of the work carries this function: {function}. The reader is still holding {thread} open from earlier chapters, the obligations are these: {beats}, and the chapter's entry state: {state_in}. The state it must leave behind: {state_out}. The craft problem is keeping all of that visible at once without the scene becoming an inventory of its own requirements.",
    "The outline hands chapter {n} {count} things it must do, which are these: {beats}. It arrives from this state: {state_in}. It departs into this state: {state_out}. The book has already promised this: {promise}. Before drafting, the writing has to decide where the chapter's central pressure sits, because the obligations will be satisfied through that pressure or not at all.",
    "Before the first sentence of chapter {n}, the obligations are already clear: {beats}. The chapter inherits this state: {state_in}. For the chapters that follow it must leave this state: {state_out}. It is also carrying {thread} as an open thread. Everything below is the reasoning that converts those requirements into decisions that can be executed at drafting speed.",
)

NEGATIVE_SITUATION_TEMPLATES = (
    "Chapter {n} is where the resistance shows up. The material in play is this state: {state_in}. The state the chapter owes the story: {state_out}. The obligations are these: {beats}. The pull described below is live at this exact point in the drafting, and it grows as the chapter gets harder, so it has to be reasoned past here rather than noticed later.",
    "The chapter in front of the draft is chapter {n}. Entry state: {state_in}. Exit state: {state_out}. The obligations: {beats}. The temptation below is the shortcut that makes those obligations easier to satisfy while quietly spending something the later chapters need.",
    "Chapter {n} has to carry its obligations out of the state it inherits and into the state the book needs next. What it inherits: {state_in}. What it must hand on: {state_out}. What it must deliver: {beats}. This is the moment where the easy shape described below becomes available, and where taking it would cost the book more than the chapter can see.",
    "At this point in the book the chapter has this function: {function}. It inherits this state: {state_in}, and it owes the story this state: {state_out}. Along the way it delivers these obligations: {beats}. The pull below is the kind that feels like craft while it is happening and reads as damage a hundred pages later.",
)

REASONING_SITUATION_TEMPLATES = (
    "Before any chapter of this book is drafted, the whole architecture is on the table. {act1} {act2} {act3} {end} The reasoning below works at that height because local choices only hold together when the book knows what it is building toward.",
    "The promises this book has already made are on the record: {promises}. Read at the level of the whole novel they form a schedule rather than a set of intentions. {act1} {act2} {act3} {end} Reasoning at this height is about distribution and cost rather than about any single scene.",
    "The shape in front of the work is a whole novel, so the unit of decision is the book rather than the chapter. {premise} {act1} {act2} {act3} {end} Everything below is scheduling: what the book spends early, what it renews in the middle, and what it holds for the last movement.",
    "The architecture is fixed at the level of the outline, and the question below concerns the whole of it. {premise} The movements the book has to pay for: {act1} {act2} {act3} The ending that has to arrive as consequence: {end} Nothing in that sequence can be repaired later, which is why the decisions below are made now.",
)

COMMITMENT_TEMPLATES = (
    "Commit to the chapter's obligations in this order, and let each decision answer one of them: {beats}. Hold the chapter's exit state as the standard the scene is measured against when it ends: {state_out}.",
    "Fix the order of work now rather than discovering it while drafting: {beats}. Write until the story holds this state: {state_out}, then stop, and let the chapter's craft pressure be handled inside that sequence rather than beside it.",
    "Carry three decisions into the draft. The staging that satisfies the first obligation: {beat_1}. The cost that makes the second consequential: {beat_2}. The state change that has to be true when the chapter ends: {state_out}.",
    "Settle the chapter on its obligations: {beats}. Write through the character's own wants rather than through the outline's language, and let the exit state decide when the chapter is finished rather than when the material runs out: {state_out}.",
)

NEGATIVE_COMMITMENT_TEMPLATES = (
    "Carry the replacement decisions forward instead of the pull: {beats}. Written from that pattern, the shortcut stops being attractive because the work it would have saved is being done well instead.",
    "Write from the corrective pattern rather than from the corrective intention: {beats}. The chapter still has to hand on this state: {state_out}. The shortcut stays closed because the alternative is concrete, not because it is forbidden.",
    "Let the replacement reasoning govern the drafting. The obligations to deliver: {beats}. The state the chapter must hand on: {state_out}. Refuse the shortcut at the point where it is cheapest to take.",
)

REASONING_COMMITMENT_TEMPLATES = (
    "Settle the architecture on these terms: the promises are scheduled, the threads are assigned positions, and the costs are distributed across the book's movements. Everything drawn later is drawn inside this structure.",
    "Fix the plan at the level it was reasoned: obligations assigned to chapters, costs carried forward, and no thread opened without a position where it closes. The drafting that follows is execution rather than invention.",
    "Commit to the structure and to the order in which it spends its material: deposits early, renewals across the middle, and the largest collections in the last movement. Each chapter is then written inside a ledger rather than beside one.",
)


def _beats_slots(chapter):
    beats = _beats(chapter)
    lowered = [b[0].lower() + b[1:] if b else b for b in beats]
    return {
        "n": chapter["n"],
        "count": len(beats),
        "beats": "; ".join(lowered),
        "beats_and": _join(lowered),
        "beat_1": lowered[0],
        "beat_2": lowered[1] if len(lowered) > 1 else lowered[0],
        "state_in": chapter["state_in"],
        "state_out": chapter["state_out"],
        "function": chapter["function"],
        "label": chapter["label"],
    }


def _story_slots(outline):
    return {
        "promise": outline["promises"][0],
        "promises": "; ".join(outline["promises"][:2]),
        "thread": outline["threads"][0]["name"],
        "threads": "; ".join(
            "%s, carried as %s" % (t["name"], _clean(t["carry"]))
            for t in outline["threads"][:3]
        ),
        "premise": outline["premise"],
        "act1": outline["act1"],
        "act2": outline["act2"],
        "act3": outline["act3"],
        "end": outline["end"],
    }


def situation_paragraph(outline, chapter, rng, rec_type):
    """The outline-grounded opening paragraph of a response."""
    slots = _story_slots(outline)
    if chapter is not None:
        slots.update(_beats_slots(chapter))
    if rec_type == "negative":
        bank = NEGATIVE_SITUATION_TEMPLATES
    elif rec_type == "reasoning":
        bank = REASONING_SITUATION_TEMPLATES
    else:
        bank = SITUATION_TEMPLATES
    return rng.choice(bank).format(**slots)


def commitment_paragraph(outline, chapter, rng, rec_type):
    """The outline-grounded closing paragraph of a response."""
    slots = _story_slots(outline)
    if chapter is not None:
        slots.update(_beats_slots(chapter))
    if rec_type == "negative":
        bank = NEGATIVE_COMMITMENT_TEMPLATES
    elif rec_type == "reasoning":
        bank = REASONING_COMMITMENT_TEMPLATES
    else:
        bank = COMMITMENT_TEMPLATES
    return rng.choice(bank).format(**slots)
