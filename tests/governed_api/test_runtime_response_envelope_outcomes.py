from __future__ import annotations

import json
from pathlib import Path


FIXTURE_DIR = Path(__file__).parent / "fixtures"
VALID_OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURE_DIR / name).read_text(encoding="utf-8"))


def test_runtime_response_envelope_outcome_fixtures_are_finite() -> None:
    fixture_names = (
        "runtime_answer.valid.json",
        "runtime_abstain.valid.json",
        "runtime_deny.valid.json",
        "runtime_error.valid.json",
    )

    payloads = [load_fixture(name) for name in fixture_names]

    assert {payload["outcome"] for payload in payloads} == VALID_OUTCOMES
    for payload in payloads:
        assert payload["object_type"] == "RuntimeResponseEnvelope"
        assert payload["schema_version"] == "v1"
        assert payload["request_id"].startswith("req-")
