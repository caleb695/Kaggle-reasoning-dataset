"""Information management between reader and characters."""

CAT = {
    "id": "information_management",
    "label": "Information management between reader and characters",
    "moves": {
        "asymmetry_map": [
            "Map who knows what at every structural moment: what the reader holds, what the point-of-view character holds, and what the other characters hold. Story energy lives in the gaps between these three positions, and each configuration produces a different effect, so decide the gap before the scene, not during it.",
            "Choose the asymmetry deliberately for each stretch of story. When the reader knows more than the character, every innocent scene carries dread; when the reader knows less, every ordinary detail becomes a candidate clue. Neither is superior, but they cannot be mixed casually within a sequence without leaking the design.",
            "Track the asymmetry as a moving system. Each scene shifts at least one of the three knowledge positions, and the direction of the shift is a decision: widening the reader-character gap increases irony, narrowing it increases alignment and relief. Plan the drift across a sequence the way you would plan a pressure curve.",
            "Watch the edges of the map. The moment a character learns something is as important as what they learn, because knowledge acquired under pressure changes decisions in ways knowledge acquired comfortably does not. Schedule the arrivals of knowledge at decision points, where the new information can do structural work.",
        ],
        "reveal_order": [
            "Order revelations by recontextualizing power, not by chronology. The best reveal is not the one that delivers the most new facts but the one that changes the meaning of the largest amount of material the reader has already absorbed. When sequencing disclosures, ask of each: how much of the past does this make different.",
            "Stage revelations in escalating order of significance, and let early ones teach the reader that the story is withholding honestly. A first reveal that reframes a small matter builds trust; each subsequent reveal should reach further back or deeper down than its predecessor. Design the staircase before placing the landings.",
            "Break large revelations into installments with distinct functions: the hint that makes the reader curious, the confirmation that makes them certain of the fact, and the context that makes them understand its meaning. Three beats carried across separate scenes outperform a single delivery, because each beat re-opens the question just as the last one closes.",
            "Time the reveal against the decision it empowers. Information released long before the choice it affects goes stale; released simultaneously with the choice, it reads as convenience. The strongest placement gives the character and the reader a short, pressured interval to understand what the new knowledge makes necessary.",
        ],
        "withholding_economy": [
            "Withhold only for structural gain, and pay for every concealment. A fact hidden from the reader must be hidden by a character's actual motive, a perception's actual limit, or a narrative position's actual constraint, and the hiding must cost something visible. Free concealment, where no one had a reason to stay silent, is the reader's first suspect.",
            "Let the shape of the silence be informative. What a character does not say in a given exchange, the question they decline, the subject they steer away from, tells the attentive reader that a withheld thing exists, which is often all the story needs. Design silences as deliberately as statements.",
            "Budget the reader's tolerance for not-knowing. Curiosity has a half-life: withhold past its expiry and the reader stops forming theories, which is the moment engagement dies. For each withheld fact, estimate how long the reader will carry the question gladly, and place the payment inside that window.",
            "Distinguish the withheld from the merely unknown. Facts the point-of-view character genuinely cannot access may stay dark honestly; facts they could access but do not seek require a motive the reader can respect. Audit every dark area of the story for which kind it is, and convert avoidable darkness into earned silence or into light.",
        ],
        "question_ledger": [
            "Keep a running ledger of open questions the reader holds, ranked by urgency: what they wonder about idly, what they are actively curious about, and what they ache to know. Every scene should collect on at least one entry and open at least one more, so the ledger never empties and never bloats.",
            "Retire questions with ceremony or with economy, as the question's rank deserves. The major questions need answers that arrive at moments of maximum leverage; the minor ones can be closed quietly in passing, as texture. But every entry must eventually be collected, and the ledger must be audited at each structural break.",
            "Nest questions inside each other. The surface question, will the plan succeed, should contain the deeper one, what is the plan actually for, which contains the deepest, who is this person becoming. When a surface question resolves, the nesting ensures a deeper one is already open underneath, and the reader never stands on empty ground.",
            "Let characters' questions diverge from the reader's questions. The character may need to know who sent the message while the reader has moved on to why the sender lied about the second name. That divergence is a sign the reader is ahead of the story's surface, which is exactly where a well-managed reader should be.",
        ],
        "channel_discipline": [
            "Define the channels through which the point of view can legitimately know things: direct witness, report from others, physical evidence, and inference. Every fact the narrative delivers should arrive through one of these, and the reader should be able, on reflection, to identify which channel it used.",
            "Keep inference honest. A character may deduce more than they have seen, but the reader must be able to retrace the deduction from evidence the narrative has already shown. When a character knows something the channels cannot yet have delivered, either plant the missing input earlier or let the character be wrong in the way their limited input would actually make them wrong.",
            "Use the constraints of a limited channel as sources of drama rather than obstacles to it. What the point-of-view character cannot see must be conveyed through behavior, absence, and consequence, and those indirections are where the reader's attention sharpens. The limit is not a restriction on the story; it is one of the story's engines.",
            "Audit each scene for channel violations before moving on: any knowledge in the narration that the character could not possess must be either cut, attributed to an accessible source, or converted into the character's mistaken inference. A single quiet violation teaches the reader that the limitation is decorative.",
        ],
    },
    "problems": [
        {
            "id": "central_secret",
            "frames": [
                "Your novel is built around a secret that would reorganize the protagonist's world if it came out.",
                "You are writing a story whose central fact must be kept from most of the characters, and from the reader, for a long stretch.",
                "Your narrative's engine is a concealed truth, and the management of that concealment is the craft problem the whole book turns on.",
            ],
            "context": "The central secret must be managed as a structure: every scene it touches either tightens or loosens its containment, and the cost of hiding it must press on the plot continuously.",
            "stages": ["the opening act", "the early middle of the book", "the long central stretch"],
            "openers": [
                "A secret is a debt that accrues interest. Every scene that depends on its concealment raises the price of exposure, and the story's tension is the interest rate. Decide now what the secret costs its keeper in each coming stretch, in behavior, in missed chances, in lies that compound, and let that cost be visible long before the secret itself is.",
                "Before writing further, fix the secret's containment system: who knows, who suspects, what evidence exists outside control, and what event would breach each wall. The plot of the middle is the slow failure of that system under pressure, so the system must be specific enough to fail in interesting ways.",
                "Decide the secret's two clocks: the internal one, how long the keeper can sustain the concealment, and the external one, when some outside pressure would surface it regardless. The story lives between the two, and whichever runs out first decides the shape of the crisis. Set both clocks in motion early.",
            ],
            "closers": [
                "Commit to the secret's accounting: the cost of each week of silence, the walls of the containment system, and the two clocks now running. Write the next scenes as movements of that system, with the pressure visible in behavior before anyone speaks of it.",
                "Fix what the concealment is doing to the keeper right now, and let the next scene be shaped by that deformation. The secret's weight is the story's tension, and it must be paid scene by scene, not saved for the reveal.",
            ],
        },
        {
            "id": "dramatic_irony",
            "frames": [
                "Your story puts the reader in possession of a fact that the point-of-view character does not have, and the gap must be maintained.",
                "You are writing a stretch where the reader knows the danger, the truth, or the identity that the character is moving blindly toward.",
                "Your narrative has opened a gap between reader knowledge and character knowledge, and the gap is the story's main tension.",
            ],
            "context": "Dramatic irony must be farmed, not just held: every scene inside the gap should harvest tension from what the reader knows, while the gap widens or narrows on a deliberate schedule.",
            "stages": ["the middle of the book", "the second act", "the approach to the crisis"],
            "openers": [
                "The gap between what the reader knows and what the character does is a field to be farmed, not a state to be maintained. Every scene inside the gap should put the character in contact with the known thing: touching it, circling it, deciding because of its absence. Decide which contacts the next stretch contains, and in what order the dread compounds.",
                "Before writing the ironic stretch, decide its trajectory: does the gap widen, with the character investing further in what the reader knows is false, or narrow, with the truth closing in on them. The two shapes produce different reading experiences, widening produces anguish, narrowing produces suspense, and the choice determines what every scene in the stretch must do.",
                "Audit the coming scenes for wasted irony: moments where the character's ignorance is present but unused. Inside the gap, every plan the character makes, every reassurance they give, every trust they extend should be load-bearing for the reader who knows better. Redesign any scene where the knowledge gap changes nothing.",
            ],
            "closers": [
                "Commit to the gap's trajectory and its harvest: each scene ahead puts the character in contact with what they do not know, and each contact raises the cost. Write the stretch as farming, not holding, and let the reader's dread compound on schedule.",
                "Fix the irony's payments: which innocent acts will now carry double meaning, which trusts will be extended toward the known danger. Write the next scene so the gap does work the character cannot see and the reader cannot miss.",
            ],
        },
        {
            "id": "recontextualizing_reveal",
            "frames": [
                "Your novel contains a reveal that will change how everything earlier is understood, and its placement is now being decided.",
                "You are writing toward a disclosure whose real power is retroactive: it will recolor scenes the reader has already lived through.",
                "Your story has a retroactive truth embedded in it, and the craft question is how to stage its detonation.",
            ],
            "context": "A recontextualizing reveal must be built backward from the moment of detonation: the earlier material planted innocent, the surface reading stable, and the new fact recasting the maximum amount of prior scene.",
            "stages": ["the middle of the book", "the second half", "the late middle"],
            "openers": [
                "Work backward from the detonation. List the scenes that the new fact will recolor, and for each, verify that it reads honestly on first pass, innocent on the surface, exact on the second. Any scene that only works after the reveal is a landmine, not a plant; fix it until both readings are true, then trust the double exposure.",
                "Decide how much of the book the reveal is allowed to recolor, and protect that allowance. The plant scenes must be written to a stricter standard than other scenes: every detail in them must serve the innocent reading so well that the second reading arrives as an overwhelming of the first, not a correction of a careless one.",
                "Before placing the reveal, test its timing against the reader's own reconstruction. If it arrives too early, the reader has not invested enough in the surface reading for the inversion to matter; too late, and the surface has had time to harden into assumption that feels cheated rather than reopened. Find the window where the first reading is fully lived but not yet owned.",
            ],
            "closers": [
                "Commit to the double exposure: every plant scene ahead is written for the innocent reading first, with the second reading latent in exact detail. Write toward the detonation point, and let nothing in the interim leak the second meaning.",
                "Fix the reveal's window and the list of scenes it will recolor, then write forward with two readings in hand at all times. The reveal will be strong exactly in proportion to how completely the first reading was believed.",
            ],
        },
        {
            "id": "limited_perception",
            "frames": [
                "Your novel is told through a point of view that cannot access key parts of the story, and the limitation must become an asset.",
                "You are writing a narrative whose viewpoint character sees less than the reader needs, and the gap must be bridged without cheating.",
                "Your story's perception channel is narrow by design, and you must now make the narrowness produce drama.",
            ],
            "context": "A limited perception channel must be exploited: its edges, its blind spots, and its failures of interpretation become the story's instruments for generating doubt, dread, and discovery.",
            "stages": ["the opening act", "the early middle of the book", "the long middle of the book"],
            "openers": [
                "The limitation is the instrument. Decide what this perception naturally misses: the meaning behind behavior, the content of other rooms, the intentions of people trained to conceal. Then decide which of the story's key facts will live precisely in those blind zones, so the reader's uncertainty is structural rather than artificial.",
                "Before writing the next stretch, inventory the character's perceptual edges: what they notice first, what they systematically misread, what they refuse to look at. The story's information will be delivered through those distortions, and the reader will learn the distortion's shape, which turns limitation into characterization.",
                "Plan the compensations honestly. The character cannot see everything, so the narrative must generate knowledge through report, evidence, and inference, each with its own reliability. Decide which channels this story uses, how each can mislead, and which lie will be believed longest.",
            ],
            "closers": [
                "Commit to the limitation as engine: the key facts live at the perception's edges, the distortions are consistent and informative, and every compensating channel has a stated reliability. Write the next scene from inside the narrowness, and let its shape do the story's work.",
                "Fix what the perception misses and how the story pays for what it cannot show, then write forward. The reader's uncertainty will be an instrument in your hands rather than a hole in the page.",
            ],
        },
        {
            "id": "final_disclosure_timing",
            "frames": [
                "Your novel is holding its biggest disclosure for the end, and the timing of that release is the last major structural decision.",
                "You are approaching the place in the story where the central unknown must finally be resolved, and the moment must be chosen.",
                "Your narrative has carried the reader's deepest question to within sight of its answer, and the placement of the answer will decide the ending's weight.",
            ],
            "context": "The final disclosure must be timed to land where it changes a decision, not merely satisfies a curiosity: after the last moment it could alter the story's course has passed, or just before, never comfortably between.",
            "stages": ["the final act", "the approach to the climax", "the last movement"],
            "openers": [
                "Decide what the final disclosure is for. If it only satisfies curiosity, place it late and let it be quiet; if it alters the meaning of the protagonist's choice, place it inside the decision's shadow, where the reader holds it while the choice is made. The timing is not a scheduling problem; it is a meaning problem.",
                "Work out the relationship between the disclosure and the climax: does the reader learn before the protagonist, so the final choice is watched with full knowledge, or after, so the choice is re-understood in the aftermath. Both orders are strong; they are different endings. Choose the one the story has been promising.",
                "Audit the cost of holding the question to the end: what the reader's patience will have been spent on, and whether the answer can bear the accumulated weight. If the disclosure cannot pay the interest, split it: release the factual part earlier, and hold only the meaning for the final pages.",
            ],
            "closers": [
                "Commit to the disclosure's placement and its function: what it changes, whose knowledge it enters, and what choice it shadows. Write toward that placement, and let the story's last unknown be spent where it buys the most.",
                "Fix the timing against the climax, and protect the interval around it: the pages before must sustain the question honestly, the pages after must show its meaning absorbed. Write the approach now, with the release point fixed in sight.",
            ],
        },
    ],
    "traps": [
        {
            "id": "contrived_silence",
            "frames": [
                "Your plot requires a character not to share information that they have every apparent reason to share.",
                "You are writing a scene where a secret's survival depends on someone staying silent without a motive to.",
                "Your story's concealment has hit the point where the only thing keeping it intact is the author's need for it.",
            ],
            "slide": "You feel the pull toward contrived silence: letting the secret survive this scene because no one mentions it, though any real person in the room would speak. The pull is quiet because the scene works on its surface; it just has a hole where a motive should be.",
            "stages": ["the early middle of the book", "the middle of the book", "the second act"],
            "openers": [
                "The scene ahead has a hole in it: the information that would naturally be spoken stays unspoken, and nothing in the character prevents them from speaking. The pull is to let the hole stand, since the plot needs the silence. Find the keeper's true reason instead, or accept that the secret breaks here and let the story grow from the breach.",
                "You are about to write a silence that the character has no motive to keep. The temptation is real, the plot depends on it, and the reader's nose is sharper than the plot. Before drafting, either give the silence a price the character is visibly unwilling to pay, or let the information go and restructure what follows.",
            ],
            "damage": "The damage is a broken contract with the reader's rationality: they extend belief to a story that hides things for reasons, and every unmotivated silence teaches them the hiding is the author's, not the character's. Once that suspicion is awake, the story's genuine mysteries are read as manipulations, and even honest reveals feel cheap.",
            "reason_past": "Reason past it while writing by pricing every silence: for each fact a character withholds, establish what speaking would cost them, in fear, shame, advantage, or danger to someone else, and make the price visible in the scene where the silence happens.",
            "closers": [
                "Commit to the priced silence: the keeper's reason will be present in the scene as motive, behavior, and cost, not as absence. Write the withholding as an act with a visible price, and the reader will carry the secret with the character.",
                "Refuse the free hole. Either the silence earns its keep through motive and cost, or the information enters the story here and the plot absorbs the shock. Decide now, and write the scene with the decision honored.",
            ],
        },
        {
            "id": "frontloaded_history",
            "frames": [
                "Your novel's world has a history that the reader needs, and the pressure to explain it all up front is strong.",
                "You are opening a story whose present depends on past events the reader cannot yet see.",
                "Your draft's early pages keep filling with explanation of how things came to be this way.",
            ],
            "slide": "You feel the pull toward the front-loaded past: settling accounts with the history early, explaining how the world got this way, so the reader can be given a clean bill of understanding before the story starts. The pull is the desire to be legible.",
            "stages": ["the opening chapters", "the very first scenes", "the first act"],
            "openers": [
                "The opening is filling with history, and the pull is to finish the job: deliver the whole past, clear the decks, then begin. The job is the trap. Decide what the reader needs of the past before the first turn, deliver only that, inside scenes under pressure, and let the rest of the history be earned out over the book.",
                "You can feel the desire to establish everything before anything happens: the full ledger of how things came to be. The desire is thoroughness and the effect is delay, because readers do not store history they have no use for yet. Select the minimum past the first movement needs, and stage even that as present friction.",
            ],
            "damage": "The damage is a dead opening and a distrusted reader: front-loaded history answers questions no one has asked yet, and questions are the currency of attention. The reader who is briefed before they are engaged arrives at the first real event without appetite, having spent their curiosity on information they could not use.",
            "reason_past": "Reason past it while writing by converting each piece of history into a present-tense pressure: decide which current behavior, law, grudge, or scar the fact explains, and deliver the fact at the moment the reader becomes curious about that pressure, never before.",
            "closers": [
                "Commit to curiosity-first delivery: no history enters the story before a present pressure makes the reader want it. Write the next scene with the past emerging as explanation of friction, and let the unneeded remainder stay in your notes.",
                "Refuse the briefing. Fix the minimum past the first turn requires, find the scenes of present pressure where each piece becomes wanted, and deliver them there. The book will begin in motion, and the past will arrive as answers rather than as homework.",
            ],
        },
        {
            "id": "reset_reveal",
            "frames": [
                "Your story has just revealed something significant, and the reveal's aftermath is threatening to be merely informational.",
                "You are writing past a disclosure that landed as new facts but changed nothing on the ground.",
                "Your narrative's latest reveal answered a question and left the story running on the same rails it was on before.",
            ],
            "slide": "Planning past the upcoming reveal, you notice it functions as a reset: the reader will learn the fact, the story will acknowledge the fact, and then everything continues as before. The pull is toward revelations that decorate rather than redirect, because they are easier to stage.",
            "stages": ["the middle of the book", "the second act", "the late middle"],
            "openers": [
                "The reveal on your plan is an event without consequence: the fact lands, the characters absorb it, the plot proceeds. You can feel how cheaply it would be delivered. Rebuild it as pressure: the disclosure must change what someone wants, make a plan impossible, or transfer an advantage, or it is not a story beat at all.",
                "You are about to spend a reveal, and the draft's plan lets it evaporate into information. A disclosure is structural only if the board is different after it: someone's position has moved, someone's options have closed. Decide what this revelation costs and whom, before you let the reader have it.",
            ],
            "damage": "The damage is inflationary: reveals that change nothing devalue revelation itself, so when a genuinely consequential disclosure arrives, the reader has been trained to wait for the story to resume. Information without consequence also slows the book's engine, because the questions it answers are replaced by nothing.",
            "reason_past": "Reason past it by attaching every reveal to a consequence chain: decide within which scene the new knowledge alters a decision, a relationship, or a plan, and hold the disclosure until that scene can begin, so the reveal and its effect arrive as one motion.",
            "closers": [
                "Commit to consequential disclosure: the reveal ahead arrives coupled to the decision it forces, within touching distance. Write them as one motion, and let the story's course visibly bend at the moment of knowing.",
                "Refuse the informational reveal. Fix what changes on the ground when the fact lands, and stage the disclosure at the point of change. The reader will feel the story accelerate rather than pause.",
            ],
        },
        {
            "id": "confusion_mistaken_for_mystery",
            "frames": [
                "Your story's early stretch has left the reader uncertain about basic orientation, and you have been counting that uncertainty as intrigue.",
                "You are writing a narrative that withholds so much that the reader cannot form questions, only complaints.",
                "Your draft's mystery depends on the reader not understanding things they would need to understand to care.",
            ],
            "slide": "You feel the pull toward withholding as a blanket: keeping the reader in the dark about orientation, stakes, and rules, and calling the resulting fog mystery. The pull comes from wanting the reveals to dominate.",
            "stages": ["the opening chapters", "the first act", "the early middle of the book"],
            "openers": [
                "The draft is dark, and the darkness is being asked to do two jobs at once: conceal the genuine mystery and orient the reader. It can only do one. Decide which facts are furniture, the rules, relationships, and stakes the reader must hold to care, and release those early and plainly, reserving darkness for the questions the story actually wants open.",
                "You can feel the appeal of total withholding: every later reveal lands harder if nothing was given early. The appeal is arithmetic and it is wrong, because mystery requires a platform: the reader must know enough to wonder. Before drafting on, fix the platform and build it in plain sight.",
            ],
            "damage": "The damage is the death of the questions the mystery depends on: confusion does not generate curiosity, it generates fatigue, and a reader who cannot tell what matters stops distinguishing between the significant unknown and the missing basics. When the real revelation arrives, it lands on a reader who has already stopped asking.",
            "reason_past": "Reason past it by separating the accounts: list what the reader must know to form the story's central questions, and deliver that list early, clearly, and without shame, then spend all your concealment budget on the questions themselves.",
            "closers": [
                "Commit to the separation: orientation delivered plainly and early, darkness reserved for the live questions. Write the next scene as platform-building, and let the mystery begin where understanding starts.",
                "Refuse the fog. Fix the minimum orientation the reader needs, place it in the next stretch of scenes without disguise, and save your withholding for the questions that will repay it. Write the platform first.",
            ],
        },
        {
            "id": "collapsed_asymmetry",
            "frames": [
                "Your story's central mystery is becoming easy for the reader to solve well before the solution is revealed.",
                "You are writing toward a twist, and the evidence trail has grown so consistent that the asymmetry between reader and character is evaporating.",
                "Your narrative's concealed answer has become the book's open secret, sustained only by the character's failure to notice.",
            ],
            "slide": "Planning forward, you notice the reader can almost certainly see the answer already, and the remaining chapters would be a long pretense of concealment. The pull is to carry on regardless, trusting momentum to paper over the collapsed gap.",
            "stages": ["the middle of the book", "the second act", "the approach to the reveal"],
            "openers": [
                "The gap has closed: the reader holds the answer, and the character's remaining ignorance is becoming a strain on both. Refuse the pretense. Either reintroduce genuine uncertainty with a credible complication, or convert the story's mode from mystery to suspense, where the reader's knowledge becomes the engine and the question becomes how and when, not who.",
                "You can see that the asymmetry has collapsed, and the plan as written asks the reader to keep a secret they have already solved. The salvage is not louder misdirection but a change of use: let the reader's knowledge generate dread for the character, and re-aim the story's question at the collision the knowledge makes inevitable.",
            ],
            "damage": "The damage is a long insult stretched across chapters: readers who have solved the puzzle are asked to watch characters fail to solve it, and the story's intelligence is discounted by both parties. The eventual confirmation lands as a formality, and the chapters spent in pretense are remembered as the book's slowest.",
            "reason_past": "Reason past it while writing by auditing the trail as a reader would: after each scene that touches the concealed answer, estimate the reader's confidence. Above the threshold, stop adding confirming evidence and start spending the knowledge, converting it into suspense before the gap closes entirely.",
            "closers": [
                "Commit to the audit and the conversion: confidence will be tracked scene by scene, and once the reader holds the answer, the story switches its question to what the knowledge will cost. Write the next scene as the beginning of that conversion, not as continued pretense.",
                "Refuse the pretense. Decide now whether a credible complication reopens the question or the story changes modes to suspense, and restructure the coming chapters accordingly. Either path respects the reader; the pretense respects neither of you.",
            ],
        },
    ],
    "discipline": [
        "Keep the three-position map current as you draft: what the reader knows, what the point-of-view character knows, and what the other characters know. Before each scene, decide which position moves, in which direction, and why the story is better for the movement.",
        "Maintain the question ledger while generating: what is the reader wondering, at what intensity, and which entry this scene collects on. A scene that neither pays nor opens a question is spending attention it has not earned.",
        "Audit every silence for motive before writing it: what speaking would cost the character, and whether the scene shows the price. Unpriced silence is the fastest route to the reader's distrust.",
        "While planning reveals, rank them by recontextualizing power rather than by surprise size: how much prior material does each one recolor. Sequence the staircase so each disclosure reaches further than the last, and place the deepest one where it can still alter a decision.",
        "Check channel discipline at the end of each scene: every delivered fact should be traceable to witness, report, evidence, or honest inference. A violation that survives into the draft is a licence the reader will use against you.",
    ],
    "themes": [
        {
            "id": "knowledge_arc",
            "frames": [
                "Your novel's secrets, reveals, and discoveries have not yet been arranged into an overall schedule.",
                "You are planning a story whose information structure, who knows what and when, is as important as its event structure.",
                "Your materials involve layered concealment, and the full arc of knowledge across the book is still unmapped.",
            ],
            "question": "Plan the knowledge arc of the whole book: how the reader's and the characters' knowledge grow, gap, and converge from first page to last.",
            "openers": [
                "A novel has two plots: the plot of events and the plot of knowledge. Before drafting, map the second as deliberately as the first: what each major character knows at each stage, what the reader knows, and where the gaps sit. Every scene's tension can then be read off the map, and every reveal can be scheduled where the map says the pressure peaks.",
                "Plan the book's knowledge from the end state backward. At the final page, who must know what, and what must the reader have understood. Then design the sequence of movements by which the three positions, reader, protagonist, and world, arrive at that state, and place the story's reversals at the moments of largest relative motion.",
            ],
            "middles": [
                "Chart the reader's knowledge as a curve with deliberate plateaus and climbs. Long flats, where nothing significant is learned, starve curiosity; constant climbing exhausts it. Choose three or four major climbs, spaced across the book, each one a reorganization of what the reader understands, and let the flats between them be spent on deepening the value of what is already known.",
                "Design the convergence points: the moments where reader knowledge and character knowledge meet. A convergence is always an event, the character learns what the reader has known, or the reader finally learns what the character has been hiding, and each convergence resets the story's tension formula. Schedule them where the story can absorb a change of formula.",
                "Decide which knowledge is withheld from everyone, held only by the narrative itself. This is the most powerful and most dangerous position: it generates the fairest surprises and the worst cheats. For each narrative-held fact, require a fair trail, perceivable in hindsight, that a rereading reader can follow from the first page.",
                "Plan the knowledge gaps between characters as sources of conflict independent of their goals. Two people wanting the same thing but knowing different amounts will collide differently than their aligned aims suggest: the better-informed one's patience, the worse-informed one's confidence. Let the information differences, not just the desire differences, drive the cast's collisions.",
            ],
            "closers": [
                "Set the knowledge arc in place: the reader's curve, the convergence points, the narrative-held facts with their fair trails, and the character-to-character gaps. Draft from the map, and every scene's information decisions will have a reason the structure can name.",
                "Commit to the schedule: which knowledge moves when, where reader and character meet, and what the final state of knowing must be. Write forward with the map in hand, and let each scene move exactly one position, on purpose.",
            ],
        },
        {
            "id": "surprise_suspense_allocation",
            "frames": [
                "Your novel contains both sudden reversals and long-burning threats, and their proportions and placement are undecided.",
                "You are planning a book that will need both the shock of the unforeseen and the dread of the foreseen, in the right measure.",
                "Your materials support two modes of tension, surprise and suspense, and the allocation between them is a live structural question.",
            ],
            "question": "Decide the allocation between surprise and suspense across the book: which questions are withheld from the reader, and which are granted early to burn.",
            "openers": [
                "Surprise and suspense draw on the same resource, the reader's knowledge, in opposite ways: surprise withholds, suspense grants. Before drafting, allocate: which of the story's major questions will be answered early and allowed to generate dread, and which will be held to detonate. The allocation is the book's tension architecture.",
                "Plan the tension modes as a portfolio. A book of pure surprise resets to zero with each reveal; a book of pure suspense spends its dread in one long note. Decide the mix for each movement: where the reader should hold knowledge the characters lack, and where they should be one step behind, and where the two positions trade.",
            ],
            "middles": [
                "Grant suspense its fuel early and completely. The scenario that will burn for two hundred pages must be delivered to the reader in full: what is coming, roughly when, and what it will mean. Withheld suspense is not suspense but confusion, and the dread you want is only available to a reader who knows exactly enough to fear precisely.",
                "Spend surprise on recontextualization rather than on novelty. The withheld revelation should change the meaning of what the reader already holds, not simply add a new fact, because recontextualizing surprise compounds backward through the book, making the reader's memory itself a scene of the story.",
                "Interleave the modes at the sequence level. After a surprise, the reader must rebuild their model, which is a moment of heightened attention; a stretch of suspense immediately after, with the new knowledge granted, converts that attention into dread. Plan the alternation deliberately: shock, then the long burn the shock enables.",
                "Protect the endings of both modes. Suspense must resolve through the character's agency in some form, a choice, a stand, a refusal, or the dread was idle; surprise must be reconstructable, the trail visible in memory, or the shock was noise. Decide each mode's terminal conditions now, and hold both to them.",
            ],
            "closers": [
                "Fix the portfolio: which questions are granted early to burn, which are held to detonate, and how the modes alternate across the book's movements. Draft with the allocation in hand, and the tension will have architecture rather than weather.",
                "Commit to the allocation and both terminal conditions: suspense resolved through agency, surprise reconstructable in memory. Write toward the first long burn now, with its fuel scheduled for early and complete delivery.",
            ],
        },
    ],
    "principles": [
        "Information is the substance of story: events are only the occasions on which knowledge changes hands. Plan who knows what at every stage, and the drama can be read directly off the map.",
        "The reader's curiosity is a budget you spend: every withheld fact must be worth its carrying cost, every answered question must purchase more attention than it closes. Manage the ledger ruthlessly.",
        "The strongest disclosure changes the past rather than adding to it. Rank revelations by how much prior material they recolor, and stage them where the recoloring can still alter a decision.",
        "Withholding is a promise: the reader accepts darkness on the guarantee that the darkness is structured, motivated, and payable. Every unmotivated silence spends the guarantee, and the guarantee is not renewable.",
    ],
}
