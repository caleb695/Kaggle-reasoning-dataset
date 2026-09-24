"""The stages of writing a novel, and the reasoning each one requires.

The dataset covers the whole process rather than only the drafting moment:

    ideation  ->  finds the premise, the promise it makes, and the choice that
                  will test it, before anything is structured
    outline   ->  turns a premise into a schedule of pressures: movements,
                  turns, chapter functions, thread positions, an earned ending
    drafting  ->  writes a specific chapter of the outlined book, deciding what
                  the chapter must establish, turn, and hand on
    revision  ->  reworks what exists, in the order revision has to happen:
                  structure first, then scene, then continuity, then line

Each stage carries its own instruction frames, its own instruction tails, and
its own response openers, so the same craft rule is reasoned at the level the
writer is actually working at. Transition records (the planning-to-writing
handoff) exist only at the drafting stage, where writing follows reasoning.

All banks are generic: they never name a particular book, so the dataset stays
pure reasoning supervision and the trained behavior transfers to any outline the
caller supplies at inference.
"""

STAGES = ("ideation", "outline", "drafting", "revision")

STAGE_ORDER = STAGES

STAGE_INFO = {
    "ideation": {
        "label": "Idea development",
        "deliverable": "a premise with an engine, the promise it makes, and the choice that tests it",
        "question_words": "the idea itself",
    },
    "outline": {
        "label": "Story architecture",
        "deliverable": "a plan whose chapters have functions, positions, and prices",
        "question_words": "the structure of the book",
    },
    "drafting": {
        "label": "Chapter drafting",
        "deliverable": "the decisions the chapter will be written from",
        "question_words": "the chapter in front of you",
    },
    "revision": {
        "label": "Revision",
        "deliverable": "a diagnosis and the order of passes that will fix it",
        "question_words": "what exists already",
    },
}

# Which categories carry a stage's native reasoning. Records at a stage draw a
# share of their craft items from these, and the rest from the full library.
NATIVE_CATEGORIES = {
    "ideation": ("idea_generation", "idea_shaping"),
    "outline": ("outline_design", "arc_mapping", "scene_planning"),
    "drafting": (),
    "revision": ("revision_craft", "revision_diagnosis"),
}

# Every stage reasons only with the libraries that belong to it, so a
# brainstorming request never reasons about sentence rhythm and an outline
# request never reasons about a chapter's entry point.
ALLOWED_CATEGORIES = {
    "ideation": (
        "idea_generation", "idea_shaping", "plot_architecture",
        "character_decisions", "epic_scale",
    ),
    "outline": (
        "outline_design", "arc_mapping", "scene_planning", "plot_architecture",
        "chapter_arcs", "setup_payoff", "tension", "momentum",
        "information_management", "conflict_escalation", "epic_scale",
        "continuity_outline",
    ),
    "drafting": (
        "plot_architecture", "conflict_escalation", "character_decisions",
        "information_management", "scene_construction", "chapter_arcs",
        "setup_payoff", "tension", "momentum", "epic_scale", "pov_perception",
        "concrete_grounding", "prose_discipline", "metaphor_imagery",
        "emotion_craft", "dialogue_voice", "action_physicality",
        "continuity_outline",
    ),
    "revision": (
        "revision_craft", "revision_diagnosis", "scene_construction", "tension",
        "momentum", "character_decisions", "information_management",
        "continuity_outline", "prose_discipline", "dialogue_voice",
    ),
}

NATIVE_SHARE = 0.65

# ---------------------------------------------------------------------------
# Instruction frames: where the writer is standing.
# ---------------------------------------------------------------------------

