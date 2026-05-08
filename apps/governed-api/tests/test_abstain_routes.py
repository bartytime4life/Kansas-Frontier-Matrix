import importlib
import json
import pkgutil
from pathlib import Path
from wsgiref.util import setup_testing_defaults

from governed_api.main import app
import governed_api.routes as routes_pkg

SCHEMA_PATH = (
    Path(__file__).resolve().parents[3]
    / "schemas"
    / "contracts"
    / "v1"
    / "runtime"
    / "decision_envelope.schema.json"
)


def _discover_scaffolded_routes() -> list[str]:
    routes: list[str] = []
    for module_info in pkgutil.iter_modules(routes_pkg.__path__):
        if module_info.name.startswith("_"):
            continue
        mod = importlib.import_module(f"{routes_pkg.__name__}.{module_info.name}")
        path = getattr(mod, "PATH", None)
        if path:
            routes.append(path)
    return sorted(routes)


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


def _validate_against_schema(payload: dict, schema: dict) -> None:
    assert schema.get("type") == "object"
    assert isinstance(payload, dict)
    for field in schema.get("required", []):
        assert field in payload


def test_all_scaffolded_routes_abstain_and_validate() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    routes = _discover_scaffolded_routes()
    assert routes, "Expected at least one scaffolded route module in governed_api.routes"

    for route in routes:
        status, payload = _call_app(route)
        assert status == "200 OK"
        assert payload["decision"] == "ABSTAIN"
        assert payload["reason_code"] == "NOT_IMPLEMENTED"
        assert payload["evidence_refs"] == []
        assert payload["spec_hash"] == "stub:abstain"
        assert payload["id"] == f"stub:{route.removeprefix('/')}"
        assert payload["version"] == "v1-stub"
        assert isinstance(payload["issued_at"], str) and payload["issued_at"]
        _validate_against_schema(payload, schema)
