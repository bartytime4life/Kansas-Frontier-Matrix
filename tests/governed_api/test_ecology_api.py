from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from apps.governed_api.server import app


@pytest.fixture()
def artifact_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    root = tmp_path / "published" / "ecology" / "dry-run"
    root.mkdir(parents=True)

    monkeypatch.setenv("KFM_ECOLOGY_ARTIFACT_ROOT", str(root))

    # server.py reads env at import time, so patch module global too.
    import apps.governed_api.server as server

    monkeypatch.setattr(server, "DEFAULT_ARTIFACT_ROOT", root)

    return root


@pytest.fixture()
def client(artifact_root: Path) -> TestClient:
    return TestClient(app)


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def seed_public_safe_artifacts(root: Path) -> None:
    write_json(
        root / "tileset_metadata.json",
        {
            "schema_version": "v1",
            "object_type": "EcologyTilesetMetadata",
            "scheme": "xyz",
            "bounds": [-102.1, 36.9, -94.5, 40.1],
            "minzoom": 6,
            "maxzoom": 12,
            "time_start": "2024-06-18T00:00:00Z",
            "time_end": "2024-06-18T23:59:59Z",
            "expected_tile_count": 256,
            "produced_tile_count": 256,
            "kfm": {
                "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            },
            "evidence_bundle_url": "kfm://evidence/ecology/example-pass-timeslice",
            "provisional": False,
            "allowed_fields": ["class", "confidence", "time_start", "time_end"],
        },
    )

    write_json(
        root / "promotion_decision.json",
        {
            "schema_version": "v1",
            "object_type": "PromotionDecision",
            "decision_id": "kfm://promotion/ecology/example-pass",
            "candidate": "kfm://tileset/ecology/example-pass",
            "decision": "PROMOTE",
            "reasons": [],
            "requires_steward": False,
            "receipt_ref": "kfm://receipt/run/ecology/dry-run",
            "evidence_bundle_url": "kfm://evidence/ecology/example-pass-timeslice",
            "decided_at": "2024-06-18T00:00:00Z",
        },
    )

    write_json(
        root / "evidence_bundle.json",
        {
            "schema_version": "v1",
            "object_type": "EvidenceBundle",
            "bundle_id": "kfm://evidence/ecology/example-pass-timeslice",
            "domain": "ecology",
            "source_refs": ["kfm://source/ecology/no-network-fixture"],
            "dataset_refs": ["kfm://dataset/ecology/no-network-fixture"],
            "evidence_refs": ["kfm://evidence/ref/ecology/no-network-fixture"],
            "object_refs": ["kfm://tileset/ecology/example-pass"],
            "resolved": True,
            "evidence_bundle_resolved": True,
            "policy_label": "public",
            "rights_status": "open",
            "sensitivity": "public",
            "spec_hash": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
            "exact_geometry_present": False,
            "artifacts": [],
            "artifact_count": 0,
            "limitations": [],
            "notes": [],
        },
    )

    write_json(
        root / "stac_catalog.json",
        {
            "stac_version": "1.0.0",
            "type": "Catalog",
            "id": "kfm-ecology-catalog",
            "title": "KFM Ecology STAC Catalog",
            "description": "Governed KFM Ecology STAC catalog with receipt-backed collections.",
            "links": [
                {
                    "rel": "self",
                    "href": "kfm://catalog/stac",
                    "type": "application/json",
                    "title": "KFM Ecology STAC Catalog",
                }
            ],
            "kfm:domain": "ecology",
            "kfm:collection_count": 1,
        },
    )

    # ---------------------------
    # NEW: LAYER MANIFEST
    # ---------------------------
    write_json(
        root / "layer_manifest.json",
        {
            "schema_version": "v1",
            "object_type": "EcologyLayerManifest",
            "layer_id": "kfm://layer/ecology/example-pass",
            "title": "KFM Ecology Example Time Slice",
            "description": "Governed ecology time-slice layer derived from HLS/Landsat inputs.",
            "source_type": "vector",
            "tiles_url": "https://example.invalid/tiles/{z}/{x}/{y}.pbf",
            "source_layer": "ecology",
            "stac_catalog_ref": "kfm://catalog/stac",
            "stac_collection_ref": "kfm://catalog/stac/collections/kfm-ecology-timeslices",
            "stac_item_ref": "kfm://catalog/stac/items/kfm-ecology-example-pass",
            "evidence_bundle_ref": "kfm://evidence/ecology/example-pass-timeslice",
            "promotion_decision_ref": "kfm://promotion/ecology/example-pass",
            "run_receipt_ref": "kfm://receipt/run/ecology/dry-run",
            "bounds": [-102.1, 36.9, -94.5, 40.1],
            "time_start": "2024-06-18T00:00:00Z",
            "time_end": "2024-06-18T23:59:59Z",
            "minzoom": 0,
            "maxzoom": 14,
            "allowed_fields": ["class", "confidence", "time_start", "time_end"],
            "public_safe": True,
            "sensitivity": "public",
            "rights_status": "open",
            "policy_label": "public",
            "limitations": ["Derived classification layer"],
        },
    )

    write_json(
        root / "run_receipt.json",
        {
            "schema_version": "v1",
            "object_type": "run_receipt",
            "run_id": "kfm://run/ecology/dry-run",
            "receipt_ref": "kfm://receipt/run/ecology/dry-run",
            "spec_hash": "dry-run",
            "policy_results": [
                {
                    "policy": "policy/ecology/publication.rego",
                    "query": "data.ecology.publication.decision",
                    "result": "allow",
                }
            ],
            "promotion": {
                "decision_ref": "kfm://promotion/ecology/example-pass",
                "decision": "PROMOTE",
            },
            "catalog": {
                "stac_item": "/tmp/stac_item.json",
                "stac_collection": "/tmp/stac_collection.json",
                "stac_catalog": "/tmp/stac_catalog.json",
            },
        },
    )


def test_healthz(client: TestClient) -> None:
    response = client.get("/healthz")
    assert response.status_code == 200


def test_get_layer_public_safe(client: TestClient, artifact_root: Path) -> None:
    seed_public_safe_artifacts(artifact_root)

    response = client.get("/ecology/layers/example-pass")

    assert response.status_code == 200
    payload = response.json()
    assert payload["object_type"] == "EcologyLayerManifest"
    assert payload["layer_id"] == "kfm://layer/ecology/example-pass"


def test_get_layer_denied_not_public_safe(client: TestClient, artifact_root: Path) -> None:
    seed_public_safe_artifacts(artifact_root)

    path = artifact_root / "layer_manifest.json"
    data = json.loads(path.read_text())
    data["public_safe"] = False
    write_json(path, data)

    response = client.get("/ecology/layers/example-pass")

    assert response.status_code == 451
    payload = response.json()["detail"]
    assert payload["outcome"] == "DENY"
