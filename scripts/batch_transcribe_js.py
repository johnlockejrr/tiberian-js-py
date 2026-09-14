#!/usr/bin/env python3
"""Batch-transcribe via the Node Tiberian wrapper (same I/O format as native/).

Verse-numbered chapter files (e.g. Genesis_1.txt)::

    1 בְּרֵאשִׁ֖ית …׃ 2 וְהָאָ֗רֶץ …׃

Output matches ``native/scripts/batch_transcribe.py`` so files can be diffed::

    1\\tbaʀ̟eːˈʃiːiθ …
    2\\tvɔhɔːˈʔɔːʀ̟ɛsˁ …

Usage (from repo root, with venv that has ``tiberian`` installed + ``js/`` deps)::

    python scripts/batch_transcribe_js.py -i Genesis_1.txt -o Genesis_1.js.ipa.txt
    python scripts/batch_transcribe_js.py -i Genesis_1.txt -o Genesis_1.js.ipa.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from tiberian.api import transcribe
from tiberian.engine_js import JsEngineError, js_engine_status

# Same parsing rules as native/scripts/batch_transcribe.py
_VERSE_START = re.compile(r"(?:(?<=^)|(?<=\s))(\d+)\s+", re.UNICODE)
_SECTION_MARK = re.compile(r"\s*\{[פס]\}")
_JUNK = re.compile(r"[\ufeff\u00ad]")


def parse_verses(text: str) -> list[tuple[str, str]]:
    """Return ``[(verse_number, hebrew), ...]`` from a chapter blob."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = _JUNK.sub("", text).strip()
    if not text:
        return []

    matches = list(_VERSE_START.finditer(text))
    if not matches:
        cleaned = _SECTION_MARK.sub("", text).strip()
        return [("?", cleaned)] if cleaned else []

    verses: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        num = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        heb = _SECTION_MARK.sub("", text[start:end]).strip()
        if heb:
            verses.append((num, heb))
    return verses


def format_line(num: str, ipa: str | None, *, mode: str) -> str:
    if ipa is None:
        return f"{num}\t# FAILED ({mode})"
    return f"{num}\t{ipa}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Batch Tiberian IPA via Node hebrew-transliteration "
            "(same output format as native/scripts/batch_transcribe.py)."
        ),
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Input UTF-8 text (verse-numbered Hebrew chapter)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="Output path (.txt or .jsonl)",
    )
    parser.add_argument(
        "--format",
        choices=("txt", "jsonl"),
        default=None,
        help="Output format (default: jsonl if --output ends with .jsonl, else txt)",
    )
    parser.add_argument(
        "-p",
        "--profile",
        default="forte_lene",
        help="Pronunciation stream label (default: forte_lene)",
    )
    args = parser.parse_args(argv)

    if not args.input.is_file():
        print(f"input not found: {args.input}", file=sys.stderr)
        return 1

    st = js_engine_status()
    if not st["available"]:
        print(
            "JS Tiberian engine unavailable. "
            f"Install Node ≥18 and run: cd js && npm install  (runner={st['runner']})",
            file=sys.stderr,
        )
        return 1

    fmt = args.format
    if fmt is None:
        fmt = "jsonl" if args.output.suffix.lower() == ".jsonl" else "txt"

    raw = args.input.read_text(encoding="utf-8")
    verses = parse_verses(raw)
    if not verses:
        print("no verses found in input", file=sys.stderr)
        return 1

    lines_out: list[str] = []
    n_ok = 0
    n_fail = 0

    for num, heb in verses:
        warnings: list[str] = []
        unresolved: list[dict] = []
        try:
            result = transcribe(heb, args.profile, engine="js")
            ipa = result.ipa
            mode = result.mode
            warnings = list(result.warnings)
            unresolved = list(result.unresolved)
        except JsEngineError as exc:
            ipa = None
            mode = "js-error"
            unresolved = [
                {
                    "span": heb,
                    "reason": "js_engine_error",
                    "message": str(exc),
                }
            ]

        if ipa is None:
            n_fail += 1
            for w in warnings:
                print(f"# {num}: warning: {w}", file=sys.stderr)
            for u in unresolved:
                print(
                    f"# {num}: {u.get('reason')}: {u.get('message') or ''}",
                    file=sys.stderr,
                )
        else:
            n_ok += 1
            for w in warnings:
                print(f"# {num}: warning: {w}", file=sys.stderr)

        if fmt == "jsonl":
            lines_out.append(
                json.dumps(
                    {
                        "verse": num,
                        "hebrew": heb,
                        "ipa": ipa,
                        "mode": mode,
                        "warnings": warnings,
                        "unresolved": unresolved,
                        "engine": "js",
                    },
                    ensure_ascii=False,
                )
            )
        else:
            lines_out.append(format_line(num, ipa, mode=mode))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    print(
        f"wrote {args.output} ({n_ok} ok, {n_fail} failed, {len(verses)} verses) [js]",
        file=sys.stderr,
    )
    return 0 if n_fail == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
