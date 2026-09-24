"""The craft rule registry.

Every authored paragraph in the generator library is written to encode one or
more of these rules. The build step tags each record with the rules its
paragraphs carry, so a training run can balance, weight, or ablate the signal
per rule.

Structure:
    GROUPS  -> ordered craft groups, each with the rule ids it contains
    RULES   -> rule id -> (key, category, lens) where
                 key      short stable slug for filtering
                 category the record category whose library encodes the rule
                 lens     shared lens pool applied on top of every category

Rule numbering follows the project craft guide exactly (1-260).
"""

GROUPS = {
    "pov_and_perception": {
        "label": "POV and character perception",
        "ids": list(range(1, 19)),
    },
    "concrete_before_abstract": {
        "label": "Concrete before abstract",
        "ids": list(range(19, 28)),
    },
    "prose_style": {
        "label": "Prose style",
        "ids": list(range(28, 47)),
    },
    "metaphor_and_imagery": {
        "label": "Metaphors and imagery",
        "ids": list(range(47, 58)),
    },
    "emotion": {
        "label": "Emotion",
        "ids": list(range(58, 76)),
    },
    "dialogue": {
        "label": "Dialogue",
        "ids": list(range(76, 100)),
    },
    "scene_construction": {
        "label": "Scene construction",
        "ids": list(range(100, 118)),
    },
    "action_and_combat": {
        "label": "Action and combat",
        "ids": list(range(118, 137)),
    },
    "worldbuilding": {
        "label": "Worldbuilding",
        "ids": list(range(137, 151)),
    },
    "characterization": {
        "label": "Characterization",
        "ids": list(range(151, 168)),
    },
    "humor": {
        "label": "Humor",
        "ids": list(range(168, 176)),
    },
    "pacing_and_chapters": {
        "label": "Pacing and chapter structure",
        "ids": list(range(176, 187)),
    },
    "reader_trust": {
        "label": "Reader trust",
        "ids": list(range(187, 197)),
    },
    "ai_pattern_avoidance": {
        "label": "Avoiding recognizable AI-writing patterns",
        "ids": list(range(197, 214)),
    },
    "plot_and_outline_obedience": {
        "label": "Plot and outline obedience",
        "ids": list(range(214, 227)),
    },
    "continuity": {
        "label": "Continuity across a whole novel",
        "ids": list(range(227, 241)),
    },
    "style_consistency": {
        "label": "Style consistency",
        "ids": list(range(241, 248)),
    },
    "overarching": {
        "label": "The most important overarching rules",
        "ids": list(range(248, 261)),
    },
}

