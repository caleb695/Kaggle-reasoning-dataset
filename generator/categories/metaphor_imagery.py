"""Metaphor, imagery, and figurative restraint."""

CAT = {
    "id": "metaphor_imagery",
    "label": "Metaphor, imagery, and figurative restraint",
    "moves": {
        "budget": [
            "Allocate figurative language the way you allocate strong sentences: a small number of moments where a comparison does work nothing else can do, and a plain register everywhere else. A chapter with one load-bearing image is stronger than one with eight decorative ones, because the reader spends attention on an image and expects a return on it.",
            "Cut comparisons that exist to impress. If a metaphor cannot be justified by what it compresses, clarifies, or reveals about the perceiver, it is ornament, and ornament in a scene that is already working reads as interference rather than richness.",
        ],
        "pov_fit": [
            "Draw comparisons from the viewpoint character's world: their work, their history, their habits of thought, their fears. A comparison sourced from outside the perceiver's experience reads as the author's, and it damages the illusion of a mind even when the image itself is good.",
            "Let expertise supply the figurative register. A sailor, a farmer, a nurse, and an engineer will reach for different material when they need to compare, and using their vocabulary keeps the imagery both specific and characterizing.",
        ],
        "concrete_first": [
            "Place the physical fact before the comparison. A comparison that extends a concrete detail deepens the reader's grip on something already present; a comparison that replaces the detail substitutes an abstraction for a thing and leaves the scene unmoored.",
            "Let the literal be the strongest option where it is available. Restraint sometimes means refusing the metaphor entirely, and that refusal protects the comparisons the chapter genuinely needs.",
        ],
        "consistency": [
            "Keep the figurative vocabulary stable across the book. If one chapter thinks in terms of water and the next in terms of clockwork, the shift registers as a change of author unless it is a deliberate characterization signal, and it is usually drift.",
            "Refuse chains. A comparison that spawns three extensions of itself is no longer clarifying anything: the reader tracks the image rather than the scene, and the passage becomes about the writing.",
        ],
        "symbol_discipline": [
            "Do not force symbolism onto objects. An object that carries meaning through its involvement in the story needs no interpretive help, and the interpretive help converts a working detail into a device the reader resents.",
            "Let important objects exist without reminder. Repeatedly describing a meaningful thing as meaningful is the most common way an effective symbol is ruined, and the repair is simply to stop mentioning its significance.",
        ],
    },
    "problems": [
        {
            "id": "imagery_budget",
            "frames": [
                "Your chapter is producing more figurative language than the scene can support.",
                "You want a single image to carry a scene's emotional weight rather than a sequence of them.",
                "You are drafting a description that keeps reaching for comparisons.",
            ],
            "context": "Figurative language is a scarce resource; spending it widely leaves nothing available for the moment that needs it.",
            "stages": ["the scene's central description", "the emotional peak", "the chapter's final passage"],
            "openers": [
                "Decide before drafting which single moment in the chapter deserves a comparison and why: what it compresses, what it reveals about the perceiver, or what it makes available that plain description cannot. Then write the rest without comparisons, and the chosen one will operate at full strength.",
                "Treat imagery as a cost against the reader's attention and spend it where the return is highest. Most descriptions become stronger when a literal observed detail replaces the comparison entirely.",
            ],
            "closers": [
                "Write the chapter with one deliberate image, placed where the scene needs compression or revelation, and keep the surrounding prose literal and exact. The image will carry further for being alone.",
                "Choose the moment, build the comparison out of the perceiver's world, and draft everything else without figurative language.",
            ],
        },
        {
            "id": "generic_imagery",
            "frames": [
                "Your comparisons are arriving from a common stock rather than from the character's experience.",
                "You notice your imagery describes atmosphere rather than perception.",
                "You are drafting a frightening or tense passage and the imagery is conventional.",
            ],
            "context": "Inherited imagery is the default at drafting speed and must be replaced with something drawn from the perceiver and the situation.",
            "stages": ["the tense sequence", "the description of a threat", "the moment of dread"],
            "openers": [
                "Before drafting, decide what this character's fear or tension actually is and what material they would reach for to describe it. A threat imagined by a person with a specific history looks different from a general one, and the difference is where a scene becomes particular rather than atmospheric.",
                "Refuse the conventional material for atmosphere when a scene is tense. Familiar comparisons arrive first because they are broadly applicable, which is exactly why they convey nothing about this person, place, or pressure.",
            ],
            "closers": [
                "Replace the generic material with comparisons sourced from the character and the physical situation, and where nothing specific is available, use literal description instead. The passage will read as observed rather than assembled.",
                "Draft the tense sequence with concrete physical detail and reserve figurative language for the moment where it will be unmistakably this character's.",
            ],
        },
        {
            "id": "symbolic_overreach",
            "frames": [
                "You want an object in your story to carry thematic weight and the writing keeps pointing at it.",
                "You are drafting a passage that explains what a recurring image means.",
                "A scene's symbolism is being reinforced rather than allowed to operate.",
            ],
            "context": "Meaning in objects is produced by involvement and consequence rather than by narration; explanatory reinforcement removes exactly the effect it seeks.",
            "stages": ["the return of a recurring object", "the chapter that resolves an image", "the scene where the symbol matters most"],
            "openers": [
                "Decide what the object does in the plot and let its significance be a byproduct. An object that is used, lost, repaired, or given away acquires meaning through those events, and the meaning is stronger when the narration never confirms it.",
                "Where an image needs to return, change its state rather than restating its meaning. A second appearance should add information about the object's history or the character's relationship to it rather than repeat the note the first appearance sounded.",
            ],
            "closers": [
                "Write the return of the object as an event with consequences and leave the interpretation alone. The reader will assemble the meaning and keep it, because it will be theirs.",
                "Keep the symbolic material in the action and out of the commentary, and end the passage on the object's new state rather than on its significance.",
            ],
        },
    ],
    "traps": [
        {
            "id": "metaphor_per_paragraph",
            "frames": [
                "Your description has settled into a rhythm of one comparison per paragraph.",
                "You are drafting and each new object is arriving with a figurative gloss.",
                "You want the prose to feel textured and the comparisons are doing the work.",
            ],
            "slide": "The comparisons multiply, one per paragraph, each individually defensible. The pull is strong because figurative language reads as richness and because drafting speed rewards it, and by the middle of the book the reader has stopped registering any of them.",
            "stages": ["the descriptive passages", "the chapter's opening", "the aftermath sequence"],
            "openers": [
                "You can feel the comparison arriving with every new description, and each one is easier than the last. Refuse the rhythm in the drafting: keep the literal detail and let the imagery appear only where the scene is compressing something.",
                "The pull here is decorative density. Reason past it now, because imagery used at a constant rate has a constant price and no variable return.",
            ],
            "damage": "Constant figurative language consumes attention without producing emphasis, so the passages that genuinely need an image have nothing available. It also makes the prose rather than the scene the object of the reader's attention, and it erases the distinction between passages that matter and passages that do not.",
            "reason_past": "Reason past it by deciding per scene whether it needs imagery at all and, where it does, identifying the single moment. Write the rest literally, and check the drafted passage for comparisons that appeared without a decision behind them.",
            "closers": [
                "Keep the literal description and let the images be rare, chosen, and load-bearing. The reader will notice every one of them.",
                "Draft the passage with physical detail and admit a comparison only where it compresses something the literal cannot.",
            ],
        },
        {
            "id": "image_chain",
            "frames": [
                "A single comparison in your draft has grown extensions.",
                "You are elaborating an image across several sentences.",
                "You want the imagery to build and the passage is becoming about the image.",
            ],
            "slide": "The image is extended: first the initial comparison, then its implications, then a second comparison built on the first. It feels like development and it is the moment the passage stops being about the scene, because the reader is now tracking an internal structure rather than a situation.",
            "stages": ["the descriptive passage", "the emotional peak", "the chapter's concluding image"],
            "openers": [
                "You can feel the image asking to be extended. Refuse the extension while drafting: one comparison, held briefly, and then back to the concrete so that the reader's attention returns to the scene rather than remaining inside the figure.",
                "The pull is toward elaboration, and it is easy to mistake for depth. Notice it and cut to the single comparison, keeping whatever concrete detail the extension was carrying.",
            ],
            "damage": "Chained imagery displaces the scene and slows the pace at the exact moments the pace should be under the writer's control. It also produces a self-referential prose surface, which reads as an author performing rather than narrating, and it consumes attention the reader needs for events.",
            "reason_past": "Reason past it by treating each comparison as one sentence's work and returning immediately to physical specifics. Where the extension carries new information, convert it into a fact about the world or the character rather than into more figure.",
            "closers": [
                "Write one comparison and return to the concrete in the next sentence. The image stays available and the scene keeps its footing.",
                "Cut the extensions and keep whatever they were carrying as literal detail.",
            ],
        },
        {
            "id": "symbolic_underlining",
            "frames": [
                "A recurring object in your book keeps being described in terms of what it means.",
                "You are writing the chapter where a symbol is revealed as significant.",
                "The narration is confirming an interpretation the reader has already formed.",
            ],
            "slide": "The object is repeatedly framed: it is noticed because it matters, described with weight, and connected to the story's larger questions. It feels like thematic integration and it converts the object into an assignment the reader has to complete.",
            "stages": ["the object's return", "the chapter that resolves a thread", "the final act"],
            "openers": [
                "You can feel the passage pointing at the object's meaning. Refuse it while drafting and give the object a job instead: something it does, something it costs, something its presence prevents.",
                "The pull is toward confirming the reader's interpretation. Reason past it now: confirmation removes the reader's ownership of the meaning, which is the only kind that lasts, and it converts a working object into a lesson.",
            ],
            "damage": "Underlined symbolism kills the effect it seeks and signals that the book does not trust its own construction, which makes every other recurrence suspect. It also damages the object as a plot element, because things that exist to mean something stop doing anything.",
            "reason_past": "Reason past it by writing the object's appearances as events: it is used, it breaks, it is given away, it goes missing. Where meaning needs to surface, let a character's behavior toward the object carry it.",
            "closers": [
                "Give the object consequences and let the meaning be a residue. Write its appearances as plot and trust the reader's assembly.",
                "Keep the interpretation out of the narration and let the object's history do the work.",
            ],
        },
    ],
    "discipline": [
        "Before drafting, identify the single moment in the chapter where a comparison earns its place, and note what it compresses or reveals. Then write the chapter's remaining description literally.",
        "During the draft, keep comparisons inside the perceiver's experience: their work, their history, their fears, and their habits of attention.",
        "After the chapter, list the figurative language that survived. Where two images do the same work, keep the stronger and delete the other; where an image is decorative, replace it with the physical detail it was standing in for.",
    ],
    "themes": [
        {
            "id": "imagery_across_book",
            "frames": [
                "You are planning how a long book's imagery will accumulate rather than repeat.",
                "You want the novel's figurative language to develop without becoming a signature.",
                "You are deciding how recurring images will operate over an entire arc.",
            ],
            "question": "How should imagery develop across a whole book so that recurrence produces meaning rather than repetition?",
            "openers": [
                "Plan the imagery as a system with a small vocabulary: a few families of comparison that belong to particular characters, places, or pressures. Recurrence inside a family generates meaning by accumulation, while a new family appearing late reads as a change of author, so the design work is deciding what the book will think in.",
                "Give each major character a figurative register drawn from their life. Then a scene's imagery signals whose perception the reader is inside without any announcement, and the same scene revisited by another character becomes a different passage rather than the same passage described again.",
            ],
            "middles": [
                "Change the state of an image rather than its content on each return: an object repaired, a landscape flooded, a comparison that used to comfort and now threatens. Accumulation comes from alteration, and repetition without alteration is what makes a recurring image feel mechanical.",
                "Quarantine the book's most charged images so that they are not spent early. An image used in three chapters cannot crown the ending, and the discipline is recognizing which comparisons the book is saving.",
                "Let the figurative register shift at structural boundaries only: a new act, a new location, a change of viewpoint. Shifts inside a scene read as inconsistency, while shifts aligned with structure read as design.",
            ],
            "closers": [
                "Commit to a small imagery system: a handful of families of comparison, assigned to characters and places, altered rather than repeated on each return, and held for the moments that need them most. Write toward a book whose images accumulate.",
            ],
        },
    ],
    "principles": [
        "Fewer and stronger: allocate figurative language deliberately and let the remaining description be literal and exact.",
        "Perceiver before image: comparisons belong to the mind that produces them, not to the author who knows what the scene means.",
        "Concrete before figurative: the physical detail comes first, and the comparison extends what the reader already holds.",
    ],
}
