import json
import os
from pathlib import Path
from wsgiref.util import setup_testing_defaults

from governed_api.main import app
from governed_api.routes.registry import ROUTES
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


def _call_app(path: str, method: str = "GET"):
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = method
    environ["PATH_INFO"] = path

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
    assert payload["evidence_refs"] == []
    assert payload["policy_state"] == "unknown_fail_closed"
    assert payload["freshness"] == "unknown_fail_closed"
    assert payload["correction_state"] == "none"
    assert "precision_actually_used" not in payload
    assert "detail" not in payload
    assert_jsonschema_subset(payload, schema)


def test_unknown_route_returns_finite_404_error() -> None:
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


def test_non_get_methods_return_finite_405_errors() -> None:
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
