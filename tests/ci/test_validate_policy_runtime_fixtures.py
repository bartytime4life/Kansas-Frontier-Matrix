#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


SCRIPT = Path("tools/ci/validate_policy_runtime_fixtures.py")
FULL_FIXTURES = {
    "answer_public_safe": {"scenario": "answer_public_safe", "expected": "ANSWER"},
    "abstain_missing_evidence": {"scenario": "abstain_missing_evidence", "expected": "ABSTAIN"},
    "deny_restricted_support": {"scenario": "deny_restricted_support", "expected": "DENY"},
    "error_policy_engine_unavailable": {
        "scenario": "error_policy_engine_unavailable",
        "expected": "ERROR",
    },
}


def _write_runtime_layout(root: Path) -> None:
    runtime_bundle = root / "policy/bundles/runtime"
    runtime_fixtures = root / "policy/fixtures/runtime"
    runtime_bundle.mkdir(parents=True, exist_ok=True)
    runtime_fixtures.mkdir(parents=True, exist_ok=True)

    (runtime_bundle / "bundle.yaml").write_text("name: runtime\n", encoding="utf-8")
    (runtime_bundle / "finite_outcomes.rego").write_text(
        'package kfm.runtime\ndefault outcome := "ABSTAIN"\n',
        encoding="utf-8",
    )
    (runtime_bundle / "runtime_denials.rego").write_text(
        "package kfm.runtime.denials\ndefault deny := false\n",
        encoding="utf-8",
    )
    (runtime_bundle / "proof_quartet.rego").write_text(
        "package kfm.runtime.proof\ndefault proof_quartet_ok := false\n",
        encoding="utf-8",
    )


def _write_runtime_fixtures(root: Path, fixtures: dict[str, dict[str, str]]) -> None:
    for name, payload in fixtures.items():
        (root / "policy/fixtures/runtime" / f"{name}.json").write_text(
            json.dumps(payload), encoding="utf-8"
        )


def _run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(SCRIPT), "--root", str(root)],
        check=False,
        capture_output=True,
        text=True,
    )


def test_validate_policy_runtime_fixtures_passes() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        _write_runtime_fixtures(root, FULL_FIXTURES)
        proc = _run_validator(root)

        assert proc.returncode == 0
        assert "validated 4 runtime fixtures" in proc.stdout


