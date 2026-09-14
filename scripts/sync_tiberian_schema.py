#!/usr/bin/env python3
"""Sync docs/tiberian.ts → js/schemas/tiberian.ts (package Schema import)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "tiberian.ts"
DST = ROOT / "js" / "schemas" / "tiberian.ts"

OLD = 'import type { Schema } from "../schema.js";'
NEW = 'import type { Schema } from "hebrew-transliteration";'


def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    if OLD not in text:
        raise SystemExit(f"unexpected import in {SRC}")
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
    print(f"synced {SRC} → {DST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
