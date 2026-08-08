from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/source_role/validate_source_role_transition_assessment.py"
SPEC = importlib.util.spec_from_file_location("source_role_transition_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads((REPO_ROOT / "schemas/contracts/v1/source/source_role_transition_assessment.schema.json").read_text())
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_expected_polarity() -> None:
    assert MODULE.fixture_profile() == 0


def test_modeled_as_observed_is_denied() -> None:
    path = REPO_ROOT / "fixtures/contracts/v1/source/source_role_transition_assessment/invalid/modeled_as_observed_marked_pass.json"
    codes = {finding.code for finding in MODULE.validate(path).findings}
    assert "SOURCE_ROLE_OUTCOME_MISMATCH" in codes
    assert "SOURCE_ROLE_REASON_REQUIRED" in codes


def test_candidate_promotion_hold_is_valid() -> None:
    path = REPO_ROOT / "fixtures/contracts/v1/source/source_role_transition_assessment/valid/candidate_promotion_hold.json"
    assert MODULE.validate(path).ok
