"""The stages of writing a novel, and the thinking each one requires.

The dataset covers the whole process rather than only the drafting moment, and
each stage teaches the work of that stage as an activity:

    ideation  ->  brainstorming: finding an idea that makes a story, with someone
                  to follow, something they want badly, and trouble that will not
                  let them have it
    outline   ->  outlining: building the story so that it works, deciding what
                  happens, why it happens, and what it costs
    drafting  ->  writing: deciding how the chapter in front of you gets written,
                  inside the outline the caller supplied
    revision  ->  revising: finding what is wrong with the draft, fixing it at the
                  cause, and protecting what already works

Every bank below is written in the voice of that activity rather than in the
voice of a process. Each stage carries its own instruction frames, tails,
openers and context lines, so the same craft rule is reasoned where the writer is
actually standing. Transition records (the planning-to-writing handoff) exist
only at the drafting stage, where writing follows the reasoning.

All banks are generic: they never name a particular book, so the dataset stays
pure reasoning supervision and the trained behavior transfers to any outline the
caller supplies at inference.
"""

STAGES = ("ideation", "outline", "drafting", "revision")

STAGE_ORDER = STAGES

STAGE_INFO = {
    "ideation": {
        "label": "Brainstorming",
        "deliverable": "an idea that makes you need to know what happens next: a person to "
                       "follow, something they want badly, and trouble that will not let "
                       "them have it",
        "question_words": "the story you are trying to find",
    },
    "outline": {
        "label": "Outlining",
        "deliverable": "a story that works from the first page to the last: what happens, "
                       "why it happens, and what it costs",
        "question_words": "how the story is built",
    },
    "drafting": {
        "label": "Writing",
        "deliverable": "how this chapter gets written: what the scene does, whose eyes it "
                       "is, and what the reader learns",
        "question_words": "the chapter in front of you",
    },
    "revision": {
        "label": "Revision",
        "deliverable": "what to change, what to keep, and the order to work in",
        "question_words": "the draft on the desk",
    },
}

# Which categories carry a stage's native reasoning. Records at a stage draw a
# share of their craft items from these, and the rest from the other libraries
# that belong to the same stage.
NATIVE_CATEGORIES = {
    "ideation": ("idea_generation", "idea_shaping"),
    "outline": ("outline_design", "arc_mapping", "scene_planning"),
    "drafting": (),
    "revision": ("revision_craft", "revision_diagnosis"),
}

# Every stage reasons only with the libraries that belong to it, so a
# brainstorming request never reasons about sentence rhythm or a chapter's entry
# point, and an outlining request never reasons about a character's hands.
ALLOWED_CATEGORIES = {
    "ideation": (
        "idea_generation", "idea_shaping",
        "genre_epic_fantasy", "genre_scifi", "genre_thriller",
    ),
    "outline": (
        "outline_design", "arc_mapping", "scene_planning", "plot_architecture",
        "chapter_arcs", "setup_payoff", "tension", "momentum",
        "information_management", "conflict_escalation", "epic_scale",
        "continuity_outline",
        "genre_epic_fantasy", "genre_scifi", "genre_thriller",
    ),
    "drafting": (
        "plot_architecture", "conflict_escalation", "character_decisions",
        "information_management", "scene_construction", "chapter_arcs",
        "setup_payoff", "tension", "momentum", "epic_scale", "pov_perception",
        "concrete_grounding", "prose_discipline", "metaphor_imagery",
        "emotion_craft", "dialogue_voice", "action_physicality",
        "continuity_outline", "genre_epic_fantasy", "genre_scifi", "genre_thriller",
    ),
    "revision": (
        "revision_craft", "revision_diagnosis",
    ),
}

# How much of a stage's records reason from that stage's own libraries. Brain-
# storming and revision reason with nothing else: a brainstorming request that
# talks about thread schedules is an outlining request, and a revision request
# that plans an arc is planning rather than repair. Outlining keeps the
# structural libraries alongside its own, and drafting draws on the full craft
# library, since writing a chapter is where all of it converges.
NATIVE_SHARE = {
    "ideation": 1.0,
    "outline": 0.65,
    "drafting": 0.0,
    "revision": 1.0,
}

