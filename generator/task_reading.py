"""Reading the task and the story before reasoning about craft.

Each stage of the process begins the same way in practice: with the writer working
out what they have been asked to produce, and what the story currently is. A
chapter request has to be read for its obligations, the chapters before it have to
be recalled for what they established, and the people in the scene have to be
reconstructed before anything can be decided about how the scene is written. An
outline request has to be read as a story problem, and a brainstorming request has
to be read as a story that does not exist yet.

This module holds that opening reasoning, per stage and per kind:

    drafting   task          what this chapter is supposed to be
               story_so_far  what the earlier chapters have already established
               characters    who is in the scene and what they carry in
               what_happens  what the chapter does, in what order
               emotion_line  what the reader should feel, and where it is earned
    outline    story         the story as a whole: plot, conflict, characters
               artifact      the outline's own deliverable and what it must contain
               chapters      what each chapter has to accomplish
               characters    who the cast are, what they want, and how they differ
    ideation   story         the idea as a story: who, want, obstacle, stakes
               artifact      what brainstorming has to produce before it is done
    revision   draft_state   what the draft currently is, read as the reader would
               repair        what a pass is for, and what it must not damage

Records lead with one or two of these paragraphs and then reason the craft, so the
dataset teaches the order the work actually happens in: read the task, reconstruct
the story, then decide.

All paragraphs are structural and generic: they never name a book, a chapter, or a
character, so the trained behavior transfers to whatever request the caller sends.
"""

