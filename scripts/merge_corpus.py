#!/usr/bin/env python3
"""Merge corpus/_partials/*_rules.json into tiberian_rules.json and generate markdown."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTIALS = ROOT / "corpus" / "_partials"
OUT_JSON = ROOT / "corpus" / "tiberian_rules.json"
OUT_MD = ROOT / "corpus" / "tiberian_rules.md"

SOURCE_FILES = [
    "T1_0_Intro.md",
    "T1_1.md",
    "T1_2B_corrected_p352.md",
    "T1_3B.md",
    "T1_4B_5_Ref.md",
]

CATEGORY_ORDER = [
    "conventions",
    "authority",
    "orthography",
    "qere-ketiv",
    "accents",
    "consonants",
    "begadkephat",
    "gutturals",
    "dagesh",
    "rafe",
    "gemination",
    "vowels",
    "vowel-length",
    "shewa",
    "hatef",
    "syllables",
    "stress",
    "maqqef",
    "samples",
    "variation",
    "gaps",
    "other",
]


FILE_TAG = {
    "t1_0_rules.json": "T0",
    "t1_1_rules.json": "T1",
    "t1_2_rules.json": "T2",
    "t1_3_rules.json": "T3",
    "t1_4_rules.json": "T4",
}


def uniquify_ids(rules: list[dict], tag: str) -> None:
    """Ensure globally unique IDs by suffixing with source-file tag on collision later."""
    for r in rules:
        rid = r["id"]
        # Prefer semantic IDs that already include descriptive tails; always stamp source tag
        # after the family prefix if the id is a short numbered form, else append tag.
        if re.search(r"-(0[0-9]{2}|[0-9]{3})$", rid) or rid.count("-") <= 2:
            # TH-VOW-001 -> TH-VOW-T0-001
            parts = rid.split("-")
            if len(parts) >= 3 and parts[-1].isdigit():
                r["id"] = "-".join(parts[:-1] + [tag, parts[-1]])
            else:
                r["id"] = f"{rid}-{tag}"
        else:
            if not rid.endswith(f"-{tag}"):
                r["id"] = f"{rid}-{tag}"


def load_partials() -> list[dict]:
    rules: list[dict] = []
    for path in sorted(PARTIALS.glob("*_rules.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise SystemExit(f"{path} must be a JSON array")
        tag = FILE_TAG.get(path.name, path.stem.upper()[:2])
        uniquify_ids(data, tag)
        rules.extend(data)
    # Final collision pass
    seen: dict[str, int] = {}
    for r in rules:
        rid = r["id"]
        if rid in seen:
            seen[rid] += 1
            r["id"] = f"{rid}-X{seen[rid]}"
        else:
            seen[rid] = 0
    return rules


STATUS_MAP = {
    "rule": "rule",
    "active": "rule",
    "standard": "rule",
    "inventory": "rule",
    "standard-sample": "rule",
    "standard-stream": "rule",
    "exception": "exception",
    "variant": "variant",
    "standard-variant": "variant",
    "evidence-variant": "variant",
    "non-standard": "variant",
    "evidence": "evidence",
    "historical-evidence": "evidence",
    "gap": "gap",
    "editorial-gap": "gap",
    "conflict": "conflict",
}

AUTHORITY_MAP_EXACT = {
    "standard-tiberian": "standard-tiberian",
    "non-standard-tiberian": "non-standard-tiberian",
    "manuscript": "manuscript",
    "comparative": "comparative",
    "editorial": "editorial",
}


def map_authority(raw: str) -> str:
    s = (raw or "").strip().lower()
    if s in AUTHORITY_MAP_EXACT:
        return AUTHORITY_MAP_EXACT[s]
    if "non-standard" in s or "nst" in s:
        return "non-standard-tiberian"
    if "manuscript" in s or "codex" in s or s in {"a", "l", "c", "b", "s"}:
        return "manuscript"
    if any(x in s for x in ("babylon", "palestin", "compar", "karaite", "modern", "yemen", "samaritan", "community")):
        return "comparative"
    if "editorial" in s or "bhs" in s or "analysis" in s:
        return "editorial"
    if "standard" in s or "tiberian" in s or "ben asher" in s or "ben naftali" in s:
        return "standard-tiberian"
    return "standard-tiberian"



def strip_ipa_brackets(s: str | None) -> str | None:
    """Book prints IPA in [brackets]; project transcriptions are bare IPA only."""
    if s is None:
        return None
    out = str(s).strip().replace("\\-", "-")
    # remove all outer/wrapping square brackets used as IPA delimiters
    while True:
        nxt = re.sub(r"^\[(.*)\]$", r"\1", out, flags=re.S).strip()
        if nxt == out:
            break
        out = nxt
    # also drop leftover delimiter brackets that are not IPA segmentals
    # (keep phonetic symbols like ʰ ʾ etc.; only ASCII [] wrappers)
    out = out.replace("[", "").replace("]", "")
    out = re.sub(r"\s+", " ", out).strip()
    return out or None


def map_stream(raw):
    if raw is None:
        return None
    s = str(raw).strip().lower()
    if s in {"forte-lene", "forte_lene", "dagesh forte-lene", "forte–lene"}:
        return "forte-lene"
    if s in {"extended-forte", "extended_forte", "extended forte"}:
        return "extended-forte"
    if s in {"either", "both", "same"}:
        return "either"
    if "standard" in s:
        return None
    return None



def as_str(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "; ".join(as_str(v) for v in value)
    return str(value)


def listify(val):
    if val is None:
        return []
    if isinstance(val, list):
        return [as_str(x) for x in val]
    if isinstance(val, str) and val.strip():
        return [val]
    return []


def normalize(rule: dict) -> dict:
    raw_status = rule.get("status", "rule")
    mapped = STATUS_MAP.get(str(raw_status).lower())
    if mapped:
        rule["status"] = mapped
    else:
        rs = str(raw_status).lower()
        if "gap" in rs:
            rule["status"] = "gap"
        elif "conflict" in rs:
            rule["status"] = "conflict"
        elif "exception" in rs:
            rule["status"] = "exception"
        elif "variant" in rs or "non-standard" in rs:
            rule["status"] = "variant"
        elif "evidence" in rs:
            rule["status"] = "evidence"
        else:
            rule["status"] = "rule"

    rule["authority"] = map_authority(str(rule.get("authority", "standard-tiberian")))
    rule["title"] = as_str(rule.get("title", ""))
    rule["statement"] = as_str(rule.get("statement", ""))
    rule["conditions"] = as_str(rule.get("conditions", ""))
    rule["operation"] = as_str(rule.get("operation", ""))
    rule["category"] = as_str(rule.get("category", "other")) or "other"
    rule["subcategory"] = as_str(rule.get("subcategory", ""))
    rule["ordering_notes"] = as_str(rule.get("ordering_notes", ""))
    rule["notes"] = as_str(rule.get("notes", ""))
    if "result_ipa" not in rule:
        rule["result_ipa"] = None
    elif rule["result_ipa"] is not None and not isinstance(rule["result_ipa"], str):
        rule["result_ipa"] = as_str(rule["result_ipa"])
    if rule.get("result_ipa") is not None:
        rule["result_ipa"] = strip_ipa_brackets(as_str(rule["result_ipa"]))

    rule["preconditions"] = listify(rule.get("preconditions"))
    rule["exceptions"] = listify(rule.get("exceptions"))
    rule["related_ids"] = listify(rule.get("related_ids"))

    rule.setdefault("certainty", "medium")
    if rule["certainty"] not in {"high", "medium", "low", "unresolved"}:
        c = str(rule["certainty"]).lower()
        if c in {"high", "medium", "low", "unresolved"}:
            rule["certainty"] = c
        elif "unresolv" in c or "unknown" in c:
            rule["certainty"] = "unresolved"
        elif "low" in c:
            rule["certainty"] = "low"
        elif "high" in c:
            rule["certainty"] = "high"
        else:
            rule["certainty"] = "medium"
    if rule["status"] in {"gap", "conflict"} and rule["certainty"] == "high":
        rule["certainty"] = "unresolved"

    examples = rule.get("examples") or []
    rule["no_example_in_source"] = bool(rule.get("no_example_in_source")) or len(examples) == 0
    if rule["no_example_in_source"] and not examples:
        rule["examples"] = []
    else:
        rule["examples"] = examples
    for ex in rule["examples"]:
        ex["hebrew"] = as_str(ex.get("hebrew", ""))
        sipa = ex.get("source_ipa")
        ex["source_ipa"] = None if sipa is None else strip_ipa_brackets(as_str(sipa))
        ex["transliteration"] = ex.get("transliteration")
        ex["gloss"] = ex.get("gloss")
        ex["citation"] = ex.get("citation")
        ex["manuscript"] = ex.get("manuscript")
        ex["stream"] = map_stream(ex.get("stream"))
    src = rule.setdefault("source", {})
    fname = src.get("file", "")
    aliases = {
        "T1_0.md": "T1_0_Intro.md",
        "T1_0_Intro": "T1_0_Intro.md",
        "T1_1": "T1_1.md",
        "T1_2": "T1_2B_corrected_p352.md",
        "T1_2B.md": "T1_2B_corrected_p352.md",
        "T1_3.md": "T1_3B.md",
        "T1_3B": "T1_3B.md",
        "T1_4.md": "T1_4B_5_Ref.md",
        "T1_4B_5_Ref": "T1_4B_5_Ref.md",
    }
    if fname in aliases:
        src["file"] = aliases[fname]
    src["section"] = as_str(src.get("section", ""))
    src.setdefault("line_start", None)
    src.setdefault("line_end", None)
    src["excerpt"] = as_str(src.get("excerpt", ""))
    return rule


def category_key(rule: dict) -> str:
    c = (rule.get("category") or "other").lower().replace(" ", "-")
    for known in CATEGORY_ORDER:
        if known in c or c in known:
            return known
    if rule["status"] in {"gap", "conflict"}:
        return "gaps"
    if rule["id"].startswith("TH-GAP"):
        return "gaps"
    return c if c in CATEGORY_ORDER else "other"


def render_md(rules: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for r in rules:
        by_cat[category_key(r)].append(r)

    lines = [
        "# Tiberian Hebrew Pronunciation Rules",
        "",
        "Source-faithful extraction from Khan T1 sources. Machine companion: `tiberian_rules.json`.",
        "",
        f"Total rules: **{len(rules)}**",
        "",
    ]
    for cat in CATEGORY_ORDER:
        items = by_cat.get(cat)
        if not items:
            continue
        lines.append(f"## {cat}")
        lines.append("")
        for r in sorted(items, key=lambda x: x["id"]):
            lines.append(f"### {r['id']}: {r['title']}")
            lines.append("")
            lines.append(f"- **Status:** {r['status']}")
            lines.append(f"- **Authority:** {r['authority']}")
            lines.append(f"- **Category:** {r['category']} / {r['subcategory']}")
            lines.append(f"- **Statement:** {r['statement']}")
            if r.get("conditions"):
                lines.append(f"- **Conditions:** {r['conditions']}")
            if r.get("operation"):
                lines.append(f"- **Operation:** {r['operation']}")
            lines.append(f"- **Result IPA:** {r['result_ipa']!s}")
            lines.append(
                f"- **Source:** {r['source']['file']} §{r['source']['section']}"
                + (
                    f" (lines {r['source'].get('line_start')}–{r['source'].get('line_end')})"
                    if r["source"].get("line_start")
                    else ""
                )
            )
            lines.append(f"- **Certainty:** {r['certainty']}")
            if r.get("notes"):
                lines.append(f"- **Notes:** {r['notes']}")
            if r.get("related_ids"):
                lines.append(f"- **Related:** {', '.join(r['related_ids'])}")
            if r.get("no_example_in_source") or not r.get("examples"):
                lines.append("- **Examples:** no example in source")
            else:
                lines.append("- **Examples:**")
                for ex in r["examples"]:
                    ipa = ex.get("source_ipa") or "—"
                    cit = f" ({ex['citation']})" if ex.get("citation") else ""
                    stream = f" [{ex['stream']}]" if ex.get("stream") else ""
                    lines.append(f"  - `{ex['hebrew']}` → `{ipa}`{cit}{stream}")
            lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    rules = [normalize(r) for r in load_partials()]
    ids = [r["id"] for r in rules]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        raise SystemExit(f"duplicate IDs: {dupes}")

    # Drop related_ids that don't exist yet (warn only)
    idset = set(ids)
    for r in rules:
        bad = [x for x in r.get("related_ids") or [] if x not in idset]
        if bad:
            r["related_ids"] = [x for x in r["related_ids"] if x in idset]
            note = f"Dropped unresolved related_ids: {bad}"
            r["notes"] = (r.get("notes") or "") + (" | " if r.get("notes") else "") + note

    corpus = {
        "version": "1.0.0",
        "description": "Source-faithful Tiberian Hebrew pronunciation rules corpus (Khan T1).",
        "source_files": SOURCE_FILES,
        "rules": sorted(rules, key=lambda r: r["id"]),
    }
    OUT_JSON.write_text(json.dumps(corpus, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(corpus["rules"]), encoding="utf-8")
    print(f"Wrote {len(rules)} rules -> {OUT_JSON} and {OUT_MD}")


if __name__ == "__main__":
    main()
