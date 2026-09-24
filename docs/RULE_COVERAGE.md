# Rule Coverage: every rule of the craft guide, with worked examples

The dataset is built on the 260-rule craft registry in `generator/rules.py` (rule numbering follows the original craft guide). Every authored paragraph in the 28 libraries encodes one or more of these rules, and every record is tagged with the rules its reasoning implements.

This file is generated from the shipped build, so the counts and ids below are the shipped dataset. `examples` lists record ids you can open: each one reasons in a way that implements the rule. Rules are exercised across brainstorming, outlining, writing and revision wherever the rule applies, and every record also carries the craft lens paragraphs that share its rule's dimension.

| Measure | Value |
|---|---|
| rules in the registry | 260 |
| rules with at least one worked example | 260 |
| examples per rule (min / median / max) | 210 / 572 / 3279 |
| rules exercised at more than one record type | 260 |
| rules exercised while brainstorming, outlining or writing | 260 |

## pov and perception

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 1 | inside character | 212 | drafting | `t-pov_perception-0266` |
| 2 | notice first | 212 | drafting | `t-pov_perception-0266` |
| 3 | perceivable only | 212 | drafting | `t-pov_perception-0266` |
| 4 | filter by priority | 212 | drafting | `t-pov_perception-0266` |
| 5 | no author knowledge | 212 | drafting | `t-pov_perception-0266` |
| 6 | limited knowledge | 212 | drafting | `t-pov_perception-0266` |
| 7 | allowed misreading | 212 | drafting | `t-pov_perception-0266` |
| 8 | wrong assumptions | 212 | drafting | `t-pov_perception-0266` |
| 9 | no immediate correction | 615 | drafting, ideation, outline | `n-genre_scifi-0886` `n-information_management-0412` |
| 10 | personality shapes reading | 212 | drafting | `t-pov_perception-0266` |
| 11 | thoughts not essays | 212 | drafting | `t-pov_perception-0266` |
| 12 | mundane in big moments | 212 | drafting | `t-pov_perception-0266` |
| 13 | petty coexists | 212 | drafting | `t-pov_perception-0266` |
| 14 | opaque own emotions | 212 | drafting | `t-emotion_craft-2201` |
| 15 | contradictory feelings | 212 | drafting | `t-emotion_craft-2201` |
| 16 | not every observation profound | 212 | drafting | `t-prose_discipline-0034` |
| 17 | not every thought relevant | 212 | drafting | `t-pov_perception-0266` |
| 18 | worldview persists | 212 | drafting | `t-pov_perception-0266` |

## concrete before abstract

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 19 | concrete over abstract | 931 | drafting, revision | `t-concrete_grounding-1974` `n-revision_craft-1722` |
| 20 | enact unease | 211 | drafting | `t-concrete_grounding-1974` |
| 21 | anger through behavior | 211 | drafting | `t-concrete_grounding-1974` |
| 22 | nervousness through body | 211 | drafting | `t-concrete_grounding-1974` |
| 23 | experience before naming | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 24 | physical grounding under load | 211 | drafting | `t-concrete_grounding-1974` |
| 25 | contact with surroundings | 211 | drafting | `t-concrete_grounding-1974` |
| 26 | avoid abstract stretches | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 27 | incidental over atmospheric | 211 | drafting | `t-concrete_grounding-1974` |

