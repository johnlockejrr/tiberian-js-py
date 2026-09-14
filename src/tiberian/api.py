"""Public API: Tiberian IPA for any Masoretic Hebrew text.

Default engine: Node ``hebrew-transliteration`` with the Tiberian schema
(same rule set as ``docs/tiberian.ts``: length, epenthesis, shewa, digraph
gemination, furtive pataḥ, etc., on top of havarotjs syllabification).

Optional ``engine="python"`` uses the incomplete pure-Python path (dev only).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

from tiberian.emit import bare_ipa
from tiberian.engine_js import JsEngineError, js_engine_status, transliterate_js
from tiberian.normalize import has_hebrew, normalize
from tiberian.phonology import phrase_to_ipa
from tiberian.pipeline import load_pipeline
from tiberian.profiles import Profile, resolve_profile
from tiberian.qere import resolve_qere
from tiberian.unresolved import UnresolvedSpan

TranscribeProfile = Profile
EngineName = Literal["js", "python", "auto"]


@dataclass
class Result:
    input: str
    reading: str
    ipa: str | None
    provenance: list[dict[str, Any]] = field(default_factory=list)
    unresolved: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    profile: str = ""
    mode: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "input": self.input,
            "reading": self.reading,
            "ipa": self.ipa,
            "provenance": self.provenance,
            "unresolved": self.unresolved,
            "warnings": self.warnings,
            "profile": self.profile,
            "mode": self.mode,
        }


def _empty_result(
    text: str,
    *,
    reading: str,
    prof: Profile,
    unresolved: list[dict[str, Any]],
    provenance: list[dict[str, Any]],
    warnings: list[str],
    mode: str,
) -> Result:
    return Result(
        input=text,
        reading=reading,
        ipa=None,
        provenance=provenance,
        unresolved=unresolved,
        warnings=warnings,
        profile=prof.name,
        mode=mode,
    )


def transcribe(
    text: str,
    profile: str | Profile | None = None,
    *,
    yhwh_as: str = "adonai",
    engine: EngineName = "js",
) -> Result:
    """Transcribe pointed Biblical Hebrew to Tiberian IPA.

    Default ``engine="js"`` runs the Tiberian schema from
    ``hebrew-transliteration`` (aligned with ``docs/tiberian.ts`` / Khan TPT).
    """
    prof = resolve_profile(profile)
    norm = normalize(text)
    warnings: list[str] = []
    provenance: list[dict[str, Any]] = [
        {
            "stage": "normalize",
            "form": "NFD",
            "fixes_applied": list(norm.fixes_applied),
            "pipeline": [s["id"] for s in load_pipeline().get("stages", [])],
        }
    ]
    unresolved: list[dict[str, Any]] = []

    if not has_hebrew(norm.working):
        unresolved.append(
            UnresolvedSpan(
                span=text,
                reason="no_hebrew_characters",
                message="Input contains no Hebrew characters.",
            ).to_dict()
        )
        return _empty_result(
            text,
            reading=norm.working,
            prof=prof,
            unresolved=unresolved,
            provenance=provenance,
            warnings=warnings,
            mode="none",
        )

    qere = resolve_qere(norm.working, yhwh_as=yhwh_as)
    reading = qere.text
    if qere.substitutions:
        provenance.append({"stage": "qere", "substitutions": qere.substitutions})

    if prof.stream == "extended_forte":
        warnings.append(
            "extended_forte: JS Tiberian schema implements the forte–lene stream; "
            "prolonged word-initial BGDKPT is not fully modelled yet."
        )

    use_js = engine == "js" or (engine == "auto" and js_engine_status()["available"])
    if engine == "python":
        use_js = False

    if use_js:
        try:
            ipa = bare_ipa(transliterate_js(reading))
            provenance.append(
                {
                    "stage": "rules",
                    "engine": "hebrew-transliteration",
                    "schema": "docs/tiberian.ts",
                    "stream": prof.stream,
                    "syllabifier": "havarotjs",
                }
            )
            return Result(
                input=text,
                reading=reading,
                ipa=ipa,
                provenance=provenance,
                unresolved=unresolved,
                warnings=warnings,
                profile=prof.name,
                mode="js-tiberian",
            )
        except JsEngineError as exc:
            if engine == "js":
                unresolved.append(
                    {
                        "span": reading,
                        "reason": "js_engine_unavailable",
                        "message": str(exc),
                    }
                )
                return _empty_result(
                    text,
                    reading=reading,
                    prof=prof,
                    unresolved=unresolved,
                    provenance=provenance,
                    warnings=warnings,
                    mode="error",
                )
            warnings.append(f"JS engine failed ({exc}); falling back to pure Python.")

    ipa, word_results, unr = phrase_to_ipa(reading, prof)
    unresolved.extend(unr)
    ipa = bare_ipa(ipa)
    provenance.append(
        {
            "stage": "rules",
            "engine": "python",
            "stream": prof.stream,
            "words": [{"raw": w.raw, "ipa": w.ipa, "rules": w.rule_ids} for w in word_results],
        }
    )
    mode = "rules-python"
    if any(u.get("reason") == "unsupported_consonant_mapping" for u in unresolved):
        mode = "rules-python-partial"
    return Result(
        input=text,
        reading=reading,
        ipa=ipa,
        provenance=provenance,
        unresolved=unresolved,
        warnings=warnings,
        profile=prof.name,
        mode=mode,
    )
