"""Concrete before abstract: physical grounding, behavior over labels."""

CAT = {
    "id": "concrete_grounding",
    "label": "Concrete grounding and behavior before explanation",
    "moves": {
        "enact_state": [
            "Convert every state you intend the reader to feel into particulars before you draft the scene. A room that should read as unsafe needs the specific things the character keeps checking, the ordinary object out of place, the sound that stopped; a person who should read as furious needs the hands, the voice, the subject they keep returning to. Decide these particulars as planning, because they are the scene's emotional equipment and they cannot be improvised convincingly in the middle of drafting.",
            "Treat behavior as the primary carrier of interior state and explanation as a fallback. What a character does with their attention, their posture, their property, and their next decision carries more information than any label applied to them, and it carries it without removing the reader's share of the inference.",
        ],
        "physical_ceiling": [
            "Raise the physical grounding when the scene's intensity rises. Under emotional or conceptual pressure the writing tends to float: the room disappears, the body disappears, and the scene becomes a debate about meanings. Keep the character in contact with the world, with weight, temperature, texture, obstruction, and effort, and the intensity will have something to press against.",
            "Keep the body's ordinary business present during important moments. What the hands are doing, where the feet are planted, what is underfoot, what the character is carrying, and what they can hear in the background are all available, and they do the work that adjectives cannot: they make the scene inhabitable.",
        ],
        "specific_over_generic": [
            "Choose the incidental specific over the atmospheric generalization. Generic atmosphere is interchangeable between scenes and therefore carries no information, while an incidental particular, selected with the character's situation in mind, implies place, class, history, and mood at the same time and does it without announcing anything.",
            "Prefer one precise image to three approximate ones. Description accumulates cheaply while drafting, because each additional clause seems to add richness, but the reader retains the strongest detail and the rest becomes noise around it, which means stacking has a negative return.",
        ],
        "concrete_before_abstract": [
            "Order the writing so that the concrete arrives before the interpretive. Give the reader the physical fact, the sound, the object, the gesture, and let meaning be assembled; an abstraction placed first becomes a frame that the details then have to satisfy, which turns observation into illustration.",
            "Let the concrete detail do the interpretive work you would otherwise state. A character counting exits, straightening objects, or cleaning a table that is already clean communicates a condition more precisely than naming that condition, and it also characterizes the person doing it.",
        ],
        "grounded_registers": [
            "Choose the sensory register according to the scene's work rather than by habit. A negotiation runs on sight and language, a physical sequence runs on touch and weight, a waiting period runs on hearing and small movements. Deciding the dominant register in advance prevents the uniform five-sense inventory that makes description feel like a checklist.",
            "Use the character's expertise as a description engine. A mechanic sees the state of a machine, a cook sees the state of a kitchen, a nurse sees the state of a person, and each of them sees those things first. Expertise converts description into perception and removes the need for a narrating observer.",
        ],
    },
    "problems": [
        {
            "id": "emotion_needs_body",
            "frames": [
                "A scene requires the reader to feel a character's emotional state without the narration announcing it.",
                "You are drafting a moment of strong feeling and the page keeps producing labels instead of particulars.",
                "Your character's reaction matters more than the event that caused it, and the reaction has not been built yet.",
            ],
            "context": "Emotional states must be built from behavior, attention, and physical circumstance; the label is the last resort and usually the weakest option.",
            "stages": ["the emotional turn in the scene", "the aftermath of an event", "the character's first reaction"],
            "openers": [
                "Before drafting the moment, decide the behavioral signature for this character in this condition. Emotional reaction is characterization, not a shared human constant: one person goes quiet and tidy, another talks faster, another becomes practical, another focuses on an irrelevant object. Choose the signature that belongs to the person and the conditions, then build the scene so the signature has room to operate.",
                "Decide what the character does before you decide what they feel. The action selected under pressure reveals the state more precisely than any statement of it, and the action also moves the scene, which a reported emotion does not. Choose the action, give it a physical cost, and let the reader arrive at the feeling.",
            ],
            "closers": [
                "Write the moment as behavior, attention, and physical circumstance, and stop before naming the state. If a single naming word survives, keep it late, precise, and partial, and let the body's evidence stand beside it rather than underneath it.",
                "Commit to the behavioral signature and to the physical specifics that carry it, and draft the scene without any emotional vocabulary. The reader's inference is the scene's payload.",
            ],
        },
        {
            "id": "intense_scene_grounding",
            "frames": [
                "Your scene's stakes are high and the writing keeps drifting into abstraction.",
                "A confrontation or revelation needs to stay physically located rather than becoming a debate.",
                "The chapter's emotional peak is approaching and the room has disappeared from the page.",
            ],
            "context": "Intensity needs physical anchoring: the higher the emotional or conceptual pressure, the more the scene needs weight, place, and effort.",
            "stages": ["the scene's peak", "the confrontation itself", "the chapter's final sequence"],
            "openers": [
                "Plan the physical spine of the intense scene before drafting it: where each person is, what they are doing with their hands, what is between them, what has to be moved, opened, carried, or signed. A scene with a physical spine can carry abstract stakes without floating, because every abstraction has something solid to sit on.",
                "When the pressure rises, add weight rather than commentary. The character's body should be engaged with the room at the exact moment the stakes peak, and the engagement should cost something, which is how intensity becomes legible rather than asserted.",
            ],
            "closers": [
                "Draft the sequence with the physical spine intact and let the abstractions arrive as brief interruptions rather than as the scene's mode. Grounding first, meaning second, and the peak will land on something.",
                "Keep the room, the body, and the cost present through the moment, and refuse the drift into summary. Write the scene so a reader could reconstruct where everyone stood.",
            ],
        },
        {
            "id": "character_specific_description",
            "frames": [
                "You are describing a place that several characters will visit across the book, and each visit should differ.",
                "Your scene's setting is established and the description is starting to feel generic.",
                "You need the description to characterize the observer rather than the location.",
            ],
            "context": "Description is a record of attention; making it character-specific converts scenery into characterization.",
            "stages": ["the arrival in a new location", "the scene's establishing passage", "a return to a familiar place"],
            "openers": [
                "Decide the character's practical relationship to the space before you decide what it contains. Someone who works there sees tools and hazards; someone who is being interviewed sees exits and the other person's hands; someone who used to live there sees changes and absences. The relationship selects the details, and the details then characterize the relationship.",
                "Convert the scene's atmosphere into an inventory of what this character notices and what they would never notice. Atmosphere as a stated quality is authorial; atmosphere as an unstated consequence of selective attention is craft.",
            ],
            "closers": [
                "Write the description through the observer's purpose and expertise, and let the place emerge from what is used, avoided, and ignored. The reader will build the location from the character's partial map, which is how places become memorable.",
                "Choose the register according to who is looking and why, and draft only what that attention would supply. The scene will read as inhabited rather than described.",
            ],
        },
        {
            "id": "abstract_stretch_repair",
            "frames": [
                "A chapter of your book has become a long stretch of abstract discussion and has stopped being a scene.",
                "You are writing the reflective movement of the story and the material has lost its physical anchor.",
                "Your middle chapters are doing their work in commentary rather than in incident.",
            ],
            "context": "Abstract stretches must be short movements inside a scene rather than the scene's mode, or the reader's experience becomes argument rather than story.",
            "stages": ["the reflective chapter", "the middle section", "the sequence after a major turn"],
            "openers": [
                "Before drafting a reflective movement, decide what it is doing and cap it. Reflection earns its place when it changes a decision, and the change should arrive within a page or two; longer abstract passages should be redistributed into action, behavior, and dialogue, where the same material can be carried without stopping the story.",
                "Give the abstract passage a physical frame and a limit. Put the thinking inside a task, a journey, an illness, or a wait, and let the task interrupt the thought at fixed intervals; the interruptions keep the scene moving and prevent the reflection from becoming the chapter's substance.",
            ],
            "closers": [
                "Draft the movement as a short burst inside a physical frame, ending on a decision or an interruption. Whatever remains abstract gets redistributed into the scene's behavior and speech.",
                "Keep the abstract material in service of an action the chapter is taking, and stop the passage as soon as the action is served.",
            ],
        },
    ],
    "traps": [
        {
            "id": "labeling_iteration",
            "frames": [
                "You are drafting an emotional beat and the prose keeps producing the name of the emotion.",
                "A scene's tension is being carried by statements about how characters feel.",
                "You want the reader to be certain about a character's state and the page is providing the label to be safe.",
            ],
            "slide": "The pull is toward naming as insurance: the behavior is on the page and the writing adds the emotion word to make sure the reader gets it. It feels precise while drafting and it removes the reader's participation, and after a few chapters the whole book is a report of conditions.",
            "stages": ["the emotional beat", "the aftermath", "the scene's final paragraph"],
            "openers": [
                "You can feel the writing reaching for the label, the word that guarantees the reader understands the moment. The reflex is understandable and it is the single most common way emotional scenes become inert. Reason past it now, at the moment of drafting, and let the behavior carry the weight.",
                "The pull here is reassurance: one more statement of feeling so the beat is unmistakable. Refuse it. Certainty delivered this way costs the reader's inference, and inference is what makes an emotional moment belong to them.",
            ],
            "damage": "The damage compounds across a book. Each label teaches the reader that the narration will explain feelings, which makes behavior redundant and eventually invisible, and it also flattens the specificity of the cast, because named emotions are generic while reactions are individual. By the final act the reader is reading about people rather than inhabiting them.",
            "reason_past": "Reason past it by deciding the behavior before the drafting begins, then refusing to annotate. Where a beat genuinely needs naming for precision, keep one word, place it late, and make it more specific than the general emotion: not fear but the particular fear, named once.",
            "closers": [
                "Carry the beat on behavior, attention, and physical circumstance, and write the scene without emotional vocabulary. Let the reader's certainty arrive from the evidence rather than from a caption.",
                "Build the reaction as action with a physical cost, and draft the passage so that nothing names what it means.",
            ],
        },
        {
            "id": "atmosphere_filler",
            "frames": [
                "Your scene openings are full of atmospheric description that could have been written before the scene existed.",
                "You are drafting an establishing passage and the details feel transferable to any story.",
                "The mood is being manufactured by adjectives rather than produced by particulars.",
            ],
            "slide": "The establishing passages grow: weather, light, sound, and a stated mood, all plausible, all interchangeable between chapters. The pull is strong because atmosphere feels like craft and because a scene with mood seems more finished than one without.",
            "stages": ["the scene's opening", "the transition between locations", "the chapter's first page"],
            "openers": [
                "You can feel the atmospheric opening assembling itself, the mood laid down before anyone wants anything. It is the most available way to start a scene and the least informative. Reason past it: begin with the character's purpose in the space, and let the weather arrive only if it obstructs something.",
                "The pull is toward mood-setting as a courtesy to the reader. Name the habit now and replace it with purpose: what the character came in for, what they find that complicates it, and what they notice because of that complication.",
            ],
            "damage": "Interchangeable atmosphere consumes the budget that specific detail needs, and it teaches the reader to skim openings. Worse, it establishes a mode in which description is scenery rather than pressure, so the book's places never become places where anything can happen, and the reader's sense of location stays thin through the whole story.",
            "reason_past": "Reason past it by giving every scene an immediate practical purpose and letting description emerge from obstruction and use. Where the environment genuinely matters, make it act: block a road, spoil a delivery, change a temperature that someone has to pay for.",
            "closers": [
                "Open inside the character's purpose and let the setting arrive as an obstacle, a tool, or a cost. Weather that changes nothing stays out of the chapter, and the environment becomes a participant rather than a backdrop.",
                "Write the opening as action with a location attached, and reserve environmental description for the moments where the environment is doing work.",
            ],
        },
        {
            "id": "body_inventory",
            "frames": [
                "Your action and emotion passages keep producing the same physical shorthand for feeling.",
                "You notice the same handful of bodily indicators recurring across chapters.",
                "A tense scene is being carried by descriptions of internal physical sensation.",
            ],
            "slide": "The shorthand arrives first and easiest: quickened breath, tightened jaw, racing heart, clenching hands. Each is individually acceptable and collectively mechanical, and the reflex strengthens as the writing speeds up, so the most intense passages end up the most formulaic.",
            "stages": ["the action sequence", "the emotional peak", "the moment of bad news"],
            "openers": [
                "You can feel the shorthand waiting for the tense moment: the note that the heart is fast, the breath is short, the hands are tight. The reflex is available because it is universal, which is also why it tells the reader nothing about this person. Reason past it while drafting and reach for the specific instead.",
                "The pull here is physiological generality. Refuse it now, and choose a reaction that only this character in this situation would have: the wrong laugh, the tidy impulse, the sudden interest in a task, the physical detail that belongs to their trade.",
            ],
            "damage": "Formulaic physical reactions erase characterization at exactly the moments that should individuate a character, and they also inflate the page with sensation while leaving the scene physically unlocated. A book full of racing hearts has no spatial spine; the reader feels a body's internal weather and never learns where anyone is standing.",
            "reason_past": "Reason past it by deciding how this person handles pressure before drafting the scene, expressing that through action in the space, and spending the physical description on the conditions that matter, weight, grip, footing, effort, rather than on internal sensation that every character would share.",
            "closers": [
                "Choose the individual reaction and the physical conditions, and draft the tense sequence as behavior in a located space. The body enters the scene as an actor rather than as a gauge.",
                "Replace the shorthand with a reaction specific to the character and a physical arrangement specific to the room, and write the passage through both.",
            ],
        },
    ],
    "discipline": [
        "Before drafting each scene, decide the concrete particulars that will carry its emotional content: what the character is doing with their hands, what they are looking for, and what in the room is out of place.",
        "During the draft, mark every sentence that states a state rather than enacting it, and convert each one into behavior, attention, or physical circumstance unless the naming is precise enough to keep.",
        "After each chapter, check the split between concrete and abstract material. When the abstract passages have grown longer than the scene's physical spine, redistribute the material into action, and keep the reflection short and consequential.",
    ],
    "themes": [
        {
            "id": "concrete_as_structure",
            "frames": [
                "You are planning how a novel's physical detail will do structural work rather than decorative work.",
                "You want objects, spaces, and bodies to carry the story rather than accompany it.",
                "You are thinking about how a book's texture can also be its architecture.",
            ],
            "question": "How does concrete grounding function as structure across a whole book rather than as local texture?",
            "openers": [
                "Physical detail becomes structure when it is given the same treatment as plot: tracked, spent, and changed. Decide which objects, spaces, and conditions the book will use as instruments, assign them states at the start of each act, and let characters' relationships to them change, so that the reader's sense of the story's movement includes its material conditions.",
                "A book grounded in the physical has an advantage that abstract books do not: its changes are visible. Plan to show the story's movement in the state of a place, the condition of an object, or the limits of a body, and the reader will feel the arc of the plot as a change in the world rather than as a report of one.",
            ],
            "middles": [
                "Give objects histories rather than meanings. An object that has been repaired, borrowed, stolen, lost, and returned carries more story than one whose significance is explained, and the accumulated states become available for later scenes at no cost to the narrative's speed.",
                "Track the body across the book: injuries, exhaustion, illness, physical capacity. A body that remembers the previous act is one of the most reliable ways to make consequence real, and it converts action sequences from set pieces into entries in a ledger.",
                "Let places change in ways the plot did not cause. Weather, decay, renovation, and crowding give the book a world that moves independently, which makes the protagonist's choices feel like interventions rather than like the only motion in the story.",
                "Use the character's expertise as a continuing descriptive resource across the book: the same trade or discipline supplies fresh attention at each stage, and its vocabulary can grow with the character's confidence, which gives the reader an economical signal of development.",
            ],
            "closers": [
                "Commit to a concrete ledger: the objects, spaces, bodies, and skills the book will track, their state at the start of each act, and the changes the reader will see. Write each chapter so that the world's condition is legible, and the story's movement will be visible in the material of the scene.",
            ],
        },
        {
            "id": "behavior_design",
            "frames": [
                "You want a novel's cast to be distinguishable by behavior rather than by description.",
                "You are planning how characters will be recognizable across a long book without relying on summaries of personality.",
                "You are deciding how a story will show change in people who cannot articulate it.",
            ],
            "question": "How does behavior function as characterization across an entire book, and how does it change without breaking recognition?",
            "openers": [
                "Behavior is the most durable characterization instrument because it can be repeated, varied, and broken. Design each major character with a small set of behavioral constants, habits of attention, ways of handling objects, ways of entering a room, ways of responding to disagreement, and then let the plot apply pressure to them, so that the reader learns the person by pattern and then learns the arc by how the pattern changes.",
                "Plan characterization as a set of pressures rather than a set of traits. What a person does under time pressure, under scrutiny, under obligation, and under boredom is four different kinds of information, and the contrast between them is what makes a character feel like a person rather than a type.",
            ],
            "middles": [
                "Decide which behaviors are stable and which are available for change. A person who tidies under stress may keep tidying for the whole book while their treatment of other people changes; the stable habit becomes the reader's recognizable anchor for the shifting material.",
                "Let behavior vary by company. The same character should behave measurably differently with a superior, a sibling, a stranger, and someone they want to impress, and those differences should be visible in what they do rather than reported as a fact about them.",
                "Stage the moments where a character acts against their own pattern, and make them cost something. A single deviation, prepared by circumstances the reader understands, does more for a character's depth than a chapter of explained contradiction.",
                "Keep small behaviors attached to specific people across the book: what they do with their hands, what they check, what they refuse to touch. These are cheap to maintain, and their recurrence is how a reader recognizes a character in a scene without being told who is present.",
            ],
            "closers": [
                "Write the cast from behavioral constants under changing pressure, and let the story's evidence of change be a modification of conduct rather than a statement about personal growth. The reader will know the people by what they do and know the arc by what they stop doing.",
            ],
        },
    ],
    "principles": [
        "Concrete before abstract: give the reader the physical fact before the interpretation, and let the meaning be assembled rather than announced.",
        "Behavior before explanation: what a person does, avoids, and attends to carries their state more exactly than any statement about it.",
        "Specific before generic: an incidental particular from this character's attention outlives any amount of transferred atmosphere.",
    ],
}