# key, category, lens  -- lens names must exist in lenses.LENSES
RULES = {
    1: ("inside_character", "pov_perception", "pov"),
    2: ("notice_first", "pov_perception", "pov"),
    3: ("perceivable_only", "pov_perception", "pov"),
    4: ("filter_by_priority", "pov_perception", "pov"),
    5: ("no_author_knowledge", "pov_perception", "pov"),
    6: ("limited_knowledge", "pov_perception", "continuity"),
    7: ("allowed_misreading", "pov_perception", "pov"),
    8: ("wrong_assumptions", "pov_perception", "pov"),
    9: ("no_immediate_correction", "information_management", "reader_trust"),
    10: ("personality_shapes_reading", "pov_perception", "pov"),
    11: ("thoughts_not_essays", "pov_perception", "prose"),
    12: ("mundane_in_big_moments", "pov_perception", "character"),
    13: ("petty_coexists", "pov_perception", "character"),
    14: ("opaque_own_emotions", "emotion_craft", "emotion"),
    15: ("contradictory_feelings", "emotion_craft", "emotion"),
    16: ("not_every_observation_profound", "prose_discipline", "prose"),
    17: ("not_every_thought_relevant", "pov_perception", "character"),
    18: ("worldview_persists", "pov_perception", "continuity"),
    19: ("concrete_over_abstract", "concrete_grounding", "concrete"),
    20: ("enact_unease", "concrete_grounding", "concrete"),
    21: ("anger_through_behavior", "concrete_grounding", "concrete"),
    22: ("nervousness_through_body", "concrete_grounding", "concrete"),
    23: ("experience_before_naming", "emotion_craft", "emotion"),
    24: ("physical_grounding_under_load", "concrete_grounding", "concrete"),
    25: ("contact_with_surroundings", "concrete_grounding", "concrete"),
    26: ("avoid_abstract_stretches", "prose_discipline", "prose"),
    27: ("incidental_over_atmospheric", "concrete_grounding", "concrete"),
    28: ("clear_natural_prose", "prose_discipline", "prose"),
    29: ("simple_precise_diction", "prose_discipline", "prose"),
    30: ("not_every_sentence_beautiful", "prose_discipline", "ai_patterns"),
    31: ("not_every_sentence_memorable", "prose_discipline", "ai_patterns"),
    32: ("invisible_prose", "prose_discipline", "prose"),
    33: ("selective_strength", "prose_discipline", "prose"),
    34: ("no_literary_posturing", "prose_discipline", "ai_patterns"),
    35: ("no_purple_prose", "prose_discipline", "ai_patterns"),
    36: ("no_decorative_adjectives", "prose_discipline", "ai_patterns"),
    37: ("no_description_stacking", "prose_discipline", "ai_patterns"),
    38: ("one_precise_image", "metaphor_imagery", "metaphor"),
    39: ("intentional_rhythm", "prose_discipline", "prose"),
    40: ("varied_sentence_length", "prose_discipline", "ai_patterns"),
    41: ("no_repetitive_structures", "prose_discipline", "ai_patterns"),
    42: ("vary_sentence_openings", "prose_discipline", "ai_patterns"),
    43: ("no_uniform_paragraph_rhythm", "prose_discipline", "ai_patterns"),
    44: ("short_for_speed_or_weight", "prose_discipline", "prose"),
    45: ("long_for_processing", "prose_discipline", "prose"),
    46: ("fragments_not_manufactured", "prose_discipline", "ai_patterns"),
    47: ("fewer_stronger_metaphors", "metaphor_imagery", "metaphor"),
    48: ("no_metaphor_per_paragraph", "metaphor_imagery", "metaphor"),
    49: ("no_impressive_metaphors", "metaphor_imagery", "metaphor"),
    50: ("metaphor_fits_pov", "metaphor_imagery", "metaphor"),
    51: ("avoid_generic_ai_metaphors", "metaphor_imagery", "ai_patterns"),
    52: ("no_metaphor_vocabulary_drift", "metaphor_imagery", "style_consistency"),
    53: ("no_metaphor_chains", "metaphor_imagery", "metaphor"),
    54: ("concrete_before_metaphor", "metaphor_imagery", "metaphor"),
    55: ("literal_can_be_strongest", "metaphor_imagery", "metaphor"),
    56: ("no_forced_symbolism", "metaphor_imagery", "reader_trust"),
    57: ("objects_can_just_exist", "metaphor_imagery", "reader_trust"),
    58: ("emotion_through_behavior", "emotion_craft", "emotion"),
    59: ("dont_name_emotions", "emotion_craft", "emotion"),
    60: ("no_formulaic_reactions", "emotion_craft", "ai_patterns"),
    61: ("surprise_not_widened_eyes", "emotion_craft", "ai_patterns"),
    62: ("fear_not_always_shaking", "emotion_craft", "ai_patterns"),
    63: ("sadness_not_always_tears", "emotion_craft", "ai_patterns"),
    64: ("individual_reactions", "emotion_craft", "character"),
    65: ("delayed_emotion", "emotion_craft", "emotion"),
    66: ("suppressed_emotion", "emotion_craft", "emotion"),
    67: ("misread_own_emotion", "emotion_craft", "emotion"),
    68: ("inappropriate_reaction", "emotion_craft", "character"),
    69: ("laughter_when_uncomfortable", "emotion_craft", "humor"),
    70: ("practical_under_fear", "emotion_craft", "character"),
    71: ("small_problem_focus", "emotion_craft", "emotion"),
    72: ("dont_resolve_emotion_fast", "emotion_craft", "emotion"),
    73: ("emotion_changes_gradually", "emotion_craft", "emotion"),
    74: ("mixed_emotions", "emotion_craft", "emotion"),
    75: ("emotional_consequences_persist", "emotion_craft", "continuity"),
    76: ("dialogue_sounds_spoken", "dialogue_voice", "dialogue"),
    77: ("no_reader_exposition", "dialogue_voice", "dialogue"),
    78: ("no_exposition_as_dialogue", "dialogue_voice", "reader_trust"),
    79: ("distinct_voices", "dialogue_voice", "dialogue"),
    80: ("voice_from_person", "dialogue_voice", "dialogue"),
    81: ("no_shared_vocabulary", "dialogue_voice", "style_consistency"),
    82: ("natural_contractions", "dialogue_voice", "dialogue"),
    83: ("allow_interruptions", "dialogue_voice", "dialogue"),
    84: ("allow_hesitation", "dialogue_voice", "dialogue"),
    85: ("allow_subject_changes", "dialogue_voice", "dialogue"),
    86: ("mutual_misunderstanding", "dialogue_voice", "dialogue"),
    87: ("use_subtext", "dialogue_voice", "dialogue"),
    88: ("say_what_they_mean_not", "dialogue_voice", "dialogue"),
    89: ("characters_can_lie", "dialogue_voice", "character"),
    90: ("avoid_answering", "dialogue_voice", "dialogue"),
    91: ("answer_other_question", "dialogue_voice", "dialogue"),
    92: ("defensive_speech", "dialogue_voice", "character"),
    93: ("conversations_not_efficient", "dialogue_voice", "dialogue"),
    94: ("irrelevant_remarks_allowed", "dialogue_voice", "dialogue"),
    95: ("dialogue_reveals_relationships", "dialogue_voice", "dialogue"),
    96: ("no_perfect_comebacks", "dialogue_voice", "ai_patterns"),
    97: ("late_perfect_response", "dialogue_voice", "character"),
    98: ("not_every_exchange_witty", "dialogue_voice", "humor"),
    99: ("humor_from_character", "humor_craft", "humor"),
    100: ("every_scene_has_reason", "scene_construction", "outline_obedience"),
    101: ("want_in_every_scene", "scene_construction", "scene"),
    102: ("scenes_have_obstacles", "scene_construction", "scene"),
    103: ("characters_can_fail", "conflict_escalation", "scene"),
    104: ("scenes_produce_consequences", "plot_architecture", "scene"),
    105: ("not_every_scene_main_plot", "scene_construction", "pacing"),
    106: ("smaller_concerns_between", "scene_construction", "pacing"),
    107: ("let_scenes_breathe", "scene_construction", "pacing"),
    108: ("dont_rush_events", "momentum", "pacing"),
    109: ("quieter_scenes_contrast", "scene_construction", "pacing"),
    110: ("uneven_scene_weight", "scene_construction", "pacing"),
    111: ("build_intensity", "tension", "pacing"),
    112: ("register_contrast", "scene_construction", "pacing"),
    113: ("avoid_repetitive_openings", "chapter_arcs", "ai_patterns"),
    114: ("enter_late", "scene_construction", "scene"),
    115: ("leave_when_done", "scene_construction", "scene"),
    116: ("dont_summarize_interesting", "momentum", "pacing"),
    117: ("dont_pad_unimportant", "momentum", "pacing"),
    118: ("action_understandable", "action_physicality", "action"),
    119: ("track_positions", "action_physicality", "action"),
    120: ("track_objects", "action_physicality", "continuity"),
    121: ("respect_physical_limits", "action_physicality", "action"),
    122: ("no_battlefield_teleporting", "action_physicality", "action"),
    123: ("no_perfect_move", "conflict_escalation", "action"),
    124: ("combat_contains_error", "action_physicality", "action"),
    125: ("characters_tire", "action_physicality", "action"),
    126: ("injuries_have_consequences", "action_physicality", "continuity"),
    127: ("selective_action_senses", "action_physicality", "action"),
    128: ("dont_slow_every_movement", "action_physicality", "action"),
    129: ("slow_at_importance", "action_physicality", "pacing"),
    130: ("speed_through_predictable", "action_physicality", "pacing"),
    131: ("combat_reveals_character", "action_physicality", "character"),
    132: ("different_characters_fight_differently", "action_physicality", "character"),
    133: ("adapt_when_plan_fails", "conflict_escalation", "action"),
    134: ("power_doesnt_solve_all", "conflict_escalation", "outline_obedience"),
    135: ("abilities_have_limits", "action_physicality", "outline_obedience"),
    136: ("no_convenient_abilities", "action_physicality", "outline_obedience"),
    137: ("worldbuilding_through_story", "worldbuilding_scale", "worldbuilding"),
    138: ("no_encyclopedia_stops", "worldbuilding_scale", "worldbuilding"),
    139: ("world_touches_ordinary_life", "worldbuilding_scale", "worldbuilding"),
    140: ("fantastical_consequences", "worldbuilding_scale", "worldbuilding"),
    141: ("magic_is_of_the_world", "worldbuilding_scale", "worldbuilding"),
    142: ("rules_before_solutions", "worldbuilding_scale", "outline_obedience"),
    143: ("rules_stay_consistent", "worldbuilding_scale", "continuity"),
    144: ("terminology_consistent", "worldbuilding_scale", "style_consistency"),
    145: ("reinforce_by_use", "worldbuilding_scale", "worldbuilding"),
    146: ("uneven_world_knowledge", "worldbuilding_scale", "pov"),
    147: ("no_walking_encyclopedias", "worldbuilding_scale", "character"),
    148: ("mystery_is_valuable", "information_management", "reader_trust"),
    149: ("dont_explain_strange_at_once", "information_management", "reader_trust"),
    150: ("not_every_mystery_answered", "information_management", "reader_trust"),
    151: ("personalities_not_roles", "character_decisions", "character"),
    152: ("no_sitcom_roles", "character_decisions", "character"),
    153: ("conflicting_traits", "character_decisions", "character"),
    154: ("behavior_varies_by_company", "character_decisions", "character"),
    155: ("relationships_change", "character_decisions", "continuity"),
    156: ("characters_remember", "character_decisions", "continuity"),
    157: ("arguments_have_consequences", "character_decisions", "continuity"),
    158: ("trust_develops_gradually", "character_decisions", "character"),
    159: ("characters_misunderstand_each_other", "character_decisions", "character"),
    160: ("friendships_have_friction", "character_decisions", "character"),
    161: ("preferences_unrelated_to_plot", "character_decisions", "character"),
    162: ("habits_and_irritations", "character_decisions", "character"),
    163: ("not_everyone_insightful", "character_decisions", "character"),
    164: ("characters_can_be_wrong", "character_decisions", "character"),
    165: ("characters_can_be_selfish", "character_decisions", "character"),
    166: ("stupid_decisions_not_stupid_people", "character_decisions", "character"),
    167: ("decide_from_their_knowledge", "character_decisions", "continuity"),
    168: ("humor_from_character_timing", "humor_craft", "humor"),
    169: ("no_jokes_to_defuse_seriousness", "humor_craft", "humor"),
    170: ("humor_can_fail", "humor_craft", "humor"),
    171: ("different_senses_of_humor", "humor_craft", "character"),
    172: ("humor_as_characterization", "humor_craft", "humor"),
    173: ("not_one_joke_deliverer", "humor_craft", "character"),
    174: ("serious_can_be_funny", "humor_craft", "character"),
    175: ("dont_undercut_emotion_with_joke", "humor_craft", "emotion"),
    176: ("no_maximum_excitement_always", "tension", "pacing"),
    177: ("rising_and_falling_tension", "tension", "pacing"),
    178: ("major_events_have_aftermath", "plot_architecture", "pacing"),
    179: ("dont_skip_consequences", "plot_architecture", "continuity"),
    180: ("no_artificial_cliffhangers", "chapter_arcs", "ai_patterns"),
    181: ("quiet_chapter_endings", "chapter_arcs", "pacing"),
    182: ("reveals_need_setup", "setup_payoff", "outline_obedience"),
    183: ("foreshadowing_natural_in_retrospect", "setup_payoff", "reader_trust"),
    184: ("dont_over_foreshadow", "setup_payoff", "reader_trust"),
    185: ("no_twists_against_characterization", "setup_payoff", "outline_obedience"),
    186: ("accumulate_mysteries", "information_management", "reader_trust"),
    187: ("trust_the_reader", "information_management", "reader_trust"),
    188: ("no_show_then_explain", "information_management", "reader_trust"),
    189: ("no_repetition_of_information", "information_management", "reader_trust"),
    190: ("dont_dictate_feeling", "information_management", "reader_trust"),
    191: ("dont_emphasize_importance", "information_management", "reader_trust"),
    192: ("dont_underline_symbolism", "information_management", "reader_trust"),
    193: ("let_readers_connect", "information_management", "reader_trust"),
    194: ("no_artificial_ignorance", "information_management", "outline_obedience"),
    195: ("no_unnatural_concealment", "information_management", "reader_trust"),
    196: ("mystery_from_uncertainty", "information_management", "reader_trust"),
    197: ("no_repetitive_templates", "prose_discipline", "ai_patterns"),
    198: ("avoid_not_x_but_y", "prose_discipline", "ai_patterns"),
    199: ("avoid_rhetorical_questions", "prose_discipline", "ai_patterns"),
    200: ("avoid_em_dash_overuse", "prose_discipline", "ai_patterns"),
    201: ("avoid_constant_fragments", "prose_discipline", "ai_patterns"),
    202: ("avoid_filler_hedges", "prose_discipline", "ai_patterns"),
    203: ("avoid_eye_heart_breath_cliches", "prose_discipline", "ai_patterns"),
    204: ("avoid_felt_seemed_something", "prose_discipline", "ai_patterns"),
    205: ("avoid_atmospheric_filler", "prose_discipline", "ai_patterns"),
    206: ("pronoun_over_name_repetition", "prose_discipline", "ai_patterns"),
    207: ("avoid_adverb_padding", "prose_discipline", "ai_patterns"),
    208: ("avoid_tricolons", "prose_discipline", "ai_patterns"),
    209: ("no_dramatic_paragraph_enders", "prose_discipline", "ai_patterns"),
    210: ("no_trailer_chapters", "prose_discipline", "ai_patterns"),
    211: ("no_foreshadowing_language", "prose_discipline", "ai_patterns"),
    212: ("no_importance_announcements", "prose_discipline", "ai_patterns"),
    213: ("plain_vocabulary_over_fancy", "prose_discipline", "ai_patterns"),
    214: ("outline_is_constraint", "continuity_outline", "outline_obedience"),
    215: ("no_plot_rewrites", "continuity_outline", "outline_obedience"),
    216: ("no_competing_arcs", "continuity_outline", "outline_obedience"),
    217: ("no_relationship_rewrites", "continuity_outline", "outline_obedience"),
    218: ("no_world_rule_changes", "continuity_outline", "outline_obedience"),
    219: ("track_open_threads", "continuity_outline", "continuity"),
    220: ("track_clues_to_explanations", "continuity_outline", "continuity"),
    221: ("track_character_knowledge", "continuity_outline", "continuity"),
    222: ("track_state_ledger", "continuity_outline", "continuity"),
    223: ("establish_how_it_matters", "continuity_outline", "outline_obedience"),
    224: ("resolution_follows_established", "plot_architecture", "outline_obedience"),
    225: ("no_coincidence_solutions", "plot_architecture", "outline_obedience"),
    226: ("no_exactly_right_discovery", "plot_architecture", "outline_obedience"),
    227: ("maintain_story_bible", "continuity_outline", "continuity"),
    228: ("track_major_characters", "continuity_outline", "continuity"),
    229: ("track_physical_descriptions", "continuity_outline", "continuity"),
    230: ("track_personalities_relationships", "continuity_outline", "continuity"),
    231: ("track_locations", "continuity_outline", "continuity"),
    232: ("track_chronology", "continuity_outline", "continuity"),
    233: ("track_objects_possession", "continuity_outline", "continuity"),
    234: ("track_abilities_limits", "continuity_outline", "continuity"),
    235: ("track_secrets_and_who_knows", "continuity_outline", "continuity"),
    236: ("track_clues_and_mysteries", "continuity_outline", "continuity"),
    237: ("track_injuries_recovery", "continuity_outline", "continuity"),
    238: ("track_promises_commitments", "continuity_outline", "continuity"),
    239: ("track_previous_conversations", "continuity_outline", "continuity"),
    240: ("no_contradicting_earlier_chapters", "continuity_outline", "continuity"),
    241: ("style_rules_apply_throughout", "prose_discipline", "style_consistency"),
    242: ("no_generic_drift", "prose_discipline", "style_consistency"),
    243: ("no_statistical_default_prose", "prose_discipline", "style_consistency"),
    244: ("style_guide_is_constraint", "prose_discipline", "style_consistency"),
    245: ("explicit_rules_win_conflicts", "prose_discipline", "style_consistency"),
    246: ("no_author_imitation", "prose_discipline", "style_consistency"),
    247: ("consistent_voice_over_showpieces", "prose_discipline", "style_consistency"),
    248: ("character_before_description", "concrete_grounding", "concrete"),
    249: ("concrete_before_abstract", "concrete_grounding", "concrete"),
    250: ("specific_before_generic", "concrete_grounding", "concrete"),
    251: ("behavior_before_explanation", "emotion_craft", "concrete"),
    252: ("subtext_before_exposition", "dialogue_voice", "dialogue"),
    253: ("restraint_before_excess", "prose_discipline", "prose"),
    254: ("consistency_before_improvisation", "continuity_outline", "continuity"),
    255: ("naturalness_before_cleverness", "prose_discipline", "style_consistency"),
    256: ("consequences_before_resets", "continuity_outline", "outline_obedience"),
    257: ("reader_trust_before_explanation", "information_management", "reader_trust"),
    258: ("character_knowledge_before_author", "continuity_outline", "continuity"),
    259: ("strong_moments_earned", "tension", "pacing"),
    260: ("prose_serves_story", "prose_discipline", "prose"),
}

