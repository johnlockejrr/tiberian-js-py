"""Node-backed Tiberian IPA engine (js/schemas/tiberian.ts + hebrew-transliteration).

The Tiberian Schema drives charlesLoder/hebrew-transliteration (plus havarotjs
syllabification): vowel length, closed-syllable epenthesis, shewa, digraph
gemination, etc. This module invokes ``js/runner.ts`` via ``npx tsx``.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from functools import lru_cache
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_JS_DIR = _REPO_ROOT / "js"
_RUNNER = _JS_DIR / "runner.ts"
_SCHEMA = _JS_DIR / "schemas" / "tiberian.ts"


class JsEngineError(RuntimeError):
    """Raised when the Node Tiberian runner cannot be used or fails."""


@lru_cache(maxsize=1)
def js_engine_status() -> dict[str, str | bool]:
    """Return availability info for diagnostics (CLI / Result.warnings)."""
    node = shutil.which("node")
    npx = shutil.which("npx")
    npm_modules = _JS_DIR / "node_modules" / "hebrew-transliteration"
    tsx = _JS_DIR / "node_modules" / "tsx"
    return {
        "available": bool(
            node
            and npx
            and _RUNNER.is_file()
            and _SCHEMA.is_file()
            and npm_modules.is_dir()
            and tsx.is_dir()
        ),
        "node": node or "",
        "npx": npx or "",
        "runner": str(_RUNNER),
        "schema": str(_SCHEMA),
        "js_dir": str(_JS_DIR),
        "deps_installed": npm_modules.is_dir() and tsx.is_dir(),
    }


def require_js_engine() -> None:
    st = js_engine_status()
    if st["available"]:
        return
    hints = []
    if not st["node"]:
        hints.append("install Node.js (>=18) and ensure `node` is on PATH")
    if not st["deps_installed"]:
        hints.append(f"run: cd {_JS_DIR} && npm install")
    if not _RUNNER.is_file():
        hints.append(f"missing runner at {_RUNNER}")
    if not _SCHEMA.is_file():
        hints.append(f"missing schema at {_SCHEMA} (run scripts/sync_tiberian_schema.py)")
    raise JsEngineError("Tiberian JS engine unavailable. " + "; ".join(hints))


def transliterate_js(hebrew: str, *, timeout: float = 60.0) -> str:
    """Transcribe pointed Hebrew to Tiberian IPA via js/schemas/tiberian.ts."""
    require_js_engine()
    npx = str(js_engine_status()["npx"] or "npx")
    payload = json.dumps({"text": hebrew}, ensure_ascii=False)
    proc = subprocess.run(
        [npx, "tsx", str(_RUNNER)],
        input=payload,
        capture_output=True,
        text=True,
        cwd=str(_JS_DIR),
        timeout=timeout,
        check=False,
        env=os.environ.copy(),
    )
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip() or f"exit {proc.returncode}"
        raise JsEngineError(f"JS Tiberian runner failed: {err}")
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise JsEngineError(f"JS runner returned non-JSON: {proc.stdout[:200]!r}") from e
    ipa = data.get("ipa")
    if not isinstance(ipa, str) or not ipa.strip():
        raise JsEngineError(f"JS runner returned empty IPA: {data!r}")
    return ipa.strip()
