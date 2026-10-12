from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/irrigation_context.json"
CASES_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/cases.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator_irrigation", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _case(manifest, case_id):
    return next(case for case in manifest["cases"] if case["case_id"] == case_id)


def test_irrigation_context_fixture_is_generalized_agriculture_context_only():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    result = module.validate_payload(candidate)

    assert result.outcome == "PASS"
    assert result.findings == ()
    assert candidate["object_family"] == "IrrigationLink"
    assert candidate["semantic_role"] == "IRRIGATION_CONTEXT"
    assert candidate["support"]["kind"] == "COUNTY"
    assert candidate["support"]["precision_class"] == "AGGREGATE_PUBLIC_SAFE"
    assert candidate["indicator"]["unit"] == "CONTEXT_ONLY"
    assert candidate["indicator"]["value_role"] == "CONTEXT_ONLY"
    assert candidate["temporal"]["kind"] == "REPORTING_PERIOD"
    assert candidate["authority"]["hydrology_observation"] is False
    assert candidate["authority"]["water_right"] is False
    assert candidate["release"]["public_use_allowed"] is False
    assert module.canonical_identity(candidate) == (
        candidate["spec_hash"],
        candidate["id"],
    )


def test_irrigation_context_cannot_claim_water_right_authority():
    module = _module()
    manifest = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(
        manifest,
        _case(manifest, "irrigation_claims_water_right"),
    )

    result = module.validate_payload(candidate)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_SCHEMA_INVALID", "/authority/water_right")
    ]


def test_irrigation_context_cannot_claim_hydrology_observation_truth():
    module = _module()
    manifest = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    candidate = module.materialize_case(
        manifest,
        _case(manifest, "irrigation_claims_hydrology_observation"),
    )

    result = module.validate_payload(candidate)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_SCHEMA_INVALID", "/authority/hydrology_observation")
    ]
