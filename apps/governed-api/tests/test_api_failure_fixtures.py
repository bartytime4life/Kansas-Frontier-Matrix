import json
import os
from pathlib import Path

import pytest

from governed_api.stub import make_fixture_failure_envelope
from schema_assert import assert_jsonschema_subset

ROOT = Path(__file__).resolve().parents[3]
FIXTURES = ROOT / "apps" / "governed-api" / "tests" / "fixtures" / "api_failure_cases.json"
SCHEMA = ROOT / "schemas" / "contracts" / "v1" / "runtime" / "runtime_response_envelope.schema.json"


def test_failure_fixtures_are_deterministic_and_schema_valid() -> None:
    cases = json.loads(FIXTURES.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    previous = os.environ.get("GOVERNED_API_ISSUED_AT")
    os.environ["GOVERNED_API_ISSUED_AT"] = "2026-09-12T00:00:00+00:00"
    try:
        for case in cases:
            first = make_fixture_failure_envelope(case["kind"], case["correlation_id"])
            second = make_fixture_failure_envelope(case["kind"], case["correlation_id"])
            assert first == second
            assert first["outcome"] == case["outcome"]
            assert first["reason_code"] == case["reason_code"]
            assert first["id"].endswith(f":{case['correlation_id']}")
            assert set(first) == set(schema["required"])
            assert_jsonschema_subset(first, schema)
    finally:
        if previous is None:
            os.environ.pop("GOVERNED_API_ISSUED_AT", None)
        else:
            os.environ["GOVERNED_API_ISSUED_AT"] = previous


def test_abstain_and_deny_are_not_collapsed_to_error() -> None:
    cases = {case["kind"]: case for case in json.loads(FIXTURES.read_text(encoding="utf-8"))}
    assert make_fixture_failure_envelope("missing_evidence", cases["missing_evidence"]["correlation_id"])["outcome"] == "ABSTAIN"
    assert make_fixture_failure_envelope("policy_denial", cases["policy_denial"]["correlation_id"])["outcome"] == "DENY"


def test_invalid_correlation_is_not_reflected() -> None:
    payload = make_fixture_failure_envelope("internal_defect", "secret/path?stack=trace&token=redacted")
    assert payload["id"] == "fixture:failure:internal_defect:unavailable"
    assert "secret" not in json.dumps(payload)
    assert "stack" not in json.dumps(payload)
    assert "token" not in json.dumps(payload)


@pytest.mark.parametrize(
    ("kind", "expected_reason"),
    [
        ("malformed_input", "INVALID_REQUEST"),
        ("dependency_unavailable", "DEPENDENCY_UNAVAILABLE"),
        ("timeout", "REQUEST_TIMEOUT"),
        ("cancellation", "REQUEST_CANCELLED"),
    ],
)
def test_operational_failure_classes_have_safe_codes(kind: str, expected_reason: str) -> None:
    payload = make_fixture_failure_envelope(kind, "fixture-operational-001")
    assert payload["reason_code"] == expected_reason
    assert payload["outcome"] in {"ABSTAIN", "ERROR"}
