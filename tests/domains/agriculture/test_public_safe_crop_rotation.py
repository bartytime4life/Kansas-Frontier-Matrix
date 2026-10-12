from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/domains/agriculture/validate_public_safe_map_feature.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/crop_rotation.json"


def _module():
    spec = importlib.util.spec_from_file_location("ag_map_validator_crop_rotation", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_crop_rotation_fixture_is_generalized_derived_context():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    result = module.validate_payload(candidate)

    assert result.outcome == "PASS"
    assert result.findings == ()
    assert candidate["object_family"] == "CropRotation"
    assert candidate["semantic_role"] == "DERIVED_CONTEXT"
    assert candidate["support"]["kind"] == "GENERALIZED_GRID"
    assert candidate["support"]["generalized"] is True
    assert candidate["support"]["precision_class"] == "GENERALIZED_PUBLIC_SAFE"
    assert candidate["temporal"]["kind"] == "CROP_YEAR"
    assert candidate["indicator"]["value_role"] == "MODELED_OR_DERIVED"
    assert candidate["sensitivity"]["exact_field_geometry"] is False
    assert candidate["release"]["public_use_allowed"] is False
    assert candidate["release"]["published"] is False
    assert module.canonical_identity(candidate) == (
        candidate["spec_hash"],
        candidate["id"],
    )


def test_crop_rotation_rejects_observed_role_collapse():
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


def test_crop_rotation_rejects_field_identifier_precision():
    module = _module()
    candidate = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    precise = copy.deepcopy(candidate)
    precise["field_id"] = "synthetic-private-field"

    result = module.validate_payload(precise)

    assert result.outcome == "DENY"
    assert [(finding.code, finding.path) for finding in result.findings] == [
        ("AG_MAP_HARMFUL_PRECISION_DENIED", "/field_id")
    ]
