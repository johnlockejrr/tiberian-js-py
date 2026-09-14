"""Qere/Ketiv resolution from corpus-documented defaults."""

from __future__ import annotations

import re
from dataclasses import dataclass

# Documented regular substitutions (T1_0 §I.0.5) — reading forms.
# Tetragrammaton reading depends on context; default Adonai.
_YHWH = "יהוה"
_ADONAI = "אֲדֹנָי"
_ELOHIM = "אֱלֹהִים"

# Jerusalem ketiv without yod → qere with yod (simplified orthographic target)
_JERUSALEM_KETIV = re.compile(r"ירושלם")
_JERUSALEM_QERE = "יְרוּשָׁלִַם"


@dataclass
class QereResult:
    text: str
    substitutions: list[dict]


def resolve_qere(text: str, *, yhwh_as: str = "adonai") -> QereResult:
    """Apply regular qere substitutions documented in the sources.

    Does not invent margin-note qere; unresolved named ketiv/qere pairs
    should be reported by the caller when required data is missing.
    """
    subs: list[dict] = []
    out = text

    replacement = _ADONAI if yhwh_as == "adonai" else _ELOHIM
    if _YHWH in out:
        count = out.count(_YHWH)
        out = out.replace(_YHWH, replacement)
        subs.append(
            {
                "type": "tetragrammaton",
                "from": _YHWH,
                "to": replacement,
                "count": count,
                "rule_hint": "TH-QK (T1_0 §I.0.5)",
            }
        )

    if _JERUSALEM_KETIV.search(out):
        out2 = _JERUSALEM_KETIV.sub(_JERUSALEM_QERE, out)
        if out2 != out:
            subs.append(
                {
                    "type": "jerusalem",
                    "from": "ירושלם",
                    "to": _JERUSALEM_QERE,
                    "rule_hint": "TH-QK Jerusalem qere",
                }
            )
            out = out2

    return QereResult(text=out, substitutions=subs)