TASK_READING = {
    "drafting": {
        "task": (
            "Read the request before deciding anything about the writing. What the chapter has to accomplish, where it sits in the book, what it must leave true when it ends, and what the reader is supposed to have learned by the last page of it.",
            "The first decision is about the assignment rather than the prose: what this chapter is for. Its function in the story, the beats it has to contain, and the state it has to hand on decide almost everything that follows.",
            "Work out what has been asked before working out how to do it. The chapter arrives with obligations about what happens, what changes, and what the reader learns, and the reasoning should be able to state those obligations in one or two sentences.",
            "Before writing, restate the chapter's job to yourself: the situation it opens in, the turn it has to reach, and the condition it must leave behind. Writing that does not know its own obligations tends to satisfy none of them.",
            "Establish the boundaries of the chapter first: what it must accomplish, what it must not resolve yet, and what the reader has to be able to do afterwards that they could not do before.",
        ),
        "story_so_far": (
            "Reconstruct the story to this point before writing a line of it: what has already happened, what has been promised, what has been lost, and what the reader is currently waiting to find out. The chapter starts inside that inheritance rather than beside it.",
            "The chapters before this one have established facts, debts, injuries, alliances, and a particular state of knowledge for every character. Reason from that state rather than from the general situation, because the reader has been holding it since the last page.",
            "Recall the open threads before deciding anything: the question left unanswered, the promise made, the threat introduced, and the relationship changed. A chapter that ignores what the reader is carrying reads as a chapter from another book.",
            "Work from the summaries of the earlier chapters rather than from memory of the plan. What matters now is what actually landed on the page: who was present, what was said, what changed, and what the reader has been told.",
            "Fix the current state before the scene is written: where everyone is, who knows what, what has already been spent, and what is still owed. Everything the chapter does has to be consistent with that ledger, because the reader is keeping it.",
        ),
        "characters": (
            "Reconstruct the people before staging them. For everyone in the scene: what they want in this conversation or confrontation, what they are carrying in from earlier chapters, what they believe about the situation, and what they are wrong about.",
            "Ask what each character in the scene is willing to do, and what they will not do even now. The scene's shape follows from the gap between those two, and the gap has to be set by what has happened to them rather than by what the scene needs.",
            "Check what each person knows at the start of the chapter. Characters act on their information, not the reader's, and a scene where someone uses knowledge they do not have breaks the story's credibility for the rest of the book.",
            "Decide what each person is feeling on entry, and how that feeling will distort what they say and notice. Emotion changes behavior, and behavior is what the reader sees; naming the feeling in narration is a missed opportunity to show it.",
            "Give everyone present a reason to be there and something to protect while they are. Characters with only a function in the scene read as furniture, while characters with a stake make the scene contestable.",
        ),
        "what_happens": (
            "Decide what the chapter does before deciding how it sounds: the event, the order it happens in, and what is different when it is over. The writing is the execution of those decisions, not the occasion for making them.",
            "Sketch the sequence in steps that can each be checked against the chapter's obligations: what opens it, what presses the characters, what turns, and what it hands on. A sequence that cannot be summarized is usually a sequence that has not been decided.",
            "Plan the order in which the reader learns things inside this chapter, because that order is what produces the chapter's effect, and it is far cheaper to decide here than to repair after writing.",
            "Decide the chapter's pressure before its events: who wants what in it, what is in the way, and what it costs to push through. Events staged without pressure are information; pressure without events is atmosphere.",
        ),
        "emotion_line": (
            "Plan the emotional line of the chapter the way the other obligations are planned: what the reader should feel on entry, what the scene does to that feeling, and what they should be left carrying into the next chapter.",
            "Track what each character's emotional state can support. A scene that requires a calm decision from someone who has just lost something makes the loss meaningless; the feeling has to be spent somewhere in the scene that follows it.",
            "Decide where the chapter earns its intensity. Feeling arrives from consequence and cost rather than from description, so the reasoning should place the moments the reader cares about after the moments the story paid for them.",
        ),
    },
    "outline": {
        "story": (
            "Reason about the story before reasoning about the document: who the story is about, what they want, what stands in the way, what it costs them, and how the situation escalates from its opening condition to its end.",
            "Establish the story's engine first: the want, the obstacle, and the pressure that will not let either rest. Every structural decision below is answerable to that engine, and the outline that cannot say what the engine is will be a list of events.",
            "Work out the conflict's escalation before arranging chapters: what gets worse, for whom, why the earlier options close, and what the protagonist has to spend to keep going. Structure that does not escalate is arrangement.",
            "Decide the story's shape in terms of condition changes rather than incidents: what is true at the start, what becomes true at each turn, and what the final condition costs. This is what a reader experiences as a story rather than a sequence.",
            "Think about the cast as the story's moving parts: who wants what, where those wants collide, and which collisions the plot will force. Plot is what happens when those collisions can no longer be avoided.",
        ),
        "artifact": (
            "The outline is the deliverable, and it has to carry enough for the writing to proceed: a paragraph summary of each chapter, short descriptions of the principal characters, the plot, the conflict, and any notes or ideas worth keeping. Reasoning here decides each of those.",
            "Everything the drafting stage will need has to be on the page or the drafting will invent it: per-chapter summaries that say what happens and what changes, character notes that say what they want and what they hide, the plot's through-line, the conflict's escalation, and open notes.",
            "Write the outline at the level a writer can work from: each chapter summarized in a paragraph, each principal character described in a few lines that imply behavior, the plot's chain of cause and effect, the conflict's pressure, and the loose ideas that might matter later.",
            "The outline's value is that it can answer questions later: what happens in chapter nine, why the protagonist cannot simply leave, what the antagonist wants, and what the story's ending must cost. Build it so those answers exist.",
        ),
        "chapters": (
            "Give every chapter a job that can be stated in a sentence: what it establishes, what it changes, and what it hands to the next chapter. Chapters that cannot be described that way are usually chapters that exist for pacing rather than for story.",
            "Arrange the chapters so that each one's ending creates the next one's problem. Causality between chapters is what makes a long book feel inevitable rather than episodic.",
            "Place the story's turns before deciding its connective chapters: the break, the reversal, the loss, and the choice. The chapters between turns inherit their shape from the turns they sit between.",
            "Keep the reader's question alive in every chapter: which thread is open, what they are waiting to learn, and when the next piece of it arrives. The chapter plan is where that question is maintained or dropped.",
        ),
        "characters": (
            "Describe the cast in terms of what they do rather than what they are: what each wants, what each will not do, what each is hiding from the others, and what each will do when pressed. Those four answers make a character usable in any chapter.",
            "Make the cast distinguishable by behavior, so that the writing stage can show who is present without labeling them: habits, preoccupations, ways of disagreeing, ways of handling an object or a silence.",
            "Plan each principal character's trajectory: what they believe at the start, what breaks that belief, and what they choose differently at the end. A character without a trajectory is a resource for other characters' trajectories.",
            "Represent the antagonist with the same care as the protagonist: a want the reader can follow, a method, a limit, and a case. Antagonists described only as obstacles make the story's conflict thin.",
        ),
    },
    "ideation": {
        "story": (
            "Reason about the story the idea would become before judging the idea itself: who it happens to, what they want, what stands in the way, what it costs them, and what the reader will be waiting to find out.",
            "Treat the material as a story in potential rather than a subject: the interesting part is not the world or the theme but the person whose life the material makes difficult, and what they will do about it.",
            "Work out the conflict before the plot: two people who want incompatible things, or a person and an obstacle that cannot be negotiated with. Conflict identified here is what generates scenes later.",
            "Think about the story's shape at the largest scale: how it begins, what it turns on, and what the ending costs. An idea whose ending cannot be imagined has usually not decided who it is about.",
            "Ask what the reader gets from this story that they cannot get from the material alone: dread, curiosity, recognition, delight. That is the promise, and it is decided here rather than during writing.",
        ),
        "artifact": (
            "Brainstorming is finished when the idea can survive a single sentence: a person, a want, an obstacle, and a cost. Reasoning here should end with that sentence and the decisions behind it rather than with a collection of options.",
            "The usable output of brainstorming is a premise with an engine, a protagonist chosen rather than assumed, a conflict that escalates on its own, stakes worth weighing, and a direction for the ending. Everything else is material for later.",
            "Decide the few things that make this story this story, and drop the rest. An idea with too many load-bearing parts is an idea whose parts will contradict each other before the outline is finished.",
        ),
    },
    "revision": {
        "draft_state": (
            "Read the draft as the reader will meet it before deciding anything: what happens in it, what has been established by this point, what the reader currently knows and wants, and where their attention is. The problems live in that experience rather than in the outline.",
            "Establish the draft's actual state rather than its intended state: what is on the page, in order, and what a reader would take from it without any of the writer's context.",
            "Locate the fault before repairing it: which chapter, which scene, and which decision creates the effect the reader experiences. Symptoms cluster, and the cluster usually points to one cause.",
        ),
        "repair": (
            "Decide what this pass is for before opening the file: which class of problem it addresses, what it is allowed to change, and what it must not touch. A pass without a scope becomes a rewrite.",
            "Protect the draft's working parts explicitly, in writing, before changing anything: the scenes, lines of voice, and character decisions the repair should leave intact.",
        ),
    },
}

# Which kinds each stage's records must lead with (the rest are drawn at random).
REQUIRED_KINDS = {
    "drafting": ("task",),
    "outline": ("story", "artifact"),
    "ideation": ("story",),
    "revision": ("draft_state",),
}


def kinds_for(stage, rng, count=2):
    """The task-reading kinds this record leads with, required kinds first."""
    required = list(REQUIRED_KINDS[stage])
    pool = [kind for kind in TASK_READING[stage] if kind not in required]
    rng.shuffle(pool)
    kinds = required + pool[: max(0, count - len(required))]
    return kinds
