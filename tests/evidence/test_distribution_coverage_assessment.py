from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/evidence/validate_distribution_coverage_assessment.py"
SPEC = importlib.util.spec_from_file_location("distribution_coverage_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads(
        (REPO_ROOT / "schemas/contracts/v1/evidence/distribution_coverage_assessment.schema.json").read_text()
    )
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_exact_expected_size_and_polarity() -> None:
    cases = MODULE.fixture_cases()
    assert len(cases) == 15
    assert MODULE.fixture_profile() == 0


def test_missing_row_abstains_and_never_becomes_absence() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[6]
    assert result.outcome == "HOLD"
    assert candidate["source_assertion"]["row_state"] == "MISSING_ROW"
    assert candidate["coverage_assessment"]["decision"] == "ABSTAIN"
    assert "DO_NOT_TREAT_MISSING_AS_ABSENCE" in candidate["coverage_assessment"]["obligations"]


def test_explicit_absence_remains_source_scoped() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[1]
    assert result.outcome == "HOLD"
    assert candidate["coverage_assessment"]["statement_scope"] == "PINNED_SOURCE_GEOGRAPHY_VERSION_AND_TIME"
    assert "DO_NOT_INFER_TRUE_ABSENCE" in candidate["coverage_assessment"]["obligations"]


def test_changed_boundary_and_conflict_fail_closed() -> None:
    cases = MODULE.fixture_cases()
    changed, changed_result, _, _ = cases[7]
    conflicted, conflicted_result, _, _ = cases[9]
    assert changed["coverage_assessment"]["coverage_state"] == "GEOGRAPHY_UNRESOLVED"
    assert conflicted["coverage_assessment"]["coverage_state"] == "CONFLICTED"
    assert changed_result.outcome == conflicted_result.outcome == "HOLD"
    assert changed["coverage_assessment"]["decision"] == "ABSTAIN"
    assert conflicted["coverage_assessment"]["decision"] == "ABSTAIN"


def test_unsupported_first_observed_dates_are_denied() -> None:
    cases = MODULE.fixture_cases()
    unsupported_codes = {finding.code for finding in cases[11][1].findings}
    wrong_state_codes = {finding.code for finding in cases[12][1].findings}
    assert "FIRST_OBSERVED_SUPPORT_REQUIRED" in unsupported_codes
    assert "FIRST_OBSERVED_STATE_UNSUPPORTED" in wrong_state_codes


def test_identity_is_deterministic_and_tamper_evident() -> None:
    first = MODULE.fixture_cases()[0][0]
    second = MODULE.seal(first)
    assert first["spec_hash"] == second["spec_hash"]
    assert first["assessment_id"] == second["assessment_id"]
    tamper_codes = {finding.code for finding in MODULE.fixture_cases()[14][1].findings}
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
