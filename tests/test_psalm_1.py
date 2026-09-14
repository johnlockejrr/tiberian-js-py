"""Psalm 1: JS Tiberian engine path."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tiberian.api import transcribe
from tiberian.engine_js import js_engine_status
from tiberian.profiles import DEFAULT_PROFILE

FIX = Path(__file__).resolve().parent / "fixtures" / "psalm_1.json"

pytestmark = pytest.mark.skipif(
    not js_engine_status()["available"],
    reason="JS Tiberian engine (node + js/npm deps) required",
)


def test_psalm_rule_engine_runs():
    verses = json.loads(FIX.read_text(encoding="utf-8"))
    assert len(verses) == 6
    for row in verses:
        r = transcribe(row["hebrew"], DEFAULT_PROFILE)
        assert r.mode == "js-tiberian"
        assert r.ipa
        assert "[" not in r.ipa
