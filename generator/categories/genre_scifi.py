"""Science fiction: how the genre works and what a story in it looks like."""

GENRE = {
    "id": "scifi",
    "label": "Science fiction",
    "category": "genre_scifi",
    "promise": "one change to the world, followed all the way to what it does to people",
    "story_shape": (
        "a science fiction story takes a single speculative change, works out its consequences honestly, "
        "and follows them into the lives that have to live with it: a person whose ordinary problem is "
        "made new by the change, an opposing interest that benefits from the old order, and an ending "
        "that answers the question the premise raised."
    ),
    "CAT": {
        "id": "genre_scifi",
        "label": "Science fiction: the speculative change and its human consequences",
        "moves": {
            "one_change_extrapolated": [
                "Choose one change and take its consequences seriously in every direction: who profits, who is displaced, what becomes cheap, what becomes impossible. One change followed honestly is more convincing than five asserted at once.",
                "Decide the change's age. A technology or discovery that arrived last year produces upheaval, one that arrived a generation ago produces customs, and the story's conflict sits differently in each case.",
                "Work out who the change is bad for, and build the plot's opposition out of the people whose position it threatens rather than out of a villain who dislikes progress.",
            ],
            "idea_dramatized": [
                "Give the idea a face and a cost before the story explains it. A premise is taught to the reader through what it makes someone do, not through what a knowledgeable character says about it.",
                "Plan an early scene in which the change makes an ordinary want harder or easier, so the reader learns the world's rules by watching them apply to something small.",
                "Reserve the conceptual explanation for the moment the reader already wants it, and keep it short enough to serve the scene rather than replace it.",
            ],
            "scale_from_personal": [
                "Start the story at the smallest scale the change touches and let the implications widen on their own. A colony's water ration is more legible than a civilization's collapse, and it can carry the same argument.",
                "Plan the ladder of scales: what the change means for a person, a household, an institution, a world. Choose which rungs the book will climb and in what order.",
                "Anchor the largest implications to something the reader has already watched being lost.",
            ],
            "competence_and_cost": [
                "Let the characters be competent inside the world's rules, and make problems arise from the rules themselves rather than from characters forgetting them.",
                "Decide what the science or technology cannot do, and make the plot's solution cost something the world's rules make expensive.",
                "Show the labor and the maintenance behind the marvels: systems that need upkeep imply a world with resources, priorities, and people who do the upkeep.",
            ],
            "society_as_argument": [
                "Treat the change as a social event as much as a technical one: who governs, who is monitored, who is left out, who is paid. The genre's strongest conflict comes from two parties who both have a case.",
                "Give the opposing side its best argument, and let the protagonist hold their position under pressure rather than by default.",
                "Decide what the world has decided to stop noticing, because the story's theme often lives in the thing the setting treats as normal.",
            ],
            "question_answered": [
                "State the question the premise raises, and decide how the ending answers it: an answer, a refusal, or a demonstration of what the answer costs.",
                "Aim the ending at the question rather than at the technology, so the book resolves what it actually asked.",
            ],
        },
        "problems": [
            {
                "id": "lecture_in_place_of_story",
                "frames": [
                    "The world's ideas are explained more often than they are inhabited.",
                    "Your characters keep informing each other of things they already know.",
                    "The most interesting material in the plan is exposition.",
                ],
                "context": "A speculative premise earns belief through consequences rather than through explanation.",
                "stages": ["the first statement of the idea", "the drafting of the early chapters", "the planning of the reveal"],
                "openers": [
                    "Convert the explanation into an event: someone is denied a service, denied passage, charged a fee, denied a memory. The reader assembles the world's rules from what they watch happen, and then the one short explanation lands as confirmation rather than as a lecture.",
                    "Give each fact a bearer with a reason to say it: a challenge, a complaint, a negotiation, a lie. Where no one would say it, let it be shown or leave it out.",
                ],
                "closers": [
                    "Commit to teaching the world through consequences: the change appears as something that constrains or enables a person in the scene before it is ever named.",
                    "Decide which three facts the reader must know by the end of the first act, and place them as events rather than as statements.",
                ],
            },
            {
                "id": "tech_solves_conflict",
                "frames": [
                    "Every obstacle in the plan has a device standing next to it.",
                    "The world's capabilities keep arriving exactly when the plot needs them.",
                    "Your protagonist's competence is a list of gadgets.",
                ],
                "context": "Technology that resolves problems shortens the story it appears in.",
                "stages": ["the design of the world's rules", "the escalation of the middle", "the arrangement of the third act"],
                "openers": [
                    "Price the technology: limited range, scarce fuel, surveillance that cuts both ways, a dependency on an institution. Every capability the plot relies on should create a new vulnerability.",
                    "Make the obstacles social and institutional rather than merely technical, so the protagonist's solution requires other people's consent, which is where the story's conflict lives.",
                ],
                "closers": [
                    "Commit to limits: what the world's devices cannot do, and who controls the ones that can.",
                    "Decide the constraints before the capabilities, and hold them for the length of the book.",
                ],
            },
            {
                "id": "metaphor_without_people",
                "frames": [
                    "The premise is compelling and there is nobody specifically in it.",
                    "The story is an argument wearing characters as illustrations.",
                    "You can state the book's point and not its plot.",
                ],
                "context": "A speculative idea is a setting for a story, not a substitute for one.",
                "stages": ["the first statement of the idea", "the casting of the protagonist", "the design of the ending"],
                "openers": [
                    "Cast the change by damage: whose ordinary life is made harder, more expensive, or more dangerous by the world's arrangement, and what do they want that the arrangement stands in the way of.",
                    "Make the book's argument something a character has to choose between rather than something the world demonstrates.",
                ],
                "closers": [
                    "Commit to a person with a want the world's change obstructs, and let the argument be a consequence of their choice.",
                    "Settle the protagonist, their ordinary want, and the way the change makes it expensive.",
                ],
            },
        ],
        "traps": [
            {
                "id": "asymmetric_knowledge_lecture",
                "frames": [
                    "One character understands the world and explains it to another who exists to ask.",
                    "You are drafting the scene that teaches the reader how the world works.",
                    "The dialogue keeps turning into an explanation of the setting.",
                ],
                "slide": "A knowledgeable character explains the world to a character who has no reason to be hearing it for the first time.",
                "stages": ["the drafting of the explanatory scene", "the plan for how the reader learns the rules", "the arrangement of the reveal"],
                "openers": [
                    "Give the informed character something to protect, sell, or hide, and let the information escape as a consequence of that interest. The reader then learns the rules while watching someone pursue something, which is the difference between an explanation and a scene.",
                    "Move the fact out of the conversation: let the protagonist encounter it as an obstacle, a charge, a refusal, or a malfunction, and let them draw the conclusion the reader needs.",
                ],
                "damage": "The scene becomes a manual. The explaining character loses their want, the listening character loses their function, and the story's tension drains into the exposition, which leaves the reader informed and uninvested.",
                "reason_past": "Reason past it by asking what each participant wants from the exchange and letting the world's rules surface as obstacles to those wants. Where no one would say a fact aloud, show its effect instead.",
                "closers": [
                    "Commit to teaching the world through consequence: the reader learns the rules by watching them cost someone something.",
                    "Decide the three facts the chapter must deliver and the want each one obstructs.",
                ],
            },
            {
                "id": "present_day_with_gadgets",
                "frames": [
                    "The world has new devices and the same institutions, manners, and economics as the present.",
                    "You are building the setting and only the technology has changed.",
                    "The plan treats the speculative change as equipment rather than as history.",
                ],
                "slide": "The change arrives as a new device while everything around it, work, family, law, and money, behaves exactly as it does today.",
                "stages": ["the design of the world", "the planning of ordinary life inside the setting", "the drafting of the domestic scenes"],
                "openers": [
                    "Trace two or three consequences of the change into ordinary life: what has become cheap, what work no longer exists, who is watched, what a household argues about now. The world then reads as a place rather than a coat of paint, and the change does the work a premise is supposed to do.",
                    "Ask who profits and who is displaced by the change, then put the protagonist where those two groups meet in daily life rather than in a briefing.",
                ],
                "damage": "The change stops being a change. Readers register the inconsistency before they can name it, so the premise costs the book its credibility while buying none of the genre's pleasures, and the story reads as the present wearing equipment.",
                "reason_past": "Reason past it by deciding the change's age, its beneficiaries, and its displaced, and then writing one ordinary scene inside each consequence. Customs and institutions are the visible residue of a change that has been in the world for a while.",
                "closers": [
                    "Commit to the change's consequences in ordinary life: what is cheap, what is watched, what is lost.",
                    "Settle who benefits, who is displaced, and what a family argues about now, before plotting the plot.",
                ],
            },
            {
                "id": "scale_inflation",
                "frames": [
                    "The premise escalates by getting bigger.",
                    "You are raising the stakes and the numbers keep rising with them.",
                    "The third act is larger than the middle in every dimension.",
                ],
                "slide": "Escalation is carried by magnitude: more ships, larger populations, longer timescales, and threats measured in worlds rather than in people.",
                "stages": ["the escalation of the middle", "the design of the third act", "the arrangement of the climax"],
                "openers": [
                    "Escalate along the ladder of intimacy instead: what the change costs a person, then a household, then an institution the reader has been inside. Keep the largest event connected to the smallest one by a chain the reader has followed, so magnitude arrives as consequence.",
                    "Measure escalation in what can no longer be undone rather than in how many are affected. Irreversibility is legible at any size.",
                ],
                "damage": "Magnitude replaces meaning. A reader cannot weigh a trillion, so each escalation raises the stakes on paper and lowers them in effect, and the ending has to out-scale the middle to feel like an ending, which pushes the story further from the people in it.",
                "reason_past": "Reason past it by keeping the story's largest consequence personal: decide what the scale costs the people the reader knows, and let the world's numbers be background to that.",
                "closers": [
                    "Commit to escalation by cost and irreversibility rather than by numbers.",
                    "Decide what each escalation makes permanent, and keep the largest one attached to a person the reader has watched.",
                ],
            },
        ],
        "discipline": [
            "Every speculative element the plot relies on should be introduced, constrained, and used in that order.",
            "Keep the world's rules consistent between chapters, and treat a convenient exception as a structural fault rather than a flourish.",
            "Make the story legible to a reader who does not know the genre's conventions: the terminology should be learnable from use.",
        ],
        "themes": [
            {
                "id": "scifi_promise",
                "frames": [
                    "You are planning a science fiction story and want the premise to pay off.",
                    "You want the idea to be felt rather than explained.",
                    "You are deciding what a science fiction story looks like before writing it.",
                ],
                "question": "What does a science fiction story need in order to work, and how is the premise built into the plan?",
                "openers": [
                    "A science fiction story turns on one honest consequence: the change is made, its costs are traced, and a person who has something ordinary at stake has to live inside the result. The book's intelligence is in the tracing rather than the invention.",
                    "The genre's promise is a question answered. The premise raises it, the middle complicates it with human counterexamples, and the ending answers it in a form the reader can weigh, usually a cost someone chose to pay.",
                ],
                "middles": [
                    "Decide the change, its age, its beneficiaries, and its losers, then place the protagonist where those two interests cross.",
                    "Plan the sequence in which the reader learns the change's rules, and make every piece of knowledge arrive as a consequence of something someone wanted.",
                    "Give the middle a counterexample to the protagonist's position: a person who has done well under the new arrangement and is not wrong about it.",
                    "Aim the third act at the question the premise raised, and let the answer be shown as a choice with a price rather than stated.",
                ],
                "closers": [
                    "Commit to the premise's consequences, the person who pays them, and the answer the ending will earn.",
                    "Settle the change, the ordinary want it obstructs, and the question the book is asking before plotting the movements.",
                ],
            },
        ],
        "principles": [
            "One change, followed honestly, beats five asserted at once.",
            "The premise is taught through consequence rather than explained.",
            "Technology with a price generates story; technology without one ends it.",
            "The book's argument belongs to characters who have to choose, not to the world.",
            "The ending answers the question the premise raised.",
        ],
    },
}

CAT = GENRE["CAT"]
