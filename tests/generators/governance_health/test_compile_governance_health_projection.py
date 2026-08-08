import json
from pathlib import Path

import pytest

from tools.generators.governance_health.compile_governance_health_projection import compile_projection

CASES = Path("fixtures/contracts/v1/governance/governance_health_projection/cases.json")


def cases():
    return json.loads(CASES.read_text(encoding="utf-8"))["cases"]


def test_fixture_coverage_states():
    for case in cases():
        assert compile_projection(case["input"])["coverage_state"] == case["expected_coverage"]


def test_complete_fixture_ratios_are_derived():
    result = compile_projection(cases()[0]["input"])
    assert result["indicators"]["evidence_ref_resolution_rate"] == {"numerator": 1, "denominator": 2, "value": 0.5}
    assert result["indicators"]["release_with_rollback_rate"]["value"] == 1.0
    assert result["indicators"]["adr_completeness"]["value"] == 0.0
    assert result["indicators"]["open_drift_count"] == 1
    assert result["indicators"]["max_open_drift_age_days"] == 12


def test_projection_is_deterministic():
    source = cases()[0]["input"]
    assert compile_projection(source) == compile_projection(json.loads(json.dumps(source)))


def test_wrong_source_family_fails_closed():
    source = json.loads(json.dumps(cases()[0]["input"]))
    source["observations"][0]["source_family"] = "RELEASE_MANIFEST"
    with pytest.raises(ValueError):
        compile_projection(source)


def test_duplicate_source_reference_fails_closed():
    source = json.loads(json.dumps(cases()[0]["input"]))
    source["observations"][1]["source_record_ref"] = source["observations"][0]["source_record_ref"]
    with pytest.raises(ValueError):
        compile_projection(source)


def test_projection_never_claims_authority():
    effects = compile_projection(cases()[0]["input"])["effects"]
    assert effects == {
        "policy_evaluated": False,
        "release_authorized": False,
        "published": False,
        "enforcement_changed": False,
    }
