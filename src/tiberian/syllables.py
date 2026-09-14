"""Shewa classification and lightweight syllabification."""

from __future__ import annotations

from dataclasses import dataclass

from tiberian.orthography import (
    AYIN,
    ALEF,
    HE,
    HET,
    YOD,
    Cluster,
    WordOrtho,
    vowel_quality,
)

GUTTURAL_ONSET = {ALEF, HE, HET, AYIN}


@dataclass
class Syllable:
    onset: list[Cluster]
    nucleus: str  # IPA quality without length
    coda: list[Cluster]
    stressed: bool = False
    secondary: bool = False
    closed: bool = False
    shewa_vocalic: bool = False


def shewa_quality(cluster: Cluster, following: Cluster | None) -> str | None:
    """Vocalic shewa quality (I.2.5 / I.5.3): default [a]; before guttural copy; before yod [i]."""
    if not cluster.shewa and not cluster.hataf:
        return None
    if cluster.hataf:
        from tiberian.orthography import VOWEL_IPA

        return VOWEL_IPA.get(cluster.hataf, "a")
    if following is None:
        return "a"
    if following.letter == YOD:
        return "i"
    if following.letter in GUTTURAL_ONSET:
        q = vowel_quality(following)
        return q if q else "a"
    return "a"


def is_vocalic_shewa(cluster: Cluster, index: int, clusters: list[Cluster]) -> bool:
    """Heuristic vocalic vs silent shewa — fail soft toward corpus rules; uncertain → vocalic at word start."""
    if cluster.hataf:
        return True
    if not cluster.shewa:
        return False
    # Word-initial shewa is vocalic (except documented שְׁתַּיִם-type — flagged elsewhere)
    if index == 0:
        return True
    prev = clusters[index - 1]
    # After dagesh (forte) on same? shewa on geminated consonant is vocalic
    if cluster.dagesh:
        return True
    # Silent after long vowel environments need full analysis — default silent word-internally
    # if previous had a full vowel and no meteg
    if prev.vowel and prev.vowel != "\u05B0" and not prev.hataf and not prev.meteg:
        # I.2.5.6 general: after long vowel word-internally, shewa silent — we don't know length yet
        # Prefer silent unless following identical consonant
        nxt = clusters[index + 1] if index + 1 < len(clusters) else None
        if nxt and nxt.letter == cluster.letter:
            return True
        if cluster.letter in GUTTURAL_ONSET:
            return True
        return False
    return True


def build_syllables(word: WordOrtho) -> list[Syllable]:
    """Approximate CV syllabification for generative IPA (not full Khan metrical theory)."""
    clusters = word.clusters
    syllables: list[Syllable] = []
    i = 0
    while i < len(clusters):
        c = clusters[i]
        onset = [c]
        nucleus = None
        shewa_voc = False
        nxt = clusters[i + 1] if i + 1 < len(clusters) else None

        if c.shureq:
            nucleus = "u"
            i += 1
        elif c.hataf:
            nucleus = shewa_quality(c, nxt)
            shewa_voc = True
            i += 1
        elif c.shewa:
            if is_vocalic_shewa(c, i, clusters):
                nucleus = shewa_quality(c, nxt)
                shewa_voc = True
                i += 1
            else:
                # silent shewa: attach as coda to previous syllable if any
                if syllables:
                    syllables[-1].coda.append(c)
                    syllables[-1].closed = True
                i += 1
                continue
        elif c.vowel:
            nucleus = vowel_quality(c)
            i += 1
        else:
            # mater / vowelless — may be coda
            if syllables:
                syllables[-1].coda.append(c)
                syllables[-1].closed = True
            else:
                # prosthetic onset waiting for vowel
                pass
            i += 1
            if nucleus is None and not syllables:
                continue
            if nucleus is None:
                continue

        # Collect coda: following consonant without vowel before next nucleus
        coda: list[Cluster] = []
        while i < len(clusters):
            n = clusters[i]
            if n.vowel or n.shewa or n.hataf or n.shureq:
                break
            coda.append(n)
            i += 1
            break  # one coda consonant typical

        if nucleus is None:
            nucleus = "a"  # should be unresolved in stricter mode
        syl = Syllable(
            onset=onset,
            nucleus=nucleus,
            coda=coda,
            closed=bool(coda),
            shewa_vocalic=shewa_voc,
        )
        syllables.append(syl)
    return syllables
