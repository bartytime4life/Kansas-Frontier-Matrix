from __future__ import annotations

import importlib.util
import json
import socket
import sys
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/release/validate_geospatial_carrier_readiness.py"
SCHEMA_PATH = ROOT / "schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json"
CASES_PATH = ROOT / "fixtures/contracts/v1/release/geospatial_carrier_readiness/cases.json"

spec = importlib.util.spec_from_file_location("carrier_readiness", MODULE_PATH)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def _cases():
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]


def _case(case_id: str):
    return next(case for case in _cases() if case["case_id"] == case_id)


def test_schema_is_valid_draft_2020_12():
    Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))


def test_all_cases_match_exact_expected_results():
    for case in _cases():
        result = module.assess(case["candidate"]).as_dict()
        result.pop("scope")
        assert result == case["expected"], case["case_id"]


def test_each_carrier_has_ready_hold_and_error_case():
    outcomes: dict[str, set[str]] = {}
    for case in _cases():
        kind = case["candidate"]["carrier_kind"]
        outcomes.setdefault(kind, set()).add(case["expected"]["outcome"])
    assert outcomes == {
        "COG": {"READY", "HOLD", "ERROR"},
        "MVT": {"READY", "HOLD", "ERROR"},
        "GEOPARQUET": {"READY", "HOLD", "ERROR"},
    }


def test_mvt_whitelist_violation_fails_closed():
    candidate = json.loads(json.dumps(_case("mvt-ready")["candidate"]))
    candidate["carrier"]["encoded_attributes"].append("secret")
    candidate["carrier"]["encoded_attributes"].sort()
    result = module.assess(candidate)
    assert result.outcome == "ERROR"
    assert "MVT_ATTRIBUTE_WHITELIST_VIOLATION" in result.reason_codes


def test_cog_small_raster_does_not_require_overviews():
    candidate = json.loads(json.dumps(_case("cog-ready")["candidate"]))
    candidate["carrier"]["width"] = 512
    candidate["carrier"]["height"] = 256
    candidate["carrier"]["overview_count"] = 0
    assert module.assess(candidate).outcome == "READY"


def test_geoparquet_missing_bbox_covering_is_advisory_only():
    result = module.assess(_case("geoparquet-ready-with-advisory")["candidate"])
    assert result.outcome == "READY"
    assert result.advisories == ("GEOPARQUET_BBOX_COVERING_RECOMMENDED",)


def test_geoparquet_layout_profile_is_required():
    candidate = json.loads(json.dumps(_case("geoparquet-ready-with-advisory")["candidate"]))
    del candidate["carrier"]["layout_profile"]
    result = module.assess(candidate)
    assert result.outcome == "ERROR"
    assert result.reason_codes == ("SCHEMA_INVALID",)


def test_geoparquet_row_group_targets_are_profile_specific():
    candidate = json.loads(json.dumps(_case("geoparquet-ready-with-advisory")["candidate"]))
    candidate["carrier"]["layout_profile"]["row_group_target_rows"] = 12000
    candidate["carrier"]["layout_profile"]["row_group_target_bytes"] = 67108864
    result = module.assess(candidate)
    assert result.outcome == "READY"
    assert "GEOPARQUET_BBOX_COVERING_RECOMMENDED" in result.advisories


def test_geoparquet_non_zstd_compression_is_advisory():
    candidate = json.loads(json.dumps(_case("geoparquet-ready-with-advisory")["candidate"]))
    candidate["carrier"]["layout_profile"]["compression"] = "SNAPPY"
    result = module.assess(candidate)
    assert result.outcome == "READY"
    assert "GEOPARQUET_ZSTD_RECOMMENDED" in result.advisories


def test_geoparquet_placeholder_benchmark_digest_fails_closed():
    candidate = json.loads(json.dumps(_case("geoparquet-ready-with-advisory")["candidate"]))
    candidate["carrier"]["layout_profile"]["benchmark_digest"] = module.ZERO_SHA256
    result = module.assess(candidate)
    assert result.outcome == "ERROR"
    assert "GEOPARQUET_BENCHMARK_DIGEST_PLACEHOLDER_DENIED" in result.reason_codes


def test_geoparquet_partition_version_matches_strategy():
    candidate = json.loads(json.dumps(_case("geoparquet-ready-with-advisory")["candidate"]))
    candidate["carrier"]["layout_profile"]["partition_strategy"] = "H3"
    result = module.assess(candidate)
    assert result.outcome == "HOLD"
    assert "GEOPARQUET_PARTITION_VERSION_REQUIRED" in result.reason_codes


def test_noncanonical_arrays_error():
    candidate = json.loads(json.dumps(_case("geoparquet-ready-with-advisory")["candidate"]))
    candidate["carrier"]["geometry_types"] = ["Polygon", "MultiPolygon"]
    result = module.assess(candidate)
    assert result.outcome == "ERROR"
    assert "NON_CANONICAL_ARRAY" in result.reason_codes


def test_validator_does_not_attempt_network():
    def denied(*_args, **_kwargs):
        raise AssertionError("network access attempted")

    with patch.object(socket.socket, "connect", denied), patch.object(socket, "create_connection", denied):
        for case in _cases():
            module.assess(case["candidate"])


def test_case_cli_contract(capsys):
    assert module.validate_cases() == 0
    output = capsys.readouterr().out
    assert "CONFIRMED: 9 geospatial carrier readiness cases passed exact polarity." in output