FRAMES = {
    "ideation": {
        "reasoning": (
            "You are developing an idea into something a book can be built on, and the story is not yet decided.",
            "You are looking for the engine of a story rather than its subject.",
            "You are deciding what kind of book this will be before deciding what happens in it.",
            "You have promising material and no plot: a place, a relationship, a situation, a what-if.",
            "You are testing an idea against the question of whether it can carry a novel.",
        ),
        "negative": (
            "You are attached to an idea and can feel it resisting story.",
            "You are developing material that reads as a setting rather than a story.",
            "You are holding an idea whose appeal is its premise and not its people.",
            "The idea keeps producing atmosphere and no decisions, and you are about to build on it anyway.",
        ),
    },
    "outline": {
        "reasoning": (
            "You are turning a decided premise into the structure of a novel before any drafting begins.",
            "You are building the plan: the movements, the turns, the thread schedule, and the ending the book has to earn.",
            "You are designing the architecture, and the decisions at stake govern the whole book rather than one chapter.",
            "You are deciding the plan that future chapters will be drafted from.",
        ),
        "negative": (
            "You are outlining, and the plan keeps resolving into a shape you have seen before.",
            "You are building the structure and can feel it being arranged to be defensible rather than to be felt.",
            "You are scheduling the book and the pull is to keep every option open.",
            "You are laying out the plan while it quietly avoids the confrontation the premise implies.",
        ),
    },
    "drafting": {
        "transition": (
            "You are drafting the scene this problem is standing in the way of.",
            "You are writing the scene in front of you, and the problem below has to be settled before the first line.",
            "You are at the desk with the scene ahead of you and the problem below still open.",
            "You are inside the chapter where this problem has just surfaced.",
        ),
        "reasoning": (
            "You are drafting a chapter of a novel that is already planned, and the decision below belongs to the book rather than to the page.",
            "You are mid-manuscript, deciding something that will govern many chapters rather than one scene.",
            "You are inside the draft, working a problem whose correct handling depends on the whole arc.",
            "You are writing this book and the question below has to be answered at the level of the novel rather than the scene.",
        ),
        "negative": (
            "You are drafting, and the pull described below is active in the writing right now.",
            "You are inside the chapter, and the temptation below is the one the draft keeps offering.",
            "You are at the page where the weak shape below is currently the easiest available move.",
            "You are writing and you can feel the pull described below starting to operate.",
        ),
    },
    "revision": {
        "reasoning": (
            "You are revising: the drafts exist and the question is what to change, and in what order.",
            "You are reworking a chapter before moving on, deciding what it needs structurally rather than line by line.",
            "You have a drafted chapter that is not yet doing its job, and the revision decisions are ahead of you.",
            "You are in the second pass through the manuscript, where the problems are structural and the fixes have to be chosen.",
        ),
        "negative": (
            "You are revising and the pull is toward the fix that is easiest to perform rather than the one the draft needs.",
            "You are in revision, where the damage described below is usually introduced.",
            "You are reworking a chapter and the shortcut below would make the draft look finished sooner.",
            "You are in the pass where the temptation below is strongest, because the prose is already readable.",
        ),
    },
}

# ---------------------------------------------------------------------------
# Instruction tails: what the reasoning has to produce.
# ---------------------------------------------------------------------------

TAILS = {
    "ideation": {
        "reasoning": (
            "Reason at the level of the idea: what it promises, who it costs, and what would turn it into scenes.",
            "Work the material until it has an engine that generates events, and say what tests it.",
            "Reason about the premise's load-bearing parts and stop when the story's engine is identified.",
            "Settle what the book is about and what it will demand of its people, at the level of the idea.",
        ),
        "negative": (
            "Reason past the pull now, at the level of the idea, and decide what would make this a story rather than a scenario.",
            "Work past the weak shape and settle what the idea's engine will be before anything is outlined.",
            "Name the pull, see what it would cost the book, and decide what replaces it at the premise level.",
            "Reason about the idea the way an editor would, forward from here, and end with the decisions that make it load-bearing.",
        ),
    },
    "outline": {
        "reasoning": (
            "Reason at the level of structure, and stop when the plan contains decisions rather than intentions.",
            "Settle the scheduling: what is planted where, what turns where, and what is earned by the final movement.",
            "Lay out the architecture and the tradeoffs, and end with the plan a chapter can be drafted from.",
            "Reason about the whole arc, then commit to the structure and the order in which it spends its material.",
        ),
        "negative": (
            "Reason past the pull at planning distance, and decide what the structure will do instead.",
            "Identify what the weak shape would cost the book, and settle the architectural decision that prevents it.",
            "Work past it now, while the plan is still cheap to change, and commit to the structure that holds.",
            "Reason about the damage the shape would do downstream, and end with the plan you will build from.",
        ),
    },
    "drafting": {
        "transition": (
            "Work through the structural problem completely, then move straight into writing the scene.",
            "Reason your way through it in full, then begin the scene.",
            "Settle every decision the problem turns on, then carry them onto the page as you start the scene.",
            "Think the problem through to the end of the reasoning, then let the scene take over.",
            "Work out exactly how the scene must be built, then start writing it.",
            "Do the structural thinking first; when nothing is left to decide, begin the scene.",
            "Resolve the craft question in your head, then write into the scene without further commentary.",
            "Plan until the path is firm, then cross from planning into the scene itself.",
        ),
        "reasoning": (
            "Give the structural reasoning only; the drafting will come later.",
            "Reason through the whole problem at the level of the book and stop when the structure is decided.",
            "Set out how you will think about this across the chapters it touches.",
            "Reason through the interactions at stake and end with the rules you will write from.",
        ),
        "negative": (
            "Reason through why this pull would undermine the story, and how you will think past it as you generate.",
            "Treat the trap as a temptation you are feeling right now; work past it and decide what you will do instead.",
            "Think past the weak shape before it reaches the page: why it fails, and what replaces it in your planning.",
            "Do not merely flag the problem; reason your way past it and end with the decisions you will carry into the writing.",
        ),
    },
    "revision": {
        "reasoning": (
            "Decide the revision in the order it has to happen, and stop when the decisions are settled.",
            "Reason about what must change and what must be protected, and end with the passes you will run.",
            "Work at the level of cause rather than symptom, and end with the change that corrects the whole.",
            "Reason about the draft as a system, and settle what the revision is allowed to touch.",
        ),
        "negative": (
            "Reason past the pull before starting the pass, and decide what the revision will actually do.",
            "Name the shortcut, see what it would leave in the book, and choose the correction that costs something.",
            "Work past the temptation while the manuscript is still movable, and end with the passes you will run.",
            "Do not settle for the visible fix; reason to the change the chapter needs and commit to it.",
        ),
    },
}

