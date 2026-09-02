from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/validators/cross_domain/soil_agriculture/validate_public_safe_context.py"
SPEC = importlib.util.spec_from_file_location("soil_agriculture_public_safe_context", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

def _cases():
    return {name: (candidate, result, dict(expected)) for name, candidate, result, expected in MODULE.fixture_cases()}

def test_fixture_matrix_passes() -> None:
    assert len(MODULE.fixture_cases()) == 7
    assert MODULE.fixture_profile() == 0

def test_public_safe_candidate_is_non_publishing_and_deterministic() -> None:
    candidate, result, _ = _cases()["public_safe_generalized_candidate"]
    assert result.status == "PASS"
    assert candidate["decision"]["validator_outcome"] == "ALLOW"
    assert candidate["decision"]["status"] == "JOIN_CANDIDATE"
    assert candidate["decision"]["source_roles"]["output_role"] == "CANDIDATE_RELATION"
    assert not any(candidate["decision"]["effects"].values())
    assert MODULE.GENERIC.seal(candidate)["assessment_id"] == candidate["assessment_id"]

def test_fail_closed_cases_preserve_finite_outcomes() -> None:
    cases = _cases()
    assert cases["restricted_exact_soil_geometry_denied"][0]["decision"]["validator_outcome"] == "DENY"
    assert cases["missing_soil_evidence_abstains"][0]["decision"]["status"] == "EVIDENCE_REF_MISSING"
    assert cases["modeled_agriculture_role_requires_review"][0]["decision"]["status"] == "SOURCE_ROLE_REVIEW_REQUIRED"
    private_candidate, private_result, _ = cases["private_parcel_agriculture_context_denied"]
    assert private_result.status == "PASS"
    assert private_candidate["decision"]["validator_outcome"] == "DENY"
    assert private_candidate["decision"]["status"] == "GEOMETRY_PRECISION_BLOCKED"

def test_pair_profile_rejects_public_exact_precision_and_wrong_profile() -> None:
    cases = _cases()
    assert [f.code for f in cases["public_safe_exact_soil_geometry_fails_pair_profile"][1].findings] == ["ALLOW_GEOMETRY_NOT_GENERALIZED"]
    assert [f.code for f in cases["wrong_relation_profile_fails_pair_profile"][1].findings] == ["RELATION_PROFILE_MISMATCH"]

def test_fixture_contains_no_coordinate_or_geometry_payload() -> None:
    data = json.loads(MODULE.CASES_PATH.read_text(encoding="utf-8"))
    forbidden = {"coordinate", "coordinates", "geometry", "lat", "latitude", "lon", "longitude", "wkt", "wkb"}
    def walk(value: object) -> None:
        if isinstance(value, dict):
            assert not (forbidden & set(value))
            for child in value.values(): walk(child)
        elif isinstance(value, list):
            for child in value: walk(child)
    walk(data["base"])
    base = json.dumps(data["base"]).lower()
    assert "http://" not in base and "https://" not in base

def test_validator_has_no_network_client_or_write_path() -> None:
    source = MODULE_PATH.read_text(encoding="utf-8")
    forbidden = ("import requests", "import urllib", "import socket", "httpx", "aiohttp", "boto3", "write_text(", "write_bytes(", "open(\"w", "open('w")
    assert not any(token in source for token in forbidden)
