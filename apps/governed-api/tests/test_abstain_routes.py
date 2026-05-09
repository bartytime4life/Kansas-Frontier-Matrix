import os
import json
from pathlib import Path
from wsgiref.util import setup_testing_defaults

from governed_api.main import app
from governed_api.routes.registry import ROUTES

SCHEMA_PATH = (
    Path(__file__).resolve().parents[3]
    / "schemas"
    / "contracts"
    / "v1"
    / "runtime"
    / "decision_envelope.schema.json"
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


from schema_assert import assert_jsonschema_subset


def test_all_scaffolded_routes_abstain_and_validate() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    assert ROUTES, "Expected at least one scaffolded route in routes.registry.ROUTES"

    fixed_time = "2026-05-09T00:00:00+00:00"
    previous = os.environ.get("GOVERNED_API_ISSUED_AT")
    os.environ["GOVERNED_API_ISSUED_AT"] = fixed_time
    try:
        for route in sorted(ROUTES):
            status, payload = _call_app(route)
            assert status == "200 OK"
            assert payload["decision"] == "ABSTAIN"
            assert payload["reason_code"] == "NOT_IMPLEMENTED"
            assert payload["evidence_refs"] == []
            assert payload["spec_hash"] == "stub:abstain"
            assert payload["id"] == f"stub:{route.removeprefix('/')}"
            assert payload["version"] == "v1-stub"
            assert payload["issued_at"] == fixed_time
            assert_jsonschema_subset(payload, schema)
    finally:
        if previous is None:
            os.environ.pop("GOVERNED_API_ISSUED_AT", None)
        else:
            os.environ["GOVERNED_API_ISSUED_AT"] = previous
