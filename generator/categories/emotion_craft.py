"""Emotion: individual reaction, timing, contradiction, and consequence."""

CAT = {
    "id": "emotion_craft",
    "label": "Emotional craft and individual reaction",
    "moves": {
        "individual_reaction": [
            "Decide the character's reaction before deciding the beat's intensity. Reaction is characterization rather than a shared constant: one person gets practical, one gets quiet and orderly, one laughs at the wrong moment, one becomes curious, one focuses on a trivial task. Choose the response that belongs to this person under these conditions and let the situation's size be visible through how badly the response fits it.",
            "Give each character a pressure signature that holds across the book: what they do with their hands, how their speech changes, what they avoid, what they attend to. Recurring signatures are what let a reader recognize an emotional state in a character without being told, and their slow alteration across acts is one of the cleanest ways a long story shows change.",
        ],
        "timing": [
            "Treat emotional timing as a variable rather than an instant. Reactions can be delayed by the demands of the moment, suppressed by training or duty, displaced onto something small, or held until the character is alone. Almost never should a feeling be delivered at full strength immediately and completely, because the available version of an emotional beat is also the least interesting one.",
            "Let consequences arrive after the emotion rather than with it. A character can absorb an event in the scene and pay for it two chapters later, and the delay makes the feeling structural rather than momentary. Decide how long the pressure is stored and what will release it, and the emotion becomes part of the plot's machinery.",
        ],
        "mixed_and_opaque": [
            "Permit contradictory feelings to coexist, and permit the character to misread themselves. Relief and resentment can occupy the same moment, and a person's own account of their state is not authoritative: they will call fear preparation, grief logistics, and anger disappointment, and the pattern of mislabeling is a characterization resource.",
            "Keep the character's understanding of their own feelings partial across the book. A person who explains themselves accurately and completely has stopped being a person in a situation and become a narrator with a psychology, and the reader's inference is worth more than the character's summary.",
        ],
        "gradient": [
            "Do not resolve an emotion as soon as it is introduced. Emotional states change gradually and leave residue, and the chapter that closes an emotional movement completely must still let it alter behavior, decisions, and relationships in later chapters, or the reader learns that feelings in this book do not persist.",
            "Keep amplitude uneven across the book. If every chapter peaks, the reader's calibration flattens and later events cannot exceed earlier ones. Decide where each chapter's emotional ceiling sits, and let most chapters stay below the book's maximum.",
        ],
    },
    "problems": [
        {
            "id": "reaction_specificity",
            "frames": [
                "A scene delivers a strong event and every character in it is reacting the same way.",
                "You are drafting a moment of shock and the writing is producing generic responses.",
                "You want the reader to learn something about a character from how they receive bad news.",
            ],
            "context": "Emotional reaction is a characterization surface; the same event should produce visibly different behavior from different people.",
            "stages": ["the reveal", "the aftermath scene", "the moment the news arrives"],
            "openers": [
                "Before drafting, decide each present character's reaction as a behavior rather than a feeling, and make sure they are not interchangeable. The person who becomes practical, the one who asks a tangential question, the one who starts cleaning, and the one who goes extremely polite are four pieces of information about four people, and the scene gains characterization at no cost to its event.",
                "Choose reactions by history rather than by intensity. What a character does with shock depends on what they have survived and how they have been trained to behave, so the scene's reaction design is a chance to display the past without narrating it.",
            ],
            "closers": [
                "Write the moment with distinct behavioral responses for each person present, and let the event be the only thing they share. Nothing in the scene should state how anyone feels.",
                "Draft the reactions as actions with physical specifics, and stop before any of them is named.",
            ],
        },
        {
            "id": "bad_timing",
            "frames": [
                "An emotional beat in your chapter resolves too quickly to be believed.",
                "Your characters recover from major events within a page.",
                "You are drafting a scene where the plot needs to continue immediately after something devastating.",
            ],
            "context": "Emotional states must be delayed, stored, or displaced; immediate resolution destroys both the character's credibility and the plot's sense of consequence.",
            "stages": ["the chapter after a catastrophe", "the scene following a loss", "the transition between acts"],
            "openers": [
                "Decide where the feeling goes rather than when it ends. It can be postponed by obligation, converted into efficiency, hidden behind a practical problem, or saved for a character who is not present. Every one of those options lets the plot continue while keeping the emotion alive, and the release, when it comes, will be an event rather than a summary.",
                "Give the character a task to do in the scene where the emotion is unaffordable. Work is the most natural container for stored feeling, and what a person chooses to do immediately after a catastrophe is itself characterizing.",
            ],
            "closers": [
                "Carry the feeling forward as behavior and pressure, and write the scene's surface as competence, procedure, or displacement. Let the release be scheduled rather than immediate.",
                "Keep the emotion stored and let the chapter's action run without resolution, so the reader can feel the pressure accumulating under the character's ordinary behavior.",
            ],
        },
        {
            "id": "emotional_consequence_chain",
            "frames": [
                "A character's emotional state in an earlier chapter has no effect on later events.",
                "You are planning how the story's emotional arc connects to its plot.",
                "You want an argument or a loss to remain consequential across several chapters.",
            ],
            "context": "Emotions become structure when they alter later decisions, relationships, and capabilities rather than belonging to the chapter that produced them.",
            "stages": ["the planning of the middle act", "the chapter following a rupture", "the approach to the final act"],
            "openers": [
                "For each significant emotional event, decide what it changes downstream: a decision the character can no longer make, a person they now cannot ask, a risk they are now willing to take, a task they now do badly. Write the immediate chapter with that downstream change in mind, even if the change appears three chapters later.",
                "Treat emotional debt as a ledger. What is owed, to whom, after a rupture, and what does the character do when the debt comes due? Planning the payment keeps the emotion structural and ensures that the book's feeling accumulates rather than resetting at each scene boundary.",
            ],
            "closers": [
                "Note the downstream change for each emotional event and write the current chapter so that the change is already visible in behavior. The feeling is then part of the plot rather than adjacent to it.",
                "Let the emotion live in what the character now cannot do, and write the scene so that impossibility is present on the page.",
            ],
        },
    ],
    "traps": [
        {
            "id": "formulaic_emotion",
            "frames": [
                "Your emotional beats are being delivered by the same physical shorthand every time.",
                "You notice adrenaline, tears, and trembling doing all the emotional work in a chapter.",
                "You are drafting a scene that needs to feel intense and the prose is reaching for standard reactions.",
            ],
            "slide": "The responses arrive pre-assembled: trembling hands, a racing heart, a breath that catches, eyes that sting. Each one is true of someone, which is why the reflex feels legitimate, and collectively they make the entire cast respond identically to everything.",
            "stages": ["the confrontation", "the bad news", "the moment of fear"],
            "openers": [
                "You can feel the standard reactions queuing up for the moment. Refuse them while drafting and choose the response this character would actually produce, including the unimpressive ones: irritation, hunger, a sudden interest in the room's arrangement, an inappropriate joke, a refusal to sit down.",
                "The pull is toward the universal physical response, and its cost is the cast's individuality. Reason past it now and decide what this person does instead, then let the situation's severity show in how inadequate the response is.",
            ],
            "damage": "Formulaic emotional reactions erase characterization at the moments a reader is most attentive, and they also flatten the book's emotional range: if every character responds with the same physiology, the reader cannot distinguish grief from fear from relief, and the more intense passages start to read as interchangeable.",
            "reason_past": "Reason past it by deciding behavior first and internal sensation last, and by giving every character a recurring signature that shows up under pressure. Where the physical response is genuinely the story's subject, make it specific in kind and consequence rather than generic in sensation.",
            "closers": [
                "Write the beat with an individual reaction and a physical cost in the scene, and leave the standard shorthand out entirely. The severity will be legible in what the response fails to cover.",
                "Choose this character's pressure signature and draft the moment through it, refusing the general physiology that would fit anyone.",
            ],
        },
        {
            "id": "underwriting_then_overwriting",
            "frames": [
                "You are moving too quickly past an event that should wound a character.",
                "Your plot's next movement requires the aftermath to be short and you are tempted to skip it.",
                "You notice your chapters resume a neutral emotional baseline after major losses.",
            ],
            "slide": "The pull is toward resuming: the event has happened, the plot needs to continue, and the next scene opens with everyone functional. It feels like professional pacing while drafting, and it means the book's largest moments leave no trace.",
            "stages": ["the chapter after the climax", "the transition between acts", "the scene following a betrayal"],
            "openers": [
                "You can feel the draft wanting to move on, and the movement is tempting because the plot is interesting. Hold the aftermath instead, in compressed form: a scene of consequence that shows what is now impossible rather than restating what happened.",
                "The pull is toward a clean slate. Reason past it now and identify the one thing that cannot be undone by the event, then build the next chapter around that impossibility rather than around the next plot step.",
            ],
            "damage": "Skipped aftermath teaches the reader that the book's stakes are theatrical. Investment is built by consequence, so a manuscript full of catastrophes that leave no residue reads as event-driven spectacle, and the ending will arrive without the accumulated weight that makes an ending mean anything.",
            "reason_past": "Reason past it by planning aftermath as compressed scenes with concrete costs: an altered relationship, a lost capability, a promise no longer possible. The plot can proceed quickly through them, but it must pass through them.",
            "closers": [
                "Write the aftermath as a short scene of impossibility and altered behavior, then continue. The pace can stay fast; the consequence cannot be skipped.",
                "Build the next chapter around what the event destroyed rather than around what it enabled, and let the plot move through that.",
            ],
        },
        {
            "id": "explaining_the_feeling",
            "frames": [
                "Your character's interior commentary keeps analyzing their own emotional state.",
                "You are drafting a scene and the character's understanding of their feelings is complete and precise.",
                "You want the reader to understand the emotional stakes clearly.",
            ],
            "slide": "The interiority becomes clinical: the character names their condition, identifies its cause, and evaluates its reasonableness. It reads as psychological depth while drafting and it removes the reader's participation, which is where emotional engagement actually happens.",
            "stages": ["the reflective passage", "the moment after a decision", "the chapter's closing movement"],
            "openers": [
                "You can feel the character becoming their own therapist, and the accuracy is the problem. Refuse the analysis while drafting and let the behavior, the misreading, and the physical setting carry the state. Where a statement is genuinely needed, make it wrong in an informative way.",
                "The pull is toward self-knowledge so the reader is not confused. Reason past it now: confusion about one's own condition is realistic and generative, and clarity is often available only much later, if at all.",
            ],
            "damage": "Characters who explain their feelings accurately become narrators rather than people, and the reader stops having to infer, which means the emotional events lose their capacity to land. It also consumes the space where behavior and circumstance would have done the work more powerfully.",
            "reason_past": "Reason past it by converting the analysis into action and misinterpretation: the character does something because of the feeling and names it wrongly, or names it correctly but too late, after the decision it should have informed.",
            "closers": [
                "Write the passage so the character's account of their own state is partial, late, or mistaken, and let their behavior carry what they cannot describe.",
                "Replace the analysis with a decision made under the influence of the feeling, and let the reader name it.",
            ],
        },
    ],
    "discipline": [
        "Before drafting an emotional sequence, write down each character's reaction as behavior, the timing of its expression, and the downstream change it will cause.",
        "During the draft, keep the emotional vocabulary out and let behavior, attention, and physical circumstance carry the state; where a feeling must be named, place the word late and make it more specific than the general emotion.",
        "After the chapter, check the emotional ledger: what was stored, what was displaced, what was released, and what consequence carried forward into the next chapter.",
    ],
    "themes": [
        {
            "id": "emotional_architecture",
            "frames": [
                "You are planning how a novel's emotional movement will be structured across its acts.",
                "You want the book's feeling to accumulate rather than reset at every chapter boundary.",
                "You are deciding how character change will be visible without being announced.",
            ],
            "question": "How is an emotional arc built as structure across a whole book rather than as intensity inside individual scenes?",
            "openers": [
                "Plan emotional movement as a ledger rather than a mood: what each act takes from each major character, what it leaves them able to do, and what remains owed at the end. Character change becomes visible in capability and willingness rather than in stated feeling, and the reader reads the arc by noticing what a person will now do that they would not have done before.",
                "Decide the book's emotional amplitude curve alongside its plot curve. The two are not the same: a plot can escalate while emotional intensity falls, and a quiet chapter can carry the largest interior movement in a book. Scheduling both curves deliberately is what prevents the middle from either sagging or shouting.",
            ],
            "middles": [
                "Assign each major character a pressure signature and plan how it alters across acts. The signature is the reader's instrument for recognizing a state, so its modification is the clearest available signal of development, and its stubborn persistence can be equally eloquent.",
                "Plan the storage and release points for important feelings: which chapter suppresses, which displaces, and which finally pays. A book with a well-scheduled release schedule feels cumulative, while one that releases immediately every time feels episodic regardless of its events.",
                "Keep consequence reciprocal between characters. If one person's action wounds another, the wound should modify what the second person will risk for the first later, and that modification is the emotional content of the middle act.",
                "Protect the low registers. The book needs passages where nothing is emotionally loaded, because contrast is the only way an emotional peak is legible, and quiet chapters are where the reader's attachment to the cast is actually built.",
            ],
            "closers": [
                "Commit to an emotional ledger and an amplitude curve for the whole book: signatures, storage and release points, reciprocal consequence, and protected low registers. Write each chapter so the reader can see what has changed in what the people are willing to do.",
            ],
        },
    ],
    "principles": [
        "Behavior before explanation: emotional states are carried by what a person does, avoids, and attends to, not by what the narration names.",
        "Individual before universal: every reaction is a characterization decision, and the standard physical shorthand is the least informative option available.",
        "Consequence before closure: a feeling that produces no later change has not been dramatized, only described.",
    ],
}