# ---------------------------------------------------------------------------
# Instruction frames: where the writer is standing.
# ---------------------------------------------------------------------------

FRAMES = {
    "ideation": {
        "reasoning": (
            "You are brainstorming a novel, and there is no story yet: only an image, a place, a person, or an itch.",
            "You are looking for a story worth writing, and the ideas you have are not stories yet.",
            "You are starting a book, and the premise keeps sliding away whenever you try to say what it is about.",
            "You have material you love and no trouble in it yet.",
            "You are testing an idea by imagining the book it would become.",
        ),
        "negative": (
            "You are brainstorming, and the idea keeps producing atmosphere instead of trouble.",
            "You are attached to a premise and can feel it refusing to become a story.",
            "You are developing an idea that is all situation and no want.",
            "You are about to build on a premise in which nobody wants anything badly enough.",
        ),
    },
    "outline": {
        "reasoning": (
            "You are outlining the story: the idea is settled and now it has to work.",
            "You are deciding what happens, why it happens, and what it costs.",
            "You are building the order of events, and every part has to earn its place.",
            "You are outlining a long story whose middle keeps trying to sag.",
            "You are turning a premise into a story a reader will follow to the end.",
        ),
        "negative": (
            "You are outlining, and the plan keeps becoming a list of things that could happen in any order.",
            "You are outlining, and the shape keeps resolving into one you have seen before.",
            "You are outlining, and the real trouble keeps getting postponed to a later chapter.",
            "You are building the outline and can feel it protecting the protagonist from the hard thing.",
        ),
    },
    "drafting": {
        "transition": (
            "You are writing the scene in front of you, and the problem below has to be settled before the first line.",
            "You are at the desk with the scene ahead of you and the problem below still open.",
            "You are inside the chapter where this problem has just surfaced.",
            "You are about to write this scene, and one decision in it will shape every line that follows.",
        ),
        "reasoning": (
            "You are writing a chapter from the outline you have been given, and one decision needs thinking through before you start.",
            "You are at the desk with the chapter's requirements in front of you, working out how to write it.",
            "You are writing this chapter, and how you handle this will set the pattern for the ones that follow.",
            "You are inside the draft, and the way this is written decides whether the chapter works.",
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
            "You are revising a draft you have written, and something in it is not working.",
            "You are reading back through the manuscript, deciding what to change.",
            "You are revising, and the problems are bigger than the sentences.",
            "You are in the second pass, where the fixes have to be chosen rather than found.",
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
            "Reason until the material has a person who wants something badly, something standing in the way, and a reason to keep reading.",
            "Push the idea past the version you already like, and keep the one that produces trouble.",
            "Find the story inside the material: who it happens to, what they want, and what it costs them.",
            "Work the idea until you can say what happens and why it matters, and stop there.",
        ),
        "negative": (
            "Reason past it now, while the idea is still soft, and find the story that would not have this problem.",
            "Name the pull, say what it costs the story, and reason to the idea that avoids it.",
            "Work past the comfort and get to the want, the obstacle, and the stakes.",
            "Reason to the version of this idea that creates trouble instead of atmosphere.",
        ),
    },
    "outline": {
        "reasoning": (
            "Reason about the story as a whole: what happens, why it happens next, and what it costs.",
            "Build the order of events so that each one causes the next and the ending arrives because of what came before.",
            "Decide the turns, the trouble, and the price, and stop when the story holds together.",
            "Work until every part of the story is doing something the story needs.",
        ),
        "negative": (
            "Reason past it while the plan is still cheap to change, and build the story the material actually demands.",
            "Identify what the weak shape would cost the story, and decide what the outline does instead.",
            "Work past the pull and commit to the order of events that makes the trouble escalate.",
            "Reason to the shape that keeps the reader's question alive, and end with the plan you will build from.",
        ),
    },
    "drafting": {
        "transition": (
            "Work through the problem completely, then move straight into writing the scene.",
            "Reason your way through it in full, then begin the scene.",
            "Settle every decision the problem turns on, then carry them onto the page as you start the scene.",
            "Think the problem through to the end of the reasoning, then let the scene take over.",
            "Work out exactly how the scene must be written, then start writing it.",
            "Do the thinking first; when nothing is left to decide, begin the scene.",
            "Resolve the craft question in your head, then write into the scene without further commentary.",
            "Plan until the path is firm, then cross from planning into the scene itself.",
        ),
        "reasoning": (
            "Work out how the chapter handles this in the writing, and stop once it is decided.",
            "Reason it to the page: what the scene shows, whose eyes it is, and what the reader learns.",
            "Settle it as a decision the writing will execute, and keep the reasoning free of prose.",
            "Think it through as the writer of this chapter, then stop before the writing begins.",
        ),
        "negative": (
            "Reason through why this pull would weaken the chapter, and how you will write past it.",
            "Treat the trap as a temptation you are feeling right now; work past it and decide what you will do instead.",
            "Think past the weak shape before it reaches the page: why it fails, and what replaces it in the writing.",
            "Do not merely flag the problem; reason your way past it and end with the decisions you will write from.",
        ),
    },
    "revision": {
        "reasoning": (
            "Decide what to change, what to leave alone, and what to do first.",
            "Reason to the cause of the problem and the change that removes it.",
            "Work out what the draft needs and what it must not lose.",
            "Choose the fix, then check what it would break before you start.",
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
            "Brainstorming is not collecting ideas; it is finding the one with trouble inside it. What follows works the material toward a person who wants something badly and something that will not let them have it.",
            "An idea becomes a story when someone wants something and cannot simply take it. The reasoning below looks for that want, the resistance to it, and the scenes it would produce.",
            "Ideas arrive as images and moods, and stories are made of wants under pressure. The work here is turning one into the other.",
            "The test of an idea is the story it produces. What follows pushes the material until events start following from wanting, and drops whatever only decorates.",
        ),
        "negative": (
            "This pull shows up while brainstorming, when an idea can still be loved without being tested, and it is cheapest to name here.",
            "The temptation below feels like imagination. It produces material that holds attention while it is being developed and produces no story once it has to make events.",
            "Premises fail before outlines are written: what looks like a story turns out to be a situation. Catching that now costs nothing but thought.",
            "Ideas that cannot produce trouble feel generous while they are being developed, and their cost appears only when the book has to make something happen.",
        ),
    },
    "outline": {
        "reasoning": (
            "Outlining is where a story is made to work: causes, consequences, and an order that makes the ending necessary rather than convenient.",
            "A story holds together when each thing that happens causes the next and costs somebody something. What follows arranges the material against that standard.",
            "The outline is the story seen from above: what happens, why, and what it costs. The reasoning below decides those in the order a reader will meet them.",
            "The story is decided here, before any scene is written, which is what makes it cheap to change and expensive to get wrong.",
        ),
        "negative": (
            "The pull below produces an outline that reads as complete and behaves as empty, which is why it is worth naming while the plan is still easy to change.",
            "Structure problems stay invisible while they are summaries. This temptation looks like flexibility and turns into a middle with nothing at stake.",
            "The trap here is a shape that could carry any story and therefore none. The reasoning works past it toward the one this material demands.",
            "This damage is paid later, chapter by chapter. Reasoning now, while the plan is only a plan, is where it costs nothing.",
        ),
    },
    "drafting": {
        "transition": (
            "The decisions below are what the scene is written from, so settle them before the first line and let the writing execute rather than negotiate.",
            "The chapter has obligations and a length; the reasoning converts them into staging, sequence, and cost rather than into intentions.",
            "What follows is the thinking the writing needs rather than the writing itself: what the chapter must do, in what order, and what it must leave behind.",
            "Thinking first, page second. The problem in front of the scene gets decided before the scene begins.",
        ),
        "reasoning": (
            "The decision below is a writing decision: what the chapter shows, whose eyes it is, and what the reader learns from it.",
            "What follows settles how the chapter is written, so the writing can follow it instead of relitigating it line by line.",
            "This is reasoned at the desk, before it becomes prose: what the scene does, where it enters and leaves, and what it costs the people in it.",
            "Writing this chapter means deciding what it does to the reader and how, which is what follows.",
        ),
        "negative": (
            "The pull below is live in the writing, and it grows as the chapter gets harder, so it is reasoned past here rather than noticed later.",
            "The temptation is the shortcut that makes this chapter easier while spending something later chapters need.",
            "The damage described below reads as craft while it is happening, which is why it has to be refused before the paragraph exists.",
            "The weak shape is available now, which is why the replacement has to be decided before the writing starts.",
        ),
    },
    "revision": {
        "reasoning": (
            "Revision starts with the cause rather than the symptom. What follows finds what is actually wrong and the change that removes it.",
            "The draft is material; the reasoning decides what survives. This fixes the problem at its source and protects what already works.",
            "Reading back is not revising. What follows turns the problem into a diagnosis, and the diagnosis into an order of work.",
            "What follows is the repair: what is wrong, why it is wrong, and what to do first.",
        ),
        "negative": (
            "The temptation below makes the draft look finished sooner and read worse later, which is why it is reasoned past before the pass begins.",
            "This is the cheapest available fix, and the reason so much revision leaves manuscripts smoother and weaker.",
            "The shortcut below trades the book's problem for the writer's comfort. The reasoning works past it to the change the draft actually needs.",
            "This damage is cumulative: each small convenience becomes a constraint on the next chapter.",
        ),
    },
}

