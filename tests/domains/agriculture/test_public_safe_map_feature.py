from __future__ import annotations

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
    candidate = module.materialize_case(manifest, manifest["cases"][0])
    assert module.validate_payload(candidate).outcome == "PASS"
    assert candidate["support"]["generalized"] is True
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


def test_harmful_precision_fails_before_shape_acceptance():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(manifest, manifest["cases"][1])
    result = module.validate_payload(candidate)
    assert result.outcome == "DENY"
    assert {f.code for f in result.findings} == {"AG_MAP_HARMFUL_PRECISION_DENIED"}


def test_identity_changes_when_temporal_or_support_semantics_change():
    module = _module()
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(manifest, manifest["cases"][0])
    first = module.canonical_identity(candidate)
    changed = json.loads(json.dumps(candidate))
    changed["temporal"]["year"] = 2024
    second = module.canonical_identity(changed)
    assert first != second
