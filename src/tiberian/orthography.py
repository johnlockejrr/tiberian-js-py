"""Orthographic analysis: letters, niqqud, dagesh, shin/sin, matres, accents."""

from __future__ import annotations

from dataclasses import dataclass, field

ALEF, BET, GIMEL, DALET, HE, VAV, ZAYIN, HET, TET, YOD = (
    "א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י",
)
KAF, FINAL_KAF, LAMED, MEM, FINAL_MEM, NUN, FINAL_NUN = "כ", "ך", "ל", "מ", "ם", "נ", "ן"
SAMEKH, AYIN, PE, FINAL_PE, TSADI, FINAL_TSADI = "ס", "ע", "פ", "ף", "צ", "ץ"
QOF, RESH, SHIN, TAV = "ק", "ר", "ש", "ת"

SHEVA = "\u05B0"
HATAF_SEGOL = "\u05B1"
HATAF_PATAH = "\u05B2"
HATAF_QAMATS = "\u05B3"
HIRIQ = "\u05B4"
TSERE = "\u05B5"
SEGOL = "\u05B6"
PATAH = "\u05B7"
QAMATS = "\u05B8"
HOLAM = "\u05B9"
HOLAM_HASER = "\u05BA"
QUBUTS = "\u05BB"
DAGESH = "\u05BC"
METEG = "\u05BD"
RAFE = "\u05BF"
SHIN_DOT = "\u05C1"
SIN_DOT = "\u05C2"
QAMATS_QATAN = "\u05C7"

VOWELS = {
    SHEVA, HATAF_SEGOL, HATAF_PATAH, HATAF_QAMATS,
    HIRIQ, TSERE, SEGOL, PATAH, QAMATS, HOLAM, HOLAM_HASER, QUBUTS, QAMATS_QATAN,
}

BGDKPT = {BET, GIMEL, DALET, KAF, FINAL_KAF, PE, FINAL_PE, TAV}

STOP_IPA = {
    BET: "b", GIMEL: "g", DALET: "d", KAF: "kʰ", FINAL_KAF: "kʰ",
    PE: "pʰ", FINAL_PE: "pʰ", TAV: "tʰ",
}
FRIC_IPA = {
    BET: "v", GIMEL: "ʁ", DALET: "ð", KAF: "χ", FINAL_KAF: "χ",
    PE: "f", FINAL_PE: "f", TAV: "θ",
}
CONS_IPA = {
    ALEF: "ʔ", HE: "h", VAV: "v", ZAYIN: "z", HET: "ħ", TET: "tˁ", YOD: "j",
    LAMED: "l", MEM: "m", FINAL_MEM: "m", NUN: "n", FINAL_NUN: "n", SAMEKH: "s",
    AYIN: "ʕ", TSADI: "sˁ", FINAL_TSADI: "sˁ", QOF: "q̟", RESH: "ʀ̟", TAV: "tʰ",
}
VOWEL_IPA = {
    PATAH: "a", QAMATS: "ɔ", QAMATS_QATAN: "ɔ", SEGOL: "ɛ", TSERE: "e",
    HIRIQ: "i", HOLAM: "o", HOLAM_HASER: "o", QUBUTS: "u",
    HATAF_PATAH: "a", HATAF_SEGOL: "ɛ", HATAF_QAMATS: "ɔ",
}


@dataclass
class Cluster:
    letter: str
    marks: str = ""
    dagesh: bool = False
    rafe: bool = False
    shin: bool | None = None
    vowel: str | None = None
    shewa: bool = False
    hataf: str | None = None
    meteg: bool = False
    shureq: bool = False
    has_accent: bool = False  # any teʿam except meteg
    accent_chars: str = ""

    @property
    def text(self) -> str:
        return self.letter + self.marks


@dataclass
class WordOrtho:
    raw: str
    clusters: list[Cluster] = field(default_factory=list)


def parse_word(word: str) -> WordOrtho:
    clusters: list[Cluster] = []
    i = 0
    chars = list(word)
    while i < len(chars):
        ch = chars[i]
        if not ("\u05D0" <= ch <= "\u05EA"):
            i += 1
            continue
        c = Cluster(letter=ch)
        i += 1
        marks: list[str] = []
        accents: list[str] = []
        while i < len(chars):
            m = chars[i]
            if "\u05D0" <= m <= "\u05EA":
                break
            cp = ord(m)
            if m == DAGESH:
                c.dagesh = True
            elif m == RAFE:
                c.rafe = True
            elif m == SHIN_DOT:
                c.shin = True
            elif m == SIN_DOT:
                c.shin = False
            elif m == METEG:
                c.meteg = True
            elif 0x0591 <= cp <= 0x05AF:
                c.has_accent = True
                accents.append(m)
            elif m == SHEVA:
                c.shewa = True
                c.vowel = SHEVA
            elif m in {HATAF_PATAH, HATAF_SEGOL, HATAF_QAMATS}:
                c.hataf = m
                c.vowel = m
            elif m in VOWELS:
                c.vowel = m
            marks.append(m)
            i += 1
        c.marks = "".join(marks)
        c.accent_chars = "".join(accents)
        if c.letter == VAV and c.dagesh and c.vowel is None and not c.shewa:
            c.shureq = True
            c.vowel = "SHUREQ"
        clusters.append(c)
    return WordOrtho(raw=word, clusters=clusters)


def is_mater(c: Cluster, prev: Cluster | None) -> bool:
    """Matres lectionis: vowelless yod/vav/he (final) after a vowel."""
    if c.vowel or c.shewa or c.hataf or c.shureq:
        return False
    if prev is None:
        return False
    if c.letter == YOD and prev.vowel in {HIRIQ, TSERE, SEGOL}:
        return True
    if c.letter == VAV and prev.vowel in {HOLAM, HOLAM_HASER, QUBUTS}:
        return True
    if c.letter == HE and not c.dagesh:  # no mappiq
        return True
    if c.letter == ALEF and not c.dagesh:
        # often quiescent between vowels / word-final
        return True
    return False


def consonant_ipa(c: Cluster, *, after_vowel: bool, geminate: bool, stream: str) -> str:
    L = c.letter
    if L == SHIN:
        base = "s" if c.shin is False else "ʃ"
        return base + base if geminate else base
    if L in BGDKPT:
        if c.rafe:
            base = FRIC_IPA[L]
        elif c.dagesh:
            base = STOP_IPA[L]
            if geminate:
                return (base[0] + base) if base.endswith("ʰ") else base + base
            return base
        elif after_vowel:
            base = FRIC_IPA[L]
        else:
            base = STOP_IPA[L]
        return base
    if L == YOD:
        return "ɟɟ" if c.dagesh else "j"
    if L == VAV:
        return "v"
    if L == ALEF:
        return "ʔ"
    if L in CONS_IPA:
        base = CONS_IPA[L]
        return base + base if (geminate and c.dagesh) else base
    return f"<{L}>"


def vowel_quality(c: Cluster) -> str | None:
    if c.shureq:
        return "u"
    if c.vowel == SHEVA:
        return None
    if c.vowel in VOWEL_IPA:
        return VOWEL_IPA[c.vowel]
    return None
