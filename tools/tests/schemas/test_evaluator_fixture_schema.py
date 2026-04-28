from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA_REF = Path("tools/evaluators/fixtures/fixture.schema.json")


def load_schema(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(instance: dict) -> list[str]:
    schema = load_schema(SCHEMA_REF)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    return [
        f"{'.'.join(str(p) for p in e.path) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(instance), key=lambda i: list(i.path))
    ]


def valid_fixture() -> dict:
    return {
        "fixture_type": "kfm.evaluator_fixture.v1",
        "fixture_id": "runtime.valid.v1",
        "fixture_category": "positive",
        "subject_ref": "kfm://fixture/runtime/valid",
        "subject_type": "runtime_response",
        "expected_outcome": "ALLOW",
        "metric_results": [
            {
                "name": "schema_valid",
                "score": 1,
                "passed": True,
                "reason_code": "SCHEMA_VALID",
                "explanation": {"summary": "ok"},
            }
        ],
    }


def test_valid_fixture_passes() -> None:
    assert validate(valid_fixture()) == []


def test_missing_required_field_fails() -> None:
    instance = valid_fixture()
    instance.pop("subject_ref")

    errors = validate(instance)

    assert errors
    assert any("subject_ref" in error for error in errors)
