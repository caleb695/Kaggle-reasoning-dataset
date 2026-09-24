"""Lens registry.

`LENSES` maps a lens name to its pool of cross-cutting craft paragraphs. Every
record draws one or two lenses determined by (a) the category of the record and
(b) the craft pressure carried by the chapter the record is about, so that
craft reasoning about plot is exercised on chapters that also have POV, pacing,
continuity, and prose obligations, and the same rule set is reached from many
directions.

`LENS_ORDER` fixes the paragraph order inside a response (POV obligations
before surface obligations) so responses read as reasoning moving from what the
scene is to how it is rendered.
"""

from generator.lenses_a import LENSES_A
from generator.lenses_b import LENSES_B

LENSES = {}
LENSES.update(LENSES_A)
LENSES.update(LENSES_B)

LENS_ORDER = (
    "pov",
    "concrete",
    "character",
    "scene",
    "pacing",
    "emotion",
    "dialogue",
    "humor",
    "action",
    "worldbuilding",
    "continuity",
    "outline_obedience",
    "reader_trust",
    "metaphor",
    "prose",
    "ai_patterns",
    "style_consistency",
)

# Which lenses a category's records may draw, most characteristic first. The
# build takes the first available lens that the chapter's craft pressure does
# not already supply, so no record repeats a lens.
CATEGORY_LENSES = {
    "plot_architecture": ("outline_obedience", "scene", "pacing", "character", "continuity"),
    "conflict_escalation": ("pacing", "character", "scene", "emotion", "outline_obedience"),
    "character_decisions": ("character", "continuity", "emotion", "dialogue", "scene"),
    "information_management": ("reader_trust", "pov", "continuity", "dialogue", "scene"),
    "scene_construction": ("scene", "concrete", "pacing", "pov", "reader_trust"),
    "chapter_arcs": ("pacing", "scene", "continuity", "style_consistency", "reader_trust"),
    "setup_payoff": ("outline_obedience", "continuity", "reader_trust", "pacing", "scene"),
    "tension": ("pacing", "scene", "emotion", "concrete", "reader_trust"),
    "momentum": ("pacing", "scene", "character", "continuity", "outline_obedience"),
    "epic_scale": ("worldbuilding", "outline_obedience", "continuity", "pacing", "character"),
    "pov_perception": ("pov", "concrete", "character", "reader_trust", "emotion"),
    "concrete_grounding": ("concrete", "pov", "emotion", "scene", "prose"),
    "prose_discipline": ("prose", "ai_patterns", "style_consistency", "metaphor", "reader_trust"),
    "metaphor_imagery": ("metaphor", "prose", "pov", "reader_trust", "ai_patterns"),
    "emotion_craft": ("emotion", "concrete", "character", "pov", "humor"),
    "dialogue_voice": ("dialogue", "humor", "character", "concrete", "reader_trust"),
    "action_physicality": ("action", "character", "continuity", "pacing", "concrete"),
    "continuity_outline": ("continuity", "outline_obedience", "reader_trust", "scene", "style_consistency"),
    "idea_generation": ("reader_trust", "character", "outline_obedience", "concrete", "metaphor"),
    "outline_design": ("outline_obedience", "pacing", "continuity", "character", "scene"),
    "revision_craft": ("continuity", "prose", "style_consistency", "reader_trust", "scene"),
    "idea_shaping": ("character", "reader_trust", "outline_obedience", "emotion", "concrete"),
    "arc_mapping": ("character", "outline_obedience", "pacing", "continuity", "reader_trust"),
    "scene_planning": ("scene", "pacing", "outline_obedience", "concrete", "action"),
    "revision_diagnosis": ("reader_trust", "scene", "continuity", "pacing", "style_consistency"),
}

# Craft pressure tags used by the outline bank, mapped to the lens that the
# chapter supplies on its own (before the category's own lens is added).
PRESSURE_LENS = {
    "pov": "pov",
    "concrete": "concrete",
    "character": "character",
    "scene": "scene",
    "pacing": "pacing",
    "emotion": "emotion",
    "dialogue": "dialogue",
    "humor": "humor",
    "action": "action",
    "worldbuilding": "worldbuilding",
    "continuity": "continuity",
    "outline": "outline_obedience",
    "trust": "reader_trust",
    "metaphor": "metaphor",
    "prose": "prose",
    "surface": "ai_patterns",
    "consistency": "style_consistency",
}

# Second lens: what kind of record it is and what the chapter is carrying.
TYPE_LENSES = {
    "transition": ("scene", "pacing", "continuity"),
    "reasoning": ("outline_obedience", "reader_trust", "pacing"),
    "negative": ("ai_patterns", "reader_trust", "outline_obedience"),
}
