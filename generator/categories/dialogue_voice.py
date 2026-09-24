"""Dialogue, voice, subtext, and humor."""

CAT = {
    "id": "dialogue_voice",
    "label": "Dialogue, voice, subtext, and humor",
    "moves": {
        "spoken_shape": [
            "Decide what each speaker wants out of the exchange and what each is unwilling to say before writing any of it, because those two facts generate the conversation's shape more reliably than any line-level plan. A conversation with two purposes in it is a scene; a conversation with one shared purpose is a briefing.",
            "Write speech the way people speak under the pressure of a scene: with interruptions, hesitations, tangents, corrections, and unfinished thoughts. Efficiency is a property of written information transfer, not of speech, and a conversation where every contribution advances the topic will read as transcription of an outline rather than as people talking.",
        ],
        "voice_differentiation": [
            "Build each character's verbal world from personality, background, confidence, age, relationship, and current circumstance, and keep it stable across the book. Vocabulary, sentence length, tolerance for silence, willingness to interrupt, and preferred method of evasion should all differ measurably between characters.",
            "Let relationships determine register inside a single character: the same person speaks differently to a superior, a sibling, a stranger, and someone they are trying to impress. Those differences are among the most economical ways to show a relationship without summary.",
        ],
        "subtext_and_evasion": [
            "Use subtext and evasion as the defaults. Characters can lie, stall, deflect, answer a different question, defend against an attack nobody made, or talk about something adjacent while the real subject waits underneath. The gap between what is said and what is happening is where dialogue becomes drama.",
            "Let dialogue reveal relationships rather than information. Who defers, who interrupts, who tolerates silence, who explains, who tests, and who refuses to answer carries more about the state of the connection between two people than any amount of exchanged fact.",
        ],
        "humor": [
            "Treat humor as characterization with a mechanical consequence. What a person finds funny shows what they notice, what they value, and what they need to keep at a distance. Decide which characters use humor as armor, as aggression, or as approach, and let the comedy fall out of those purposes rather than being inserted.",
            "Keep the wit budget low and distributed. Not every exchange can be sharp, not every character can produce the perfect line, and the perfect response that arrives five minutes too late is more useful characterization than the instant one. Humor should also be allowed to fail on the page, because a joke that lands awkwardly or is ignored is more true to how people behave than a run of successful laughs.",
        ],
        "register_discipline": [
            "Keep exposition out of speech. Information in dialogue should be something a person has a reason to say aloud: a challenge, a correction, a lie, a question concealing another question. Where the reader needs a fact and no speaker would state it, move the fact out of the conversation entirely.",
            "Resist the temptation to make every exchange a showcase. Uniformly witty, uniformly articulate dialogue flattens the cast into the same voice and makes the passages that should land feel no different from the surrounding chatter.",
        ],
    },
    "problems": [
        {
            "id": "exposition_in_dialogue",
            "frames": [
                "A scene of your book must deliver background information that the speakers already know.",
                "Your chapter needs the reader to understand a situation whose parties are all present and informed.",
                "You are drafting a conversation whose purpose is to explain something the plot depends on.",
            ],
            "context": "Information should enter dialogue only through a reason to speak: conflict, correction, test, lie, or bid for advantage.",
            "stages": ["the early chapter that establishes the situation", "the scene before a major decision", "the conversation with an ally"],
            "openers": [
                "Before drafting, find the conflict that makes the information worth saying aloud. Two people who both know a fact will discuss it only if they disagree about what it means or what should be done, and that disagreement lets the reader learn the fact while watching a relationship operate. Where no disagreement exists, the material belongs in narration, behavior, or consequence rather than in speech.",
                "Convert the exposition into an act. A character can test a subordinate, warn an ally, threaten a rival, or lie about the same material, and each of those carries the information while also advancing the scene. Decide what the speech does, then let the content arrive inside the doing.",
            ],
            "closers": [
                "Write the conversation as a contest of purposes with the information embedded in what is contested, and have every statement be a move rather than a fact supplied for the reader.",
                "Route the exposition through conflict, correction, or evasion, and let the reader assemble the background from what the characters argue about.",
            ],
        },
        {
            "id": "voice_blur",
            "frames": [
                "Your characters sound like each other on the page.",
                "You are drafting an ensemble scene and the dialogue could be redistributed among speakers without anyone noticing.",
                "You want the reader to be able to identify a speaker without attributions.",
            ],
            "context": "Voice is constructed from background, confidence, purpose, and relationship rather than from catchphrases or accents applied to the surface.",
            "stages": ["the ensemble scene", "the negotiation", "any conversation with three or more people"],
            "openers": [
                "Before drafting the scene, write down for each speaker what they want, what they will not say, how much they are willing to interrupt, and what kind of sentence they use when they are stalling. Those four decisions produce separable voices without any surface styling, because each one changes the shape of what appears on the page.",
                "Choose the register per relationship: a person who speaks in full paragraphs with a superior may speak in fragments to a sibling. Then the scene's dialogue encodes the social structure of the room, which is information the reader receives without being told.",
            ],
            "closers": [
                "Write the exchange with each speaker's purpose and resistance distinct, and check that no line could be moved to another character without damage. Voices will separate by construction rather than by decoration.",
                "Draft with the four decisions in force, and let relationship rather than vocabulary carry the difference between speakers.",
            ],
        },
        {
            "id": "humor_placement",
            "frames": [
                "You want humor in a chapter without weakening its tension.",
                "A serious scene in your book needs relief and you are deciding where it comes from.",
                "You are drafting a conversation that keeps producing jokes and the stakes are dissolving.",
            ],
            "context": "Humor belongs to character and circumstance; inserted levity that exists to relieve pressure signals that the book does not trust its own weight.",
            "stages": ["the tense conversation", "the scene after a loss", "the chapter's closing exchange"],
            "openers": [
                "Decide which character's comic instinct will operate and what it is protecting them from. Humor that emerges from a person's coping style deepens the scene and its stakes, while humor inserted to give the reader a break spends the pressure the scene has accumulated.",
                "Place the humor before or inside the pressure rather than immediately after its peak. A joke that arrives at the moment of maximum seriousness tells the reader the danger was not real, and the same joke five minutes earlier functions as character rather than as retreat.",
            ],
            "closers": [
                "Write the scene with humor generated by a specific character's coping mechanism and keep the peak clear of it. The levity will read as personality and the pressure will survive.",
                "Draft the exchange with the comic material attached to a person rather than to the moment, and let the serious beats end without a joke to soften them.",
            ],
        },
    ],
    "traps": [
        {
            "id": "witty_cast",
            "frames": [
                "Every character in your book is producing strong lines at speed.",
                "You are drafting a scene and the dialogue is uniformly sharp.",
                "You want the conversations to be entertaining and the competence is flattening the cast.",
            ],
            "slide": "The repartee arrives easily: everyone is quick, everyone is articulate, and every exchange ends on a good line. It is pleasant on the page and it removes the possibility of unequal relationships, since a cast that matches each other line for line has no social structure left to dramatize.",
            "stages": ["the ensemble scene", "the negotiation", "the meeting that opens the middle act"],
            "openers": [
                "You can feel the dialogue becoming a showcase where every speaker is equally equipped. Refuse it while drafting: let some characters be slower, let some be inarticulate under pressure, and let some win by refusing to engage at all.",
                "The pull is toward the satisfying exchange, and the cost is the cast's differentiation. Reason past it by deciding which characters can afford wit in this situation and which cannot, then writing the scene around that asymmetry.",
            ],
            "damage": "Uniform competence in speech erases the power differences that make dialogue dramatic, and it also makes the story's important conversations indistinguishable from its trivial ones. When everyone is equally impressive, nothing a character says carries weight, and the reader's sense of who holds advantage in a scene disappears.",
            "reason_past": "Reason past it by allocating verbal ability deliberately: age, confidence, education, exhaustion, and stakes should all constrain speech. Where a character would be quick, let them be quick about the wrong thing, which restores both the humor and the hierarchy.",
            "closers": [
                "Write the scene with unequal verbal capability and let the strongest line belong to whoever has the most at stake rather than to whoever is wittiest. The conversation will feel like a room full of people rather than a script.",
                "Draft with each character's verbal resources set by circumstance, and keep the brilliant line rare enough to matter.",
            ],
        },
        {
            "id": "information_transfer",
            "frames": [
                "Your dialogue exists mainly to move information from one character to another.",
                "You are drafting a scene whose purpose is to bring a character up to date.",
                "You notice that scenes involving new information all have the same shape.",
            ],
            "slide": "The briefing shape: one character explains, another listens, the reader receives. It is efficient and it is the most common way scenes become inert, because a character receiving information has nothing to do and the exchange has no resistance in it.",
            "stages": ["the scene after a discovery", "the conversation between allies", "the chapter that opens an act"],
            "openers": [
                "You can see the briefing forming, and the draft wants it because the plot needs the reader informed. Break the shape: introduce disagreement about the information's meaning, or have the receiver already know part of it and lie about what they know.",
                "The pull is toward the clean handoff of fact. Reason past it by deciding what each person wants from the exchange independent of the fact being exchanged, then writing the scene so that the information is a byproduct of that pursuit.",
            ],
            "damage": "Information-transfer scenes remove the reader's agency, because there is nothing to infer, and they also flatten characters into carriers of plot. Over a book, the reader learns that conversations are where facts appear and skips them, which is fatal when a later conversation is where the story actually turns.",
            "reason_past": "Reason past it by making every exchange a contest with an outcome: a test passed or failed, a lie believed or doubted, an alliance formed or refused. The information can still be delivered, but it should cost something to deliver.",
            "closers": [
                "Rewrite the scene's purposes so that the exchange has a winner and a loser, and let the information pass as a consequence of the contest rather than as its purpose.",
                "Give each participant a private objective and write the conversation so the reader learns the facts by watching the objectives collide.",
            ],
        },
        {
            "id": "underwritten_conflict",
            "frames": [
                "Your characters are being polite with each other in scenes that should be difficult.",
                "You are drafting an argument and the participants are being reasonable.",
                "You want the scene to escalate and the dialogue keeps resolving disputes rather than deepening them.",
            ],
            "slide": "The conversation becomes cooperative: each character grants the other's point, apologizes, or explains themselves clearly. It feels mature on the page and it means the scene has no engine, because conflict requires that at least one participant be unwilling to be satisfied.",
            "stages": ["the argument scene", "the negotiation", "the confrontation between allies"],
            "openers": [
                "You can feel the scene resolving itself before it has done anything. Refuse the maturity: give each participant a reason not to accept the other's account, and let the disagreement be about meaning or priority rather than about facts.",
                "The pull is toward reasonable discourse. Reason past it by letting each character be right about something the other cannot concede, so that agreement would cost one of them more than continuing costs.",
            ],
            "damage": "Cooperative dialogue removes stakes from the book's relationships and makes its conflicts external only, which means character cannot be revealed by disagreement. It also makes the eventual ruptures unconvincing, since the reader has never seen these people genuinely unable to accommodate each other.",
            "reason_past": "Reason past it by identifying what each participant needs to protect in the scene and writing the exchange so that either concession damages that thing. Conflict then arises from integrity rather than from aggressiveness.",
            "closers": [
                "Write the exchange so that each person is defending something real and neither can yield without loss, and let the scene end without resolution or with a bad one.",
                "Give each participant a position they cannot abandon and draft the conversation as an attempt to make the other abandon theirs.",
            ],
        },
    ],
    "discipline": [
        "Before drafting any conversation, write down what each participant wants, what each will not say, and what the exchange's outcome is, so that the scene has a direction before it has lines.",
        "During the draft, keep the exposition out and the subtext in: every statement should be a move in a contest rather than a delivery of fact, and no character should explain something another character already knows for the reader's benefit.",
        "After the chapter, read the dialogue for voice separation and for efficiency. If a speaker could be swapped without damage, the voice is not distinct; if the conversation resolves too neatly, it needs resistance.",
    ],
    "themes": [
        {
            "id": "voice_across_book",
            "frames": [
                "You are planning how a cast's voices will stay distinct across a long book.",
                "You want the relationships in a novel to be legible from speech alone.",
                "You are deciding how dialogue will carry character development over an entire arc.",
            ],
            "question": "How should voice and dialogue operate across a whole novel so that relationships and change are visible in speech rather than in summary?",
            "openers": [
                "Plan voice as a set of constraints per character: vocabulary range, sentence behavior, how they handle interruption, what they do when they are lying, and what they refuse to talk about. Constraints produce distinct voices without surface decoration, and they can be relaxed or tightened to show change under pressure.",
                "Plan relationship registers as a matrix: how each pair speaks to each other at the start, and how each pair should speak by the end. The differences between those two states are dialogue's version of character arc, and they can be delivered without anyone stating that a relationship has changed.",
            ],
            "middles": [
                "Let pressure alter speech measurably. A character who speaks in complete sentences should fragment under stress, and a character who evades should start answering directly when something finally matters; those shifts are visible to the reader as events.",
                "Keep the cast's verbal resources unequal and stable. Some people are inarticulate, some are fluent only about their work, some use humor as a wall; the inequality is what makes a conversation's outcome uncertain and what makes dialogue dramatic rather than decorative.",
                "Track the promises, lies, and refusals made in speech and let them return. Dialogue that leaves residue in later dialogue, an unkept promise raised again, a lie visible through a change of story, makes the book's conversations cumulative rather than episodic.",
                "Use silence deliberately across the book. Who withholds, when, and what it costs is as characterizing as anything said, and a scene that ends in silence can carry more weight than one that resolves in speech.",
            ],
            "closers": [
                "Commit to per-character verbal constraints, a relationship register matrix, and a ledger of spoken promises and refusals. Write each conversation as a move in those systems, and the book's relationships will be audible.",
            ],
        },
    ],
    "principles": [
        "Subtext before exposition: what is not said carries the scene, and speech exists to be a move rather than a delivery system.",
        "Individual voices before showcase dialogue: capability, background, and stakes should constrain speech, and the brilliant line should be rare enough to register.",
        "Character before comedy: humor emerges from who someone is and what they are protecting, not from an obligation to be entertaining.",
    ],
}
