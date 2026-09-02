"""Deterministic no-network tests for the CSV-to-GeoJSON preflight."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
from unittest.mock import patch

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/ingest/csv_geojson_preflight/preflight.py"
FIXTURES = ROOT / "fixtures/ingest/csv_geojson_preflight"
SCHEMA_PATH = ROOT / "schemas/contracts/v1/source/csv_geojson_normalization_candidate.schema.json"

spec = importlib.util.spec_from_file_location("csv_geojson_preflight", MODULE_PATH)
assert spec and spec.loader
preflight = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = preflight
spec.loader.exec_module(preflight)


def candidate(csv_name: str = "valid.csv"):
    return preflight.normalize_files(FIXTURES / "profile.json", FIXTURES / csv_name)


def test_valid_candidate_is_deterministic_schema_valid_and_sorted():
    first = candidate()
    second = candidate()
    assert first == second
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema).validate(first)
    features = first["result"]["feature_collection"]["features"]
    assert [item["properties"]["source_row_id"] for item in features] == [
        "fixture-a",
        "fixture-b",
        "fixture-c",
    ]
    assert features[0]["geometry"]["coordinates"] == [-98.5, 38.5]
    assert first["result"]["feature_count"] == 3
    assert first["input"]["row_count"] == 3


def test_identity_and_hashes_are_stable_and_bound_to_input(tmp_path):
    baseline = candidate()
    changed_csv = tmp_path / "changed.csv"
    changed_csv.write_text(
        (FIXTURES / "valid.csv").read_text(encoding="utf-8").replace(
            "fixture point b", "fixture point b changed"
        ),
        encoding="utf-8",
    )
    changed = preflight.normalize_files(FIXTURES / "profile.json", changed_csv)
    assert baseline["candidate_id"] != changed["candidate_id"]
    assert baseline["spec_hash"] != changed["spec_hash"]
    assert baseline["input"]["content_digest"] != changed["input"]["content_digest"]
    assert baseline["result"]["feature_collection_digest"] != changed["result"][
        "feature_collection_digest"
    ]
    baseline_ids = [item["id"] for item in baseline["result"]["feature_collection"]["features"]]
    changed_ids = [item["id"] for item in changed["result"]["feature_collection"]["features"]]
    assert baseline_ids == changed_ids


@pytest.mark.parametrize(
    "fixture_name,reason_code",
    [
        ("invalid_duplicate_id.csv", "DUPLICATE_ROW_ID"),
        ("invalid_coordinate.csv", "COORDINATE_OUT_OF_RANGE"),
        ("invalid_formula.csv", "FORMULA_LIKE_CELL"),
    ],
)
def test_invalid_fixtures_fail_closed_without_values(fixture_name, reason_code):
    with pytest.raises(preflight.PreflightError) as captured:
        candidate(fixture_name)
    assert captured.value.reason_code == reason_code
    report = captured.value.as_report()
    assert report["outcome"] == "QUARANTINE_CANDIDATE"
    assert not report["authority_created"]
    assert not report["lifecycle_write_allowed"]
    assert not report["network_accessed"]
    assert not report["publication_allowed"]
    assert "fixture point" not in json.dumps(report)


def test_exact_header_order_and_no_partial_output(tmp_path):
    invalid = tmp_path / "headers.csv"
    invalid.write_text(
        "record_id,longitude,latitude,fixture_area,label\n"
        "fixture-a,-98.5,38.5,SYNTHETIC-001,fixture point a\n",
        encoding="utf-8",
    )
    with pytest.raises(preflight.PreflightError, match="headers do not match") as captured:
        preflight.normalize_files(FIXTURES / "profile.json", invalid)
    assert captured.value.reason_code == "CSV_HEADER_MISMATCH"


def test_profile_is_exact_fixture_only_and_mapping_closed(tmp_path):
    raw = json.loads((FIXTURES / "profile.json").read_text(encoding="utf-8"))
    raw["execution_mode"] = "LIVE"
    path = tmp_path / "profile.json"
    path.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(preflight.PreflightError) as captured:
        preflight.load_profile(path)
    assert captured.value.reason_code == "EXECUTION_MODE_NOT_ADMITTED"

    raw["execution_mode"] = "FIXTURE_ONLY"
    raw["unexpected"] = True
    path.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(preflight.PreflightError) as captured:
        preflight.load_profile(path)
    assert captured.value.reason_code == "PROFILE_FIELDS_INVALID"


def test_symlink_input_is_rejected(tmp_path):
    target = tmp_path / "target.csv"
    target.write_bytes((FIXTURES / "valid.csv").read_bytes())
    link = tmp_path / "link.csv"
    try:
        link.symlink_to(target)
    except (OSError, NotImplementedError):
        pytest.skip("symlinks are unavailable")
    with pytest.raises(preflight.PreflightError) as captured:
        preflight.normalize_files(FIXTURES / "profile.json", link)
    assert captured.value.reason_code == "INPUT_UNREADABLE"


def test_cli_success_is_atomic_non_overwriting_and_value_minimized(tmp_path):
    output = tmp_path / "candidate.json"
    command = [
        sys.executable,
        str(MODULE_PATH),
        "--profile",
        str(FIXTURES / "profile.json"),
        "--csv",
        str(FIXTURES / "valid.csv"),
        "--output",
        str(output),
    ]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    assert completed.returncode == 0, completed.stderr
    summary = json.loads(completed.stdout)
    assert summary["outcome"] == "NORMALIZED_CANDIDATE"
    assert summary["feature_count"] == 3
    assert output.is_file()

    original = output.read_bytes()
    second = subprocess.run(command, check=False, capture_output=True, text=True)
    assert second.returncode == 2
    failure = json.loads(second.stdout)
    assert failure["reason_code"] == "OUTPUT_ALREADY_EXISTS"
    assert output.read_bytes() == original


def test_cli_quarantine_creates_no_output(tmp_path):
    output = tmp_path / "candidate.json"
    completed = subprocess.run(
        [
            sys.executable,
            str(MODULE_PATH),
            "--profile",
            str(FIXTURES / "profile.json"),
            "--csv",
            str(FIXTURES / "invalid_coordinate.csv"),
            "--output",
            str(output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 2
    assert not output.exists()
    assert json.loads(completed.stdout)["reason_code"] == "COORDINATE_OUT_OF_RANGE"


def test_import_and_execution_do_not_touch_ambient_network(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    boom = AssertionError("ambient network")
    with (
        patch.object(socket.socket, "connect", side_effect=boom),
        patch.object(socket.socket, "connect_ex", side_effect=boom),
        patch.object(socket, "create_connection", side_effect=boom),
        patch.object(socket, "getaddrinfo", side_effect=boom),
    ):
        result = candidate()
    assert result["governance"] == {
        "authority_created": False,
        "evidence_created": False,
        "fixture_only": True,
        "lifecycle_write_allowed": False,
        "network_accessed": False,
        "policy_decided": False,
        "publication_allowed": False,
        "release_created": False,
        "source_activated": False,
    }


def test_static_boundary_has_no_network_lifecycle_or_release_clients():
    source = MODULE_PATH.read_text(encoding="utf-8")
    forbidden = (
        "import requests",
        "import httpx",
        "import aiohttp",
        "import urllib.request",
        "import socket",
        "import subprocess",
        "data/raw",
        "data/work",
        "data/quarantine",
        "data/processed",
        "data/catalog",
        "data/published",
        "release/",
        "api.waterdata.usgs.gov",
        "usgs.gov",
    )
    assert all(token not in source for token in forbidden)
