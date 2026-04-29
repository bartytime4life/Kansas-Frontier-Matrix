from __future__ import annotations

import pytest

pytest.importorskip("fastapi")

from fastapi.testclient import TestClient

from apps.governed_api.ecology import app as focus_app


def test_ecology_focus_returns_runtime_response(monkeypatch) -> None:
    expected = {"outcome": "ANSWER", "answer": "example"}

    def fake_answer(payload: dict) -> dict:
        assert payload == {"request_id": "kfm://request/ecology/example"}
        return expected

    monkeypatch.setattr(focus_app, "answer_focus_request", fake_answer)
    client = TestClient(focus_app.app)

    response = client.post(
        "/ecology/focus",
        json={"payload": {"request_id": "kfm://request/ecology/example"}},
    )

    assert response.status_code == 200
    assert response.json() == expected


def test_ecology_focus_wraps_runtime_errors(monkeypatch) -> None:
    def boom(_: dict) -> dict:
        raise RuntimeError("runtime failed")

    monkeypatch.setattr(focus_app, "answer_focus_request", boom)
    client = TestClient(focus_app.app)

    response = client.post("/ecology/focus", json={"payload": {}})

    assert response.status_code == 500
    assert response.json() == {"detail": "runtime failed"}
