"""Regression: user verse + shalom against Tiberian schema reference."""

from __future__ import annotations

import pytest

from tiberian.api import transcribe
from tiberian.engine_js import js_engine_status

pytestmark = pytest.mark.skipif(
    not js_engine_status()["available"],
    reason="JS Tiberian engine (node + js/npm deps) required",
)

USER_VERSE = "מִֽי־פָקַ֣ד עָלָ֣יו אָ֑רְצָה וּמִ֥י שָׂ֝֗ם תֵּבֵ֥ל כֻּלָּֽהּ׃"
# hebrew-transliteration Tiberian schema (docs/tiberian.ts rule set)
USER_IPA = "ˌmiˑ-ppʰɔːˈq̟aːað ʕɔːˈlɔːɔw ˈʔɔːɔʀ̟sˁɔː wuˈmiː ˈsɔːɔm tʰeːˈveːel kʰulˈlɔːɔh"


def test_user_verse_tiberian_schema():
    r = transcribe(USER_VERSE)
    assert r.mode == "js-tiberian"
    assert r.ipa == USER_IPA
    # Must not regress to the broken pure-Python output
    assert "ˈmiː-pʰɔːˈq̟aːad" not in (r.ipa or "")
    assert "hh" not in (r.ipa or "")


def test_shalom():
    r = transcribe("שָׁלוֹם")
    assert r.ipa == "ʃɔːˈloːom"


def test_elohim():
    r = transcribe("אֱלֹהִים")
    assert r.ipa == "ʔɛloːˈhiːim"
