"""Prose style: clarity, restraint, rhythm, and the avoidance of machine tics."""

CAT = {
    "id": "prose_discipline",
    "label": "Prose style and machine-tell avoidance",
    "moves": {
        "invisible_prose": [
            "Treat the prose as a delivery system for the scene, not as an exhibit. The sentence that draws attention to its own construction spends the reader's attention on the writing, and the reader's attention is the story's working capital. Decide which few moments in the chapter are permitted to be beautiful, and write everything else plainly enough that those moments carry weight.",
            "Prefer simple, precise diction. Plain words used exactly outperform elaborate words used approximately, and the elevated register invites the reader to notice the author, which is the opposite of what a scene needs. When a larger word is tempting, ask whether it adds information the ordinary word cannot.",
        ],
        "rhythm": [
            "Use sentence length as a pacing instrument and vary it deliberately. Speed and weight live in short sentences; observation, memory, and complicated processing live in longer ones; a chapter whose sentences are all the same length has told the reader that everything in it matters equally, which is never true.",
            "Watch for repeated structures across consecutive paragraphs, particularly repeated openings and repeated three-beat lists. Habitual rhythm becomes the reader's primary impression of the voice, which means a tic noticed once will be noticed for the rest of the book.",
            "Refuse manufactured fragmentation. Short fragments thrown in for emphasis are a resource with a very small budget, and once the reader has seen the trick they stop being moved by it and start predicting it.",
        ],
        "restraint": [
            "Notice when a passage is exceeding its importance. Two metaphors where one would do, three descriptions of the same object, an extra clause of atmosphere: each addition dilutes the strongest element present. Cut to the strongest and let the rest of the page stay quiet.",
            "Keep the emotional and stylistic temperature even across a chapter except where the material genuinely spikes. Uniform intensity is the same as no intensity, and a book that is always at its maximum has no way to signal when something matters.",
        ],
        "machine_tells": [
            "Plan against the specific shapes that make machine-written prose recognizable: the repeated negate-and-redefine construction, rhetorical questions used for emphasis, em dashes doing the work of commas and periods, filter verbs like felt, seemed, and noticed, and the constant three-item list. Individually each is acceptable; as habits they are diagnosis.",
            "Keep the emotional shorthand out of the draft: widened eyes, racing hearts, caught breath, tightened jaws, clenched hands. These are the most available indicators of feeling and therefore the least informative, and their presence at high frequency is the clearest signal that a passage is being produced rather than written.",
            "Avoid the closing gesture. The paragraph-ending sentence that dramatizes what was just said, the chapter that ends by announcing significance, the phrase that promises the reader something terrible is coming: these are rhetorical habits that make a book sound like a trailer for itself, and they prevent the reader from arriving at conclusions independently.",
        ],
        "consistency": [
            "Apply the style rules continuously rather than at the start of the book. Drift is quiet and cumulative: by the middle chapters the prose has relaxed toward whatever is easiest to generate, and a book with two voices reads as a book with none.",
            "Where two stylistic options conflict, let the explicit rules decide, and where the rules are silent, let consistency decide. The target is a coherent voice sustained across hundreds of pages, not a set of impressive passages that could have come from different books.",
        ],
    },
    "problems": [
        {
            "id": "intensity_plateau",
            "frames": [
                "Your chapters are written at a uniformly high pitch and the effect has flattened.",
                "You are drafting a chapter where every paragraph is trying to be memorable.",
                "The book's dramatic moments are not landing because the surrounding prose is at the same temperature.",
            ],
            "context": "Intensity is produced by contrast, and a book with no low register has no high one; the prose needs to be willing to be ordinary for most of its length.",
            "stages": ["the chapter's middle movement", "the sequence after a major event", "the book's second act"],
            "openers": [
                "Decide where the chapter's one or two peak moments are and write the rest of it plainly. The ordinary prose is not failed prose; it is the material against which the peaks register, and it also gives the reader room to breathe, which is what makes them keep reading through a long book.",
                "Plan the chapter's intensity as a curve with a floor as well as a ceiling. Note where the writing can be quiet, functional, and unremarkable, and protect those stretches from improvement, because upgrading them is how a book loses its dynamic range.",
            ],
            "closers": [
                "Write the chapter with one or two strong moments and keep the rest in a plain register that carries information and moves the scene. The peaks will land harder for the contrast and the reader will stay.",
                "Set the peaks deliberately and let everything between them be serviceable. Draft the quiet passages without embellishment and let them do their work.",
            ],
        },
        {
            "id": "style_drift",
            "frames": [
                "You are far into a long book and the prose no longer sounds like the chapters that opened it.",
                "You are drafting in a long session and notice the sentences becoming more generic as they go.",
                "The style rules that governed the first act have faded out of the writing.",
            ],
            "context": "Voice decays over long generations unless the explicit style rules are treated as constraints on every chapter rather than as descriptions of how the book began.",
            "stages": ["the middle of the book", "a long drafting session", "the chapters after a complex sequence"],
            "openers": [
                "Before drafting, re-read the style rules as active constraints and choose the three that this chapter is most likely to violate. Drift happens precisely where the material is hardest to write, and naming the rules in advance is what keeps the hardest chapters inside the book's voice.",
                "Treat the voice as a property of the whole book rather than of the current paragraph. Any passage is only as good as the surrounding pages allow, and a brilliant paragraph that breaks the register costs more than it earns, which means the correct move is often to write the scene plainly.",
            ],
            "closers": [
                "Draft the chapter against the explicit rules and re-read the opening of the book during the work rather than after it. Keep the voice as a monitored constraint, and the last chapters will sound like the first.",
                "Hold the register deliberately through the difficult stretch, choosing consistency where the material invites a different mode.",
            ],
        },
        {
            "id": "tells_under_speed",
            "frames": [
                "Your fastest passages contain the most formulaic prose.",
                "You are drafting an action or emotional sequence and the sentences are defaulting to templates.",
                "You notice your dialogue attributions and emotional beats have become mechanical.",
            ],
            "context": "Machine tells cluster where generation speed is highest, so the passages that need the most control are exactly the ones that receive the least.",
            "stages": ["the action sequence", "the emotional peak", "the dialogue-heavy stretch"],
            "openers": [
                "Decide before drafting which three tells this chapter is at risk of and hold the positive replacement for each: a specific behavior instead of the shorthand, a period instead of the dash, a concrete particular instead of the atmospheric filler. Replacing a reflex with a decision is the only reliable method, since simply forbidding the tell tends to leave a gap where it was.",
                "Slow down in the draft's fastest moments and spend the extra attention on construction rather than on vocabulary. Speed is where the templates arrive, and the antidote is not a larger word but a different decision about what the sentence is doing.",
            ],
            "closers": [
                "Write the fast passages with the positive decisions in place, and check the dialogue and emotional beats for reflex phrasings before moving on. The chapter will read as written rather than produced.",
                "Keep the replacement decisions in hand and apply them at drafting speed. Where a template is the easiest option, choose the specific instead.",
            ],
        },
    ],
    "traps": [
        {
            "id": "literary_performance",
            "frames": [
                "You are tempted to make each paragraph demonstrate craft rather than deliver the scene.",
                "Your drafting has begun producing elaborate constructions that feel like quality.",
                "You are writing a passage whose elegance is outrunning its information.",
            ],
            "slide": "The prose thickens: unusual verbs, inverted constructions, restrained punctuation used as an effect, metaphor in every paragraph. It feels like literature while drafting, and it is the most available way to signal seriousness, which is why it is the most common failure of writing produced at speed.",
            "stages": ["the opening chapter", "the scene of high emotion", "the description of a significant place"],
            "openers": [
                "You can feel the writing reaching for significance, dressing ordinary material in elaborated syntax. The pull is strong because it feels like effort and because the sentences look good in isolation. Reason past it while drafting and keep the ordinary material ordinary.",
                "The temptation is to write the chapter as a demonstration. Refuse it now: the reader's experience of a scene is damaged by prose that asks to be admired, and admiration is not attention.",
            ],
            "damage": "Performed prose spends the reader's attention on the writing rather than on the story, and it makes the honest passages that follow look thin by comparison, which pushes the whole book upward in register until nothing can land. It also produces a recognizable signature, and a signature is the opposite of an invisible voice.",
            "reason_past": "Reason past it by choosing one or two moments for elaboration and writing the rest in plain, exact sentences. Where the elaborate line feels necessary, ask what it adds that a plain statement would not, and where the answer is emphasis alone, cut it.",
            "closers": [
                "Write the chapter in plain prose with two deliberate exceptions, and refuse the register that asks for admiration. The scene will carry the reader further than the performance would.",
                "Keep the language functional and precise, and reserve visible craft for the moments that are doing structural work.",
            ],
        },
        {
            "id": "sentence_machine",
            "frames": [
                "Your paragraphs all have the same shape and the rhythm has become audible.",
                "You notice that consecutive sentences begin with the same construction.",
                "Your description has settled into a repeating pattern of clause, clause, dramatic short sentence.",
            ],
            "slide": "The template settles in: a medium sentence, an extension, a fragment for emphasis, then a paragraph-ending sentence that comments on what was described. It is fluent and it reads as competent, and after four or five repetitions the reader hears machinery rather than prose.",
            "stages": ["the chapter's descriptive passages", "the middle of a scene", "any long passage of interiority"],
            "openers": [
                "You can hear the pattern forming: the same rhythm arriving paragraph after paragraph. Refuse it in the drafting by varying deliberately: different openings, different lengths, different places for the emphasis. Rhythm should be chosen per moment rather than repeated as a signature.",
                "The pull is toward the shape that worked last time. Notice it and break it, since consistency of sentence architecture is what makes a page feel generated rather than composed.",
            ],
            "damage": "A single repeated shape flattens the scene's pacing, because pacing is carried by variation, and it also removes the reader's sense of a voice making decisions. Machine rhythm is one of the tells that readers register long before they can name it, and its presence makes even good material feel synthetic.",
            "reason_past": "Reason past it by deciding the rhythm for the passage before writing it: where speed belongs, where weight belongs, and where the writing should lengthen to allow processing. Then write into that shape rather than into the one that comes most easily.",
            "closers": [
                "Write the passage with deliberate variation in sentence length, opening construction, and the placement of emphasis. Where three sentences fall into a shape, break the third one.",
                "Choreograph the rhythm consciously and keep any repeated construction down to a single appearance per page.",
            ],
        },
        {
            "id": "explaining_after_showing",
            "frames": [
                "Your draft follows a strong behavioral beat with a sentence that explains it.",
                "You are writing a scene in which the reader has understood something and the narration confirms it.",
                "You keep ending passages with a line that tells the reader what the passage meant.",
            ],
            "slide": "The clarifying sentence arrives immediately after the material that did the work. It feels like completeness and it is the most common way a good beat is spent, and the habit strengthens as the chapter gets more ambitious, so the most important scenes end up the most over-explained.",
            "stages": ["after an emotional turn", "the end of a reveal", "the paragraph following a decision"],
            "openers": [
                "You can feel the sentence approaching that will make sure the reader got it. Refuse it in the drafting and leave the beat to stand: the reader who has just inferred something does not need confirmation, and the one who has not is better served by a stronger beat than by a caption.",
                "The pull is toward closure and clarity at the end of a scene. Reason past it now, because every explanatory line spends a piece of the reader's trust and the account is difficult to refill.",
            ],
            "damage": "Explanations after showing teach the reader that the narration will resolve any ambiguity, which converts reading from participation into reception. Over a book, this makes the reader stop assembling meaning, and the emotional moments that depend on inference stop working even when they are executed correctly.",
            "reason_past": "Reason past it by ending the beat on the strongest concrete element and moving to the next thing without comment. Where clarity genuinely requires a statement, put it earlier as a fact, before the scene enacts it, so the enactment is not annotated.",
            "closers": [
                "End the sequence on the behavior or the physical fact and go on to the next movement. The reader will take the meaning and keep it.",
                "Draft the beat and then delete the sentence that explains it, keeping whatever the following scene needs as an action rather than a statement.",
            ],
        },
    ],
    "discipline": [
        "Before drafting, choose the chapter's one or two permitted showpieces and accept that the rest of the prose will be plain. This decision is what protects the peaks.",
        "During the draft, keep the specific tells in mind as positive decisions rather than prohibitions: the period instead of the dash, the concrete detail instead of the atmospheric phrase, the individual reaction instead of the shorthand.",
        "After the chapter, read only the sentence openings and the paragraph endings. If more than two openings share a construction, or most paragraphs end in a dramatic statement, the rhythm has become a template.",
    ],
    "themes": [
        {
            "id": "voice_as_constraint",
            "frames": [
                "You are planning how a long book will maintain one voice across hundreds of pages.",
                "You want the style rules to function as generation constraints rather than as revision checklists.",
                "You are deciding how to keep the prose from drifting toward the easiest available register.",
            ],
            "question": "How does a style guide become a live constraint on generation rather than a document about the book?",
            "openers": [
                "A style guide works only if it is consulted as a set of decisions at the moment of writing. Convert each rule into a positive instruction that can be executed at drafting speed, a decision to make rather than a fault to avoid, and the rules will operate on the prose as it is produced rather than after the fact.",
                "Plan the voice as a maintained system: a small set of permitted elaborations, a list of tells with their replacements, and a rule for resolving conflicts between preferences. Then the consistency across a long book becomes a matter of process rather than of memory.",
            ],
            "middles": [
                "Give the rules priority in specific terms: where two stylistic options conflict, the explicit rule wins, and where the rules are silent, consistency with the surrounding book wins over local improvement. Ambiguity about precedence is what allows drift.",
                "Budget the elaborations across the whole book rather than per chapter. Knowing that there are a limited number of showpieces available changes drafting decisions at the margin, which is where the voice is actually decided.",
                "Build in a periodic check that compares the current chapter against the early chapters on the measurable features: sentence length distribution, ratio of description to action, density of figurative language, and frequency of the named tells. Measured drift is correctable; felt drift is usually invisible until the end.",
                "Keep the rules aimed at enabling rather than forbidding. A style guide made only of prohibitions leaves gaps where the habits were and produces prose that is careful without being alive, whereas positive instructions give the drafting something to do instead.",
            ],
            "closers": [
                "Treat the style guide as an operating procedure: positive decisions at drafting speed, explicit precedence when preferences conflict, and periodic measured comparison against the opening chapters. The voice will hold because it is being maintained rather than remembered.",
            ],
        },
        {
            "id": "tell_avoidance_strategy",
            "frames": [
                "You want to design the book's prose against the recognizable patterns of machine writing.",
                "You are planning a style guide whose purpose is to prevent a specific family of tics.",
                "You are thinking about which surface habits most damage a long manuscript.",
            ],
            "question": "How should the avoidance of recognizable machine-writing patterns be built into the writing process rather than reviewed afterward?",
            "openers": [
                "Tells are best handled as a design problem rather than a polishing problem, because they are produced by generation speed and are therefore most frequent exactly where the writer is least likely to notice them. Decide the replacements in advance, attach each one to the situation that triggers the reflex, and the correction happens during composition.",
                "Rate the tells by damage rather than by visibility. The highest-cost patterns are the ones that change what the prose does: explanatory closers that stop the reader inferring, habitual emotional shorthand that erases characterization, and rhythmic templates that flatten pacing. Vocabulary oddities are the cheapest problem and the easiest to fix.",
            ],
            "middles": [
                "Attach each tell to a positive substitute: the individual reaction for the physiological shorthand, the concrete particular for the atmospheric abstraction, the specific rhythm for the template, the period for the dash, the unnamed beat for the explanatory line.",
                "Watch the density of surface features that accumulate invisibly: filter words, hedges, adverb padding, repeated name use where a pronoun is natural. Individually harmless, collectively they produce the impression of a text that is being generated rather than written.",
                "Guard the register of the book's most important passages most carefully, since that is where the reflex habits gather and where their cost is highest. The final act should be the most deliberately written part of the manuscript, not the fastest.",
                "Keep the calibration book-specific rather than generic: some constructions are legitimate in a given voice and fatal in another, so the guide should specify what this book permits alongside what it forbids.",
            ],
            "closers": [
                "Commit to a tell-avoidance procedure built on positive replacements, damage-weighted priorities, and extra attention at the passages that matter most. Write the book's most important scenes as its most controlled ones.",
            ],
        },
    ],
    "principles": [
        "Restraint before excess: the strongest element in a passage is diluted by every additional effect placed beside it.",
        "Invisible prose before impressive prose: the reader's attention belongs to the scene, and any sentence that takes it has to earn the theft.",
        "Consistency of voice before local brilliance: a book is a voice sustained, not a collection of passages.",
    ],
}
