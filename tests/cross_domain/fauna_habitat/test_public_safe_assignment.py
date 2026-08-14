from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/cross_domain/fauna_habitat/"
    "validate_public_safe_assignment.py"
)
SPEC = importlib.util.spec_from_file_location(
    "fauna_habitat_public_safe_assignment", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _cases() -> dict[str, tuple[dict, object, dict]]:
    return {
        name: (candidate, result, dict(expected))
        for name, candidate, result, expected in MODULE.fixture_cases()
    }


def test_fixture_matrix_has_exact_expected_size_and_polarity() -> None:
    assert len(MODULE.fixture_cases()) == 10
    assert MODULE.fixture_profile() == 0


def test_public_safe_generalized_candidate_is_deterministic_and_non_publishing() -> None:
    candidate, result, _ = _cases()["public_safe_generalized_candidate"]
    assert result.status == "PASS"
    assert candidate["decision"]["validator_outcome"] == "ALLOW"
    assert candidate["decision"]["status"] == "JOIN_CANDIDATE"
    assert candidate["decision"]["source_roles"]["output_role"] == "CANDIDATE_RELATION"
    assert not any(candidate["decision"]["effects"].values())
    assert MODULE.GENERIC.seal(candidate)["assessment_id"] == candidate["assessment_id"]


def test_sensitive_and_incomplete_cases_preserve_finite_outcomes() -> None:
    cases = _cases()
    assert cases["restricted_exact_fauna_geometry_denied"][0]["decision"]["validator_outcome"] == "DENY"
    assert cases["restricted_generalized_fauna_context_abstains"][0]["decision"]["status"] == "SENSITIVITY_REVIEW_REQUIRED"
    assert cases["missing_fauna_evidence_abstains"][0]["decision"]["status"] == "EVIDENCE_REF_MISSING"
    assert cases["modeled_habitat_role_requires_review"][0]["decision"]["status"] == "SOURCE_ROLE_REVIEW_REQUIRED"


def test_pair_profile_rejects_wrong_precision_domain_profile_and_provenance() -> None:
    cases = _cases()
    assert [finding.code for finding in cases["public_safe_exact_fauna_geometry_fails_pair_profile"][1].findings] == ["ALLOW_GEOMETRY_NOT_GENERALIZED"]
    assert [finding.code for finding in cases["swapped_domain_order_fails_pair_profile"][1].findings] == ["ENDPOINT_DOMAIN_MISMATCH", "ENDPOINT_DOMAIN_MISMATCH"]
    assert [finding.code for finding in cases["wrong_relation_profile_fails_pair_profile"][1].findings] == ["RELATION_PROFILE_MISMATCH"]
    assert [finding.code for finding in cases["non_fixture_object_ref_fails_pair_profile"][1].findings] == ["NON_FIXTURE_REF_DENIED"]


def test_generic_schema_still_rejects_publisher_effect() -> None:
    candidate, result, _ = _cases()["publisher_effect_is_schema_rejected"]
    assert result.status == "FAIL"
    assert [finding.code for finding in result.findings] == ["SCHEMA_INVALID"]
    assert candidate["decision"]["effects"]["publication"] is True


def test_fixture_contains_no_coordinate_fields_or_live_network_targets() -> None:
    fixture_path = MODULE.CASES_PATH
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    text = fixture_path.read_text(encoding="utf-8").lower()
    forbidden_keys = {"coordinate", "coordinates", "geometry", "lat", "latitude", "lon", "longitude", "wkt", "wkb"}

    def walk(value: object) -> None:
        if isinstance(value, dict):
            assert not (forbidden_keys & set(value))
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(data["base"])
    assert "http://" not in json.dumps(data["base"]).lower()
    assert "https://" not in json.dumps(data["base"]).lower()
    assert "example.invalid" in text  # one negative mutation proves rejection


def test_validator_has_no_network_client_or_file_write_path() -> None:
    source = MODULE_PATH.read_text(encoding="utf-8")
    forbidden = (
        "import requests",
        "import urllib",
        "import socket",
        "httpx",
        "aiohttp",
        "boto3",
        "write_text(",
        "write_bytes(",
        "open(\"w",
        "open('w",
    )
    assert not any(token in source for token in forbidden)
