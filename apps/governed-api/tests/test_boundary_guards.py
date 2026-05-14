from pathlib import Path
from wsgiref.util import setup_testing_defaults
import json

from governed_api.main import app
from governed_api.routes.registry import ROUTES
from tests.policy.boundary_constants import FORBIDDEN_INTERNAL_STORE_PATHS


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


def test_unknown_route_returns_404() -> None:
    status, payload = _call_app("/not-a-route")
    assert status == "404 Not Found"
    assert payload == {"detail": "Not Found"}


def test_non_get_methods_rejected_for_scaffolded_routes() -> None:
    for route in ROUTES:
        for method in ("POST", "PUT", "DELETE"):
            status, payload = _call_app(route, method=method)
            assert status == "405 Method Not Allowed"
            assert payload == {"detail": "Method Not Allowed"}


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
