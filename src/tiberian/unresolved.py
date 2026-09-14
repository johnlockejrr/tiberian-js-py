"""Unresolved / fail-closed reporting."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class UnresolvedSpan:
    span: str
    reason: str
    rule_ids: list[str] = field(default_factory=list)
    message: str = ""

    def to_dict(self) -> dict:
        return {
            "span": self.span,
            "reason": self.reason,
            "rule_ids": self.rule_ids,
            "message": self.message
            or (
                "No source-supported IPA without invention; "
                "refusing Modern Hebrew / comparative fallback."
            ),
        }


FORBIDDEN_FALLBACKS = (
    "modern hebrew",
    "israeli",
    "babylonian",
    "palestinian",
    "guess",
)