## prose style

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 28 | clear natural prose | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 29 | simple precise diction | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 30 | not every sentence beautiful | 572 | drafting, revision | `t-prose_discipline-0034` `r-revision_diagnosis-1638` |
| 31 | not every sentence memorable | 572 | drafting, revision | `t-prose_discipline-0034` `r-revision_diagnosis-1638` |
| 32 | invisible prose | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 33 | selective strength | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 34 | no literary posturing | 212 | drafting | `t-prose_discipline-0034` |
| 35 | no purple prose | 572 | drafting, revision | `t-prose_discipline-0034` `r-revision_diagnosis-1638` |
| 36 | no decorative adjectives | 572 | drafting, revision | `t-prose_discipline-0034` `r-revision_diagnosis-1638` |
| 37 | no description stacking | 572 | drafting, revision | `t-prose_discipline-0034` `r-revision_diagnosis-1638` |
| 38 | one precise image | 210 | drafting | `t-metaphor_imagery-2615` |
| 39 | intentional rhythm | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 40 | varied sentence length | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 41 | no repetitive structures | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 42 | vary sentence openings | 212 | drafting | `t-prose_discipline-0034` |
| 43 | no uniform paragraph rhythm | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 44 | short for speed or weight | 212 | drafting | `t-prose_discipline-0034` |
| 45 | long for processing | 212 | drafting | `t-prose_discipline-0034` |
| 46 | fragments not manufactured | 572 | drafting, revision | `t-prose_discipline-0034` `r-revision_diagnosis-1638` |

## metaphor and imagery

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 47 | fewer stronger metaphors | 210 | drafting | `t-metaphor_imagery-2615` |
| 48 | no metaphor per paragraph | 210 | drafting | `t-metaphor_imagery-2615` |
| 49 | no impressive metaphors | 210 | drafting | `t-metaphor_imagery-2615` |
| 50 | metaphor fits pov | 210 | drafting | `t-metaphor_imagery-2615` |
| 51 | avoid generic ai metaphors | 210 | drafting | `t-metaphor_imagery-2615` |
| 52 | no metaphor vocabulary drift | 210 | drafting | `t-metaphor_imagery-2615` |
| 53 | no metaphor chains | 210 | drafting | `t-metaphor_imagery-2615` |
| 54 | concrete before metaphor | 210 | drafting | `t-metaphor_imagery-2615` |
| 55 | literal can be strongest | 210 | drafting | `t-metaphor_imagery-2615` |
| 56 | no forced symbolism | 210 | drafting | `t-metaphor_imagery-2615` |
| 57 | objects can just exist | 210 | drafting | `t-metaphor_imagery-2615` |

## emotion

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 58 | emotion through behavior | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 59 | dont name emotions | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 60 | no formulaic reactions | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 61 | surprise not widened eyes | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 62 | fear not always shaking | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 63 | sadness not always tears | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 64 | individual reactions | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 65 | delayed emotion | 212 | drafting | `t-emotion_craft-2201` |
| 66 | suppressed emotion | 212 | drafting | `t-emotion_craft-2201` |
| 67 | misread own emotion | 212 | drafting | `t-emotion_craft-2201` |
| 68 | inappropriate reaction | 212 | drafting | `t-emotion_craft-2201` |
| 69 | laughter when uncomfortable | 212 | drafting | `t-emotion_craft-2201` |
| 70 | practical under fear | 212 | drafting | `t-emotion_craft-2201` |
| 71 | small problem focus | 212 | drafting | `t-emotion_craft-2201` |
| 72 | dont resolve emotion fast | 932 | drafting, revision | `t-emotion_craft-2201` `n-revision_craft-1722` |
| 73 | emotion changes gradually | 932 | drafting, revision | `t-emotion_craft-2201` `n-revision_craft-1722` |
| 74 | mixed emotions | 572 | drafting, revision | `t-emotion_craft-2201` `r-revision_diagnosis-1638` |
| 75 | emotional consequences persist | 932 | drafting, revision | `t-emotion_craft-2201` `n-revision_craft-1722` |

