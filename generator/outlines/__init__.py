"""Outline bank loader.

Every record in the dataset is built against one chapter of one outline: the
request hands the model the outline and the chapter position, and the response
reasons from that material. Load this module to get the full bank, plus a
structural check used by the build and by the validator tests.
"""

from generator.lenses import PRESSURE_LENS
from generator.outlines.cluster_fantasy import OUTLINES as FANTASY
from generator.outlines.cluster_horror import OUTLINES as HORROR
from generator.outlines.cluster_scifi import OUTLINES as SCIFI
from generator.outlines.cluster_crime import OUTLINES as CRIME
from generator.outlines.cluster_literary import OUTLINES as LITERARY
from generator.outlines.cluster_other import OUTLINES as OTHER

OUTLINES = FANTASY + HORROR + SCIFI + CRIME + LITERARY + OTHER

BY_ID = {o["id"]: o for o in OUTLINES}

OUTLINE_KEYS = (
    "id", "title", "form", "genre", "pov", "premise", "rules", "cast",
    "act1", "act2", "act3", "end", "threads", "promises", "chapters",
)

CAST_KEYS = ("name", "role", "want", "flaw", "secret", "contradiction", "knows")

CHAPTER_KEYS = ("n", "label", "function", "beats", "state_in", "state_out", "pressure")


def _chapter_number(value):
    if isinstance(value, int):
        return value
    text = str(value).strip().lower()
    if text.startswith("ch"):
        text = text[2:]
    return int(text)


def normalize(outline):
    """Return an outline copy whose thread chapter references are integers."""
    out = dict(outline)
    out["threads"] = [
        {
            "name": t["name"],
            "setup": _chapter_number(t["setup"]),
            "payoff": _chapter_number(t["payoff"]),
            "carry": t["carry"],
        }
        for t in outline["threads"]
    ]
    return out


OUTLINES = [normalize(o) for o in OUTLINES]
BY_ID = {o["id"]: o for o in OUTLINES}


def validate_outlines(outlines=None):
    """Structural check over the bank. Raises ValueError on the first problem."""
    outlines = outlines if outlines is not None else OUTLINES
    seen = set()
    for o in outlines:
        where = o.get("id", "?")
        for key in OUTLINE_KEYS:
            if key not in o:
                raise ValueError("%s missing outline key %s" % (where, key))
        if o["id"] in seen:
            raise ValueError("duplicate outline id %s" % o["id"])
        seen.add(o["id"])
        if len(o["cast"]) < 3:
            raise ValueError("%s has fewer than three cast members" % where)
        for member in o["cast"]:
            for key in CAST_KEYS:
                if key not in member:
                    raise ValueError("%s cast member missing %s" % (where, key))
        if len(o["rules"]) < 2:
            raise ValueError("%s needs at least two world rules" % where)
        if len(o["promises"]) < 2:
            raise ValueError("%s needs at least two reader promises" % where)
        numbers = [c["n"] for c in o["chapters"]]
        if numbers != list(range(1, len(numbers) + 1)):
            raise ValueError("%s chapter numbering is not contiguous" % where)
        for chapter in o["chapters"]:
            for key in CHAPTER_KEYS:
                if key not in chapter:
                    raise ValueError("%s chapter %s missing %s" % (where, chapter.get("n"), key))
            if not chapter["beats"]:
                raise ValueError("%s chapter %s has no beats" % (where, chapter["n"]))
            if chapter["pressure"] not in PRESSURE_LENS:
                raise ValueError(
                    "%s chapter %s has unknown pressure %r"
                    % (where, chapter["n"], chapter["pressure"])
                )
        for thread in o["threads"]:
            for key in ("setup", "payoff"):
                if thread[key] not in numbers:
                    raise ValueError(
                        "%s thread %s references missing chapter %s"
                        % (where, thread["name"], thread[key])
                    )
    return len(outlines)
