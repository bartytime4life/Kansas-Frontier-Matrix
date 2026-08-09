from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/validate_claim_envelope.py"
SCHEMA = ROOT / "schemas/contracts/v1/evidence/claim_envelope.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/claim_envelope"
MANIFEST = FIXTURES / "expected_findings_manifest.json"

SPEC = importlib.util.spec_from_file_location("validate_claim_envelope", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _cases():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["cases"]


def test_schema_is_closed_and_names_validator():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    assert schema["additionalProperties"] is False
    assert schema["x-kfm"]["validator"] == "tools/validators/validate_claim_envelope.py"


def test_manifest_has_exact_reviewed_polarity():
    cases = _cases()
    assert len(cases) == 12
    assert {case["case_kind"] for case in cases} == {"VALID", "SCHEMA_NEGATIVE", "SEMANTIC_NEGATIVE"}


def test_exact_manifest_outcomes_and_findings():
    for case in _cases():
        result = MODULE.validate(FIXTURES / case["path"])
        assert result.outcome == case["expected_outcome"], case["case_id"]
        assert sorted({item.code for item in result.findings}) == sorted(case["expected_findings"]), case["case_id"]


def test_schema_and_semantic_negative_boundary():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for case in _cases():
        errors = list(validator.iter_errors(json.loads((FIXTURES / case["path"]).read_text(encoding="utf-8"))))
        if case["case_kind"] == "SCHEMA_NEGATIVE":
            assert errors, case["case_id"]
        elif case["case_kind"] == "SEMANTIC_NEGATIVE":
            assert not errors, case["case_id"]


def test_internal_reference_is_denied_without_value_echo():
    path = FIXTURES / "semantic_invalid/semantic_internal_reference.json"
    result = MODULE.validate(path)
    rendered = json.dumps([item.__dict__ for item in result.findings])
    assert "INTERNAL_REFERENCE_DENIED" in rendered
    assert "internal:evidence:secret" not in rendered


def test_duplicate_key_nonfinite_and_symlink_fail_closed():
    with tempfile.TemporaryDirectory() as directory:
        directory = Path(directory)
        duplicate = directory / "duplicate.json"
        nonfinite = directory / "nonfinite.json"
        duplicate.write_text('{"claim_id":"a","claim_id":"b"}', encoding="utf-8")
        nonfinite.write_text('{"claim_id":"a","value":NaN}', encoding="utf-8")
        assert {item.code for item in MODULE.validate(duplicate).findings} == {"JSON_DUPLICATE_KEY"}
        assert {item.code for item in MODULE.validate(nonfinite).findings} == {"JSON_NONFINITE_NUMBER"}
        target = directory / "target.json"
        link = directory / "link.json"
        target.write_text("{}", encoding="utf-8")
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            return
        assert {item.code for item in MODULE.validate(link).findings} == {"INPUT_SYMLINK_DENIED"}


def test_no_network_replay_and_cli_fixture_mode():
    with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network access attempted")), mock.patch.object(socket, "socket", side_effect=AssertionError("network access attempted")):
        first = [(case["case_id"], MODULE.validate(FIXTURES / case["path"])) for case in _cases()]
        second = [(case["case_id"], MODULE.validate(FIXTURES / case["path"])) for case in _cases()]
    assert first == second
    completed = subprocess.run([sys.executable, str(VALIDATOR), "--fixtures"], cwd=ROOT, text=True, capture_output=True, check=False)
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert "CLAIM_ENVELOPE_FIXTURES_VALID cases=12" in completed.stdout


def test_cli_exit_codes_are_finite():
    cases = [
        (FIXTURES / "valid/valid_supported_draft.json", 0),
        (FIXTURES / "semantic_invalid/semantic_internal_reference.json", 1),
        (ROOT / "missing.json", 2),
    ]
    for path, expected in cases:
        completed = subprocess.run([sys.executable, str(VALIDATOR), str(path)], cwd=ROOT, text=True, capture_output=True, check=False)
        assert completed.returncode == expected, completed.stdout + completed.stderr
