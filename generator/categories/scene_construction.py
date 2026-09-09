"""Scene-level pacing and multi-purpose construction."""

CAT = {
    "id": "scene_construction",
    "label": "Scene-level pacing and multi-purpose construction",
    "moves": {
        "scene_engine": [
            "Give every scene a three-part engine: someone wants something concrete within the scene's span, something stands in the way, and the encounter ends with the situation shifted in value, better or worse, safer or more exposed, for at least one person on the page. A scene whose engine cannot be stated in those terms is a passage, not a scene, whatever its content.",
            "Make the scene's outcome different from its expectation. If the scene resolves the way its opening promised, the reader has watched a confirmation; if it resolves otherwise, through reversal, cost, partial gain, or the discovery that the real obstacle was elsewhere, the reader has watched a story. Plan the departure from expectation deliberately.",
            "Keep the scene's want nested inside the story's want. The character's goal in the room should be a strategy step for their larger objective, so that winning or losing the scene moves the book's plot, not just the scene's mood. When the nesting breaks, the scene may entertain but it will not accumulate.",
            "End the scene on the turn, not on the settling. The moment of shift, the decision made, the refusal delivered, the fact understood, is the scene's payload; what follows the turn is cooldown that belongs in the next scene or nowhere. Locate the turn first, then build the scene toward it.",
        ],
        "duty_loading": [
            "Load each scene with multiple duties: advancing the plot, revealing character, deepening relationship, planting information, or thickening the world. The load is not additive work but a single event designed so that its several effects are inseparable: the confrontation that also plants the clue that also shifts the friendship. Assign the duties before writing, then design one event that carries all of them.",
            "Prefer scenes where the duties conflict slightly. A scene whose plot duty and character duty pull in different directions, the useful victory that costs a relationship, the kind gesture that endangers the plan, generates its own tension from the loading itself. Pure alignment of duties produces efficiency without friction.",
            "Know each scene's primary duty and protect it. When a scene carries four obligations, the temptation under pressure is to serve the loudest and drop the rest, which is how planted material gets orphaned. Rank the duties, and if the scene cannot honestly carry them all, move the lowest-ranked one to a scene that can.",
            "Use secondary characters as carriers of load. A scene gains duties when its other participants bring their own objectives into the room: the ally who needs a favor at the worst time converts an expository scene into a negotiation. Design the ensemble of each scene so the load is distributed across real wants.",
        ],
        "beat_order": [
            "Order the scene's beats so pressure rises and each beat alters the terms of the next. A beat is one move in the scene's contest, an approach, a deflection, an escalation, a concession, and the sequence should close options as it goes, so the final beat lands on a narrower field than the first. If the scene's middle beats could be shuffled without damage, the order is not yet designed.",
            "Put reactions before deliberations and deliberations before decisions. When something happens to a character, the immediate response is reflex and feeling, the considered response comes after, and the decision comes last, under whatever time remains. Compressing or reordering that chain is how scenes come to feel false without any single wrong line.",
            "Vary the beat types to control pace. Escalation beats, retreat beats, revelation beats, and silence beats do different work at different speeds, and a scene built from escalation alone numbs the reader by its third turn. Plan the alternation so intensity has somewhere to breathe inside the scene itself.",
            "Give the scene's opening beat a job beyond entry. The first exchange should either advance a live question from the previous scene or establish the scene's own pressure, ideally both, so the reader is inside motion from the first line. An opening beat spent on orientation is a tax collected at the moment of highest attention.",
        ],
        "entry_exit": [
            "Enter the scene as late as comprehension allows. Everything before the first pressure, the arrival, the greeting, the settling in, is runway, and the reader's attention is highest exactly where the runway is longest. Cut to the first moment something is at stake in the room, and let the necessary orientation arrive in fragments under way.",
            "Leave at the turn or its first consequence, not at the explanation. The scene's exit is the reader's last impression and the next scene's springboard; ending on the unresolved shift, the choice just made, the information just landing, converts the scene break into a question. Ending on resolution converts it into a rest stop.",
            "Design the exits and entries as a connected system across consecutive scenes: what scene one ends on should be what scene two cannot ignore. The strongest continuity is obligation, a door opened that must be walked through, a question posed that must be answered, a cost just landed that must be dealt with. Exit on the obligation, enter inside the response.",
            "Cut the approach and the departure even when they contain good material. The conversation on the stairs, the drive home after, belongs to the scenes it connects only as the shortest possible trace. When good material lives in a scene's margins, give it its own scene or fold its duty into an adjacent one; the margin is where pacing dies.",
        ],
        "time_density": [
            "Control the scene's clock explicitly. Real-time treatment stretches an event to full duration and gives it weight; summary compresses hours into a sentence and signals subordination. Decide the density of each scene against its importance: the decisive confrontations in real time, the connective tissue compressed, and the transitions between densities made deliberate rather than accidental.",
            "Stretch the moments that carry the scene's turn. A decision, a revelation, or a reversal deserves granular treatment, perception, hesitation, the physical world in detail, because slowness is how the narrative marks significance. Save the stretch for the few moments that have earned it, or the mark loses value.",
            "Compress without losing causality. When summarizing, keep the chain of consequence intact: the summary must still show what led to what, or the compressed period will read as a gap when the story later depends on it. A summary sentence that preserves one causal link is worth three that preserve atmosphere.",
            "Use white space and scene breaks as pacing instruments. A break before the scene's turn creates a held breath across the gap; a break after the turn lets the consequence land offstage and be discovered later. Choose the break positions as deliberately as the beats, because the reader experiences the rhythm of the book through them.",
        ],
    },
    "problems": [
        {
            "id": "information_only_scene",
            "frames": [
                "Your next scene exists mainly to deliver information the reader needs, and you can feel how flat that purpose makes it.",
                "You are planning a scene whose only duty is exposition, and the scene keeps wanting to become a report.",
                "Your outline contains a scene that must convey a complicated situation, and no conflict has yet been attached to it.",
            ],
            "context": "The exposition must be smuggled inside conflict: the information arrives as it is needed by characters with live objectives, so the reader absorbs it under pressure rather than receiving it as a report.",
            "stages": ["the first act", "the early middle of the book", "the middle of the book"],
            "openers": [
                "The scene's information has no engine yet, and information without an engine is a document. Give the facts a seeker: someone in the scene needs some of them urgently, someone else benefits from withholding or distorting others, and the reader's understanding arrives as the residue of a contest rather than as delivery.",
                "Before writing the exposition scene, break the information into pieces by urgency: what is needed now, what would help, what can wait. Then attach each piece to a want in the scene, so the facts emerge as answers to questions the scene has made live. Nothing kills a needed fact faster than delivering it before anyone on the page wants it.",
                "The scene as planned is a lecture wearing a location. Rework it around a disagreement: the information changes meaning depending on who is right, the two parties read the same facts differently, and the reader must adjudicate. Exposition delivered inside a live dispute is remembered; exposition delivered in agreement is skimmed.",
            ],
            "closers": [
                "Commit to the contest: the facts enter the story as they are fought over, withheld, and paid for, and the reader's picture assembles from the sparks. Write the scene as a negotiation in which the information is the currency.",
                "Fix the pieces by urgency, attach each to a live want, and write the scene where the most urgent piece is worth arguing about. The information will arrive because someone on the page cannot proceed without it.",
            ],
        },
        {
            "id": "confrontation_scene",
            "frames": [
                "Your novel is moving toward a direct confrontation between two characters whose conflict has so far been indirect.",
                "You are writing the scene where two opposing forces finally occupy the same room.",
                "Your story's central tension is about to become face-to-face, and the scene must carry the accumulated weight.",
            ],
            "context": "The confrontation must be built as a contest with moves, counters, and a value shift, so that the meeting changes the relationship's position rather than merely displaying it.",
            "stages": ["the end of the first act", "the middle of the book", "the approach to the climax"],
            "openers": [
                "A confrontation is a game with positions, not a statement of positions. Decide what each party wants from the meeting, what they are willing to show, what they must hide, and which leverage each holds. Then design the exchange as moves against those hidden stakes, so the scene's outcome repositions the relationship.",
                "Before drafting, fix the scene's turn: what is different between these two after the encounter that was not different before. A confession extracted, a threat made credible, an alliance revealed as betrayal, the turn is the scene's reason for existing, and every beat before it is built to make the turn cost something.",
                "Decide the balance of power at entry and how the scene destabilizes it. If the confrontation ends with the same party dominant, it has only dramatized a known fact; let the underdog score, the dominant party overreach, or a third weight enter, so the reader leaves the scene with a changed map of who can hurt whom.",
            ],
            "closers": [
                "Commit to the turn and the repositioning: the encounter changes what these two can do to each other, and the final beat lands on the new terms. Write the contest move by move, hiding each side's real stake until the pressure extracts it.",
                "Fix the entry positions and the destabilizing move, then write toward the moment the map changes. The scene's value will be measured in what each party now knows about the other, and in what the reader has learned that neither would say.",
            ],
        },
        {
            "id": "ensemble_scene",
            "frames": [
                "Your next scene gathers several characters with different agendas in one place, and the management of the crowd is the problem.",
                "You are writing a dinner, a meeting, a wake, or a negotiation where the whole cast's tensions must share one frame.",
                "Your story requires a group scene in which multiple relationships must shift within a single occasion.",
            ],
            "context": "The ensemble scene must be orchestrated: one controlling event, assigned positions for each participant, and a clear track of which relationships change and in what order.",
            "stages": ["the first act", "the middle of the book", "the second act"],
            "openers": [
                "An ensemble scene needs a conductor's score. Decide the controlling event, the announcement, the arrival, the revelation that puts everyone in the same pressure, then assign each character a position toward it: who wants it, who dreads it, who can use it. The scene's beats are then collisions between positions, and no one is present merely as furniture.",
                "Before drafting, map the side conversations: what each pair at this gathering needs from each other, and which of those needs will be advanced tonight. A group scene is several scenes in one frame, and the craft is in the cutting between them, so each two-person thread gets exactly the beats it needs and no more.",
                "Decide the scene's public event and its private event. The group gathers for one reason, visible to all, while the scene's real business happens in the seams: a word in the doorway, a face across the table, an absence noticed. Design both layers, and let the public event's schedule govern when the private ones can breathe.",
            ],
            "closers": [
                "Commit to the score: controlling event, assigned positions, and the order in which the pairings get their beats. Write the scene as orchestration, and let the crowd's density become the source of pressure rather than a problem to be reduced.",
                "Fix the public event and the private business, then write the seams. Each character leaves the scene having moved at most one relationship, and the reader leaves having seen everyone's position more clearly than any of them would admit.",
            ],
        },
        {
            "id": "aftermath_scene",
            "frames": [
                "Your story has just delivered a major event, and the scene that follows must metabolize it without going slack.",
                "You are writing the aftermath of a death, a betrayal, a disaster, or a victory, and the pull toward quiet threatens the momentum.",
                "Your narrative needs a scene of processing and response after a shock, and the scene must do real work.",
            ],
            "context": "The aftermath scene must convert the event into consequence: decisions revised, positions recalculated, and the shock's meaning distributed across the cast, all while the next pressure assembles.",
            "stages": ["the stretch after a major turn", "the middle of the book", "the passage into a new act"],
            "openers": [
                "An aftermath is not a pause but a redistribution: the event's energy disperses into new positions, new fears, new plans. Decide who recalculates what, whose position improves in ways they have not yet noticed, whose worsens visibly, and let the scene's quiet be the sound of those recalculations rather than an absence of motion.",
                "Before writing the quiet scene, decide what decision it contains. Aftermath earns its space when a character, changed by what happened, makes or refuses a choice the old self could not have faced; the grief and shock are the pressure under that decision, not a substitute for it.",
                "Plan the aftermath as the hinge between two pressures: the event's residue still radiating, the next threat already assembling. The scene should hold both in frame, the characters tending wounds while the first sign of the new problem shows at the edge, so the quiet carries forward motion inside it.",
            ],
            "closers": [
                "Commit to the redistribution: recalculations, the decision under grief, and the first edge of the next pressure. Write the aftermath as work being done quietly, and let the scene end before the quiet does.",
                "Fix the scene's decision and the new pressure's first appearance, then write the in-between. The aftermath will hold the event's weight precisely because it is already moving toward what comes next.",
            ],
        },
        {
            "id": "overloaded_scene",
            "frames": [
                "Your planned scene has accumulated more duties than any single occasion can carry, and the strain is visible in the outline.",
                "You are designing a scene that must advance the plot, resolve a relationship question, and deliver a major revelation at once.",
                "Your story's next scene keeps growing as more obligations get attached to it during planning.",
            ],
            "context": "The overloaded scene must be triaged: rank the duties, keep the combination that strengthens each other, and redistribute the rest to scenes that can carry them honestly.",
            "stages": ["the planning stage", "the middle of the book", "the second act"],
            "openers": [
                "The scene is overweight, and the failure mode is predictable: all duties served thinly instead of two served deeply. Triage now. Rank the obligations, test which pairings strengthen each other, the revelation that also breaks the relationship, and move the rest. A scene can be dense or it can be crowded; density is several duties in one event, crowding is several events in one room.",
                "Before writing, decide what this scene is really about, in one sentence that does not list. Whatever the sentence names is the primary duty; everything else is either integrated into it or scheduled elsewhere. The discipline feels like loss and is the difference between a scene that lands and one that blurs.",
                "Check whether the load is one event or a chain pretending to be a scene. Three obligations that arrive in sequence, one after another, are a movement of story, not a scene, and they will fight the scene's clock. Either find the single event that genuinely carries them together or split the chain into its own sequence of scenes.",
            ],
            "closers": [
                "Commit to the triage: the duties that stay are fused into one event, the rest are reassigned with destinations. Write the slimmed scene to full depth, and give each exiled duty the scene that will actually carry it.",
                "Fix the single sentence of purpose, keep only the obligations that serve it, and write toward the scene's turn. The cut material is not lost; it is waiting for the scenes that can honor it.",
            ],
        },
    ],
    "traps": [
        {
            "id": "static_conversation",
            "frames": [
                "Your planned scene is two characters talking in a room, and the talk, however good, changes nothing between them.",
                "You are writing an exchange whose information is necessary but whose outcome is foreordained.",
                "Your draft keeps producing dialogue scenes that end where they began, with everyone's position intact.",
            ],
            "slide": "You notice the scene ahead is shaped as pure conversation: two people exchange views, the views are interesting, and neither leaves the room different. The pull is toward the well-written talk, because talk is the easiest material to make sparkle while it does nothing.",
            "stages": ["the first act", "the early middle of the book", "the middle of the book"],
            "openers": [
                "The conversation in your plan is static: the words will be good and the distance between the two people at the end will be exactly what it was at the start. Give the talk stakes before drafting: a decision pending, a truth at risk, a proposal that cannot be taken back. Let the dialogue be the contest rather than the commentary.",
                "You can feel the scene resolving into two voices and a sofa. The fix is not more vivid speech but a shift: the exchange must end with someone's position moved, someone's knowledge changed, or someone's mask cracked. Decide the shift now, and build the conversation as the pressure that produces it.",
            ],
            "damage": "The damage is the scene's invisible cost: static scenes consume the reader's page trust, and the habit teaches them that talk in this book is decoration, so when a conversation carries genuine weight, the reader has stopped weighing it. Dialogue's power is entirely borrowed from its consequences.",
            "reason_past": "Reason past it while writing by giving every conversation a contested object: something on the table that one party wants and the other resists, so each line is a move, and the scene's end state differs from its start in knowledge, position, or intention.",
            "closers": [
                "Commit to the contested object: the talk ahead is a negotiation with a live outcome, and each exchange is a move toward or away from it. Write the scene so the room is different at the end, and let the words earn their place by what they change.",
                "Refuse the decorative conversation. Fix the shift the scene must deliver, choose the pressure that forces it, and write the dialogue as the contest's record. If no shift can be found, the scene's duty belongs somewhere else.",
            ],
        },
        {
            "id": "connective_filler",
            "frames": [
                "Your outline has gaps between major scenes, and you are tempted to fill them with travel, meals, and transitions.",
                "You are writing the connective tissue between two events the story cares about, and the tissue is consuming pages.",
                "Your draft's scene list includes several scenes whose purpose is only to get characters from one place to another.",
            ],
            "slide": "You feel the pull toward connective filler: a scene of travel, preparation, or small domestic business to bridge the gap between the load-bearing scenes. The pull comes from the fear of abruptness, the wish that the story should breathe between efforts.",
            "stages": ["the first act", "the middle of the book", "the second act"],
            "openers": [
                "The bridge scene is forming, and its only function will be to slow the story down politely. Refuse the function and keep the bridge if the connection needs one: a paragraph of compression that preserves the causal link, or better, cut the gap entirely by ending the first scene later or starting the second sooner.",
                "You are about to write a scene whose best defense is that it comes between two good scenes. The defense fails the moment the reader notices. Before writing it, either find a duty it can genuinely carry, a plant, a shift, a decision, or compress its whole existence into the seam between its neighbors.",
            ],
            "damage": "The damage is cumulative dilution: each filler scene trains the reader that some pages can be skimmed, and the skill they acquire skimming your transitions is waiting to be applied to your climaxes. Pacing is a promise that every page is on the story's side.",
            "reason_past": "Reason past it while writing by testing every connective candidate for a duty: if a plant, a shift, or a decision can live inside it, write it as a real scene; if not, compress the connection to its causal minimum and spend the recovered pages where pressure lives.",
            "closers": [
                "Commit to the duty test: the connection ahead either earns a scene or becomes a seam. Make the decision now, and either write the bridge as real work or collapse it into a sentence that carries the cause.",
                "Refuse the filler before it is written. End the previous scene closer to the event, open the next inside its consequence, and let the gap close around them. The story's rhythm will tighten, and the reader's trust in every page will grow.",
            ],
        },
        {
            "id": "repeated_information",
            "frames": [
                "Your scenes keep re-explaining things the reader already knows, out of a generous instinct to keep everyone oriented.",
                "You are writing a scene whose participants would naturally discuss matters the reader has already witnessed firsthand.",
                "Your draft's characters keep summarizing recent events to each other for the reader's benefit.",
            ],
            "slide": "You feel the pull toward the recap: having characters tell each other what the reader watched happen, as a courtesy to memory and a hedge against confusion. The pull is kindness, and the cost is the reader's sense of their own standing in the story.",
            "stages": ["the middle of the book", "the second act", "the long middle of the book"],
            "openers": [
                "The recap temptation is in front of you: the characters will politely restate what the reader saw an hour ago. Refuse it. The reader's memory is better than the characters' manners, and every repetition signals that the story does not trust its own audience. If the information must surface, let it surface changed: argued over, misread, or put to a use the first scene never implied.",
                "You are about to write a scene whose information content is already in the reader's possession. The scene can still earn its place, but not by repetition: find the new angle, the disagreement about what the known event means, the consequence that lands here. Write the delta, not the summary.",
            ],
            "damage": "The damage is a reader's quiet demotion to a visitor: repeated information tells them the story expects them to be forgetful, and the expectation is self-fulfilling, since a reader who is being managed stops attending closely. The book also slows measurably, because recaps occupy the exact pages where new pressure should be landing.",
            "reason_past": "Reason past it while writing by assuming the reader holds everything the narrative has shown: before any scene, list what is genuinely new to the reader, and build the scene from that list, letting known material appear only as the object of dispute, development, or use.",
            "closers": [
                "Commit to the delta: the scene ahead contains only what the reader does not yet hold, and known events enter solely as material the characters contest or deploy. Write from the new list, and the story will accelerate where it used to summarize.",
                "Refuse the courtesy recap. Trust the reader's retention, and spend the scene's length on consequence instead: what the known event has changed, cost, or made possible. Write the first consequence now.",
            ],
        },
        {
            "id": "single_duty_bloat",
            "frames": [
                "Your scene list is growing long, and several scenes each carry only one small duty.",
                "You are planning a stretch where every plot movement gets its own dedicated scene, and the count is inflating.",
                "Your draft's middle section contains a crowd of single-purpose scenes, each necessary but each thin.",
            ],
            "slide": "You notice the stretch ahead is built from single-duty scenes: one plant here, one small shift there, each scene doing exactly one thing. The pull is toward this spreading, because one duty per scene is easier to design than a scene that fuses several.",
            "stages": ["the planning stage", "the middle of the book", "the second act"],
            "openers": [
                "The single-duty scenes are multiplying, and the stretch they form will read as a corridor of small rooms. Consolidate by fusion: find the duties that can share an event, the plant that can happen during the confrontation, the shift that can occur inside the decision, and rebuild the corridor into a few dense rooms.",
                "You can feel the comfort of one-duty scenes, and you can also see their cost: page count rising, each scene thin, the middle stretching. The stronger design fuses duties into shared events, so the plant happens under pressure, the reveal costs a relationship, and the scene count falls while the density rises.",
            ],
            "damage": "The damage is structural sprawl: single-duty scenes are individually easy and collectively fatal, because their sum is a book that moves at the speed of its slowest necessity. Each thin scene also dilutes its neighbors, since a reader trained by thin scenes discounts the weight of everything around them.",
            "reason_past": "Reason past it while planning by running a fusion pass over the scene list: for each single-duty scene, find a neighboring scene whose event could carry the same duty without strain, and merge. Repeat until every scene on the list carries at least two duties honestly.",
            "closers": [
                "Commit to the fusion pass: the duties ahead will share events, the scene count will fall, and the survivors will be denser. Rework the stretch now, and write the first merged scene to prove the fusion holds.",
                "Refuse the corridor of small rooms. Assign every duty on your list to an event that carries at least two, and let the thin scenes dissolve into their neighbors. Write the first dense scene and feel the pace recover.",
            ],
        },
        {
            "id": "costless_conflict_scene",
            "frames": [
                "Your scenes keep generating arguments and clashes that produce heat without changing anyone's circumstances.",
                "You are writing conflict that stays verbal, recurring, and inconclusive, scene after scene.",
                "Your draft's characters fight often, and the fighting has become a substitute for story movement.",
            ],
            "slide": "You notice the planned scene's conflict is performative: the characters will clash, sparks will fly, and nothing will be different afterward. The pull is toward friction as flavor, because conflict is easy to write and its consequences are hard to arrange.",
            "stages": ["the early middle of the book", "the middle of the book", "the second act"],
            "openers": [
                "The conflict on your page is becoming a ritual: the same two people, the same friction, the same reset. Break the ritual by pricing the next clash: one of them will say the thing that cannot be unsaid, or take the action that forecloses an option. Decide which, before drafting, so the friction produces a permanent change.",
                "You can feel how easily this scene becomes another display of animosity with no ledger entry. Conflict earns its page time by spending something: a possibility, a pretense, an ally's patience. Set the spend for this scene now, and let the sparks be the instrument rather than the point.",
            ],
            "damage": "The damage is the devaluation of conflict itself: readers calibrate to the story's fights, and repeated friction without cost teaches them that clashes here are weather, not events. When a genuinely consequential conflict arrives, it enters a market where its currency has already been inflated away.",
            "reason_past": "Reason past it while writing by attaching a ledger entry to every clash: decide what the scene's conflict changes in options, knowledge, or standing, and if no honest entry exists, either find one or let the friction stay beneath the surface in this scene and save the eruption for one that pays.",
            "closers": [
                "Commit to the priced clash: the conflict ahead changes the ledger, the unsayable said or the option foreclosed, and the scene ends with the spend visible. Write toward the irrevocable moment inside it.",
                "Refuse the ritual. Give this scene's friction a consequence that survives it, or withhold the eruption for a scene that can afford one. Write the decision into the plan before the sparks fly.",
            ],
        },
    ],
    "discipline": [
        "Before drafting any scene, state its engine in one sentence: who wants what within the scene, what opposes them, and how the value of the situation shifts at the end. If the sentence cannot be completed, the scene is not ready to be written.",
        "Assign each scene its duty load in the planning stage, ranked: primary, secondary, planted. While drafting, check the load at the scene's midpoint, because the loudest duty will always try to devour the quiet ones.",
        "Choose entry and exit points last, after the beats are clear: enter at the first moment of stake in the room, leave at the turn or its first consequence. Never spend the scene's margins on approach and departure.",
        "Set the clock deliberately for each scene: real-time for the turn, summary for the connective, and a chosen density for everything between. The reader reads your time choices as judgments of importance, so make them on purpose.",
        "Run the fusion check over each stretch of scenes: any scene carrying a single duty is a candidate for merging. Density is several duties inside one event; the fusion pass is how a book's middle stays short and deep.",
    ],
    "themes": [
        {
            "id": "scene_as_change_unit",
            "frames": [
                "You are planning a novel at the level of its scenes, and the definition of what a scene is for is still open.",
                "Your story will be built from several dozen scenes, and you want a working theory of the unit before you compose them.",
                "You are deciding how much change each unit of your narrative must carry and how the units connect.",
            ],
            "question": "Establish the scene as your story's unit of change: what each scene must alter, and how the alterations chain into the book's motion.",
            "openers": [
                "A scene is a machine for changing one thing that cannot be unchanged: a fact learned, a position lost, a decision made, a bond broken. Hold your scenes to that standard from the start, and the book's motion is guaranteed by its construction; release the standard, and no amount of eventful incident will make the story move.",
                "Plan the book as a chain of irreversible deltas. Each scene delivers one or two changes to the story's state, and the next scene inherits the changed state as its ground. Before drafting, decide the size of the unit's delta: a scene that changes everything is a climax, a scene that changes nothing is a pause, and the book's pace is the distribution between them.",
            ],
            "middles": [
                "Define the change types your scenes will draw on, and keep the list short: knowledge, position, relationship, intention, capability. Every scene shifts at least one, and the type should vary across consecutive scenes, because three knowledge scenes in a row thin the story even when each is individually strong. Plan the type sequence for each stretch as deliberately as the events.",
                "Make the changes legible at their scene's end without narration summarizing them. The reader should feel the delta in the situation's altered pressure: the door that closed, the name that can no longer be spoken, the plan that now requires a different skill. If a scene's change needs a sentence of explanation to register, the change was staged too abstractly.",
                "Connect the deltas causally, not just sequentially. The change one scene delivers should be the ground the next scene stands on: the knowledge gained is used, the position lost is mourned and compensated, the decision made is implemented. A chain of unrelated deltas is a string of incidents; a causal chain is a plot.",
                "Budget the irreversible against the reversible. Most scene-level changes can theoretically be undone, and a story that undoes them freely teaches the reader that nothing is at stake. Decide which changes across the book are permanent, mark them as the story's real spine, and treat every other change as negotiation around those fixed points.",
            ],
            "closers": [
                "Adopt the unit standard: every scene alters at least one of the five state types, irreversibly where it matters, and inherits the altered state from its predecessor. Draft from the standard, and the book will move by construction.",
                "Fix the delta budget: which changes are permanent, how the types rotate, and how each delta seeds the next. Write the scenes as links in that chain, and the story's motion will be structural rather than habitual.",
            ],
        },
        {
            "id": "multi_duty_design",
            "frames": [
                "You want your novel's scenes to carry more than one kind of weight, and the method of fusing duties is undecided.",
                "Your story's page budget is finite, and the scenes must each do the work of more than their obvious purpose.",
                "You are planning a dense book, and the design of multi-purpose scenes is the central craft question.",
            ],
            "question": "Establish the method for designing multi-duty scenes: how plot, character, world, and information work are fused into single events.",
            "openers": [
                "The multi-duty scene is not a scene doing several things in sequence but one event whose consequences radiate through several registers at once: the confrontation that advances the plot, exposes the character, and plants the information in the same motion. The design method is to find the event where the duties naturally intersect, rather than bolting duties onto an occasion.",
                "Plan each scene's duties before its events, then invert: search for the single event that would produce all the assigned effects as consequences of one another. The search usually fails twice before it succeeds, and the failures, a scene doing plot and character side by side, are where the extra work gets spent. Hold out for the intersection.",
            ],
            "middles": [
                "Rank the duties by what happens if each is dropped. The duty whose loss damages the book's spine is primary; the rest are payload, and payload duties must attach to the primary's event so tightly that cutting them would damage the primary's staging. This ranking is what keeps multi-duty scenes coherent under the pressure of drafting.",
                "Use the conflict between duties as the scene's engine. When the plot duty and the relationship duty demand different outcomes from the same event, the scene generates its own drama: the character cannot serve both, and the choice between them is the scene's turn. Design duty conflicts into at least the major scenes, and the loading will never feel mechanical.",
                "Distribute the load across the cast. A scene carries more duties legitimately when its several participants bring their own agendas into the event: the visitor who needs a favor advances the plot by asking, exposes character by how they ask, and plants the information by what they noticed on the way. Orchestrate the participants as carriers, and the scene's density will be social rather than authorial.",
                "Verify the fusion at the sentence level while drafting. Multi-duty scenes fail when the duties take turns: a paragraph of plot, a paragraph of character. The test is whether the scene's key beats carry two registers simultaneously, the line that is both a threat and a confession, the object that is both a clue and a wound. Revise any beat that serves only one master.",
            ],
            "closers": [
                "Adopt the method: duties ranked, event searched for at the intersection, conflict between duties as engine, load distributed through the cast. Design the next scene by this method from the duties backward, and expect the search to be the real work.",
                "Commit to fused construction: no duty delivered in isolation, no beat serving one register. Plan the coming scenes as intersections, and let the book's density be structural rather than accreted.",
            ],
        },
    ],
    "principles": [
        "A scene exists to change something that cannot be unchanged. Every other virtue, atmosphere, wit, beauty, is welcome, but the change is the reason the scene occupies the reader's time.",
        "Scene density is the ratio of consequence to page count. The dense scene fuses duties into single events; the thin scene performs one obligation and leaves the rest of its length unspent.",
        "Enter late, leave early, and let the margins go. The scene's power concentrates at its point of attack and its turn, and everything else is either instrument or overhead.",
        "The reader experiences structure as rhythm: real-time against summary, beat against break, density against breath. Make the rhythm deliberate at every scale, and the book will feel designed without ever seeming managed.",
    ],
}