## dialogue

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 76 | dialogue sounds spoken | 210 | drafting | `t-dialogue_voice-0941` |
| 77 | no reader exposition | 210 | drafting | `t-dialogue_voice-0941` |
| 78 | no exposition as dialogue | 930 | drafting, revision | `t-dialogue_voice-0941` `n-revision_craft-1722` |
| 79 | distinct voices | 570 | drafting, revision | `t-dialogue_voice-0941` `r-revision_diagnosis-1638` |
| 80 | voice from person | 210 | drafting | `t-dialogue_voice-0941` |
| 81 | no shared vocabulary | 570 | drafting, revision | `t-dialogue_voice-0941` `r-revision_diagnosis-1638` |
| 82 | natural contractions | 210 | drafting | `t-dialogue_voice-0941` |
| 83 | allow interruptions | 210 | drafting | `t-dialogue_voice-0941` |
| 84 | allow hesitation | 210 | drafting | `t-dialogue_voice-0941` |
| 85 | allow subject changes | 210 | drafting | `t-dialogue_voice-0941` |
| 86 | mutual misunderstanding | 210 | drafting | `t-dialogue_voice-0941` |
| 87 | use subtext | 210 | drafting | `t-dialogue_voice-0941` |
| 88 | say what they mean not | 210 | drafting | `t-dialogue_voice-0941` |
| 89 | characters can lie | 210 | drafting | `t-dialogue_voice-0941` |
| 90 | avoid answering | 210 | drafting | `t-dialogue_voice-0941` |
| 91 | answer other question | 210 | drafting | `t-dialogue_voice-0941` |
| 92 | defensive speech | 210 | drafting | `t-dialogue_voice-0941` |
| 93 | conversations not efficient | 210 | drafting | `t-dialogue_voice-0941` |
| 94 | irrelevant remarks allowed | 210 | drafting | `t-dialogue_voice-0941` |
| 95 | dialogue reveals relationships | 210 | drafting | `t-dialogue_voice-0941` |
| 96 | no perfect comebacks | 570 | drafting, revision | `t-dialogue_voice-0941` `r-revision_diagnosis-1638` |
| 97 | late perfect response | 210 | drafting | `t-dialogue_voice-0941` |
| 98 | not every exchange witty | 210 | drafting | `t-dialogue_voice-0941` |
| 99 | humor from character | 210 | drafting | `t-dialogue_voice-0941` |

## scene construction

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 100 | every scene has reason | 1341 | drafting, outline, revision | `n-outline_design-0296` `t-scene_construction-2812` |
| 101 | want in every scene | 1145 | drafting, ideation, outline, revision | `r-genre_thriller-0672` `n-scene_planning-0070` |
| 102 | scenes have obstacles | 785 | drafting, ideation, outline | `r-genre_thriller-0672` `n-scene_planning-0070` |
| 103 | characters can fail | 1709 | drafting, ideation, outline | `r-idea_shaping-0750` `n-genre_epic_fantasy-0495` |
| 104 | scenes produce consequences | 1376 | drafting, outline, revision | `n-outline_design-0296` `r-plot_architecture-1151` |
| 105 | not every scene main plot | 981 | drafting, outline, revision | `n-outline_design-0296` `t-scene_construction-2812` |
| 106 | smaller concerns between | 621 | drafting, outline | `n-outline_design-0296` `t-scene_construction-2812` |
| 107 | let scenes breathe | 621 | drafting, outline | `n-outline_design-0296` `t-scene_construction-2812` |
| 108 | dont rush events | 1542 | drafting, ideation, outline, revision | `r-genre_thriller-0672` `n-outline_design-0296` |
| 109 | quieter scenes contrast | 990 | drafting, ideation, outline | `r-genre_thriller-0672` `n-outline_design-0296` |
| 110 | uneven scene weight | 990 | drafting, ideation, outline | `r-genre_thriller-0672` `n-outline_design-0296` |
| 111 | build intensity | 1542 | drafting, ideation, outline, revision | `r-genre_thriller-0672` `n-outline_design-0296` |
| 112 | register contrast | 785 | drafting, ideation, outline | `r-genre_thriller-0672` `n-scene_planning-0070` |
| 113 | avoid repetitive openings | 453 | drafting, outline | `n-outline_design-0296` `t-chapter_arcs-3360` |
| 114 | enter late | 416 | drafting, outline | `n-scene_planning-0070` `t-scene_construction-2812` |
| 115 | leave when done | 416 | drafting, outline | `n-scene_planning-0070` `t-scene_construction-2812` |
| 116 | dont summarize interesting | 822 | drafting, ideation, outline | `r-genre_thriller-0672` `n-outline_design-0296` |
| 117 | dont pad unimportant | 822 | drafting, ideation, outline | `r-genre_thriller-0672` `n-outline_design-0296` |

