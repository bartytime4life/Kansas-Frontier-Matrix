from __future__ import annotations

import json
from pathlib import Path

import pytest

pytest.importorskip("jsonschema")

from apps.governed_api.ecology import routes


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def schema() -> dict:
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


def configure_paths(monkeypatch, tmp_path: Path) -> tuple[Path, Path]:
    proof_root = tmp_path / "proofs"
    schema_path = tmp_path / "schema.json"

    monkeypatch.setattr(routes, "DEFAULT_PROOF_ROOT", proof_root)
    monkeypatch.setattr(routes, "DEFAULT_SCHEMA_PATH", schema_path)

    write_json(schema_path, schema())

    return proof_root, schema_path


def test_get_ecology_evidence_bundle_returns_cite(monkeypatch, tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    proof_root, _ = configure_paths(monkeypatch, tmp_path)

    write_json(
        proof_root / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    response = routes.get_ecology_evidence_bundle(
        candidate_id=candidate_id,
        spec_hash=SPEC_HASH,
    )

    assert response["status"] == "ok"
    assert response["data"]["decision"] == "cite"
    assert response["data"]["candidate_id"] == candidate_id
    assert response["data"]["spec_hash"] == SPEC_HASH
    assert "receipts" in response["data"]["evidence"]
    assert "catalog_refs" in response["data"]["evidence"]
    assert "uncertainty" in response["data"]


def test_get_ecology_evidence_bundle_can_hide_receipts(monkeypatch, tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    proof_root, _ = configure_paths(monkeypatch, tmp_path)

    write_json(
        proof_root / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    response = routes.get_ecology_evidence_bundle(
        candidate_id=candidate_id,
        include_receipts=False,
    )

    assert response["data"]["decision"] == "cite"
    assert "receipts" not in response["data"]["evidence"]
    assert "catalog_refs" in response["data"]["evidence"]


def test_get_ecology_evidence_bundle_can_hide_catalog_refs(monkeypatch, tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    proof_root, _ = configure_paths(monkeypatch, tmp_path)

    write_json(
        proof_root / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    response = routes.get_ecology_evidence_bundle(
        candidate_id=candidate_id,
        include_catalog_refs=False,
    )

    assert response["data"]["decision"] == "cite"
    assert "receipts" in response["data"]["evidence"]
    assert "catalog_refs" not in response["data"]["evidence"]


def test_get_ecology_evidence_bundle_can_hide_uncertainty(monkeypatch, tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    proof_root, _ = configure_paths(monkeypatch, tmp_path)

    write_json(
        proof_root / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    response = routes.get_ecology_evidence_bundle(
        candidate_id=candidate_id,
        include_uncertainty=False,
    )

    assert response["data"]["decision"] == "cite"
    assert "uncertainty" not in response["data"]


def test_get_ecology_evidence_bundle_abstains_for_missing_proof_pack(
    monkeypatch,
    tmp_path: Path,
) -> None:
    configure_paths(monkeypatch, tmp_path)

    response = routes.get_ecology_evidence_bundle(
        candidate_id="eco_index.missing",
    )

    assert response["status"] == "ok"
    assert response["data"]["decision"] == "abstain"
    assert response["data"]["reason"] == "proof_pack_missing"
