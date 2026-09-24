"""Arc mapping: designing the changes a novel is made of.

This library reasons about the shapes that run through a whole book: the
protagonist's change, the antagonist's campaign, relationship arcs, the
knowledge arc, the stakes ladder, act breaks, the climax, and the resolution.
It is the answer to the question of what the book is actually becoming while the
plot is happening.
"""

CAT = {
    "id": "arc_mapping",
    "label": "Arc mapping: character, antagonist, knowledge, stakes, and act design",
    "moves": {
        "protagonist_arc": [
            "Design the arc as a belief under pressure rather than as a personality change. Decide what the protagonist believes about how the world works at the start, what the story does to that belief, and what they do when it fails; the change is then visible in behavior rather than announced.",
            "Place the arc's proof in a choice, not a realization. Characters who understand something new and act the same way have not changed, and the plan should identify the decision at which the new understanding becomes expensive to honor.",
            "Decide whether the arc is positive, negative, or flat, and plan accordingly. A positive arc needs the belief to be wrong and costly to abandon; a negative arc needs it to be wrong and the protagonist to double down; a flat arc needs a protagonist who is right while the world around them is wrong, and each shape demands different pressure.",
            "Make the trait that opens the book become the liability that closes it. Competence, loyalty, or caution can carry a character through the first movement and be exactly what the final choice requires them to spend, and deciding that reversal early is what makes an ending feel designed rather than delivered.",
        ],
        "antagonist_arc": [
            "Give the opposition its own trajectory: an initial position, a campaign that escalates, and a cost it is willing to pay. An antagonist who only reacts to the protagonist has no arc, and an antagonist with no arc makes the book's pressure one-directional.",
            "Connect the antagonist to the protagonist's private life as well as their goal. Opposition becomes personal when it costs the protagonist the relationships and habits they are not defending, and the plan should schedule where those costs land.",
            "Decide what the antagonist wants and why the reader should understand it. Comprehension is not sympathy: the reader needs to be able to state the antagonist's case, and the plan should give it at least one scene in which it is nearly convincing.",
            "Plan the antagonist's reversals. A force that only gains ground is a weather system; a force that loses something and adapts is a character, and those adaptations are what keep a long middle from repeating its confrontations.",
        ],
        "relationship_arcs": [
            "Build relationship arcs in stages: alliance on terms, a test that reveals the terms were false, a rupture, and a renegotiation on different terms. Skipping the test produces a relationship that changes because the plot requires it to.",
            "Schedule the beats of a relationship against the main pressure rather than beside it. The best relationships in novels change at the moments when the plot is asking the most of both people, which converts a subplot into the book's emotional record.",
            "Decide what each relationship is for in the book's argument. A relationship carries the theme in a form the reader can feel, so the plan should know which pair demonstrates the question in a small way while the spine demonstrates it at full cost.",
        ],
        "knowledge_arc": [
            "Plan the knowledge arc from the reader's position rather than the characters'. For every revelation, decide what the reader knows, what they suspect, and what they are wrong about when it lands, since a reveal's effect is entirely a function of that state.",
            "Schedule the trail with the reveal rather than after it. Evidence planted before a disclosure turns a surprise into a recognition, and the plan should hold the position of each clue, each misdirection, and each false conclusion.",
            "Give characters different knowledge of the same events and let the differences cause action. Asymmetric knowledge is a plot engine: it produces mistakes, private decisions, and collisions that no external threat could arrange.",
        ],
        "stakes_ladder": [
            "Map the stakes as a ladder of currencies: physical losses first, then social and relational ones, then the protagonist's account of who they are. Changing currency is what keeps escalation from becoming volume, and the positions should be scheduled before the chapters are.",
            "Decide what each movement takes rather than what it threatens. Stakes that are only threatened accumulate without weight; stakes that are charged, in order, produce a book whose final act is genuinely expensive.",
            "Keep the largest stake unspent until the final movement and make it dependent on earlier losses. An ending feels earned when it costs the specific things the reader has watched the protagonist accumulate and defend across the middle.",
        ],
        "act_breaks": [
            "Design breaks as changes of condition rather than as pauses. A movement should end when the situation the protagonist is working in has changed, which gives the next movement a different problem rather than a continuation.",
            "Decide the midpoint reversal exactly: the moment when the protagonist's understanding or method is shown to be insufficient in a way that makes the goal harder. Middles that neither turn nor narrow produce chapters with the same job, which is what a sagging middle is.",
            "Choose the number of movements from the material rather than from convention. Two or four are legitimate; what matters is that each movement has its own question, its own escalation, and its own cost, and that the movement's ending is a loss the protagonist cannot undo.",
            "Plan the break after the midpoint to close doors. The third movement works best when the protagonist's earlier options are gone, which means the break should spend the resources, allies, or credibility that made the first half's approach possible.",
        ],
        "climax_design": [
            "Decide the choice at the center of the climax before deciding the events around it. The climax is where the book's question is answered by an action with a price, and everything else in the final movement is staging for that decision.",
            "Make the climax resolve the protagonist's arc and the plot's question in the same act. If the external problem is solved by one decision and the character's change is demonstrated somewhere else, the ending reads as two endings, and the plan should fuse them.",
            "Ensure the climax pays every thread the book opened. Threads that are left unpaid are experienced as loose ends regardless of intent, and the plan should list, before drafting, which threads converge and which are deliberately left open.",
        ],
        "mystery_and_clue": [
            "Design a mystery as a question with a fair trail rather than as information withheld. The reader should be able to assemble the answer from material already on the page, and the plan should hold the specific pieces and their positions.",
            "Plan the false solution as carefully as the true one. A misdirection works when it explains the evidence the reader has, which means it needs its own supporting material and its own reason to be believed.",
            "Decide what the mystery is for. A puzzle that resolves into information closes a question; a puzzle that resolves into a changed relationship or a decision it forces on the protagonist pays the book something the reader can feel.",
        ],
        "resolution_design": [
            "Decide what remains unresolved on purpose. Ambiguity works when the book has prepared the reader for an open ending, and reads as evasion when it arrives in place of a choice the plan avoided making.",
            "Keep the resolution proportional to the question. A long denouement for a small question drains the ending, and a rushed resolution for a large one leaves the reader holding a debt, so the plan should decide the scale of the aftermath in advance.",
            "Design the final image to demonstrate the change rather than describe it. The last scene should show the protagonist acting from who they have become, and the plan should know what that action is.",
        ],
    },
    "problems": [
        {
            "id": "flat_arc",
            "frames": [
                "Your protagonist ends the book as the person they started as.",
                "The plot resolves and the character is unchanged by it.",
                "Your plan tests the protagonist and never asks them to become different.",
            ],
            "context": "An unchanged protagonist makes the plot an event and the character a witness.",
            "stages": ["the protagonist's arc", "the midpoint's arrangement", "the climax's design"],
            "openers": [
                "Decide the belief the character starts with and the experience that makes it untenable. Then place two positions in the plan: where the belief first fails visibly, and where holding it becomes more expensive than abandoning it.",
                "Reason about what the protagonist must do differently at the end than they would have at the start, and work backward to the pressures that make the new behavior possible. The arc is a sequence of costs, not a sequence of feelings.",
            ],
            "closers": [
                "Commit to a belief, a series of pressures against it, and a final choice that demonstrates the change in action rather than in reflection.",
                "Give the protagonist something to spend: the trait that made them effective early becomes the thing the ending costs them.",
            ],
        },
        {
            "id": "antagonist_passive",
            "frames": [
                "Your opposition waits for the protagonist to act.",
                "Your antagonist has no plan and no timetable.",
                "The pressure in your plan only moves when the protagonist moves.",
            ],
            "context": "An antagonist who reacts rather than campaigns removes half of the story's engine.",
            "stages": ["the antagonist's arc", "the escalation ladder", "the middle's design"],
            "openers": [
                "Give the opposition a campaign with its own schedule: what it wants, what it does when nobody interferes, and what it does when the protagonist interferes. The protagonist's choices then interrupt a plan already in motion rather than starting one.",
                "Reason about the antagonist's losses and adaptations. A campaign that is repeatedly frustrated while still advancing keeps a long middle from repeating itself, and it makes each confrontation a consequence of the last.",
            ],
            "closers": [
                "Commit to an antagonist with a plan, a timetable, and at least two adaptations, and let the protagonist's middle be a series of collisions with it.",
                "Give the opposition its own scenes of progress, so the reader can feel a clock that the protagonist cannot stop.",
            ],
        },
        {
            "id": "reveal_without_trail",
            "frames": [
                "Your planned revelation depends on material the plan does not plant.",
                "The reader is meant to be surprised and has nothing to be surprised with.",
                "Your disclosure arrives at the end of the movement rather than being set up in the middle.",
            ],
            "context": "A reveal is experienced as recognition or as cheating, and the difference is entirely the trail.",
            "stages": ["the knowledge arc", "the middle's design", "the climax's arrangement"],
            "openers": [
                "Build the reveal backward: decide the disclosure, then place the evidence that makes it inevitable in retrospect, at least a movement before it lands. Each piece should be readable in two ways, one innocent and one true.",
                "Reason about what the reader will believe before the reveal and what they will reinterpret after it. If nothing in the middle changes meaning, the reveal is information rather than a turn, and the plan is missing its trail.",
            ],
            "closers": [
                "Commit to a trail with positions: the evidence, the misdirection that explains it, and the false conclusion the reader is invited to hold.",
                "Place the plants before drafting the chapters that pay them, and list the changes of meaning the reveal will produce.",
            ],
        },
        {
            "id": "climax_resolves_wrong_thread",
            "frames": [
                "Your climax solves the external problem and leaves the character's question untouched.",
                "The ending answers a question the book spent the middle not asking.",
                "Your final movement is about the plot and not about the protagonist's choice.",
            ],
            "context": "A climax that resolves the surface problem leaves the reader's main question unpaid.",
            "stages": ["the climax's design", "the arc's final movement", "the resolution's scale"],
            "openers": [
                "Identify the question the middle has actually been asking and rebuild the climax around a decision that answers it. The external resolution can be the setting for that decision rather than the point of it.",
                "Reason about the choice the protagonist must make that only they can make, and what it costs them relative to their starting belief. The climax is that decision, and the events around it are staging.",
            ],
            "closers": [
                "Commit to a climax that fuses the plot's question and the protagonist's arc in one action with one price.",
                "Answer the middle's question with a decision, and let the external resolution follow from that decision rather than substitute for it.",
            ],
        },
        {
            "id": "subplots_never_converge",
            "frames": [
                "Your subplots run alongside the spine without ever touching it.",
                "The secondary material in your plan stays secondary for the whole book.",
                "Your subplots resolve in their own scene and leave the main question alone.",
            ],
            "context": "Subplots that never intersect the spine read as interruptions regardless of their quality.",
            "stages": ["the subplot arrangement", "the convergence points", "the final movement's design"],
            "openers": [
                "Assign each subplot a point of contact with the main pressure: a chapter where it interferes, supplies, or costs something. Convergence should be scheduled, and the contact point is usually where the subplot's own question gets answered.",
                "Reason about what each subplot is testing. A subplot that tests the book's theme at a smaller cost earns its pages; a subplot that exists to rest the reader is a pause, and pauses belong inside chapters.",
            ],
            "closers": [
                "Commit to subplots with scheduled contact points, each one delivering a change the main line inherits.",
                "Reduce the subplot count to what the plan can converge on the spine, and place the convergences before the final movement so their costs are available to the ending.",
            ],
        },
        {
            "id": "stakes_plateau",
            "frames": [
                "Your plan raises the same kind of pressure in every movement.",
                "The middle keeps threatening the same thing at increasing volume.",
                "Your escalation is measured in size rather than in cost.",
            ],
            "context": "Escalation without a change of currency becomes noise the reader learns to discount.",
            "stages": ["the stakes ladder", "the movement design", "the third movement's arrangement"],
            "openers": [
                "Change the currency at each rung: physical risk, then relational cost, then the protagonist's self-account. Each change requires the plan to have established what is being threatened before it is spent.",
                "Reason about what the previous movement charged rather than what it threatened. Escalation means the protagonist begins each movement with less than they had, and the plan should record the balance.",
            ],
            "closers": [
                "Commit to a ladder that charges rather than threatens, with a different currency at each rung and a balance that falls across the book.",
                "Schedule what each movement takes, and let the final movement spend what the middle accumulated.",
            ],
        },
    ],
    "traps": [
        {
            "id": "arc_as_announcement",
            "frames": [
                "Your character's growth is delivered through statements about growth.",
                "The plan marks the arc with conversations in which the protagonist explains what they have learned.",
                "Your arc is legible in the outline summary and not in the decisions.",
            ],
            "slide": "The arc is written as commentary. Characters discuss their own development, supporting figures confirm it, and the change is marked in dialogue rather than in the choices that required it, so the reader is told about a transformation that the plot never made expensive.",
            "stages": ["the arc's design", "the climax's arrangement", "the resolution's scale"],
            "openers": [
                "The pull is toward legibility, and the correction is toward consequence. Reason about what the protagonist does differently at each stage, and remove the plan's announcements in favor of the decisions that demonstrate the change.",
                "Reason past it by giving the arc a price. If the growth costs nothing, it is a mood; decide what the protagonist must lose to become different and place that loss in the plan.",
            ],
            "damage": "Announced arcs read as unearned. Readers track what characters do, so a book that narrates its own transformation produces a protagonist whose change is asserted and contradicted by their behavior, and the ending feels like a claim the story never supported.",
            "reason_past": "Reason past it by testing the arc in action at three positions: the choice that shows the old belief, the choice where it fails, and the choice where the cost is paid. The commentary then becomes unnecessary and the change becomes visible.",
            "closers": [
                "Commit to an arc demonstrated in decisions, with each stage marked by what the protagonist does rather than what they say.",
                "Remove the arc's explanations from the plan and replace them with the choices that carry them.",
            ],
        },
        {
            "id": "escalation_by_inflation",
            "frames": [
                "Each movement in your plan introduces a larger threat than the last.",
                "You are solving flatness by adding power to the antagonist.",
                "Your ladder is measured in scale rather than in cost.",
            ],
            "slide": "The story escalates by enlarging the threat. A bigger enemy, a wider conspiracy, a larger disaster, none of which is connected to what the protagonist has lost, so the middle inflates while the reader's sense of risk stays flat and the plan eventually runs out of room to grow.",
            "stages": ["the escalation ladder", "the middle's design", "the final movement's arrangement"],
            "openers": [
                "The pull is toward magnitude, and the correction is toward cost. Reason about what the protagonist can no longer do at each stage rather than what is now facing them, and let the ladder be built from narrowing options.",
                "Reason past it by connecting each rise to the previous loss. A new threat that arrives as a consequence of the protagonist's earlier choice escalates the story; a new threat that merely arrives escalates the noise.",
            ],
            "damage": "Inflated stakes exhaust a book's credibility in its middle. The reader learns that the threats are interchangeable, the final movement has to manufacture something larger than everything before it, and the ending cannot be earned through escalation because the largest possible stake has already been spent.",
            "reason_past": "Reason past it by scheduling costs rather than threats, changing currency at each rung and keeping the highest stake unspent until the ending. The story's pressure then compounds instead of widening.",
            "closers": [
                "Commit to a ladder that charges rather than enlarges, with the largest cost reserved for the final movement.",
                "Measure each movement by what it took, and let new threats arise from the protagonist's own prior decisions.",
            ],
        },
        {
            "id": "twist_as_substitute",
            "frames": [
                "Your plan relies on a twist to make the third act work.",
                "The middle of your book exists to set up a reveal.",
                "You are counting on the ending to retroactively justify the book.",
            ],
            "slide": "The twist is carrying the structure. The middle is engineered to conceal rather than to develop, the characters hold their positions until the reveal, and the final act's job becomes explaining what the reader has already read instead of changing what they understand about it.",
            "stages": ["the knowledge arc", "the middle's design", "the resolution's scale"],
            "openers": [
                "The pull is toward the reveal, and the correction is toward consequence. Reason about what the twist changes about decisions already taken, and if the answer is only information, the plan needs development where the reveal currently sits.",
                "Reason past it by building the middle as though the twist did not exist: characters wanting things, failing, and paying. The reveal then lands on a story with weight and makes it heavier rather than supplying all the weight itself.",
            ],
            "damage": "Reveal-dependent books collapse under their own structure. Readers who guess early have nothing to enjoy, readers who do not feel manipulated, and the emotional arcs the middle never built cannot be created by the final explanation, which is why so many twist endings land as clever rather than moving.",
            "reason_past": "Reason past it by giving the middle its own escalation and its own costs, and by placing the reveal where it redirects an action the protagonist was already committed to. The twist becomes a turn inside a story rather than a replacement for one.",
            "closers": [
                "Commit to a middle that escalates on its own terms, with the reveal arranged to change the meaning of decisions already in motion.",
                "Make the story work without the twist, then place the twist where it costs the protagonist something.",
            ],
        },
    ],
    "discipline": [
        "Every arc should be expressible as a starting position, a pressure, and a final action. Arcs that cannot be stated that way are descriptions of mood.",
        "Schedule what each movement takes rather than what it threatens, and keep a falling balance across the book.",
        "Converge subplots on the spine and reserve the largest cost for the final movement; the ending is paid for by the middle rather than by the final chapter.",
    ],
    "themes": [
        {
            "id": "arcs_in_concert",
            "frames": [
                "You are designing several arcs at once and want them to reinforce each other.",
                "You want the plot's movement and the character's change to happen together.",
                "You are mapping the shapes that run through the whole book.",
            ],
            "question": "How do the parts of a story move together: what the protagonist wants, what opposes them, and what each of them learns?",
            "openers": [
                "Treat the arcs as a system with a shared clock: the plot's turns should occur at the moments when the protagonist's belief is failing, the antagonist is gaining, and the reader's knowledge is shifting. Designing the coincidence is what makes a book feel inevitable.",
                "The work at this level is alignment. Each movement should advance the plot and cost the character something, and each revelation should land where it changes a relationship as well as a fact, so a single scene does several jobs at once.",
            ],
            "middles": [
                "Decide the midpoint as an intersection: the moment when the plot's reversal, the character's false belief, and the reader's understanding all move at once. Middles that turn on one axis only have to fill the rest with incident.",
                "Map what each principal character wants at the start and how it changes by the end. Wants that stay constant while the plot moves produce a cast that reads as scenery, and the plan should record the shifts.",
                "Place the antagonist's gains where the protagonist's relationships are most exposed, so the opposition's progress costs the protagonist socially as well as materially.",
                "Give the theme a position in the arc map. Each movement should test the book's question at a higher cost, with the counter-position growing more plausible as the cost of the protagonist's belief increases.",
                "Schedule the resolution's requirements backward from the ending, so the last movement does not have to establish anything it needs. Everything the ending spends should have been placed before the midpoint where possible.",
                "Check that every arc has a cost attached to its resolution. An arc that resolves favorably and a plot that resolves favorably produce a book with no exchange rate, and the ending reads as a reward rather than a settlement.",
            ],
            "closers": [
                "Commit to the aligned map: plot turns, character costs, knowledge shifts, and stakes charges at the same positions, each movement ending with the protagonist worse off and better informed.",
                "Design the arcs so one scene can turn several of them, then plan the chapters around those intersections.",
            ],
        },
        {
            "id": "movement_design",
            "frames": [
                "You are dividing the book into movements.",
                "You want each part of the book to have its own shape rather than repeating the last.",
                "You are deciding how many turns the story needs and where.",
            ],
            "question": "How do you break a long story into movements, and what has to change by the end of each one?",
            "openers": [
                "Divide the book by changes of condition rather than by equal length. A movement ends when the protagonist's situation has changed so much that the previous method no longer applies, and the next movement begins with a different problem rather than a continuation.",
                "Give each movement a question, an escalation, and a cost. The question organizes the chapters, the escalation supplies the momentum, and the cost is what the next movement inherits; movements missing any of the three tend to sag or repeat.",
            ],
            "middles": [
                "Decide the movement's turn before its contents. Knowing what the protagonist loses at the end of the movement makes the preceding chapters a buildup toward a specific pressure rather than a sequence of events.",
                "Vary the movement's shape as well as its content: one may be a pursuit, another a siege, another a slow unraveling. Structural variety is what keeps a long book from reading as the same chapter repeated with new names.",
                "Place the revelations where they change the protagonist's options rather than where they are most dramatic. A fact that arrives after the decision it should have informed is a fact spent badly, and the movement map is where that misplacement is visible.",
                "Let the protagonist's method fail once per movement. The repeated failure of an approach, each time at a higher cost, is what makes the final movement's necessity feel structural rather than arbitrary.",
                "Reserve the movement after the midpoint for consequences. Once the protagonist's options have narrowed, the chapters work best when they show what the earlier choices have already spent.",
                "Decide what the reader is waiting for at the end of each movement, and make sure the next movement's opening does not answer it immediately. Anticipation is a resource the movement map is responsible for.",
            ],
            "closers": [
                "Commit to movements defined by change of condition, each with its own question, escalation, and cost, and to a final movement that spends what the middle charged.",
                "Plan the turns first, then fill the movements with chapters that build toward those turns.",
            ],
        },
    ],
    "principles": [
        "Arcs are sequences of cost: each movement should take something the reader has watched the character accumulate.",
        "Alignment is the point: plot turns, character costs, and knowledge shifts belong at the same positions.",
        "The ending is paid for by the middle, so schedule the charges before designing the climax.",
    ],
}
