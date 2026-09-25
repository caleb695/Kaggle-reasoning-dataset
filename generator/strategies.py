"""Reasoning strategies: how a decision is reached, not what it is about.

The craft libraries supply the content of the reasoning. These banks supply its
form: the moves a writer uses to get a decision rather than a preference. They
are included in a share of every stage's records, tagged on the record, so a
training run can balance them.

Research note on why these exist: reasoning data transfers best when its
*strategies* vary, not only its topics, and traces that compare options, reason
backward from an outcome, keep a ledger of costs, and end with a check the
writer can run while drafting teach reusable procedure rather than reusable
phrasing. The last group (`verify`) is the cheap form of self-verification: an
explicit condition the writer checks in the draft instead of trusting the plan.
"""

STRATEGIES = {
    "two_routes": {
        "label": "Compare two routes and choose on stated grounds",
        "paragraphs": (
            "Two routes are available here, and the choice should be made on stated grounds rather than on taste. One route costs the character something the reader has already seen them value; the other costs time. Choose the first when the unit's job is character, the second when its job is plot, and when it has to do both, take the first and let the second arrive as its consequence.",
            "The decision has two defensible answers, so reason about which failure is cheaper. Route one risks a slower passage and a reader who understands more than the character does. Route two risks a faster passage that spends meaning the book has not deposited yet. Choose the failure the book can absorb at this point in its arc, and say why in one line before moving.",
            "Where two options look equally good, they are not: they differ in what they commit the book to later. Reason about the tenth chapter each option implies, and choose the one whose implied chapter is the one the book actually wants to reach.",
        ),
    },
    "backward": {
        "label": "Reason backward from the ending",
        "paragraphs": (
            "Decide the end first and reason backward. Ask what has to be true at the last line for the unit to have done its job, then what has to be true one step before that, and continue until the reasoning reaches the opening. Backward reasoning prevents the middle from being filled with whatever is available.",
            "Work from the outcome the book needs at the far end of this material, and treat the reasoning as a path that must arrive there. Forward motion tends to lower stakes as it searches for what is dramatic; backward motion shows where the story has to be planted for the arrival to be earned.",
            "Name the condition that must hold when this is finished, then decide what it requires, and only then decide the order of events. Structured this way, the reasoning produces obligations rather than options, and obligations are what a draft can execute.",
        ),
    },
    "cost_ledger": {
        "label": "Keep a ledger of costs",
        "paragraphs": (
            "Keep a ledger as the reasoning proceeds: what each decision takes from the character, from the reader's patience, and from the later chapters that will have to pay for it. A decision with no cost attached is decoration, and decoration in a load-bearing position reads as weakness.",
            "For each choice, write down the price and the payer. If the same character pays every time, the story is not escalating so much as repeating; if nobody pays, nothing has been decided. The ledger is the fastest way to see whether the plan is doing work.",
            "Track what the unit spends rather than what it contains. Material is finite at every scale: the chapter has one turn available, the book has a limited number of revelations, and the reasoning should assign those resources to the positions where they matter most.",
        ),
    },
    "pre_mortem": {
        "label": "Assume the failure and find where it would show",
        "paragraphs": (
            "Assume the work has been drafted and has failed in the way this kind of problem usually fails. Identify the sentence, beat, or chapter where the failure would be visible, and place the decision that prevents it at that spot rather than planning to repair it later.",
            "Before committing, reason about the most likely way this goes wrong, and decide which of its causes is structural rather than local. Structural causes are the ones that cannot be fixed by better execution, and those are the ones the reasoning has to remove now.",
            "Read the plan as an unsympathetic editor: the moment where attention slips, the line where the reader could stop believing, the turn that arrives before it has been earned. Decide which of those risks the reasoning has to close and which it can carry.",
        ),
    },
    "constraints_as_conditions": {
        "label": "Turn the constraints into conditions",
        "paragraphs": (
            "Write the constraints down as conditions the finished unit must satisfy, then reason until each condition has a decision attached to it. Constraints without a decision attached are discovered during drafting in the form of problems.",
            "The requirements here are few but they interact, so reason about them as a system: satisfying one usually makes another expensive. Decide which requirement is the one the unit exists to satisfy, and let the others be arranged around it rather than added beside it.",
            "Separate the non-negotiables from the preferences before choosing anything. The non-negotiables are what the surrounding story has already promised; the preferences are what would be nice. Reasoning that muddles the two produces a plan that cannot be defended when it is tested by a later chapter.",
        ),
    },
    "weakest_link": {
        "label": "Strengthen the weakest link rather than the strongest part",
        "paragraphs": (
            "Find the weakest link in the reasoning so far and strengthen that one instead of improving the part that already works. Structural failure is almost always local, and it is almost always the place where the thinking is thinnest.",
            "Reason about which single decision carries the most weight for the rest, and decide that one first. Everything else becomes cheaper once the load-bearing decision is settled, and nothing else compensates if it is wrong.",
            "Rank the decisions by how expensive they are to reverse later. Make the irreversible ones here, in the reasoning, and leave the cheap ones to be discovered while drafting.",
        ),
    },
    "reader_model": {
        "label": "Reason from the reader's model of events",
        "paragraphs": (
            "Reason from the reader's model rather than the plan's: what they know, what they expect to happen next, and what they would conclude from this as staged. The gap between the plan's version and the reader's version is where suspense, surprise, and confusion all come from.",
            "Check the reasoning against a first-time reader who has not seen the plan. Anything that only makes sense because the ending is known is an obligation the draft has not yet earned, and the reasoning has to plant it here.",
            "Decide what the reader should be able to predict before this unit ends. Predictability is not a flaw when the reader is right about the shape and wrong about the price, and the reasoning should be clear about which of those the unit is trading on.",
        ),
    },
    "ordering": {
        "label": "Order the work by consequence",
        "paragraphs": (
            "Order the decisions by consequence: the structural choice first, the scene-level choices that follow from it second, and the local choices last. Reversing that order is how drafts end up polished in places that have to be rewritten.",
            "Decide the sequence of work before deciding the content. Knowing that one choice forecloses another changes which choices are available, and reasoning out of order produces plans that cannot be executed in the order they were imagined.",
            "Separate what has to be decided now from what can be decided in the draft. The reasoning should carry only the decisions that the writing cannot make for itself, because decisions deferred to drafting are usually the ones drafting is equipped to make.",
        ),
    },
    "verify": {
        "label": "Leave a check the draft can run",
        "paragraphs": (
            "Leave a check for the moment of drafting. State the condition that decides whether the decision held: a thing the reader should be able to infer, a state that should be true at the unit's end, or a cost that should have been paid on the page. Checks are cheap while drafting and expensive after the draft is finished.",
            "Decide how the reasoning will be falsified. Name what would show that the decision was wrong, and where in the draft that evidence would appear. A decision that cannot fail is not a decision; it is a preference with reasons attached.",
            "Set the verification before the writing: what the unit must establish, what it must not spend, and what it must leave true for the chapters after it. The draft is then checked against those conditions rather than judged by how it feels.",
        ),
    },
}

STRATEGY_ORDER = tuple(STRATEGIES)

# Which strategies suit which record types.
TYPE_STRATEGIES = {
    "transition": (
        "two_routes", "backward", "cost_ledger", "pre_mortem",
        "constraints_as_conditions", "weakest_link", "reader_model", "verify",
    ),
    "reasoning": (
        "backward", "two_routes", "cost_ledger", "constraints_as_conditions",
        "ordering", "weakest_link", "verify",
    ),
    "negative": (
        "pre_mortem", "reader_model", "cost_ledger", "weakest_link",
        "constraints_as_conditions", "verify",
    ),
}

# Which strategies are the verification form (a check the draft can run).
VERIFY_STRATEGIES = ("verify",)
