from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/yield_observation.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator_yield_observation", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_yield_observation_fixture_is_generalized_observed_aggregate():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    result = module.validate_payload(candidate)

    assert result.outcome == "PASS"
    assert result.findings == ()
    assert candidate["object_family"] == "YieldObservation"
    assert candidate["semantic_role"] == "OBSERVED_AGGREGATE"
    assert candidate["support"]["kind"] == "COUNTY"
    assert candidate["support"]["generalized"] is True
    assert candidate["support"]["precision_class"] == "AGGREGATE_PUBLIC_SAFE"
    assert candidate["temporal"]["kind"] == "CROP_YEAR"
    assert candidate["indicator"]["value_role"] == "OBSERVED"
    assert candidate["sensitivity"]["proprietary_value"] is False
    assert candidate["release"]["public_use_allowed"] is False
    assert candidate["release"]["published"] is False
    assert module.canonical_identity(candidate) == (
        candidate["spec_hash"],
        candidate["id"],
    )


def test_yield_observation_rejects_modeled_role_collapse():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    collapsed = copy.deepcopy(candidate)
    collapsed["semantic_role"] = "DERIVED_INDICATOR"
    collapsed["indicator"]["value_role"] = "MODELED_OR_DERIVED"
    collapsed["spec_hash"], collapsed["id"] = module.canonical_identity(collapsed)

    result = module.validate_payload(collapsed)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_FAMILY_ROLE_COLLAPSE", "/semantic_role")
    ]


def test_yield_observation_rejects_proprietary_yield_detail():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    precise = copy.deepcopy(candidate)
    precise["proprietary_yield"] = 211.7

    result = module.validate_payload(precise)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_HARMFUL_PRECISION_DENIED", "/proprietary_yield")
    ]