# ---------------------------------------------------------------------------
# Response openers: the first paragraph of a response situates the reasoning.
# ---------------------------------------------------------------------------

OPENERS = {
    "ideation": {
        "reasoning": (
            "An idea becomes a story when someone wants something that costs them, and something makes the wanting dangerous. Test the material against that shape: who wants what, why now, and what failure would mean for them.",
            "Before anything is structured, the idea has to be load-bearing: it must generate events, force choices, and survive being told badly. Reasoning at this level is deciding what the book is actually about, which is usually narrower and more personal than the material suggests.",
            "Premises live or die on the pressure they create rather than the novelty they display. The work here is finding the situation's built-in demand: what the premise makes impossible to avoid, and who has to pay for it.",
            "A book is a promise made in the first pages and paid across the rest. Deciding the idea means deciding the promise, the pressure that tests it, and the change that will make the ending feel earned rather than announced.",
        ),
        "negative": (
            "The pull described below is visible earlier than drafting, at the moment the premise is being chosen, and it is cheaper to resist here than anywhere else in the process.",
            "This is a trap that is normally discovered in a finished draft, when the fix is a rewrite. Reasoning about it now, at the level of the idea, is the cheapest possible place to catch it.",
            "Ideas that cannot generate scenes feel generous while they are being developed, and the cost only appears when the book has to produce events. The pull is worth naming at the premise stage rather than the plotting stage.",
            "At this distance the temptation looks like imagination rather than avoidance. Reasoning past it now means the structure that follows is built on an engine instead of on atmosphere.",
        ),
    },
    "outline": {
        "reasoning": (
            "An outline is a schedule of pressures rather than a list of events: decide where the book spends its setup, where it turns, and what each chapter is responsible for handing on.",
            "Structure is the order in which a story spends what it has. Reasoning at this level means deciding what is planted for later, what is paid early, and what the ending is allowed to cost.",
            "The plan has to be strong at three scales at once: the movement, the chapter, and the thread that runs through both. Work them as one system, because decisions at one scale become constraints at the others.",
            "Deciding the architecture means deciding what the reader is waiting for at every point in the book. That is a scheduling problem: anticipation has to be created, maintained, and discharged, and every chapter does some of all three.",
        ),
        "negative": (
            "The pull described below is a planning failure, which means it is cheap to correct now and expensive to correct after three hundred pages have been written inside its shape.",
            "Structure problems are invisible while the plan is a summary and obvious once the plan becomes chapters. Reasoning at this distance is the only place the correction costs nothing but thought.",
            "A weak structure is usually a defensible idea applied too purely: the shape is recognisable, so it feels safe. The damage appears as a book that reads competently and moves nobody.",
            "The temptation here produces a plan that looks complete. Completeness is the trap: what matters is whether each part has a function and a price, which is what the reasoning below settles.",
        ),
    },
    "drafting": {
        "transition": (
            "The decisions below are what the scene is written from, so settle them before the first line and let the writing execute rather than negotiate.",
            "The chapter has obligations and a length; the reasoning that follows converts them into staging, sequence, and cost rather than into intentions.",
            "What follows is the planning the draft needs rather than the draft itself: what the chapter must do, in what order, and what it must leave behind.",
            "Reasoning first, page second. The problem in front of the scene has to be decided at the level it actually lives at, and then the scene begins from those decisions.",
        ),
        "reasoning": (
            "This decision reaches past the scene it appears in, so it is reasoned at the level of the book: what the choice costs later, and what it makes available.",
            "A problem that looks local is usually structural. The reasoning below works the whole arc the decision touches, because fixing it scene by scene is how a manuscript accumulates contradictions.",
            "The question is about the book rather than the page, which means the answer has to hold for chapters that have not been drafted yet. Reasoning at this height is how a draft stays consistent with itself.",
            "Stepping back from the page is the point here: the choice governs many chapters, and the reasoning below decides it once rather than re-deciding it scene by scene.",
        ),
        "negative": (
            "The pull described below is live in the writing right now, and it grows as the chapter gets harder, so it is reasoned past here rather than noticed later.",
            "The temptation is the shortcut that makes the current chapter easier while spending something the later chapters need. Naming it at drafting speed is what keeps it from reaching the page.",
            "The damage described below is the kind that reads as craft while it is happening. It has to be refused on structural grounds before the paragraph exists, not diagnosed afterwards.",
            "The weak shape is available now, which is exactly why the reasoning has to happen now: the replacement has to be decided before the writing starts, not after it fails.",
        ),
    },
    "revision": {
        "reasoning": (
            "Revision is ordered, not exhaustive: structural decisions first, because every later pass is wasted work if the structure moves underneath it.",
            "A drafted chapter that is not working usually has one cause and several symptoms. Reasoning here means finding the cause, then deciding which changes are allowed to follow from it.",
            "Revision fixes the book rather than the page. The reasoning below decides what the draft needs at the level of cause, and what it must be protected from while the change is made.",
            "Every revision decision has a cost somewhere else in the manuscript. The work is choosing the change that improves the whole, then checking what it breaks before making it.",
        ),
        "negative": (
            "The pull described below is the reason revision so often makes manuscripts smoother and weaker, and it is strongest exactly where the prose is already readable.",
            "Revision is where the cheapest available fix is most tempting, because the draft looks finished enough to polish. Reasoning past it now is what keeps the second pass from being the last one.",
            "The shortcut below produces a manuscript that passes a quick read and fails a slow one. It is refused here, at the level of cause, before the pass begins.",
            "The damage described below is cumulative: the easy fix stays acceptable until the whole book has been shaped around it, at which point the correction is a rewrite.",
        ),
    },
}

