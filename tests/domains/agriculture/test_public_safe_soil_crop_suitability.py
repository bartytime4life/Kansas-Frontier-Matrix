from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/soil_crop_suitability.json"
CASES_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/cases.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator_soil", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _case(manifest, case_id):
    return next(case for case in manifest["cases"] if case["case_id"] == case_id)


def test_soil_crop_suitability_fixture_is_generalized_modeled_agronomic_context():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    result = module.validate_payload(candidate)

    assert result.outcome == "PASS"
    assert result.findings == ()
    assert candidate["object_family"] == "SoilCropSuitability"
    assert candidate["semantic_role"] == "MODELED_SUITABILITY"
    assert candidate["support"]["kind"] == "GENERALIZED_GRID"
    assert candidate["support"]["precision_class"] == "GENERALIZED_PUBLIC_SAFE"
    assert candidate["indicator"]["value_role"] == "MODELED_OR_DERIVED"
    assert candidate["temporal"]["kind"] == "VALID_INTERVAL"
    assert candidate["uncertainty"]["state"] == "BOUNDED"
    assert candidate["authority"]["geology_truth"] is False
    assert candidate["authority"]["habitat_occurrence"] is False
    assert candidate["release"]["public_use_allowed"] is False
    assert module.canonical_identity(candidate) == (
        candidate["spec_hash"],
        candidate["id"],
    )


def test_soil_crop_suitability_cannot_collapse_to_observed_land_use_truth():
    module = _module()
    manifest = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(
        manifest,
        _case(manifest, "modeled_suitability_as_observed"),
    )

    result = module.validate_payload(candidate)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_FAMILY_ROLE_COLLAPSE", "/semantic_role")
    ]
