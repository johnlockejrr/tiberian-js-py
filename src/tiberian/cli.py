"""CLI: tiberian TEXT [--profile PROFILE] [--json]."""

from __future__ import annotations

import argparse
import json
import sys

from tiberian.api import transcribe
from tiberian.profiles import PROFILES


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="tiberian",
        description=(
            "Rule-based Tiberian Hebrew IPA (Khan T1). "
            "Applies pronunciation rules to any pointed Biblical Hebrew."
        ),
    )
    parser.add_argument("text", nargs="?", help="Masoretic Hebrew (or stdin)")
    parser.add_argument(
        "--profile",
        "-p",
        default="forte_lene",
        help=(
            "forte_lene (default, first I.5.4 stream) or extended_forte (prolonged). "
            f"Known: {', '.join(sorted(set(PROFILES)))}"
        ),
    )
    parser.add_argument("--json", action="store_true", help="Emit full Result JSON")
    parser.add_argument(
        "--yhwh",
        choices=("adonai", "elohim"),
        default="adonai",
        help="Tetragrammaton qere",
    )
    parser.add_argument(
        "--engine",
        choices=("js", "python", "auto"),
        default="js",
        help=(
            "js (default): hebrew-transliteration Tiberian schema "
            "(js/schemas/tiberian.ts + havarotjs syllables); "
            "python: incomplete pure-Python path; auto: js if available"
        ),
    )
    args = parser.parse_args(argv)
    text = args.text if args.text is not None else sys.stdin.read()
    if not text or not str(text).strip():
        parser.error("No input text")

    result = transcribe(text, args.profile, yhwh_as=args.yhwh, engine=args.engine)

    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    else:
        if result.ipa is None:
            print("IPA: (unresolved)", file=sys.stderr)
            for u in result.unresolved:
                print(f"  - {u.get('reason')}: {u.get('span')!r}", file=sys.stderr)
            return 2
        print(result.ipa)
        for w in result.warnings:
            print(f"# warning: {w}", file=sys.stderr)
        if result.unresolved:
            print(f"# unresolved: {len(result.unresolved)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
