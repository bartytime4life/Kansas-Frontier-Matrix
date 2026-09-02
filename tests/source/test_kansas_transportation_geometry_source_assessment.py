from __future__ import annotations

import importlib.util
import json
import socket
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    ROOT
    / "tools/validators/source/validate_kansas_transportation_geometry_source_assessment.py"
)
SCHEMA_PATH = (
    ROOT
    / "schemas/contracts/v1/source/kansas_transportation_geometry_source_assessment.schema.json"
)
CASES_PATH = (
    ROOT
    / "fixtures/contracts/v1/source/kansas_transportation_geometry_source_assessment/cases.json"
)

spec = importlib.util.spec_from_file_location("transport_assessment_validator", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def _manifest() -> dict:
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))


def _case(case_id: str) -> dict:
    manifest = _manifest()
    case = next(item for item in manifest["cases"] if item["case_id"] == case_id)
    return validator.materialize_case(manifest, case)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    Draft202012Validator.check_schema(schema)


def test_case_inventory_is_exact_and_unique() -> None:
    case_ids = [item["case_id"] for item in _manifest()["cases"]]
    assert len(case_ids) == 19
    assert len(case_ids) == len(set(case_ids))
    assert case_ids[0] == "coherent_four_lane_profile"
    assert {
        "malformed_endpoint_identity",
        "unpinned_khub_layer",
        "unknown_ng911_crs",
        "rights_falsely_marked_reviewed",
        "lidar_authentication_requirement_erased",
        "khub_identifier_role_conflict",
        "precision_marked_approved_without_policy",
        "source_role_collapse",
        "proximity_only_crosswalk",
        "crosswalk_identifier_role_collapse",
        "governance_effect_claimed",
        "spec_hash_tampered",
    }.issubset(case_ids)


def test_exact_case_polarity_passes() -> None:
    results = validator.validate_fixture_manifest()
    assert results
    assert all(result["ok"] for result in results), results


def test_pass_candidate_has_deterministic_identity() -> None:
    candidate = _case("coherent_four_lane_profile")
    assert candidate["spec_hash"] == validator.canonical_spec_hash(candidate)
    assert candidate["assessment_id"] == validator.expected_assessment_id(candidate)
    assert validator.validate_payload(candidate).outcome == "PASS"


def test_pass_candidate_preserves_four_roles_and_false_effects() -> None:
    candidate = _case("coherent_four_lane_profile")
    assert [lane["lane_id"] for lane in candidate["lanes"]] == validator.EXPECTED_LANE_ORDER
    assert len({lane["source_role"] for lane in candidate["lanes"]}) == 4
    assert candidate["effects"] == validator.EXPECTED_EFFECTS
    assert not any(candidate["effects"].values())


def test_validator_performs_no_network_access(monkeypatch) -> None:
    def denied(*_args, **_kwargs):
        raise AssertionError("network access attempted")

    monkeypatch.setattr(socket, "socket", denied)
    results = validator.validate_fixture_manifest()
    assert all(result["ok"] for result in results)


def test_duplicate_json_keys_fail_closed(tmp_path: Path) -> None:
    candidate = _case("coherent_four_lane_profile")
    text = json.dumps(candidate, separators=(",", ":"))
    duplicate = text[:-1] + ',"status":"PROPOSED_INACTIVE"}'
    path = tmp_path / "duplicate.json"
    path.write_text(duplicate, encoding="utf-8")
    result = validator.validate_file(path)
    assert result.outcome == "ERROR"
    assert result.findings == (
        validator.Finding("TRANSPORT_JSON_DUPLICATE_KEY", "/"),
    )


def test_nonfinite_number_fails_closed(tmp_path: Path) -> None:
    path = tmp_path / "nonfinite.json"
    path.write_text('{"value":NaN}', encoding="utf-8")
    result = validator.validate_file(path)
    assert result.outcome == "ERROR"
    assert result.findings == (
        validator.Finding("TRANSPORT_JSON_NONFINITE_NUMBER", "/"),
    )


def test_cli_serialization_exposes_only_codes_and_paths() -> None:
    result = validator.validate_payload(_case("malformed_endpoint_identity"))
    payload = json.loads(validator.serialize(None, result))
    assert payload["authority"] == "NONE"
    assert payload["execution_mode"] == "FIXTURE_ONLY_NO_NETWORK"
    assert payload["outcome"] == "DENY"
    assert payload["findings"] == [
        {"code": "ENDPOINT_IDENTITY_MISMATCH", "path": "/lanes/0/interface_ref"}
    ]
    serialized = json.dumps(payload)
    assert "services.kansasgis.org" not in serialized
    assert "kanplan.ksdot.gov" not in serialized
