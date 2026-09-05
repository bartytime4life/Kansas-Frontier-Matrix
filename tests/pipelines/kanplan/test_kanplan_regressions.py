"""Regressions found while adapting the handoff, not live-source conformance."""
import ast
import copy
import dataclasses
import importlib
import json
from pathlib import Path
import subprocess
import sys

import pytest
from connectors.kansas.kanplan import (
    CaptureError, CaptureProfile, DormantReadOnlyHTTP, collect, content_hash,
    decode, metadata_fingerprint, SyntheticTransport, validate_capture,
)
from packages.geo.src.geo.esri_polyline import GeometryError, polyline_to_geojson
from test_kanplan_capture import setup_capture, run, Altered

pipeline = importlib.import_module("pipelines.normalize.roads-rail-trade.kanplan_state_system")
ROOT = Path(__file__).resolve().parents[3]


@pytest.mark.parametrize("surface", ["features", "raw", "metadata", "hash", "count", "scope", "trace"])
def test_mutable_capture_rebinds_to_preserved_bytes(surface):
    p, m, f = setup_capture()
    capture = run(p, SyntheticTransport(m, f))
    validate_capture(capture)
    if surface == "features":
        capture.features[0]["attributes"]["RouteId"] = "altered"
    elif surface == "raw":
        capture.raw_responses[0] += b" "
    elif surface == "metadata":
        capture.metadata["description"] = "changed terms"
    elif surface == "hash":
        capture.receipt["normalized_content_sha256"] = "0" * 64
    elif surface == "count":
        capture.receipt["returned_count"] += 1
    elif surface == "scope":
        capture.receipt["scope"]["bbox_4326"] = [0, 0, 1, 1]
    else:
        capture.receipt["trace"].pop()
    with pytest.raises(CaptureError):
        pipeline.compile_fixture(capture)


def test_evidence_identity_includes_derived_transform_version(monkeypatch):
    p, m, f = setup_capture()
    capture = run(p, SyntheticTransport(m, f))
    first = pipeline.compile_fixture(capture)
    original = pipeline.polyline_to_geojson
    def changed(*args, **kwargs):
        geometry, receipt = original(*args, **kwargs)
        receipt["engine_version"] += "-synthetic-regression-change"
        return geometry, receipt
    monkeypatch.setattr(pipeline, "polyline_to_geojson", changed)
    second = pipeline.compile_fixture(capture)
    assert first.dataset_version != second.dataset_version
    assert set(first.bundles).isdisjoint(second.bundles)


@pytest.mark.parametrize("bad", [False, True, 0.0])
def test_layer_id_does_not_accept_boolean_or_float(bad):
    p, m, f = setup_capture()
    m["id"] = bad
    with pytest.raises(CaptureError, match="LAYER_ID_DRIFT"):
        run(p, SyntheticTransport(m, f))


@pytest.mark.parametrize("bad", [0, 1, "false", [], {}])
def test_transfer_limit_uses_strict_false_or_absence(bad):
    p, m, f = setup_capture()
    def change(value, params, _):
        return {**value, "exceededTransferLimit": bad} if params.get("objectIds") else value
    with pytest.raises(CaptureError, match="TRANSFER_LIMIT"):
        run(p, Altered(m, f, change))


@pytest.mark.parametrize("bad", [1, "true", None])
def test_fixture_boolean_cannot_be_coerced(bad):
    p, _, _ = setup_capture()
    with pytest.raises(CaptureError, match="FIXTURE_MODE_TYPE"):
        dataclasses.replace(p, synthetic=bad)


def test_profile_does_not_share_mutable_field_mapping():
    p, _, _ = setup_capture()
    required = dict(p.required_types)
    replacement = dataclasses.replace(p, required_types=required)
    required["RouteId"] = "changed"
    assert replacement.required_types["RouteId"] == "esriFieldTypeString"
    with pytest.raises(TypeError):
        replacement.required_types["RouteId"] = "changed"


@pytest.mark.parametrize("field", ["copyrightText", "description", "serviceItemId"])
def test_metadata_identity_tracks_usage_and_origin_fields(field):
    _, m, _ = setup_capture()
    baseline = metadata_fingerprint(m)
    m[field] = "synthetic material change"
    assert metadata_fingerprint(m) != baseline


@pytest.mark.parametrize("sr", [{"wkid": 6923, "latestWkid": 4326},
                               {"wkid": 3857, "latestWkid": 4326}])
def test_conflicting_crs_aliases_cannot_relabel_coordinates(sr):
    with pytest.raises(GeometryError, match="CRS_ALIAS_CONFLICT"):
        polyline_to_geojson({"paths": [[[0, 0], [1, 1]]]}, sr, has_z=False, has_m=False)


