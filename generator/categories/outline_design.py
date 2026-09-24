"""Outline design: turning a premise into an architecture that holds."""

CAT = {
    "id": "outline_design",
    "label": "Outline and story architecture design",
    "moves": {
        "movements": [
            "Define the movements by changes of condition rather than by sequences of events. A movement ends when the situation the protagonist is operating in has changed, not when a set piece is finished, and the change is what the next movement inherits.",
            "Give each movement a single question it is working on. The first movement asks whether the problem is real, the second asks what it will cost, the third asks what the protagonist will do about it, and the answer to each is provisional until the ending settles it.",
            "Let the turn between movements be a loss rather than an arrival. Moves that end in victory change the protagonist's capability, while turns that end in loss change their understanding, and only the second produces the pressure the later movements need.",
        ],
        "chapter_functions": [
            "Assign every chapter a function from a small set: establish, deepen, turn, pay, or delay with purpose. A chapter with two functions is usually fine; a chapter with none is the reason a middle feels long, and the fix belongs in the plan rather than in the prose.",
            "Write the chapter's obligation as a change: what is different at the end of this chapter that was not true at the start. Chapters whose obligation cannot be phrased as a change are transitions, and there is a limit to how many transitions a book can carry.",
            "Position chapters by what the reader should be waiting for when they begin. Anticipation is created, maintained, and discharged across the plan, and a chapter that neither opens nor closes a line of waiting is where attention drifts.",
        ],
        "thread_schedule": [
            "Settle the setup and payoff positions of every thread before writing any of them. A thread opened without a scheduled payment becomes a liability, and the reader's memory is the resource being spent to carry it.",
            "Intersperse threads so each one is left at a moment of pressure and returned to when it has developed. Alternation is what makes a long book feel continuous, and the decision about which thread the reader is holding at any point is a structural decision rather than a stylistic one.",
            "Keep the number of live threads within what the reader can hold. Two or three open lines generate expectation; six produce a book whose parts are individually interesting and collectively forgettable.",
        ],
        "escalation_ladder": [
            "Build the escalation as a ladder of currencies rather than a rising volume: physical, social, moral, and finally the protagonist's own identity. Changing the currency is what keeps a long middle from feeling repetitive, and the ladder has to be designed before it is climbed.",
            "Re-ground after each rise. Every new level of pressure should be shown to be within the world's rules and reachable from the previous one, or the reader stops trusting that the stakes are real and starts waiting to see what the book does next instead of what the character does.",
            "Decide in advance what the story will not spend until the end. A book that has used its largest threat by the midpoint has to invent something larger, and invented stakes read as inflation rather than escalation.",
        ],
        "ending_first": [
            "Decide the conditions of the ending before the events: what has to be true, what has to be lost, who has to choose, and what the choice costs. Then each earlier chapter can be positioned by what it deposits toward those conditions rather than by what it contains.",
            "Test the ending against the opening promise. If the honest version of the ending does not pay the promise the first chapter made, either the promise or the ending is wrong, and the correction is cheap here and expensive after drafting.",
            "Work backward from the final movement to define the minimum the book must establish. Everything that is not required by the ending is optional material, and identifying the required minimum is what makes a plan lean enough to hold pressure.",
        ],
        "subplot_convergence": [
            "Give every subplot a point at which it touches the spine. Subplots that never intersect the main pressure read as interruptions no matter how good they are, and the point of contact should be scheduled rather than hoped for.",
            "Let the subplot carry the theme the main plot cannot state. The spine delivers events and the subplot delivers the interpretation of them, which is how a book can be about something without anyone explaining it.",
            "Use subplots to test the protagonist's choices rather than to rest them. A subplot that exists so the reader can catch their breath is a pause, and pauses belong inside chapters rather than beside them.",
        ],
        "pressure_contour": [
            "Design the contour of the whole book: where it rises, where it rests, and where it crests. Rests are structural, not indulgence, and a book without them has no way of making its crests feel like crests.",
            "Alternate intensity with preparation rather than with relief. The chapter before a crest should tighten what is available, and the chapter after should show what the crest costs, which is how a sequence of highs becomes a curve rather than a list.",
            "Decide the book's quietest chapter deliberately. A well-placed low point deepens attachment and makes the last movement possible, and it is almost always more useful than another crisis.",
        ],
    },
    "problems": [
        {
            "id": "sagging_middle",
            "frames": [
                "Your middle movement has chapters and no pressure.",
                "The plan works at both ends and stops working in the long stretch between them.",
                "Your outline's second movement keeps producing variations of the same scene.",
            ],
            "context": "Middles sag when the plan carries events without carrying escalating costs.",
            "stages": ["the second movement's design", "the midpoint decision", "the mapping of chapters to functions"],
            "openers": [
                "Give the middle a question of its own rather than a continuation of the first act. The first movement asks whether the problem is real; the middle has to ask what the protagonist is willing to become in order to solve it, which is a different question with different scenes attached.",
                "Raise the price of the protagonist's method rather than the size of the threat. Middles hold when the approach that worked in the opening turns out to cost something, and they sag when the plan provides only more obstacles of the same kind.",
                "Decide the midpoint reversal exactly: the moment when the protagonist learns that their understanding of the situation was wrong in a way that makes the goal harder. Without it, the middle has no turn and every chapter has the same job.",
            ],
            "closers": [
                "Commit to a middle built on cost rather than on volume: a midpoint reversal, a method that becomes a liability, and a final movement that spends what the middle charged.",
                "Fix the middle by giving it its own question, its own turn, and its own price, and by letting the first act's momentum end where it should rather than dragging into it.",
            ],
        },
        {
            "id": "formula_scaffold",
            "frames": [
                "Your outline is shaped like a template with the specifics filled in.",
                "The plan keeps resolving into exactly the beats you expected it to have.",
                "You are defending the structure by citing its proportions rather than its effects.",
            ],
            "context": "A structure assembled from expected beats produces a book that reads as an outline of itself.",
            "stages": ["the movement design", "the chapter function map", "the ending's conditions"],
            "openers": [
                "Derive the structure from the story's own turning points instead of from expected proportions. Identify the decisions that change what is possible, place them where they need to be for the pressure to build, and let the shape be whatever those positions imply.",
                "Reason from effects rather than from counts: what must the reader be feeling and thinking at each stage, and what does that require the plan to have established? A structure derived from intended effects survives being read, and a structure derived from proportions is visible from a distance.",
            ],
            "closers": [
                "Commit to a structure whose beats exist because the story's pressure requires them, and let the proportions be an output of the design rather than an input to it.",
                "Build from required effects: anticipation at this point, reversal here, and a cost that lands at the end because the middle charged it.",
            ],
        },
        {
            "id": "unclosed_threads",
            "frames": [
                "Your plan keeps opening lines of interest and closing them vaguely.",
                "You have threads in the outline whose payoff is undecided.",
                "The outline is rich in setup and thin on payment positions.",
            ],
            "context": "Threads without scheduled payments become the reader's unfinished business, which is experienced as a flaw even when it goes unnoticed.",
            "stages": ["the thread schedule", "the mapping of chapters to functions", "the ending's conditions"],
            "openers": [
                "Write the payoff position beside every setup before drafting the first chapter. Threads are promises, and a plan that opens more than it schedules is accumulating debt with no repayment plan.",
                "For each thread, decide what changes when it is paid: an understanding, an allegiance, a state of the world, or a decision. Threads paid by revelation alone close information, and threads paid by choice close the story.",
            ],
            "closers": [
                "Commit to a schedule in which every thread has a setup position, a payoff position, and a change it delivers. Anything that cannot be scheduled is cut or demoted to texture.",
                "Reduce the thread count to what the plan can pay well, and place the payments where they do the most work for the final movement.",
            ],
        },
        {
            "id": "escalation_without_ground",
            "frames": [
                "Your plan raises stakes in every movement without re-establishing how the new pressure works.",
                "Each movement is bigger than the last and less credible than the last.",
                "You are escalating by adding threats rather than by raising costs.",
            ],
            "context": "Escalation requires the reader to understand the new pressure before it is applied.",
            "stages": ["the escalation ladder", "the third movement's design", "the final movement's conditions"],
            "openers": [
                "Establish the means before the threat. Every level of the ladder needs a scene in which the reader learns what the new pressure is capable of, and that scene belongs in the movement before the pressure is applied.",
                "Escalate by narrowing the protagonist's options rather than by enlarging the antagonist. A character with three options who loses one at a time generates more suspense than one confronted by a larger enemy, because the reader can compute what is left.",
            ],
            "closers": [
                "Commit to an escalation that changes currency, teaches each new pressure before applying it, and keeps the final threat unspent until the last movement.",
                "Plan the ladder so every rise is understood before it is felt, and so the book's largest cost arrives as a consequence of the middle rather than as an addition to it.",
            ],
        },
        {
            "id": "ending_unearned",
            "frames": [
                "Your planned ending is the one you want and the plan has not prepared it.",
                "The final movement resolves through material that was never established.",
                "Your ending depends on a decision the protagonist has not been built to make.",
            ],
            "context": "Endings feel earned when their conditions were deposited earlier, and arbitrary when they arrive on schedule.",
            "stages": ["the ending's conditions", "the third movement's design", "the first act's plantings"],
            "openers": [
                "List the conditions the ending requires and place each one's deposit in an earlier chapter. If a condition has no deposit, the ending is a decision imposed on the story rather than a consequence of it, and the repair is a planting rather than a rewrite.",
                "Check the ending against the protagonist's established character. The final choice has to be possible for who they have been shown to be and also costly for exactly that person, which usually means the trait that made them effective must become the thing they have to spend.",
            ],
            "closers": [
                "Commit to an ending whose every condition is planted, whose cost falls on the trait the protagonist has relied on, and whose payment matches the promise the opening made.",
                "Work backward from the ending until every requirement has a chapter responsible for it, then make those chapters' functions part of the plan.",
            ],
        },
    ],
    "traps": [
        {
            "id": "outline_as_event_list",
            "frames": [
                "Your outline is a list of things that happen.",
                "The plan describes events and not changes of condition.",
                "You are about to draft from a sequence rather than from a design.",
            ],
            "slide": "The outline reads as a schedule of incidents, each one clear and none of them connected by pressure. Events arrive, the protagonist responds, and the next event is queued, so the plan contains activity without escalation and each chapter competes with the last rather than building on it.",
            "stages": ["the outline's construction", "the mapping of chapters to functions", "the review of the plan before drafting"],
            "openers": [
                "The pull is toward incident, because incidents are easy to imagine and changes of condition require decisions. Reason past it by rewriting each outline line as a change: what is true after this chapter that was not true before, and what does that make possible or impossible.",
                "Reason past it by asking what each planned event costs the protagonist and what they lose by the time it is over. Events that cost nothing are texture, and a plan made of them produces a book that is busy and unmoving.",
            ],
            "damage": "Books drafted from event lists have middles that sag and endings that arrive rather than land. Each chapter has to justify itself with a bigger incident because nothing has accumulated, escalation becomes a matter of volume, and the final movement has to be louder than everything before it in order to feel like an ending at all.",
            "reason_past": "Reason past it while outlining by writing each chapter's obligation as a change of state and each movement's turn as a loss. The plan then carries pressure rather than activity, and the drafting stage inherits decisions instead of improvising them.",
            "closers": [
                "Commit to an outline where every chapter changes something and every movement ends with the protagonist in a worse or different position. Events become the vehicles of those changes rather than the point of the plan.",
                "Rewrite the plan as a sequence of conditions: what is true after each chapter, what it cost, and what it makes unavoidable next.",
            ],
        },
        {
            "id": "options_kept_open",
            "frames": [
                "Your plan keeps every possibility available for later.",
                "You are avoiding the commitment that would give the middle a shape.",
                "The outline is deliberately flexible about what the protagonist will do.",
            ],
            "slide": "The plan is kept general in the name of flexibility. The protagonist's central choice is unnamed, the antagonist's method is undecided, and the ending has alternatives, so every chapter is drafted without knowing what it is building toward and the book accumulates pages that each assume a different story.",
            "stages": ["the movement design", "the midpoint decision", "the ending's conditions"],
            "openers": [
                "The pull is toward keeping options, and the cost is that no chapter can be written with confidence. Reason past it by committing to the protagonist's central choice and the ending's conditions now, in the plan, and treating later changes as revisions rather than as the plan's fault.",
                "Reason past it by recognizing which decisions the drafting stage cannot make. Anything that determines the meaning of earlier chapters has to be decided in the outline, and the outline's value comes from the decisions it makes rather than the room it leaves.",
            ],
            "damage": "Undecided structures produce manuscripts with three possible books tangled in them: scenes that assume a redemption, scenes that assume a tragedy, and a final movement that has to choose among them at the point of maximum cost. The result is a book whose parts are better than its whole, and whose revision is a rewrite rather than a pass.",
            "reason_past": "Reason past it by naming the central choice and the ending's conditions in the plan itself, then reasoning forward to check that each chapter can be drafted with those decisions fixed. Commitment made early is what makes the drafting stage fast.",
            "closers": [
                "Commit to the protagonist's central choice, the antagonist's method, and the ending's conditions, and treat every chapter as written in the light of those decisions.",
                "Fix the load-bearing decisions in the plan, and let the drafting stage decide only what those decisions leave open.",
            ],
        },
        {
            "id": "outline_dictating_prose",
            "frames": [
                "Your outline specifies what each scene will look like on the page.",
                "The plan is detailed enough that drafting has nothing left to decide.",
                "Your outline dictates staging, dialogue beats, and imagery.",
            ],
            "slide": "The plan has grown into a draft in note form. Camera angles, reveal order, and line-level effects are all specified, so drafting becomes transcription and the writing cannot respond to what the scenes actually do, which is where a manuscript's best material usually comes from.",
            "stages": ["the outline's construction", "the review of the plan before drafting", "the chapter briefs"],
            "openers": [
                "The pull is toward completeness, and the correction is to specify decisions rather than executions. An outline should fix what each chapter must accomplish, what it costs, and what it leaves true, while leaving the staging to the moment of writing.",
                "Reason past it by asking, for each line of the outline, whether the drafting stage could decide it better with the scene in front of it. If the answer is yes, the line is planning the prose rather than planning the story.",
            ],
            "damage": "Over-specified plans produce flat manuscripts. The writing has no decisions left, so it cannot discover the particular behaviour, the telling detail, or the exchange that makes a scene feel inhabited, and the revision stage then has to invent life inside a structure that was designed as a transcript.",
            "reason_past": "Reason past it by keeping the outline at the level of purpose: obligations, costs, states, and positions. The drafting stage then inherits direction rather than instruction, and the decisions it makes in the scene are the ones only the scene can make.",
            "closers": [
                "Commit to an outline that fixes obligations and leaves execution open, and to chapter briefs that describe what must change rather than what must be seen.",
                "Keep the plan at the level of purpose. Everything the drafting stage can decide better with the scene in front of it belongs to the drafting stage.",
            ],
        },
    ],
    "discipline": [
        "Every structural decision should be expressed as a change of condition, a cost, or a position in the schedule. Structure that cannot be described that way is decoration.",
        "Decide the load-bearing choices in the plan. Anything that determines the meaning of earlier chapters cannot be left to be discovered while drafting.",
        "Work at one scale at a time and check the others after: movement, then chapter, then thread, then the whole shape.",
    ],
    "themes": [
        {
            "id": "architecture_scheduling",
            "frames": [
                "You are deciding the order in which the book spends what it has.",
                "You want an outline that produces pressure in every chapter rather than in the important ones.",
                "You are building a structure and want it to hold at every scale.",
            ],
            "question": "How should a novel's material be scheduled so that every chapter has a function and the ending arrives as a consequence?",
            "openers": [
                "Treat the outline as a schedule of pressure: what is planted where, what is paid where, what each chapter changes, and what the last movement is allowed to spend. Structure is the order in which a story spends its material rather than the sequence in which events occur.",
                "Architecture is the discipline of deciding positions. Once the ending's conditions are known, every plant, turn, and payoff has a position, and the outline is the record of those positions together with the reason each one is where it is.",
            ],
            "middles": [
                "Assign every chapter an obligation that can be checked: a change of state, a cost paid, a thread advanced, or a question sharpened. Chapters whose obligation cannot be checked are the ones that will be rewritten.",
                "Place the turns where they do the most work for the pressure rather than where they look symmetrical. A turn placed for shape is visible, while a turn placed where the protagonist's method has just failed is felt.",
                "Schedule the setup of everything the ending needs at least one movement before the ending, and prefer two. Anticipation is built by position, and the reader's memory of an early plant is what makes a late payoff land.",
                "Keep track of what the reader knows at each position in the plan. Most structural confusion is not caused by complexity but by the plan delivering information in an order that makes the events unreadable when they arrive.",
                "Let each movement end with the protagonist further from their original method of solving the problem. The book's forward motion is made of those losses rather than of victories, and the plan should show them in sequence.",
                "Decide what the plan will do at the two-thirds point, where books most often lose their pressure. That position needs either a new complication with a cost attached or the revelation that reframes the goal, and choosing it in advance is what prevents the middle from being padded.",
            ],
            "closers": [
                "Commit to the schedule: conditions for the ending, positions for every plant and payoff, an obligation for every chapter, and turns placed where the pressure requires them.",
                "Fix the positions and the reasons for them. The drafting stage then writes into a structure rather than searching for one.",
            ],
        },
        {
            "id": "theme_in_structure",
            "frames": [
                "You want the book to be about something without anyone saying it.",
                "You are deciding how the theme will be carried by the plan rather than by dialogue.",
                "You are designing a structure that has to argue with itself.",
            ],
            "question": "How is a theme built into a novel's structure rather than stated in its text?",
            "openers": [
                "A theme carried by structure is a pattern of pressure: the same test applied to different characters, the same mistake made at increasing cost, the counter-argument given its best scene. The plan embodies the question in what it makes people do.",
                "Deciding theme at the level of architecture means deciding what the book will repeatedly put its characters in a position to choose, and how those choices will differ in cost each time they recur.",
            ],
            "middles": [
                "Give the counter-position its own scenes and its own competence. A theme tested only against weak opposition produces agreement, and agreement is where a novel's argument stops being dramatic.",
                "Let the subplots carry the variations. The spine delivers the test at full price, while a subplot can deliver the same test at a smaller cost or from another angle, which is how a book accumulates meaning without repetition.",
                "Design at least one scene in which the protagonist's position is shown to be wrong in a way they cannot explain away. That scene is the difference between a theme that has been examined and one that has been asserted, and it belongs in the plan rather than in the revision.",
                "Make the resolution of the theme a decision rather than a conclusion. The final movement should force the protagonist to act on what they have learned, which is what converts a book's idea into its ending.",
                "Keep the theme out of the characters' mouths. If a character could state the book's question in one line, the plan has not yet found the action that embodies it, and the fix is structural rather than editorial.",
            ],
            "closers": [
                "Commit to a structure that tests the theme at increasing cost: the same question asked of different people, the counter-argument given its best case, and the answer delivered as a decision in the final movement.",
                "Build the theme into the shape of the pressure rather than into the text. The book will then be about something because of what it makes people do.",
            ],
        },
    ],
    "principles": [
        "Structure is a schedule of pressure: every plant, turn, and payoff has a position and a reason for that position.",
        "Every chapter changes a condition; a chapter that changes nothing is a transition, and books carry few of them well.",
        "Commit in the plan to everything that determines the meaning of earlier chapters, and leave execution to the writing.",
    ],
}
