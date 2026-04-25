from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.testclient import TestClient

from apps.governed_api.ecology import routes
from apps.governed_api.ecology.fastapi_routes import router


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


def make_client(monkeypatch, tmp_path: Path) -> TestClient:
    proof_root = tmp_path / "proofs"
    schema_path = tmp_path / "schema.json"

    monkeypatch.setattr(routes, "DEFAULT_PROOF_ROOT", proof_root)
    monkeypatch.setattr(routes, "DEFAULT_SCHEMA_PATH", schema_path)

    write_json(schema_path, schema())

    app = FastAPI()
    app.include_router(router)

    return TestClient(app)


def test_fastapi_route_returns_cite(monkeypatch, tmp_path: Path) -> None:
    candidate_id = "eco_index.example"
    client = make_client(monkeypatch, tmp_path)

    write_json(
        tmp_path / "proofs" / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    response = client.get(
        f"/v1/ecology/evidence-bundles/{candidate_id}",
        params={"spec_hash": SPEC_HASH},
    )

    assert response.status_code == 200

    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["data"]["decision"] == "cite"
    assert payload["data"]["candidate_id"] == candidate_id
    assert payload["data"]["spec_hash"] == SPEC_HASH


def test_fastapi_route_returns_abstain_for_missing_proof_pack(
    monkeypatch,
    tmp_path: Path,
) -> None:
    client = make_client(monkeypatch, tmp_path)

    response = client.get("/v1/ecology/evidence-bundles/eco_index.missing")

    assert response.status_code == 200

    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["data"]["decision"] == "abstain"
    assert payload["data"]["reason"] == "proof_pack_missing"


def test_fastapi_route_respects_include_receipts_false(
    monkeypatch,
    tmp_path: Path,
) -> None:
    candidate_id = "eco_index.example"
    client = make_client(monkeypatch, tmp_path)

    write_json(
        tmp_path / "proofs" / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    response = client.get(
        f"/v1/ecology/evidence-bundles/{candidate_id}",
        params={"include_receipts": "false"},
    )

    assert response.status_code == 200

    payload = response.json()
    assert payload["data"]["decision"] == "cite"
    assert "receipts" not in payload["data"]["evidence"]
    assert "catalog_refs" in payload["data"]["evidence"]


def test_fastapi_route_respects_include_catalog_refs_false(
    monkeypatch,
    tmp_path: Path,
) -> None:
    candidate_id = "eco_index.example"
    client = make_client(monkeypatch, tmp_path)

    write_json(
        tmp_path / "proofs" / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    response = client.get(
        f"/v1/ecology/evidence-bundles/{candidate_id}",
        params={"include_catalog_refs": "false"},
    )

    assert response.status_code == 200

    payload = response.json()
    assert payload["data"]["decision"] == "cite"
    assert "receipts" in payload["data"]["evidence"]
    assert "catalog_refs" not in payload["data"]["evidence"]


def test_fastapi_route_respects_include_uncertainty_false(
    monkeypatch,
    tmp_path: Path,
) -> None:
    candidate_id = "eco_index.example"
    client = make_client(monkeypatch, tmp_path)

    write_json(
        tmp_path / "proofs" / f"{candidate_id}.proof_pack.json",
        proof_pack(candidate_id=candidate_id),
    )

    response = client.get(
        f"/v1/ecology/evidence-bundles/{candidate_id}",
        params={"include_uncertainty": "false"},
    )

    assert response.status_code == 200

    payload = response.json()
    assert payload["data"]["decision"] == "cite"
    assert "uncertainty" not in payload["data"]
