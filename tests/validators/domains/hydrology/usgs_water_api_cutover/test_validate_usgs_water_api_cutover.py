"""Tests for the fixture-only USGS Water API cutover assessment."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO_ROOT / (
    "tools/validators/domains/hydrology/usgs_water_api_cutover/"
    "validate_usgs_water_api_cutover.py"
)
FIXTURES = REPO_ROOT / "fixtures/domains/hydrology/usgs_water_api_cutover/valid"

SPEC = importlib.util.spec_from_file_location("kfm_usgs_water_cutover", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _fixture(name: str) -> dict[str, object]:
    value = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _rehash(payload: dict[str, object]) -> None:
    payload["spec_hash"] = MODULE.canonical_spec_hash(payload)


def _set_expected_decision(payload: dict[str, object]) -> None:
    reasons = MODULE.expected_reasons(payload)
    payload["decision"] = {
        "outcome": MODULE.expected_outcome(reasons),
        "reasons": reasons,
    }
    _rehash(payload)


def test_cutover_candidate_is_valid_and_deterministic() -> None:
    payload = _fixture("cutover_candidate.json")

    first = MODULE.validate_payload(payload)
    second = MODULE.validate_payload(copy.deepcopy(payload))

    assert first == second
    assert first.ok
    assert payload["decision"] == {"outcome": "CUTOVER_CANDIDATE", "reasons": []}


def test_dual_run_missing_reconciliation_is_a_valid_hold() -> None:
    payload = _fixture("dual_run_hold.json")

    result = MODULE.validate_payload(payload)

    assert result.ok
    assert payload["decision"]["outcome"] == "HOLD"


def test_legacy_only_reliance_is_a_valid_deny() -> None:
    payload = _fixture("legacy_only_denied.json")

    result = MODULE.validate_payload(payload)

    assert result.ok
    assert payload["decision"]["outcome"] == "DENY"


def test_missing_modern_role_cannot_remain_cutover_candidate() -> None:
    payload = _fixture("cutover_candidate.json")
    payload["endpoint_profiles"] = [
        item for item in payload["endpoint_profiles"] if item["role"] != "daily"
    ]
    payload["migration"]["modern_coverage"].remove("daily")
    _rehash(payload)

    result = MODULE.validate_payload(payload)

    assert not result.ok
    assert MODULE.Finding(
        "DECISION_REASONS_MISMATCH", "/decision/reasons"
    ) in result.findings
    assert MODULE.Finding(
        "DECISION_OUTCOME_MISMATCH", "/decision/outcome"
    ) in result.findings


def test_denied_source_descriptor_requires_deny() -> None:
    payload = _fixture("cutover_candidate.json")
    payload["source_descriptor_state"] = "DENIED"
    _rehash(payload)

    result = MODULE.validate_payload(payload)

    assert not result.ok
    assert MODULE.Finding(
        "DECISION_OUTCOME_MISMATCH", "/decision/outcome"
    ) in result.findings


def test_conflicted_dual_run_can_be_represented_only_as_deny() -> None:
    payload = _fixture("dual_run_hold.json")
    payload["migration"]["dual_run_reconciliation"] = "CONFLICTED"
    payload["migration"]["rewrite_map_complete"] = True
    payload["migration"]["legacy_dependency_count"] = 0
    _set_expected_decision(payload)

    result = MODULE.validate_payload(payload)

    assert result.ok
    assert payload["decision"] == {
        "outcome": "DENY",
        "reasons": ["DUAL_RUN_CONFLICT"],
    }


def test_endpoint_order_is_canonical() -> None:
    payload = _fixture("cutover_candidate.json")
    payload["endpoint_profiles"].reverse()
    _rehash(payload)

    result = MODULE.validate_payload(payload)

    assert result.findings == (
        MODULE.Finding("ENDPOINT_PROFILES_NOT_CANONICAL", "/endpoint_profiles"),
    )


def test_duplicate_endpoint_identity_fails_closed() -> None:
    payload = _fixture("cutover_candidate.json")
    duplicate = copy.deepcopy(payload["endpoint_profiles"][0])
    duplicate["role"] = "daily"
    payload["endpoint_profiles"].append(duplicate)
    payload["endpoint_profiles"].sort(key=lambda item: item["endpoint_id"])
    _rehash(payload)

    result = MODULE.validate_payload(payload)

    assert MODULE.Finding(
        "ENDPOINT_ID_DUPLICATE", "/endpoint_profiles"
    ) in result.findings


def test_spec_hash_mismatch_is_rejected() -> None:
    payload = _fixture("cutover_candidate.json")
    payload["migration"]["legacy_dependency_count"] = 1

    result = MODULE.validate_payload(payload)

    assert MODULE.Finding("SPEC_HASH_MISMATCH", "/spec_hash") in result.findings
