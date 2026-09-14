"""Genesis 1.1–13: JS Tiberian schema vs I.5.4 gold."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tiberian.api import transcribe
from tiberian.engine_js import js_engine_status
from tiberian.profiles import DEFAULT_PROFILE, EXTENDED_FORTE

FIX = Path(__file__).resolve().parent / "fixtures" / "genesis_1_1_13.json"

pytestmark = pytest.mark.skipif(
    not js_engine_status()["available"],
    reason="JS Tiberian engine (node + js/npm deps) required",
)


@pytest.fixture(scope="module")
def verses():
    return json.loads(FIX.read_text(encoding="utf-8"))


def test_genesis_1_1_matches_i54_gold(verses):
    r = transcribe(verses[0]["hebrew"], DEFAULT_PROFILE)
    assert r.mode == "js-tiberian"
    assert r.ipa == verses[0]["forte_lene"]


def test_genesis_rule_engine_runs(verses):
    for row in verses:
        r = transcribe(row["hebrew"], DEFAULT_PROFILE)
        assert r.mode == "js-tiberian", row["verse"]
        assert r.ipa
        assert "[" not in r.ipa and "]" not in r.ipa


def test_genesis_1_1_not_prolonged_by_default(verses):
    r = transcribe(verses[0]["hebrew"], DEFAULT_PROFILE)
    assert not r.ipa.startswith("bba")
    assert r.ipa.startswith("b")


def test_extended_forte_available(verses):
    r = transcribe(verses[0]["hebrew"], EXTENDED_FORTE)
    assert r.mode == "js-tiberian"
    assert r.ipa
