from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_DIR = REPO_ROOT / "tools/validators/governance"
if str(VALIDATOR_DIR) not in sys.path:
    sys.path.insert(0, str(VALIDATOR_DIR))

from validate_review_coverage_snapshot import (  # noqa: E402
    FIXTURE_PATH,
    finalize,
    run_fixture_cases,
    validate_document,
)


def _base() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))["base"]


def test_fixture_matrix_passes() -> None:
    assert run_fixture_cases() == []


def test_current_exact_head_is_current() -> None:
    result = validate_document(finalize(_base()))
    assert result.status == "PASS"
    assert result.coverage_outcome == "CURRENT"
    assert result.findings == ()


def test_stale_counted_review_is_stale() -> None:
    candidate = _base()
    candidate["reviews"][0]["reviewed_head_sha"] = "3" * 40
    result = validate_document(finalize(candidate))
    assert result.status == "PASS"
    assert result.coverage_outcome == "STALE"


def test_missing_required_role_holds() -> None:
    candidate = _base()
    candidate["requirements"]["required_roles"] = ["policy_steward", "release_authority"]
    result = validate_document(finalize(candidate))
    assert result.status == "PASS"
    assert result.coverage_outcome == "HOLD"


def test_independence_requirement_holds_when_not_declared() -> None:
    candidate = _base()
    candidate["reviews"][0]["independent"] = False
    result = validate_document(finalize(candidate))
    assert result.status == "PASS"
    assert result.coverage_outcome == "HOLD"


def test_forged_derived_state_is_denied() -> None:
    candidate = _base()
    candidate["reviews"][0]["reviewed_head_sha"] = "3" * 40
    candidate = finalize(candidate)
    candidate["outcome"] = "CURRENT"
    result = validate_document(candidate)
    assert result.status == "DENY"
    assert result.coverage_outcome == "STALE"
    assert any(item.code == "DERIVED_OUTCOME_MISMATCH" for item in result.findings)


def test_duplicate_review_refs_are_denied() -> None:
    candidate = _base()
    duplicate = copy.deepcopy(candidate["reviews"][0])
    candidate["reviews"].append(duplicate)
    result = validate_document(finalize(candidate))
    assert result.status == "DENY"
    assert any(item.code == "DUPLICATE_REVIEW_REF" for item in result.findings)
