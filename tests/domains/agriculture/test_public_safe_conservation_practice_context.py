from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/conservation_practice_context.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator_conservation_practice", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_conservation_practice_context_fixture_is_generalized_and_context_only():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    result = module.validate_payload(candidate)

    assert result.outcome == "PASS"
    assert result.findings == ()
    assert candidate["object_family"] == "ConservationPractice"
    assert candidate["semantic_role"] == "PRACTICE_CONTEXT"
    assert candidate["support"]["kind"] == "REGION"
    assert candidate["support"]["generalized"] is True
    assert candidate["support"]["precision_class"] == "GENERALIZED_PUBLIC_SAFE"
    assert candidate["indicator"]["unit"] == "CONTEXT_ONLY"
    assert candidate["indicator"]["value_role"] == "CONTEXT_ONLY"
    assert candidate["authority"]["habitat_occurrence"] is False
    assert candidate["sensitivity"]["operator_identity"] is False
    assert candidate["release"]["public_use_allowed"] is False
    assert candidate["release"]["published"] is False
    assert module.canonical_identity(candidate) == (
        candidate["spec_hash"],
        candidate["id"],
    )


def test_conservation_practice_context_rejects_habitat_authority():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    overclaim = copy.deepcopy(candidate)
    overclaim["authority"]["habitat_occurrence"] = True

    result = module.validate_payload(overclaim)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_SCHEMA_INVALID", "/authority/habitat_occurrence")
    ]


def test_conservation_practice_context_rejects_operator_identity():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    precise = copy.deepcopy(candidate)
    precise["operator_id"] = "synthetic-operator-001"

    result = module.validate_payload(precise)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_HARMFUL_PRECISION_DENIED", "/operator_id")
    ]
