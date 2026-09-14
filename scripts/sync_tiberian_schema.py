#!/usr/bin/env python3
"""Deprecated: schema now lives only at js/schemas/tiberian.ts (docs/ is private)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DST = ROOT / "js" / "schemas" / "tiberian.ts"


def main() -> int:
    if DST.is_file():
        print(f"schema already at {DST} (no docs/ sync; docs/ is not published)")
        return 0
    print(f"missing {DST}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
