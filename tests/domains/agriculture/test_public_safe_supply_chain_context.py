from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/supply_chain_context.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator_supply_chain", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_supply_chain_context_fixture_is_generalized_and_context_only():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    result = module.validate_payload(candidate)

    assert result.outcome == "PASS"
    assert result.findings == ()
    assert candidate["object_family"] == "SupplyChainNode"
    assert candidate["semantic_role"] == "INFRASTRUCTURE_CONTEXT"
    assert candidate["support"]["kind"] == "REGION"
    assert candidate["support"]["generalized"] is True
    assert candidate["support"]["precision_class"] == "GENERALIZED_PUBLIC_SAFE"
    assert candidate["indicator"]["unit"] == "CONTEXT_ONLY"
    assert candidate["indicator"]["value_role"] == "CONTEXT_ONLY"
    assert candidate["sensitivity"]["sensitive_infrastructure"] is False
    assert candidate["release"]["public_use_allowed"] is False
    assert candidate["release"]["published"] is False
    assert module.canonical_identity(candidate) == (
        candidate["spec_hash"],
        candidate["id"],
    )


def test_supply_chain_context_rejects_precise_facility_longitude():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    precise = copy.deepcopy(candidate)
    precise["longitude"] = -98.4123

    result = module.validate_payload(precise)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_HARMFUL_PRECISION_DENIED", "/longitude")
    ]
