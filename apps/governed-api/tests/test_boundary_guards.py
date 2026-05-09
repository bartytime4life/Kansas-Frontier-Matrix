from pathlib import Path
from wsgiref.util import setup_testing_defaults
import json

from governed_api.main import app


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


def test_unknown_route_returns_404() -> None:
    status, payload = _call_app("/not-a-route")
    assert status == "404 Not Found"
    assert payload == {"detail": "Not Found"}


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
