from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from apps.governed_api.server import app
from tests.governed_api.test_ecology_api import seed_public_safe_artifacts, write_json


@pytest.fixture()
def artifact_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    root = tmp_path / "published" / "ecology" / "dry-run"
    root.mkdir(parents=True)

    monkeypatch.setenv("KFM_ECOLOGY_ARTIFACT_ROOT", str(root))

    import apps.governed_api.server as server

    monkeypatch.setattr(server, "DEFAULT_ARTIFACT_ROOT", root)
    return root


@pytest.fixture()
def client(artifact_root: Path) -> TestClient:
    return TestClient(app)


def test_policy_denial_visible_at_boundary(client: TestClient, artifact_root: Path) -> None:
    seed_public_safe_artifacts(artifact_root)

    receipt_path = artifact_root / "run_receipt.json"
    payload = json.loads(receipt_path.read_text(encoding="utf-8"))
    payload["policy_results"][0]["result"] = "deny"
    payload["policy_results"][0]["reasons"] = ["classification_policy_block"]
    write_json(receipt_path, payload)

    response = client.get("/ecology/timeslices/example-pass")

    assert response.status_code == 451
    detail = response.json()["detail"]
    assert detail["outcome"] == "DENY"
    assert "classification_policy_block" in detail["reasons"]
    assert detail["policy_ref"] == "policy/ecology/publication.rego"
