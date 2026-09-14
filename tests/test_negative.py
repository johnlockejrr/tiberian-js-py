"""Fail-closed + default stream behaviour."""

from __future__ import annotations

import json
from pathlib import Path

from tiberian.api import transcribe


def test_empty_latin_unresolved():
    r = transcribe("hello")
    assert r.ipa is None
    assert r.unresolved[0]["reason"] == "no_hebrew_characters"


def test_arbitrary_verse_uses_rules_not_sample_lookup():
    """Any biblical verse must go through the Tiberian rule engine (not sample lookup)."""
    text = "מִֽי־פָקַ֣ד עָלָ֣יו אָ֑רְצָה וּמִ֥י שָׂ֝֗ם תֵּבֵ֥ל כֻּלָּֽהּ׃"
    r = transcribe(text)
    assert r.mode in ("js-tiberian", "rules-python", "rules-python-partial")
    assert "sample" not in r.mode
    assert r.ipa
    assert "[" not in r.ipa
    # Closed stressed syllable epenthesis (Khan §I.2.4 / tiberian.ts Full Vowel)
    assert "q̟aːað" in r.ipa or "q̟aːad" in r.ipa
    assert "kʰulˈlɔːɔh" in r.ipa or "ˈllɔː" in r.ipa
    # No residual doubled he from broken pure-Python path
    assert "hh" not in r.ipa


def test_default_not_prolonged_stream():
    row = json.loads(
        (Path(__file__).parent / "fixtures" / "genesis_1_1_13.json").read_text(
            encoding="utf-8"
        )
    )[0]
    r = transcribe(row["hebrew"])
    assert not r.ipa.startswith("bbaʀ̟")
