"""Contract/schema alignment proof for RuntimeResponseEnvelope precision.

This test enforces declared links and documented shape coverage. It does not
reimplement JSON Schema validation, calculate precision, resolve evidence,
authorize an answer, or establish release or publication authority.
"""
from __future__ import annotations

import json
from pathlib import Path
import re


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = (
    REPOSITORY_ROOT / "contracts/runtime/runtime_response_envelope.md"
)
PRECISION_PROFILE_PATH = (
    REPOSITORY_ROOT / "contracts/runtime/precision_actually_used.md"
)
SCHEMA_PATH = (
    REPOSITORY_ROOT
    / "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
)


def _load_schema() -> dict[str, object]:
    value = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object: {SCHEMA_PATH}")
    return value


def _documented_table_fields(markdown: str) -> set[str]:
    return set(
        re.findall(
            r"^\| `([a-z][a-z0-9_]*)` \|",
            markdown,
            flags=re.MULTILINE,
        )
    )


def test_runtime_response_contract_tracks_schema_precision_profile() -> None:
    schema = _load_schema()
    contract = CONTRACT_PATH.read_text(encoding="utf-8")
    precision_profile = PRECISION_PROFILE_PATH.read_text(encoding="utf-8")

    metadata = schema["x-kfm"]
    assert isinstance(metadata, dict)
    assert metadata["contract_doc"] == CONTRACT_PATH.relative_to(
        REPOSITORY_ROOT
    ).as_posix()
    assert metadata["precision_contract_doc"] == PRECISION_PROFILE_PATH.relative_to(
        REPOSITORY_ROOT
    ).as_posix()

    documented_fields = _documented_table_fields(contract)
    top_level_properties = set(schema["properties"])
    precision_properties = set(schema["$defs"]["precisionActuallyUsed"]["properties"])
    assert top_level_properties <= documented_fields
    assert precision_properties <= documented_fields

    assert "./precision_actually_used.md" in contract
    assert "./runtime_response_envelope.md" in precision_profile

    assert re.search(
        r"\| `outcome == ANSWER` \| "
        r"`evidence_refs` has at least one item and "
        r"`precision_actually_used` is required\. \|",
        contract,
    )
    assert re.search(
        r"\| `outcome != ANSWER` \| "
        r"`precision_actually_used` is forbidden\. \|",
        contract,
    )
