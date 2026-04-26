from __future__ import annotations

import json
from pathlib import Path

import pytest

pytest.importorskip("jsonschema")
from jsonschema import Draft202012Validator

from apps.governed_api.ecology.evidencebundle_resolver import (
    ResolverConfig,
    resolve_ecology_evidence_bundle,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
RUNTIME_ENVELOPE_SCHEMA_REF = Path(
    "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def proof_pack_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": True,
        "required": [
            "proof_pack_id",
            "candidate_id",
            "candidate_type",
            "spec_hash",
            "manifest_ref",
            "receipts",
            "catalog_refs",
            "generated_at",
            "status",
        ],
        "properties": {
            "proof_pack_id": {"type": "string"},
            "candidate_id": {"type": "string"},
            "candidate_type": {"type": "string"},
            "spec_hash": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
            "manifest_ref": {"type": "string"},
            "receipts": {"type": "array", "minItems": 1},
            "catalog_refs": {
                "type": "object",
                "required": ["prov"],
                "properties": {
                    "prov": {"type": "array", "minItems": 1}
                },
            },
            "generated_at": {"type": "string"},
            "status": {"const": "proof_complete"},
        },
    }


def proof_pack(candidate_id: str = "eco_index.example") -> dict:
    return {
        "proof_pack_id": f"kfm.proof.ecology.{candidate_id}",
        "candidate_id": candidate_id,
        "candidate_type": "eco_index",
        "spec_hash": SPEC_HASH,
        "manifest_ref": "data/receipts/ecology/manifests/example.receipt_manifest.json",
        "receipts": [
            {
                "receipt_type": "validator_result",
                "receipt_ref": "data/receipts/ecology/index/example.validator_receipt.json",
                "decision": "pass",
                "generated_at": "2026-04-24T00:00:00Z",
            }
        ],
        "catalog_refs": {
            "dcat": ["kfm:dcat:dataset:ecology:example"],
            "stac": ["kfm:stac:item:ecology:example"],
            "prov": ["kfm:prov:entity:ecology:example"],
        },
        "generated_at": "2026-04-24T00:00:00Z",
        "status": "proof_complete",
    }


def load_schema(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_runtime_envelope_valid(payload: dict) -> None:
    schema = load_schema(RUNTIME_ENVELOPE_SCHEMA_REF)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    errors = sorted(validator.iter_errors(payload), key=lambda item: list(item.path))

    assert errors == []


def config(tmp_path: Path) -> ResolverConfig:
    proof_root = tmp_path / "proofs"
    schema_path = tmp_path / "proof_pack.schema.json"

    write_json(schema_path, proof_pack_schema())

    return ResolverConfig(
        proof_root=proof_root,
        schema_path=schema_path,
    )


def test_cite_response_matches_runtime_envelope(tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    resolver_config = config(tmp_path)

    write_json(
        tmp_path / "proofs" / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    payload = resolve_ecology_evidence_bundle(
        candidate_id=candidate_id,
        config=resolver_config,
        expected_spec_hash=SPEC_HASH,
    )

    assert payload["data"]["decision"] == "cite"
    assert_runtime_envelope_valid(payload)


def test_abstain_response_matches_runtime_envelope(tmp_path: Path) -> None:
    payload = resolve_ecology_evidence_bundle(
        candidate_id="eco_index.missing",
        config=config(tmp_path),
    )

    assert payload["data"]["decision"] == "abstain"
    assert_runtime_envelope_valid(payload)
