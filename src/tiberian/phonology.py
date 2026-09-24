"""Rule-based Tiberian IPA from Masoretic Hebrew (Khan T1 conventions).

Applies Standard Tiberian rules for any pointed biblical text:
inventory (I.5.1–3), length (I.2.2), closed-syllable epenthesis (I.2.4),
shewa (I.2.5), BGDKPT, gemination streams, resh allophony, word-initial וּ.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from tiberian.orthography import (
    ALEF,
    AYIN,
    BGDKPT,
    HE,
    HET,
    HIRIQ,
    HOLAM,
    PATAH,
    QAMATS,
    QAMATS_QATAN,
    QUBUTS,
    RESH,
    SEGOL,
    SHEVA,
    TSERE,
    VAV,
    YOD,
    Cluster,
    WordOrtho,
    consonant_ipa,
    is_mater,
    parse_word,
    vowel_quality,
)
from tiberian.profiles import Profile
from tiberian.syllables import is_vocalic_shewa, shewa_quality
from tiberian.dehiq import is_dehiq_pair


@dataclass
class WordIPA:
    raw: str
    ipa: str
    unresolved: list[dict] = field(default_factory=list)
    rule_ids: list[str] = field(default_factory=list)


def _geminate(c: Cluster, *, word_initial: bool, stream: str, force_forte: bool = False) -> bool:
    if not c.dagesh:
        return False
    if force_forte and word_initial:
        return True
    if c.letter in BGDKPT:
        if word_initial:
            return stream == "extended_forte"
        return True
    return True


def _pharyngealized_resh(prev: Cluster | None) -> bool:
    if prev is None:
        return False
    if prev.letter in "דזצתטסלן":
        return True
    if prev.letter == "ש" and prev.shin is False:
        return True
    return False


def _is_furtive_host(clusters: list[Cluster], i: int) -> bool:
    """Final ח/ע/הּ + pataḥ after a high/mid vowel (I.2.4) — never stressed."""
    if i != len(clusters) - 1:
        return False
    c = clusters[i]
    if c.vowel != PATAH:
        return False
    if c.letter not in {HET, AYIN, HE}:
        return False
    if c.letter == HE and not c.dagesh:
        return False
    for j in range(i - 1, -1, -1):
        prev = clusters[j]
        if is_mater(prev, clusters[j - 1] if j else None) or (
            prev.letter in {YOD, VAV, HE, ALEF}
            and not prev.vowel
            and not prev.shewa
            and not prev.shureq
            and not prev.hataf
        ):
            continue
        pq = "u" if prev.shureq else vowel_quality(prev)
        return pq in {"u", "o", "i", "e"}
    return False


def _prev_vowel_quality(clusters: list[Cluster], i: int) -> str | None:
    for j in range(i - 1, -1, -1):
        prev = clusters[j]
        if is_mater(prev, clusters[j - 1] if j else None) or (
            prev.letter in {YOD, VAV, HE, ALEF}
            and not prev.vowel
            and not prev.shewa
            and not prev.shureq
            and not prev.hataf
        ):
            continue
        return "u" if prev.shureq else vowel_quality(prev)
    return None


def _stress_index(clusters: list[Cluster]) -> int:
    """Cluster index bearing main stress; furtive pataḥ never stressed."""
    si: int | None = None
    for i, c in enumerate(clusters):
        if c.has_accent:
            si = i
            break
    if si is None:
        for i in range(len(clusters) - 1, -1, -1):
            c = clusters[i]
            if c.shureq or c.hataf or (c.vowel and c.vowel != SHEVA):
                si = i
                break
            if c.shewa and is_vocalic_shewa(c, i, clusters):
                si = i
                break
        if si is None:
            si = max(0, len(clusters) - 1)

    # Accent on a mater / vowelless letter → preceding vocalic cluster.
    c0 = clusters[si]
    if not (c0.shureq or c0.hataf or (c0.vowel and c0.vowel != SHEVA) or (
        c0.shewa and is_vocalic_shewa(c0, si, clusters)
    )):
        for j in range(si - 1, -1, -1):
            c = clusters[j]
            if c.shureq or c.hataf or (c.vowel and c.vowel != SHEVA):
                si = j
                break
            if c.shewa and is_vocalic_shewa(c, j, clusters):
                si = j
                break

    if _is_furtive_host(clusters, si) and si > 0:
        for j in range(si - 1, -1, -1):
            c = clusters[j]
            if c.shureq or c.hataf or (c.vowel and c.vowel != SHEVA):
                return j
            if c.shewa and is_vocalic_shewa(c, j, clusters):
                return j
    return si


def _emit_consonant(
    c: Cluster,
    *,
    after_vowel: bool,
    word_initial: bool,
    prev: Cluster | None,
    profile: Profile,
    rules: list[str],
    force_forte: bool = False,
) -> str:
    if c.letter == RESH:
        if c.dagesh:
            rules.append("TH-CON-RESH-GEM")
            return "ʀ̟ʀ̟"
        if _pharyngealized_resh(prev):
            rules.append("TH-CON-RESH-PHAR")
            return "rˁ"
        rules.append("TH-CON-RESH")
        return "ʀ̟"

    gem = _geminate(
        c, word_initial=word_initial, stream=profile.stream, force_forte=force_forte
    )
    if c.letter == YOD and c.dagesh:
        rules.append("TH-CON-YOD-GEM")
        return "ɟɟ"
    if gem:
        rules.append(
            "TH-DAG-FORTE"
            if not (c.letter in BGDKPT and word_initial and not force_forte)
            else "TH-DAG-EXTENDED-FORTE"
        )
        if force_forte and word_initial:
            rules.append("TH-STR-DEHIQ")
    elif c.letter in BGDKPT and c.dagesh and word_initial:
        rules.append("TH-DAG-LENE")

    return consonant_ipa(c, after_vowel=after_vowel, geminate=gem, stream=profile.stream)


def word_to_ipa(
    word: str,
    profile: Profile,
    *,
    dehiq_host: bool = False,
    dehiq_onset: bool = False,
) -> WordIPA:
    """Transcribe one orthographic word (may include maqqef-internal pieces already split)."""
    raw = word
    w = word.replace("׃", "").replace("׀", "").strip()
    if not w:
        return WordIPA(raw=raw, ipa="")

    ortho = parse_word(w)
    clusters = ortho.clusters
    if not clusters:
        return WordIPA(
            raw=raw,
            ipa="",
            unresolved=[{"span": raw, "reason": "no_consonantal_clusters", "rule_ids": []}],
        )

    stress_ci = _stress_index(clusters)
    parts: list[str] = []
    rules: list[str] = []
    unresolved: list[dict] = []
    after_vowel = False
    prev: Cluster | None = None

    i = 0
    while i < len(clusters):
        c = clusters[i]
        nxt = clusters[i + 1] if i + 1 < len(clusters) else None
        word_initial = i == 0

        # Matres: lengthen previous vowel representation already emitted — skip consonant
        if is_mater(c, prev):
            # Ensure previous vowel is long (mater marks length)
            if parts:
                # find last vowel-ish chunk and ensure ː
                for j in range(len(parts) - 1, -1, -1):
                    p = parts[j]
                    if any(v in p for v in "aeiouɔɛ"):
                        if "ː" not in p and "ˑ" not in p:
                            # insert length before trailing epenthetic duplicate if any
                            parts[j] = p + "ː" if not p.endswith("ː") else p
                        break
            rules.append("TH-ORTH-MATER")
            prev = c
            i += 1
            continue

        # Word-initial shureq וּ → [wu] (I.1.6 / I.5 samples)
        if c.shureq and word_initial:
            stress = i == stress_ci
            body = "wu"
            if c.meteg:
                body = "wuˑ"
                rules.append("TH-STR-METEG")
            if stress and profile.emit_prosody:
                body = "ˈ" + body
            parts.append(body)
            rules.append("TH-CON-SHUREQ-INITIAL")
            after_vowel = True
            prev = c
            i += 1
            continue

        # Silent shewa → coda only (consonant already part of onset of this cluster)
        if c.shewa and not is_vocalic_shewa(c, i, clusters) and not c.hataf:
            # Emit as coda consonant attached after previous vowel (no nucleus)
            cipa = _emit_consonant(
                c, after_vowel=False, word_initial=False, prev=prev, profile=profile, rules=rules
            )
            if cipa.startswith("<"):
                unresolved.append({"span": c.text, "reason": "unsupported_consonant_mapping", "rule_ids": []})
            parts.append(cipa)
            # If previous long closed → may need epenthesis before this coda
            # (handled when we emitted previous nucleus if we knew coda — here retrofit)
            after_vowel = False
            prev = c
            i += 1
            continue

        # Onset consonant (+ vowel nucleus)
        # Special: shureq medial = onset [v] or just [u]? Consonantal vav with shureq is vowel letter.
        if c.shureq:
            # medial/final shureq as vowel [uː] under length rules
            q = "u"
            stressed = i == stress_ci
            secondary = c.meteg and not stressed
            cipa = ""  # no separate onset
        else:
            cipa = _emit_consonant(
                c,
                after_vowel=after_vowel,
                word_initial=word_initial,
                prev=prev,
                profile=profile,
                rules=rules,
                force_forte=dehiq_onset and word_initial,
            )
            if cipa.startswith("<"):
                unresolved.append({"span": c.text, "reason": "unsupported_consonant_mapping", "rule_ids": []})

            if c.hataf or (c.shewa and is_vocalic_shewa(c, i, clusters)):
                q = shewa_quality(c, nxt) or "a"
                rules.append("TH-SHEWA" if c.shewa else "TH-HATEF")
                stressed = i == stress_ci
                secondary = False
            elif c.vowel:
                q = vowel_quality(c)
                if q is None:
                    q = "a"
                    unresolved.append({"span": c.text, "reason": "unknown_vowel", "rule_ids": []})
                stressed = i == stress_ci
                secondary = c.meteg and not stressed
            else:
                # vowelless non-mater consonant: onset waiting — emit C only
                parts.append(cipa)
                after_vowel = False
                prev = c
                i += 1
                continue

        # Determine coda: next silent-shewa cluster OR next vowelless non-mater before another vowel
        coda: Cluster | None = None
        coda_idx = None
        if nxt and nxt.shewa and not is_vocalic_shewa(nxt, i + 1, clusters) and not nxt.hataf:
            coda = nxt
            coda_idx = i + 1
        elif nxt and not nxt.vowel and not nxt.shewa and not nxt.hataf and not nxt.shureq and not is_mater(nxt, c):
            # single coda consonant (e.g. final C)
            # only if nothing after or after is mater/end
            nxt2 = clusters[i + 2] if i + 2 < len(clusters) else None
            if nxt2 is None or is_mater(nxt2, nxt) or (
                nxt2.shewa and not is_vocalic_shewa(nxt2, i + 2, clusters)
            ):
                coda = nxt
                coda_idx = i + 1

        # Furtive pataḥ: final guttural with pataḥ after high/mid vowel
        furtive = _is_furtive_host(clusters, i)
        closed = coda is not None and not furtive
        always_long = q in {"e", "o"}  # ṣere / ḥolem (I.2.2.4)
        # Length (I.2.2): long if stressed OR open unstressed; short if closed unstressed
        # Deḥiq: final unstressed qameṣ/segol → half-long (§I.2.8.1.2),
        # including when a quiet mater he follows.
        is_last_vocalic = True
        for k in range(i + 1, len(clusters)):
            ck = clusters[k]
            if ck.shureq or ck.hataf or (ck.vowel and ck.vowel != SHEVA):
                is_last_vocalic = False
                break
            if ck.shewa and is_vocalic_shewa(ck, k, clusters):
                is_last_vocalic = False
                break
        dehiq_half = (
            dehiq_host
            and is_last_vocalic
            and not stressed
            and not closed
            and c.vowel in {QAMATS, QAMATS_QATAN, SEGOL}
        )
        if c.hataf or (c.shewa and not c.hataf):
            long = False  # shewa/ḥaṭef short
        elif dehiq_half:
            long = False
        elif always_long:
            long = True
        elif stressed:
            long = True
        elif not closed:
            long = True
        else:
            long = False

        if secondary:
            # minor gaʿya / meteg: half-long (I.2.8)
            nuc = q + "ˑ"
            rules.append("TH-STR-METEG")
        elif dehiq_half:
            nuc = q + "ˑ"
            rules.append("TH-STR-DEHIQ")
        elif long:
            nuc = q + "ː"
            rules.append("TH-LEN-LONG")
        else:
            nuc = q
            rules.append("TH-LEN-SHORT")

        # Closed + long (+ stress): epenthetic copy (I.2.4) — ˈCVːVC
        if closed and long and not (c.hataf or c.shewa):
            nuc = nuc + q
            rules.append("TH-LEN-EPENTHESIS")

        if furtive:
            # emit onset of previous already done; this cluster is guttural with pataḥ
            pq = _prev_vowel_quality(clusters, i) or ""
            glide = "w" if pq in {"u", "o"} else ("j" if pq in {"i", "e"} else "")
            parts.append(glide + "a")
            parts.append(
                _emit_consonant(
                    c, after_vowel=False, word_initial=False, prev=prev, profile=profile, rules=rules
                )
            )
            rules.append("TH-LEN-FURTIVE")
            after_vowel = False
            prev = c
            i += 1
            continue

        # Assemble: (stress mark before syllable) + onset C + nucleus
        if profile.emit_prosody and stressed:
            chunk = "ˈ" + cipa + nuc
        elif profile.emit_prosody and secondary:
            chunk = "ˌ" + cipa + nuc
        else:
            chunk = cipa + nuc

        parts.append(chunk)

        if coda is not None and coda_idx is not None:
            c_ipa = _emit_consonant(
                coda,
                after_vowel=False,
                word_initial=False,
                prev=c,
                profile=profile,
                rules=rules,
            )
            parts.append(c_ipa)
            after_vowel = False
            prev = coda
            i = coda_idx + 1
            continue

        after_vowel = True
        prev = c
        i += 1

    return WordIPA(raw=raw, ipa="".join(parts), unresolved=unresolved, rule_ids=rules)


def phrase_to_ipa(text: str, profile: Profile) -> tuple[str, list[WordIPA], list[dict]]:
    tokens = re.split(r"(\s+|־)", text)
    # Collect Hebrew word tokens with maqqaf-binding flags for deḥiq.
    words: list[tuple[str, bool]] = []  # (token, bound_to_next_by_maqaf)
    i = 0
    raw_tokens = [t for t in tokens if t]
    while i < len(raw_tokens):
        tok = raw_tokens[i]
        if tok.isspace() or tok == "־":
            i += 1
            continue
        bound = False
        # maqqaf immediately after this word
        if i + 1 < len(raw_tokens) and raw_tokens[i + 1] == "־":
            bound = True
        words.append((tok, bound))
        i += 1

    word_results: list[WordIPA] = []
    pieces: list[str] = []
    unresolved: list[dict] = []

    # Rebuild with spaces/maqafs, applying deḥiq pair flags.
    heb_idx = 0
    for tok in raw_tokens:
        if tok.isspace():
            pieces.append(" ")
            continue
        if tok == "־":
            pieces.append("-")
            continue
        host = False
        onset = False
        if heb_idx < len(words):
            cur, bound = words[heb_idx]
            if heb_idx + 1 < len(words):
                nxt, _ = words[heb_idx + 1]
                if is_dehiq_pair(cur, nxt, bound_by_maqaf=bound):
                    host = True
                    # mark next word's onset when we get there
            if heb_idx > 0:
                prev, prev_bound = words[heb_idx - 1]
                if is_dehiq_pair(prev, cur, bound_by_maqaf=prev_bound):
                    onset = True
            wr = word_to_ipa(tok, profile, dehiq_host=host, dehiq_onset=onset)
            word_results.append(wr)
            pieces.append(wr.ipa)
            unresolved.extend(wr.unresolved)
            heb_idx += 1
    return "".join(pieces), word_results, unresolved
