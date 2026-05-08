import json
from pathlib import Path

from fastapi.testclient import TestClient
from jsonschema import Draft202012Validator

from governed_api.main import app

SCHEMA_PATH = (
    Path(__file__).resolve().parents[3]
    / "schemas"
    / "contracts"
    / "v1"
    / "runtime"
    / "decision_envelope.schema.json"
)
ROUTES = ["/bootstrap", "/layers", "/evidence"]


def test_all_scaffolded_routes_abstain_and_validate() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    client = TestClient(app)

    for route in ROUTES:
        response = client.get(route)
        assert response.status_code == 200
        payload = response.json()
        assert payload["decision"] == "ABSTAIN"
        assert payload["reason_code"] == "NOT_IMPLEMENTED"
        assert payload["evidence_refs"] == []
        validator.validate(payload)