## action and combat

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 118 | action understandable | 784 | drafting, ideation, outline | `r-genre_thriller-0672` `n-scene_planning-0070` |
| 119 | track positions | 784 | drafting, ideation, outline | `r-genre_thriller-0672` `n-scene_planning-0070` |
| 120 | track objects | 784 | drafting, ideation, outline | `r-genre_thriller-0672` `n-scene_planning-0070` |
| 121 | respect physical limits | 211 | drafting | `t-action_physicality-0459` |
| 122 | no battlefield teleporting | 211 | drafting | `t-action_physicality-0459` |
| 123 | no perfect move | 249 | drafting, outline | `n-conflict_escalation-0469` `t-conflict_escalation-2260` |
| 124 | combat contains error | 784 | drafting, ideation, outline | `r-genre_thriller-0672` `n-scene_planning-0070` |
| 125 | characters tire | 580 | drafting, ideation, outline | `r-genre_thriller-0672` `r-genre_thriller-0610` |
| 126 | injuries have consequences | 580 | drafting, ideation, outline | `r-genre_thriller-0672` `r-genre_thriller-0610` |
| 127 | selective action senses | 211 | drafting | `t-action_physicality-0459` |
| 128 | dont slow every movement | 211 | drafting | `t-action_physicality-0459` |
| 129 | slow at importance | 211 | drafting | `t-action_physicality-0459` |
| 130 | speed through predictable | 211 | drafting | `t-action_physicality-0459` |
| 131 | combat reveals character | 211 | drafting | `t-action_physicality-0459` |
| 132 | different characters fight differently | 211 | drafting | `t-action_physicality-0459` |
| 133 | adapt when plan fails | 1505 | drafting, ideation, outline | `r-idea_shaping-0750` `n-genre_epic_fantasy-0495` |
| 134 | power doesnt solve all | 1505 | drafting, ideation, outline | `r-idea_shaping-0750` `n-genre_epic_fantasy-0495` |
| 135 | abilities have limits | 580 | drafting, ideation, outline | `r-genre_thriller-0672` `r-genre_thriller-0610` |
| 136 | no convenient abilities | 580 | drafting, ideation, outline | `r-genre_thriller-0672` `r-genre_thriller-0610` |

## worldbuilding

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 137 | worldbuilding through story | 1704 | drafting, ideation, outline | `r-idea_shaping-0750` `n-genre_epic_fantasy-0495` |
| 138 | no encyclopedia stops | 1295 | drafting, ideation, outline | `r-idea_shaping-0750` `n-genre_epic_fantasy-0495` |
| 139 | world touches ordinary life | 1295 | drafting, ideation, outline | `r-idea_shaping-0750` `n-genre_epic_fantasy-0495` |
| 140 | fantastical consequences | 1295 | drafting, ideation, outline | `r-idea_shaping-0750` `n-genre_epic_fantasy-0495` |
| 141 | magic is of the world | 1295 | drafting, ideation, outline | `r-idea_shaping-0750` `n-genre_epic_fantasy-0495` |
| 142 | rules before solutions | 981 | drafting, ideation, outline | `n-genre_scifi-0886` `n-genre_epic_fantasy-0495` |
| 143 | rules stay consistent | 981 | drafting, ideation, outline | `n-genre_scifi-0886` `n-genre_epic_fantasy-0495` |
| 144 | terminology consistent | 981 | drafting, ideation, outline | `n-genre_scifi-0886` `n-genre_epic_fantasy-0495` |
| 145 | reinforce by use | 981 | drafting, ideation, outline | `n-genre_scifi-0886` `n-genre_epic_fantasy-0495` |
| 146 | uneven world knowledge | 981 | drafting, ideation, outline | `n-genre_scifi-0886` `n-genre_epic_fantasy-0495` |
| 147 | no walking encyclopedias | 981 | drafting, ideation, outline | `n-genre_scifi-0886` `n-genre_epic_fantasy-0495` |
| 148 | mystery is valuable | 615 | drafting, ideation, outline | `n-genre_scifi-0886` `n-information_management-0412` |
| 149 | dont explain strange at once | 615 | drafting, ideation, outline | `n-genre_scifi-0886` `n-information_management-0412` |
| 150 | not every mystery answered | 615 | drafting, ideation, outline | `n-genre_scifi-0886` `n-information_management-0412` |

