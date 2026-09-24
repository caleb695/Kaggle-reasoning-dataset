"""Stage-level lens reasoning.

The 17 lens pools in `lenses_a` and `lenses_b` reason at drafting height: they
talk about scenes, chapters, and the page. That is exactly right for the drafting
stage and for revision, which works on written scenes.

It is wrong for brainstorming and outlining. A brainstorming request that
receives a paragraph about sentence rhythm, or an outlining request that receives
one about a scene's entry point, is being answered at the wrong height: it teaches
a decision the writer does not have in front of them and leaves the decision they
do have undeveloped.

This module holds a paragraph bank per lens for brainstorming and for outlining.
Each paragraph is about the work of that activity: for brainstorming, what makes
an idea into a story someone will follow; for outlining, what makes a story hold
together from first page to last.
"""

IDEATION_LENSES = {
    "reader_trust": (
        "Judge the idea by whether it makes someone want to know what happens, not by whether it is clever. The want comes from a person in specific trouble, and an idea that cannot produce that has not become a story yet.",
        "Ask what question the reader will be holding after the first pages, and whether the idea can keep answering and renewing it. An idea that keeps its only question for the end has nothing to carry the reading.",
        "Decide what experience the idea promises: dread, longing, delight, unease, momentum. A premise that does not imply an experience has to find one before it can be written.",
    ),
    "character": (
        "Choose the person the premise damages most. Whoever has the least ability to walk away will generate the most story, and whoever is most capable will generate the least pressure.",
        "Give the protagonist a want that can be photographed and a reason to need it now. A want without urgency produces a book that can always start tomorrow.",
        "Find the thing this person would not give up even to win. That boundary is what makes them legible, and it belongs to the idea rather than to a later rewrite.",
    ),
    "emotion": (
        "Decide what the story is about emotionally before deciding what it is about event-wise: the feeling you want the reader left holding.",
        "Look for the moment the idea promises where someone must choose between two things they want. That is where feeling comes from, and an idea with no such moment has nowhere to land.",
        "Make the stakes something a person can lose and feel. Stakes nobody can weigh produce events the reader watches rather than dreads.",
    ),
    "worldbuilding": (
        "Build the world only as far as it presses on the people in it. Rules matter when they make something expensive, forbidden, or dangerous.",
        "Find the one condition of this world that makes the story's problem unavoidable, and leave the rest in the notes.",
        "Count the cost of the world's wonders. A world where nothing is scarce gives its people nothing to struggle against.",
    ),
    "pacing": (
        "Test the premise by imagining three things that happen because of it. An idea that generates events has a book in it; an idea that needs new inventions on top is not one yet.",
        "Ask what keeps the pressure up after the first act. An idea whose only engine is the opening incident will stall where the book needs a middle.",
        "Look for the idea's turn: the moment the problem changes shape. An idea with one problem and no turn gives a long book nothing to do in its second half.",
    ),
    "scene": (
        "Imagine the scenes the idea already implies. If the material suggests moments where someone must choose and pay, it is a story; if it suggests description, it is a setting.",
        "Find the confrontation the premise is really about and keep it in view while the idea is shaped. Ideas that avoid their own central scene tend to be outlines of something else.",
        "Ask what the idea makes happen to someone rather than what it makes true about the world. Stories are events that fall on people.",
    ),
    "continuity": (
        "Decide, while the idea is still soft, what it will have to stay true to: one or two facts about the world or the past that every later choice respects.",
        "Look for the idea's promises to itself, and make sure the version you keep can pay them. An idea loaded with implications it cannot honour becomes a revision.",
        "Choose the version of the idea with the fewest moving parts. Fewer commitments in the premise means fewer contradictions later.",
    ),
    "concrete": (
        "Ground the idea in something that can be seen and done: a place with rules, a task with stakes, an object that matters.",
        "Prefer the specific over the representative. A story about one person's particular trouble reaches more readers than a story about everyone's general one.",
        "Find the physical fact inside the idea, the thing someone has to do with their hands, and build outward from there.",
    ),
    "metaphor": (
        "Find the image the idea keeps circling and decide whether it belongs to the story or to the mood. Images that only decorate can be set aside now rather than during revision.",
        "Let the idea's central image do structural work: if the same object or gesture can carry meaning at the start and at the end, the story has a spine before it has a plot.",
        "Watch for the idea that is itself a metaphor, where the meaning is entirely in the comparison. Those need a person in them before they can become scenes.",
    ),
    "outline_obedience": (
        "Decide what this idea commits the book to before any of it is planned. The promise made here is what later chapters have to keep.",
        "Separate what the idea requires from what it merely allows. The requirements will become the plan; the allowances are where invention stays free.",
        "Choose the idea whose obligations you would be glad to keep for a whole book, because those obligations are the work.",
    ),
    "pov": (
        "Decide whose experience this story is. The same events become a different book depending on who has to live through them, and the choice is usually visible in the idea already.",
        "Ask whose knowledge makes the story most interesting: the person who knows too little, the person who knows too much, or the person who is wrong.",
        "Choose the point of view the premise most needs rather than the one that is most convenient to tell. An idea told from the wrong vantage has to be discovered as a rewrite.",
    ),
    "dialogue": (
        "Listen for what the people in the idea would say to each other, and whether any of it would change anything. Ideas whose people only explain themselves are not yet dramatic.",
        "Find the conversation the premise makes inevitable, and let it shape the idea. If no conversation matters, the story may be about events happening to things rather than to people.",
        "Decide what the people in this idea cannot say to each other. That gap is usually where the story's pressure lives.",
    ),
    "humor": (
        "Notice where the idea is funny and whether the humour comes from the people or from the premise. Character-borne humour survives a long book; premise-borne humour runs out.",
        "Decide the register the story can carry, and keep the version of the idea that matches it. A grim story told in a comic key has to be a deliberate choice rather than an accident.",
        "Look for the absurdity inside the material and decide whether to use it or answer it. Ignored absurdity reads as a mistake.",
    ),
    "action": (
        "Find the physical stakes inside the idea: what can be lost or broken, and by whom. Ideas with a body in them hold attention differently than ideas without.",
        "Ask what the people in the idea are willing to do with their hands, and make sure the premise gives them something worth doing.",
        "Make the danger concrete before making it large. A specific physical risk is more persuasive than a general catastrophe.",
    ),
    "prose": (
        "Notice the kind of language the idea seems to want, and decide whether that voice can be sustained for a whole book rather than a page.",
        "Choose the version of the idea that can be told in the register you want to hold. Ideas that demand a voice you do not want to write are a long argument with yourself.",
        "Prefer the plainest statement of the idea. If it needs ornament to be interesting, the trouble is in the idea rather than in the telling.",
    ),
    "ai_patterns": (
        "Test the idea against the version of it that is easiest to write. If the premise reads like a familiar summary, it needs a specific person and a specific cost before it is worth writing.",
        "Look for the idea that arrives complete and unsurprising, the one that satisfies rather than unsettles. That is usually a sign of a shape borrowed rather than found.",
        "Prefer the idea with a complication you have not already solved in your head. The difficulty is the part that will keep the writing alive.",
    ),
    "style_consistency": (
        "Decide the idea's tone at the level of a whole book, and choose the version you can hold: wry, grave, tender, cold.",
        "Keep the idea's promise of register in mind when choosing between versions, because the register will have to survive every chapter.",
        "Reject any version of the idea that needs the book to change key halfway without a reason in the story.",
    ),
}