# ---------------------------------------------------------------------------
# Behavioural contract: the last line of every instruction.
# ---------------------------------------------------------------------------

CONTRACTS = (
    "Reason in structural and conceptual terms only; the prose comes after.",
    "Structure and concept only: no prose is to be written as part of the reasoning.",
    "Keep the reasoning structural. Do not draft prose, quoted lines, or invented detail.",
    "Reasoning only. The output is decisions, costs, and staging, not prose.",
    "Hold to craft reasoning alone; no written passages of any kind.",
    "Reason about the craft and stop there, with no prose on the page.",
)

SUBJECT = {
    "ideation": "this idea",
    "outline": "this story",
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
        "Nothing is decided yet, which makes this the cheapest place in the whole process to get it right.",
        "The material is still soft; the reasoning should end with a story specific enough to follow.",
        "Everything here is still open, so the work is generation rather than repair.",
    ),
    "outline": (
        "The idea is settled; what follows decides how it becomes a story.",
        "These are the decisions the chapters will be written inside, so they are made rather than deferred.",
        "The outline is what the later writing inherits, so the reasoning commits rather than lists options.",
    ),
    "drafting": (
        "The outline you have been given fixes what this chapter must accomplish; the reasoning decides how it is written.",
        "The chapter's obligations are set; what remains is how they reach the page.",
        "The writing follows this reasoning, so it settles what the chapter does rather than describing it.",
    ),
    "revision": (
        "The draft exists, so the question is what to change and what to leave alone.",
        "Everything on the page is material; the reasoning decides what survives.",
        "The manuscript is movable, so the order of the work matters as much as the changes.",
    ),
}

# ---------------------------------------------------------------------------
# Which craft lenses each stage reasons with most naturally.
# ---------------------------------------------------------------------------

LENS_AFFINITY = {
    "ideation": ("reader_trust", "character", "emotion", "worldbuilding", "pacing", "genre"),
    "outline": ("pacing", "character", "scene", "continuity", "reader_trust",
                "emotion", "worldbuilding", "genre"),
    "drafting": (),  # every lens applies; the chapter's craft pressure leads
    "revision": ("continuity", "prose", "style_consistency", "ai_patterns", "scene",
                 "reader_trust", "pacing", "character"),
}
