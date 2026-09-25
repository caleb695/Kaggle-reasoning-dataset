"""Idea development: finding a premise that can carry a novel."""

CAT = {
    "id": "idea_generation",
    "label": "Idea development and premise design",
    "moves": {
        "engine_test": [
            "Test the material against the shape every story has: someone wants something, something stands in the way, and failing costs them. If the material cannot answer who wants what and what failure would mean, it is a situation rather than a premise, and the reasoning at this stage is to find the want rather than to decorate the situation.",
            "Look for the demand the idea makes: the thing the premise renders impossible to avoid. Premises that permit a character to walk away produce books whose first act is a negotiation with the plot, while premises that remove the exit produce books that start moving on their own.",
            "Decide what the idea makes expensive. A premise becomes a story engine when it prices the options: staying costs one thing, leaving costs another, and acting costs a third. If nothing in the material has a price, the reasoning has to create one before the book is planned.",
        ],
        "specificity": [
            "Replace the genre with a person. A book about a heist is a category; a book about the one member of the crew who has to decide whether to warn the target is a story, and the whole difference lives in the specificity of who is asked to pay.",
            "Ground the premise in a concrete situation rather than a concept: a place, an obligation, a date, a relationship already under strain. Concepts generate conversation and concrete situations generate scenes, and only one of them can be drafted.",
            "Prefer the narrow version. A premise that covers a decade and a continent has to be summarised before it can be dramatised; a premise that covers one week in one building can be written scene by scene. The narrow version is almost always the stronger book.",
        ],
        "promise": [
            "Decide what the idea promises the reader. Every book makes a promise in its first pages about the kind of experience ahead: a puzzle, a slow burn, a loss, a recovery. The promise is a contract, and the ending has to pay it rather than replace it with something the book prefers.",
            "Name the emotional destination before the events. Knowing whether the book ends in vindication, in accommodation, or in grief determines what the middle has to test, and a middle that tests nothing arrives at an ending the reader has not been prepared to accept.",
            "Make the promise specific enough to be broken. A premise that promises everything promises nothing, and its ending can only disappoint. The narrower promise is the one the book can deliver exactly, which is what makes an ending feel earned rather than adequate.",
        ],
        "forced_choice": [
            "Find the choice the premise will eventually force. The strongest ideas contain a decision that cannot be made well: two things the protagonist needs, only one of which can survive. That decision is the reason the book exists, and the plan should be built backward from it.",
            "Decide what is genuinely at stake in that choice, in a form the reader can weigh: a person, a promise, a claim about who the protagonist is. Stakes that cannot be named as alternatives are stakes the reader cannot hold, and the ending will feel abstract no matter how much is destroyed.",
            "Look for the point where the protagonist's own qualities become the obstacle. A book gains depth when the trait that made the character effective in the first act is the thing that makes the final choice unbearable, and that symmetry is usually visible already in the idea.",
        ],
        "collision": [
            "Combine two elements that complicate each other rather than two that complement each other. A setting plus a problem is a plot; a duty plus a desire that cannot both be honored is a story, and the friction between the elements is what generates scenes without being engineered.",
            "Look for the collision that makes ordinary competence insufficient. If the protagonist's existing skills solve the premise, the book has no pressure, and the repair at this stage is to add the element that makes their strengths part of the problem.",
            "Prefer the combination that costs the protagonist their support rather than the one that costs them their resources. Isolation is generative because it converts every later decision into a private one, which is where a novel's interior life comes from.",
        ],
        "theme_as_question": [
            "State the theme as a question the book will test rather than a conclusion it will deliver. Questions generate structure because every movement can be an attempt at an answer; conclusions generate argument, and argument in a novel usually arrives as a speech.",
            "Decide which side of the question the book is willing to take seriously. A theme that is tested only against its opponents is propaganda, and the strongest books are those in which the counter-position is embodied by someone the reader likes.",
            "Let the theme arrive through what the premise makes unavoidable rather than through what characters discuss. The theme is the pressure the idea applies to everyone in it, and it should be visible in what the characters cannot avoid choosing.",
        ],
        "character_pressure": [
            "Find the character who is worst served by the situation, and consider making them the protagonist. The most interesting person in the premise is usually the one whose life the situation damages most, not the one who investigates it.",
            "Decide what each principal character wants independently of the plot. Wants that exist outside the premise are what make a cast read as people, and they also supply the conflicts the outline will need when the main problem is temporarily quiet.",
            "Give the protagonist a competence the premise will not fully use. An ability that is established and then made insufficient is one of the most efficient ways an idea produces escalating pressure without new threats arriving.",
        ],
    },
    "problems": [
        {
            "id": "premise_without_pressure",
            "frames": [
                "Your premise is vivid and nothing has been asked of anyone yet.",
                "You have an idea that produces atmosphere and no decisions.",
                "You are developing material that could support a book about almost anything.",
            ],
            "context": "A premise without pressure is a setting, and a setting cannot generate a middle.",
            "stages": ["the idea's first statement", "the first planning pass", "the decision about whose story this is"],
            "openers": [
                "Find the demand inside the material. Ask what the premise makes impossible to leave alone, and if the answer is nothing, the reasoning has to add the element that removes the exits: an obligation with a deadline, a relationship that cannot be abandoned, or a price already partly paid.",
                "Decide what the situation costs a specific person per day it continues. Pressure in a novel is usually attrition rather than catastrophe, and a premise with a running cost generates chapters, while a premise with a single threat generates one confrontation.",
            ],
            "closers": [
                "Commit to a premise with a built-in demand: one person, one obligation, one cost that grows with time. Then the story is a question of how they bear it rather than whether anything happens.",
                "Write the premise in one sentence that includes who pays and what they lose by waiting. If the sentence cannot be written, the idea is still a setting.",
            ],
        },
        {
            "id": "engine_missing",
            "frames": [
                "You have a world and a cast and no event that must follow from them.",
                "Your idea explains itself well and produces no scenes.",
                "You are holding a concept that requires the plot to be invented on top of it.",
            ],
            "context": "An engine is whatever makes events necessary, and concepts do not contain one.",
            "stages": ["the shift from premise to plot", "the first outline pass", "the decision about the opening event"],
            "openers": [
                "Look for the event the world already implies. A setting with a rule, a hierarchy, or a debt contains events that must occur on schedule: an audit, a harvest, an inheritance, a hearing. Building the book from the system's own timetables is how concept becomes plot.",
                "Turn the premise's most interesting fact into a pressure on a person. Facts generate lore, and pressures generate scenes; the conversion is always the same and it is always about who is made to act because of the fact.",
            ],
            "closers": [
                "Commit to an engine: a rule of the premise that produces obligations, a character whose role puts them in the path of those obligations, and a clock that will not stop. Then plan events as consequences of the engine rather than inventions beside it.",
                "Settle the first event that the premise makes unavoidable, and build outward from it. The book begins where the idea stops permitting delay.",
            ],
        },
        {
            "id": "promise_undefined",
            "frames": [
                "You are about to plan a book without having decided what it promises the reader.",
                "Your idea could end several very different ways and the differences are not explored.",
                "You are unsure whether this book is a tragedy, a recovery, or an escape, and the structure will suffer for it.",
            ],
            "context": "The promise decides what the ending must be, and the ending decides what the middle has to do.",
            "stages": ["the idea's completion", "the decision about the arcs final movement", "the planning of the first chapter"],
            "openers": [
                "Decide the promise by choosing the emotional destination and then working backward to what must be true at the start. A book that promises recovery needs a character with something to recover; a book that promises loss needs one who has something worth losing, and the opening has to establish it.",
                "Name the experience the reader is being offered: a puzzle with a solution, a pressure that resolves, a relationship that changes, a place that is lost. Once named, the promise constrains the ending and the middle simultaneously, which is exactly what a plan needs from an idea.",
            ],
            "closers": [
                "Commit to a promise in one sentence, then check that the premise contains what the promise will need at both ends. Anything missing is a piece to add now rather than discover in the last act.",
                "Fix the promise and the price of the ending together. A book pays for its resolution with the character's earlier certainties, and the idea has to contain those certainties.",
            ],
        },
        {
            "id": "idea_sprawl",
            "frames": [
                "Your idea contains four books and a trilogy's worth of world.",
                "You are trying to include every interesting element of the material in one project.",
                "The premise is generous and the through-line is hard to find.",
            ],
            "context": "Sprawl at the idea stage becomes a manuscript that cannot decide what it is about.",
            "stages": ["the selection of the central line", "the decision about the cast", "the first structural pass"],
            "openers": [
                "Choose one line and let the rest become texture. A book is about a single pressure applied to a handful of people; everything else in the material is available as the world that pressure happens inside, and moving it to the background is not a loss but a clarification.",
                "Rank the material by how much the ending depends on it and keep only the top tier as plot. Anything that could be removed without changing the final decision belongs in the setting, the cast's histories, or the next book.",
            ],
            "closers": [
                "Commit to one through-line, one protagonist, and one unavoidable choice, with everything else demoted to setting or saved. The book is what remains after that decision, and it is stronger for it.",
                "State the book in a sentence that names one person and one problem. If other elements cannot be omitted from the sentence, the design work is not yet done.",
            ],
        },
    ],
    "traps": [
        {
            "id": "genre_as_idea",
            "frames": [
                "Your idea is currently described by its genre and its trappings.",
                "You are excited about a category of book rather than a specific one.",
                "The premise sounds like a shelf label with a cast attached.",
            ],
            "slide": "The genre and the world are doing the work the story should be doing. The premise is recognisable and compelling at a glance, and it contains no particular person with a particular problem, so every planning session produces worldbuilding instead of events.",
            "stages": ["the idea's statement", "the first outline pass", "the pitch of the book"],
            "openers": [
                "The pull is toward the recognisable shape, and the repair is specificity. Replace the category with a person and an obligation: not a heist in a clockwork city, but one crew member who has to decide whether to warn the man they are robbing.",
                "Reason past it by finding the concrete situation inside the category and building the idea from that instead. Genres are shelves, not stories; the story is the specific life the premise disrupts.",
            ],
            "damage": "Genre-shaped premises produce books that satisfy every expectation and surprise no one. The reader knows what happens next because the category says so, the characters act to service set pieces, and the ending arrives as the genre's ending rather than this story's ending, which is the difference between a book that is read and a book that is remembered.",
            "reason_past": "Reason past it while planning by refusing to write the premise sentence until it names a person, a want, and a cost. If the sentence works with the names removed, the book is a genre rather than a story, and the correction belongs here, before any structure exists.",
            "closers": [
                "Commit to the specific version: one person, one obligation, one cost, inside the recognisable world. The genre becomes the medium the book works in rather than the reason it exists.",
                "Build from the particular and let the trappings support it. The book will still be legible as its genre, and it will also be about someone.",
            ],
        },
        {
            "id": "theme_as_message",
            "frames": [
                "Your idea knows what it wants to say and cannot yet generate conflict.",
                "The premise is built around a conclusion you want the reader to reach.",
                "Your planning keeps returning to the theme rather than to the people.",
            ],
            "slide": "The theme is fixed and the characters are arranged to illustrate it. Opposition exists to be wrong, the middle repeats the argument in different registers, and the ending confirms what the first chapter already stated, so the reader is given an answer that was never in doubt.",
            "stages": ["the idea's completion", "the first structural pass", "the planning of the antagonist"],
            "openers": [
                "Convert the conclusion into a question the book will test, and give the strongest counter-position to someone sympathetic. The story then has somewhere to go, because a question can be probed while an answer can only be restated.",
                "Reason past it by finding what the theme costs a specific person. A position becomes dramatic when holding it makes someone's life harder, and that cost is the scene the idea is missing.",
            ],
            "damage": "Message-driven books read as arguments and are judged as arguments, which means the reader evaluates whether they agree rather than whether the story moved them. The characters become instruments, the middle becomes repetition, and the ending cannot surprise because it was decided before the situation existed.",
            "reason_past": "Reason past it by giving the opposition its best case and letting the protagonist be wrong in the first movement. A theme survives testing and dies of agreement, so the planning decision is to make the book an inquiry with consequences rather than a demonstration.",
            "closers": [
                "Commit to a question with two live answers, embodied in people rather than in dialogue. The theme will arrive as what the book's pressure forced, which is the only form that moves a reader.",
                "Hold the theme as a live question and let the ending answer it at a cost. Any position that costs someone nothing cannot be tested by a story.",
            ],
        },
        {
            "id": "world_as_substitute",
            "frames": [
                "Your planning keeps producing history, systems, and geography rather than events.",
                "The world is detailed and nobody in it wants anything urgently.",
                "Your idea's appeal is its invention, and the story is being built around it.",
            ],
            "slide": "The world is carrying the book. The setting is intricate and internally consistent, the exposition is already written in the notes, and the plot exists to tour it, so the reader is asked to admire a construction rather than follow a person under pressure.",
            "stages": ["the idea's development", "the first structural pass", "the design of the opening chapter"],
            "openers": [
                "The pull is toward elaboration, and the correction is to make the world cost somebody something. Take the single most interesting rule of the setting and ask who it damages this week, then plan from that person's problem rather than from the map.",
                "Reason past it by converting invention into pressure. Every element worth keeping should be able to answer what it makes difficult, expensive, or forbidden for the protagonist, and elements that cannot answer are background rather than story.",
            ],
            "damage": "Books built around their worlds produce readers who remember the setting and not the story, or who leave early because nothing has been demanded of anyone. Every chapter spent establishing the world is a chapter not spent creating anticipation, and no amount of internal consistency repairs a middle with no pressure in it.",
            "reason_past": "Reason past it while planning by starting from a person under an obligation and letting the world surface only where it obstructs them. The invention then earns its place by making the story's problem harder, and the reader learns the world by watching someone struggle inside it.",
            "closers": [
                "Commit to the world as the medium of the story rather than its subject: rules appear where they cost the protagonist something, and everything else stays in the notes.",
                "Choose the one invention the book cannot proceed without and make it the reason someone's week is ruined. The rest is setting, and setting is learned on the way.",
            ],
        },
    ],
    "discipline": [
        "Every idea decision should make the story more specific. If the reasoning could apply to a different book with the nouns changed, it has not decided anything yet.",
        "When the material is rich and the story is unclear, prefer narrowing. A smaller, more particular premise is easier to plan, easier to write, and easier to end well.",
        "Decide the promise and the price before the plot. Structure derived from a promise has a reason for every movement, and structure derived from events has to justify itself later.",
    ],
    "themes": [
        {
            "id": "idea_stress_test",
            "frames": [
                "You want to know whether this idea can carry a novel before committing months to it.",
                "You are deciding between two ideas and want to test them on grounds other than enthusiasm.",
                "You are about to commit to a premise and want to know where it will fail.",
            ],
            "question": "How do you tell whether an idea can carry a whole book before you commit to writing it?",
            "openers": [
                "An idea has to survive four questions before it can be planned: what does the premise make impossible to avoid, who pays for it, what does the protagonist want that conflicts with what they need, and what would the ending cost. Ideas that answer all four generate structure, and ideas that answer fewer generate revisions.",
                "Testing an idea means looking for its failure mode before the manuscript can hide it. Premises fail in predictable ways, and each failure has a diagnostic question attached to it, which means the test can be run in an afternoon rather than after a first draft.",
            ],
            "middles": [
                "Test for generated events. Take the premise and ask what must happen in the first five chapters without inventing anything new. A premise that produces obligations generates a book; a premise that requires ideas on top of it will always need ideas on top of it.",
                "Test for an unavoidable choice. The strongest premises contain a decision with two acceptable and incompatible answers, and the book is the work of making that decision expensive enough that the reader cannot take it lightly.",
                "Test for a running cost. Pressure that accrues with time produces chapters, and pressure that exists as a single threat produces one confrontation. Prefer the premise whose cost is charged every week.",
                "Test for a specific person. If no one in the material is damaged by the premise in a way the reader can feel, the book will be about the premise rather than about anyone, and the repair is a casting decision rather than a plot decision.",
                "Test for an ending that pays the promise. If the honest ending is available in the first chapter, the premise does not generate enough pressure, and it will need either a harder choice at the center or a smaller promise to keep.",
            ],
            "closers": [
                "Commit to the idea that answered the tests, and write the answers down as the plan's first page. What follows is then a story rather than an attractive situation.",
                "Settle the premise, its promise, and its central choice. The outlining begins from those decisions and not before them.",
            ],
        },
        {
            "id": "story_not_situation",
            "frames": [
                "You have material you find interesting and no story inside it yet.",
                "You are trying to turn a setting, a mood, or a theme into something that happens to somebody.",
                "You keep describing the idea instead of finding the trouble in it.",
            ],
            "question": "How does an idea become a story: who wants what, what stands in the way, and why will the reader need to know how it turns out?",
            "openers": [
                "A situation becomes a story when someone in it wants something and cannot simply take it. The work at this stage is finding that want and the resistance to it, because everything else the world, the tone, the theme, is carried by the trouble they create.",
                "Brainstorming is a search for trouble. The material supplies a world, a mood, or a question; the story supplies a person who wants something badly enough to act, an obstacle that will not move, and a reason the reader stays to see which one wins.",
            ],
            "middles": [
                "Ask what the premise makes impossible for one particular person. Ideas that let everyone walk away produce books whose opening act is a negotiation with the plot; ideas that remove the exit start moving on their own.",
                "Cast the story by damage rather than by interest. Whoever the events hurt most is the protagonist, and whoever the premise leaves untouched is scenery, so deciding who suffers decides the book.",
                "Find the running cost. Pressure that accrues produces chapters, while pressure that exists as a single threat produces one confrontation, so prefer the version of the idea that charges somebody something every week.",
                "Look for the choice the idea demands with two acceptable and incompatible answers. A premise whose crisis has one obvious resolution has already told the reader how it ends.",
                "Follow the question the reader will be holding and check that it can be renewed. Curiosity is what carries a book through its middle, and an idea with one secret kept for the last page has nothing to renew.",
                "Test the idea by imagining what happens next without inventing anything new. A premise that generates its own events has a book in it; a premise that needs ideas added on top will always need ideas added on top.",
            ],
            "closers": [
                "Commit to the version with the want, the obstacle, and the cost, and say what the reader is waiting to find out. That is the story the outline will be built from.",
                "Finish by naming what the story is about in terms of a person and a problem rather than a theme or a world. If that sentence cannot be written, the idea is still a situation.",
            ],
        },
    ],
    "principles": [
        "Pressure before premise polish: an idea is only usable when it makes something unavoidable for someone specific.",
        "Specific over general: replace categories with people, obligations, and costs, and narrow until the material can be drafted scene by scene.",
        "Promise and price: decide what the book offers the reader and what the ending will cost, before any structure is built.",
    ],
}
