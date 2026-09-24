"""Thriller: how the genre works and what a story in it looks like."""

GENRE = {
    "id": "thriller",
    "label": "Thriller",
    "category": "genre_thriller",
    "promise": "a competent person under a clock, with something worse behind every answer",
    "story_shape": (
        "a thriller story puts a protagonist with something to lose into a situation where the danger "
        "advances on its own schedule: an antagonist whose plan is already ahead, information the "
        "protagonist needs and cannot trust, and an escalation in which each solution reveals a larger "
        "problem until the final confrontation is forced by the protagonist's own choice."
    ),
    "CAT": {
        "id": "genre_thriller",
        "label": "Thriller: the clock, the asymmetry, and escalation under pressure",
        "moves": {
            "clock_and_pressure": [
                "Give the story a clock that advances without the protagonist: a deadline, a departure, a procedure, an expiring window. The clock is what converts thinking time into tension, and it must be established early enough that the reader feels it before they are told about it.",
                "Decide what the clock runs out on, and make it something the protagonist cannot accomplish alone: the deadline should force cooperation with someone they do not trust.",
                "Keep the clock honest. A deadline that can be extended when convenient teaches the reader to stop counting.",
            ],
            "antagonist_ahead": [
                "Plan the antagonist's moves as a schedule that runs underneath the protagonist's investigation, so every discovery is met by evidence that someone expected them to get there.",
                "Give the antagonist a goal that is legible and a method that is proportionate: the reader should be able to imagine the next move without being able to prevent it.",
                "Let the antagonist be right about the protagonist's weakness, and let the plot exploit it specifically rather than generally.",
            ],
            "information_asymmetry": [
                "Decide what the protagonist knows, what the reader knows, and what the antagonist knows at every stage, then use the gaps as fuel: the reader's knowledge creates dread, and the protagonist's ignorance creates motion.",
                "Plan revelations that reframe rather than resolve: each answer should make the situation more dangerous or more personal, so escalation comes from comprehension rather than from the antagonist's growing power.",
                "Keep one thread the reader can verify and cannot act on, because helpless knowledge is the genre's most efficient form of suspense.",
            ],
            "escalating_cost": [
                "Raise the cost to the protagonist rather than the number of threats: access lost, a relationship spent, a rule broken, safety abandoned.",
                "Make each solution create the next problem, so that competence advances the story and complicates it at once.",
                "Decide the point at which running is no longer possible, and build the third act around the protagonist choosing to act instead of being cornered.",
            ],
            "competence_and_flaw": [
                "Give the protagonist a specific competence that produces solutions the reader can follow, and a flaw the antagonist can use. Both should be visible before the plot needs them.",
                "Show the protagonist thinking under pressure: decisions made with partial information, then revised. Competence in a thriller is the quality of the decisions rather than the size of the resources.",
                "Let the protagonist make one costly error caused by their flaw, at the point in the story where the mistake cannot be absorbed.",
            ],
            "personal_stakes": [
                "Attach the case to something private: a debt, a loyalty, a past the protagonist would rather not revisit. Public stakes create a job; private stakes create a person.",
                "Decide what the protagonist would have to give up to walk away, and make that price rise across the story so that walking away becomes impossible.",
            ],
        },
        "problems": [
            {
                "id": "no_clock",
                "frames": [
                    "The investigation proceeds at whatever pace the protagonist chooses.",
                    "The antagonist waits to be found.",
                    "The middle is a sequence of discoveries with no pressure behind them.",
                ],
                "context": "A thriller without a clock is a mystery that has forgotten its deadline.",
                "stages": ["the planning of the middle", "the arrangement of the antagonist's schedule", "the drafting of the pursuit"],
                "openers": [
                    "Install a mechanism that moves on its own: a hearing, a shipment, a treatment window, a surveillance authorization due to expire. Then plan the antagonist's moves in parallel, so the protagonist is always working against two schedules rather than one.",
                    "Decide what happens if the protagonist does nothing, and make it worse each chapter. Inaction with a cost is what makes the clock structural rather than decorative.",
                ],
                "closers": [
                    "Commit to the two schedules: what the protagonist must do, and what happens regardless of them. The tension is in the gap between the two.",
                    "Fix the deadline, the antagonist's timetable, and the cost of delay before arranging the middle.",
                ],
            },
            {
                "id": "villain_waiting",
                "frames": [
                    "Your antagonist exists only where the protagonist looks.",
                    "The opposition reacts to the investigation instead of pursuing its own plan.",
                    "The danger is atmospheric until the climax.",
                ],
                "context": "Threat that only appears on demand is a costume rather than a force.",
                "stages": ["the design of the antagonist", "the planning of the second act", "the arrangement of the confrontation"],
                "openers": [
                    "Write the antagonist's plan first, including the steps that do not involve the protagonist at all. The story then has two engines, and the protagonist's decisions intersect them.",
                    "Let the antagonist act before the protagonist understands: the first strike should establish the method and the reach, and it should be aimed at something the reader has already seen valued.",
                ],
                "closers": [
                    "Commit to an antagonist with a schedule, a reach, and a reason, and let the protagonist's progress be measured against it.",
                    "Settle what the antagonist does in chapters where the protagonist is not present, and hold it consistent.",
                ],
            },
            {
                "id": "twist_without_preparation",
                "frames": [
                    "The plan depends on the reader being surprised by a reveal.",
                    "Your reversal changes the story rather than the reader's understanding of it.",
                    "The middle conceals information rather than managing it.",
                ],
                "context": "A thriller's revelation must be paid for earlier by evidence the reader did not weigh correctly.",
                "stages": ["the planning of the reveal", "the drafting of the investigation", "the arrangement of the ending"],
                "openers": [
                    "Place the evidence for the reveal in plain sight with an innocent explanation, and let the reader's correct observation be misread. The reveal then reorganizes the story instead of replacing it.",
                    "Check that the reversal survives a reread: what the reader learns should make the earlier chapters more coherent, not more convenient.",
                ],
                "closers": [
                    "Commit to the reveal's prerequisites: what the reader must have seen, and what would have to be true for them to have misread it.",
                    "Decide the reveal, its necessary evidence, and the innocent reading for each clue.",
                ],
            },
        ],
        "traps": [
            {
                "id": "protagonist_needs_rescue",
                "frames": [
                    "The protagonist is repeatedly saved by circumstance or by an ally arriving.",
                    "You are writing the pursuit and the pressure keeps being relieved from outside.",
                    "The plan relies on the antagonist's restraint to keep the protagonist alive.",
                ],
                "slide": "The protagonist is rescued from each tightening situation by an arrival, a coincidence, or the antagonist choosing not to finish the job.",
                "stages": ["the drafting of the pursuit", "the planning of the second act", "the arrangement of the confrontation"],
                "openers": [
                    "Let the protagonist solve a smaller problem first with their own competence and their own risk, so the reader has watched them act before the plot escalates. Every aid that does arrive should cost something: a favor owed, a secret surrendered, an alliance that constrains them later.",
                    "Make the antagonist's restraint a decision with a reason, and let that reason be a trap the protagonist walks into rather than a mercy.",
                ],
                "damage": "Passivity drains the genre. Each rescue teaches the reader that the protagonist is not driving the story, so the final confrontation arrives with someone who has not been making decisions, and the ending has to be won by the antagonist's error rather than by the protagonist's choice.",
                "reason_past": "Reason past it by deciding what the protagonist does, on their own, in every act, and by pricing every piece of help they receive. A protagonist who drives the story does not need saving from it.",
                "closers": [
                    "Commit to a protagonist who acts first and pays for what they need.",
                    "Decide the protagonist's own solution in each movement, and the cost of every alliance.",
                ],
            },
            {
                "id": "information_dump",
                "frames": [
                    "The situation is delivered to the protagonist in a single briefing.",
                    "You are opening the story and need the reader oriented quickly.",
                    "The investigation advances by being told rather than by being done.",
                ],
                "slide": "The situation, the players, and the stakes are explained to the protagonist in one scene, and the story proceeds from complete information.",
                "stages": ["the drafting of the opening chapters", "the plan for how the investigation develops", "the arrangement of the first act"],
                "openers": [
                    "Give the protagonist one fact and one obstacle, and let each later piece of information cost something to obtain: a risk taken, a rule broken, a favor called in. What the reader learns then arrives attached to what the protagonist has spent, which is what makes knowledge feel like progress under pressure.",
                    "Open with a decision the protagonist has to make on incomplete information, and let the situation's shape emerge from the consequences.",
                ],
                "damage": "Everything is known and nothing is felt. The reader receives the plot's map without the experience of working inside the protagonist's limits, and the story's remaining tension has to be manufactured from scratch in the second act, which is where thrillers usually stall.",
                "reason_past": "Reason past it by planning knowledge as a series of purchases: what the protagonist gives up to learn each thing. The clock and the antagonist's schedule supply the pressure while the information arrives in pieces.",
                "closers": [
                    "Commit to an investigation that is paid for in risk, favors, and rules broken.",
                    "Decide what the protagonist knows at the start, and the price of every later discovery.",
                ],
            },
            {
                "id": "false_escalation",
                "frames": [
                    "Each act introduces a larger organization, a bigger weapon, or a higher level of conspiracy.",
                    "You are raising the threat and the protagonist's ability to affect it keeps shrinking.",
                    "The plan answers the middle with more resources on the antagonist's side.",
                ],
                "slide": "Escalation is achieved by enlarging the threat, so the story grows in scale while the protagonist's situation stays the same size.",
                "stages": ["the escalation of the middle", "the design of the antagonist", "the arrangement of the third act"],
                "openers": [
                    "Escalate along the protagonist's costs: what they can no longer do, who they can no longer rely on, what they have had to admit, what they have had to give away. The antagonist's plan can stay the same size while its consequences tighten around a person whose options are visibly shrinking.",
                    "Make each solution remove an option rather than add a resource, so competence advances the story and complicates it at once.",
                ],
                "damage": "The threat grows but the protagonist's ability to affect it shrinks, so the third act requires new resources rather than earned capability, and the reader's sense of pressure is replaced by a sense of spectacle with nothing at stake in it.",
                "reason_past": "Reason past it by keeping the antagonist's plan fixed in size and letting its consequences tighten: each act should leave the protagonist with fewer allies, fewer options, and more to lose.",
                "closers": [
                    "Commit to escalation by cost: fewer options, fewer allies, more to lose.",
                    "Decide what each movement takes from the protagonist rather than what it adds to the antagonist.",
                ],
            },
        ],
        "discipline": [
            "Every scene should be answerable in one line of what changed for the protagonist: knowledge, position, safety, or obligation.",
            "Keep the timeline reconstructable: when things happen, how long each step takes, and how much time remains on the clock.",
            "The reader should always be able to name the danger and where it currently sits, even when the protagonist cannot.",
        ],
        "themes": [
            {
                "id": "thriller_promise",
                "frames": [
                    "You are planning a thriller and want the pressure to hold from the first page.",
                    "You want the ending to be forced by the protagonist rather than by the plot.",
                    "You are deciding what a thriller story looks like before writing it.",
                ],
                "question": "What does a thriller story need in order to work, and how is the pressure built into the plan?",
                "openers": [
                    "A thriller story is a clock, an antagonist ahead of the protagonist, and a protagonist whose flaws are worth exploiting. The plot is the intersection of the antagonist's schedule with the protagonist's choices, and the ending is the moment the protagonist takes control of the schedule.",
                    "The genre promises pressure that keeps increasing. That comes from three decisions: something advances without the protagonist, information that is dangerous to hold, and a cost that rises every time the protagonist makes progress.",
                ],
                "middles": [
                    "Decide the antagonist's plan, the clock that measures it, and what the reader knows that the protagonist does not before planning any scene.",
                    "Design the middle as a sequence of answers that make the problem worse: each solution removes an option, and each revelation reframes what the protagonist is actually up against.",
                    "Give the protagonist one error caused by their flaw at the point of maximum investment, and make the rest of the story carry its consequence.",
                    "Plan the third act as the protagonist choosing to force the confrontation rather than being caught by it, so the ending belongs to their decision.",
                ],
                "closers": [
                    "Commit to the clock, the antagonist's schedule, and the protagonist's choice that ends it.",
                    "Settle the danger, what the protagonist has to lose, and what the reader knows, before plotting the pursuit.",
                ],
            },
        ],
        "principles": [
            "Something in the story must advance without the protagonist.",
            "The antagonist has a schedule of their own.",
            "Every answer widens the problem rather than closing it.",
            "Competence is visible in decisions made under partial information.",
            "The ending is forced by the protagonist's choice, not by the antagonist's mistake.",
        ],
    },
}

CAT = GENRE["CAT"]
