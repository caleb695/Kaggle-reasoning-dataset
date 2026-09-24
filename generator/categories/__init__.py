"""Category registry. Each module exposes a CAT dict with this schema:

CAT = {
    "id": ..., "label": ...,
    "moves": {move_key: [paragraph, ...], ...},      # ordered reasoning facets
    "problems": [{id, frames, context, stages, openers, closers}, ...],
    "traps": [{id, frames, slide, stages, openers, damage, reason_past, closers}, ...],
    "discipline": [paragraph, ...],                  # shared forward checks (negatives)
    "themes": [{id, frames, question, openers, middles, closers}, ...],
    "principles": [paragraph, ...],                  # shared principles (reasoning)
}
"""

from . import plot_architecture
from . import conflict_escalation
from . import character_decisions
from . import information_management
from . import scene_construction
from . import chapter_arcs
from . import setup_payoff
from . import tension
from . import momentum
from . import epic_scale
from . import pov_perception
from . import concrete_grounding
from . import prose_discipline
from . import metaphor_imagery
from . import emotion_craft
from . import dialogue_voice
from . import action_physicality
from . import continuity_outline
from . import idea_generation
from . import outline_design
from . import revision_craft
from . import idea_shaping
from . import arc_mapping
from . import scene_planning
from . import revision_diagnosis
from . import genre_epic_fantasy
from . import genre_scifi
from . import genre_thriller

CATEGORIES = [
    plot_architecture.CAT,
    conflict_escalation.CAT,
    character_decisions.CAT,
    information_management.CAT,
    scene_construction.CAT,
    chapter_arcs.CAT,
    setup_payoff.CAT,
    tension.CAT,
    momentum.CAT,
    epic_scale.CAT,
    pov_perception.CAT,
    concrete_grounding.CAT,
    prose_discipline.CAT,
    metaphor_imagery.CAT,
    emotion_craft.CAT,
    dialogue_voice.CAT,
    action_physicality.CAT,
    continuity_outline.CAT,
    idea_generation.CAT,
    outline_design.CAT,
    revision_craft.CAT,
    idea_shaping.CAT,
    arc_mapping.CAT,
    scene_planning.CAT,
    revision_diagnosis.CAT,
    genre_epic_fantasy.CAT,
    genre_scifi.CAT,
    genre_thriller.CAT,
]
