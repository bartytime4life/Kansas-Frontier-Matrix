from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/cases.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _case(manifest, case_id):
    return next(case for case in manifest["cases"] if case["case_id"] == case_id)


def test_fixture_matrix_is_exact():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    actual = []
    for case in manifest["cases"]:
        result = module.validate_payload(module.materialize_case(manifest, case))
        actual.append((
            case["case_id"],
            result.outcome,
            [{"code": f.code, "path": f.path} for f in result.findings],
        ))
    expected = [
        (case["case_id"], case["expected_outcome"], case["expected_findings"])
        for case in manifest["cases"]
    ]
    assert actual == expected


def test_valid_candidate_exposes_generalized_support_only():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(manifest, _case(manifest, "valid_county_crop_observation"))
    assert module.validate_payload(candidate).outcome == "PASS"
    assert candidate["support"]["generalized"] is True
    assert candidate["freshness"]["state"] == "CURRENT"
    assert candidate["release"]["public_use_allowed"] is False
    assert candidate["authority"] == module.FALSE_AUTHORITY

    def keys(value):
        if isinstance(value, dict):
            return set(value) | {key for item in value.values() for key in keys(item)}
        if isinstance(value, list):
            return {key for item in value for key in keys(item)}
        return set()

    candidate_keys = keys(candidate)
    for forbidden in ("coordinates", "parcel_id", "operator_id", "water_right_id"):
        assert forbidden not in candidate_keys


def test_crop_rotation_fixture_is_generalized_derived_context():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    valid = module.materialize_case(manifest, _case(manifest, "valid_generalized_grid_crop_rotation"))
    collapsed = module.materialize_case(manifest, _case(manifest, "crop_rotation_as_observed_role_denied"))

    valid_result = module.validate_payload(valid)
    collapsed_result = module.validate_payload(collapsed)

    assert valid_result.outcome == "PASS"
    assert valid["object_family"] == "CropRotation"
    assert valid["semantic_role"] == "DERIVED_CONTEXT"
    assert valid["support"]["kind"] == "GENERALIZED_GRID"
    assert valid["support"]["precision_class"] == "GENERALIZED_PUBLIC_SAFE"
    assert valid["indicator"]["value_role"] == "MODELED_OR_DERIVED"
    assert collapsed_result.outcome == "DENY"
    assert [(f.code, f.path) for f in collapsed_result.findings] == [
        ("AG_MAP_FAMILY_ROLE_COLLAPSE", "/semantic_role")
    ]


def test_harmful_precision_fails_before_shape_acceptance():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(manifest, _case(manifest, "harmful_precision_geometry"))
    result = module.validate_payload(candidate)
    assert result.outcome == "DENY"
    assert {f.code for f in result.findings} == {"AG_MAP_HARMFUL_PRECISION_DENIED"}


def test_freshness_state_is_derived_from_vintage_and_evaluation_date():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    mismatch = module.materialize_case(manifest, _case(manifest, "stale_state_mismatch"))
    stale = module.materialize_case(manifest, _case(manifest, "explicit_stale_candidate"))

    mismatch_result = module.validate_payload(mismatch)
    stale_result = module.validate_payload(stale)

    assert mismatch_result.outcome == "DENY"
    assert [(f.code, f.path) for f in mismatch_result.findings] == [
        ("AG_MAP_FRESHNESS_STATE_MISMATCH", "/freshness/state")
    ]
    assert stale_result.outcome == "PASS"
    assert stale["freshness"]["state"] == "STALE"


def test_identity_changes_when_temporal_freshness_or_support_semantics_change():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(manifest, _case(manifest, "valid_county_crop_observation"))
    first = module.canonical_identity(candidate)

    temporal_change = json.loads(json.dumps(candidate))
    temporal_change["temporal"]["year"] = 2024
    assert module.canonical_identity(temporal_change) != first

    freshness_change = json.loads(json.dumps(candidate))
    freshness_change["freshness"]["evaluated_at"] = "2025-10-02"
    assert module.canonical_identity(freshness_change) != first


def test_support_key_namespace_matches_declared_kind():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    county = module.materialize_case(
        manifest, _case(manifest, "valid_county_crop_observation")
    )
    grid = module.materialize_case(
        manifest, _case(manifest, "valid_generalized_grid_crop_rotation")
    )
    region = copy.deepcopy(county)
    region["support"]["kind"] = "REGION"
    region["support"]["key"] = "KS-AG-CROP-REGION-01"
    region["spec_hash"], region["id"] = module.canonical_identity(region)

    assert module.validate_payload(county).outcome == "PASS"
    assert module.validate_payload(region).outcome == "PASS"
    assert module.validate_payload(grid).outcome == "PASS"

    mismatches = (
        (county, "KS-GRID-20KM-038-024"),
        (region, "US-KS-20169"),
        (grid, "KS-AG-CROP-REGION-01"),
    )
    for candidate, wrong_key in mismatches:
        candidate = copy.deepcopy(candidate)
        candidate["support"]["key"] = wrong_key
        candidate["spec_hash"], candidate["id"] = module.canonical_identity(candidate)
        result = module.validate_payload(candidate)
        assert [(finding.code, finding.path) for finding in result.findings] == [
            ("AG_MAP_SCHEMA_INVALID", "/support/key")
        ]


def test_indicator_key_is_bound_to_object_family():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(
        manifest, _case(manifest, "valid_county_crop_observation")
    )

    for forbidden_value in ("operator_name", "private_address", "proprietary_yield"):
        mutated = copy.deepcopy(candidate)
        mutated["indicator"]["key"] = forbidden_value
        mutated["spec_hash"], mutated["id"] = module.canonical_identity(mutated)
        result = module.validate_payload(mutated)
        assert [(finding.code, finding.path) for finding in result.findings] == [
            ("AG_MAP_SCHEMA_INVALID", "/indicator/key")
        ]


def test_schema_binds_support_key_to_declared_kind():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(
        manifest, _case(manifest, "valid_county_crop_observation")
    )

    candidate["support"]["key"] = "KS-GRID-20KM-038-024"
    candidate["spec_hash"], candidate["id"] = module.canonical_identity(candidate)

    assert [(finding.code, finding.path) for finding in module._schema_findings(candidate)] == [
        ("AG_MAP_SCHEMA_INVALID", "/support/key")
    ]


def test_schema_binds_indicator_key_to_object_family():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(
        manifest, _case(manifest, "valid_county_crop_observation")
    )

    candidate["indicator"]["key"] = "operator_name"
    candidate["spec_hash"], candidate["id"] = module.canonical_identity(candidate)

    assert [(finding.code, finding.path) for finding in module._schema_findings(candidate)] == [
        ("AG_MAP_SCHEMA_INVALID", "/indicator/key")
    ]
