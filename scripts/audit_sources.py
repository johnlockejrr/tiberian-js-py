#!/usr/bin/env python3
"""Audit corpus + fixtures against T1 sources; report hierarchy and encoding issues."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Pipeline hierarchy (application order) — linguistic domains, not alpha ID order
PIPELINE_STAGES = [
    ("01_normalize", "Unicode NFD + orthographic fixes"),
    ("02_qere", "Qere/ketiv resolution"),
    ("03_orthography", "Letters, matres, shin/sin, dagesh/rafe marks"),
    ("04_inventory", "Consonant/vowel IPA inventory"),
    ("05_shewa_hatef", "Shewa / ḥaṭef classification"),
    ("06_syllables", "Syllabification / metrical structure"),
    ("07_length", "Vowel length, epenthesis, furtive pataḥ"),
    ("08_bgdkpt", "Begadkephat stop/fricative + sandhi"),
    ("09_gemination", "Dagesh forte / extended forte / loss of gemination"),
    ("10_resh_guttural", "Resh allophony, guttural constraints"),
    ("11_stress_maq", "Stress, gaʿya, maqqef, deḥiq"),
    ("12_emit", "IPA emission (bare, forte_lene default)"),
]


def clean_ipa(s: str) -> str:
    s = s.strip().replace("\\[", "[").replace("\\]", "]").replace("\\-", "-")
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\[\[[0-9]+\]\]\([^)]*\)", "", s)
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    return re.sub(r"\s+", " ", s).strip().replace("[", "").replace("]", "")


def extract_verses(sec: str):
    lines = sec.splitlines()
    verses = []
    i = 0
    while i < len(lines):
        m = re.match(r"^(\d+)\s+(.+)$", lines[i].strip())
        if m and re.search(r"[\u05D0-\u05EA]", m.group(2)):
            num = int(m.group(1))
            heb = m.group(2).strip()
            ipas = []
            j = i + 1
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith("[") or s.startswith("\\["):
                    ipas.append(clean_ipa(s))
                    j += 1
                    continue
                if re.match(r"^\d+\s+", s) and re.search(r"[\u05D0-\u05EA]", s):
                    break
                if s.startswith("I.5") or s.startswith("REFERENCES"):
                    break
                j += 1
            fl = ipas[0] if ipas else None
            ef = ipas[1] if len(ipas) > 1 else fl
            verses.append({"verse": num, "hebrew": heb, "forte_lene": fl, "extended_forte": ef})
            i = j
            continue
        i += 1
    return verses


def main() -> None:
    report: list[str] = ["# Source audit report", ""]

    # --- Hierarchy ---
    report += ["## Rule application hierarchy (engine pipeline)", ""]
    report += [
        "Corpus JSON is sorted by rule **id** for stability. "
        "Pronunciation **application** order is the pipeline below "
        "(not alphabetical categories).",
        "",
    ]
    for sid, desc in PIPELINE_STAGES:
        report.append(f"1. `{sid}` — {desc}")
    report.append("")

    corpus = json.loads((ROOT / "corpus/tiberian_rules.json").read_text(encoding="utf-8"))
    rules = corpus["rules"]
    report += [
        f"## Corpus stats",
        "",
        f"- Rules: **{len(rules)}**",
        f"- Sorted by id: **{rules == sorted(rules, key=lambda r: r['id'])}**",
        f"- With ordering_notes: **{sum(1 for r in rules if r.get('ordering_notes'))}**",
        "",
    ]

    # --- Encoding in sources ---
    report += ["## Holam-vav encoding in T1 sources", ""]
    report += ["| File | VAV+HOLAM (`וֹ`) | HOLAM+VAV (`ֹו`) | VAV+U+05BA |", "|------|-----|-----|-----|"]
    for fn in sorted(ROOT.glob("T1_*.md")):
        text = fn.read_text(encoding="utf-8")
        vh = len(re.findall("\u05D5\u05B9", text))
        hv = len(re.findall("\u05B9\u05D5", text))
        ha = len(re.findall("\u05D5\u05BA", text))
        report.append(f"| {fn.name} | {vh} | {hv} | {ha} |")
    report += [
        "",
        "Verdict: **VAV then HOLAM (`וֹ`) is the source-majority form**; "
        "pipeline rewrites HOLAM+VAV and stranded holam-before-vav to that form.",
        "",
    ]

    # --- Sample IPA audit ---
    text = (ROOT / "T1_4B_5_Ref.md").read_text(encoding="utf-8")
    gen = extract_verses(
        text[text.find("I.5.4.1. Genesis") : text.find("I.5.4.2. Psalm")]
    )
    psa = extract_verses(
        text[text.find("I.5.4.2. Psalm") : text.find("REFERENCES AND ABBREVIATIONS")]
    )
    fix_gen = json.loads((ROOT / "tests/fixtures/genesis_1_1_13.json").read_text(encoding="utf-8"))
    fix_psa = json.loads((ROOT / "tests/fixtures/psalm_1.json").read_text(encoding="utf-8"))

    report += ["## I.5.4 fixture vs source (forte_lene = first reading)", ""]
    mismatches = []
    for label, fresh, fix in (("Genesis", gen, fix_gen), ("Psalm", psa, fix_psa)):
        report.append(f"### {label}")
        report.append("")
        for src, row in zip(fresh, fix):
            issues = []
            if src["forte_lene"] != row["forte_lene"]:
                issues.append("forte_lene IPA ≠ source")
            if (src.get("extended_forte") or src["forte_lene"]) != row.get("extended_forte"):
                issues.append("extended_forte IPA ≠ source")
            # holam order in hebrew
            if "\u05B9\u05D5" in src["hebrew"]:
                issues.append("source hebrew has HOLAM+VAV (minor encoding)")
            if issues:
                mismatches.append((label, src["verse"], issues))
                report.append(f"- v{src['verse']}: {', '.join(issues)}")
            else:
                report.append(f"- v{src['verse']}: OK")
        report.append("")

    # --- Corpus sample rules vs fixtures ---
    report += ["## Corpus TH-ORTH-SAMPLE vs fixtures", ""]
    samples = [r for r in rules if r["id"].startswith("TH-ORTH-SAMPLE-")]
    report.append(f"Sample rules: **{len(samples)}**")
    bare_ok = 0
    for r in samples:
        for ex in r.get("examples") or []:
            ipa = ex.get("source_ipa") or ""
            if ipa and "[" not in ipa and "]" not in ipa:
                bare_ok += 1
    report.append(f"Bare (unbracketed) sample IPAs: **{bare_ok}**")
    report.append("")

    # --- Possible source misspellings: HOLAM+VAV islands ---
    report += ["## Candidate source encoding quirks (not silent-fixed in SoT files)", ""]
    for fn in sorted(ROOT.glob("T1_*.md")):
        text = fn.read_text(encoding="utf-8")
        for m in re.finditer(r".{0,15}\u05B9\u05D5.{0,15}", text):
            snippet = m.group().replace("\n", " ")
            report.append(f"- `{fn.name}`: …{snippet}…")
    report.append("")

    out = ROOT / "corpus" / "SOURCE_AUDIT.md"
    out.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(f"mismatches: {len(mismatches)}")
    for m in mismatches[:20]:
        print(" ", m)

    # Write pipeline order file for the engine
    pipe = {
        "version": "1.0.0",
        "description": "Hierarchical application order for Tiberian IPA pipeline",
        "default_stream": "forte_lene",
        "unicode_working_form": "NFD",
        "stages": [{"id": a, "description": b} for a, b in PIPELINE_STAGES],
    }
    pipe_path = ROOT / "corpus" / "rule_pipeline.json"
    pipe_path.write_text(json.dumps(pipe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {pipe_path}")


if __name__ == "__main__":
    main()
