import json
import os
from pathlib import Path
from wsgiref.util import setup_testing_defaults

from governed_api.main import app
from schema_assert import assert_jsonschema_subset

SCHEMA_PATH = (
    Path(__file__).resolve().parents[3]
    / "schemas"
    / "contracts"
    / "v1"
    / "runtime"
    / "runtime_response_envelope.schema.json"
)


def _call_app(path: str):
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = "GET"
    environ["PATH_INFO"] = path

    status_holder = {}

    def start_response(status, headers):
        status_holder["status"] = status
        status_holder["headers"] = headers

    body_chunks = app(environ, start_response)
    body = b"".join(body_chunks)
    return status_holder["status"], json.loads(body.decode("utf-8"))


def test_unchanged_bootstrap_route_abstains_and_validates() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    expected_keys = set(schema["required"])

    fixed_time = "2026-05-09T00:00:00+00:00"
    previous = os.environ.get("GOVERNED_API_ISSUED_AT")
    os.environ["GOVERNED_API_ISSUED_AT"] = fixed_time
    try:
        status, payload = _call_app("/bootstrap")
        assert status == "200 OK"
        assert payload["outcome"] == "ABSTAIN"
        assert payload["reason_code"] == "NOT_IMPLEMENTED"
        assert payload["evidence_refs"] == []
        assert payload["spec_hash"] == "sha256:" + "a" * 64
        assert payload["id"] == "stub:bootstrap"
        assert payload["version"] == "v1-stub"
        assert payload["issued_at"] == fixed_time
        assert payload["policy_state"] == "baseline"
        assert payload["freshness"] == "current"
        assert payload["correction_state"] == "none"
        assert set(payload) == expected_keys
        assert "decision" not in payload
        assert "decision_id" not in payload
        assert "precision_actually_used" not in payload
        assert_jsonschema_subset(payload, schema)
    finally:
        if previous is None:
            os.environ.pop("GOVERNED_API_ISSUED_AT", None)
        else:
            os.environ["GOVERNED_API_ISSUED_AT"] = previous
