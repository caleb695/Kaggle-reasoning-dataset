"""Action, combat, and physical consequence."""

CAT = {
    "id": "action_physicality",
    "label": "Action, combat, and physical consequence",
    "moves": {
        "legibility": [
            "Keep the physical situation reconstructable at every moment: who is where, what each person is trying to accomplish, what is in the way, and what changed as a result. Rhythm can be shaped later, but legibility cannot be repaired once the reader has lost the space, and the loss is usually caused by sentences written for effect at the expense of position.",
            "Track the ledger of objects and conditions while planning the sequence: who holds what, what is loaded, damaged, dropped, or spent, which surface is wet, which door is open, how far the nearest cover is. The tracking is invisible when it is done and unmistakable when it is not, because the reader reconstructs the space whether or not the writing supplies it.",
        ],
        "imperfection": [
            "Let competence be partial. Characters misjudge distance, choose the wrong tool, hesitate at the wrong beat, and do the expedient thing rather than the elegant one. Imperfection is not a failure of the sequence; it is the mechanism by which a fight reveals who is having it, and it keeps the outcome uncertain, which is the sequence's only source of tension.",
            "Respect the body's economy: exhaustion, injury, breath, grip, footing, and the cost of carrying weight. Fatigue reduces options, and reduced options are exactly what the scene needs. An injury that persists past the scene is the cheapest available proof that the story's consequences are real.",
        ],
        "pacing_control": [
            "Control the sequence's tempo deliberately. Speed through the predictable and the mechanical, and slow down at the two or three moments that decide the outcome, using weight, traction, effort, and sensory narrowing to make those moments occupy more space on the page than the movement around them.",
            "Narrow the senses under speed and widen them at the decision points. Uniform sensory density flattens a sequence into a list of movements, while variation tells the reader where the stakes are without any statement about stakes.",
        ],
        "character_through_combat": [
            "Differentiate fighters by how they think rather than by what they can do. The patient one waits, the proud one overcommits, the frightened one protects something first, the trained one defaults to procedure even when it is wrong. The same person should be recognizable across every encounter in the book, which means choreography is a characterization surface rather than a set piece.",
            "Let the characters adapt when the first approach fails. Adaptation displays thinking under pressure, which is far more interesting than capability, and it keeps the sequence from becoming a demonstration of a fixed skill set.",
        ],
        "limits_and_costs": [
            "Keep abilities bounded and consistent, and establish the bounds before a scene depends on them. When a plan fails, the failure should come from the established limits or from an error, never from the sudden absence of a capability that was previously reliable.",
            "Refuse the convenient solution. Any power, ally, or resource that appears specifically to resolve the current difficulty damages the story's logic and retroactively discounts every earlier difficulty the characters took seriously.",
        ],
    },
    "problems": [
        {
            "id": "spatial_clarity",
            "frames": [
                "Your action sequence reads well but the reader cannot say where anyone is.",
                "You are drafting a fight in a confined space and the geography keeps dissolving.",
                "Your combat scene has several participants and the choreography is becoming abstract.",
            ],
            "context": "Physical clarity precedes dramatic effect: the reader must be able to reconstruct the space and the state of the objects in it.",
            "stages": ["the sequence's opening", "the middle of the fight", "the moment of the reversal"],
            "openers": [
                "Before drafting, fix the space on paper: the ground's condition, the exits, the obstacles, the distances that matter, and where each person starts. Then decide which of those elements the sequence will use and which will be allowed to stay in the background, so that the description spends its words on the two or three features that shape the fight.",
                "Decide the sequence's spatial spine as a series of positions rather than as a series of blows: an advance, a loss of ground, a moment of separation, a convergence. Readers follow the movement of bodies and the state of space far more readily than they follow exchanges of technique, and the spine keeps the sequence coherent even when the sentences are short.",
            ],
            "closers": [
                "Write the sequence with positions, objects, and conditions tracked explicitly, and refuse any sentence that improves the rhythm at the cost of the reader's ability to place everyone. Legibility is the tension.",
                "Draft the fight as movement through a specific space with specific obstacles, and let the technique stay secondary to who is where.",
            ],
        },
        {
            "id": "injury_consequence",
            "frames": [
                "A character in your book is injured and the injury has no effect on later chapters.",
                "You are drafting a physically costly sequence and the consequences are being left on the page.",
                "You want the story's violence to matter beyond its own scene.",
            ],
            "context": "Physical consequences are a ledger: what a body loses in one chapter should constrain what it can do in the next.",
            "stages": ["the aftermath of the sequence", "the following chapter", "the planning of the next act"],
            "openers": [
                "Before drafting the sequence, decide what the injury will cost later: a task the character can no longer perform, a dependency they now have, a delay, a decision made because of pain or weakness. Then the injury is not decoration but plot, and the reader learns that the story's physical events are real.",
                "Treat recovery as a schedule rather than a switch. Charting when a wound improves, what it prevents in the interim, and what it leaves permanently gives the middle act a body of accumulated cost, which is one of the most reliable sources of consequence in a long book.",
            ],
            "closers": [
                "Write the sequence and then carry the injury forward as a constraint on the next chapter's options, noting what it prevents rather than what it feels like.",
                "Fix the injury's schedule and let later scenes be shaped by what the character cannot do, so the physical event becomes structure.",
            ],
        },
        {
            "id": "power_without_price",
            "frames": [
                "A character's ability threatens to resolve the story's problems too easily.",
                "You are drafting a confrontation where one side can simply win.",
                "Your book's powers have no costs attached and the tension is thinning.",
            ],
            "context": "Capability needs a price, a limit, or a consequence; otherwise the story's obstacles become administrative rather than dramatic.",
            "stages": ["the confrontation", "the planning of the climax", "the chapter where an ability is used"],
            "openers": [
                "Attach a cost to the capability before the scene needs it: what it consumes, what condition it requires, what it prevents the character from doing simultaneously, who notices when it is used. A priced ability generates plot every time it is employed, while an unpriced one only ends scenes.",
                "Decide what the ability cannot do, and make sure the story's central problem lies on that side of the line. The most useful limit is the one that forces the character to solve the story's problem as a person rather than as a capability.",
            ],
            "closers": [
                "Write the confrontation inside the ability's established limits, with the cost paid on the page, and let the resolution depend on a human decision rather than on a capacity.",
                "Fix the price and the boundary before drafting, and build the scene so that using the power makes the situation harder in a specific way.",
            ],
        },
    ],
    "traps": [
        {
            "id": "cinematic_speed",
            "frames": [
                "Your action passages are fast but the reader cannot follow the sequence.",
                "You are drafting a fight and the prose is producing momentum instead of clarity.",
                "You want the scene to feel quick and the movement is outrunning comprehension.",
            ],
            "slide": "The sentences shorten and the verbs intensify, and the sequence acquires momentum at the cost of position. Movement blurs, geography collapses, and the reader acquires the impression of a fight without being able to reconstruct one, which is satisfying for a paragraph and hollow over a chapter.",
            "stages": ["the fight's middle", "the chase", "the sequence's climax"],
            "openers": [
                "You can feel the prose accelerating past the reader's ability to track the room. Refuse the acceleration and hold the positions: who moved where, what changed on the ground, and what the cost was. Speed should be created by what is omitted, not by what is obscured.",
                "The pull is toward impressionistic velocity, and it is easy to mistake for intensity. Reason past it now: the reader's tension depends on knowing what could happen next, which requires knowing where everyone is.",
            ],
            "damage": "Illegible action removes the possibility of suspense, because suspense requires a clear sense of the available options, and it also removes the possibility of consequence, since nothing that happens in a blur can be remembered or paid for. A book of blurred fights reads as a book without physical stakes no matter how violent the events.",
            "reason_past": "Reason past it by compressing the predictable and spending the words on the two or three moments that decide the outcome, always with a legible position attached. Speed comes from selection rather than from obscurity.",
            "closers": [
                "Write the sequence with positions tracked and the decisive moments slowed, keeping the prose efficient but never vague about where anyone is.",
                "Choose the moments that matter, place everyone clearly inside them, and skip the rest.",
            ],
        },
        {
            "id": "invincible_protagonist",
            "frames": [
                "Your protagonist keeps winning without paying for it.",
                "You are drafting a confrontation and both sides are operating at maximum competence.",
                "Your action sequences resolve too cleanly and the reader's investment is thinning.",
            ],
            "slide": "The character performs at the exact level the situation requires, chooses correctly under pressure, and exits with the objective and no damage. It feels like competence while drafting and it removes the scene's uncertainty, which was its only source of tension.",
            "stages": ["the confrontation", "the escape", "the sequence that resolves an act"],
            "openers": [
                "You can feel the scene arranging itself so that the protagonist's competence is displayed rather than tested. Break the arrangement: choose the error they make, the hesitation that costs them something, and the objective they fail to secure.",
                "The pull is toward the satisfying competence display. Reason past it by deciding what the character is bad at under pressure and letting that deficit decide part of the outcome.",
            ],
            "damage": "An unlosable protagonist destroys tension across the entire book, not only in the sequence where it occurs, because the reader extrapolates from the pattern and stops worrying. It also removes characterization, since character is most visible in how a person behaves when their competence fails.",
            "reason_past": "Reason past it by planning the sequence's cost before its outcome: what the character loses, fails to secure, or reveals in order to survive. Where the plot requires a success, let it be partial and paid for.",
            "closers": [
                "Write the sequence with a specific failure inside the success and a price attached to the outcome. The win should complicate the situation rather than resolve it.",
                "Plan the cost first and draft the sequence so that the character's competence is insufficient in one identifiable way.",
            ],
        },
        {
            "id": "convenient_capability",
            "frames": [
                "A solution to your current difficulty is arriving as a new capability.",
                "You are planning how a character escapes a situation that has no established route out.",
                "You notice a new ability or resource appearing exactly where the plot needs it.",
            ],
            "slide": "The rescue arrives: an ability the character has not used before, an ally whose skills exactly match the problem, an object discovered at the right moment. The pull is strong because the situation is genuinely difficult and the arrival solves it in one stroke.",
            "stages": ["the sequence's resolution", "the escape", "the chapter before the climax"],
            "openers": [
                "You can feel the convenient solution approaching, and it would be easy to write. Refuse it and go back to the established material: what does the character actually have, what did they lose earlier, who owes them, and which limit have they already hit.",
                "The pull is toward the new capability as a rescue. Reason past it by asking what the character can do with what the story has already given them, and if the answer is nothing, the problem is in the planning rather than in the scene.",
            ],
            "damage": "Convenient capabilities discount the story retroactively: every earlier scene in which the character struggled against a similar problem becomes theater, and the reader learns that the book's constraints are negotiable, which removes the weight from every future difficulty.",
            "reason_past": "Reason past it by planning the resolution from the story's existing inventory, and where a new element is genuinely required, introduce it earlier as an ordinary feature so its later use reads as inevitable rather than improvised.",
            "closers": [
                "Write the resolution from established material, with limits applied and costs paid, and let the difficulty be resolved by a decision rather than by an arrival.",
                "Refuse the new capability and build the way out from what the story has already supplied.",
            ],
        },
    ],
    "discipline": [
        "Before drafting any physical sequence, write down the space, the starting positions, the objects in play, and the three moments that will decide the outcome.",
        "During the draft, keep the physical ledger current: who holds what, what is broken, who is hurt, and what has changed on the ground. Any sentence that obscures those facts is a sentence to rewrite.",
        "After the sequence, carry the consequences forward: injuries, exhaustion, damage, lost objects, and the changed state of the location, all of which constrain the next chapter's options.",
    ],
    "themes": [
        {
            "id": "violence_as_ledger",
            "frames": [
                "You are planning how a novel's physical conflict will accumulate meaning across its acts.",
                "You want the story's violence to structure the plot rather than decorate it.",
                "You are deciding how a book's cost will be visible in its characters' bodies and choices.",
            ],
            "question": "How does physical conflict function as structural cost across an entire book rather than as isolated spectacle?",
            "openers": [
                "Plan physical events as entries in a ledger with continuing balances: injuries and their recovery schedules, wrecked equipment, burnt resources, alienated allies, damaged reputations, and lost ground. Each entry constrains later scenes, and the accumulation of constraints is what makes a long story's violence feel consequential rather than thrilling.",
                "Design the book's conflicts so that each one removes an option the characters had relied on. Availability of routes, allies, funds, and body impose the plot's pressure, and a series of conflicts that leaves the situation unchanged has no structural function beyond the scenes it occupies.",
            ],
            "middles": [
                "Distribute the costs across the cast rather than concentrating them on the protagonist. Secondary characters carrying injuries, debts, and grief makes the world feel like it is being spent by the story rather than by the plot.",
                "Keep an equipment and capability inventory with the story state: what is functional, what is repaired, what is gone. Its effects on the planning of later scenes is the practical measure of whether the book is tracking its own costs.",
                "Plan confrontations so that the resolution of one creates the conditions of the next: a victory that increases exposure, a retreat that costs a position, a rescue that incurs an obligation. Consequence linking is the structural form of escalation.",
                "Allow at least one major physical event to be survived badly rather than overcome. Partial outcomes that leave the characters changed, diminished, or in debt maintain the credibility of every other sequence in the book.",
            ],
            "closers": [
                "Commit to a physical ledger and a cost-based escalation plan: injuries with schedules, spent resources, removed options, and linked consequences. Then write each sequence so that what it takes is visible in what the following chapters cannot do.",
            ],
        },
    ],
    "principles": [
        "Legibility before intensity: the reader must be able to reconstruct the space and the state of the objects, or the sequence has no tension.",
        "Cost before outcome: every physical event should take something the later story will miss.",
        "Character before choreography: how a person fights is a continuation of how they think and decide.",
    ],
}