def test_validate_policy_runtime_fixtures_fails_when_outcome_coverage_incomplete() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures = {
            "answer_public_safe": {"scenario": "answer_public_safe", "expected": "ANSWER"},
            "abstain_missing_evidence": {"scenario": "abstain_missing_evidence", "expected": "ABSTAIN"},
            "deny_restricted_support": {"scenario": "deny_restricted_support", "expected": "DENY"},
        }
        _write_runtime_fixtures(root, fixtures)
        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "missing: ERROR" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_scenario_mismatch() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures = dict(FULL_FIXTURES)
        fixtures["error_policy_engine_unavailable"] = {
            "scenario": "error_name_mismatch",
            "expected": "ERROR",
        }
        _write_runtime_fixtures(root, fixtures)
        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "does not match filename stem" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_on_invalid_json_fixture() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures_dir = root / "policy/fixtures/runtime"
        (fixtures_dir / "answer_public_safe.json").write_text(
            json.dumps({"scenario": "answer_public_safe", "expected": "ANSWER"}),
            encoding="utf-8",
        )
        (fixtures_dir / "abstain_missing_evidence.json").write_text(
            json.dumps({"scenario": "abstain_missing_evidence", "expected": "ABSTAIN"}),
            encoding="utf-8",
        )
        (fixtures_dir / "deny_restricted_support.json").write_text(
            json.dumps({"scenario": "deny_restricted_support", "expected": "DENY"}),
            encoding="utf-8",
        )
        (fixtures_dir / "error_policy_engine_unavailable.json").write_text("{not-json", encoding="utf-8")

        proc = subprocess.run(
            ["python3", str(SCRIPT), "--root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )

        assert proc.returncode != 0
        assert "invalid JSON" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_runtime_scaffold_missing() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        # Remove one required runtime scaffold file.
        (root / "policy/bundles/runtime/proof_quartet.rego").unlink()

        _write_runtime_fixtures(root, FULL_FIXTURES)
        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "missing runtime policy file" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_on_duplicate_scenario_names() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures_dir = root / "policy/fixtures/runtime"
        _write_runtime_fixtures(root, FULL_FIXTURES)

        # Add a second fixture with a duplicate scenario value.
        (fixtures_dir / "answer_public_safe_duplicate.json").write_text(
            json.dumps({"scenario": "answer_public_safe", "expected": "ANSWER"}),
            encoding="utf-8",
        )

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "duplicate scenario 'answer_public_safe'" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_on_invalid_expected_outcome() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures = dict(FULL_FIXTURES)
        fixtures["error_policy_engine_unavailable"] = {
            "scenario": "error_policy_engine_unavailable",
            "expected": "BOGUS",
        }
        _write_runtime_fixtures(root, fixtures)
        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "invalid expected outcome 'BOGUS'" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_on_non_object_json_fixture() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures_dir = root / "policy/fixtures/runtime"
        (fixtures_dir / "answer_public_safe.json").write_text("[]", encoding="utf-8")
        (fixtures_dir / "abstain_missing_evidence.json").write_text(
            json.dumps({"scenario": "abstain_missing_evidence", "expected": "ABSTAIN"}),
            encoding="utf-8",
        )
        (fixtures_dir / "deny_restricted_support.json").write_text(
            json.dumps({"scenario": "deny_restricted_support", "expected": "DENY"}),
            encoding="utf-8",
        )
        (fixtures_dir / "error_policy_engine_unavailable.json").write_text(
            json.dumps({"scenario": "error_policy_engine_unavailable", "expected": "ERROR"}),
            encoding="utf-8",
        )

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "invalid top-level JSON type" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_runtime_fixture_directory_missing() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)

        runtime_bundle = root / "policy/bundles/runtime"
        runtime_bundle.mkdir(parents=True, exist_ok=True)
        (runtime_bundle / "bundle.yaml").write_text("name: runtime\n", encoding="utf-8")
        (runtime_bundle / "finite_outcomes.rego").write_text("package kfm.runtime\n", encoding="utf-8")
        (runtime_bundle / "runtime_denials.rego").write_text("package kfm.runtime.denials\n", encoding="utf-8")
        (runtime_bundle / "proof_quartet.rego").write_text("package kfm.runtime.proof\n", encoding="utf-8")

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "missing runtime fixtures directory" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_fixture_directory_empty() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "no runtime fixture JSON files found" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_scenario_key_missing() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures = dict(FULL_FIXTURES)
        fixtures["answer_public_safe"] = {"expected": "ANSWER"}
        _write_runtime_fixtures(root, fixtures)

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "missing required non-empty string key 'scenario'" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_scenario_key_empty() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures = dict(FULL_FIXTURES)
        fixtures["answer_public_safe"] = {"scenario": "", "expected": "ANSWER"}
        _write_runtime_fixtures(root, fixtures)

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "missing required non-empty string key 'scenario'" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_expected_key_missing() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures = dict(FULL_FIXTURES)
        fixtures["answer_public_safe"] = {"scenario": "answer_public_safe"}
        _write_runtime_fixtures(root, fixtures)

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "missing required non-empty string key 'expected'" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_expected_key_empty() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)

        fixtures = dict(FULL_FIXTURES)
        fixtures["answer_public_safe"] = {"scenario": "answer_public_safe", "expected": ""}
        _write_runtime_fixtures(root, fixtures)

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "missing required non-empty string key 'expected'" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_rego_package_declaration_missing() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)
        _write_runtime_fixtures(root, FULL_FIXTURES)

        (root / "policy/bundles/runtime/finite_outcomes.rego").write_text(
            "# deliberately invalid module\n",
            encoding="utf-8",
        )

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "runtime policy file missing package declaration" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_bundle_name_missing() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)
        _write_runtime_fixtures(root, FULL_FIXTURES)

        (root / "policy/bundles/runtime/bundle.yaml").write_text(
            "version: 1\n",
            encoding="utf-8",
        )

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "runtime policy bundle missing name field" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_when_required_rego_marker_missing() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)
        _write_runtime_fixtures(root, FULL_FIXTURES)

        (root / "policy/bundles/runtime/finite_outcomes.rego").write_text(
            "package kfm.runtime\ndefault outcome := \"DENY\"\n",
            encoding="utf-8",
        )

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "runtime policy file missing required marker 'ABSTAIN'" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_on_non_utf8_runtime_file() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)
        _write_runtime_fixtures(root, FULL_FIXTURES)

        (root / "policy/bundles/runtime/runtime_denials.rego").write_bytes(b"\xff\xfe")

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "non-utf8 runtime policy file" in proc.stderr


def test_validate_policy_runtime_fixtures_fails_on_non_utf8_fixture_file() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_runtime_layout(root)
        _write_runtime_fixtures(root, FULL_FIXTURES)

        (root / "policy/fixtures/runtime/answer_public_safe.json").write_bytes(b"\xff\xfe")

        proc = _run_validator(root)

        assert proc.returncode != 0
        assert "non-utf8 fixture JSON file" in proc.stderr
