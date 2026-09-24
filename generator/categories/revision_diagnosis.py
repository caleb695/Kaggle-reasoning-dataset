"""Revision diagnosis: reading a draft for its causes.

This library reasons about the standard symptoms a draft produces, the causes
behind them, and the specific structural repairs that follow. It is organized
around what a writer actually notices while rereading: a slow opening, a flat
middle, a confusing sequence, an unlikeable protagonist, an ending that does not
land.
"""

CAT = {
    "id": "revision_diagnosis",
    "label": "Revision diagnosis: symptoms, causes, and structural repair",
    "moves": {
        "symptom_to_cause": [
            "Convert the symptom into a structural question before touching the pages. A slow opening is usually a scene that starts too early or a protagonist with nothing to want; an unlikeable protagonist is usually a character with no competence and no self-awareness; an unearned ending is usually an ending whose conditions were never planted.",
            "Ask what the draft is failing to produce rather than what it contains. Revision decisions made from the intended effect are precise, while decisions made from the presence of material tend to add more of what is already there.",
            "Distinguish local faults from systemic ones by looking for repetition. A fault that appears once is a scene problem, and a fault that appears in five chapters is a decision made once and never revisited, which is where the repair belongs.",
        ],
        "scene_audit": [
            "Audit each scene against four questions: whose scene is it, what do they want in it, what stands in the way, and what is different when it ends. Scenes that fail two or more of those questions are the ones to cut, merge, or relocate rather than polish.",
            "Look for scenes that are doing two jobs badly and split the jobs across the chapter. Then look for pairs of scenes doing the same job and merge them, which is the fastest way to shorten a draft without losing material.",
            "Check the scenes that exist because the reader needed information and find the scene that could carry it instead. Explanation folded into a scene that is already turning is invisible, while the same information delivered in its own scene is felt as a pause.",
        ],
        "chapter_function_audit": [
            "For each chapter, write its function and then write what the draft actually does. The gap between those two sentences is the revision, and it is usually a matter of a chapter carrying obligations that belong elsewhere.",
            "Check the balance of chapters by function: too many establishing chapters produce a slow opening, too many turning chapters produce exhaustion, and too many confirming chapters produce a middle that reads as long.",
            "Look for the chapter that has no consequence for the next one. It is either the chapter to cut or the chapter that needs the consequence moved into it from somewhere else.",
        ],
        "pacing_repair": [
            "Diagnose pacing by position rather than by speed: the draft is slow where nothing is at stake for the character in the scene they are in, and it is rushed where a change of state happens without being staged. Those two diagnoses have opposite repairs.",
            "Repair an inert stretch by relocating rather than by trimming. Shortening a scene that has no pressure produces a shorter scene with no pressure, while moving a pressure-bearing beat into it can transform the same number of pages.",
            "Decide the draft's compression ratio deliberately: summarize what the reader can predict, stage what they cannot. Most sagging middles are made of stages that should have been summaries and summaries that should have been stages.",
        ],
        "character_repair": [
            "Repair an unlikeable protagonist by giving them competence, self-awareness, or a cost they accept willingly, and by removing the draft's attempts to defend them. Readers forgive almost anything except a character who is presented as blameless.",
            "Repair a passive protagonist by moving the decisions from the supporting cast into their hands, then letting those decisions have consequences the draft already contains. Passivity is usually a distribution problem rather than a personality problem.",
            "Repair unclear motivation by making the want visible before the choice that requires it. Characters who behave inexplicably are usually characters whose reasons were cut for pace or delivered after the fact.",
        ],
        "clarity_repair": [
            "Repair confusion by reordering information rather than by adding explanation. Most confusion in a draft comes from facts arriving after the scene that needed them, and moving the fact is invisible while explaining it is felt as a pause.",
            "Audit what the reader knows at each chapter boundary and compare it with what the following chapter assumes. The mismatch list is the most actionable artifact revision produces, and it usually shortens the draft rather than lengthening it.",
            "Check that the pressure is legible: at any point the reader should be able to say what the protagonist wants and what stands in the way. Where that cannot be stated, the scene is doing private work that the draft has not licensed.",
        ],
        "stakes_and_ending_repair": [
            "Repair weak stakes by specifying rather than escalating: name the thing at risk, show it being protected earlier, and let the threat reach it. Inflating the threat is the repair that fails most often.",
            "Repair an unearned ending by tracing its conditions backward and planting them, then removing the draft's explanations of why the ending is justified. Endings are made credible by material, and defended endings read as arguments.",
            "Check whether the ending answers the question the middle actually asked. Where the middle's live question is different from the one the ending resolves, the revision is to either change the ending or move the middle's question into the plan.",
        ],
        "line_pass": [
            "Save the line pass for last and run it against a specific list: filter verbs, explanations of what has already been shown, repeated sentence constructions, and the paragraph-ending sentence that dramatizes what was just said. A list keeps the pass from removing the draft's voice along with its habits.",
            "Protect the passages where the draft is doing something unusual. Revision tends toward smoothness, and smoothness is what removes the particular material that made the draft interesting in the first place.",
            "Cut toward clarity rather than toward brevity. The goal of the line pass is prose that is easy to read and specific, not prose that is short; compression applied indiscriminately removes texture and leaves the draft correct and lifeless.",
        ],
        "structural_moves": [
            "Choose among the three structural moves before editing: cut, merge, or relocate. Cutting removes obligations, merging concentrates them, and relocating changes what the reader knows when; most revision problems are solved by one of the three rather than by rewriting.",
            "Relocate rather than rewrite whenever the material is good and the position is wrong. Scenes that fail in one sequence often work in another, and the decision is about the reader's state at the moment of arrival.",
            "Decide what the revision will not touch, and write it down. Revision erodes what it is allowed to improve, and the list of protected material is what keeps a second pass from flattening the book.",
        ],
    },
    "problems": [
        {
            "id": "slow_opening",
            "frames": [
                "Your first chapters establish without pressuring anyone.",
                "The draft's opening is competent and easy to put down.",
                "Your first act introduces a world and postpones the story.",
            ],
            "context": "Openings read as slow when the protagonist has nothing they are trying to do in the scene they are in.",
            "stages": ["the first act's audit", "the first chapter's function", "the opening's information load"],
            "openers": [
                "Give the protagonist something to attempt in the first scene and let the world arrive through what obstructs them. The story's explanation can be distributed across the first three chapters, but the character's want has to be present immediately.",
                "Reason about where the draft's actual story begins and move the opening later. Most slow openings are three scenes of establishment in front of a first scene that already contains everything the reader needs.",
            ],
            "closers": [
                "Commit to an opening in which the protagonist wants something, is obstructed, and is changed by the outcome, with the world delivered as an obstacle rather than as a tour.",
                "Start the draft at the first scene where something is at stake, and fold the necessary establishment into it.",
            ],
        },
        {
            "id": "sagging_middle_diagnosis",
            "frames": [
                "Your middle chapters repeat their function with new content.",
                "The draft's second act has episodes rather than escalation.",
                "Your middle is where readers stop.",
            ],
            "context": "Middles sag when the plan carries events without a rising cost to the protagonist.",
            "stages": ["the middle's audit", "the sequence functions", "the midpoint's position"],
            "openers": [
                "Look for the missing midpoint. Middles that do not turn produce chapters with interchangeable jobs, and the repair is to place a reversal that makes the protagonist's current method insufficient rather than to add new obstacles.",
                "Reason about what the middle is charging. Each sequence in the middle should take something from the protagonist; where the draft's sequences develop information without charging anything, the middle reads as a plateau regardless of how good the individual chapters are.",
            ],
            "closers": [
                "Commit to a middle built on rising cost with a midpoint reversal, and convert the episodes that develop without charging into sequences that charge.",
                "Give each middle sequence a job, a crest, and a bill, and cut or merge whatever cannot answer for one of the three.",
            ],
        },
        {
            "id": "flat_ending",
            "frames": [
                "Your ending resolves and does not land.",
                "The climax happens to the protagonist rather than because of them.",
                "The last chapters feel like an epilogue to the book's real ending.",
            ],
            "context": "Endings flatten when the resolution arrives without a decision the protagonist has to pay for.",
            "stages": ["the climax's audit", "the final movement", "the resolution's scale"],
            "openers": [
                "Locate the choice the protagonist makes and check whether it costs them anything they have been shown to value. Where the resolution arrives through events rather than through a decision, the repair is to put the decision back at the center and let the events serve it.",
                "Reason about what the ending proves about the protagonist compared with the opening. If the same person could make the same choice at the start of the book, the arc has not been paid off, and the fix belongs in the middle rather than in the last chapter.",
            ],
            "closers": [
                "Commit to an ending in which the protagonist's choice carries the resolution, the cost is drawn from what the draft established, and the last image demonstrates the change.",
                "Rebuild the final movement around a decision with a price, and let the events be the conditions that force it.",
            ],
        },
        {
            "id": "confusing_sequence",
            "frames": [
                "Readers cannot follow what is happening in a stretch of your draft.",
                "Your sequences assume knowledge the reader does not have yet.",
                "The draft is clear to you and not to anyone else.",
            ],
            "context": "Confusion in a draft is almost always an ordering problem rather than a complexity problem.",
            "stages": ["the sequence's audit", "the information schedule", "the chapter boundaries"],
            "openers": [
                "Write down what the reader knows at the start of the sequence and compare it with what the sequence assumes. The difference is a list of facts to relocate rather than to explain.",
                "Reason about the order in which the sequence delivers its facts. Facts delivered before the reader can use them are forgotten, and facts delivered after the scene that needed them make the scene unreadable, so position rather than quantity is what repairs clarity.",
            ],
            "closers": [
                "Commit to reordering information so each scene is legible on a first read, with the mystery held in what happens next rather than in what is currently happening.",
                "Audit knowledge at every chapter boundary, and move facts forward rather than adding explanation.",
            ],
        },
        {
            "id": "unlikeable_protagonist",
            "frames": [
                "Your protagonist is defensible and hard to root for.",
                "Beta readers describe the draft's central character as annoying.",
                "Your protagonist is competent in the plot and unpleasant on the page.",
            ],
            "context": "Readers extend patience for competence, self-awareness, or willingly accepted cost, and withdraw it otherwise.",
            "stages": ["the protagonist's audit", "the first act", "the behavioural evidence"],
            "openers": [
                "Check the draft for the three signals readers use: does this person do anything well, do they know anything true about themselves, and do they pay a cost without complaining about it. Most unlikeable protagonists are missing at least one of the three in the first chapter.",
                "Remove the draft's defenses of the character. Explanations of why the protagonist is justified read as the author arguing with the reader, and the same material delivered as behavior usually produces sympathy the narration could not.",
            ],
            "closers": [
                "Commit to showing competence, self-awareness, and one willingly accepted cost inside the first act, and to cutting the narration's defenses.",
                "Let the reader arrive at sympathy from behavior rather than from the draft's assurances.",
            ],
        },
        {
            "id": "motivation_gap",
            "frames": [
                "Characters in your draft act for reasons the reader has not been given.",
                "Your draft cuts from a decision to its execution without the motive.",
                "Readers say the plot moves because it must rather than because anyone chose it.",
            ],
            "context": "Behavior that is unexplained is experienced as authorial convenience even when the plan's reasoning is sound.",
            "stages": ["the motivation audit", "the choice scenes", "the first act"],
            "openers": [
                "For each significant decision in the draft, find where the character's reason has been established. Where the reason is absent, either move the material that supplies it earlier or add one line of behavior that implies it before the choice.",
                "Reason about the want that stands behind the behavior. Characters who act inexplicably are usually characters whose want was assumed in the plan and never staged, and the repair is a scene of pursuit earlier in the act.",
            ],
            "closers": [
                "Commit to establishing each principal decision's motive before the decision, through behavior rather than through explanation.",
                "Audit decisions against their reasons, and plant the reason earlier rather than defending the choice afterward.",
            ],
        },
        {
            "id": "overwritten_draft",
            "frames": [
                "Your draft is longer than its story.",
                "Every scene is doing something and the book is still too slow.",
                "You are cutting words and the manuscript is not getting faster.",
            ],
            "context": "Length is a structural property, not a line-level one; cutting adjectives rarely changes how long a book feels.",
            "stages": ["the structural audit", "the scene list", "the line pass's position"],
            "openers": [
                "Work at the scene level before the sentence level: merge scenes that share a function, cut the scenes that change nothing, and relocate material that is good but positioned wrong. Word-level cuts cannot fix a book with too many scenes.",
                "Reason about what the draft is repeating. Redundant explanation, restated emotion, and behavior that repeats an established trait are the three most common sources of a manuscript that is longer than its story, and all three are cuttable at the structural level.",
            ],
            "closers": [
                "Commit to cutting and merging at the scene level before any line pass, and to measuring progress by pressure per page rather than by word count.",
                "Remove the scenes that change nothing and the explanations that repeat what the draft has shown, and leave the line pass for last.",
            ],
        },
    ],
    "traps": [
        {
            "id": "explaining_to_repair",
            "frames": [
                "Your revision adds explanations where the draft was unclear.",
                "You are fixing confusion by telling the reader what is happening.",
                "The repaired draft is clearer and longer.",
            ],
            "slide": "Every unclear moment is being solved with an explanation. The new sentences clarify the immediate confusion, so each repair looks successful, and the draft accumulates passages in which the narrator explains what the scene failed to establish.",
            "stages": ["the clarity repair", "the line pass", "the scene audit"],
            "openers": [
                "The pull is toward instruction, and the correction is toward evidence. Reason about what the scene could show instead, then move the necessary facts to a position where the reader can use them and delete the explanation.",
                "Reason past it by treating each explanatory passage as a diagnosis: what did the scene fail to establish, and can it be established in action? Explanations mark structural gaps, and the gap is the thing to fix.",
            ],
            "damage": "Explanation-as-repair produces drafts that are understandable and inert. The reader is told what to conclude before the conclusion forms, the text loses the trust that makes reading pleasurable, and the revision has lengthened the book in exactly the places that were slowing it down.",
            "reason_past": "Reason past it by relocating facts and staging conclusions. A scene that has been repaired by reordering is shorter than the broken version, while a scene repaired by explanation is longer, and that difference is the diagnostic.",
            "closers": [
                "Commit to repairs that reorder and stage rather than explain, and treat each explanatory passage as a pointer to a scene that needs work.",
                "Fix the scene until the explanation is unnecessary, then delete the explanation.",
            ],
        },
        {
            "id": "cutting_the_wrong_thing",
            "frames": [
                "You are cutting to reach a word count.",
                "Your revision removes material that carries character.",
                "The draft is shorter and less interesting.",
            ],
            "slide": "Cuts are being made by convenience rather than by function. The easiest material to remove is the specific, odd, character-bearing detail, so the draft loses its texture first and its excess last, arriving at a lower word count and a flatter book.",
            "stages": ["the structural audit", "the scene list", "the line pass"],
            "openers": [
                "The pull is toward the target, and the correction is toward function. Reason about what each passage does for the story and cut by that standard; the material that carries voice, character, or local specificity is the last thing to remove.",
                "Reason past it by cutting obligations rather than words: scenes that change nothing, explanations the reader does not need, and beats that repeat an established trait. Structural cuts remove more length and cost the draft less.",
            ],
            "damage": "Convenience cutting hollows a manuscript. The book reaches its target length while losing the particular material that made it feel inhabited, and readers describe the result as competent and forgettable, which is the failure that revision by word count reliably produces.",
            "reason_past": "Reason past it by cutting at the scene level first, where removals are large and the losses are structural rather than textural, and by protecting the draft's specific material explicitly.",
            "closers": [
                "Commit to cutting obligations rather than details, with the specific and character-bearing material named as protected.",
                "Reach the target by removing scenes and redundancies, and keep the texture that makes the book particular.",
            ],
        },
        {
            "id": "smoothing_voice",
            "frames": [
                "Your revision is making every chapter sound alike.",
                "You are removing irregularities that carried character.",
                "The repaired draft reads more evenly and less distinctly.",
            ],
            "slide": "Consistency is being applied where variation was doing work. Unusual constructions, odd details, and shifts of register are all normalized, so the book becomes uniformly competent, and the voice that made the first draft worth reading is gone by the third pass.",
            "stages": ["the line pass", "the style consistency check", "the second pass"],
            "openers": [
                "The pull is toward evenness, and the correction is toward distinction. Reason about which irregularities are errors and which are the draft's voice, then protect the second category before beginning the pass.",
                "Reason past it by defining the voice in specific terms: permitted constructions, characteristic moves, and the material the draft is allowed to be strange about. A pass with a definition protects more than a pass with a feeling.",
            ],
            "damage": "Flattened drafts lose their readers at the first page. Voice is what makes a manuscript recognizable, and revision that files it down trades the draft's one unrepeatable asset for a consistency that nobody was asking for.",
            "reason_past": "Reason past it by separating clarity problems from stylistic preferences, and by listing what the revision is not allowed to change. Voice is maintained by being described rather than by being remembered.",
            "closers": [
                "Commit to repairing clarity while protecting voice, with the draft's characteristic moves named before the pass begins.",
                "Normalize confusion and repetition, and leave the draft's particular manner alone.",
            ],
        },
    ],
    "discipline": [
        "Diagnose before repairing: name the effect the draft is failing to produce, then find the decision that would produce it.",
        "Choose among cut, merge, relocate, or strengthen before rewriting, and prefer the move that removes work rather than adds it.",
        "Cut obligations rather than words, protect the material that carries voice, and leave the line pass until last.",
    ],
    "themes": [
        {
            "id": "diagnostic_pass",
            "frames": [
                "You are rereading a finished draft and want to know what is wrong with it.",
                "You want a revision plan rather than a set of impressions.",
                "You are deciding where to begin repairing a manuscript.",
            ],
            "question": "How is a draft diagnosed so that the revision addresses causes rather than symptoms?",
            "openers": [
                "Diagnose in a fixed order: the story's spine first, then the chapters' functions, then the scenes' turns, then the information schedule, then the prose. Reading downward keeps a structural fault from being treated as a line problem, which is the most expensive mistake revision makes.",
                "A diagnostic pass produces a list of faults with causes attached rather than a feeling about the manuscript. Each symptom maps to a small number of structural causes, and choosing between them is what the revision plan is for.",
            ],
            "middles": [
                "Read for the reader's experience rather than the author's intention: where attention slips, where the situation becomes unclear, where a choice arrives without a reason. Those three readings locate most of what is wrong in a draft.",
                "Write the chapter functions from the draft rather than from the plan, and compare them with the outline. The chapters that have drifted from their function are the ones whose revision unlocks the rest.",
                "Check the balance of scene types across the draft: too many confrontations exhaust the reader, too many conversations stall the story, and too few quiet scenes mean nothing is established well enough to be threatened.",
                "Track the protagonist's want at every chapter. Where it cannot be named, the chapter is being organized around events rather than around a person, and that diagnosis usually explains both slowness and low stakes.",
                "List every promise the draft makes and find its payment. Unpaid threads are the reader's unfinished business, and the list is the fastest way to see whether the draft is complete or merely ended.",
                "Rank the faults by how much revision each one forces. Fixing the highest-ranked fault first is what stops a revision from expanding indefinitely, because most of the smaller faults disappear with it.",
            ],
            "closers": [
                "Commit to a diagnosis with causes, an order of repair, and criteria that will show when each one is finished: the spine, then functions, then scenes, then information, then prose.",
                "Produce the fault list with causes attached, then revise the largest cause first and re-diagnose afterward.",
            ],
        },
        {
            "id": "repair_without_damage",
            "frames": [
                "You are reworking a draft that mostly works.",
                "You want to fix the problems without losing what is good about the manuscript.",
                "You are deciding how far the revision is allowed to reach.",
            ],
            "question": "How is a draft repaired so that the fixes do not damage what already works?",
            "openers": [
                "Repair is bounded by two lists: what must change and what must survive. Writing both before opening the file is what keeps a structural repair from becoming a rewrite that loses the draft's best material and the writer's confidence along with it.",
                "The safe repair is the smallest change that removes the cause. Deciding that principle before starting is what converts revision from an appetite into a procedure, and it is what keeps a manuscript from being improved until it is worse.",
            ],
            "middles": [
                "Mark the fixed points: the scenes that work, the voice that holds, and the material the ending depends on. Fixed points constrain the repair, and constraint is what makes a revision finishable.",
                "Make one structural change at a time and re-read the chapters it touches before making the next. Parallel changes produce a manuscript whose parts no longer fit, which is a larger problem than the one the pass began with.",
                "Re-check the ending's conditions after every structural change. The ending is the most dependent part of a book and the first thing that breaks when an earlier chapter is altered.",
                "Keep a record of what was changed and why, so the second half of the revision is consistent with the first. Unrecorded changes are how continuity damage enters a manuscript during revision.",
                "Distinguish a fault from a preference before acting on it. Preferences are the bulk of revision notes and the source of most damage, because they are indistinguishable from real faults while they are being applied.",
                "Stop when the criteria are met rather than when the pages stop improving. Further passes at that point change the book rather than repairing it.",
            ],
            "closers": [
                "Commit to bounded repair: fixed points protected, one structural change at a time, the ending re-verified after each, and criteria that end the pass.",
                "Choose the smallest change that removes the cause, protect what works, and finish when the criteria are satisfied.",
            ],
        },
    ],
    "principles": [
        "Symptom, cause, repair: every revision decision should trace to a cause rather than to a feeling about the pages.",
        "Cut, merge, relocate, strengthen: choose the move that removes work before rewriting anything.",
        "Protect what works and verify the ending after every structural change.",
    ],
}
