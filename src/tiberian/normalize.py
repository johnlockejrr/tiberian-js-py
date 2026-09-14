"""Unicode Masoretic Hebrew normalization.

Working form is **NFD**, not NFC:

- Vowels, dagesh, meteg, rafe, shin/sin dots, and teʿamim stay separate
  code points after the base letter (easy to match individually).
- Hebrew presentation forms (FB1D–FB4F) decompose to letter + marks.
- Canonical combining-class order makes mark sequences deterministic.

Unicode NFD/NFC do **not** fix ḥolem-male encoding. The T1 sources almost
always use ``וֹ`` (VAV then HOLAM). We rewrite:

- ``ֹו`` (HOLAM then VAV) → ``וֹ``
- holam stranded on the previous consonant before a bare vav (``בֹו`` / ``בֹּו``)
  → holam moved onto that vav (``בוֹ`` / ``בּוֹ``)
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

_HEBREW_RE = re.compile(r"[\u0590-\u05FF\uFB1D-\uFB4F]+")
_STRIP = dict.fromkeys(map(ord, "\u200e\u200f\ufeff"))

VAV = "\u05D5"
HOLAM = "\u05B9"
HOLAM_HASER_FOR_VAV = "\u05BA"

# Vowel points (excluding shewa/ḥaṭef handled separately; holam listed for detection)
_VOWEL_POINTS = {
    "\u05B0",  # sheva
    "\u05B1",  # hataf segol
    "\u05B2",  # hataf patah
    "\u05B3",  # hataf qamats
    "\u05B4",  # hiriq
    "\u05B5",  # tsere
    "\u05B6",  # segol
    "\u05B7",  # patah
    "\u05B8",  # qamats
    "\u05B9",  # holam
    "\u05BA",  # holam haser for vav
    "\u05BB",  # qubuts
    "\u05C7",  # qamats qatan
}


@dataclass(frozen=True)
class NormalizedInput:
    original: str
    nfd: str
    working: str
    nfc: str
    fixes_applied: tuple[str, ...]


def _is_hebrew_letter(ch: str) -> bool:
    cp = ord(ch)
    return 0x05D0 <= cp <= 0x05EA


def _split_clusters(text: str) -> list[tuple[str, str]]:
    """Split NFD Hebrew into (base, marks) clusters; non-letters kept as base+''."""
    clusters: list[tuple[str, str]] = []
    i = 0
    chars = list(text)
    while i < len(chars):
        ch = chars[i]
        if _is_hebrew_letter(ch):
            base = ch
            i += 1
            marks: list[str] = []
            while i < len(chars) and not _is_hebrew_letter(chars[i]) and ord(chars[i]) > 0x7F:
                # combining marks / Hebrew points / taamim (not ASCII space etc.)
                cp = ord(chars[i])
                if chars[i] in " \t\r\n־׃׀" or (0x20 <= cp <= 0x7E):
                    break
                marks.append(chars[i])
                i += 1
            clusters.append((base, "".join(marks)))
        else:
            clusters.append((ch, ""))
            i += 1
    return clusters


def _join_clusters(clusters: list[tuple[str, str]]) -> str:
    return "".join(base + marks for base, marks in clusters)


def canonicalize_hebrew_orthography(text: str) -> tuple[str, list[str]]:
    """Hebrew fixes beyond Unicode NFD (ḥolem male, etc.)."""
    fixes: list[str] = []
    out = text

    # 1) Adjacent HOLAM + VAV (no base between) → VAV + HOLAM
    if HOLAM + VAV in out:
        n = out.count(HOLAM + VAV)
        out = out.replace(HOLAM + VAV, VAV + HOLAM)
        fixes.append(f"holam_before_vav→vav_holam×{n}")

    # 2) VAV + HOLAM HASER FOR VAV → VAV + HOLAM
    if VAV + HOLAM_HASER_FOR_VAV in out:
        n = out.count(VAV + HOLAM_HASER_FOR_VAV)
        out = out.replace(VAV + HOLAM_HASER_FOR_VAV, VAV + HOLAM)
        fixes.append(f"holam_haser_for_vav→vav_holam×{n}")

    # 3) Holam on consonant immediately before a vav that has no vowel → move holam to vav
    clusters = _split_clusters(out)
    moved = 0
    for i in range(len(clusters) - 1):
        base, marks = clusters[i]
        nbase, nmarks = clusters[i + 1]
        if not _is_hebrew_letter(base) or nbase != VAV:
            continue
        if HOLAM not in marks and HOLAM_HASER_FOR_VAV not in marks:
            continue
        # If vav already has a full vowel (not just dagesh/shin), skip
        if any(m in _VOWEL_POINTS and m not in {HOLAM, HOLAM_HASER_FOR_VAV} for m in nmarks):
            continue
        if HOLAM in nmarks or HOLAM_HASER_FOR_VAV in nmarks:
            continue
        # Move holam onto vav
        new_marks = marks.replace(HOLAM, "").replace(HOLAM_HASER_FOR_VAV, "")
        clusters[i] = (base, new_marks)
        clusters[i + 1] = (VAV, nmarks + HOLAM)
        moved += 1
    if moved:
        out = _join_clusters(clusters)
        fixes.append(f"holam_on_prev→vav_holam×{moved}")
        out = unicodedata.normalize("NFD", out)

    return out, fixes


def normalize(text: str) -> NormalizedInput:
    """Always Unicode-normalize input to NFD working form + Hebrew fixes."""
    cleaned = text.translate(_STRIP)
    nfd = unicodedata.normalize("NFD", cleaned)
    nfd, fixes = canonicalize_hebrew_orthography(nfd)
    nfd = unicodedata.normalize("NFD", nfd)
    working = re.sub(r"[ \t\r\n]+", " ", nfd).strip()
    nfc = unicodedata.normalize("NFC", working)
    return NormalizedInput(
        original=text,
        nfd=working,
        working=working,
        nfc=nfc,
        fixes_applied=tuple(fixes),
    )


def has_hebrew(text: str) -> bool:
    return bool(_HEBREW_RE.search(text))


def strip_cantillation(text: str) -> str:
    """Remove teʿamim (U+0591–U+05AF); keep vowels, dagesh, meteg, rafe, shin dots."""
    out: list[str] = []
    for ch in text:
        cp = ord(ch)
        if 0x0591 <= cp <= 0x05AF:
            if cp == 0x05BD:  # meteg
                out.append(ch)
            continue
        out.append(ch)
    return "".join(out)


def match_key(text: str, *, keep_cantillation: bool = False) -> str:
    """Normalize for lookup/compare: NFD + fixes, optionally strip teʿamim."""
    norm = normalize(text)
    s = norm.working
    if not keep_cantillation:
        s = strip_cantillation(s)
    s = s.replace("׃", "").replace("׀", "").replace("׳", "").replace("״", "")
    s = s.replace("\\-", "-")
    s = re.sub(r"\s+", " ", s).strip()
    return s
