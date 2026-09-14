"""Corpus / inventory unit checks."""

from __future__ import annotations

from tiberian.api import transcribe
from tiberian.corpus_loader import iter_rules, load_corpus
from tiberian.emit import bare_ipa
from tiberian.inventory import consonant_inventory, vowel_inventory
from tiberian.orthography import BET, parse_word, consonant_ipa
from tiberian.cli import main


def test_corpus_loads():
    assert len(load_corpus()["rules"]) >= 400


def test_inventory_bet():
    w = parse_word("בּ")
    assert consonant_ipa(w.clusters[0], after_vowel=False, geminate=False, stream="forte_lene") == "b"


def test_all_source_ipa_bare():
    n = 0
    for rule in iter_rules():
        for ex in rule.get("examples") or []:
            if ex.get("source_ipa"):
                n += 1
                assert "[" not in bare_ipa(ex["source_ipa"])
    assert n >= 200


def test_i5_inventory_loads():
    assert len(consonant_inventory()) >= 10
    assert len(vowel_inventory()) >= 5


def test_cli_runs(capsys):
    code = main(["שָׁלוֹם"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out
    assert "[" not in out
    assert out == "ʃɔːˈloːom"


def test_transcribe_simple_word():
    r = transcribe("שָׁלוֹם")
    assert r.mode in ("js-tiberian", "rules-python", "rules-python-partial")
    assert r.ipa
    if r.mode == "js-tiberian":
        assert r.ipa == "ʃɔːˈloːom"