## characterization

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 151 | personalities not roles | 2151 | drafting, ideation, outline | `r-idea_generation-0929` `n-genre_epic_fantasy-0495` |
| 152 | no sitcom roles | 2151 | drafting, ideation, outline | `r-idea_generation-0929` `n-genre_epic_fantasy-0495` |
| 153 | conflicting traits | 1782 | drafting, ideation, outline | `r-idea_generation-0929` `n-genre_epic_fantasy-0495` |
| 154 | behavior varies by company | 1782 | drafting, ideation, outline | `r-idea_generation-0929` `n-genre_epic_fantasy-0495` |
| 155 | relationships change | 1416 | drafting, ideation, outline | `r-idea_generation-0929` `n-arc_mapping-0198` |
| 156 | characters remember | 1416 | drafting, ideation, outline | `r-idea_generation-0929` `n-arc_mapping-0198` |
| 157 | arguments have consequences | 731 | drafting, ideation, outline | `r-idea_shaping-0750` `n-arc_mapping-0198` |
| 158 | trust develops gradually | 731 | drafting, ideation, outline | `r-idea_shaping-0750` `n-arc_mapping-0198` |
| 159 | characters misunderstand each other | 526 | drafting, ideation | `r-idea_shaping-0750` `n-character_decisions-1373` |
| 160 | friendships have friction | 842 | drafting, ideation | `r-idea_generation-0929` `n-character_decisions-1373` |
| 161 | preferences unrelated to plot | 842 | drafting, ideation | `r-idea_generation-0929` `n-character_decisions-1373` |
| 162 | habits and irritations | 733 | drafting, ideation, outline | `r-idea_generation-0929` `n-arc_mapping-0198` |
| 163 | not everyone insightful | 528 | drafting, ideation | `r-idea_generation-0929` `n-character_decisions-1373` |
| 164 | characters can be wrong | 528 | drafting, ideation | `r-idea_generation-0929` `n-character_decisions-1373` |
| 165 | characters can be selfish | 842 | drafting, ideation | `r-idea_generation-0929` `n-character_decisions-1373` |
| 166 | stupid decisions not stupid people | 2151 | drafting, ideation, outline | `r-idea_generation-0929` `n-genre_epic_fantasy-0495` |
| 167 | decide from their knowledge | 2151 | drafting, ideation, outline | `r-idea_generation-0929` `n-genre_epic_fantasy-0495` |

## humor

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 168 | humor from character timing | 210 | drafting | `t-dialogue_voice-0941` |
| 169 | no jokes to defuse seriousness | 210 | drafting | `t-dialogue_voice-0941` |
| 170 | humor can fail | 210 | drafting | `t-dialogue_voice-0941` |
| 171 | different senses of humor | 210 | drafting | `t-dialogue_voice-0941` |
| 172 | humor as characterization | 210 | drafting | `t-dialogue_voice-0941` |
| 173 | not one joke deliverer | 210 | drafting | `t-dialogue_voice-0941` |
| 174 | serious can be funny | 210 | drafting | `t-dialogue_voice-0941` |
| 175 | dont undercut emotion with joke | 210 | drafting | `t-dialogue_voice-0941` |

