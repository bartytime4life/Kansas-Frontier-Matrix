from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/evidence/validate_temporal_support_assessment.py"
SPEC = importlib.util.spec_from_file_location("temporal_support_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads((REPO_ROOT / "schemas/contracts/v1/evidence/temporal_support_assessment.schema.json").read_text())
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_expected_polarity() -> None:
    assert MODULE.fixture_profile() == 0


def test_stale_supported_mismatch_is_rejected() -> None:
    path = REPO_ROOT / "fixtures/contracts/v1/evidence/temporal_support_assessment/invalid/stale_marked_supported.json"
    codes = {finding.code for finding in MODULE.validate(path).findings}
    assert "TEMPORAL_OUTCOME_MISMATCH" in codes


def test_corrected_release_requires_correction_reference() -> None:
    path = REPO_ROOT / "fixtures/contracts/v1/evidence/temporal_support_assessment/invalid/corrected_missing_reference.json"
    codes = {finding.code for finding in MODULE.validate(path).findings}
    assert "CORRECTION_REF_REQUIRED" in codes
