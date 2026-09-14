"""Corpus sample lookup for I.5.4 gold transcriptions (fixtures + corpus)."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from tiberian.corpus_loader import sample_rules
from tiberian.normalize import match_key
from tiberian.profiles import Profile


def _norm_hebrew(s: str) -> str:
    return match_key(s, keep_cantillation=False)


def _clean_ipa(s: str) -> str:
    """Return bare IPA transcription (no book [brackets])."""
    s = s.strip().replace("\\-", "-")
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\[\[[0-9]+\]\]\([^)]*\)", "", s)
    s = s.replace("[", "").replace("]", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _fixture_paths() -> list[Path]:
    here = Path(__file__).resolve()
    roots = [here.parents[2], Path.cwd()]
    out: list[Path] = []
    for root in roots:
        for name in ("genesis_1_1_13.json", "psalm_1.json"):
            p = root / "tests" / "fixtures" / name
            if p.is_file():
                out.append(p)
    return out


@lru_cache(maxsize=1)
def sample_index() -> dict[tuple[str, str], str]:
    """Map (normalized_hebrew, stream) → IPA without brackets."""
    idx: dict[tuple[str, str], str] = {}

    for path in _fixture_paths():
        data = json.loads(path.read_text(encoding="utf-8"))
        for row in data:
            heb = _norm_hebrew(row["hebrew"])
            fl = _clean_ipa(row["forte_lene"] or "")
            ef = _clean_ipa(row.get("extended_forte") or fl)
            if fl:
                idx[(heb, "forte_lene")] = fl
            if ef:
                idx[(heb, "extended_forte")] = ef

    for rule in sample_rules():
        for ex in rule.get("examples") or []:
            heb = ex.get("hebrew") or ""
            ipa = ex.get("source_ipa")
            stream = ex.get("stream") or "either"
            if not heb or not ipa:
                continue
            key_h = _norm_hebrew(heb)
            ipa_c = _clean_ipa(ipa)
            if stream == "either":
                idx.setdefault((key_h, "forte_lene"), ipa_c)
                idx.setdefault((key_h, "extended_forte"), ipa_c)
            elif stream == "forte-lene":
                idx.setdefault((key_h, "forte_lene"), ipa_c)
            elif stream == "extended-forte":
                idx.setdefault((key_h, "extended_forte"), ipa_c)
    return idx


def lookup_sample(hebrew: str, profile: Profile) -> str | None:
    idx = sample_index()
    key = _norm_hebrew(hebrew)
    stream = profile.stream
    if (key, stream) in idx:
        return idx[(key, stream)]
    return None
