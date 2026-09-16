"""Exercise the summary CI shell and preserve scheduling after a prior failure.

These checks do not evaluate GitHub expressions or prove hosted execution.
The real summary regressions run beside this module in the Make target.
"""

from pathlib import Path
import os
import subprocess

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/promotion-gate.yml"
STEP = "Test normalized-summary structure and compatibility"


def workflow():
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def test_summary_regressions_run_after_prior_failure_without_neutralizing_it():
    document = workflow()
    assert document["permissions"] == {"contents": "read"}
    assert "pull_request" in document["on"]
    assert document["on"]["push"]["branches"] == ["main"]
    assert "paths" not in document["on"]["push"]
    assert document["on"]["pull_request"] is None
    job = document["jobs"]["doctrine-artifact-prereq"]
    matches = [step for step in job["steps"] if step.get("name") == STEP]
    assert len(matches) == 1
    step = matches[0]
    assert step["if"] == "${{ !cancelled() }}"
    assert step["shell"] == "bash"
    assert not job.get("continue-on-error", False)
    assert not step.get("continue-on-error", False)
    assert any(s.get("run") == "python tools/ci/install_python_ci.py project-test"
               for s in job["steps"])


@pytest.mark.parametrize("exit_code", [0, 1, 7])
def test_summary_shell_propagates_command_failure(tmp_path, exit_code):
    step = next(s for s in workflow()["jobs"]["doctrine-artifact-prereq"]["steps"]
                if s.get("name") == STEP)
    assert step["run"].splitlines() == ["set -euo pipefail", "make normalized-summary-check"]
    fake_make = tmp_path / "make"
    fake_make.write_text('#!/bin/sh\nprintf "%s\\n" "$*" > "$KFM_TEST_CALLS"\nexit "$KFM_TEST_EXIT"\n')
    fake_make.chmod(0o700)
    calls = tmp_path / "calls"
    result = subprocess.run(
        ["/bin/bash", "--noprofile", "--norc", "-c", step["run"]],
        env={**os.environ, "PATH": str(tmp_path), "KFM_TEST_CALLS": str(calls),
             "KFM_TEST_EXIT": str(exit_code)},
        cwd=tmp_path, capture_output=True, text=True, timeout=5, check=False,
    )
    assert calls.read_text() == "normalized-summary-check\n"
    assert result.returncode == exit_code


def test_summary_renders_literal_command_without_executing_it(tmp_path):
    step = next(s for s in workflow()["jobs"]["doctrine-artifact-prereq"]["steps"]
                if s.get("name") == "Record normalized-summary coverage boundary")
    summary = tmp_path / "summary.md"
    result = subprocess.run(
        ["/bin/bash", "--noprofile", "--norc", "-e", "-c", step["run"]],
        env={**os.environ, "PATH": str(tmp_path), "GITHUB_STEP_SUMMARY": str(summary)},
        cwd=tmp_path, capture_output=True, text=True, timeout=5, check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    assert "`make normalized-summary-check`" in summary.read_text()
