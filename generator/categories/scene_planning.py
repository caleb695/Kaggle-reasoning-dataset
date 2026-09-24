"""Scene planning: designing the scenes and set pieces a book is made of.

This library reasons about the unit below the chapter: what a scene is for, how
it turns, where it enters and leaves, how sequences of scenes form a movement,
and how set pieces are staged so that they cost something. It is the practical
middle layer between an outline and a draft.
"""

CAT = {
    "id": "scene_planning",
    "label": "Scene planning: purpose, turns, sequences, and set pieces",
    "moves": {
        "scene_purpose": [
            "Give every planned scene a goal, an obstacle, and an outcome, and make the outcome a change. A scene in which someone tries something and the situation is identical afterward is a transition, and a plan should carry few of them deliberately and none by accident.",
            "Decide the scene's reason in one line before deciding its content: what becomes possible, known, or impossible because this scene exists. If the line cannot be written, the scene is atmosphere, and atmosphere belongs inside a scene that is already doing structural work.",
            "Let multi-purpose scenes carry two or three jobs rather than one: advancing the plot, developing a relationship, delivering information, and demonstrating character can often share a single scene, and planning the combination keeps a book from feeling padded.",
        ],
        "scene_turn": [
            "Plan the turn rather than the events. A scene's power comes from the moment the situation changes direction: someone reveals, refuses, concedes, or discovers, and the plan should know what that moment is before the scene's dialogue is imagined.",
            "Place the turn close to the end of the scene. Scenes that turn early spend their remaining length confirming what the reader already understands, and the same material becomes momentum when the turn is held until it forces the scene to stop.",
            "Make the turn cost somebody something. A reversal that costs nothing is information, and a plan built from costless turns produces a book in which much happens and little accumulates.",
        ],
        "entry_and_exit": [
            "Enter late and leave early at the planning level: decide the first image and the last image of each scene and plan nothing outside them. A scene that begins before the pressure and ends after the consequence reads as slow even when every paragraph is competent.",
            "Decide what each scene inherits and what it hands on. Writing those two states into the plan turns a list of scenes into a chain, and it makes continuity a design property rather than a correction.",
            "Choose the last line's work rather than its content: a scene should end on a change, a decision, or a question the reader wants settled. Endings that summarize what the scene established are the most common source of an exhausting book.",
        ],
        "sequence_design": [
            "Group scenes into sequences with their own question and crest, then chain the sequences into movements. A plan made of individual scenes has no rhythm, while a plan made of sequences has shape at two scales at once and reads as paced rather than as long.",
            "Design the sequence's crest before its approach. Knowing which scene carries the peak lets the preceding scenes prepare it with information, positioning, and cost instead of competing with it.",
            "Alternate the sequence's pressure with preparation rather than with rest. The scene before a crest should tighten what is available, and the scene after should show what the crest spent, which is how a sequence becomes a curve rather than a spike.",
        ],
        "set_piece_design": [
            "Design set pieces around a turn rather than around spectacle. The staging is the medium, not the point: what the reader remembers is the moment the terms changed, and the plan should know what that moment is and who pays for it.",
            "Give each set piece a cost and a consequence before planning its staging. A confrontation that ends exactly as it began is a performance, and the plan should record what changes in the story's ledger because the set piece happened.",
            "Plan the physical facts the staging depends on: the space, the positions, the constraints, and the two or three features that decide the outcome. Deciding these in the plan keeps the drafting from inventing geography and resolving the scene by convenience.",
        ],
        "ordering": [
            "Order scenes by consequence rather than by chronology. The most informative arrangement is usually not the order in which things happened, and the plan should choose where to withhold, where to intercut, and where to delay a revelation for structural reasons.",
            "Place the quiet scene deliberately. A low-pressure scene deepens attachment and gives the next sequence something to threaten, and leaving it unplanned means the middle fills with pressure of the same kind, which is what flatness is made of.",
            "Decide the chapter breaks as part of the ordering. Where a chapter ends determines what the reader is holding when it ends, and the plan should place breaks on changes rather than on scenes that have simply run out.",
        ],
        "pov_and_staging_plan": [
            "Decide whose scene each planned scene is before deciding what happens in it. The viewpoint selects which facts can arrive and in what order, and the plan should note the choice where the scene depends on a limited view.",
            "Plan what the viewpoint character cannot see. Withholding is a structural decision: a scene can be designed so that the reader is inside a limited perspective that is nonetheless fair, and the plan should record what is deliberately unavailable.",
        ],
        "scene_budget": [
            "Budget the book's scenes against its movements: a sense of how many scenes each movement can afford and which of them are load-bearing. A plan that spends its best scenes early has to inflate later ones, and the budget is what prevents that.",
            "Decide which scenes are expendable and which are not. Knowing which three scenes a movement cannot do without makes revision faster and stops the plan from treating all scenes as equally necessary.",
        ],
    },
    "problems": [
        {
            "id": "scene_without_turn",
            "frames": [
                "Your planned scenes establish things without changing anything.",
                "The scenes in your plan end where they began, with more information available.",
                "Your scene list is made of conversations that confirm what the reader already knows.",
            ],
            "context": "A scene whose outcome does not change the situation is a transition, and transitions spent as scenes are what make a draft feel long.",
            "stages": ["the scene's design", "the chapter's arrangement", "the sequence's crest"],
            "openers": [
                "Give the scene a goal and let the outcome be the opposite of what was attempted, or the same success at a cost. Either version changes the state; the current version only moves information from one place to another.",
                "Reason about what is different after the scene than before it, in one of five currencies: possibility, knowledge, allegiance, resource, or self-account. If nothing has changed in any of them, the scene is a summary that has been staged, and the plan should merge it into a scene that is already changing something.",
            ],
            "closers": [
                "Commit to scenes whose outcomes change the story's state, and merge the ones that only deliver information into scenes that turn.",
                "Give each scene a goal, an obstacle, and a changed outcome, and let the plan record the change rather than the content.",
            ],
        },
        {
            "id": "repeated_scene_shape",
            "frames": [
                "Your plan contains several scenes that work the same way.",
                "Every chapter in your middle has the same rhythm of approach and confrontation.",
                "Your scenes differ in content and not in shape.",
            ],
            "context": "Repetition of scene shape is what makes a book feel as though nothing is happening even when a great deal is.",
            "stages": ["the sequence design", "the middle's arrangement", "the chapter's functions"],
            "openers": [
                "Vary the shape as well as the content: a pursuit, a negotiation, a discovery, a refusal, a domestic scene under pressure. Each shape has its own tempo and its own kind of turn, and alternating them keeps the reader from learning the pattern.",
                "Reason about the sequence as a rhythm: what the previous sequence did, what this one has to do differently, and where the contrast lands. Structural variety is a planning decision, and it disappears if the plan is written one scene at a time.",
            ],
            "closers": [
                "Commit to a sequence plan with varied scene shapes and a defined crest, and to alternating pressure with preparation rather than with more pressure of the same kind.",
                "Give each sequence a different shape from the one before it, and let the plan record what kind of turn each sequence delivers.",
            ],
        },
        {
            "id": "set_piece_without_consequence",
            "frames": [
                "A set piece in your plan consumes chapters and changes nothing.",
                "Your confrontation resolves and the situation returns to its previous state.",
                "You are planning spectacle without planning its bill.",
            ],
            "context": "Set pieces that cost nothing in the story's ledger make the surrounding chapters feel like filler.",
            "stages": ["the set piece's design", "the sequence's arrangement", "the movement's turn"],
            "openers": [
                "Decide the cost and the consequence before the staging: who is worse off, what is now impossible, and what the next scene inherits. The staging then has a purpose beyond itself, and the chapter earns its length.",
                "Reason about what the set piece proves. A confrontation should demonstrate something about a character or a rule of the world that the reader needs later, and the plan should name that demonstration before designing the spectacle.",
            ],
            "closers": [
                "Commit to set pieces that change the ledger: a cost, a consequence, and an inheritance for the following scene.",
                "Give each planned confrontation a turn and a bill, and cut the ones that carry neither.",
            ],
        },
        {
            "id": "chapter_overload",
            "frames": [
                "Your chapters are expected to accomplish too many unrelated things.",
                "The plan puts three turns in a chapter that has room for one.",
                "Your chapters are containers rather than units.",
            ],
            "context": "A chapter carrying more obligations than it can stage produces scenes that solve themselves and a reader who cannot say what happened.",
            "stages": ["the chapter's functions", "the scene list", "the movement's arrangement"],
            "openers": [
                "Fix the chapter's function and move the rest. A chapter can usually deliver one turn and support it with preparation and consequence; when the plan asks for three, the third is almost always a scene that belongs in the next chapter.",
                "Reason about the reader's attention. Obligations compete, and a chapter asked to establish a world, resolve a relationship, and reverse the plot will do all three shallowly, which reads as haste rather than as density.",
            ],
            "closers": [
                "Commit to one turn per chapter with supporting scenes around it, and relocate the surplus obligations rather than compressing them.",
                "Give every chapter a single function, and let the scene list serve that function only.",
            ],
        },
        {
            "id": "middle_sequence_sag",
            "frames": [
                "Your middle sequences develop without escalating.",
                "The plan's second movement is a series of scenes with the same stakes.",
                "Your sequences are shaped like a plateau rather than a curve.",
            ],
            "context": "Sequences that develop without charging produce a middle that reads as competent and inert.",
            "stages": ["the sequence design", "the crest's placement", "the movement's arrangement"],
            "openers": [
                "Give each middle sequence a charge: something the protagonist loses, spends, or lets someone else pay. Sequences that only add information are development in the plan's terms and stalling in the reader's.",
                "Reason about the sequence's crest and its cost together. A crest that the protagonist survives intact is a peak the reader will discount, and the plan should decide in advance what the peak takes.",
            ],
            "closers": [
                "Commit to sequences that charge as well as develop, each with a crest and a cost that the following sequence inherits.",
                "Plan the middle as a series of charges, and let the information arrive inside them rather than between them.",
            ],
        },
        {
            "id": "scenes_not_caused",
            "frames": [
                "Your scene order is a sequence of moments rather than of causes.",
                "Scenes in your plan happen because they come next.",
                "Your chapters are arranged by topic rather than by consequence.",
            ],
            "context": "Scenes that are not caused by earlier scenes produce a book the reader can put down between chapters without losing anything.",
            "stages": ["the scene list", "the ordering", "the movement's design"],
            "openers": [
                "For each planned scene, name the earlier decision that made it necessary. Scenes without a cause are candidates for cutting or relocating, and the ones with causes are the spine the plan should be built from.",
                "Reason about the chain: what this scene makes possible or impossible for the next. A plan that reads as a chain of consequences generates momentum without any scene being louder than the last.",
            ],
            "closers": [
                "Commit to a scene list in which each scene is caused by an earlier one and causes the next, and keep the uncaused material only where it earns its place as deliberate quiet.",
                "Build the order from consequences rather than from chronology, and check each scene's cause before drafting it.",
            ],
        },
    ],
    "traps": [
        {
            "id": "beat_sheet_as_script",
            "frames": [
                "Your scene briefs specify what characters will say and where they will stand.",
                "Your plan has grown specific enough that drafting has nothing to decide.",
                "You are writing the scenes in note form before writing them.",
            ],
            "slide": "The scene plan has become a transcript of the draft. Entrances, gestures, and exchanges are all fixed, so drafting turns into transcription, and the writing cannot respond to what the scene actually does, which is where a manuscript's best material usually comes from.",
            "stages": ["the scene brief's detail level", "the chapter's plan", "the review before drafting"],
            "openers": [
                "The pull is toward completeness, and the correction is to plan decisions rather than executions. Reason about what the scene must accomplish, what it costs, and what it hands on, and leave the staging to the moment of writing.",
                "Reason past it by asking, for each line of the brief, whether the drafting stage could decide it better with the scene in front of it. If it could, the line belongs to the drafting stage, and the plan keeps the obligations instead.",
            ],
            "damage": "Over-specified scene plans produce flat manuscripts. The writing has no decisions left, so the small inventions that make a scene feel inhabited never happen, and the revision stage has to create life inside a structure designed as a transcript of a scene that was never actually written well.",
            "reason_past": "Reason past it by keeping briefs at the level of purpose: goal, obstacle, outcome, cost, and what the scene leaves true. Everything else is available to the drafting stage, which is equipped to decide it better.",
            "closers": [
                "Commit to briefs that fix the scene's purpose and leave the execution to the writing.",
                "Keep the plan at the level of decisions, and let the drafting stage make the ones only the scene can make.",
            ],
        },
        {
            "id": "scenes_added_for_length",
            "frames": [
                "You are adding scenes to reach a target length or a chapter count.",
                "Your plan is growing sideways rather than escalating.",
                "You are filling the space between the beats you actually want.",
            ],
            "slide": "Scenes are being added to make the book the size it is supposed to be. Each addition is defensible on its own, the chapter count reaches the target, and the pressure spreads thinner across more pages until no scene is doing enough work to hold a reader.",
            "stages": ["the scene list", "the chapter's functions", "the middle's arrangement"],
            "openers": [
                "The pull is toward the target, and the correction is toward charge. Reason about what each added scene takes from the protagonist, and cut whatever cannot answer that question; a shorter book with pressure in every scene reads as fuller than a longer one with slack.",
                "Reason past it by asking whether the material in the added scene belongs inside an existing scene. Most padding is a good beat that has been given its own scene instead of being folded into one that already needed it.",
            ],
            "damage": "Length-driven additions dilute a book's momentum. The reader's sense of progress falls with every scene that does not change the situation, the important chapters have to be louder to be felt, and the revision stage has to do the cutting that planning avoided doing.",
            "reason_past": "Reason past it by measuring the plan in charges rather than in chapters. If the book needs more length, it needs more escalation rather than more scenes, and the escalation is a decision about cost rather than about content.",
            "closers": [
                "Commit to the scene list that the story requires, and add capacity through escalation rather than through additional scenes.",
                "Fold the padding into scenes that need the beat, and keep the plan's pressure per page constant.",
            ],
        },
        {
            "id": "reveal_before_setup",
            "frames": [
                "Your plan reveals information in the sequence that needed it earlier.",
                "A scene's meaning depends on material that arrives after it.",
                "You are planning the disclosure before planning what the reader needs to make sense of it.",
            ],
            "slide": "The information is placed where it is dramatic rather than where it is usable. Scenes are planned with the ending known, so their significance is invisible to a first-time reader, and the material that would have made them legible is scheduled later as a revelation.",
            "stages": ["the ordering", "the knowledge arc", "the sequence's design"],
            "openers": [
                "For each planned scene, decide what the reader must already know for the scene to work as intended. Anything that fails that test is a plant to be relocated earlier rather than a mystery to be preserved.",
                "Reason past it by reading the scene order as a first-time reader rather than as the author. Scenes that only make sense in hindsight are being staged for the wrong audience, and the plan should move the minimum necessary forward.",
            ],
            "damage": "Misplaced information produces scenes that read as confusing rather than as mysterious. The reader cannot tell whether something is significant, the later explanation has to do work that a plant would have done invisibly, and the book's clarity suffers in exactly the places where it needs to be strongest.",
            "reason_past": "Reason past it by scheduling the minimum information each scene requires and letting the mystery live in what remains unstated. Clarity about the situation and uncertainty about the outcome are compatible; confusion about the situation is not a mystery at all.",
            "closers": [
                "Commit to a scene order in which every scene is legible on a first read, with the mystery held in the outcome rather than in the situation.",
                "Place the plants before the scenes that depend on them, and let the planning pass run in the reader's order rather than the story's.",
            ],
        },
    ],
    "discipline": [
        "Every scene should be expressible as a goal, an obstacle, and a changed outcome; scenes that cannot be are transitions and should be few.",
        "Plan the turn before the content, and place it near the scene's end so the scene stops on the change.",
        "Set pieces need a cost and a consequence before they get staging, and sequences need a crest before they get scenes.",
    ],
    "themes": [
        {
            "id": "scene_to_sequence",
            "frames": [
                "You are turning an outline into a workable list of scenes.",
                "You want the book's middle to have shape rather than length.",
                "You are deciding how much to plan before drafting.",
            ],
            "question": "How do you turn an outline into scenes: what each one does, where it starts, and what it leaves changed?",
            "openers": [
                "The conversion runs in one direction and it is mechanical once the outline exists: each movement becomes two or three sequences, each sequence becomes three to five scenes with a crest, and each scene gets a goal, an obstacle, an outcome, and a position. The planning effort belongs at the sequence level, where the shape of the reading experience is decided.",
                "Scene planning is where a story's pressure becomes physical. The sequence's crest decides where the reader's attention peaks, the scenes between it decide what the peak costs, and the entry and exit points decide whether the whole thing reads as fast or as long.",
            ],
            "middles": [
                "Give each sequence one question and one crest. Sequences with two questions read as transitions, and sequences with two crests flatten the second by comparison.",
                "Decide the sequence's entry state and exit state in the plan. Knowing what has to change across the sequence keeps the individual scenes pointed at the same pressure rather than competing for importance.",
                "Distribute the information the sequence needs before the crest rather than at it. Material delivered during the crest competes with the crest, and material delivered after it reads as explanation.",
                "Vary the sizes of scenes deliberately: a short scene after a long one reads as acceleration, and two long scenes in sequence read as a plateau regardless of their content.",
                "Plan the transitions between sequences as deliberately as the sequences themselves. A movement's end should leave the protagonist in a condition the next sequence has to deal with, and the planning of that condition is what makes a middle feel like one book.",
                "Check the scene list against the chapter map: every chapter should contain one turn, and no chapter should contain two crests. Where the map and the list disagree, the sequence plan is what needs to change.",
            ],
            "closers": [
                "Commit to a scene list derived from sequences, each with a question, a crest, and an entry and exit state, and to chapters built around one turn each.",
                "Plan the sequences, then the scenes, then hand the briefs to the drafting stage with the executions left open.",
            ],
        },
        {
            "id": "set_piece_staging",
            "frames": [
                "You are planning a confrontation, a chase, or a public scene.",
                "You want a set piece to carry a chapter without becoming a spectacle.",
                "You are designing the physical facts of a scene that the story depends on.",
            ],
            "question": "How do you plan a big scene so that it turns the story instead of only being impressive?",
            "openers": [
                "A staged scene is built from four decisions: the space and its constraints, the positions and capabilities of everyone present, the moment the terms change, and the bill that comes due afterward. Staging without a turn is a performance, and a turn without staging is an announcement.",
                "Set-piece planning starts from what must be true when it ends. Deciding the exit condition first tells you which facts the staging has to establish, which is what keeps the scene's second half from inventing conveniences.",
            ],
            "middles": [
                "Plan the space before the action: exits, obstacles, distances, and the two or three features that will decide the outcome. Every later convenience in a staged scene traces back to geography that was never decided.",
                "Establish capabilities before the scene depends on them. A resource that appears at the moment of need discounts every earlier difficulty, so the plan should place its introduction where the reader can verify it.",
                "Decide where the reader's attention should be at each stage of the scene. Attention is a budget: a staged scene works when the plan indicates what matters at the beginning, what changes at the turn, and what the reader should be looking at when it ends.",
                "Give the scene a witness whose reaction carries the meaning. A confrontation lands harder through someone's response than through its own description, and the plan should decide who is watching and what they do about it.",
                "Plan the cost of the scene's aftermath: injury, exposure, lost ground, a debt incurred. Consequences decided in advance keep the following chapter from resetting to a neutral state, which is the most common way a strong set piece is wasted.",
                "Check the scene against the world's rules and the characters' established abilities. Consistency here is not a detail; it is what allows the reader to follow the scene rather than watch it.",
            ],
            "closers": [
                "Commit to a staged scene with a decided space, established capabilities, a turn with a price, and a bill that the next chapter inherits.",
                "Plan the exit condition first, then the staging that makes it arrive as a consequence rather than as a convenience.",
            ],
        },
    ],
    "principles": [
        "Scenes change state: goal, obstacle, changed outcome, in one of five currencies.",
        "Sequences have shape: one question, one crest, one entry state, one exit state.",
        "Set pieces earn their length with a turn, a cost, and a consequence decided before the staging.",
    ],
}
