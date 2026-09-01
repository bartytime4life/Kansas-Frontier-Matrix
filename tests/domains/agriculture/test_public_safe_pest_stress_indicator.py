from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/pest_stress_indicator.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator_pest_stress_indicator", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_pest_stress_fixture_is_generalized_derived_agronomic_context():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    result = module.validate_payload(candidate)

    assert result.outcome == "PASS"
    assert result.findings == ()
    assert candidate["object_family"] == "PestStressIndicator"
    assert candidate["semantic_role"] == "DERIVED_INDICATOR"
    assert candidate["support"]["kind"] == "GENERALIZED_GRID"
    assert candidate["support"]["generalized"] is True
    assert candidate["support"]["precision_class"] == "GENERALIZED_PUBLIC_SAFE"
    assert candidate["temporal"]["kind"] == "REPORTING_PERIOD"
    assert candidate["indicator"]["unit"] == "INDEX"
    assert candidate["indicator"]["value_role"] == "MODELED_OR_DERIVED"
    assert candidate["authority"]["habitat_occurrence"] is False
    assert candidate["authority"]["hazard_alert"] is False
    assert candidate["release"]["public_use_allowed"] is False
    assert candidate["release"]["published"] is False
    assert module.canonical_identity(candidate) == (
        candidate["spec_hash"],
        candidate["id"],
    )


def test_pest_stress_rejects_observed_role_collapse():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    collapsed = copy.deepcopy(candidate)
    collapsed["semantic_role"] = "OBSERVED_AGGREGATE"
    collapsed["support"]["kind"] = "COUNTY"
    collapsed["support"]["key"] = "US-KS-20169"
    collapsed["support"]["precision_class"] = "AGGREGATE_PUBLIC_SAFE"
    collapsed["indicator"]["value_role"] = "OBSERVED"
    collapsed["spec_hash"], collapsed["id"] = module.canonical_identity(collapsed)

    result = module.validate_payload(collapsed)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_FAMILY_ROLE_COLLAPSE", "/semantic_role")
    ]


def test_pest_stress_rejects_habitat_occurrence_authority():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    overclaim = copy.deepcopy(candidate)
    overclaim["authority"]["habitat_occurrence"] = True

    result = module.validate_payload(overclaim)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_SCHEMA_INVALID", "/authority/habitat_occurrence")
    ]
