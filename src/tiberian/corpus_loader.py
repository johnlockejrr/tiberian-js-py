"""Load and query the Phase-1 rules corpus."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterator


def _candidate_paths() -> list[Path]:
    here = Path(__file__).resolve().parent
    return [
        here / "data" / "corpus" / "tiberian_rules.json",
        here.parents[2] / "corpus" / "tiberian_rules.json",
        Path.cwd() / "corpus" / "tiberian_rules.json",
    ]


@lru_cache(maxsize=1)
def corpus_path() -> Path:
    for p in _candidate_paths():
        if p.is_file():
            return p
    raise FileNotFoundError(
        "tiberian_rules.json not found. Expected under corpus/ or package data."
    )


@lru_cache(maxsize=1)
def load_corpus() -> dict[str, Any]:
    return json.loads(corpus_path().read_text(encoding="utf-8"))


def iter_rules(
    *,
    status: str | None = None,
    authority: str | None = None,
    category_substr: str | None = None,
    id_prefix: str | None = None,
) -> Iterator[dict[str, Any]]:
    for rule in load_corpus()["rules"]:
        if status and rule["status"] != status:
            continue
        if authority and rule["authority"] != authority:
            continue
        if category_substr and category_substr.lower() not in rule["category"].lower():
            continue
        if id_prefix and not rule["id"].startswith(id_prefix):
            continue
        yield rule


def rules_by_id() -> dict[str, dict[str, Any]]:
    return {r["id"]: r for r in load_corpus()["rules"]}


def sample_rules() -> list[dict[str, Any]]:
    return [
        r
        for r in load_corpus()["rules"]
        if r["id"].startswith("TH-ORTH-SAMPLE-")
    ]