OUTLINE_LENSES = {
    "pacing": (
        "Plan the shape of the reader's attention: where the story tightens, where it lets them breathe, and what each tightening costs.",
        "Vary what is at risk rather than only how much. A story that raises the same threat repeatedly stops escalating, however loud it gets.",
        "Decide where the quiet scenes go before writing them off. Consequences need room, and an outline made only of crises leaves nothing to accumulate.",
    ),
    "character": (
        "Decide what each principal character wants independently of the main problem, because those wants are what collide when the plot is briefly quiet.",
        "Plan the arc as a series of choices rather than a change of temperament: what this person does differently at the end shows what happened to them.",
        "Decide what each character refuses to do, then build the outline so the story eventually requires it of them.",
    ),
    "scene": (
        "Plan each scene around the change it makes: what is different for someone when it ends.",
        "Decide where each scene enters and leaves. Most scenes begin too early and end too late, and the outline is where that is cheapest to fix.",
        "Give the scenes that matter a shape in the plan: what is being attempted, what interferes, and what it costs.",
    ),
    "continuity": (
        "Track what each character knows and when they learn it. A story breaks the moment someone acts on information they do not have.",
        "Plan consequences forward instead of resetting between chapters: injuries, debts, and promises should still be in force later.",
        "Decide what the story has already established and hold later chapters to it.",
    ),
    "reader_trust": (
        "Decide what the story will not explain and trust the reader to assemble. What the reader works out is remembered; what they are told is only received.",
        "Plan the questions the reader will be holding and when each is answered. A question the story forgets reads as a mistake rather than a mystery.",
        "Keep the clues honest: whatever the resolution needs must have been available earlier, even if only in plain sight.",
    ),
    "emotion": (
        "Plan where the story asks the reader to feel something, and make sure the ground has been laid before it does.",
        "Decide the emotional turn of each movement: what the reader should want by its end that they did not want at its start.",
        "Build the ending's feeling out of the story's costs rather than its events. What the reader mourns or celebrates has to have been paid for earlier.",
    ),
    "worldbuilding": (
        "Decide the world's rules and what each one makes impossible or expensive, then plan the story so those pressures do work.",
        "Introduce the world where it obstructs someone. A world learned in a lecture is scenery; a world learned while a character struggles with it is a place.",
        "Keep the invention serving the story's problem rather than competing with it.",
    ),
    "plot_architecture": (
        "Build the outline as a chain of causes: this happens because of that, and what it costs is what makes the next thing necessary.",
        "Decide the turns before the transitions. Where the story changes direction is structure; everything between turns is connective tissue and can be written later.",
        "Test the outline by asking what each part makes worse for someone. Parts that change nothing can be moved, merged, or cut.",
    ),
    "tension": (
        "Keep a question open at every point in the plan, and make sure the reader knows it is open before it is answered.",
        "Decide what the story is hiding from whom, and when the hiding stops being worth it.",
        "Plan the obstacles in the reader's way as carefully as the obstacles in the protagonist's: the order in which things are learned is half of the tension.",
    ),
    "momentum": (
        "Plan so that each part opens something the next part can close. A story that resolves everything it raises before moving on has nowhere left to pull from.",
        "Give the middle its own question rather than a longer version of the opening one.",
        "Decide what the reader is waiting for at each point, and make sure the answer keeps changing.",
    ),
    "information_management": (
        "Decide who knows what, and make the gaps between them do work in the plan rather than being repaired in dialogue.",
        "Plan the reveals in order of cost: what the reader learns early should make later events harder, not easier.",
        "Choose deliberately what the story withholds, and decide what the withholding forces people to do.",
    ),
    "conflict_escalation": (
        "Give the opposition a legitimate claim, and let the pressure come from two rights rather than one wrong.",
        "Raise the cost of the protagonist's choices rather than the volume of the opposition. Escalation is a price, not a number.",
        "Plan each defeat so that it removes an option. A setback that leaves everything as it was buys the story nothing.",
    ),
    "epic_scale": (
        "Keep the scale visible through people: what the world's events cost the cast in the same chapter they occur.",
        "Decide the price of the world's powers, and let magic or technology be as expensive as the story needs it to be.",
        "Plan the widening so that the story's problem grows with the scope rather than being replaced by it.",
    ),
    "chapter_arcs": (
        "Give every chapter something to change, so a reader can say what is different at its end.",
        "Plan the chapters as movements of the story rather than containers of scenes: each one takes a position and leaves it altered.",
        "Decide what question each chapter raises and when the story answers it, then place the chapters so the questions overlap.",
    ),
    "setup_payoff": (
        "Plant what the ending needs early and in plain sight, and let the payoff collect what the reader has been carrying.",
        "Decide the distance between the plant and the payoff, because the distance is what makes the recognition land.",
        "Plan the innocent reason each plant exists, so nothing in the story exists only to be used later.",
    ),
    "scene_construction": (
        "Plan the scene as a contest of wants: what each person is trying to get out of it, and which of them will not get it.",
        "Decide the turn before the content: what changes inside the scene, and who pays for it.",
        "Give each scene a job in the story's chain of cause and effect, and cut the ones that only deliver information.",
    ),
    "dialogue": (
        "Plan the conversations that change something, and decide what each speaker wants from the other before they start.",
        "Decide what cannot be said aloud in the scenes that matter, because that is what the scene will be about.",
        "Keep the talking in the plan to the encounters where the story turns; the rest can be handled in the writing.",
    ),
    "pov": (
        "Decide whose experience carries each movement, and let the choice cost something: the story should lose access to information it would like to have.",
        "Plan the story so that the point of view makes some things hard to see, because a vantage that costs nothing is only a camera.",
        "Choose the vantage that makes the story's central trouble most immediate, not the one that makes it easiest to explain.",
    ),
    "prose": (
        "Plan the register the story will hold, and choose the version of events that can be told in it from beginning to end.",
        "Keep the plan free of writing that belongs to the draft; the outline decides what happens, not how it sounds.",
        "Decide which moments the story will let itself be beautiful in, and spend them there rather than everywhere.",
    ),
    "metaphor": (
        "Find one image the story can return to, and plan what it means at each appearance so it accumulates rather than repeats.",
        "Use imagery to carry what the story would otherwise have to say, and decide where that substitution happens.",
        "Keep the story's central image tied to its action, so the meaning is discovered rather than explained.",
    ),
    "style_consistency": (
        "Decide the story's register once, and plan events that can be told inside it.",
        "Keep the plan's language plain, so the decisions stand on their own without the writing dressed up around them.",
        "Choose the shape of the story that the voice you want can carry for a whole book.",
    ),
    "ai_patterns": (
        "Prefer the plan with a complication that unsettles the familiar shape rather than one that completes it.",
        "Test the outline against how a reader would summarize it. If the summary is the whole story, the plan has no surprises left in it.",
        "Keep the plan specific: particular people in particular trouble rather than a general situation with roles filled in.",
    ),
    "humor": (
        "Decide where the story can afford levity, and let it come from the characters rather than from the narration.",
        "Plan the comic beats where they relieve pressure rather than where they interrupt it.",
        "Use humour to reveal people: what someone finds funny, or refuses to, shows character faster than description.",
    ),
    "action": (
        "Plan the physical sequences so their outcome follows from what the reader already knows about the space and the people.",
        "Decide the cost of each physical sequence before its spectacle, so the action changes the story rather than pausing it.",
        "Make the plan's physical events legible on the page: who is where, what is in the way, and what it costs to get past it.",
    ),
    "concrete": (
        "Plan with things rather than abstractions: the object that gets handed over, the door that is locked, the money that is short.",
        "Ground every movement of the story in a place and a task, so the reader is somewhere rather than being told about somewhere.",
        "Choose the specific detail that can carry a whole beat, and let the outline mark where it belongs.",
    ),
    "dialogue_voice": (
        "Decide which voices the story needs, so that characters can be told apart by what they say and what they avoid saying.",
        "Plan the conversations where power shifts, and let the rest of the talk be written in the draft.",
        "Keep the plan's dialogue intentions to what speech must accomplish rather than what it must say.",
    ),
}


