"""Focused tests for deterministic georeference control-point-set identity."""
from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator
from tools.validators.map import validate_georeference_control_point_set as target

ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT / "fixtures/contracts/v1/map/georeference_control_point_set/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/map/georeference_control_point_set.schema.json"


def manifest():
    return json.loads(CASES.read_text(encoding="utf-8"))


def case(case_id: str):
    source = manifest()
    entry = next(item for item in source["cases"] if item["case_id"] == case_id)
    return target.materialize_case(source, entry), entry


def test_schema_meta_valid():
    Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))


def test_fixture_matrix_exact():
    source = manifest()
    assert len(source["cases"]) == 11
    outcomes = set()
    for entry in source["cases"]:
        result = target.validate_candidate(target.materialize_case(source, entry))
        actual = {"outcome": result.outcome, "reasons": list(result.reasons)}
        assert actual == entry["expected"]
        outcomes.add(result.outcome)
    assert outcomes == {"VALID", "ERROR"}


def test_known_identity_is_stable():
    candidate, _ = case("valid_baseline")
    assert target.identity(candidate) == (
        "kfm:georeference-gcp-set:sha256:9d9da050628e5efe57737fa791116066a1bab4921e28a98d70ec7603730a174a",
        "sha256:30d9ac02ce788cc1e5c74162ca432bd40b46d779564468547729342930f2db81",
        "sha256:bc2a8f740578f6f1112e888126eef236fb0a81a594e95dad3f977037ed373ad5",
    )


def test_numeric_spelling_does_not_change_identity():
    baseline, _ = case("valid_baseline")
    variant, _ = case("valid_numeric_spelling_normalized")
    assert target.identity(baseline) == target.identity(variant)


def test_resource_change_only_changes_resource_and_full_identity():
    candidate, _ = case("valid_baseline")
    before = target.identity(candidate)
    changed = copy.deepcopy(candidate)
    changed["control_points"][4]["resource"] = [501, 400]
    after = target.identity(changed)
    assert before[0] != after[0]
    assert before[1] != after[1]
    assert before[2] == after[2]


def test_target_change_only_changes_target_and_full_identity():
    candidate, _ = case("valid_baseline")
    before = target.identity(candidate)
    changed = copy.deepcopy(candidate)
    changed["control_points"][4]["target"] = [1301, 675]
    after = target.identity(changed)
    assert before[0] != after[0]
    assert before[1] == after[1]
    assert before[2] != after[2]


def test_unsorted_ids_fail_before_hash_acceptance():
    candidate, _ = case("error_unsorted_ids")
    assert target.validate_candidate(candidate).reasons == ("POINT_IDS_NOT_CANONICAL",)


def test_duplicate_coordinate_lanes_fail_closed():
    candidate, _ = case("error_duplicate_resource")
    assert target.validate_candidate(candidate).reasons == ("DUPLICATE_RESOURCE_POINT",)
    candidate, _ = case("error_duplicate_target")
    assert target.validate_candidate(candidate).reasons == ("DUPLICATE_TARGET_POINT",)


def test_hash_drift_is_lane_specific():
    candidate, _ = case("error_resource_hash_mismatch")
    assert target.validate_candidate(candidate).reasons == ("RESOURCE_SET_HASH_MISMATCH",)
    candidate, _ = case("error_target_hash_mismatch")
    assert target.validate_candidate(candidate).reasons == ("TARGET_SET_HASH_MISMATCH",)


def test_validator_imports_no_network_or_geospatial_runtime():
    source = Path(target.__file__).read_text(encoding="utf-8")
    denied = (
        "import socket", "import requests", "import httpx", "import urllib", "import subprocess",
        "import rasterio", "import pyproj", "from osgeo", "import geopandas"
    )
    assert not any(item in source for item in denied)


def test_fixture_cli_passes():
    assert target.validate_fixtures() == 0
