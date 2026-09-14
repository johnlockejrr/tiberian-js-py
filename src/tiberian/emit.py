"""IPA emission helpers — bare transcription only (no book-style [brackets])."""

from __future__ import annotations


def bare_ipa(ipa: str | None) -> str | None:
    """Strip editorial [ ] wrappers; return transcription only."""
    if ipa is None:
        return None
    out = str(ipa).strip().replace("\\-", "-")
    if out.startswith("[") and out.endswith("]"):
        out = out[1:-1].strip()
    out = out.replace("[", "").replace("]", "")
    return out.strip() or None


def join_words(parts: list[str]) -> str:
    return " ".join(p for p in parts if p)
