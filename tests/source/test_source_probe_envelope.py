"""Tests for SourceProbeEnvelope profile anti-collapse rules."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/source_probe/validate_source_probe_envelope.py"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/source/source_probe_envelope"
SPEC = importlib.util.spec_from_file_location("kfm_source_probe_envelope", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def load(kind: str, name: str) -> dict[str, object]:
    value = json.loads((FIXTURES / kind / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_all_valid_profiles_pass() -> None:
    expected = {
        "nass_aggregate_changed.json": "NASS_AGGREGATE",
        "edna_detection_signal.json": "EDNA_MONITORING",
        "kgs_bedrock_changed.json": "KGS_GEOLOGY",
        "loc_deferred_hold.json": "LOC_CHRONICLING_AMERICA",
    }
    for name, profile in expected.items():
        path = FIXTURES / "valid" / name
        assert load("valid", name)["profile"] == profile
        assert MODULE.validate(path).ok, name


def test_invalid_profiles_fail_with_specific_codes() -> None:
    expected = {
        "nass_field_level.json": {"NASS_GEOGRAPHY_TOO_PRECISE", "NASS_FIELD_LEVEL_CLAIM_DENIED"},
        "edna_population_inference.json": {"EDNA_POPULATION_INFERENCE_DENIED"},
        "kgs_resource_inference.json": {"KGS_RESOURCE_INFERENCE_DENIED"},
        "loc_activated.json": {"LOC_ACTIVATION_DENIED", "LOC_PROFILE_MUST_HOLD"},
    }
    for name, codes in expected.items():
        result = MODULE.validate(FIXTURES / "invalid" / name)
        assert not result.ok, name
        assert codes.issubset({finding.code for finding in result.findings}), name


def test_loc_hold_is_valid_shape_but_not_activation() -> None:
    value = load("valid", "loc_deferred_hold.json")
    assert value["materiality"]["status"] == "HOLD"
    assert value["profile_data"]["source_activation"] is False
    assert value["governance"]["publication_allowed"] is False


def test_spec_hash_change_fails_closed(tmp_path: Path) -> None:
    value = load("valid", "nass_aggregate_changed.json")
    value["profile_data"]["row_count"] = 129
    target = tmp_path / "tampered.json"
    target.write_text(json.dumps(value), encoding="utf-8")
    result = MODULE.validate(target)
    assert MODULE.Finding("SPEC_HASH_MISMATCH", "/spec_hash") in result.findings