def test_documented_mercator_alias_preserves_transform():
    geometry, receipt = polyline_to_geojson(
        {"paths": [[[0, 0], [111319.49079327357, 0]]]},
        {"wkid": 102100, "latestWkid": 3857}, has_z=False, has_m=False)
    assert geometry["coordinates"][1][0] == pytest.approx(1)
    assert receipt["input_crs"]["wkid"] == 102100


@pytest.mark.parametrize("limit", [True, 0, -1, 100001, float("inf")])
def test_geometry_budget_is_itself_bounded(limit):
    with pytest.raises(GeometryError, match="INVALID_VERTEX_LIMIT"):
        polyline_to_geojson({"paths": [[[0, 0], [1, 1]]]}, {"wkid": 4326},
                            has_z=False, has_m=False, maximum_vertices=limit)


def test_huge_number_and_json_integer_are_finite_failures():
    with pytest.raises(GeometryError, match="NONFINITE_COORDINATE"):
        polyline_to_geojson({"paths": [[[0, 0], [10**1000, 1]]]}, {"wkid": 4326},
                            has_z=False, has_m=False)
    with pytest.raises(CaptureError):
        decode(b'{"number":' + b'9' * 5000 + b'}', 6000)


@pytest.mark.parametrize("time", ["not-a-date", "2026-09-05T00:00:00", None])
def test_retrieval_window_requires_valid_zoned_times(time):
    p, m, f = setup_capture()
    with pytest.raises(CaptureError, match="RETRIEVAL_TIME"):
        collect(p, SyntheticTransport(m, f), clock=lambda: time, sleep=lambda _: None)


def test_duplicate_global_id_is_not_a_stable_key():
    p, m, f = setup_capture()
    m["fields"].append({"name": "GlobalID", "type": "esriFieldTypeGlobalID"})
    for feature in f:
        feature["attributes"]["GlobalID"] = "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"
    p = dataclasses.replace(p, acquired_fields=(*p.acquired_fields, "GlobalID"),
                            expected_metadata_hash=metadata_fingerprint(m))
    with pytest.raises(CaptureError):
        pipeline.compile_fixture(run(p, SyntheticTransport(m, f)))


def test_candidate_keeps_raw_integrity_and_evidence_feature_binding():
    c = pipeline.build_fixture()
    c.raw_responses[0] += b" "
    with pytest.raises(CaptureError, match="CAPTURE_RAW_INTEGRITY"):
        pipeline.validate_candidate(c)
    c = pipeline.build_fixture()
    ref = next(iter(c.bundles))
    c.bundles[ref]["checksums"]["display_feature"] = "sha256:" + "0" * 64
    c.manifest["bundle_index_sha256"] = content_hash(c.bundles)
    with pytest.raises(CaptureError, match="EVIDENCE_FEATURE_BINDING"):
        pipeline.validate_candidate(c)


@pytest.mark.parametrize("key", ["rights_revoked", "withdrawn"])
def test_missing_rights_and_withdrawal_state_denies_private_resolution(key):
    c = pipeline.build_fixture()
    del c.manifest[key]
    result = pipeline.resolve_fixture(c, c.display["features"][0]["id"], context="private_fixture")
    assert result["outcome"] == "DENY"


def test_shared_geo_does_not_depend_on_connectors():
    source = ROOT / "packages/geo/src/geo/esri_polyline.py"
    imports = [n.module for n in ast.walk(ast.parse(source.read_text())) if isinstance(n, ast.ImportFrom)]
    assert not any(x and x.startswith(("connectors", "pipelines", "tools", "apps")) for x in imports)


@pytest.mark.parametrize("url", ["http://127.0.0.1/private", "https://kanplan.ksdot.gov/applyEdits"])
def test_http_has_no_activation_switch(url):
    with pytest.raises(CaptureError, match="LIVE_SOURCE_NOT_ACTIVATED"):
        DormantReadOnlyHTTP()(url, {"token": "must-not-echo"}, timeout=1, maximum=100)


def test_cli_rejects_option_abbreviations_and_in_repository_output(tmp_path):
    module = "pipelines.normalize.roads-rail-trade.kanplan_state_system"
    output = tmp_path / "not-created"
    result = subprocess.run([sys.executable, "-m", module, "--fixture", str(output)],
                            cwd=ROOT, capture_output=True, text=True)
    assert result.returncode != 0 and not output.exists()
    result = subprocess.run([sys.executable, "-m", module, "--fixture-output", str(ROOT / "tests/pipelines/kanplan/should-not-be-created")],
                            cwd=ROOT, capture_output=True, text=True)
    assert result.returncode != 0 and "OUTPUT_MUST_BE_OUTSIDE_REPOSITORY" in result.stderr
    assert not (ROOT / "tests/pipelines/kanplan/should-not-be-created").exists()