# Rule ids whose library lives in the eight newly authored craft categories.
NEW_CRAFT_CATEGORIES = (
    "pov_perception",
    "concrete_grounding",
    "prose_discipline",
    "metaphor_imagery",
    "emotion_craft",
    "dialogue_voice",
    "action_physicality",
    "continuity_outline",
)

# Humor rules live inside the dialogue and voice library (spoken timing and
# character voice carry nearly all of the humor signal).
CATEGORY_ALIASES = {"humor_craft": "dialogue_voice", "worldbuilding_scale": "epic_scale"}

# The generative libraries reason at brainstorming, outlining and drafting, so
# they carry the guide rules that govern those decisions rather than falling back
# on a single lens. Each list is the subset of the rule registry that the
# library's paragraphs encode, so a tagged record's rules describe what its
# reasoning actually implements.
GENERATIVE_RULES = {
    "idea_generation": (
        151, 152, 153, 154, 155, 156, 160, 161, 162, 163, 164, 165, 166, 167,
        178, 179, 214, 215, 216, 224, 225, 226, 248, 249, 250, 251, 252,
    ),
    "idea_shaping": (
        151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 165, 166, 167,
        103, 133, 134, 137, 138, 139, 140, 141, 178, 179, 248, 251, 252, 253,
    ),
    "outline_design": (
        100, 104, 105, 106, 107, 108, 109, 110, 111, 113, 116, 117, 176, 177,
        178, 179, 180, 181, 182, 183, 184, 185, 186, 214, 215, 216, 217, 218,
        224, 225, 226, 227, 228, 229, 230, 231, 248, 249, 254, 255, 256, 257,
    ),
    "arc_mapping": (
        151, 152, 153, 154, 155, 156, 157, 158, 162, 166, 167, 103, 133, 134,
        137, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 214, 217, 218,
        225, 226, 227, 228, 229, 230, 231, 248, 251, 252, 254,
    ),
    "scene_planning": (
        100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 112, 114, 115, 118,
        119, 120, 124, 137, 176, 177, 182, 183, 214, 215, 216, 217, 218, 224,
        248, 249, 250, 256,
    ),
    "revision_craft": (
        19, 26, 28, 29, 32, 33, 39, 40, 41, 43, 72, 73, 75, 78, 100, 104, 108,
        111, 182, 183, 184, 197, 198, 199, 200, 201, 202, 209, 210, 213, 227,
        228, 231, 232, 241, 242, 243, 248, 249, 253, 255,
    ),
    "revision_diagnosis": (
        19, 23, 26, 28, 29, 30, 31, 32, 33, 35, 36, 37, 40, 41, 43, 46, 58,
        59, 60, 61, 62, 63, 64, 72, 73, 74, 75, 78, 79, 81, 96, 100, 101, 104,
        105, 108, 111, 176, 177, 186, 187, 188, 197, 209, 213, 227, 232, 248,
        253, 254, 257,
    ),
    "genre_epic_fantasy": (
        103, 133, 134, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147,
        151, 152, 153, 154, 166, 167, 176, 177, 178, 179, 180, 181, 182, 183,
        184, 185, 214, 215, 217, 225, 226, 227, 228, 230, 231, 248, 251, 252,
        254, 255, 256,
    ),
    "genre_scifi": (
        9, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 166, 167, 176, 177, 178, 179, 187, 188, 189,
        190, 214, 215, 216, 225, 226, 248, 250, 251, 252, 253, 255, 257,
    ),
    "genre_thriller": (
        101, 102, 103, 108, 109, 110, 111, 112, 116, 117, 118, 119, 120, 124,
        125, 126, 133, 134, 135, 136, 151, 152, 155, 156, 166, 167, 176, 177,
        186, 214, 215, 216, 224, 225, 226, 248, 249, 251, 253, 256, 259,
    ),
}


def rule_category(rule_id):
    cat = RULES[rule_id][1]
    return CATEGORY_ALIASES.get(cat, cat)


def rule_lens(rule_id):
    return RULES[rule_id][2]


def rules_for_category(category_id):
    if category_id in GENERATIVE_RULES:
        return sorted(GENERATIVE_RULES[category_id])
    return [rid for rid, (_k, cat, _l) in RULES.items()
            if CATEGORY_ALIASES.get(cat, cat) == category_id]


def rule_key(rule_id):
    return RULES[rule_id][0]


def all_rule_ids():
    return sorted(RULES)


def group_of(rule_id):
    for name, spec in GROUPS.items():
        if rule_id in spec["ids"]:
            return name
    raise KeyError(rule_id)
