"""Furtive accent + deḥiq — JS schema and pure-Python path (parity with native)."""

from __future__ import annotations

import pytest

from tiberian.api import transcribe
from tiberian.engine_js import js_engine_status

FURTIVE = "הָרָקִיעַ֒"
FURTIVE_IPA = "hɔːʀ̟ɔːˈq̟iːjaʕ"
OSEH = "עֹ֤שֶׂה פְּרִי֙"
OSEH_IPA = "ˈʕoːsɛˑ ppʰaˈʀ̟iː"
BAM = "וְאָעִ֣ידָה בָּ֔ם"
BAM_IPA = "vɔʔɔːˈʕiːðɔˑ ˈbbɔːɔm"


@pytest.mark.parametrize(
    "heb,ipa",
    [(FURTIVE, FURTIVE_IPA), (OSEH, OSEH_IPA), (BAM, BAM_IPA)],
    ids=["furtive", "dehiq_oseh", "dehiq_bam"],
)
def test_python_furtive_dehiq(heb: str, ipa: str):
    r = transcribe(heb, engine="python")
    assert r.ipa == ipa


@pytest.mark.skipif(
    not js_engine_status()["available"],
    reason="JS Tiberian engine required",
)
@pytest.mark.parametrize(
    "heb,ipa",
    [(FURTIVE, FURTIVE_IPA), (OSEH, OSEH_IPA), (BAM, BAM_IPA)],
    ids=["furtive", "dehiq_oseh", "dehiq_bam"],
)
def test_js_furtive_dehiq(heb: str, ipa: str):
    r = transcribe(heb, engine="js")
    assert r.mode == "js-tiberian"
    assert r.ipa == ipa
