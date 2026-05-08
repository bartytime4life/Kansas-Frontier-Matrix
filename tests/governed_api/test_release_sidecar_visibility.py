from __future__ import annotations
import pytest
pytest.importorskip("jsonschema", reason="jsonschema dependency unavailable in this environment")


import pytest
from fastapi.testclient import TestClient

from apps.api.server import app
from tests.governed_api.test_ecology_api import seed_public_safe_artifacts


@pytest.fixture()
def artifact_root(tmp_path, monkeypatch):
    root = tmp_path / "published" / "ecology" / "dry-run"
    root.mkdir(parents=True)

    monkeypatch.setenv("KFM_ECOLOGY_ARTIFACT_ROOT", str(root))

    import apps.api.server as server

    monkeypatch.setattr(server, "DEFAULT_ARTIFACT_ROOT", root)
    return root


@pytest.fixture()
def client(artifact_root):
    return TestClient(app)


def test_release_sidecar_references_visible_in_public_timeslice_response(client, artifact_root) -> None:
    seed_public_safe_artifacts(artifact_root)

    response = client.get("/ecology/timeslices/example-pass")

    assert response.status_code == 200
    payload = response.json()
    assert payload["evidence_bundle_ref"].startswith("kfm://evidence/")
    assert payload["run_receipt_ref"].startswith("kfm://receipt/run/")
    assert payload["promotion"]["decision_ref"].startswith("kfm://promotion/")
