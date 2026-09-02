from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.evidence import validate_distribution_coverage_assessment as validator

ROOT = Path(__file__).resolve().parents[2]


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads(validator.SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


def test_exact_fixture_matrix() -> None:
    cases = validator.fixture_cases()
    assert len(cases) == 20
    for _candidate, result, expected_outcome, expected_findings in cases:
        assert result.outcome == expected_outcome
        assert set(expected_findings) <= {finding.code for finding in result.findings}


def test_all_eight_finite_states_have_coherent_cases() -> None:
    coherent = [candidate for candidate, result, _, _ in validator.fixture_cases() if result.coherent]
    assert {
        "PRESENT", "EXPLICITLY_ABSENT", "NOT_ASSESSED", "UNKNOWN",
        "SUPPRESSED", "DISPUTED", "STALE", "OUT_OF_SCOPE",
    } <= {candidate["distribution_assertion"]["status"] for candidate in coherent}


def test_missing_row_never_derives_explicit_absence() -> None:
    candidate = copy.deepcopy(validator.fixture_cases()[0][0])
    candidate["coverage_assessment"].update({
        "source_row_state": "MISSING",
        "source_native_status": None,
        "mapping_basis": "NO_EXPLICIT_STATUS",
    })
    status, decision, reason, obligation = validator.derive(candidate)
    assert (status, decision, reason, obligation) == (
        "UNKNOWN", "ABSTAIN", "SOURCE_ROW_MISSING", "DO_NOT_INFER_ABSENCE"
    )


def test_identity_is_deterministic_and_tamper_evident() -> None:
    matrix = validator.load_json_file(validator.CASES_PATH)
    first = validator.seal(matrix["base"])
    second = validator.seal(json.loads(json.dumps(matrix["base"])))
    assert first["spec_hash"] == second["spec_hash"]
    assert first["assessment_id"] == second["assessment_id"]
    tamper_codes = {finding.code for finding in validator.fixture_cases()[-1][1].findings}
    assert {"SPEC_HASH_MISMATCH", "ASSESSMENT_ID_MISMATCH"} <= tamper_codes


def test_validation_opens_no_network() -> None:
    candidate = validator.fixture_cases()[0][0]
    with mock.patch("socket.socket", side_effect=AssertionError("network denied")):
        assert validator.validate_document(candidate).coherent
    source = Path(validator.__file__).read_text(encoding="utf-8")
    for token in ("import requests", "import urllib", "import socket", "httpx", "aiohttp", "boto3"):
        assert token not in source


def test_cli_fixture_replay_is_deterministic() -> None:
    command = [sys.executable, str(Path(validator.__file__)), "--fixtures"]
    first = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
    second = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
    assert first.returncode == 0, first.stderr
    assert first.stdout == second.stdout
    assert '"cases":20' in first.stdout
    assert '"status":"PASS"' in first.stdout


def test_unsafe_json_inputs_fail_closed() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        duplicate = root / "duplicate.json"
        duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
        nonfinite = root / "nonfinite.json"
        nonfinite.write_text('{"a":NaN}', encoding="utf-8")
        target = root / "target.json"
        target.write_text("{}", encoding="utf-8")
        link = root / "link.json"
        link.symlink_to(target)
        for path in (duplicate, nonfinite, link):
            result = validator.validate_file(path)
            assert result.outcome == "DENY"
            assert result.findings[0].code == "INPUT_JSON_INVALID"
