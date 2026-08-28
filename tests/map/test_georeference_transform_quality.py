"""Focused deterministic tests for synthetic affine georeference quality."""
from __future__ import annotations
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from tools.validators.map import validate_georeference_transform_quality as target

ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT / "fixtures/contracts/v1/map/georeference_transform_quality/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/map/georeference_transform_quality.schema.json"

def manifest(): return json.loads(CASES.read_text(encoding="utf-8"))
def case(cid):
    m=manifest(); e=next(x for x in m["cases"] if x["case_id"]==cid); return target.materialize_case(m,e),e

def test_schema_meta_valid(): Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))
def test_fixture_matrix_exact():
    m=manifest(); assert len(m["cases"])==10
    for e in m["cases"]:
        r=target.validate_candidate(target.materialize_case(m,e)); assert {"outcome":r.outcome,"reasons":list(r.reasons)}==e["expected"]
def test_exact_affine_coefficients():
    c,_=case("ready_exact_affine"); assert c["computed"]["affine_coefficients"]==[100.0,2.0,0.5,200.0,-0.25,1.5]; assert c["computed"]["rms"]==0.0
def test_small_noise_is_bounded_and_repeatable():
    c,_=case("ready_small_noise"); q1=target.compute_quality(c["gcps"]); q2=target.compute_quality(c["gcps"]); assert target._declared(q1)==target._declared(q2)==c["computed"]
def test_leave_one_out_gate_can_hold_when_in_sample_passes():
    c,_=case("hold_loo_only"); r=target.validate_candidate(c); assert r.outcome=="HOLD"; assert r.reasons==("LOO_MAX_RESIDUAL_THRESHOLD_EXCEEDED","LOO_RMS_THRESHOLD_EXCEEDED")
def test_three_gcps_fit_but_do_not_establish_redundant_quality():
    c,_=case("hold_three_gcps"); assert c["computed"]["rms"]==0.0; assert c["computed"]["loo_rms"] is None; assert target.validate_candidate(c).reasons==("INSUFFICIENT_REDUNDANCY",)
def test_collinear_gcps_fail_closed():
    c,_=case("error_collinear_gcps"); assert target.validate_candidate(c).reasons==("DEGENERATE_GCP_GEOMETRY",)
def test_claimed_metric_drift_fails_closed():
    c,_=case("error_metric_mismatch"); assert target.validate_candidate(c).reasons==("METRIC_MISMATCH",)
def test_validator_imports_no_network_or_warp_runtime():
    s=Path(target.__file__).read_text(encoding="utf-8"); denied=("import socket","import requests","import httpx","import urllib","import subprocess","import rasterio","import pyproj","from osgeo")
    assert not any(x in s for x in denied)
def test_fixture_cli_passes(): assert target.validate_fixtures()==0
