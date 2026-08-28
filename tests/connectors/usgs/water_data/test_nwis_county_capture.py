"""Tests for the captured-input-only NWIS county normalizer."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
from unittest import mock

import pytest
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = ROOT / "connectors/usgs/water_data/nwis_county_capture.py"
FIXTURE_PATH = ROOT / "fixtures/connectors/usgs/water_data/nwis_county_capture/valid_capture.json"
SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/hydrology/nwis_county_capture_manifest.schema.json"

SPEC = importlib.util.spec_from_file_location("kfm_nwis_county_capture", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def _fixture() -> dict[str, object]:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def _schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def test_schema_is_valid_draft_2020_12() -> None:
    Draft202012Validator.check_schema(_schema())


def test_request_plan_uses_modern_api_without_credentials() -> None:
    location = MODULE.build_monitoring_location_request("20045")
    daily = MODULE.build_daily_request(
        "USGS-00000001", "2026-07-01", "2026-07-03", "00060", "00003"
    )
    assert location["url"] == (
        "https://api.waterdata.usgs.gov/ogcapi/v0/collections/monitoring-locations/items"
        "?f=json&county_code=20045&limit=1000"
    )
    assert daily["url"] == (
        "https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily/items"
        "?f=json&monitoring_location_id=USGS-00000001&parameter_code=00060"
        "&statistic_id=00003&datetime=2026-07-01%2F2026-07-03&limit=1000"
    )
    assert location["api_key_included"] is False
    assert daily["api_key_included"] is False
    assert "api_key" not in location["url"] + daily["url"]


def test_normalization_is_deterministic_schema_valid_and_sorted() -> None:
    request = _fixture()
    first = MODULE.normalize_capture(request)
    reordered = copy.deepcopy(request)
    reordered["daily_value_captures"].reverse()
    second = MODULE.normalize_capture(reordered)
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    assert list(validator.iter_errors(first)) == []
    assert first == second
    assert [item["monitoring_location_id"] for item in first["monitoring_locations"]] == [
        "USGS-00000001",
        "USGS-00000002",
    ]
    assert [item["feature_id"] for item in first["observations"]] == [
        "fixture-daily-001",
        "fixture-daily-002",
        "fixture-daily-003",
    ]
    subject = {key: value for key, value in first.items() if key != "result_digest"}
    assert first["result_digest"] == MODULE._canonical_digest(subject)


def test_values_and_approval_states_are_preserved_without_coercion() -> None:
    result = MODULE.normalize_capture(_fixture())
    assert [item["value"] for item in result["observations"]] == ["12.30", "13.10", "4.20"]
    assert [item["approval_status"] for item in result["observations"]] == [
        "Approved",
        "Provisional",
        "Approved",
    ]
    assert result["summary"] == {
        "monitoring_location_count": 2,
        "observation_count": 3,
        "approved_count": 2,
        "provisional_count": 1,
        "first_observation_date": "2026-07-01",
        "last_observation_date": "2026-07-02",
    }


def test_cross_county_location_fails_closed() -> None:
    request = _fixture()
    request["monitoring_location_pages"][0]["features"][0]["properties"]["county_code"] = "20091"
    with pytest.raises(MODULE.CaptureError, match="does not match the request county"):
        MODULE.normalize_capture(request)

    wrong_state = _fixture()
    wrong_state["monitoring_location_pages"][0]["features"][0]["properties"]["state_code"] = "19"
    with pytest.raises(MODULE.CaptureError, match="state_code is not Kansas"):
        MODULE.normalize_capture(wrong_state)


def test_unknown_or_cross_location_daily_capture_fails_closed() -> None:
    unknown = _fixture()
    unknown["daily_value_captures"][0]["monitoring_location_id"] = "USGS-99999999"
    with pytest.raises(MODULE.CaptureError, match="unknown monitoring location"):
        MODULE.normalize_capture(unknown)

    cross = _fixture()
    cross["daily_value_captures"][0]["pages"][0]["features"][0]["properties"][
        "monitoring_location_id"
    ] = "USGS-00000001"
    with pytest.raises(MODULE.CaptureError, match="wrong location capture"):
        MODULE.normalize_capture(cross)


def test_parameter_statistic_and_time_drift_fail_closed() -> None:
    parameter = _fixture()
    parameter["daily_value_captures"][0]["pages"][0]["features"][0]["properties"][
        "parameter_code"
    ] = "00065"
    with pytest.raises(MODULE.CaptureError, match="does not match the request"):
        MODULE.normalize_capture(parameter)

    outside = _fixture()
    outside["daily_value_captures"][0]["pages"][0]["features"][0]["properties"][
        "time"
    ] = "2026-06-30"
    with pytest.raises(MODULE.CaptureError, match="outside the requested interval"):
        MODULE.normalize_capture(outside)


def test_incomplete_or_credential_bearing_pagination_fails_closed() -> None:
    incomplete = _fixture()
    incomplete["monitoring_location_pages"][0]["links"].append(
        {
            "rel": "next",
            "href": "https://api.waterdata.usgs.gov/ogcapi/v0/collections/monitoring-locations/items?county_code=20045&offset=2&limit=2",
        }
    )
    with pytest.raises(MODULE.CaptureError, match="final page has a next link"):
        MODULE.normalize_capture(incomplete)

    secret = _fixture()
    secret["monitoring_location_pages"][0]["links"].append(
        {
            "rel": "next",
            "href": "https://api.waterdata.usgs.gov/ogcapi/v0/collections/monitoring-locations/items?county_code=20045&offset=2&api_key=secret",
        }
    )
    with pytest.raises(MODULE.CaptureError, match="must not embed an API key"):
        MODULE.normalize_capture(secret)


def test_output_omits_geometry_and_has_no_authority() -> None:
    result = MODULE.normalize_capture(_fixture())
    serialized = json.dumps(result, sort_keys=True)
    assert '"geometry"' not in serialized
    assert all(
        value is False
        for key, value in result["governance"].items()
        if key != "execution_mode"
    )


def test_normalizer_does_not_open_network_or_read_credentials() -> None:
    def denied(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("network access denied")

    with mock.patch.object(socket, "socket", denied), mock.patch.object(
        socket, "create_connection", denied
    ), mock.patch.object(socket, "getaddrinfo", denied), mock.patch.dict(
        "os.environ", {"USGS_API_KEY": "must-not-be-read"}, clear=False
    ):
        result = MODULE.normalize_capture(_fixture())
    assert result["governance"]["network_attempted"] is False
    assert result["governance"]["credentials_read"] is False
    assert "must-not-be-read" not in json.dumps(result)


def test_duplicate_json_member_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.json"
    path.write_text('{"profile":"one","profile":"two"}', encoding="utf-8")
    with pytest.raises(MODULE.CaptureError, match="duplicate JSON member"):
        MODULE.load_capture(path)


def test_cli_emits_stdout_only(tmp_path: Path) -> None:
    capture_path = tmp_path / "capture.json"
    capture_path.write_text(json.dumps(_fixture()), encoding="utf-8")
    before = set(tmp_path.iterdir())
    completed = subprocess.run(
        [sys.executable, str(MODULE_PATH), "--input", str(capture_path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert json.loads(completed.stdout)["object_type"] == "NwisCountyCaptureManifest"
    assert set(tmp_path.iterdir()) == before
