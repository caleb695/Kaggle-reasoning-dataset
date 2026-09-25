"""Epic fantasy: how the genre works and what a story in it looks like."""

GENRE = {
    "id": "epic_fantasy",
    "label": "Epic fantasy",
    "category": "genre_epic_fantasy",
    "promise": "a large world with power in it, followed through people who pay for using it",
    "story_shape": (
        "an epic fantasy story is built on a world whose powers are priced: a threat larger than any "
        "single person, a protagonist drawn into it against their preference, allies whose interests "
        "diverge, and a resolution that costs the protagonist something they cannot get back. "
        "Its scale is carried by consequences rather than by geography."
    ),
    "CAT": {
        "id": "genre_epic_fantasy",
        "label": "Epic fantasy: world at scale, priced power, the long arc",
        "moves": {
            "priced_power": [
                "Decide what magic, or any power in this world, takes from the person using it. A power with no price is a solution, and solutions end stories; a power with a price is a decision, and decisions generate chapters.",
                "Make the price personal and legible before the power becomes useful: the cost is known to the reader in advance, so every later use is a choice the reader can weigh.",
                "Keep the power's limits as firm as its capabilities. The reader trusts a magic that refuses something the plot would like it to do.",
            ],
            "world_with_consequence": [
                "Build the world outward from its scarcities: what is short, who controls it, and what that control makes people do. Scarcity is what turns a setting into a place with politics.",
                "Decide what the world's history has already decided for the present, and make the story's conflict follow from that inheritance rather than from a new invention introduced for the plot.",
                "Give every culture the same treatment: wants, costs, and a reason its own people find it reasonable. A world with one right side reads as a map rather than a place.",
            ],
            "protagonist_against_preference": [
                "Draw the protagonist in against their preference, not toward their destiny. Reluctance gives the story a person to be while the plot makes its demands, and it postpones the choice that the ending will collect.",
                "Give the protagonist a competence the world needs and a private cost for using it, so capability and reluctance can operate at once.",
                "Let the scale arrive through obligation: a debt, a bloodline, a promise, a border. Scale by appointment, a prophecy or an inheritance of title, has to be backed by an obligation someone can refuse at a price.",
            ],
            "alliance_and_fracture": [
                "Plan the alliance before its fracture: what each faction wants from the shared goal, and which of those wants only survive while the threat is immediate.",
                "Make the group's disagreements practical rather than moral: routes, resources, time, command. Disagreements about means produce scenes; disagreements about good and evil produce arguments.",
                "Decide the moment the alliance breaks and what that break costs the story's chances. The break should be caused by the plot's pressure rather than by a character's sudden stupidity.",
            ],
            "scale_management": [
                "Keep the scale legible by returning to the same few people for each magnitude of event: what the war means is what it does to the people the reader has been following.",
                "Alternate the register of scenes: the large movement and the ordinary one. A book of only large movements has no contrast and no place for the reader to live.",
                "Decide the series-level shape before the volume-level one when the story is long: what each volume promises and keeps, and what is reserved for later.",
            ],
            "prophecy_and_agency": [
                "If the world contains prophecy or fate, decide what it can and cannot do: a prophecy that settles outcomes removes the protagonist's choices, so it must be ambiguous, conditional, or misread.",
                "Let the protagonist act inside the prophecy's terms rather than waiting on them, so the ending is a decision and not an announcement.",
                "Keep the counter-position alive: someone who believes the fate should be refused or redirected, with reasons the reader can follow.",
            ],
        },
        "problems": [
            {
                "id": "world_before_story",
                "frames": [
                    "The world is doing the work that the story should be doing.",
                    "You have a continent of material and no one whose problem it is.",
                    "The setting keeps expanding and the trouble stays general.",
                ],
                "context": "A world is not a story until it costs someone something specific.",
                "stages": ["the first statement of the idea", "the planning of the world's rules", "the decision about who the book follows"],
                "openers": [
                    "Start from a person under an obligation and let the world surface where it obstructs them. The reader learns the world by watching someone work inside it, and every piece of the world then earns its place by making the story's problem harder.",
                    "Reduce the world to the three facts that constrain the protagonist, and make the rest of the invention serve those. A world is legible through its pressures, not through its inventory.",
                ],
                "closers": [
                    "Commit to the world's costs, its scarcities, and the one condition that makes the story inevitable, and keep everything else in the notes.",
                    "Fix what the world makes expensive for this person, then build outward from there.",
                ],
            },
            {
                "id": "power_without_price",
                "frames": [
                    "The magic solves problems as fast as the plot creates them.",
                    "Your powers have rules and no costs.",
                    "Every crisis in the plan has a convenient capability standing next to it.",
                ],
                "context": "Power without a price is a genre trap: it ends tension rather than generating it.",
                "stages": ["the design of the world's rules", "the escalation of the middle", "the arrangement of the ending"],
                "openers": [
                    "Attach a cost to every capability the plot depends on: time, health, obligation, memory, a bond, a debt. The cost should be payable before the benefit, so the reader watches the choice rather than the result.",
                    "Give the protagonist's own power the most painful price. The book's best scenes come from the moment the power is available and expensive at once.",
                ],
                "closers": [
                    "Commit to costs that bind: magic that takes something back, and a protagonist who pays before the story hands them anything.",
                    "Decide the price list before the power list, and hold both fixed across the book.",
                ],
            },
            {
                "id": "scale_without_person",
                "frames": [
                    "The stakes keep growing and the reader's grip keeps loosening.",
                    "The middle is a sequence of armies and no one's particular life.",
                    "The ending's stakes are larger than anything the reader has personally watched.",
                ],
                "context": "Scale only moves a reader when it arrives through something small and specific.",
                "stages": ["the planning of the middle", "the design of the climax", "the escalation of the final movement"],
                "openers": [
                    "Translate each escalation into a private cost before staging the public event: the siege is also the week someone's family runs out of options. The pattern is one large movement, one small consequence, deliberately paired.",
                    "Anchor the scale to a limited number of lives. A reader can hold a household, a squad, a village; the world has to be carried through them.",
                ],
                "closers": [
                    "Commit to pairing each large event with a personal cost the reader has already been made to care about.",
                    "Decide who pays for the scale, in every movement, before deciding how large it gets.",
                ],
            },
        ],
        "traps": [
            {
                "id": "lore_opening",
                "frames": [
                    "The book opens on the world's history and its powers.",
                    "You are arranging the first chapters and the setting keeps arriving before the trouble.",
                    "You want the reader to understand the world before anything is asked of anyone.",
                ],
                "slide": "The opening establishes the world, its history, and its powers before anything is demanded of a single person in it.",
                "stages": ["the drafting of the opening chapters", "the arrangement of the first movement", "the plan for how the world is taught"],
                "openers": [
                    "Open inside a cost that is already running: someone is short of something, late for something, owed something, or afraid of something specific. The reader learns the world by watching a person work inside it, and the history can arrive later, attached to a choice.",
                    "Give the first chapter a person with a problem the world makes harder, and let the setting surface where it obstructs them.",
                ],
                "damage": "The reader is asked to memorize before being given a reason to care, so the book spends its cheapest attention on material that would have been interesting later, when it explained something that had already happened.",
                "reason_past": "Reason past it while planning the opening by deciding what the reader must feel by the end of the first chapter, and placing only the world's facts that produce that feeling. Everything else waits for a scene that needs it.",
                "closers": [
                    "Commit to an opening that runs on a person's problem, with the world introduced through what it costs them.",
                    "Fix the first chapter's pressure, then decide which three facts about the world that pressure requires.",
                ],
            },
            {
                "id": "chosen_one_default",
                "frames": [
                    "The protagonist's importance comes from a prophecy the reader has just been told about.",
                    "You are deciding why this person is at the center of the story.",
                    "The plan keeps reaching for fate to explain why the protagonist matters.",
                ],
                "slide": "The protagonist is the foretold one, and their centrality is established by destiny rather than by anything they do or owe.",
                "stages": ["the casting of the protagonist", "the design of the antagonist", "the arrangement of the ending"],
                "openers": [
                    "Make the protagonist's involvement the consequence of a choice they made or an obligation they carry, so their presence in the story is something they can be held to. Belief in a fate can stay, held by other characters, which keeps the world's prophecy while returning the story to a person.",
                    "Swap appointment for debt: the protagonist is here because of something they did, owe, or broke, and the ending will collect on it.",
                ],
                "damage": "Destiny does the work that character should do. The protagonist's choices stop mattering because the ending is guaranteed, and every ally's loyalty becomes a fact about prophecy rather than a decision about a person, which drains the cast of stakes.",
                "reason_past": "Reason past it from the ending backward: decide what the protagonist must choose for the ending to be theirs, then build the earlier chapters so that choice is available and expensive rather than foretold.",
                "closers": [
                    "Commit to a protagonist whose presence is an obligation, and let any prophecy in the world be something believed rather than something guaranteed.",
                    "Settle what the protagonist owes and what choosing costs them, then build the fate talk around it.",
                ],
            },
            {
                "id": "quest_by_itinerary",
                "frames": [
                    "The middle is a list of destinations, each with its own obstacle.",
                    "You are structuring the long journey and each stop resolves itself.",
                    "The plan advances by travel rather than by consequence.",
                ],
                "slide": "The middle moves from location to location, each one supplying an episode that resolves inside itself before the story moves on.",
                "stages": ["the planning of the middle", "the design of the journey", "the escalation of the second movement"],
                "openers": [
                    "Give the journey a cost that accrues across stops: the thing being carried degrades, the group loses something it cannot replace, the destination's meaning changes with what they learn. Progress then has a price measured against something the reader was shown at the start.",
                    "Tie each stop to the previous one causally rather than geographically: they are here because of what happened there, and leaving costs something they will miss later.",
                ],
                "damage": "The story reads as a tour. Nothing accumulates between episodes, the relationships reset each time the scenery changes, and the ending depends on the itinerary finishing rather than on anything the characters chose, so the climax arrives as an appointment.",
                "reason_past": "Reason past it by keeping one ledger across the whole journey: what has been spent, who has left, what is now impossible. Every stop should change that ledger, and the ending should be decided by it.",
                "closers": [
                    "Commit to a journey whose stops cost the group something that survives into the next chapter.",
                    "Decide what degrades, what is lost, and what becomes impossible across the middle, and hold those losses.",
                ],
            },
        ],
        "discipline": [
            "Every scene should be legible to someone who has skipped nothing: who wants what, what it costs, and what changed.",
            "Hold the world's rules as fixed constraints on the same page as the plot's conveniences, and refuse the temptation to bend them for a scene.",
            "Keep the cast's number of names, factions, and places low enough that the reader can hold them, and let the map be as large as the story requires and no larger.",
        ],
        "themes": [
            {
                "id": "fantasy_promise",
                "frames": [
                    "You are planning an epic fantasy and need the book to promise the right experience.",
                    "You want the scale to land on a reader rather than wash over them.",
                    "You are deciding what an epic fantasy story looks like before writing it.",
                ],
                "question": "What does an epic fantasy story need in order to work, and how do you build the promise into the plan?",
                "openers": [
                    "An epic fantasy story is built on three commitments: a world whose powers are priced, a protagonist drawn into a conflict larger than their preference, and consequences that arrive at the level of people the reader has watched. Structure that keeps all three produces the genre's characteristic experience of scope carried by intimacy.",
                    "The genre promises bigness felt personally. That promise is kept by architecture rather than by description: the world's rules create costs, the costs create choices, the choices create the escalation, and the escalation is paid by a small, specific cast.",
                ],
                "middles": [
                    "Decide the scale of the conflict and the size of the protagonist's life, then plan deliberately so the story's events reach that life in every movement.",
                    "Plan the power system, the political map, and the protagonist's obligation as one system rather than three: the power determines what is scarce, the scarcity determines the politics, and the politics determines what the protagonist owes.",
                    "Arrange the middle so the protagonist's competence grows while their situation worsens; growth without worsening produces a book where the ending is easy.",
                    "Keep the antagonist's case coherent: the opposition should want something a reasonable person in that world would want, and the protagonist should be able to name it.",
                ],
                "closers": [
                    "Commit to the promise: priced power, personal stakes, and an ending that costs the protagonist something they cannot recover.",
                    "Settle the world's pressure, the protagonist's obligation, and the shape of the ending's price before plotting the movements.",
                ],
            },
        ],
        "principles": [
            "Scale is carried by consequence, never by inventory.",
            "Every power in the world has a price the reader knows in advance.",
            "The protagonist's involvement is a choice or an obligation, not a destiny.",
            "The world's politics exist to make the protagonist's choices expensive.",
            "The ending costs something the protagonist cannot get back.",
        ],
    },
}

CAT = GENRE["CAT"]
