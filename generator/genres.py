"""The genre layer: epic fantasy, science fiction, thriller.

Each genre here is a promise to the reader plus a set of structural expectations
about what a story in that genre looks like. The lines below are written to be
placed inside an instruction, so a request that involves one of these genres
carries the genre's frame with it rather than leaving it implied.

Nothing here is prose: the genre's shape is described as structure (what the
story is about, who pays, what escalates, what the ending costs), never as a
written-out example.
"""

GENRES = {
    "epic_fantasy": {
        "label": "Epic fantasy",
        "category": "genre_epic_fantasy",
        "promise": "a large world with power in it, followed through people who pay for using it",
        "story_line": (
            "An epic fantasy story is built on a world whose powers are priced, a protagonist "
            "drawn into a conflict larger than their own life, allies whose interests diverge "
            "under pressure, and an ending that costs the protagonist something they cannot get back."
        ),
        "frame": (
            "The book is epic fantasy: the world's powers cost something to use, the scale is "
            "carried by consequences that land on specific people, and the protagonist's "
            "involvement comes from an obligation rather than a destiny."
        ),
        "covers": "world at scale, priced power, the long arc",
    },
    "scifi": {
        "label": "Science fiction",
        "category": "genre_scifi",
        "promise": "one change to the world, followed all the way to what it does to people",
        "story_line": (
            "A science fiction story takes one speculative change, works out its consequences "
            "honestly, and follows them into the lives that have to live with it: an ordinary want "
            "made expensive by the change, an opposing interest that benefits from the old order, "
            "and an ending that answers the question the premise raised."
        ),
        "frame": (
            "The book is science fiction: one speculative change is taken seriously in every "
            "direction it reaches, the story stays legible at the scale of people who live inside "
            "it, and the premise is taught through consequence rather than explanation."
        ),
        "covers": "the speculative change and its human consequences",
    },
    "thriller": {
        "label": "Thriller",
        "category": "genre_thriller",
        "promise": "a competent person under a clock, with something worse behind every answer",
        "story_line": (
            "A thriller story puts a protagonist with something to lose into a situation where the "
            "danger advances on its own schedule: an antagonist already ahead, information that is "
            "dangerous to hold, escalation in which every answer widens the problem, and a final "
            "confrontation forced by the protagonist's own choice."
        ),
        "frame": (
            "The book is a thriller: something in the story advances without the protagonist, the "
            "antagonist has a schedule of their own, and each solution the protagonist reaches "
            "makes the situation worse rather than safer."
        ),
        "covers": "the clock, the asymmetry, and escalation under pressure",
    },
}

GENRE_ORDER = ("epic_fantasy", "scifi", "thriller")

GENRE_BY_CATEGORY = {spec["category"]: gid for gid, spec in GENRES.items()}


def genre_of_category(category_id):
    return GENRE_BY_CATEGORY.get(category_id)


def frame_line(genre_id):
    return GENRES[genre_id]["frame"]


def story_line(genre_id):
    return GENRES[genre_id]["story_line"]
