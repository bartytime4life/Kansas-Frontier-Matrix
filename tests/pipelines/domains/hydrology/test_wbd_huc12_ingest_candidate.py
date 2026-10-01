"""Tests for the fixture-first WBD HUC12 ingest candidate producer."""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = (
    REPO_ROOT
    / "pipelines/domains/hydrology/ingest_wbd_huc/produce_wbd_huc12_candidate.py"
)
FIXTURES = REPO_ROOT / "fixtures/domains/hydrology/wbd_huc12_ingest"

SPEC = importlib.util.spec_from_file_location("kfm_wbd_huc12_ingest_candidate", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def load(kind: str, name: str) -> dict[str, object]:
    value = json.loads((FIXTURES / kind / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_metadata_churn_becomes_no_change_receipt() -> None:
    package = load("valid", "no_change.json")
    first = MODULE.build_candidate(package)
    second = MODULE.build_candidate(copy.deepcopy(package))
    assert first == second
    assert first.ok and first.output
    assert first.output["disposition"] == "NO_CHANGE_RECEIPT"
    assert first.output["reason_codes"] == ["CONTENT_UNCHANGED"]
    assert first.output["assessment"]["decision"] == {
        "change_types": [],
        "outcome": "NO_CHANGE",
    }


def test_material_geometry_change_becomes_raw_candidate() -> None:
    result = MODULE.build_candidate(load("valid", "material_change.json"))
    assert result.ok and result.output
    assert result.output["disposition"] == "RAW_CANDIDATE"
    assert result.output["reason_codes"] == ["FEATURE_MATERIAL_CHANGE"]
    assert result.output["assessment"]["decision"] == {
        "change_types": ["geometry_change"],
        "outcome": "MATERIAL_CHANGE",
    }


def test_add_and_remove_become_raw_candidates() -> None:
    added = MODULE.build_candidate(load("valid", "add.json"))
    removed = MODULE.build_candidate(load("valid", "remove.json"))
    assert added.ok and added.output
    assert removed.ok and removed.output
    assert added.output["disposition"] == "RAW_CANDIDATE"
    assert added.output["reason_codes"] == ["FEATURE_ADDED"]
    assert added.output["assessment"]["decision"] == {
        "change_types": ["added"],
        "outcome": "ADD",
    }
    assert removed.output["disposition"] == "RAW_CANDIDATE"
    assert removed.output["reason_codes"] == ["FEATURE_REMOVED"]
    assert removed.output["assessment"]["decision"] == {
        "change_types": ["removed"],
        "outcome": "REMOVE",
    }


def test_http_not_modified_never_synthesizes_current_bytes() -> None:
    result = MODULE.build_candidate(load("valid", "not_modified.json"))
    assert result.ok and result.output
    assert result.output["assessment"] is None
    assert result.output["disposition"] == "NO_CHANGE_RECEIPT"
    assert result.output["reason_codes"] == ["HTTP_NOT_MODIFIED"]
    assert result.output["request_evidence"]["body_sha256"] is None


def test_duplicate_huc12_fails_closed() -> None:
    result = MODULE.build_candidate(load("invalid", "duplicate_huc12.json"))
    assert not result.ok
    assert MODULE.Finding(
        "FEATURE_DUPLICATE_HUC12",
        "/response/feature_collection/features",
    ) in result.findings


def test_response_body_hash_mismatch_fails_closed() -> None:
    package = load("valid", "no_change.json")
    package["response"]["body_sha256"] = "sha256:" + ("0" * 64)
    package["spec_hash"] = MODULE.canonical_hash(package)
    result = MODULE.build_candidate(package)
    assert not result.ok
    assert MODULE.Finding(
        "RESPONSE_BODY_HASH_MISMATCH",
        "/response/body_sha256",
    ) in result.findings


def test_source_package_spec_hash_mismatch_fails_closed() -> None:
    package = load("valid", "no_change.json")
    package["observed_at"] = "2026-04-11T18:00:01Z"
    result = MODULE.build_candidate(package)
    assert not result.ok
    assert MODULE.Finding(
        "SOURCE_PACKAGE_SPEC_HASH_MISMATCH",
        "/spec_hash",
    ) in result.findings


@pytest.mark.parametrize(
    ("literal", "reason"),
    [
        ("1e999", "JSON_NONFINITE_NUMBER"),
        ("-1e999", "JSON_NONFINITE_NUMBER"),
        ("1" * 5000, "JSON_INVALID"),
    ],
)
def test_extreme_numeric_input_has_finite_cli_diagnostic(
    tmp_path: Path, literal: str, reason: str
) -> None:
    fixture = (FIXTURES / "valid/no_change.json").read_text(encoding="utf-8")
    target = '"areasqkm": 12.3456784'
    assert fixture.count(target) == 1
    source = tmp_path / "extreme.json"
    source.write_text(fixture.replace(target, f'"areasqkm": {literal}'), encoding="utf-8")

    completed = subprocess.run(
        [sys.executable, str(MODULE_PATH), str(source)],
        check=False, capture_output=True, text=True,
    )

    assert completed.returncode == 2
    assert json.loads(completed.stdout)["findings"] == [{"code": reason, "path": "/"}]
    assert completed.stderr == ""


def test_nonfinite_programmatic_package_has_finite_diagnostic() -> None:
    package = load("valid", "no_change.json")
    package["response"]["feature_collection"]["features"][0]["properties"]["areasqkm"] = float("inf")

    result = MODULE.build_candidate(package)

    assert not result.ok
    assert result.findings == (MODULE.Finding("SOURCE_PACKAGE_CANONICALIZATION_INVALID", "/"),)


def test_cli_is_deterministic_and_value_bounded() -> None:
    fixture = FIXTURES / "valid/no_change.json"
    first = subprocess.run(
        [sys.executable, str(MODULE_PATH), str(fixture)],
        check=False,
        capture_output=True,
        text=True,
    )
    second = subprocess.run(
        [sys.executable, str(MODULE_PATH), str(fixture)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert first.returncode == 0
    assert first.stdout == second.stdout
    result = json.loads(first.stdout)
    assert result["governance"] == {
        "fixture_only": True,
        "lifecycle_write": False,
        "network_fetch": False,
        "promotion_allowed": False,
        "publication_allowed": False,
        "release_allowed": False,
        "source_activation": False,
    }


def test_cli_does_not_overwrite_output(tmp_path: Path) -> None:
    fixture = FIXTURES / "valid/no_change.json"
    output = tmp_path / "candidate.json"
    output.write_text("preserve", encoding="utf-8")
    completed = subprocess.run(
        [
            sys.executable,
            str(MODULE_PATH),
            str(fixture),
            "--output",
            str(output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 2
    assert output.read_text(encoding="utf-8") == "preserve"
    payload = json.loads(completed.stdout)
    assert payload["findings"] == [{"code": "OUTPUT_PATH_UNSAFE", "path": "/"}]


def test_cli_creates_external_output_without_overwrite(tmp_path: Path) -> None:
    output = tmp_path / "candidate.json"
    completed = subprocess.run(
        [sys.executable, str(MODULE_PATH), str(FIXTURES / "valid/no_change.json"),
         "--output", str(output)],
        check=False, capture_output=True, text=True,
    )

    assert completed.returncode == 0
    assert json.loads(output.read_text(encoding="utf-8")) == json.loads(completed.stdout)
    assert output.stat().st_mode & 0o077 == 0


def test_cli_rejects_symlinked_output_parent(tmp_path: Path) -> None:
    destination = tmp_path / "destination"
    destination.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(destination, target_is_directory=True)
    completed = subprocess.run(
        [sys.executable, str(MODULE_PATH), str(FIXTURES / "valid/no_change.json"),
         "--output", str(alias / "candidate.json")],
        check=False, capture_output=True, text=True,
    )

    assert completed.returncode == 2
    assert json.loads(completed.stdout)["findings"] == [
        {"code": "OUTPUT_PATH_UNSAFE", "path": "/"}
    ]
    assert not (destination / "candidate.json").exists()


def test_cli_rejects_dangling_output_symlink(tmp_path: Path) -> None:
    target = tmp_path / "missing.json"
    output = tmp_path / "candidate.json"
    output.symlink_to(target)
    completed = subprocess.run(
        [sys.executable, str(MODULE_PATH), str(FIXTURES / "valid/no_change.json"),
         "--output", str(output)],
        check=False, capture_output=True, text=True,
    )

    assert completed.returncode == 2
    assert json.loads(completed.stdout)["findings"] == [
        {"code": "OUTPUT_PATH_UNSAFE", "path": "/"}
    ]
    assert output.is_symlink() and not target.exists()


def test_output_rejects_repository_lifecycle_path_before_write(monkeypatch: pytest.MonkeyPatch) -> None:
    def unexpected_tempfile(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("repository lifecycle output was opened")

    monkeypatch.setattr(MODULE.tempfile, "mkstemp", unexpected_tempfile)
    output = REPO_ROOT / "data/raw/hydrology/wbd-huc12-test-output.json"
    with pytest.raises(OSError, match="OUTPUT_PATH_UNSAFE"):
        MODULE.write_output(output, "{}")


def test_output_link_failure_leaves_no_partial_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def fail_link(*_args: object, **_kwargs: object) -> None:
        raise OSError("synthetic link failure")

    monkeypatch.setattr(MODULE.os, "link", fail_link)
    with pytest.raises(OSError, match="OUTPUT_PATH_UNSAFE"):
        MODULE.write_output(tmp_path / "candidate.json", "{}")
    assert not list(tmp_path.iterdir())