# ---------------------------------------------------------------------------
# Behavioural contract: the last line of every instruction.
# ---------------------------------------------------------------------------

CONTRACTS = (
    "Reason in structural and conceptual terms only; do not write any prose.",
    "Structure and concept only: no prose is to be written as part of the reasoning.",
    "Keep the reasoning structural. Do not draft prose, quoted lines, or invented detail.",
    "Reasoning only. The output is decisions, costs, and staging, not prose.",
    "Hold to craft reasoning alone; no written passages of any kind.",
    "Reason about the craft and stop there, with no prose on the page.",
)

SUBJECT = {
    "ideation": "this idea",
    "outline": "this book's structure",
    "drafting": "this chapter",
    "revision": "this draft",
}


def deliverable_line(stage):
    return "Deliverable: %s." % STAGE_INFO[stage]["deliverable"]


# ---------------------------------------------------------------------------
# Context lines: how the reasoning relates to the material at hand.
# ---------------------------------------------------------------------------

CONTEXT_LINES = {
    "ideation": (
        "The material is still open, so the reasoning here decides the book rather than describing it.",
        "Nothing is fixed yet; the value of this reasoning is in the decisions it makes rather than the options it lists.",
        "Treat the material as a proposal that has to survive scrutiny before anything is built on it.",
    ),
    "outline": (
        "The premise is decided, so the reasoning works inside it and decides the structure.",
        "The plan is being made now, and the drafting stage will inherit whatever is decided here.",
        "The outline you produce is the constraint later chapters are written inside, so the reasoning has to commit.",
    ),
    "drafting": (
        "The outline you have been given fixes what this chapter must accomplish, so the reasoning works inside those obligations rather than renegotiating them.",
        "The plan already decides the chapter's obligations; what remains is how they are staged, ordered, and paid for.",
        "The book's established state and its plan are both fixed, and the reasoning below decides how the chapter meets them.",
    ),
    "revision": (
        "The draft exists and cannot be un-written, so the reasoning decides what changes and what the change costs.",
        "Everything already drafted is material; the reasoning decides which of it survives the pass.",
        "The manuscript is movable, which means the decisions here are about order as much as about content.",
    ),
}

# ---------------------------------------------------------------------------
# Which craft lenses each stage reasons with most naturally.
# ---------------------------------------------------------------------------

LENS_AFFINITY = {
    "ideation": ("reader_trust", "character", "continuity", "outline_obedience", "pacing"),
    "outline": ("outline_obedience", "pacing", "continuity", "character", "scene", "reader_trust"),
    "drafting": (),  # every lens applies; the chapter's craft pressure leads
    "revision": ("continuity", "prose", "style_consistency", "ai_patterns", "scene", "reader_trust"),
}
