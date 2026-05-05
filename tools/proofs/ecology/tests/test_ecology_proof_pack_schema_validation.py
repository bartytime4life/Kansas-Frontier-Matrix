from __future__ import annotations

from pathlib import Path

from tools.proofs.ecology.ecology_proof_pack_builder import (
    build_proof_pack,
    validate_proof_pack,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SCHEMA_REF = Path("schemas/ecology/ecology_proof_pack.schema.json")


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
