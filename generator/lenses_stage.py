"""Stage-level lens reasoning.

The 17 lens pools in `lenses_a` and `lenses_b` reason at drafting height: they
talk about scenes, chapters, and the page. That is exactly right for the drafting
stage, and wrong for ideation, outlining, and revision, where a paragraph about
sentence rhythm or a scene's entry point answers a question nobody asked.

This module holds a planning-height paragraph bank per lens. Stages below
drafting draw from these instead, so a lens keeps its craft dimension while the
reasoning stays at the level of the work being done.
"""

PLANNING_LENSES = {
    "reader_trust": (
        "Plan the book around what the reader can infer. Every explanation the book intends to supply early is a conclusion the reader was capable of reaching later, and the plan should spend its explanations only where the inference is not available to anyone.",
        "Decide at the planning stage what the book will not explain. An unexplained act that the surrounding material accounts for is the reader's reward for paying attention, and a book whose plan explains everything has budgeted nothing for that pleasure.",
        "Treat withheld information as a debt with terms. The reader will carry an unanswered question across a long book only if the plan keeps showing that the question is live, and any question the plan forgets is experienced as an error rather than as a mystery.",
    ),
    "character": (
        "Decide the cast's wants before the plot's needs. Every principal character should want something independently of the story's problem, because those independent wants are what supply collisions when the main pressure is briefly quiet.",
        "Plan the boundaries rather than the traits. What each character will not do even to succeed is where they become legible, and those limits are set at the planning stage because later chapters rely on them.",
        "Give the cast an uneven distribution of competence, insight, and nerve. A book whose people are uniformly capable has no internal friction, and the plan should decide who is weak at what before the middle needs the friction.",
        "Build contradiction into the plan rather than into the exposition: generosity beside vanity, competence beside cowardice in one specific area. Contradictions that are only described read as character notes, while contradictions that produce behavior read as people.",
    ),
    "outline_obedience": (
        "Treat the plan as the constraint the later stages work inside. The decisions made here fix what the chapters must accomplish, so anything left undecided will be decided by whichever scene happens to be easiest later.",
        "Keep the book's obligations traceable to positions: what is established where, what is paid where, and what each movement hands on. Structure that cannot be traced is advice rather than a plan.",
        "Decide the structural questions rather than deferring them. Where the plan leaves the meaning of earlier material open, it guarantees a revision, because the chapters drafted before the decision will have assumed different answers.",
    ),
    "pacing": (
        "Shape the book's intensity as a curve. Escalation works by contrast, so the plan should decide where the book rests, where it crests, and what each crest costs rather than distributing pressure evenly across the chapters.",
        "Decide the aftermath positions as deliberately as the crisis positions. Consequences are where a story's pressure becomes weight, and a plan that schedules only its peaks produces a book that moves and does not accumulate.",
        "Vary the kind of pressure rather than the amount. Changing the currency of what is at risk is what keeps a long book's middle from reading as the same event with new names.",
        "Reserve the largest cost for the final movement and keep the earlier chapters from spending it. A book that has already used its biggest consequence has to invent a larger one, and invented stakes are read as inflation.",
    ),
    "continuity": (
        "Carry a state ledger across the whole book: injuries, possessions, promises, debts, and who knows what. The plan is where the ledger is created; anything the plan does not record will be contradicted by a later chapter.",
        "Track knowledge as rigorously as events. A character can only act on what they have been shown to know, so the plan should record the knowledge positions and treat every violation as a structural fault rather than a slip.",
        "Plan consequences forward rather than restoring a neutral baseline between movements. Fatigue, position, money, and trust should all reflect what the earlier chapters did, and that cumulative state is what makes a long book feel continuous.",
    ),
    "worldbuilding": (
        "Make the world's rules cost somebody something. A rule that never constrains a character is decoration, and the plan should decide which constraints the story's pressure depends on.",
        "Deliver the world through consequence and use rather than through explanation, and plan where the reader will learn each essential fact. World information that arrives without a scene that needs it is a detour, however interesting the material is.",
        "Decide the everyday texture of the world at the planning stage: what people eat, how they travel, what they fear, who holds power. Scale becomes legible through ordinary life, and the plan is where the ordinary details get chosen.",
    ),
    "scene": (
        "Plan scenes as units of change: a goal, an obstacle, and an outcome that alters what is possible, known, or intended. A scene that cannot be stated that way is a transition, and the plan should carry few of them on purpose.",
        "Decide what each scene inherits and what it hands on. Writing both states into the plan turns a scene list into a chain of causes, and it is what makes the drafting stage's work a matter of execution rather than invention.",
        "Give every scene a turn near its end. The moment the situation changes direction is what the reader remembers, and placing it late is what makes the scene end on pressure rather than on summary.",
    ),
    "prose": (
        "Decide the register the book intends to hold, and treat it as a promise to the reader rather than a preference of the writer. Register that shifts without a structural reason reads as drift.",
        "Budget the book's visible effort. Every book has a small number of passages that are meant to be noticed, and deciding where those are, at the planning level, is what keeps the rest of the prose in service of the story.",
        "Prefer plain, precise language as the book's default and reserve elaboration for the moments that earn it. The plan can name those moments now, which is cheaper than discovering later that the book has spent its intensity evenly.",
    ),
    "style_consistency": (
        "Plan the book's voice as a maintained system: a small set of permitted moves, a list of habits to avoid, and a rule for resolving conflicts between them. Consistency across a long book is a matter of procedure rather than memory.",
        "Decide where the voice may vary and why. Variation that follows structure, a new viewpoint, a new place, a changed state, reads as design, while variation that follows the writer's mood reads as inconsistency.",
        "Check the plan against the voice it implies before drafting. A structure that requires the register to change three times needs those changes designed rather than improvised.",
    ),
    "ai_patterns": (
        "Plan against the shapes that make machine-written prose recognizable before they enter the manuscript: the repeated negate-and-redefine construction, the constant three-item list, the summarizing sentence that restates what was just delivered, and the habit of announcing significance.",
        "Decide what the book will do instead of its tics. Prohibitions leave gaps where the habits were, so the plan should record the positive alternative: how a scene ends when it is not ending on a thesis, how a description works when it is not listing three things.",
        "Watch for the emotional shorthand that substitutes for observation and plan its replacements. Named physiological reactions are the most available indicators and the least specific, and the plan should decide what this book will use instead.",
    ),
    "emotion": (
        "Plan the emotional movement of the whole book, not only of its scenes: what the protagonist feels at the start, what the story does to that, and what remains at the end. Feelings that are never scheduled arrive as reactions to the plot rather than as a record of it.",
        "Decide which emotional states the book withholds and pays for later. A book that spends its strongest feeling early has nothing left for the ending, and the plan is where the budget is set.",
        "Give the cast different emotional signatures rather than a shared repertoire. Deciding at the planning level who withdraws, who attacks, and who goes quiet under pressure is what makes later scenes specific before they are written.",
    ),
    "dialogue": (
        "Plan what speech is for in each stage of the book. Conversations that exist to transfer information announce themselves, while conversations that exist because two people want incompatible things generate their own material.",
        "Decide what each principal character will not say. Withholding, evasion, and misdirection are structural decisions about the cast, and the plan should know what each person protects before the scenes require it.",
        "Plan the conflict under the conversation rather than the conversation itself. A scene between two people with opposing aims works with almost any content, while a scene between two people who agree needs the plan to give one of them a reason to stay.",
    ),
    "metaphor": (
        "Plan the book's figurative vocabulary as a system with a small number of families, assigned to particular characters or places. Recurrence inside a family accumulates meaning, while a new family arriving late reads as a change of author.",
        "Decide which images the book is saving. The comparisons reserved for the final movement cannot be spent in the middle, and the planning stage is where that reservation is made.",
        "Let the figurative register follow the structure. A shift at a new movement or a new viewpoint reads as design, while the same shift inside a chapter reads as inconsistency.",
    ),
    "humor": (
        "Plan where levity is allowed to come from. Humor generated by character is characterization, while humor generated by the narration distances the reader from the pressure the book has built.",
        "Decide what the book finds funny and what it refuses to treat lightly. A comedy of manners and a novel about grief can both use humor, and the plan has to decide which material is protected from it.",
        "Budget the book's wit. Sharp exchanges lose their value when everyone is capable of one, and the plan should decide which characters carry the humor and where it lands relative to the pressure.",
    ),
    "concrete": (
        "Decide the physical facts the story depends on before deciding its incidents: what the place is, what it costs to move through, what the characters do with their hands. Concrete particulars are what make a plan's pressure payable on the page.",
        "Plan the world's texture through what the characters handle rather than through description. Objects that appear because someone needs them generate both place and character, and the plan can choose them early.",
        "Anchor abstract pressures in physical consequences. A rule, a debt, or a fear becomes legible when the plan knows what it does to a body, a room, or a schedule.",
    ),
    "pov": (
        "Decide the book's point of view as a constraint on what can be told: which facts can arrive, in what order, and with what charge. The plan's information schedule depends on this choice more than on any other.",
        "Choose the viewpoint for what it withholds as well as what it reveals. A limited perspective is the mechanism that keeps the book's mysteries honest, and the plan should record where the limits are load-bearing.",
        "Plan where the reader is inside a character's interpretation and where they are outside it. The pattern of those positions is what produces suspense in one chapter and sympathy in another.",
    ),
    "action": (
        "Plan physical sequences around the decisions they force rather than around the spectacle they provide. The staging is the medium; what the reader takes away is who chose what, and at what cost.",
        "Decide the limits before the plan depends on them: what each character can do, what it costs them, and what happens when it fails. Capabilities established late discount every earlier difficulty.",
        "Give the plan's conflicts consequences that outlive them: injuries, lost ground, debts, exposure. A confrontation that resets to a neutral state is a performance rather than a turn.",
    ),
}

# Which lenses each stage may reason through.
STAGE_LENSES = {
    "ideation": ("reader_trust", "character", "outline_obedience", "continuity", "pacing",
                 "worldbuilding", "emotion"),
    "outline": ("outline_obedience", "pacing", "continuity", "character", "scene",
                "reader_trust", "worldbuilding", "emotion", "metaphor"),
    "revision": ("continuity", "prose", "style_consistency", "ai_patterns", "reader_trust",
                 "scene", "pacing", "character", "dialogue", "emotion", "metaphor", "pov"),
    "drafting": tuple(PLANNING_LENSES) + (
        "concrete", "dialogue", "humor", "action", "metaphor", "pov", "emotion",
    ),
}


def lens_bank(stage, lens, full_bank):
    """The paragraph bank to draw from: planning height below drafting."""
    if stage == "drafting":
        return full_bank
    return PLANNING_LENSES.get(lens, full_bank)
