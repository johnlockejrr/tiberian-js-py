"""Load I.5 inventory IPA values from the rules corpus (source-faithful)."""

from __future__ import annotations

from functools import lru_cache

from tiberian.corpus_loader import iter_rules


@lru_cache(maxsize=1)
def consonant_inventory() -> dict[str, str]:
    """Map rule titles / letters to primary IPA from I.5.1 corpus rules."""
    # Hard-coded letter keys filled from corpus result_ipa where available
    mapping: dict[str, str] = {}
    for rule in iter_rules(id_prefix="TH-CON-T4-"):
        ipa = rule.get("result_ipa") or ""
        # take first alternate before comma
        primary = ipa.split(",")[0].strip()
        title = rule.get("title", "").lower()
        statement = rule.get("statement", "").lower()
        blob = title + " " + statement
        letter_hints = [
            ("ʾalef", "א"),
            ("alef", "א"),
            ("bet (dagesh)", "בּ"),
            ("bet (rafe)", "ב"),
            ("gimel (dagesh)", "גּ"),
            ("gimel (rafe)", "ג"),
            ("dalet (dagesh)", "דּ"),
            ("dalet (rafe)", "ד"),
            ("he ", "ה"),
            ("vav", "ו"),
            ("zayin", "ז"),
            ("ḥet", "ח"),
            ("het", "ח"),
            ("ṭet", "ט"),
            ("tet", "ט"),
            ("yod", "י"),
            ("kaf (dagesh)", "כּ"),
            ("kaf (rafe)", "כ"),
            ("lamed", "ל"),
            ("mem", "מ"),
            ("nun", "נ"),
            ("samekh", "ס"),
            ("ʿayin", "ע"),
            ("ayin", "ע"),
            ("emphatic pe", "פּˁ"),
            ("pe (dagesh)", "פּ"),
            ("pe (rafe)", "פ"),
            ("ṣade", "צ"),
            ("sade", "צ"),
            ("qof", "ק"),
            ("resh", "ר"),
            ("sin", "שׂ"),
            ("shin", "שׁ"),
            ("tav (dagesh)", "תּ"),
            ("tav (rafe)", "ת"),
        ]
        for hint, key in letter_hints:
            if hint in blob and key not in mapping and primary:
                mapping[key] = primary
                break
    return mapping


@lru_cache(maxsize=1)
def vowel_inventory() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for rule in iter_rules(id_prefix="TH-VOW-T4-"):
        ipa = rule.get("result_ipa") or ""
        primary = ipa.split(",")[0].strip()
        title = rule.get("title", "").lower()
        keys = {
            "pataḥ": "patah",
            "patah": "patah",
            "qameṣ": "qamets",
            "qamets": "qamets",
            "segol": "segol",
            "ṣere": "tsere",
            "sere": "tsere",
            "ḥireq": "hiriq",
            "hireq": "hiriq",
            "ḥolem": "holam",
            "holem": "holam",
            "shureq": "shureq",
            "qibbuṣ": "shureq",
        }
        for needle, key in keys.items():
            if needle in title and primary:
                mapping[key] = primary
                break
    return mapping
