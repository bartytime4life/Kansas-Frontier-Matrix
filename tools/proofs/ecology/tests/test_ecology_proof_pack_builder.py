from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.proofs.ecology.ecology_proof_pack_builder import (
    build_proof_pack,
    load_json,
    write_proof_pack,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def manifest(*, decision: str = "ready_for_promotion", receipt_decision: str = "pass") -> dict:
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
                "decision": receipt_decision,
                "spec_hash": SPEC_HASH,
                "generated_at": "2026-04-24T00:00:00Z",
            }
        ],
        "decision": decision,
        "generated_at": "2026-04-24T00:00:00Z",
    }


def catalog_refs() -> dict:
    return {
        "dcat": ["kfm:dcat:dataset:ecology:example"],
        "stac": ["kfm:stac:item:ecology:example"],
        "prov": ["kfm:prov:entity:ecology:example"],
    }


def test_build_proof_pack_success() -> None:
    proof_pack = build_proof_pack(
        manifest=manifest(),
        manifest_ref="data/receipts/ecology/manifests/example.receipt_manifest.json",
        catalog_refs=catalog_refs(),
    )

    assert proof_pack["proof_pack_id"] == "kfm.proof.ecology.eco_index.example"
    assert proof_pack["candidate_id"] == "eco_index.example"
    assert proof_pack["candidate_type"] == "eco_index"
    assert proof_pack["spec_hash"] == SPEC_HASH
    assert proof_pack["manifest_ref"] == "data/receipts/ecology/manifests/example.receipt_manifest.json"
    assert proof_pack["catalog_refs"] == catalog_refs()
    assert proof_pack["status"] == "proof_complete"
    assert "generated_at" in proof_pack


def test_load_json_requires_object(tmp_path: Path) -> None:
    path = tmp_path / "array.json"
    path.write_text("[]\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Proof-pack input must be a JSON object"):
        load_json(path)


def test_write_proof_pack_creates_parent_directory(tmp_path: Path) -> None:
    proof_pack = build_proof_pack(
        manifest=manifest(),
        manifest_ref="manifest.json",
        catalog_refs=catalog_refs(),
    )

    out_path = tmp_path / "nested" / "proof_pack.json"
    write_proof_pack(out_path, proof_pack)

    assert out_path.exists()
    written = json.loads(out_path.read_text(encoding="utf-8"))
    assert written["status"] == "proof_complete"
