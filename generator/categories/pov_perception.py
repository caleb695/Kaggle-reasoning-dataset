"""POV and character perception."""

CAT = {
    "id": "pov_perception",
    "label": "POV and character perception",
    "moves": {
        "interiority": [
            "Decide whose perceptual position the chapter runs through before you decide what happens in it. The stance is not decoration: it selects which facts can arrive, in what order, and with what emotional charge. Establish the position concretely, where the character is standing, what they are doing with their hands, what they are listening for, and what they currently expect, and the scene will filter itself as it drafts.",
            "Write from inside the character rather than from a place above them. The vantage above the scene knows the shape of the whole situation and reports it evenly; the vantage inside knows only what has arrived, and it notices according to what it cares about. When you catch the narration describing something because it is important to the story rather than because it is available to the perceiver, cut it or route it through a sense.",
            "Keep the perceptual budget limited to what the viewpoint can reasonably notice, infer, or misread. Unlimited knowledge is the single most common way a scene loses its interiority, and it is also a plotting error, because a character who understands everything the author understands has no need to decide anything.",
        ],
        "attention_filter": [
            "Rank the available details by the character's priorities before you choose which ones reach the page. A frightened person notices exits, distances, and what could be used; a curious person notices anomalies; a competitive person notices relative strength and standing; a tired person notices what the body is doing. Pick the filter for this chapter and let it choose the description.",
            "Let the personality shape interpretation as well as attention. Two characters can perceive the same event and hold different facts about it, not because the event differs but because each has a habitual way of reading intent, risk, and blame. Decide the habit, then let it decide what the scene's evidence means.",
            "Give the character something to want in the scene before you describe anything. Attention organized by a goal produces specific, purposeful detail, while attention without a goal produces inventory, and inventory is where description goes to die.",
        ],
        "limited_knowledge": [
            "Respect limited knowledge as a structural rule, not a flourish. Characters should act on what they have been told, seen, or inferred, and any scene that requires them to know more is a problem to solve in the plot rather than in the prose. Track who knows what at the start of the chapter and update it at the end.",
            "Allow characters to misunderstand and to build incorrect assumptions on top of partial information. A misunderstanding that persists across several chapters becomes a source of pressure, an engine for decisions, and a route to a later turn; a misunderstanding corrected immediately is only a speed bump.",
            "Do not immediately correct a character's misreading for the reader's benefit. The correction is often the least interesting part of the material, and the reader's awareness of the gap is one of the reliable pleasures of close narration. Let the wrong assumption stand and let its consequences arrive on their own schedule.",
        ],
        "interpretation": [
            "Filter every external fact through the character's worldview as you draft. The same corridor is different to a person who expects violence than to one who expects an inspection, and the difference should live in what gets noticed, what gets dismissed, and what gets explained away, not in a label applied to the corridor.",
            "Preserve the character's worldview across the whole book rather than resetting it each chapter. A suspicious person remains suspicious in the next chapter, though the suspicion may shift targets; a hopeful person finds reasons, and the reasons should be consistent in kind even when they are wrong.",
            "Let the character's own state color the material without commentary. A person who has just been humiliated will read the next room differently, and the reading can do the work of a paragraph of emotional reporting if you allow it to select what is seen.",
        ],
        "interior_texture": [
            "Keep interior thought short, partial, and interruptible, the way thought behaves when a person is also doing something. Long reflective passages belong in the planning stage; on the page, the character's mind should be broken by the work of the scene, and the breaks are where the reader feels a person thinking rather than a narrative explaining.",
            "Allow mundane and irrelevant material into the character's mind during important moments. A person facing an emergency still notices a bill due, a rude remark from yesterday, the state of their shoes. These details coexist with the catastrophe and are the most efficient available proof that a life is being interrupted rather than a plot advanced.",
            "Give the character a private register that is not the book's public register: a habit of understatement, an internal joke, a returning grievance, a way of describing people by their function. This private register is what makes interiority specific rather than generic reflective narration.",
        ],
    },
    "problems": [
        {
            "id": "whose_head",
            "frames": [
                "You are writing a chapter that has to carry two characters' competing stakes, and the choice of viewpoint is still open.",
                "Your scene involves several people whose interests diverge, and you must decide whose perception the chapter runs through.",
                "You are about to draft a chapter where the outcome depends on what a particular person fails to notice.",
            ],
            "context": "The viewpoint decision comes before staging: it determines which facts are available to the reader, which remain invisible, and where the scene's tension actually sits.",
            "stages": ["the chapter's opening", "the planning of the scene", "the decision before drafting"],
            "openers": [
                "Choose the viewpoint by asking whose ignorance is the most useful. A scene filtered through a character who does not understand what is happening produces tension that no amount of staging can create, while a scene filtered through the person who understands everything becomes an explanation with dialogue. Before drafting, name the fact the viewpoint must not have, and the second fact they must misinterpret, and the chapter's shape will follow.",
                "The viewpoint belongs to whoever pays the most for the scene's information. If a character's decision at the end of the chapter turns on something they learn inside it, the learning should be the chapter's spine, and it should arrive late and incompletely. Decide what the perceiver wants, what they are prepared to believe, and which detail their attention will skip, then write the scene as their experience rather than as a record of events.",
            ],
            "closers": [
                "Commit to one perceiving position for the chapter and hold it: one set of sensory priorities, one set of assumptions, one order in which facts become available. The reader will assemble the larger picture from the gap between what is happening and what the viewpoint understands, so write toward that gap deliberately.",
                "Fix the viewpoint's limits before drafting and treat them as instruments: what this character cannot see, what they will misread, and what their body is busy doing while they misread it. Then write the chapter as an experience rather than as a report.",
            ],
        },
        {
            "id": "event_through_perception",
            "frames": [
                "A major event in your story must be delivered through the eyes of someone who can only grasp part of it.",
                "You are writing the chapter where the plot's largest development arrives, and it arrives to a character who was not prepared for it.",
                "Your chapter contains a turn of events whose full significance the viewpoint character will not understand for several chapters.",
            ],
            "context": "Large events read as large when they are experienced partially; delivering them through an unprepared perceiver is the difference between an event and an announcement.",
            "stages": ["the chapter's central sequence", "the scene that turns the arc", "the moment the news arrives"],
            "openers": [
                "Deliver the event through what the character can perceive, misunderstand, and decide, and let the reader do the assembling. The temptation is to widen the lens at the important moment, which is exactly when the close lens is most valuable: a large event half-understood lands harder than a large event explained, because the reader's own recognition arrives alongside the character's partial one.",
                "Before drafting a major development, decide the sequence of what this character notices first, what they notice late, and which of their concerns intrudes on the moment. Catastrophe in close narration is always mixed with ordinary preoccupations, and the mixture is what makes the moment belong to a person rather than to the plot.",
            ],
            "closers": [
                "Write the development as it arrives: in the wrong order, through the character's existing expectations, with their body occupied and their attention imperfect. Then close the sequence on the decision the partial understanding forces, not on the explanation the reader is waiting for.",
                "Hold the close position through the event and let comprehension trail the facts. The chapter's job is not to deliver the full meaning but to deliver the experience that makes the reader construct it.",
            ],
        },
        {
            "id": "knowledge_limit",
            "frames": [
                "Your chapter requires a piece of information that the viewpoint character cannot plausibly possess yet.",
                "You need the reader to understand a situation whose details only a different character knows.",
                "Your plot's next movement depends on a fact that has to reach the reader without the viewpoint learning it directly.",
            ],
            "context": "Information that must cross a knowledge boundary should travel by means the reader can verify: behavior, consequence, inference, or another character's mistake.",
            "stages": ["the middle of the book", "the chapter's investigative stretch", "a scene built on partial knowledge"],
            "openers": [
                "Treat the knowledge limit as a design constraint and solve it with the story's own machinery. Whatever the reader needs can be carried by a visible consequence, a behavior that only makes sense given the hidden fact, or an inference the viewpoint draws incorrectly. Reject the shortcuts, the convenient overhearing and the unexplained certainty, because they teach the reader that knowledge in this book is awarded rather than earned.",
                "When the plot needs the reader to know something the viewpoint cannot, give the reader the evidence and deny the character the conclusion. The asymmetry is productive: the reader's knowledge generates dread, patience, or frustration, and the character's ignorance generates the decisions that move the story. Decide what evidence the chapter can show and what conclusion the viewpoint will draw from it, and let the difference carry the information.",
            ],
            "closers": [
                "Route the information through behavior, consequence, or misreading, and write the chapter so that every reader-side inference is supported by something physically present. The limit stays intact and the reader still learns what the plot requires.",
                "Hold the character inside their knowledge and let the reader stand outside it. Write the scene so the gap is visible to the reader and invisible to the person inside it, and the chapter will generate pressure from a fact nobody has stated.",
            ],
        },
        {
            "id": "misread_that_holds",
            "frames": [
                "The viewpoint character's interpretation of this chapter's events is wrong, and it needs to stay wrong for several chapters.",
                "You want a misunderstanding to function as structure rather than as a small complication.",
                "Your protagonist is about to draw the wrong conclusion from accurate evidence.",
            ],
            "context": "A durable misreading must be earned from the character's existing beliefs and must produce consequences that look like consequences of the truth.",
            "stages": ["the first act's close", "the chapter after the midpoint", "a scene where the evidence is ambiguous"],
            "openers": [
                "Build the misreading out of accurate observation and a wrong frame. The character should notice real details, reason plausibly from them, and arrive somewhere false because their assumption about the situation's meaning was already in place before the chapter began. Decide the assumption, decide the two details that will appear to confirm it, and decide the decision it will produce.",
                "Make the wrong conclusion consequential rather than merely held. A misreading that changes nothing is a delay; a misreading that produces a decision, a betrayal, or an alliance is a structure. Identify the action this wrong belief makes the character take, and let the action be the chapter's actual plot movement.",
            ],
            "closers": [
                "Write the chapter as if the misreading were correct: describe through it, decide through it, and let every consequence proceed as though it were true. The reader will register the error without being told, and the correction, when it arrives chapters later, will be a turn rather than a clarification.",
                "Fix the false assumption, the confirming details, and the decision it drives, then draft the scene from inside the error. Nothing in the chapter should hint that the narration knows better.",
            ],
        },
    ],
    "traps": [
        {
            "id": "camera_above",
            "frames": [
                "Your scene keeps drifting into a vantage that knows more than the viewpoint character can.",
                "You are drafting a scene and notice the narration quietly reporting what other people are thinking.",
                "You want the reader to understand the whole situation in a chapter that is supposed to be close.",
            ],
            "slide": "The pull is toward the useful vantage: a sentence that explains another character's intention, a detail placed because the author knows it matters, a summary of what everyone in the room is feeling. It feels efficient while drafting, because it delivers information in one stroke, and it costs the scene its interiority.",
            "stages": ["the chapter's description", "the scene's opening", "the sequence after the turn"],
            "openers": [
                "You can feel the pull upward: the moment the scene becomes complicated, the writing wants to rise out of the character and explain the room from above. The move is tempting because it removes ambiguity in a single gesture. Refuse it while drafting, and let the difficulty stay inside the perception where it belongs.",
                "The temptation in front of you is omniscient convenience, the sentence that tells the reader what is actually happening because the author finally wants the situation clear. Name it now and set it aside: clarity bought this way is subtracted from the reader's experience of a mind under pressure.",
            ],
            "damage": "The cost is structural rather than stylistic. Interiority is what makes limited knowledge legible, and limited knowledge is what makes decisions necessary; a chapter that drifts above its characters resolves its own tensions and leaves the reader with no work and no uncertainty, which is also why such chapters feel inert even when a great deal happens in them.",
            "reason_past": "Reason past it while drafting by asking, for every sentence of perception, whether the perceiver could have arrived at it from inside the scene. Where the answer is no, either delete it or convert it into something available: a gesture, a consequence, a piece of evidence that the viewpoint misreads.",
            "closers": [
                "Write the whole chapter from inside the position and route every piece of information through something perceptible. Set the rule now, before drafting begins, and hold it even where the scene would be easier to clarify from above.",
                "Keep the vantage fixed and let the reader do the assembling. Nothing in the chapter should know more than the person living it, and the story is stronger for the gap.",
            ],
        },
        {
            "id": "author_knowledge",
            "frames": [
                "You are describing a location whose real importance lies several chapters ahead.",
                "Your chapter contains an object, room, or person that matters later and feels important now for reasons the viewpoint cannot have.",
                "You notice the description emphasizing something that the story has not yet made relevant.",
            ],
            "slide": "The scene fills with forward-pointing weight: an object described at length, a room given more detail than the viewpoint would spend on it, a person examined because the author knows they will matter. The pull is strong because planting matters and detail feels like planting.",
            "stages": ["the chapter's description of place", "the introduction of an object", "the arrival of a new character"],
            "openers": [
                "The pull here is authorial emphasis, detail placed because the plot needs it rather than because the perceiver would notice it. It is easy to mistake this for good planting. Reason past it now: whatever must be established later should be established inside the character's ordinary attention, or the reader will register the author's hand before they register the story.",
                "You can feel the description reaching forward, spending the viewpoint's attention on something whose meaning lives in a later chapter. Refuse the reach and find the reason the character would notice it now: use, obstruction, familiarity, irritation, cost.",
            ],
            "damage": "Readers learn the author's tonal habits quickly. When detail is allocated by future importance rather than by present perception, the important material announces itself, foreshadowing becomes visible as mechanics, and the reader can predict which objects will return, which removes the surprise that the return was supposed to produce.",
            "reason_past": "Reason past it by giving every planted detail a present function inside the scene: it is used, hated, paid for, blocked by, or ignored for a specific reason. The planting survives as texture, the reader's attention stays on the scene, and the later payoff arrives as recognition rather than as the confirmation of a hint.",
            "closers": [
                "Let the character's attention allocate the chapter's detail and trust that a thing which is used in the present can be recalled in the fortieth chapter. Write the description as work, obstacle, or habit, and the planting will look like ordinary life.",
                "Keep every detail inside the perceiver's purpose. Nothing is described because the book needs it later; everything is described because someone in the scene has a reason to look at it now.",
            ],
        },
        {
            "id": "essay_thought",
            "frames": [
                "Your viewpoint character is thinking at length in a chapter that also needs to keep moving.",
                "You find yourself writing reflective interior passages that summarize the story's themes.",
                "A scene's tension is being carried mostly by paragraphs of internal commentary.",
            ],
            "slide": "The interior passages grow longer and more articulate, and the character begins to formulate their situation in complete, well-shaped sentences that name their own emotional state and its causes. The pull is strong because it feels like depth, and it is the easiest way to say what the book means.",
            "stages": ["the reflective stretch", "the scene after a reversal", "the chapter's final movement"],
            "openers": [
                "You can feel the interiority hardening into essay: the character begins to explain their own psychology in ordered clauses. It reads as insight while drafting and it flattens the character into a narrator. Reason past it now, before the passages set.",
                "The pull is toward articulated self-knowledge, the paragraph where the character states exactly what they feel and why. Refuse it. Thought on the page is partial, interrupted, and frequently wrong about itself, and the reader's inference is worth more than the character's summary.",
            ],
            "damage": "The damage is to both character and pace. A character who can articulate their condition completely is no longer in it, and a book whose interior passages report the meaning of its events removes the reader's share of the work. The scene also stops moving, because articulated reflection is static by nature, and static stretches accumulate until the middle of the book feels like thinking rather than happening.",
            "reason_past": "Reason past it by converting reflection into pressure: the character thinks while doing something, the thought is interrupted by the task, and the conclusion is partial or self-serving. Keep a task in the scene, keep the thought in fragments, and let the reader assemble the meaning the character cannot state.",
            "closers": [
                "Keep the character's mind occupied with the scene's practical demands and let the thought break against them. What the character concludes should be smaller, stranger, or more self-serving than the truth, and the chapter should end on an action rather than an insight.",
                "Write interiority as work interrupted and as conclusions that are only partly earned. The reader will supply the larger understanding, and the character stays inside the experience rather than above it.",
            ],
        },
    ],
    "discipline": [
        "Before drafting the chapter, write down the perceiving position, the two things the character wants in the scene, and the one fact they must not learn. These three decisions govern everything else about the chapter's texture.",
        "While drafting, check each descriptive passage against the perceiver's attention: if a detail is present because the author knows it matters, either route it through a character's use, or cut it and save the material for a chapter where someone has a reason to see it.",
        "Keep the character's worldview stable across the book and let it change only in response to events that are on the page. Consistency of perception is what makes a character recognizable from chapter to chapter, and its slow alteration is one of the clearest ways a long story shows change.",
    ],
    "themes": [
        {
            "id": "perception_as_instrument",
            "frames": [
                "You are planning how a novel will distribute information across its chapters.",
                "You want the book's point of view to do structural work rather than to be a surface choice.",
                "You are deciding, across an arc, who perceives which parts of the story.",
            ],
            "question": "How does viewpoint choice work as a plotting instrument across the whole book rather than as a per-scene preference?",
            "openers": [
                "Perception is a plot mechanism before it is a stylistic one. Who sees what determines what can be decided, and the sequence in which information becomes available to a character is the sequence of the plot's turns. Treat viewpoint as distribution: at each stage of the book, decide who holds which facts, who has been given a wrong frame for them, and where the reader stands in relation to both.",
                "Across a whole book, the pattern of who knows what is the story's hidden architecture. Plan it deliberately: the moments when the reader learns something before a character, and the moments when a character learns something after the reader, are the two engines of suspense and surprise, and their placement can be scheduled the way scenes are scheduled.",
            ],
            "middles": [
                "Decide the reader's position relative to each character's knowledge, scene by scene, and let the gap be intentional rather than accidental. Reader ahead of character generates dread and impatience; reader behind character generates curiosity and the wish to catch up; both are useful and neither should persist unchallenged for too long.",
                "Restrict knowledge unevenly across the cast. Different characters should hold different fragments, and no one should hold all of them, because a single informed character converts the story's information problem into a delivery problem and removes the need for the cast to act under uncertainty.",
                "Let errors survive. A wrong belief held by a character for several chapters is not a delay in the plot but a plot of its own, and the correction, when it comes, should cost something, which means the wrong belief must have produced consequences the character cannot simply undo.",
                "Schedule perception-driven turns deliberately: the chapter where a character's interpretation of an earlier event changes, the chapter where a misreading is confirmed by new evidence and becomes stronger, and the chapter where the error collapses. These three movements are as structural as any confrontation.",
            ],
            "closers": [
                "Commit to a knowledge architecture for the book: who holds what, when the reader is ahead, when the reader is behind, and which errors are load-bearing. Write each chapter inside the position its perceiver can occupy, and let the plot's turns arrive as changes in understanding rather than as announcements.",
            ],
        },
        {
            "id": "interiority_across_arc",
            "frames": [
                "You want a novel's interior life to stay specific across hundreds of pages rather than generic after the first chapters.",
                "You are planning how a protagonist's inner life should develop without becoming more articulate than the character.",
                "You are thinking about how close narration survives the length of a whole book.",
            ],
            "question": "How does interiority stay specific, limited, and alive across an entire novel rather than collapsing into reflective summary?",
            "openers": [
                "Interiority decays over a long book. Early chapters carry a genuine perceptual filter; later chapters drift toward a general thoughtful voice that could belong to anyone, because the most available way to write reflection is also the least specific. Plan against the decay: maintain a private register for each viewpoint character, and refresh it with the character's ongoing concerns rather than with thematic reflection.",
                "The long-arc problem with interiority is articulation creep: the character's inner language becomes more fluent as the book proceeds, because fluency is what the writing rewards. Decide now what this character can and cannot put into words, and hold that boundary even when an articulate passage would save the scene; the character's limits are part of the story's information design.",
            ],
            "middles": [
                "Keep a list of the character's persistent concerns, irritations, and habits of thought, and let them resurface across chapters. Continuity of preoccupation is what makes interiority feel like a mind rather than a mood, and it gives later scenes material to work with that the plot did not have to supply.",
                "Vary the interiority's texture by circumstance. Under threat, attention narrows and thought becomes fragmentary and practical; in intervals, thought wanders, remembers, and is petty. A book whose inner passages have the same texture under all conditions has only one interior mode, which is the same as having none.",
                "Let the character's interpretation of their own feelings stay unreliable and inconsistent in detail. Self-report that is always accurate is a characterization failure; a person mislabels anger as tiredness, treats grief as logistics, and calls fear preparation, and the pattern should be stable enough to be recognizable and wrong enough to be interesting.",
                "Carry the effects of earlier interiority forward. What a character concluded privately in chapter three should influence what they attempt in chapter twelve, even if the conclusion was wrong, which is how interior life becomes plot rather than commentary.",
            ],
            "closers": [
                "Plan interiority as a maintained system: a private register per viewpoint, persistent concerns, circumstance-dependent texture, and a boundary on how much the character can articulate about themselves. Then the close narration will keep its specificity for the length of the book.",
            ],
        },
    ],
    "principles": [
        "Perception before description: the scene is delivered by a mind with limits, and those limits are the scene's engine rather than its obstacle.",
        "Interiority before explanation: whatever the reader needs to understand about a character should be inferable from how they perceive, decide, and misread, rather than stated by the narration.",
        "Misreading before correction: a wrong belief that has produced consequences is worth more than a clarification delivered as soon as the error appears.",
    ],
}
