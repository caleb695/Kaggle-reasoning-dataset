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
]
