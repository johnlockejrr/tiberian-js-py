"""Load hierarchical rule-application pipeline (not alphabetical rule IDs)."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path


def _paths() -> list[Path]:
    here = Path(__file__).resolve().parent
    return [
        here.parents[2] / "corpus" / "rule_pipeline.json",
        Path.cwd() / "corpus" / "rule_pipeline.json",
        here / "data" / "corpus" / "rule_pipeline.json",
    ]


@lru_cache(maxsize=1)
def load_pipeline() -> dict:
    for p in _paths():
        if p.is_file():
            return json.loads(p.read_text(encoding="utf-8"))
    return {
        "version": "0",
        "unicode_working_form": "NFD",
        "default_stream": "forte_lene",
        "stages": [],
    }


def stage_ids() -> list[str]:
    return [s["id"] for s in load_pipeline().get("stages", [])]
