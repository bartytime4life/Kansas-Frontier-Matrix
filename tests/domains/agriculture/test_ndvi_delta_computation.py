"""Tests for deterministic, no-network NDVI delta computation."""

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
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/generators/compute_ndvi_delta.py"
FIXTURE_PATH = ROOT / "fixtures/domains/agriculture/ndvi_delta_computation/cases.json"
SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/agriculture/ndvi_delta_computation.schema.json"

SPEC = importlib.util.spec_from_file_location("kfm_compute_ndvi_delta", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def _manifest() -> dict[str, object]:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def _case(case_id: str) -> dict[str, object]:
    case = next(item for item in _manifest()["cases"] if item["case_id"] == case_id)
    return copy.deepcopy(case)


def _schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def test_schema_is_valid_draft_2020_12() -> None:
    Draft202012Validator.check_schema(_schema())


def test_all_fixture_results_close_expected_arithmetic_and_schema() -> None:
    validator = Draft202012Validator(_schema())
    cases = _manifest()["cases"]
    assert len(cases) == 5
    for case in cases:
        result = MODULE.compute_ndvi_delta(case["request"])
        assert result["classification"] == case["expected_classification"]
        assert result["delta_ndvi_millionths"] == case["expected_delta_ndvi_millionths"]
        assert result["reasons"] == case["expected_reasons"]
        assert list(validator.iter_errors(result)) == []


def test_threshold_equality_and_strict_cloud_limit_are_frozen() -> None:
    gain = MODULE.compute_ndvi_delta(_case("gain-threshold-equality")["request"])
    cloudy = MODULE.compute_ndvi_delta(_case("cloud-filter-insufficient")["request"])
    assert gain["delta_ndvi_millionths"] == 120000
    assert gain["classification"] == "GAIN_CANDIDATE"
    assert cloudy["baseline"]["accepted_observation_ids"] == ["baseline-41"]
    assert cloudy["baseline"]["rejected_cloud_observation_ids"] == ["baseline-42"]


def test_request_order_does_not_change_result() -> None:
    request = _case("stable")["request"]
    reversed_request = copy.deepcopy(request)
    reversed_request["baseline"].reverse()
    reversed_request["recent"].reverse()
    assert MODULE.compute_ndvi_delta(request) == MODULE.compute_ndvi_delta(reversed_request)


def test_invalid_clear_zero_denominator_fails_closed() -> None:
    request = _case("stable")["request"]
    request["baseline"][0]["nir_scaled_int"] = 0
    request["baseline"][0]["red_scaled_int"] = 0
    with pytest.raises(MODULE.InputError, match="zero NDVI denominator"):
        MODULE.compute_ndvi_delta(request)


def test_duplicate_or_cross_window_observation_id_fails_closed() -> None:
    duplicate = _case("stable")["request"]
    duplicate["baseline"][1]["observation_id"] = duplicate["baseline"][0]["observation_id"]
    with pytest.raises(MODULE.InputError, match="must be unique"):
        MODULE.compute_ndvi_delta(duplicate)

    overlap = _case("stable")["request"]
    overlap["recent"][0]["observation_id"] = overlap["baseline"][0]["observation_id"]
    with pytest.raises(MODULE.InputError, match="must be disjoint"):
        MODULE.compute_ndvi_delta(overlap)


def test_digests_are_stable_and_result_authority_is_false() -> None:
    request = _case("loss")["request"]
    first = MODULE.compute_ndvi_delta(request)
    second = MODULE.compute_ndvi_delta(request)
    assert first == second
    assert first["input_digest"].startswith("sha256:")
    assert first["result_digest"].startswith("sha256:")
    assert all(
        value is False
        for key, value in first["governance"].items()
        if key != "execution_mode"
    )


def test_computation_does_not_open_network() -> None:
    def denied(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("network access denied")

    with mock.patch.object(socket, "socket", denied), mock.patch.object(
        socket, "create_connection", denied
    ), mock.patch.object(socket, "getaddrinfo", denied):
        assert MODULE.compute_ndvi_delta(_case("stable")["request"])["classification"] == "STABLE"


def test_cli_emits_stdout_and_does_not_create_outputs(tmp_path: Path) -> None:
    request_path = tmp_path / "request.json"
    request_path.write_text(json.dumps(_case("gain-threshold-equality")["request"]), encoding="utf-8")
    before = set(tmp_path.iterdir())
    completed = subprocess.run(
        [sys.executable, str(MODULE_PATH), "--input", str(request_path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert json.loads(completed.stdout)["classification"] == "GAIN_CANDIDATE"
    assert set(tmp_path.iterdir()) == before
