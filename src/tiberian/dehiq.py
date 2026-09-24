"""Deḥiq (דחיק) detection for pure-Python path — Khan T1 §I.2.8.1.2.

Compress word-final unstressed long *qameṣ* / *segol* to half-long and
geminate the following word's initial consonant when the first word is
penultimately stressed and bound by a conjunctive accent or *maqqef*.
"""

from __future__ import annotations

import re

from tiberian.orthography import (
    ALEF,
    AYIN,
    HE,
    HET,
    PATAH,
    QAMATS,
    QAMATS_QATAN,
    SEGOL,
    SHEVA,
    Cluster,
    parse_word,
    vowel_quality,
)
from tiberian.syllables import is_vocalic_shewa

_CONJUNCTIVE = re.compile(r"[\u05A3-\u05AA\u05AC]")
_GUTTURAL = {ALEF, HE, HET, AYIN}


def _is_furtive_host(clusters: list[Cluster], i: int) -> bool:
    if i != len(clusters) - 1:
        return False
    c = clusters[i]
    if c.vowel != PATAH:
        return False
    if c.letter not in {HET, AYIN, HE}:
        return False
    if c.letter == HE and not c.dagesh:
        return False
    # Look back past matres for a high/mid vowel.
    for j in range(i - 1, -1, -1):
        prev = clusters[j]
        if prev.letter in {"י", "ו", "ה", "א"} and not prev.vowel and not prev.shewa and not prev.shureq:
            continue  # mater-like
        pq = "u" if prev.shureq else vowel_quality(prev)
        return pq in {"u", "o", "i", "e"}
    return False


def _raw_accent_index(clusters: list[Cluster]) -> int | None:
    for i, c in enumerate(clusters):
        if c.has_accent:
            return i
    return None


def _last_vocalic(clusters: list[Cluster]) -> int:
    for i in range(len(clusters) - 1, -1, -1):
        c = clusters[i]
        if c.shureq or c.hataf or (c.vowel and c.vowel != SHEVA):
            return i
        if c.shewa and is_vocalic_shewa(c, i, clusters):
            return i
    return max(0, len(clusters) - 1)


def _stress_ci(clusters: list[Cluster]) -> int:
    """Main-stress cluster index; never on a furtive-pataḥ host."""
    si = _raw_accent_index(clusters)
    if si is None:
        si = _last_vocalic(clusters)
    if _is_furtive_host(clusters, si) and si > 0:
        for j in range(si - 1, -1, -1):
            c = clusters[j]
            if c.shureq or c.hataf or (c.vowel and c.vowel != SHEVA):
                return j
            if c.shewa and is_vocalic_shewa(c, j, clusters):
                return j
    return si


def _vocalic_indices(clusters: list[Cluster]) -> list[int]:
    out: list[int] = []
    for i, c in enumerate(clusters):
        if c.shureq or c.hataf:
            out.append(i)
        elif c.vowel and c.vowel != SHEVA:
            out.append(i)
        elif c.shewa and is_vocalic_shewa(c, i, clusters):
            out.append(i)
    return out


def _penultimately_stressed(clusters: list[Cluster]) -> bool:
    voc = _vocalic_indices(clusters)
    if len(voc) < 2:
        return False
    return _stress_ci(clusters) < voc[-1]


def _final_is_lax_open(clusters: list[Cluster]) -> bool:
    if not clusters:
        return False
    # Skip final mater he/alef — the lax vowel sits on the preceding letter.
    idx = len(clusters) - 1
    last = clusters[idx]
    if last.letter in {HE, ALEF} and not last.vowel and not last.shewa and not last.dagesh:
        idx -= 1
        if idx < 0:
            return False
        last = clusters[idx]
    if last.meteg:
        return False
    return last.vowel in {QAMATS, QAMATS_QATAN, SEGOL}


def _initial_foot_stressed(clusters: list[Cluster]) -> bool:
    if not clusters:
        return False
    if clusters[0].has_accent:
        return True
    if (
        len(clusters) > 1
        and clusters[0].shewa
        and is_vocalic_shewa(clusters[0], 0, clusters)
        and any(c.has_accent for c in clusters[1:])
    ):
        # e.g. פְּרִי֙ — shewa then accented ri
        return True
    si = _stress_ci(clusters)
    voc = _vocalic_indices(clusters)
    if not voc:
        return False
    first_full = voc[0]
    if clusters[voc[0]].shewa and len(voc) > 1:
        first_full = voc[1]
    return si == first_full


def is_dehiq_pair(
    first_text: str,
    second_text: str,
    *,
    bound_by_maqaf: bool = False,
) -> bool:
    """True if ``first`` + ``second`` form a deḥiq / ʾathe me-raḥiq bond."""
    first = parse_word(first_text).clusters
    second = parse_word(second_text).clusters
    if not first or not second:
        return False
    if not _penultimately_stressed(first):
        return False
    if not _final_is_lax_open(first):
        return False
    bound = bound_by_maqaf or bool(_CONJUNCTIVE.search(first_text))
    if not bound:
        return False
    if not _initial_foot_stressed(second):
        return False
    if second[0].letter in _GUTTURAL:
        return False
    if not second[0].dagesh:
        return False
    return True
