import json
import os
from pathlib import Path
from wsgiref.util import setup_testing_defaults

from governed_api.main import app
from governed_api.routes.registry import ROUTES
from governed_api.stub import make_fixture_failure_envelope
from schema_assert import assert_jsonschema_subset
from tests.policy.boundary_constants import FORBIDDEN_INTERNAL_STORE_PATHS

SCHEMA_PATH = (
    Path(__file__).resolve().parents[3]
    / "schemas"
    / "contracts"
    / "v1"
    / "runtime"
    / "runtime_response_envelope.schema.json"
)


def _call_app(path: str, method: str = "GET", **environ_updates):
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = method
    environ["PATH_INFO"] = path
    environ.update(environ_updates)

    status_holder = {}

    def start_response(status, headers):
        status_holder["status"] = status
        status_holder["headers"] = headers

    body_chunks = app(environ, start_response)
    body = b"".join(body_chunks)
    return status_holder["status"], json.loads(body.decode("utf-8"))


def _assert_safe_error_envelope(payload: dict, expected_id: str) -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    assert set(payload) == set(schema["required"])
    assert payload["id"] == expected_id
    assert payload["spec_hash"] == "sha256:" + "a" * 64
    assert payload["version"] == "v1-stub"
    assert payload["outcome"] == "ERROR"
    assert payload["reason_code"] == "SAFE_RUNTIME_ERROR"
    assert_jsonschema_subset(payload, json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))
    assert payload["evidence_refs"] == []
    assert payload["policy_state"] == "unknown_fail_closed"
    assert payload["freshness"] == "unknown_fail_closed"
    assert payload["correction_state"] == "none"
    assert "precision_actually_used" not in payload
    assert "detail" not in payload
    assert_jsonschema_subset(payload, schema)


def test_unknown_route_returns_404() -> None:
    fixed_time = "2026-05-09T00:00:00+00:00"
    previous = os.environ.get("GOVERNED_API_ISSUED_AT")
    os.environ["GOVERNED_API_ISSUED_AT"] = fixed_time
    try:
        status, payload = _call_app("/not-a-route")
        assert status == "404 Not Found"
        assert payload["issued_at"] == fixed_time
        _assert_safe_error_envelope(payload, "stub:error:route-not-found")
    finally:
        if previous is None:
            os.environ.pop("GOVERNED_API_ISSUED_AT", None)
        else:
            os.environ["GOVERNED_API_ISSUED_AT"] = previous


def test_non_get_methods_rejected_for_scaffolded_routes() -> None:
    fixed_time = "2026-05-09T00:00:00+00:00"
    previous = os.environ.get("GOVERNED_API_ISSUED_AT")
    os.environ["GOVERNED_API_ISSUED_AT"] = fixed_time
    try:
        for route in ROUTES:
            for method in ("POST", "PUT", "DELETE"):
                status, payload = _call_app(route, method=method)
                assert status == "405 Method Not Allowed"
                assert payload["issued_at"] == fixed_time
                _assert_safe_error_envelope(payload, "stub:error:method-not-allowed")
    finally:
        if previous is None:
            os.environ.pop("GOVERNED_API_ISSUED_AT", None)
        else:
            os.environ["GOVERNED_API_ISSUED_AT"] = previous


def test_forbidden_runtime_imports_absent() -> None:
    root = Path(__file__).resolve().parents[1]
    bad_prefixes = (
        "import maplibre",
        "from maplibre",
        "import cesium",
        "from cesium",
        "import ollama",
        "from ollama",
    )

    for py_file in root.rglob("*.py"):
        text = py_file.read_text(encoding="utf-8")
        for line in text.splitlines():
            stripped = line.strip()
            assert not stripped.startswith(bad_prefixes), f"Forbidden import in {py_file}: {line}"


def test_api_surface_manifest() -> None:
    expected_routes = {"/bootstrap", "/layers", "/evidence"}
    assert set(ROUTES.keys()) == expected_routes


def test_no_internal_data_store_path_literals_in_api_code() -> None:
    root = Path(__file__).resolve().parents[1] / "src"
    for py_file in root.rglob("*.py"):
        text = py_file.read_text(encoding="utf-8")
        for marker in FORBIDDEN_INTERNAL_STORE_PATHS:
            assert marker not in text, f"Forbidden internal-store reference in {py_file}: {marker}"


def test_registered_route_exception_returns_safe_correlated_error(monkeypatch) -> None:
    def raises_secret() -> dict:
        raise RuntimeError("/private/store token=never-reflect")

    monkeypatch.setitem(ROUTES, "/evidence", raises_secret)
    status, payload = _call_app(
        "/evidence",
        **{"kfm.correlation_id": "fixture-wsgi-001"},
    )

    assert status == "500 Internal Server Error"
    assert payload["id"] == "fixture:failure:internal_defect:fixture-wsgi-001"
    assert payload["outcome"] == "ERROR"
    assert payload["reason_code"] == "SAFE_RUNTIME_ERROR"
    assert "/private/store" not in json.dumps(payload)
    assert "never-reflect" not in json.dumps(payload)


def test_registered_route_invalid_or_error_response_uses_500(monkeypatch) -> None:
    monkeypatch.setitem(ROUTES, "/evidence", lambda: {"outcome": "ANSWER", "payload": "unsupported"})
    status, payload = _call_app(
        "/evidence",
        **{"kfm.correlation_id": "fixture-invalid-wsgi-001"},
    )

    assert status == "500 Internal Server Error"
    assert payload["id"] == "fixture:failure:invalid_response:fixture-invalid-wsgi-001"
    assert payload["outcome"] == "ERROR"
    assert payload["reason_code"] == "INVALID_RESPONSE"
    assert "payload" not in payload
    assert_jsonschema_subset(payload, json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    monkeypatch.setitem(
        ROUTES,
        "/evidence",
        lambda: make_fixture_failure_envelope("dependency_unavailable", "fixture-handler-error-001"),
    )
    status, payload = _call_app("/evidence")

    assert status == "500 Internal Server Error"
    assert payload["outcome"] == "ERROR"
    assert payload["reason_code"] == "DEPENDENCY_UNAVAILABLE"
    assert_jsonschema_subset(payload, json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))


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
    import asyncio

    def times_out() -> dict:
        raise TimeoutError("upstream /private/store timed out")

    def cancelled() -> dict:
        raise asyncio.CancelledError()

    monkeypatch.setitem(ROUTES, "/evidence", times_out)
    status, payload = _call_app("/evidence", **{"kfm.correlation_id": "fixture-timeout-001"})
    assert status == "504 Gateway Timeout"
    assert payload["outcome"] == "ERROR"
    assert payload["reason_code"] == "REQUEST_TIMEOUT"
    assert "/private/store" not in json.dumps(payload)
    assert_jsonschema_subset(payload, json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    monkeypatch.setitem(ROUTES, "/evidence", cancelled)
    status, payload = _call_app("/evidence", **{"kfm.correlation_id": "fixture-cancel-001"})
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
    status, payload = _call_app("/evidence")
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
