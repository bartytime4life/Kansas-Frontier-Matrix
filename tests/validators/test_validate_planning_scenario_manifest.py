from __future__ import annotations

import copy
import json
import socket
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.domains.water_planning import validate_planning_scenario_manifest as module

ROOT = Path(__file__).resolve().parents[2]


def _base() -> dict[str, object]:
    return json.loads(module.VALID_FIXTURE.read_text(encoding="utf-8"))


def test_schema_is_valid_draft_2020_12():
    schema = json.loads(module.SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


def test_synthetic_kansas_pilot_passes():
    assert module.validate(_base()) == ("PASS", [])


def test_schema_negative_fails_closed():
    document = json.loads(module.INVALID_FIXTURE.read_text(encoding="utf-8"))
    assert module.validate(document) == ("FAIL", ["SCHEMA_INVALID"])


def test_exact_fixture_matrix_passes():
    assert module.run_fixtures() == 0


def test_spec_hash_binds_manifest_body():
    document = _base()
    original = module.expected_spec_hash(document)
    document["purpose"] = "A different bounded synthetic purpose."
    assert module.expected_spec_hash(document) != original


def test_ready_for_review_requires_review_and_policy_bindings():
    document = _base()
    document["status"] = "READY_FOR_REVIEW"
    document["spec_hash"] = module.expected_spec_hash(document)
    outcome, findings = module.validate(document)
    assert outcome == "FAIL"
    assert findings == ["READY_REVIEW_BINDINGS_REQUIRED"]


def test_validation_is_no_network(monkeypatch):
    def denied(*_args, **_kwargs):
        raise AssertionError("network access is outside validator scope")

    monkeypatch.setattr(socket, "socket", denied)
    assert module.validate(_base()) == ("PASS", [])


def test_cli_output_is_finite_and_does_not_echo_payload(tmp_path):
    document = _base()
    document["public_summary"]["text"] = "PROTECTED_FIXTURE_VALUE"
    document["spec_hash"] = module.expected_spec_hash(document)
    candidate = tmp_path / "candidate.json"
    candidate.write_text(json.dumps(document), encoding="utf-8")
    completed = subprocess.run(
        [sys.executable, str(module.__file__), str(candidate)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert completed.stdout == '{"findings":[],"outcome":"PASS"}\n'
    assert "PROTECTED_FIXTURE_VALUE" not in completed.stdout + completed.stderr


def test_mutations_do_not_change_base_fixture():
    base = _base()
    before = copy.deepcopy(base)
    module.mutate(base, {"drawer_payload.outcome": "DENY"})
    assert base == before
