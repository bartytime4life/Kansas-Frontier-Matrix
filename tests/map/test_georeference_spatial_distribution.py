"""Focused deterministic tests for GCP spatial-distribution quality."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from tools.validators.map import validate_georeference_spatial_distribution as target

ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT / "fixtures/contracts/v1/map/georeference_spatial_distribution/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/map/georeference_spatial_distribution.schema.json"


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
    assert outcomes == {"READY", "HOLD", "ERROR"}


def test_baseline_metrics_are_recomputed_exactly():
    candidate, _ = case("ready_baseline")
    metrics = target.compute_metrics(candidate)
    assert target._declared(metrics) == candidate["computed"]
    assert candidate["computed"] == {
        "hull_vertex_count": 4,
        "hull_area_ratio": 0.7875,
        "max_extrapolation_ratio": 0.055216,
        "centroid_offset_ratio": 0.0,
        "occupied_quadrants": 4,
    }


def test_clustered_gcps_hold_on_coverage_and_extrapolation():
    candidate, _ = case("hold_clustered_center")
    result = target.validate_candidate(candidate)
    assert result.outcome == "HOLD"
    assert result.reasons == ("EXTRAPOLATION_RISK_HIGH", "HULL_COVERAGE_LOW")


def test_asymmetric_distribution_detects_centroid_bias():
    candidate, _ = case("hold_asymmetric_right")
    result = target.validate_candidate(candidate)
    assert result.outcome == "HOLD"
    assert result.reasons == ("CENTROID_OFFSET_HIGH",)


def test_three_gcps_do_not_establish_spatial_redundancy():
    candidate, _ = case("hold_three_gcps")
    result = target.validate_candidate(candidate)
    assert result.outcome == "HOLD"
    assert "INSUFFICIENT_GCPS" in result.reasons
    assert "QUADRANT_COVERAGE_LOW" in result.reasons


def test_self_intersecting_resource_mask_fails_closed():
    candidate, _ = case("error_self_intersecting_mask")
    assert target.validate_candidate(candidate).reasons == ("RESOURCE_MASK_SELF_INTERSECTION",)


def test_collinear_control_points_fail_closed():
    candidate, _ = case("error_collinear_gcps")
    assert target.validate_candidate(candidate).reasons == ("GCP_HULL_DEGENERATE",)


def test_metric_drift_fails_closed():
    candidate, _ = case("error_metric_mismatch")
    assert target.validate_candidate(candidate).reasons == ("METRIC_MISMATCH",)


def test_validator_imports_no_network_warp_or_crs_runtime():
    source = Path(target.__file__).read_text(encoding="utf-8")
    denied = (
        "import socket",
        "import requests",
        "import httpx",
        "import urllib",
        "import subprocess",
        "import rasterio",
        "import pyproj",
        "from osgeo",
        "import geopandas",
    )
    assert not any(item in source for item in denied)


def test_fixture_cli_passes():
    assert target.validate_fixtures() == 0