## pacing and chapters

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 176 | no maximum excitement always | 2326 | drafting, ideation, outline, revision | `r-genre_thriller-0672` `n-outline_design-0296` |
| 177 | rising and falling tension | 2326 | drafting, ideation, outline, revision | `r-genre_thriller-0672` `n-outline_design-0296` |
| 178 | major events have aftermath | 2022 | drafting, ideation, outline | `r-idea_generation-0929` `n-outline_design-0296` |
| 179 | dont skip consequences | 2022 | drafting, ideation, outline | `r-idea_generation-0929` `n-outline_design-0296` |
| 180 | no artificial cliffhangers | 1026 | drafting, ideation, outline | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 181 | quiet chapter endings | 1026 | drafting, ideation, outline | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 182 | reveals need setup | 1590 | drafting, ideation, outline, revision | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 183 | foreshadowing natural in retrospect | 1590 | drafting, ideation, outline, revision | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 184 | dont over foreshadow | 1386 | drafting, ideation, outline, revision | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 185 | no twists against characterization | 1026 | drafting, ideation, outline | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 186 | accumulate mysteries | 1182 | drafting, ideation, outline, revision | `r-genre_thriller-0672` `n-outline_design-0296` |

## reader trust

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 187 | trust the reader | 975 | drafting, ideation, outline, revision | `n-genre_scifi-0886` `n-information_management-0412` |
| 188 | no show then explain | 975 | drafting, ideation, outline, revision | `n-genre_scifi-0886` `n-information_management-0412` |
| 189 | no repetition of information | 615 | drafting, ideation, outline | `n-genre_scifi-0886` `n-information_management-0412` |
| 190 | dont dictate feeling | 615 | drafting, ideation, outline | `n-genre_scifi-0886` `n-information_management-0412` |
| 191 | dont emphasize importance | 248 | drafting, outline | `n-information_management-0412` `t-information_management-1698` |
| 192 | dont underline symbolism | 248 | drafting, outline | `n-information_management-0412` `t-information_management-1698` |
| 193 | let readers connect | 248 | drafting, outline | `n-information_management-0412` `t-information_management-1698` |
| 194 | no artificial ignorance | 248 | drafting, outline | `n-information_management-0412` `t-information_management-1698` |
| 195 | no unnatural concealment | 248 | drafting, outline | `n-information_management-0412` `t-information_management-1698` |
| 196 | mystery from uncertainty | 248 | drafting, outline | `n-information_management-0412` `t-information_management-1698` |

## ai pattern avoidance

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 197 | no repetitive templates | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 198 | avoid not x but y | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 199 | avoid rhetorical questions | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 200 | avoid em dash overuse | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 201 | avoid constant fragments | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 202 | avoid filler hedges | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 203 | avoid eye heart breath cliches | 212 | drafting | `t-prose_discipline-0034` |
| 204 | avoid felt seemed something | 212 | drafting | `t-prose_discipline-0034` |
| 205 | avoid atmospheric filler | 212 | drafting | `t-prose_discipline-0034` |
| 206 | pronoun over name repetition | 212 | drafting | `t-prose_discipline-0034` |
| 207 | avoid adverb padding | 212 | drafting | `t-prose_discipline-0034` |
| 208 | avoid tricolons | 212 | drafting | `t-prose_discipline-0034` |
| 209 | no dramatic paragraph enders | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 210 | no trailer chapters | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 211 | no foreshadowing language | 212 | drafting | `t-prose_discipline-0034` |
| 212 | no importance announcements | 212 | drafting | `t-prose_discipline-0034` |
| 213 | plain vocabulary over fancy | 932 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |

