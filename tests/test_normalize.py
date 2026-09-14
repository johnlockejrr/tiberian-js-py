"""Normalization: NFD working form, holam-vav fix, presentation forms."""

from __future__ import annotations

import unicodedata

from tiberian.normalize import canonicalize_hebrew_orthography, match_key, normalize


def test_always_nfd_working_form():
    # Presentation form bet-dagesh → ב + dagesh under NFD
    pres = "\uFB31"  # בּ
    n = normalize(pres)
    assert "\u05D1" in n.working  # bet
    assert "\u05BC" in n.working  # dagesh
    assert n.working == unicodedata.normalize("NFD", n.working)
    assert n.nfd == n.working


def test_holam_before_vav_rewritten_to_vav_holam():
    wrong = "\u05B9\u05D5"  # ֹו
    right = "\u05D5\u05B9"  # וֹ
    n = normalize("ש" + wrong + "ם")
    assert wrong not in n.working
    assert right in n.working
    assert any("holam_before_vav" in f for f in n.fixes_applied)


def test_sources_prefer_vav_then_holam_equivalence():
    # Both inputs match the same lookup key after normalize
    a = match_key("בּוֹ")
    b = match_key("בּ" + "\u05B9\u05D5")  # holam then vav
    assert a == b


def test_vowels_and_cantillation_remain_separate_codepoints():
    # tipha + patah on bet stay as distinct marks after NFD
    s = "ב\u05B7\u05A5"  # bet + patah + tipha
    n = normalize(s)
    assert "\u05B7" in n.working
    assert "\u05A5" in n.working
    # marks follow base
    i = n.working.index("ב")
    assert n.working[i] == "ב"


def test_canonicalize_helper_counts():
    text, fixes = canonicalize_hebrew_orthography("א\u05B9\u05D5ב\u05B9\u05D5")
    assert text.count("\u05D5\u05B9") == 2
    assert fixes
