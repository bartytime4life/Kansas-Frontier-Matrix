from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tools.validators.watchers.validate_watcher_gate_packet import (
    FIXTURE_ROOT,
    PACKET_SCHEMA_PATH,
    PROFILE_PATH,
    PROFILE_SCHEMA_PATH,
    REPO_ROOT,
    validate_packet,
)


def _canonical_without(value: dict, field: str = "spec_hash") -> bytes:
    return json.dumps(
        {key: item for key, item in value.items() if key != field},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def test_profile_and_packet_schemas_are_valid() -> None:
    for path in (PROFILE_SCHEMA_PATH, PACKET_SCHEMA_PATH):
        Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))


def test_profile_hash_is_bound_to_canonical_content() -> None:
    profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    declared = profile["spec_hash"]
    computed = "sha256:" + hashlib.sha256(_canonical_without(profile)).hexdigest()
    assert declared == computed


def test_valid_fixtures_match_expected_outputs() -> None:
    manifest = json.loads((FIXTURE_ROOT / "valid/expected_outputs_manifest.json").read_text(encoding="utf-8"))
    assert len(manifest) == 3
    for name, expected in sorted(manifest.items()):
        result = validate_packet(FIXTURE_ROOT / "valid" / name)
        assert result.ok, result.findings
        assert result.packet is not None
        assert {"decision": result.packet["decision"], "exit_code": result.packet["process_exit_code"]} == expected
        assert result.packet["governance"]["promotion_authorized"] is False


def test_invalid_fixtures_match_exact_reviewed_codes() -> None:
    manifest = json.loads((FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
    assert len(manifest) == 5
    for name, expected in sorted(manifest.items()):
        result = validate_packet(FIXTURE_ROOT / "invalid" / name)
        assert not result.ok
        assert sorted({item.code for item in result.findings}) == sorted(expected)


def test_boundary_scores_are_deterministic() -> None:
    source = json.loads((FIXTURE_ROOT / "valid/valid_green.json").read_text(encoding="utf-8"))
    source["score"] = 80
    source["decision"] = "GREEN"
    source["reason_codes"] = ["ALL_GATES_GREEN"]
    source["obligations"] = []
    source["process_exit_code"] = 0
    source["spec_hash"] = "sha256:" + hashlib.sha256(_canonical_without(source)).hexdigest()
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "score-80.json"
        path.write_text(json.dumps(source), encoding="utf-8")
        result = validate_packet(path)
    assert result.ok, result.findings


def test_cloud_threshold_is_strictly_above() -> None:
    source = json.loads((FIXTURE_ROOT / "valid/valid_green.json").read_text(encoding="utf-8"))
    source["prefilter"]["median_cloud_percent"] = 40.0
    source["spec_hash"] = "sha256:" + hashlib.sha256(_canonical_without(source)).hexdigest()
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "cloud-40.json"
        path.write_text(json.dumps(source), encoding="utf-8")
        result = validate_packet(path)
    assert result.ok, result.findings


def test_profile_tampering_fails_closed() -> None:
    profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    profile["thresholds"]["green_score_min"] = 90
    with tempfile.TemporaryDirectory() as directory:
        profile_path = Path(directory) / "profile.json"
        profile_path.write_text(json.dumps(profile), encoding="utf-8")
        result = validate_packet(FIXTURE_ROOT / "valid/valid_green.json", profile_path)
    assert sorted({item.code for item in result.findings}) == ["PROFILE_HASH_MISMATCH"]


def test_fixture_cli_passes_without_echoing_artifact_refs() -> None:
    result = subprocess.run(
        [sys.executable, "tools/validators/watchers/validate_watcher_gate_packet.py", "--fixtures"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert '"decision":"DENY"' in result.stdout
    assert "fixture://watcher-gate/run-receipt" not in result.stdout


def test_duplicate_keys_and_nonfinite_numbers_fail_closed(tmp_path: Path) -> None:
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"packet_id":"a","packet_id":"b"}', encoding="utf-8")
    assert [item.code for item in validate_packet(duplicate).findings] == ["JSON_DUPLICATE_KEY"]
    nonfinite = tmp_path / "nonfinite.json"
    nonfinite.write_text('{"score":NaN}', encoding="utf-8")
    assert [item.code for item in validate_packet(nonfinite).findings] == ["JSON_NONFINITE_NUMBER"]
