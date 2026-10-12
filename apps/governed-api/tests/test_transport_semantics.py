"""Transport-status and response-header semantics for the governed API scaffold.

Kept separate from the reviewed boundary-guard inventory: these tests pin how
finite outcomes map to HTTP transport, not trust-boundary structure.
"""

import asyncio
import json
from pathlib import Path
from wsgiref.util import setup_testing_defaults

from governed_api.main import app
from governed_api.routes.registry import ROUTES
from governed_api.stub import make_fixture_failure_envelope
from schema_assert import assert_jsonschema_subset

SCHEMA_PATH = (
    Path(__file__).resolve().parents[3]
    / "schemas"
    / "contracts"
    / "v1"
    / "runtime"
    / "runtime_response_envelope.schema.json"
)


def _call_app_with_headers(path: str, method: str = "GET"):
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = method
    environ["PATH_INFO"] = path
    response = {}

    def start_response(status, headers):
        response["status"] = status
        response["headers"] = headers

    body = b"".join(app(environ, start_response))
    return response["status"], response["headers"], json.loads(body.decode("utf-8"))


def test_expected_negative_failures_are_not_generic_server_errors(monkeypatch) -> None:
    def times_out() -> dict:
        raise TimeoutError("upstream /private/store timed out")

    def cancelled() -> dict:
        raise asyncio.CancelledError()

    monkeypatch.setitem(ROUTES, "/evidence", times_out)
    status, _headers, payload = _call_app_with_headers("/evidence")
    assert status == "504 Gateway Timeout"
    assert payload["outcome"] == "ERROR"
    assert payload["reason_code"] == "REQUEST_TIMEOUT"
    assert "/private/store" not in json.dumps(payload)
    assert_jsonschema_subset(payload, json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    monkeypatch.setitem(ROUTES, "/evidence", cancelled)
    status, _headers, payload = _call_app_with_headers("/evidence")
    assert status == "503 Service Unavailable"
    assert payload["outcome"] == "ABSTAIN"
    assert payload["reason_code"] == "REQUEST_CANCELLED"
    assert_jsonschema_subset(payload, json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))


def test_intentional_deny_is_not_transported_as_server_error(monkeypatch) -> None:
    monkeypatch.setitem(
        ROUTES,
        "/evidence",
        lambda: make_fixture_failure_envelope("policy_denial", "fixture-deny-wsgi-001"),
    )
    status, _headers, payload = _call_app_with_headers("/evidence")
    assert status == "200 OK"
    assert payload["outcome"] == "DENY"
    assert payload["reason_code"] == "POLICY_DENIED"


def test_every_response_is_uncacheable_and_nosniff() -> None:
    for path, method in (
        ("/evidence", "GET"),
        ("/evidence", "POST"),
        ("/not-a-route", "GET"),
    ):
        _status, headers, _payload = _call_app_with_headers(path, method)
        header_map = dict(headers)
        assert header_map["Cache-Control"] == "no-store"
        assert header_map["X-Content-Type-Options"] == "nosniff"
        assert header_map["Content-Type"] == "application/json"


def test_method_not_allowed_advertises_get_only() -> None:
    for route in ROUTES:
        status, headers, _payload = _call_app_with_headers(route, "POST")
        assert status == "405 Method Not Allowed"
        assert dict(headers)["Allow"] == "GET"

    status, headers, _payload = _call_app_with_headers("/not-a-route", "POST")
    assert status == "404 Not Found"
    assert "Allow" not in dict(headers)
