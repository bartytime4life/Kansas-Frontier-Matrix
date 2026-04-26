from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema.exceptions import SchemaError

from tools.receipts.ecology_manifest_builder import (
    build_manifest,
    validate_manifest,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SCHEMA_REF = Path("schemas/ecology/ecology_receipt_manifest.schema.json")


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def validator_receipt(
    *,
    decision: str = "pass",
    spec_hash: str = SPEC_HASH,
) -> dict:
    return {
        "receipt_type": "validator_result",
        "validator": "tools/validators/ecology_index",
        "schema_ref": "schemas/ecology/kfm_eco_index.schema.json",
        "input_ref": "candidate.json",
        "decision": decision,
        "errors": [],
        "warnings": [],
        "spec_hash": spec_hash,
        "generated_at": "2026-04-24T00:00:00Z",
    }


def test_validate_manifest_accepts_generated_manifest(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipt.json"
    write_json(receipt_path, validator_receipt())

    manifest = build_manifest(
        candidate_id="eco_index.example",
        candidate_type="eco_index",
        spec_hash=SPEC_HASH,
        receipt_paths=[receipt_path],
    )

    errors = validate_manifest(
        manifest=manifest,
        schema_path=SCHEMA_REF,
    )

    assert errors == []


def test_validate_manifest_reports_schema_errors(tmp_path: Path) -> None:
    bad_manifest = {
        "manifest_id": "kfm.receipt_manifest.ecology.eco_index.example",
        "candidate_id": "eco_index.example",
        "candidate_type": "not_a_candidate_type",
        "spec_hash": "not-a-sha256",
        "receipts": [],
        "decision": "ready_for_promotion",
        "generated_at": "2026-04-24T00:00:00Z",
    }

    errors = validate_manifest(
        manifest=bad_manifest,
        schema_path=SCHEMA_REF,
    )

    assert errors
    assert any("candidate_type" in error for error in errors)
    assert any("spec_hash" in error for error in errors)
    assert any("receipts" in error for error in errors)


def test_validate_manifest_rejects_invalid_schema(tmp_path: Path) -> None:
    schema_path = tmp_path / "invalid_manifest_schema.json"
    write_json(
        schema_path,
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": 123,
        },
    )

    manifest = {
        "manifest_id": "kfm.receipt_manifest.ecology.eco_index.example",
        "candidate_id": "eco_index.example",
        "candidate_type": "eco_index",
        "spec_hash": SPEC_HASH,
        "receipts": [
            {
                "receipt_type": "validator_result",
                "receipt_ref": "receipt.json",
                "decision": "pass",
                "generated_at": "2026-04-24T00:00:00Z",
            }
        ],
        "decision": "ready_for_promotion",
        "generated_at": "2026-04-24T00:00:00Z",
    }

    with pytest.raises(SchemaError):
        validate_manifest(
            manifest=manifest,
            schema_path=schema_path,
        )
