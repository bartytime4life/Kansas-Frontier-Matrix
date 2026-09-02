from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/agricultural_economy_observation.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator_economy_observation", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_agricultural_economy_fixture_is_generalized_observed_aggregate():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    result = module.validate_payload(candidate)

    assert result.outcome == "PASS"
    assert result.findings == ()
    assert candidate["object_family"] == "AgriculturalEconomyObservation"
    assert candidate["semantic_role"] == "ECONOMIC_AGGREGATE"
    assert candidate["support"]["kind"] == "COUNTY"
    assert candidate["support"]["generalized"] is True
    assert candidate["support"]["precision_class"] == "AGGREGATE_PUBLIC_SAFE"
    assert candidate["temporal"]["kind"] == "CALENDAR_YEAR"
    assert candidate["indicator"]["unit"] == "USD"
    assert candidate["indicator"]["value_role"] == "OBSERVED"
    assert candidate["sensitivity"]["operator_identity"] is False
    assert candidate["sensitivity"]["proprietary_value"] is False
    assert candidate["release"]["public_use_allowed"] is False
    assert candidate["release"]["published"] is False
    assert module.canonical_identity(candidate) == (
        candidate["spec_hash"],
        candidate["id"],
    )


def test_agricultural_economy_rejects_context_role_collapse():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    collapsed = copy.deepcopy(candidate)
    collapsed["semantic_role"] = "INFRASTRUCTURE_CONTEXT"
    collapsed["indicator"]["value_role"] = "CONTEXT_ONLY"
    collapsed["spec_hash"], collapsed["id"] = module.canonical_identity(collapsed)

    result = module.validate_payload(collapsed)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_FAMILY_ROLE_COLLAPSE", "/semantic_role")
    ]


def test_agricultural_economy_rejects_operator_identity():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    precise = copy.deepcopy(candidate)
    precise["operator_id"] = "synthetic-operator-001"

    result = module.validate_payload(precise)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_HARMFUL_PRECISION_DENIED", "/operator_id")
    ]
