"""Revision: deciding what to change, in what order, and what to protect."""

CAT = {
    "id": "revision_craft",
    "label": "Revision and structural repair",
    "moves": {
        "cause_before_symptom": [
            "Find the cause before treating the symptom. A chapter that feels slow, a scene that feels thin, and an ending that feels unearned are symptoms, and each has a small number of structural causes that the revision has to identify before it touches the pages.",
            "Describe the effect the chapter is failing to produce, then work backward to the decision that would produce it. Revising from the symptom produces local improvements that leave the cause in place, and the cause will reappear in three chapters.",
            "Name the one change that would make several fixes unnecessary. Revisions that address causes remove work, and revisions that address symptoms add it, which is why the second kind of pass tends to make manuscripts longer and weaker.",
        ],
        "cut_first": [
            "Cut before adding. The first pass should remove whatever is not load-bearing, because a shorter chapter makes its structural problems visible and an added scene usually hides them behind new material.",
            "Test every passage against its function. Passages that neither change a condition, deepen a character, nor prepare a later payment are candidates for removal, and the removal is usually faster than the repair would be.",
            "Prefer the cut that removes an explanation over the cut that removes a scene. Explanation is the cheapest thing to lose and the most common reason a chapter feels as though it is stalling, while scenes carry the pressure the book needs.",
        ],
        "protect_what_works": [
            "Decide what the revision must not touch. The scenes that work, the voice in the passages where it holds, and the material the ending depends on should be marked before any pass begins, so repair does not erode them.",
            "Keep the odd, specific, inconvenient material unless it is the direct cause of a failure. Revision tends toward smoothness, and smoothness is what removes the texture that made the draft particular.",
            "Change one thing at a time and re-read the affected chapters before the next change. Revisions made in parallel produce a manuscript whose parts no longer fit, which is a larger problem than the one the pass was fixing.",
        ],
        "pass_order": [
            "Run the passes in order: structure, then scene, then continuity, then line. Structure comes first because it decides which scenes exist; line comes last because polishing a scene that will be cut is wasted work, and it is the most common way revision time is lost.",
            "Do the structural pass on a summary rather than on the manuscript. Reading the chapter map and the function of each scene shows the shape of the problem, and the pages make local quality so visible that structural faults are easy to miss.",
            "Separate the diagnosis pass from the repair pass. Revision that fixes as it reads makes inconsistent decisions, because the criterion keeps changing as the reader moves through the draft.",
        ],
        "pressure_repair": [
            "Where a chapter sags, raise the pressure rather than the stakes. Pressure comes from what the protagonist wants being obstructed in the scene they are in, and stake inflation is what a draft reaches for when it cannot find the local obstruction.",
            "Repair an inert scene by giving someone in it something to lose now. Scenes feel flat when participation is costless, and the smallest repair that works is usually an obligation with a deadline attached to a character who has been present without needing anything.",
            "Check the chapter's entry and exit before rewriting its middle. A scene that begins too early and ends too late reads as slow even when every paragraph is competent.",
        ],
        "continuity_after_change": [
            "After any structural change, trace its consequences forward. A decision altered in the first act changes what characters know in the third, and the revision has to carry the correction through every chapter the change touches.",
            "Maintain a state record while revising: who knows what, what has been promised to the reader, what has been lost, and what is still owed. Revision is where continuity damage is usually introduced rather than discovered.",
            "Re-check the setup chain after cuts. Removing a scene removes its plants, and the payoff that depended on them becomes an unearned event three hundred pages later.",
        ],
    },
    "problems": [
        {
            "id": "revision_by_addition",
            "frames": [
                "Your revision plan is a list of scenes to add.",
                "The draft's problems are being addressed by explaining them more.",
                "You are repairing the chapter by building around what does not work.",
            ],
            "context": "Additive revision lengthens the manuscript and leaves the original fault in place.",
            "stages": ["the revision plan", "the second pass", "the decision about what the draft needs"],
            "openers": [
                "Decide what to remove first. For every planned addition, find the existing material that would make it unnecessary, which is usually a scene that has been made to carry a function it was not designed for.",
                "Reason from the draft's structure rather than from its gaps. A missing beat is usually a beat that exists in the wrong place, and the repair is a relocation rather than a new chapter.",
            ],
            "closers": [
                "Commit to a revision that removes before it adds: the chapter's structure decided first, the redundant material cut, and the additions limited to what the plan genuinely requires.",
                "Fix the draft's cause rather than its coverage. If a scene has to be added, the decision should come with a corresponding cut.",
            ],
        },
        {
            "id": "line_before_structure",
            "frames": [
                "You are editing sentences in a chapter whose structure is undecided.",
                "The prose is receiving attention while the scene's function is still unclear.",
                "Your revision began at the paragraph level and has not yet examined the chapter's shape.",
            ],
            "context": "Line work on a structure that may change is work that will be redone.",
            "stages": ["the first revision pass", "the decision about pass order", "the chapter's structural review"],
            "openers": [
                "Defer the line pass. Read the chapter map first and decide which scenes exist, in what order, and with what obligation; only then is the prose worth refining, because the passages worth refining are the ones that will survive the structural pass.",
                "Reason about the pass order explicitly: structure, then scene, then continuity, then line. Any other order spends attention on material that the next pass may remove, and it also makes the structural faults harder to see because the pages read well.",
            ],
            "closers": [
                "Commit to the pass order and to finishing each pass before beginning the next. Structural decisions come first because they determine which pages are worth polishing.",
                "Settle the chapter's shape before touching its sentences, and let the line pass be the last work the chapter receives.",
            ],
        },
        {
            "id": "symptom_patching",
            "frames": [
                "The same problem keeps returning in different chapters.",
                "You have fixed this fault three times in three places.",
                "Your revisions address the scenes where the fault appears rather than the decision that produces it.",
            ],
            "context": "A fault that reappears is a cause that has not been found, and each patch raises the cost of the real repair.",
            "stages": ["the diagnostic pass", "the decision about what the draft needs", "the review of the revision plan"],
            "openers": [
                "Look for the decision upstream that produces the symptom. Repeated faults usually trace back to an outline decision or a character choice, and correcting it once removes the need for the patches.",
                "Reason about the fault's pattern rather than its instances: where it occurs, what is true in each place, and what the draft is doing when it happens. The pattern identifies the cause, and the cause identifies the change.",
            ],
            "closers": [
                "Commit to a single upstream correction rather than a set of local patches, and re-read the affected chapters after it to see which patches are still needed.",
                "Find the cause, make one change, and verify its consequences forward through the chapters it touches.",
            ],
        },
        {
            "id": "flattening_pass",
            "frames": [
                "Your revision is making the draft smoother and less distinctive.",
                "The chapters are more consistent and less alive than they were.",
                "You are removing irregularities that were carrying character.",
            ],
            "context": "Revision toward smoothness removes the specific material that makes a draft particular.",
            "stages": ["the line pass", "the continuity pass", "the review of the revision plan"],
            "openers": [
                "Separate errors from preferences before the line pass. Irregularities that damage clarity are errors; irregularities that carry voice, character, or local specificity are the draft's assets, and a pass that cannot tell them apart will remove both.",
                "Decide what the revision is allowed to touch. Voice, odd detail, and the passages where the draft is doing something unusual should be named as protected before the pass begins, because smoothness is the default direction of revision.",
            ],
            "closers": [
                "Commit to protecting the specific and repairing the unclear: the pass removes confusion and repetition while leaving the voice and the odd, particular material intact.",
                "State what the revision will not change, then hold to it while working through the pages.",
            ],
        },
        {
            "id": "no_revision_criteria",
            "frames": [
                "You have been through the draft twice and cannot tell whether it is finished.",
                "Your revision keeps changing direction because there is no standard to measure against.",
                "You are revising by feel and the manuscript is not converging.",
            ],
            "context": "Without criteria, revision either stops early or continues indefinitely, and neither produces a finished book.",
            "stages": ["the revision plan", "the decision about when the draft is finished", "the final pass"],
            "openers": [
                "Write the criteria down before the pass: what the chapter must accomplish, what the reader must be able to infer, what must remain true for the chapters after it, and what the book's promise requires. The pass then has a standard, and the draft can be judged against it rather than felt.",
                "Reason about what finished means for this draft in checkable terms: every chapter's obligation met, every thread planted and paid, every consequence traced, and no contradiction outstanding. Criteria convert an endless process into a finite one.",
            ],
            "closers": [
                "Commit to criteria and to passing only until they are satisfied: obligations met, continuity sound, promises paid, and prose clear rather than perfect.",
                "Decide what the draft must satisfy and check it chapter by chapter. Revision ends when the criteria are met rather than when the manuscript stops improving.",
            ],
        },
    ],
    "traps": [
        {
            "id": "polish_before_repair",
            "frames": [
                "The prose is receiving attention while the chapter's structure is still wrong.",
                "You are refining sentences in a scene that may not survive the next pass.",
                "The draft reads well and does not work.",
            ],
            "slide": "The pages are being polished because polishing is pleasant and immediately measurable. Sentences improve, the chapter reads more smoothly, and the structural fault remains underneath, now harder to see because the surface is convincing.",
            "stages": ["the first revision pass", "the decision about pass order", "the review of the chapter's function"],
            "openers": [
                "The pull is toward the sentences, and the correction is to decide the chapter's function and structure first. Reason at the level of what the chapter must change and how that change is staged before any line is touched.",
                "Reason past it by asking what would be wasted if the scene were cut. That question identifies which material deserves refinement and which material is currently absorbing attention it has not earned.",
            ],
            "damage": "Polishing before structural repair produces manuscripts that read better than they are, which makes the real problems harder for the writer to see and easier for a reader to feel without naming. The revision time is spent on pages that later get removed, and the structural fault is still present at the end of the pass.",
            "reason_past": "Reason past it by fixing the pass order: structure, then scene, then continuity, then line. Each pass is finished before the next begins, and the line pass is the last work the chapter receives.",
            "closers": [
                "Commit to structural decisions first and to the line pass last, with each pass finished before the next begins.",
                "Settle what the chapter is for and what it must change before refining how it reads.",
            ],
        },
        {
            "id": "patch_and_keep",
            "frames": [
                "You are repairing the chapter around material you know should go.",
                "The draft contains scenes you are defending because they were expensive to write.",
                "Your revision keeps accommodating a part of the manuscript that no longer belongs.",
            ],
            "slide": "The revision is arranged around the material that should be removed. Scenes are given new functions, transitions are built to reach them, and explanations are added to justify them, so a fixable draft becomes a structure that has to be protected.",
            "stages": ["the revision plan", "the second pass", "the decision about the draft's remaining problems"],
            "openers": [
                "The pull is the sunk cost of work already done, and the correction is a decision about function rather than about effort. Reason about what each scene contributes to the book's pressure and cut by that standard, not by how long it took.",
                "Reason past it by testing the scene in the abstract: if it had been cut before the draft began, would the story need to replace it? Scenes that would not be replaced are the ones the revision is protecting rather than the book.",
            ],
            "damage": "Manuscripts revised around their weakest material keep the faults and add explanations. The book becomes longer, its pressure dilutes across scenes that exist to justify other scenes, and the revision that would have fixed the structure in a week becomes a rewrite in a month.",
            "reason_past": "Reason past it by deciding the book's required material first, from the ending backward, and treating everything else as removable. Cuts made on structural grounds do not need defending, and they make every remaining scene stronger.",
            "closers": [
                "Commit to cutting on function rather than on effort: what the book requires from the ending backward stays, and the rest is available to remove.",
                "Decide what the story needs, then let the revision remove what it does not, whatever that material cost to write.",
            ],
        },
        {
            "id": "final_pass_infinite",
            "frames": [
                "You have revised the chapter four times and cannot say whether it is done.",
                "Each pass improves something and reveals something else.",
                "You are revising without a standard that could be met.",
            ],
            "slide": "The revision continues because there is no criterion for stopping. Every pass finds real improvements, so each pass feels justified, and the manuscript is never released, or is released at a point chosen by exhaustion rather than by judgement.",
            "stages": ["the revision plan", "the decision about when the draft is finished", "the final pass"],
            "openers": [
                "The pull is the absence of criteria, and the correction is to define them before the pass. Reason about what this chapter must accomplish, what the reader must be able to infer, and what must remain true afterward, then treat those conditions as the finish line.",
                "Reason past it by separating the passes that change the book from the passes that change the prose. Deciding that the prose is clear rather than perfect is a decision, and it is the one that allows a draft to become a book.",
            ],
            "damage": "Revision without criteria consumes the time that the next book needs and produces diminishing returns on the current one. Passes begin to undo each other, the manuscript loses the accidental particularity that made it interesting, and the writer's confidence in judgement erodes because there is no standard to be right about.",
            "reason_past": "Reason past it by defining explicit criteria and running passes against them rather than running passes until the manuscript feels finished. Completeness is checkable, and the sense of finishedness is not.",
            "closers": [
                "Commit to criteria and to the passes that satisfy them, and stop when they are met rather than when the pages stop improving.",
                "Decide what the chapter must satisfy, verify it, and move to the next chapter.",
            ],
        },
    ],
    "discipline": [
        "Diagnose before repairing. Every revision decision should trace back to a cause rather than to a symptom that has been noticed twice.",
        "Run passes in order and finish each one. Structure, then scene, then continuity, then line.",
        "Protect what works while repairing what fails; revision that removes character in exchange for smoothness is a loss rather than a fix.",
    ],
    "themes": [
        {
            "id": "whole_book_revision",
            "frames": [
                "You are planning a revision pass across an entire manuscript.",
                "You want the revision to fix causes rather than chapters.",
                "You are deciding what the book needs before you open the file.",
            ],
            "question": "How should a whole manuscript be revised so that the work done in one chapter does not have to be redone in the next?",
            "openers": [
                "Revision across a book is a scheduling problem. The order of passes decides how much work survives, and the discipline is to make the structural decisions once, high enough in the manuscript that every later fix is smaller.",
                "Treat the manuscript as a system of dependencies: chapters depend on earlier plants, characters depend on earlier knowledge, and the ending depends on everything the middle paid for. Revision has to work on the dependencies rather than on the chapters, which means it starts with the map and not the pages.",
            ],
            "middles": [
                "Read the chapter functions together before reading any chapter. What the book is doing at each position becomes visible in the map, and the faults it shows are the ones that no amount of local revision can address.",
                "Decide which chapters the revision is allowed to restructure and which are fixed points. Marking the fixed points prevents the pass from expanding indefinitely, and it also shows which structural change would require the fewest other repairs.",
                "Fix continuity after structure and before line. Every structural change alters what characters know and what the reader has been promised, and a continuity pass run in the right position catches those alterations cheaply.",
                "Keep a running record of decisions made during the revision: what was cut, what was added, what state was changed. Revision damage comes from unrecorded changes, and the record is what makes the second half of the pass consistent with the first.",
                "Verify the ending's conditions after every structural change. The ending is the most dependent element in the book and the first thing that breaks when an earlier chapter is altered.",
                "Stop when the criteria are met, and treat further passes as a different project. A manuscript that satisfies its obligations, its continuity, and its clarity is finished, even when a better version can be imagined.",
            ],
            "closers": [
                "Commit to revision by dependency rather than by chapter: structural decisions first, continuity after, line last, and criteria for stopping set before the pass begins.",
                "Work the manuscript as a system, correct causes once, and release the draft when the criteria are met.",
            ],
        },
        {
            "id": "reader_gap_audit",
            "frames": [
                "You want to know how the draft reads to someone who does not know the plan.",
                "You suspect the chapters assume knowledge the reader does not have.",
                "You are checking whether the book's information arrives in a readable order.",
            ],
            "question": "How is a draft audited for what the reader can actually follow, know, and infer at each point?",
            "openers": [
                "Audit the draft against a reader's model of events rather than against the plan. At each chapter boundary, write down what the reader knows, what they expect, what they want to know, and what they have been promised, then compare that against what the following chapter assumes.",
                "The gap between the plan and the reader is where revision produces the largest gains, because a fault in the order of information reads as a fault in the story no matter how good the individual chapters are.",
            ],
            "middles": [
                "Check the arrival order of every essential fact. Facts delivered before the reader can use them are forgotten, and facts delivered after the scene that needed them make the scene confusing, so position is what decides whether an explanation is help or noise.",
                "Look for places where the draft explains something the reader has already inferred. Those passages are the clearest sign of a chapter written from the plan rather than from the page, and cutting them usually improves both pace and trust.",
                "Verify that pressure is legible: the reader should be able to name what the protagonist wants and what stands in the way at every point. Where that cannot be named, the scene is doing private work.",
                "Track the threads the reader is holding at each position. More than a few open questions at once produces a chapter that is read passively, and one or none produces a book that is easy to put down.",
                "Confirm that every reversal has been prepared by something the reader has seen. Reversals that depend on information appearing for the first time at the moment of reversal read as authorial convenience regardless of the plan's intention.",
                "Read the draft's quiet chapters against the reader's attachment. Low-pressure chapters work when the reader cares about what is at risk, and the audit question is whether the draft has spent enough time on the people before asking the reader to worry.",
            ],
            "closers": [
                "Commit to revising the order of information before revising the prose: what the reader knows at each position, what they can infer, and what the draft may stop explaining.",
                "Audit the draft from the reader's side, correct the order of what is delivered, and let the clarity gains do the work.",
            ],
        },
    ],
    "principles": [
        "Cause before symptom: a fault that reappears has not been diagnosed, and each patch raises the cost of the real repair.",
        "Structure, then scene, then continuity, then line, with each pass finished before the next begins.",
        "Protect what works and measure against criteria; revision ends when the draft satisfies its obligations rather than when the pages stop improving.",
    ],
}