## plot and outline obedience

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 214 | outline is constraint | 2282 | drafting, ideation, outline | `r-idea_generation-0929` `n-outline_design-0296` |
| 215 | no plot rewrites | 2077 | drafting, ideation, outline | `r-idea_generation-0929` `n-outline_design-0296` |
| 216 | no competing arcs | 1709 | drafting, ideation, outline | `r-idea_generation-0929` `n-outline_design-0296` |
| 217 | no relationship rewrites | 1230 | drafting, ideation, outline | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 218 | no world rule changes | 862 | drafting, outline | `n-outline_design-0296` `t-continuity_outline-0688` |
| 219 | track open threads | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 220 | track clues to explanations | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 221 | track character knowledge | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 222 | track state ledger | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 223 | establish how it matters | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 224 | resolution follows established | 1341 | drafting, ideation, outline | `r-idea_generation-0929` `n-outline_design-0296` |
| 225 | no coincidence solutions | 2077 | drafting, ideation, outline | `r-idea_generation-0929` `n-outline_design-0296` |
| 226 | no exactly right discovery | 2077 | drafting, ideation, outline | `r-idea_generation-0929` `n-outline_design-0296` |

## continuity

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 227 | maintain story bible | 1746 | drafting, ideation, outline, revision | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 228 | track major characters | 1386 | drafting, ideation, outline, revision | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 229 | track physical descriptions | 658 | drafting, outline | `n-outline_design-0296` `t-continuity_outline-0688` |
| 230 | track personalities relationships | 1026 | drafting, ideation, outline | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 231 | track locations | 1386 | drafting, ideation, outline, revision | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 232 | track chronology | 968 | drafting, outline, revision | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 233 | track objects possession | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 234 | track abilities limits | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 235 | track secrets and who knows | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 236 | track clues and mysteries | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 237 | track injuries recovery | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 238 | track promises commitments | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 239 | track previous conversations | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 240 | no contradicting earlier chapters | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |

## style consistency

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 241 | style rules apply throughout | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 242 | no generic drift | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 243 | no statistical default prose | 572 | drafting, revision | `t-prose_discipline-0034` `n-revision_craft-1722` |
| 244 | style guide is constraint | 212 | drafting | `t-prose_discipline-0034` |
| 245 | explicit rules win conflicts | 212 | drafting | `t-prose_discipline-0034` |
| 246 | no author imitation | 212 | drafting | `t-prose_discipline-0034` |
| 247 | consistent voice over showpieces | 212 | drafting | `t-prose_discipline-0034` |

## overarching

| Rule | What it governs | Records | Stages | Example records |
|---|---|---|---|---|
| 248 | character before description | 3279 | drafting, ideation, outline, revision | `r-idea_generation-0929` `n-outline_design-0296` |
| 249 | concrete before abstract | 1665 | drafting, ideation, outline, revision | `r-idea_generation-0929` `n-outline_design-0296` |
| 250 | specific before generic | 1098 | drafting, ideation, outline | `r-idea_generation-0929` `n-scene_planning-0070` |
| 251 | behavior before explanation | 2151 | drafting, ideation, outline | `r-idea_generation-0929` `n-genre_epic_fantasy-0495` |
| 252 | subtext before exposition | 1780 | drafting, ideation, outline | `r-idea_generation-0929` `n-genre_epic_fantasy-0495` |
| 253 | restraint before excess | 1982 | drafting, ideation, outline, revision | `r-idea_shaping-0750` `r-genre_scifi-0552` |
| 254 | consistency before improvisation | 1386 | drafting, ideation, outline, revision | `n-genre_epic_fantasy-0858` `n-outline_design-0296` |
| 255 | naturalness before cleverness | 1512 | drafting, ideation, outline, revision | `n-genre_scifi-0886` `n-outline_design-0296` |
| 256 | consequences before resets | 1394 | drafting, ideation, outline | `r-genre_thriller-0672` `n-outline_design-0296` |
| 257 | reader trust before explanation | 1180 | drafting, ideation, outline, revision | `n-genre_scifi-0886` `n-outline_design-0296` |
| 258 | character knowledge before author | 248 | drafting, outline | `r-continuity_outline-0384` `t-continuity_outline-0688` |
| 259 | strong moments earned | 617 | drafting, ideation, outline | `r-genre_thriller-0672` `n-tension-0434` |
| 260 | prose serves story | 212 | drafting | `t-prose_discipline-0034` |
