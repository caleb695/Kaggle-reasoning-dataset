"""Outline obedience, story state, and continuity across a whole novel."""

CAT = {
    "id": "continuity_outline",
    "label": "Outline obedience, state tracking, and continuity",
    "moves": {
        "obedience": [
            "Treat the outline as a constraint rather than as a suggestion. Every planned beat must survive into the draft in recognizable form; where a beat resists dramatization, find the staging that makes it work rather than substituting an easier event. A chapter that is excellent in itself and that spends material the book has not authorized is a structural liability.",
            "When the plan and the scene conflict, the resolution belongs to planning rather than to the page. Drafting is where decisions are executed, and changing a plot event mid-scene silently is how books acquire contradictions that no amount of later revision can tidy.",
        ],
        "state_ledger": [
            "Assemble the story state before drafting: injuries and recovery stages, possessions and who holds them, promises and to whom, secrets and exactly who knows them, capabilities and their limits, the current location and time, and the last significant exchange between each pair of characters present. The ledger is the difference between continuity and improvisation.",
            "Track knowledge separately for the reader and for each character. A character may act only on what they possess, and any scene requiring them to know something they were never given is a structural problem rather than a detail to smooth over in the prose.",
        ],
        "consequence_threads": [
            "Keep unresolved threads visible in the working notes: what was opened, where it was last touched, and what will close it. Threads tracked only in memory are the ones that quietly disappear, and a dropped thread teaches the reader that the book's promises are unreliable.",
            "Make each resolution follow from information established earlier. Coincidence, convenient discovery, and the arrival of exactly the right fact at the right moment all read as authorial rescue and discount the reader's investment in the story's logic.",
        ],
        "establishing_futures": [
            "When introducing something that will matter later, establish how it can matter: its capability, its cost, its owner, or the interest it attracts. A detail introduced without available consequence is either decoration or a promise the ending will have to improvise around.",
            "Plant at more than one appearance. A single mention is fragile, since the reader may not retain it and its later importance can feel assembled; two or three touches, each natural to its scene, build the detail into the story's furniture so the payoff lands as recognition.",
        ],
        "drift_control": [
            "Re-read the relevant earlier material before writing a chapter that depends on it, particularly when the dependence is on a conversation, a physical detail, or a decision from many chapters back. Distance in the context window is not distance in the reader's memory.",
            "Keep the operating rules of the world, abilities, and terminology stable, and locate any departure in something that happened on the page. Consistency before improvisation; where improvisation is genuinely required, convert it into a consequence that the story pays for rather than a rule that quietly changes.",
        ],
    },
    "problems": [
        {
            "id": "outline_pressure",
            "frames": [
                "A chapter you are drafting resists one of the beats the outline requires.",
                "The planned event in this chapter is dramatic but awkward, and an easier alternative is available.",
                "You are writing into a chapter whose required function conflicts with what the scene seems to want.",
            ],
            "context": "The outline's beats are obligations; a scene that writes more easily by replacing them has solved a drafting problem by creating a structural one.",
            "stages": ["the middle act", "the chapter before a major turn", "the sequence the outline marks as required"],
            "openers": [
                "Before drafting, separate the beat from its staging. The requirement is what the chapter must accomplish, not the specific scene you first imagined for it, and the freedom is entirely in the staging. Find the setting, the point of entry, and the character's private purpose that make the required beat the natural outcome of the scene's own pressure.",
                "Decide which of the chapter's obligations is non-negotiable and which are flexible in execution, then design the scene around the fixed one. Obstruction in the draft is usually the sign that the staging is wrong rather than that the plan is wrong, and the correct response is to change the frame rather than the event.",
            ],
            "closers": [
                "Write the chapter so that its required beat arrives as a consequence of the scene's own logic, and hold every planned event in place. Where the staging resists, change the staging and keep the obligation.",
                "Fix the required outcome, then draft the scene that produces it from inside the characters' wants rather than around it.",
            ],
        },
        {
            "id": "state_carryover",
            "frames": [
                "You are writing a chapter whose events depend on what happened several chapters ago.",
                "The current scene requires a character to be in a particular physical or emotional condition that was established earlier.",
                "You are drafting a sequence that depends on an object, promise, or secret from an earlier act.",
            ],
            "context": "Story state is a live ledger, and the chapter's behavior must reflect what the book has already spent or incurred.",
            "stages": ["the later middle of the book", "the sequence after an act break", "the chapter that pays off a setup"],
            "openers": [
                "Before drafting, assemble the state inventory for every character present: injuries in progress, possessions, obligations, what they know, and what they believe about each other. Then decide how each item on the inventory constrains the scene's options, which turns continuity from a memory task into a pressure source.",
                "Treat continuity as behavior rather than bookkeeping. A recovering injury changes what a character chooses to carry; a secret changes what they will agree to discuss; a debt changes who they can ask for help. Write the scene so the state shows up in decisions, and the reader feels the story accumulating.",
            ],
            "closers": [
                "Write the chapter with the state inventory applied to each scene's options, and update the ledger at the chapter's end with what changed. Continuity will then produce pressure rather than merely avoid errors.",
                "Draft the scene so that what the characters can and cannot do reflects the story's accumulated state, and let the constraint be visible in their choices.",
            ],
        },
        {
            "id": "payoff_grounding",
            "frames": [
                "You are approaching a payoff whose setup may be too thin to support it.",
                "You are drafting the chapter where a long thread resolves and the resolution is arriving suddenly.",
                "A reveal in your book depends on information the reader may not have retained.",
            ],
            "context": "The weight of a payoff must be supported by earlier deposits, and the reader's memory is the only ledger that matters.",
            "stages": ["the final act", "the chapter that resolves a thread", "the approach to the climax"],
            "openers": [
                "Before drafting the payoff, audit the setup: how many times the relevant material has appeared, how naturally it was placed, and whether a reader who was not looking for it would recall it. Where the audit fails, deepen the plant in an earlier chapter or reduce the payoff's weight, but do not proceed on the assumption that the reader remembers what the draft knows.",
                "Build the payoff on established capability, established knowledge, and established cost. When all three are in place, the resolution reads as inevitable; when any one is missing, the moment reads as authorial and the reader's trust in the story's logic is spent.",
            ],
            "closers": [
                "Write the payoff with the setup material deliberately recalled in the scene's own terms, and with the resolution following from what was established rather than from what the plot requires.",
                "Ground the resolution in earlier material that the reader has already seen used, and let the payoff be recognition rather than news.",
            ],
        },
    ],
    "traps": [
        {
            "id": "silent_plot_rewrite",
            "frames": [
                "Your draft is quietly changing a planned plot event to make a scene easier.",
                "You are drafting a chapter and the outline's required beat is being replaced by a more convenient one.",
                "The scene you are writing would be stronger with a different outcome than the plan specifies.",
            ],
            "slide": "The rewrite happens gradually: a beat is softened, an outcome is reversed, a character who was meant to stay absent appears. Each change is defensible in isolation, and the accumulation is a book that no longer matches its own plan, with consequences upstream that the later chapters still expect.",
            "stages": ["the middle act", "the chapter after a difficult scene", "the sequence the outline marks as a turn"],
            "openers": [
                "You can feel the scene negotiating with the plan, and the negotiation is easy to mistake for discovery. Refuse it while drafting: if the plan is wrong, that is a planning decision to make deliberately and in full, not a drafting decision to make silently.",
                "The pull is toward the better scene at the cost of the planned event. Reason past it now by asking what later chapters require, since those requirements were built on the outline's version of this moment.",
            ],
            "damage": "Silent rewrites create contradictions that surface much later as impossible situations, and they break the causal chains that other chapters depend on. The damage is also expensive to repair retrospectively, because by the time the contradiction appears, several chapters have been built on the substitution.",
            "reason_past": "Reason past it by separating the obligation from the staging: keep the required outcome and rebuild the scene around it. Where the plan itself is genuinely wrong, revise the plan explicitly and propagate the change to every chapter that depends on it.",
            "closers": [
                "Write the required beat and change the staging until the scene works. If the plan must change, change it deliberately and reconcile the downstream chapters before drafting further.",
                "Hold the outline's obligation in place and treat the scene as the variable.",
            ],
        },
        {
            "id": "forgotten_thread",
            "frames": [
                "A thread you opened several chapters ago has not been touched since.",
                "You are drafting a chapter and an earlier promise or clue is being ignored.",
                "The story's middle is filling with new material while older obligations go unpaid.",
            ],
            "slide": "New material is more interesting than old obligations, so the middle grows fresh incidents while threads from the first act quietly fall out of the book entirely. It feels productive while drafting because the pages are filling.",
            "stages": ["the middle of the book", "the chapter after an act break", "the planning of the next sequence"],
            "openers": [
                "You can feel the draft preferring new material to old obligations. Refuse the drift: run the thread list against the last several chapters and identify what has gone unpaid, then schedule its renewal before generating more.",
                "The pull is toward novelty, and the cost is the story's promise ledger. Reason past it by treating every open thread as a scheduled obligation with a renewal point rather than as a note the book can outgrow.",
            ],
            "damage": "Dropped threads convert the story's accumulated promises into noise, and readers who have been holding a question for two hundred pages are being told that their attention was misplaced. It also costs the ending its material: an unpaid thread cannot be part of the climax, so the final act arrives with less to gather.",
            "reason_past": "Reason past it by maintaining a thread ledger with renewal points and by refusing to open new threads faster than the book can service them. Renewals should deepen the thread rather than repeat it, so the middle stays productive as well as honest.",
            "closers": [
                "Write the renewal of the neglected thread into the current stretch, deepening rather than repeating it, and update the ledger with its next touch.",
                "Bring the unpaid obligation back into play now, before adding new material, and let it carry some of the chapter's work.",
            ],
        },
        {
            "id": "context_amnesia",
            "frames": [
                "Your later chapters contradict details established earlier in the book.",
                "You are drafting a scene and cannot recall the exact physical description, conversation, or decision it depends on.",
                "The book's terminology and rules are shifting from chapter to chapter.",
            ],
            "slide": "Writing at distance, the draft reconstructs earlier material from memory and gets the details approximately right: a scar on the wrong side, a promise slightly different, a character's habitual response inverted. Approximation feels acceptable because the difference is small, and it accumulates into a book that disagrees with itself.",
            "stages": ["the third act", "a long drafting session", "the chapter that calls back to an earlier scene"],
            "openers": [
                "You can feel the draft relying on recollection. Refuse it: re-read the specific earlier passages this chapter depends on before writing, and keep the state inventory open beside the draft so the details are available rather than remembered.",
                "The pull is toward continuity by memory, which is unreliable at exactly the distances that matter. Reason past it by checking the source rather than the recollection, especially for conversations, physical facts, and the exact wording of promises.",
            ],
            "damage": "Contradictions of detail damage the reader's trust disproportionately, because they are verifiable and because they suggest the book does not know its own story. They are also the most expensive defects to repair at the end, since every affected passage has to be reconciled by hand.",
            "reason_past": "Reason past it by maintaining the story bible as a live document and by consulting it at the start of every chapter rather than at the end of the draft. Consistency before improvisation, and a check before an assumption.",
            "closers": [
                "Write the chapter with the earlier material open and the ledger current, and reconcile every detail against the source as it is used.",
                "Verify rather than recall, and update the bible with whatever this chapter establishes for later chapters to depend on.",
            ],
        },
    ],
    "discipline": [
        "Before each chapter, assemble the story state, the open threads, and the knowledge positions of everyone present, and note the three details the chapter must not contradict.",
        "During drafting, keep the chapter's obligations visible and treat every deviation from the outline as a planning decision that must be made explicitly rather than adopted silently.",
        "After each chapter, update the ledgers: state changes, new threads, ring changes in who knows what, and the next renewal point for every open obligation.",
    ],
    "themes": [
        {
            "id": "state_architecture",
            "frames": [
                "You are planning how a long novel will maintain consistency across hundreds of pages.",
                "You want continuity to function as structure rather than as a repair task.",
                "You are deciding what tracking systems the book needs before drafting begins.",
            ],
            "question": "How should state, knowledge, and obligation tracking be designed as part of the book's architecture rather than managed as a maintenance burden?",
            "openers": [
                "Continuity is architecture, not hygiene. Design the tracking before drafting: character sheets with current condition and knowledge, a thread ledger with setup and payoff positions, an object and possession inventory, a chronology, and a rules sheet for the world's mechanics. Each becomes a pressure source, since a constraint the book respects generates plot.",
                "Plan knowledge as a map rather than a list. For each secret in the book, decide who knows it, when each of them learned it, what they believe about who else knows, and what each would do if they found out more. The map produces scenes, while a secret tracked as a single fact only produces a reveal.",
            ],
            "middles": [
                "Schedule the renewals of long threads the way scenes are scheduled, so that the middle of the book has obligations to service rather than only new material to generate.",
                "Keep commitments from characters to each other in the same ledger as plot facts. Promises, agreements, and debts are the most reliable source of later scene pressure, and they are the easiest obligations to lose.",
                "Maintain a recovery schedule for physical and emotional damage. What the characters cannot do is as structural as what they can, and the schedule keeps the book's costs visible across acts.",
                "Review the ledgers at act boundaries and use the review to plan the next act: what must be paid, what must be renewed, and what the accumulated state now makes possible.",
            ],
            "closers": [
                "Commit to the tracking systems as working documents and treat the book's accumulated state as the material of every later chapter. Continuity maintained this way stops being a correction and becomes an engine.",
            ],
        },
    ],
    "principles": [
        "Outline before improvisation: the plan's obligations are structural, and any genuine change to them belongs in planning rather than in a scene.",
        "State before scene: what the story has already spent and established constrains what the chapter can do, and the constraint is a source of pressure.",
        "Established before resolved: every major resolution should follow from material the reader has already seen used.",
    ],
}
