"""Idea shaping: turning a premise into a story that can carry a book.

Where `idea_generation` is about finding an idea with an engine at all, this
library is about the next move: choosing whose story it is, generating conflict
and stakes, deciding the promise and the ending's direction, and compressing the
whole thing into a pitch that exposes whether it holds.
"""

CAT = {
    "id": "idea_shaping",
    "label": "Idea shaping: protagonist, conflict, stakes, promise, pitch",
    "moves": {
        "protagonist_choice": [
            "Choose the protagonist by asking whose life the premise damages most, not who would investigate it. The person with the least ability to walk away generates the most scenes, and the person with the most competence generates the least pressure.",
            "Audition two or three members of the situation before deciding. For each, ask what they want, what they would refuse to do, and what the premise takes from them; the one whose answers are most specific and most costly is the protagonist, and the others become the cast.",
            "Give the protagonist a stake in the outcome that exists before the story's problem arrives: an obligation, a debt, a person, a reputation. Characters who enter a situation with nothing already at risk spend the first act acquiring a reason to care, which is the weakest possible opening.",
        ],
        "want_and_need": [
            "Separate what the protagonist wants from what they need, and make the want concrete enough to be photographed: a thing, a person, a status, a place. The need is what the story's pressure will reveal to them, and the gap between the two is the engine of the middle.",
            "Give the want a deadline and a cost of failure. A want without a clock produces a book that can always start tomorrow, and a want without a price produces a goal the reader cannot weigh. Both are decisions made at the idea stage rather than discovered while writing.",
            "Let the want be active: something the protagonist pursues rather than something they wait to receive. Pursuit generates scenes, and waiting generates scenes for other characters to interrupt.",
        ],
        "conflict_generation": [
            "Generate conflict by giving the opposition a legitimate claim on the same thing. The strongest antagonism is two people who want the same scarce thing for reasons the reader can follow on both sides, which makes every confrontation a question rather than an obstacle course.",
            "Build opposition into the world rather than into a single villain: a law, a debt, a custom, a shortage. Structural opposition cannot be defeated in one scene, cannot be reasoned with, and keeps producing pressure while the cast is doing something else.",
            "Place the antagonist's pressure on the protagonist's private life rather than only on the goal. When the opposition costs the protagonist the relationships they are not defending, the conflict stops being a contest and becomes a squeeze.",
            "Decide what each principal character would have to give up to get what they want, and make those sacrifices mutually exclusive across the cast. Mutual exclusivity is what turns a group of people with compatible goals into a story that forces choices.",
        ],
        "stakes_design": [
            "Make the stakes specific, personal, and weighable. A reader cannot hold a threatened kingdom, but they can hold one person's house, one promise, one job; build the large stake out of small ones that the reader has already seen the character protect.",
            "Escalate the currency of the stakes across the book: first external losses, then losses to relationships, then the protagonist's own self-account. Each rung of the ladder needs to be visible in the premise before the outline is built.",
            "Decide what the protagonist stands to lose that they cannot replace. Stakes become real when the thing at risk has no substitute, and the idea stage is where that thing is chosen rather than discovered at the climax.",
            "Keep one stake alive that is not the plot's business. A private cost running underneath the main problem keeps the middle interesting and gives the ending a second thing to pay.",
        ],
        "hook_and_opening": [
            "Design the opening as a promise rather than a beginning: the first pages should establish the kind of experience the book intends to deliver, the pressure the protagonist is under, and the question the reader will be holding. Everything else can wait.",
            "Open on the premise already in motion. The inciting event can arrive later, but the first scene should show the situation's ordinary pressure, so the reader learns the rules of the world by watching someone work inside them.",
            "Decide the first question the reader asks. A hook is not a shock; it is a question the reader wants answered, planted early and precise enough that the rest of the book can pay it.",
            "Give the opening a cost that the protagonist has already paid or is about to pay. Books that open on an intact character spend chapters undoing the intactness; books that open on a character already short of something start with pressure available.",
        ],
        "tone_and_promise": [
            "Decide the tone and hold it as a promise. A premise delivered in a comic register and answered in a tragic one is not a twist; it is a broken contract, and readers register the violation long before they can name it.",
            "Match the register to the pressure. Levity in a book about survival is not forbidden, but it has to come from character rather than from narration, and the decision about where the book allows humor belongs at the idea stage.",
            "Choose whether the book's mode is dread, curiosity, or sympathy, and let that choice govern the first chapter's material. Dread is built from what the reader knows and the character does not; curiosity from the reverse; sympathy from watching someone choose at a cost.",
        ],
        "ending_direction": [
            "Decide the shape of the ending before the plot: victory at a price, accommodation with the terms changed, loss with something preserved, or a return to a home that no longer fits. Each shape demands different material earlier, which is why the choice belongs at the idea stage.",
            "Ask what the protagonist will have to give up to get what they want, and design the ending as the moment that price comes due. Endings fail most often because the cost was never specified while the goal was.",
            "Choose the final image's work before its content: the ending has to demonstrate the change in one action or one image rather than state it. Deciding what that demonstration must prove is an idea-level decision.",
        ],
        "theme_stated_as_question": [
            "State the theme as the question the book's pressure will test, then assign each principal character a position on it. The theme becomes structural when the positions collide in action rather than in dialogue.",
            "Give the opposing position its best case, embodied in the most sympathetic character available. A theme that is only ever held by the antagonist is an argument the reader is being told to accept, not a question they are invited to hold.",
            "Let the theme cost the protagonist something they cannot argue away. When holding a position makes a character's life measurably worse, the book stops discussing the theme and starts testing it.",
        ],
        "pitch_compression": [
            "Compress the story into a few lines that contain a person, a want, an obstacle, a cost, and a turn. Anything that will not fit is either decoration or a gap, and the compression is a diagnostic rather than a marketing exercise.",
            "Say the idea out loud in one sentence and note where you hesitate. Hesitation marks the place where the story is not yet decided, and that place is the next decision rather than a problem with the sentence.",
            "State the idea's comparison points and ask what readers of those books would expect: the promise those comparisons make is the promise this book has to keep or deliberately refuse.",
        ],
        "candidate_selection": [
            "Generate several candidate versions of the idea before choosing one: the smallest version, the version with the antagonist as protagonist, the version set ten years later, the version where the protagonist has already lost. Comparison is what turns a preference into a decision.",
            "Choose among candidates by the engine rather than by the appeal: which version produces events without being pushed, which one has the highest escalation ceiling, and which one makes the ending expensive. Enthusiasm alone selects for setting.",
            "Keep the rejected candidates in the notes rather than discarding them. The version where the antagonist is the protagonist usually supplies the antagonist's motivation, and the smaller version usually supplies the opening.",
        ],
        "capacity_check": [
            "Test whether the premise can reach a novel's length without repeating itself. A premise with one crisis and no accumulating cost is a short story, and the fix is to add capacity: a deadline, a second front, or a price that grows while the protagonist works.",
            "Decide the ceiling of the idea's escalation. If the largest possible consequence is available in the first act, the book has nowhere to go, and the ceiling has to be raised at the idea stage rather than patched during drafting.",
            "Ask what happens to the story if the protagonist simply succeeds early, and if the answer is nothing, the idea needs a counterforce strong enough to keep the success from being available.",
        ],
    },
    "problems": [
        {
            "id": "wrong_protagonist",
            "frames": [
                "Your premise is vivid and the person you have chosen to follow is not the one it damages.",
                "The character at the center of the story is investigating the problem rather than living inside it.",
                "You have picked the most competent character rather than the most affected one.",
            ],
            "context": "The protagonist decides which scenes exist, so a poor choice here constrains every later stage.",
            "stages": ["the choice of protagonist", "the arrangement of the cast", "the opening chapter's design"],
            "openers": [
                "Reason from damage rather than from capability. List the ways this premise disrupts each person's life, the obligations each of them cannot abandon, and the cost each would pay by acting; the character with the most to lose and the least room to maneuver is the one whose story generates scenes.",
                "Audition a second candidate for the role and reason about the first act each choice produces. If one version produces a character who must act and the other produces a character who may act, the choice is settled on structural grounds rather than on preference.",
            ],
            "closers": [
                "Commit to the protagonist whose life the premise damages most and whose obligations prevent them from simply leaving, then reassign the others in the cast to the pressures that protagonist cannot supply.",
                "Choose the character, state what they stand to lose before the story begins, and build the opening from that loss rather than from their competence.",
            ],
        },
        {
            "id": "stakes_not_weighable",
            "frames": [
                "Your premise stakes are large and the reader has nothing to weigh them against.",
                "The story threatens a city and no one has shown the reader what one person's corner of it costs.",
                "Your stakes are stated at the level of the world rather than the level of a life.",
            ],
            "context": "Stakes become real in proportion to what the reader has watched the character protect, not in proportion to what is destroyed.",
            "stages": ["the definition of what is at risk", "the design of the first act", "the arrangement of the climax"],
            "openers": [
                "Replace scale with specificity. Decide the one thing the protagonist cannot replace, show it being protected early, and let the world-sized threat arrive through damage to that thing rather than beside it.",
                "Build the stakes out of a ladder the reader can climb: a job, a relationship, a reputation, a self-account. Each rung has to be established before it is threatened, and the ladder has to exist in the premise rather than be assembled during plotting.",
            ],
            "closers": [
                "Commit to specific stakes with a visible ladder, so the largest risk in the book is paid for by smaller risks the reader has already felt.",
                "Decide what the protagonist cannot replace and make it the currency of the story's pressure.",
            ],
        },
        {
            "id": "idea_without_capacity",
            "frames": [
                "Your idea is compelling and produces one crisis.",
                "The premise has a strong beginning and no accumulating pressure.",
                "You are trying to stretch a short-story idea into a novel.",
            ],
            "context": "A novel needs a cost that compounds while the protagonist works, not a single decisive threat.",
            "stages": ["the idea's capacity check", "the decision about scale", "the planning of the middle"],
            "openers": [
                "Add capacity rather than adding events. A deadline that cannot be extended, a second front the protagonist must defend, or a price that rises the longer they delay all generate chapters, whereas new incidents only reset the pressure.",
                "Reason about what the premise makes worse with time. Ideas that decay on a schedule produce long books; ideas that can wait produce short ones, and the repair is to put the protagonist's options on a clock.",
            ],
            "closers": [
                "Commit to a premise with compounding cost: one deadline, one rising price, and one front the protagonist cannot abandon while dealing with the other.",
                "Give the idea a clock and a growing bill, then plan the middle as the record of both.",
            ],
        },
        {
            "id": "want_without_obstacle",
            "frames": [
                "Your protagonist wants something and the story lets them pursue it without opposition.",
                "The obstacle in your premise is an inconvenience rather than a force.",
                "Your character's goal is achievable in the first chapter.",
            ],
            "context": "A want becomes a story only when something with its own agenda is standing in the way.",
            "stages": ["the design of the conflict", "the antagonist's arrangement", "the first movement's plan"],
            "openers": [
                "Give the opposition a claim on the same scarce thing, and give that claim a reason the reader can follow. The protagonist's obstacle should be someone else's legitimate pursuit, which converts a blocked goal into a collision of wants.",
                "Build structural opposition into the premise so the pressure cannot be resolved by one confrontation: a rule, a debt, a shortage, a custom. Then every scene has an obstacle that does not need to be scheduled.",
            ],
            "closers": [
                "Commit to an opposition with its own wants and its own means, and to at least one structural obstacle the protagonist cannot argue with.",
                "Design the obstacle so that removing it costs the protagonist something, and let the story's pressure come from that price rather than from the obstacle's size.",
            ],
        },
        {
            "id": "tone_break",
            "frames": [
                "Your premise promises one kind of experience and your plans deliver another.",
                "The book's register keeps sliding between comic and grave.",
                "You have not decided what the reader is supposed to feel while reading.",
            ],
            "context": "Tone is a promise the first pages make, and a book that changes it without earning the change loses the reader's trust.",
            "stages": ["the idea's tone decision", "the first chapter's design", "the arrangement of the cast"],
            "openers": [
                "Decide the mode and hold it: dread, curiosity, or sympathy, with a fixed allowance for humor and where that humor is permitted to come from. The decision constrains the first chapter's material and the narrator's distance.",
                "Reason about the tone the premise implies rather than the tone you enjoy writing. A premise whose central cost is irreversible carries a register that jokes in the narration will undermine, while the same premise can carry humor from the characters.",
            ],
            "closers": [
                "Commit to a mode and to the sources of levity inside it, and let the first chapter establish that contract so the rest of the book can be read against it.",
                "Fix the register now, and treat any later change of tone as a structural event the book has to earn.",
            ],
        },
        {
            "id": "ending_undecided",
            "frames": [
                "You are planning a book without knowing what its ending costs.",
                "Your premise could end several ways and you are postponing the choice.",
                "You know what happens and not what it means.",
            ],
            "context": "The ending's shape decides what the opening must establish, so leaving it open leaves everything upstream undecided too.",
            "stages": ["the ending's direction", "the first act's plantings", "the pitch of the book"],
            "openers": [
                "Decide the shape of the ending now: what the protagonist gains, what it costs, and what is left altered. Then check the premise for the material that price will require, and add whatever is missing before any structure is built.",
                "Reason backward from the last demonstration of change. The final scene has to prove the protagonist is not who they were, which means the premise must contain the trait that will be spent, and that is a decision rather than a discovery.",
            ],
            "closers": [
                "Commit to the ending's shape and its price, and to the opening material that makes both possible.",
                "Name what the protagonist gives up for the outcome, and let that price govern the middle rather than appear at the end.",
            ],
        },
        {
            "id": "single_candidate",
            "frames": [
                "You have one version of this idea and no basis for judging it.",
                "You are committed to the first version of the premise you wrote down.",
                "Your planning keeps adding details to a shape you have never compared to another.",
            ],
            "context": "An idea judged against nothing gets judged by its own elaborations, which always look like progress.",
            "stages": ["the idea's development", "the choice between candidates", "the pitch of the book"],
            "openers": [
                "Generate alternatives deliberately: the version with a smaller scope, the version where the antagonist carries the story, the version that opens after the disaster rather than before it. Each alternative exposes what the current version does and does not have.",
                "Reason against your own candidate before committing. Name the cheapest version of the story and the version that produces the most painful ending, then decide which of them the premise actually supports.",
            ],
            "closers": [
                "Choose among considered alternatives on stated grounds: engine, escalation capacity, and the cost of the ending.",
                "Commit to the version that produces the most pressure rather than the version that is most comfortable to imagine.",
            ],
        },
    ],
    "traps": [
        {
            "id": "premise_love",
            "frames": [
                "You keep adding to the premise instead of testing it.",
                "Your development sessions produce lore, history, and rules rather than people under pressure.",
                "You are defending the idea's central conceit against the story's needs.",
            ],
            "slide": "The premise is being expanded because expansion feels like progress. New rules, new factions, and new history arrive in place of decisions about who wants what, so the idea grows more intricate and no more story-shaped, and the first thing any outline has to do is invent the drama the development stage skipped.",
            "stages": ["the idea's development", "the capacity check", "the choice of protagonist"],
            "openers": [
                "The pull is affection for the conceit, and the correction is to test it against pressure. Reason at the level of who is damaged and what they want, and treat every element of the premise that cannot answer that as unavailable until it costs someone something.",
                "Reason past it by writing the story's smallest possible version: one person, one obligation, one collision inside this premise. If the small version works, the premise holds; if it does not, the elaboration is covering a hole.",
            ],
            "damage": "Premise-driven development produces books whose appeal is on the cover. The middle has no pressure to draw on because nothing was ever decided about the people, the escalation has to be invented during drafting, and the ending either arrives from nowhere or is replaced with a display of the conceit.",
            "reason_past": "Reason past it by requiring every premise element to name the pressure it creates for a specific person. Elements that cannot name one are demoted to texture, and the decisions that remain form the basis of the outline.",
            "closers": [
                "Commit to the premise only as far as it creates pressure, and to the people inside it as the book's actual subject.",
                "Reduce the premise to the smallest version that still produces the story, and build from that rather than from the full elaboration.",
            ],
        },
        {
            "id": "twist_before_story",
            "frames": [
                "You are building the idea around its reveal.",
                "The premise's appeal is what the reader will learn rather than what the characters must do.",
                "Your planning goes straight to the surprise and has not yet produced a middle.",
            ],
            "slide": "The twist is chosen first and the story is arranged to deliver it. Characters withhold for the sake of the reveal, the middle is engineered to look innocent, and the eventual discovery has to carry the whole book because nothing else in the plan has been given weight.",
            "stages": ["the idea's development", "the design of the mystery", "the arrangement of the middle"],
            "openers": [
                "Reason from the story the reveal has to disturb. Decide what the characters want and what they are doing when the truth lands, then place the reveal where it changes an action rather than where it produces the largest shock.",
                "Reason past it by building the middle first and letting the reveal serve it. A good twist changes the meaning of decisions already taken; a twist that only supplies information has to be carried by the book, rather than carrying it.",
            ],
            "damage": "Reveal-first books have thin middles and a final act that explains itself. Because the characters were arranged around withholding, their relationships never develop enough to make the reveal matter, and readers who guess early are left with nothing else to enjoy.",
            "reason_past": "Reason past it by giving every character a goal that the reveal will complicate rather than a secret that the reveal will expose, so the book works at both levels and the twist changes the stakes instead of replacing them.",
            "closers": [
                "Commit to a story that works without the reveal, with the reveal placed where it redirects decisions already in motion.",
                "Give the characters something to want that the twist will make harder, and let the middle develop that want.",
            ],
        },
        {
            "id": "borrowed_stakes",
            "frames": [
                "Your stakes come from the genre rather than from the characters.",
                "The world is in danger and the protagonist has no personal reason to care yet.",
                "You are raising the size of the threat instead of the cost to anyone in particular.",
            ],
            "slide": "The threat is inherited wholesale from the genre: the kingdom falls, the species ends, the city burns. Nobody in the story has a specific reason to be in its path, so the reader is asked to care about a number, and the protagonist's motivation has to be asserted rather than felt.",
            "stages": ["the design of the stakes", "the protagonist's setup", "the climax's arrangement"],
            "openers": [
                "The pull is toward scale, and the correction is toward attachment. Reason about what the protagonist has already protected, who depends on them, and what they would refuse to lose, then let the large threat arrive as damage to that rather than as a statistic.",
                "Reason past it by giving the protagonist a reason specific to their life: an obligation in the threatened place, a person they cannot evacuate, a debt that comes due with the disaster. The genre's stakes become vivid only through someone's private cost.",
            ],
            "damage": "Borrowed stakes produce competent books that move nobody. The middle has nothing to escalate except the size of the threat, the climax has to be louder than everything before it, and the ending cannot be personal because the risk was never personal to begin with.",
            "reason_past": "Reason past it while developing the idea by making the world's problem arrive through a private one. The reader learns what is at risk by watching one person lose something specific, and the large stake then has a scale the reader can hold.",
            "closers": [
                "Commit to stakes that start as a personal cost and grow into the world's problem rather than the reverse.",
                "Give the protagonist something in the path of the threat that they cannot replace, and let the scale of the threat be measured by it.",
            ],
        },
        {
            "id": "theme_debate",
            "frames": [
                "Your idea is a position and your characters are its examples.",
                "Your planning keeps returning to what the book is saying.",
                "Every character in your notes represents an opinion.",
            ],
            "slide": "The theme is decided and the story is arranged to illustrate it. Characters argue positions, the plot resolves into agreement, and the reader is shown a conclusion they were never in doubt about, which turns the book into a demonstration and the characters into evidence.",
            "stages": ["the idea's development", "the cast's arrangement", "the ending's design"],
            "openers": [
                "The pull is certainty, and the correction is to convert the position into a question with two expensive answers. Give the counter-position to someone the reader likes, and give the protagonist a reason to hold their own position that costs them something.",
                "Reason past it by making the theme arrive as consequence. Decide what the protagonist's belief causes in the plot, then let the story's pressure test it in action rather than in argument.",
            ],
            "damage": "Argumentative books are read as claims and judged as claims. The reader stops wondering what will happen and starts deciding whether they agree, the middle repeats the case in different registers, and the ending cannot move anyone because it was settled before the story began.",
            "reason_past": "Reason past it by giving the opposing position its best expression and letting the protagonist be wrong at a cost. A theme survives being tested and dies of being agreed with, and the testing is what the story's pressure is for.",
            "closers": [
                "Commit to a theme that is tested by action and to a counter-position with a real case behind it.",
                "Turn the position into a question, and let the protagonist's answer be a decision at the end rather than a stance at the beginning.",
            ],
        },
        {
            "id": "protagonist_indecisive",
            "frames": [
                "Your protagonist keeps deliberating and the story keeps waiting.",
                "The central character in your plan reacts to events rather than pursuing anything.",
                "Your protagonist is well observed and has no active want.",
            ],
            "slide": "The protagonist is drawn with care and given no appetite. They are observant, reasonable, and reactive, so other characters have to supply every turn, and the book becomes a record of things happening to someone rather than a story about someone doing anything.",
            "stages": ["the protagonist's design", "the want's definition", "the first movement's plan"],
            "openers": [
                "The pull is toward interiority, and the correction is toward appetite. Decide one thing this person wants badly enough to act against their own judgment for, then make the opening scene show them pursuing it. Character is legible through pursuit, not through reflection.",
                "Reason past it by giving the protagonist an intention that conflicts with the plot's demands. A character who wants something the story opposes has to act, and their actions generate the turns the middle needs.",
            ],
            "damage": "Reactive protagonists flatten a manuscript. The plot has to keep supplying events, the supporting cast does the deciding, and the ending has to be delivered to a character who never chose anything, which is why so many drafts end with a rescue or a revelation instead of a decision.",
            "reason_past": "Reason past it by making the protagonist's want the engine of the plan: every obstacle is measured against what they are trying to do, and every turn is a consequence of something they attempted. The character's interiority then colors the action rather than replacing it.",
            "closers": [
                "Commit to a protagonist with an active want and a willingness to act against their own comfort, and build the plan around their attempts rather than around events.",
                "Give the character something to pursue from the first scene, and let the story's pressure be made of the costs they accept in pursuing it.",
            ],
        },
    ],
    "discipline": [
        "Every idea decision should identify who pays and what they lose. Decisions without a payer are decoration, which is the failure mode of development rather than of drafting.",
        "Prefer the version that produces more pressure over the version that is more comfortable to imagine, and say the grounds for the choice out loud.",
        "Decide the promise, the protagonist, and the ending's price before the plot; structure derived from those three has a reason for every movement.",
    ],
    "themes": [
        {
            "id": "idea_to_story_pipeline",
            "frames": [
                "You have material and need a story, in that order.",
                "You want a repeatable way to turn an idea into something plannable.",
                "You are deciding how to move from a premise to a book without guessing.",
            ],
            "question": "How is an idea converted into a story that can be outlined, step by step?",
            "openers": [
                "The conversion has four moves and they are ordered: find the pressure the material creates, choose the person it damages most, give that person a want that costs them, and decide what the ending will take from them. Each move constrains the next, and skipping one produces a book that stalls at the stage it skipped.",
                "Developing an idea means deciding, in sequence, what the situation makes unavoidable, who is least able to avoid it, what they want badly enough to act, and what their acting will cost. The order matters because the later decisions are only possible once the earlier ones are fixed.",
            ],
            "middles": [
                "Generate candidates before committing. Write three versions of the premise: the smallest, the one that opens after the disaster, and the one where the opposing force carries the story. Comparison is how a preference becomes a decision, and the rejected versions supply material for the one that survives.",
                "Test the candidate against escalation. Ask what the worst consequence is that the premise can produce, whether that consequence is available in the first act, and what could raise the ceiling. Ideas that peak early have to be given capacity rather than incidents.",
                "Decide the ending's cost and work backward. What will the protagonist have to give up, what trait will they have to spend, and what must the opening establish so that spending it lands as a loss rather than as a change of mood.",
                "Compress the result into a pitch and treat the compression as a test. A person, a want, an obstacle, a cost, and a turn; anything that will not fit identifies a decision that has not been made, not a flaw in the sentence.",
                "Write down what the story is not. Deciding that this book is not about the faction war, not about the prophecy, and not about the father keeps the elaboration from returning during outlining.",
            ],
            "closers": [
                "Commit to the sequence: pressure, protagonist, want, obstacle, price, promise, and a pitch that fits in one breath. Everything that follows in the outline is derived from those decisions.",
                "Finish the conversion before planning anything. An idea that has been through these moves arrives at the architecture stage as a story rather than as material.",
            ],
        },
        {
            "id": "engagement_engine",
            "frames": [
                "You want readers to care about an idea that is interesting on paper.",
                "You are trying to identify what makes a premise gripping rather than merely clever.",
                "You want to build the book around the thing that holds attention.",
            ],
            "question": "What makes a premise engaging, and how is that quality built into the idea deliberately?",
            "openers": [
                "Engagement in a novel comes from three sources that can be designed: an unresolved question the reader wants answered, a person the reader wants to see succeed or fail, and a cost the reader can feel approaching. A premise that supplies all three produces momentum from the first chapter.",
                "A grip on the reader is made of anticipation rather than surprise. Reasoning about a premise means deciding what the reader will be waiting for, and making sure that thing is concrete, personal, and continuously threatened.",
            ],
            "middles": [
                "Make the protagonist's want concrete enough to be pictured. Abstract goals produce abstract suspense: the reader waits for a resolution they cannot visualize, and nothing that happens feels like progress or setback.",
                "Put something of the protagonist's in the path of the story's pressure. Care is built from the reader having watched someone protect a specific thing, and the shortest route to care is a small, ordinary vulnerability established early.",
                "Give the opposition a plan of its own with a timetable. Antagonism that only reacts to the protagonist creates episodes; antagonism with its own schedule creates a clock, and a clock is what makes a middle feel inevitable.",
                "Decide the intermediate questions the reader will hold while the large one is open. A book holds attention by managing a stack of smaller unanswered questions that are answered and replaced across the middle.",
                "Make the story's cost visible before it is charged. The reader needs to see the price to dread it, and the price has to be specific enough to be imagined rather than summarized.",
                "Choose an opening question the reader can repeat. If a reader cannot say what they are waiting to find out by the end of the first chapter, the hook has not been decided even if the scene is well built.",
            ],
            "closers": [
                "Commit to the engagement engine: a question the reader holds, a person whose want is pictureable, and a cost approaching on a clock. Everything else in the book arranges itself around those three.",
                "Build the premise so the reader's anticipation is the source of momentum, then check that each of the three sources is present before outlining anything.",
            ],
        },
    ],
    "principles": [
        "Pressure, then protagonist, then price: the decisions of the idea stage are ordered, and each one constrains the next.",
        "Specific beats spectacular: stakes a reader can picture hold attention better than stakes a reader can only measure.",
        "Decide the promise and the ending's cost before the plot, and let the structure be derived from both.",
    ],
}
