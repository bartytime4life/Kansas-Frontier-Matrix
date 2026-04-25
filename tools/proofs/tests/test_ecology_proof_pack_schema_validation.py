from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema.exceptions import SchemaError

from tools.proofs.ecology_proof_pack_builder import (
    build_proof_pack,
    validate_proof_pack,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SCHEMA_REF = Path("schemas/ecology/ecology_proof_pack.schema.json")


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def manifest() -> dict:
    return {
        "manifest_id": "kfm.receipt_manifest.ecology.eco_index.example",
        "candidate_id": "eco_index.example",
        "candidate_type": "eco_index",
        "spec_hash": SPEC_HASH,
        "receipts": [
            {
                "receipt_type": "validator_result",
                "validator": "tools/validators/ecology_index",
                "receipt_ref": "data/receipts/ecology/index/example.validator_receipt.json",
                "decision": "pass",
                "spec_hash": SPEC_HASH,
                "generated_at": "2026-04-24T00:00:00Z",
            }
        ],
        "decision": "ready_for_promotion",
        "generated_at": "2026-04-24T00:00:00Z",
    }


def catalog_refs() -> dict:
    return {
        "dcat": ["kfm:dcat:dataset:ecology:example"],
        "stac": ["kfm:stac:item:ecology:example"],
        "prov": ["kfm:prov:entity:ecology:example"],
    }


def test_validate_proof_pack_accepts_generated_pack() -> None:
    proof_pack = build_proof_pack(
        manifest=manifest(),
        manifest_ref="data/receipts/ecology/manifests/example.receipt_manifest.json",
        catalog_refs=catalog_refs(),
    )

    errors = validate_proof_pack(
        proof_pack=proof_pack,
        schema_path=SCHEMA_REF,
    )

    assert errors == []


def test_validate_proof_pack_reports_schema_errors() -> None:
    bad_pack = {
        "proof_pack_id": "kfm.proof.ecology.eco_index.example",
        "candidate_id": "eco_index.example",
        "candidate_type": "not_a_candidate_type",
        "spec_hash": "not-a-sha256",
        "manifest_ref": "manifest.json",
        "receipts": [],
        "catalog_refs": {
            "dcat": [],
            "stac": [],
            "prov": [],
        },
        "generated_at": "2026-04-24T00:00:00Z",
        "status": "not_complete",
    }

    errors = validate_proof_pack(
        proof_pack=bad_pack,
        schema_path=SCHEMA_REF,
    )

    assert errors
    assert any("candidate_type" in error for error in errors)
    assert any("spec_hash" in error for error in errors)
    assert any("receipts" in error for error in errors)
    assert any("catalog_refs.prov" in error for error in errors)
    assert any("status" in error for error in errors)


def test_validate_proof_pack_rejects_invalid_schema(tmp_path: Path) -> None:
    schema_path = tmp_path / "invalid_proof_pack_schema.json"
    write_json(
        schema_path,
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": 123,
        },
    )

    proof_pack = build_proof_pack(
        manifest=manifest(),
        manifest_ref="manifest.json",
        catalog_refs=catalog_refs(),
    )

    with pytest.raises(SchemaError):
        validate_proof_pack(
            proof_pack=proof_pack,
            schema_path=schema_path,
        )
