"""Phase 1: validate corpus JSON schema, uniqueness, and MD↔JSON parity."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
CORPUS_DIR = ROOT / "corpus"
JSON_PATH = CORPUS_DIR / "tiberian_rules.json"
MD_PATH = CORPUS_DIR / "tiberian_rules.md"
SCHEMA_PATH = CORPUS_DIR / "schema" / "rule.schema.json"

SOURCE_FILES = [
    "T1_0_Intro.md",
    "T1_1.md",
    "T1_2B_corrected_p352.md",
    "T1_3B.md",
    "T1_4B_5_Ref.md",
]

ID_RE = re.compile(
    r"^TH-(CON|BGDKPT|GUTT|DAG|RAF|VOW|LEN|SHEWA|HATEF|SYL|STR|MAQ|QK|VAR|GAP|ACC|ORTH)"
    r"-[A-Z0-9]+(-[A-Z0-9]+)*$"
)


@pytest.fixture(scope="module")
def corpus() -> dict:
    assert JSON_PATH.exists(), f"missing {JSON_PATH}"
    return json.loads(JSON_PATH.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def test_schema_file_exists(schema: dict) -> None:
    assert schema.get("$schema")
    assert "rule" in schema.get("$defs", {})


def test_corpus_meta(corpus: dict) -> None:
    assert corpus.get("version")
    assert set(corpus.get("source_files", [])) == set(SOURCE_FILES)
    assert isinstance(corpus.get("rules"), list)
    assert len(corpus["rules"]) > 0


def test_unique_ids(corpus: dict) -> None:
    ids = [r["id"] for r in corpus["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs"


def test_id_pattern(corpus: dict) -> None:
    bad = [r["id"] for r in corpus["rules"] if not ID_RE.match(r["id"])]
    assert not bad, f"bad IDs: {bad[:10]}"


def test_required_fields(corpus: dict) -> None:
    required = [
        "id",
        "title",
        "status",
        "authority",
        "category",
        "subcategory",
        "statement",
        "conditions",
        "operation",
        "result_ipa",
        "examples",
        "source",
        "certainty",
    ]
    for rule in corpus["rules"]:
        for key in required:
            assert key in rule, f"{rule.get('id')} missing {key}"
        assert rule["status"] in {
            "rule",
            "exception",
            "variant",
            "evidence",
            "gap",
            "conflict",
        }
        assert rule["authority"] in {
            "standard-tiberian",
            "non-standard-tiberian",
            "manuscript",
            "comparative",
            "editorial",
        }
        assert rule["source"]["file"] in SOURCE_FILES
        assert rule["source"].get("section")
        if not rule["examples"]:
            assert rule.get("no_example_in_source") is True, (
                f"{rule['id']} has no examples but no_example_in_source is not true"
            )


def test_related_ids_resolve(corpus: dict) -> None:
    ids = {r["id"] for r in corpus["rules"]}
    missing = []
    for rule in corpus["rules"]:
        for rid in rule.get("related_ids") or []:
            if rid not in ids:
                missing.append((rule["id"], rid))
    assert not missing, f"dangling related_ids: {missing[:20]}"


def test_markdown_lists_every_id(corpus: dict) -> None:
    assert MD_PATH.exists()
    md = MD_PATH.read_text(encoding="utf-8")
    missing = [r["id"] for r in corpus["rules"] if r["id"] not in md]
    assert not missing, f"IDs missing from markdown: {missing[:20]}"


def test_no_json_only_invented_status_without_source(corpus: dict) -> None:
    for rule in corpus["rules"]:
        assert rule["source"]["file"] in SOURCE_FILES
        assert rule["statement"].strip()


def test_gap_rules_have_null_or_unresolved(corpus: dict) -> None:
    for rule in corpus["rules"]:
        if rule["status"] in {"gap", "conflict"}:
            assert rule["certainty"] in {"low", "unresolved", "medium"}


def test_jsonschema_if_available(corpus: dict, schema: dict) -> None:
    jsonschema = pytest.importorskip("jsonschema")
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema).validate(corpus)
