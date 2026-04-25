from __future__ import annotations

import json
from pathlib import Path

import pytest

pytest.importorskip("jsonschema")
from jsonschema import Draft202012Validator

from apps.governed_api.ecology import routes


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SCHEMA_PATH = Path("schemas/contracts/v1/runtime/ecology_evidence_bundle_response.schema.json")


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
            "catalog_refs": {"type": "object"},
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
            "prov": ["kfm:prov:entity:ecology:example"],
        },
        "generated_at": "2026-04-24T00:00:00Z",
        "status": "proof_complete",
    }


def configure_paths(monkeypatch, tmp_path: Path) -> Path:
    proof_root = tmp_path / "proofs"
    schema_path = tmp_path / "proof_pack.schema.json"
    monkeypatch.setattr(routes, "DEFAULT_PROOF_ROOT", proof_root)
    monkeypatch.setattr(routes, "DEFAULT_SCHEMA_PATH", schema_path)
    write_json(schema_path, proof_pack_schema())
    return proof_root


def validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_route_cite_payload_matches_contract_schema(monkeypatch, tmp_path: Path) -> None:
    proof_root = configure_paths(monkeypatch, tmp_path)
    candidate_id = "eco_index.example"
    write_json(proof_root / f"{candidate_id}.proof_pack.json", proof_pack(candidate_id))

    payload = routes.get_ecology_evidence_bundle(candidate_id=candidate_id, spec_hash=SPEC_HASH)

    errors = sorted(validator().iter_errors(payload), key=lambda err: list(err.path))
    assert errors == []


def test_route_abstain_payload_matches_contract_schema(monkeypatch, tmp_path: Path) -> None:
    configure_paths(monkeypatch, tmp_path)
    payload = routes.get_ecology_evidence_bundle(candidate_id="eco_index.missing")

    errors = sorted(validator().iter_errors(payload), key=lambda err: list(err.path))
    assert errors == []


def test_route_contract_negative_missing_candidate_id_is_rejected(monkeypatch, tmp_path: Path) -> None:
    proof_root = configure_paths(monkeypatch, tmp_path)
    candidate_id = "eco_index.example"
    write_json(proof_root / f"{candidate_id}.proof_pack.json", proof_pack(candidate_id))
    payload = routes.get_ecology_evidence_bundle(candidate_id=candidate_id, spec_hash=SPEC_HASH)

    del payload["data"]["candidate_id"]
    errors = sorted(validator().iter_errors(payload), key=lambda err: list(err.path))

    assert errors
    assert any("'candidate_id' is a required property" in err.message for err in errors)
