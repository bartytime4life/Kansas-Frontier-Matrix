from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.proofs.ecology_proof_pack_builder import (
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


def test_proof_complete_manifest_is_allowed() -> None:
    proof_pack = build_proof_pack(
        manifest=manifest(decision="proof_complete"),
        manifest_ref="manifest.json",
        catalog_refs=catalog_refs(),
    )

    assert proof_pack["status"] == "proof_complete"


def test_non_promotable_manifest_fails() -> None:
    with pytest.raises(ValueError, match="manifest not promotable: not_ready"):
        build_proof_pack(
            manifest=manifest(decision="not_ready"),
            manifest_ref="manifest.json",
            catalog_refs=catalog_refs(),
        )


def test_failed_receipt_fails() -> None:
    with pytest.raises(ValueError, match="receipt not passing: fail"):
        build_proof_pack(
            manifest=manifest(receipt_decision="fail"),
            manifest_ref="manifest.json",
            catalog_refs=catalog_refs(),
        )


def test_receipt_spec_hash_mismatch_fails() -> None:
    value = manifest()
    value["receipts"][0]["spec_hash"] = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

    with pytest.raises(ValueError, match="receipt spec_hash mismatch"):
        build_proof_pack(
            manifest=value,
            manifest_ref="manifest.json",
            catalog_refs=catalog_refs(),
        )


def test_missing_prov_catalog_ref_fails() -> None:
    refs = {
        "dcat": ["kfm:dcat:dataset:ecology:example"],
        "stac": ["kfm:stac:item:ecology:example"],
        "prov": [],
    }

    with pytest.raises(ValueError, match="proof pack requires at least one PROV catalog reference"):
        build_proof_pack(
            manifest=manifest(),
            manifest_ref="manifest.json",
            catalog_refs=refs,
        )


def test_missing_candidate_id_fails() -> None:
    value = manifest()
    value.pop("candidate_id")

    with pytest.raises(ValueError, match="manifest missing candidate_id"):
        build_proof_pack(
            manifest=value,
            manifest_ref="manifest.json",
            catalog_refs=catalog_refs(),
        )


def test_empty_receipts_fail() -> None:
    value = manifest()
    value["receipts"] = []

    with pytest.raises(ValueError, match="manifest receipts must contain at least one receipt"):
        build_proof_pack(
            manifest=value,
            manifest_ref="manifest.json",
            catalog_refs=catalog_refs(),
        )


def test_non_object_receipt_entry_fails() -> None:
    value = manifest()
    value["receipts"] = ["not an object"]

    with pytest.raises(ValueError, match="manifest receipt entries must be JSON objects"):
        build_proof_pack(
            manifest=value,
            manifest_ref="manifest.json",
            catalog_refs=catalog_refs(),
        )


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


def test_load_json_requires_object(tmp_path: Path) -> None:
    path = tmp_path / "array.json"
    path.write_text("[]\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Proof-pack input must be a JSON object"):
        load_json(path)
