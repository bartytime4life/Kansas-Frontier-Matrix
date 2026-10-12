"""CLI handoff to the bounded validator, without operational telemetry."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from kfm_cli.cli import TELEMETRY_PROFILES, build_app


runner = CliRunner()


def _report(outcome: str, profiles: dict[str, str]) -> dict[str, object]:
    return {
        "authority": "NONE", "execution_mode": "FIXTURE_ONLY_NO_NETWORK",
        "outcome": outcome, "profiles": profiles,
        "scope": "bounded_telemetry_profile_validation_only",
    }


def test_telemetry_fixtures_delegate_to_existing_validator() -> None:
    report = _report("PASS", dict.fromkeys(TELEMETRY_PROFILES, "PASS"))
    with patch("kfm_cli.cli.subprocess.run", return_value=subprocess.CompletedProcess(
        [], 0, json.dumps(report), ""
    )) as run:
        result = runner.invoke(build_app(), ["telemetry", "--fixtures"])
    assert result.exit_code == 0
    assert json.loads(result.stdout) == report
    assert run.call_args.args[0][-1] == "--fixtures"
    assert run.call_args.kwargs["cwd"].is_dir()


def test_relative_candidate_from_another_directory_is_passed_as_absolute(tmp_path) -> None:
    candidate = tmp_path / "candidate.json"
    candidate.write_text("{}", encoding="utf-8")
    previous = Path.cwd()
    try:
        os.chdir(tmp_path)
        with patch("kfm_cli.cli.subprocess.run", return_value=subprocess.CompletedProcess(
            [], 1, json.dumps(_report("DENY", {"map_build_sustainability": "DENY"})), ""
        )) as run:
            result = runner.invoke(build_app(), [
                "telemetry", "--candidate", "candidate.json",
                "--profile", "map_build_sustainability",
            ])
    finally:
        os.chdir(previous)
    assert result.exit_code == 1
    assert json.loads(result.stdout)["outcome"] == "DENY"
    assert str(candidate) in run.call_args.args[0]
    assert str(candidate) not in result.stdout


def test_invalid_handoff_is_error_without_child_output_or_candidate_path(tmp_path) -> None:
    candidate = tmp_path / "secret.json"
    with patch("kfm_cli.cli.subprocess.run", return_value=subprocess.CompletedProcess(
        [], 0, '{"authority":"NONE","outcome":"DENY","secret":"raw"}',
        "secret: raw"
    )):
        result = runner.invoke(build_app(), [
            "telemetry", "--candidate", str(candidate), "--profile", "trace_receipt_link"
        ])
    assert result.exit_code == 1
    assert json.loads(result.stdout)["outcome"] == "ERROR"
    assert "raw" not in result.stdout
    assert str(candidate) not in result.stdout


def test_candidate_requires_explicit_profile() -> None:
    result = runner.invoke(build_app(), ["telemetry", "--candidate", "secret.json"])
    assert result.exit_code != 0
    assert "secret.json" not in result.stdout