def lens_bank(stage, lens, full_bank):
    """The paragraph bank to draw from, at the height of the stage's work."""
    if stage == "ideation":
        return IDEATION_LENSES.get(lens) or OUTLINE_LENSES.get(lens) or full_bank
    if stage == "outline":
        return OUTLINE_LENSES.get(lens) or full_bank
    return full_bank


def stage_lenses():
    """Which lenses each stage reasons with.

    Brainstorming and outlining keep the lenses that belong to their own work:
    a brainstorming record does not reason about obeying a plan that does not
    exist yet, and an outlining record does not reason about sentence rhythm.
    Drafting draws on every lens, and revision on the ones its passes touch.
    """
    drafting = (
        "pov", "concrete", "character", "scene", "pacing", "emotion", "dialogue",
        "humor", "action", "worldbuilding", "continuity", "outline_obedience",
        "reader_trust", "metaphor", "prose", "ai_patterns", "style_consistency",
    )
    return {
        "ideation": ("reader_trust", "character", "emotion", "worldbuilding", "pacing"),
        "outline": ("pacing", "character", "scene", "continuity", "reader_trust",
                    "emotion", "worldbuilding"),
        "drafting": drafting,
        "revision": ("continuity", "prose", "style_consistency", "ai_patterns", "scene",
                     "reader_trust", "pacing", "character", "dialogue", "emotion",
                     "metaphor", "pov"),
    }


STAGE_LENSES = stage_lenses()
