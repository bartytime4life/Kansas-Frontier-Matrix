from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/evidence/validate_non_detection_support_assessment.py"
SPEC = importlib.util.spec_from_file_location("non_detection_support_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads((REPO_ROOT / "schemas/contracts/v1/evidence/non_detection_support_assessment.schema.json").read_text())
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_exact_expected_size_and_polarity() -> None:
    cases = MODULE.fixture_cases()
    assert len(cases) == 12
    assert MODULE.fixture_profile() == 0


def test_supported_non_detection_is_scoped_and_cannot_mean_absence() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[0]
    assert result.outcome == "HOLD"
    assert candidate["assertion"]["statement_scope"] == "WITHIN_DECLARED_SAMPLING_EFFORT"
    assert "DO_NOT_INFER_ABSENCE" in candidate["assertion"]["obligations"]


def test_incomplete_effort_abstains_and_mismatch_is_denied() -> None:
    cases = MODULE.fixture_cases()
    incomplete, incomplete_result, _, _ = cases[2]
    assert incomplete["assertion"]["decision"] == "ABSTAIN"
    assert incomplete_result.outcome == "HOLD"
    mismatch_codes = {finding.code for finding in cases[6][1].findings}
    assert {"ASSERTION_STATE_MISMATCH", "ASSERTION_DECISION_MISMATCH"} <= mismatch_codes


def test_restricted_event_without_transform_fails_closed() -> None:
    codes = {finding.code for finding in MODULE.fixture_cases()[8][1].findings}
    assert "PRIVACY_TRANSFORM_REQUIRED" in codes


def test_identity_is_deterministic_and_tamper_evident() -> None:
    first = MODULE.fixture_cases()[0][0]
    second = MODULE.seal(first)
    assert first["spec_hash"] == second["spec_hash"]
    assert first["assessment_id"] == second["assessment_id"]
    tamper_codes = {finding.code for finding in MODULE.fixture_cases()[11][1].findings}
    assert {"SPEC_HASH_MISMATCH", "ASSESSMENT_ID_MISMATCH"} <= tamper_codes


def test_duplicate_keys_and_symlinks_are_denied_without_echoing_values(tmp_path: Path) -> None:
    sentinel = "SENSITIVE_SENTINEL_DO_NOT_ECHO"
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"subject_ref":"%s","subject_ref":"other"}' % sentinel)
    result = MODULE.validate_file(duplicate)
    assert result.outcome == "DENY"
    assert {finding.code for finding in result.findings} == {"INPUT_JSON_INVALID"}
    assert sentinel not in repr(result)

    target = tmp_path / "target.json"
    target.write_text("{}")
    link = tmp_path / "link.json"
    try:
        os.symlink(target, link)
    except (OSError, NotImplementedError):
        return
    assert {finding.code for finding in MODULE.validate_file(link).findings} == {"INPUT_JSON_INVALID"}


def test_validator_has_no_network_client_imports() -> None:
    source = MODULE_PATH.read_text(encoding="utf-8")
    forbidden = ("import requests", "import urllib", "import socket", "httpx", "aiohttp", "boto3")
    assert not any(token in source for token in forbidden)
