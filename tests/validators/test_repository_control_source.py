from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from tools.validators.repository_control.validate_control_source_availability import (
    append_github_step_summary,
    evaluate,
)

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    ROOT
    / "tools/validators/repository_control/validate_control_source_availability.py"
)
WORKFLOW_PATH = ROOT / ".github/workflows/repository-control.yml"
BINDING_PATH = ROOT / "docs/governance/REPOSITORY_TRANSITION_CONTROL_SOURCE.md"
REPOSITORY = "bartytime4life/Kansas-Frontier-Matrix"
CONTROL_ISSUE = 4233


def source_status(status: str = "AVAILABLE") -> dict[str, object]:
    return {
        "schema_version": "1.0.0",
        "repository": REPOSITORY,
        "control_issue": CONTROL_ISSUE,
        "status": status,
    }


def run(value: object):
    return evaluate(
        value,
        expected_repository=REPOSITORY,
        expected_control_issue=CONTROL_ISSUE,
    )


def test_available_exact_binding_passes() -> None:
    result = run(source_status())
    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "PASS",
        "CONTROL_SOURCE_AVAILABLE",
        0,
    )
    assert result.repository == REPOSITORY
    assert result.control_issue == CONTROL_ISSUE


def test_unavailable_source_fails_closed_explicitly() -> None:
    result = run(source_status("UNAVAILABLE"))
    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "REGRESSION",
        "CONTROL_SOURCE_UNAVAILABLE",
        1,
    )


def test_wrong_repository_or_issue_fails_binding() -> None:
    cases = (
        {**source_status(), "repository": "example/other"},
        {**source_status(), "control_issue": CONTROL_ISSUE + 1},
    )
    for value in cases:
        result = run(value)
        assert (result.outcome_class, result.reason_code, result.exit_code) == (
            "REGRESSION",
            "CONTROL_SOURCE_BINDING_MISMATCH",
            1,
        )


def test_malformed_status_shape_fails_closed() -> None:
    cases = (
        [],
        {**source_status(), "unexpected": True},
        {key: value for key, value in source_status().items() if key != "status"},
        {**source_status(), "status": "UNKNOWN"},
        {**source_status(), "schema_version": "2.0.0"},
    )
    for value in cases:
        result = run(value)
        assert (result.outcome_class, result.reason_code, result.exit_code) == (
            "REGRESSION",
            "CONTROL_SOURCE_STATUS_INVALID",
            1,
        )


def test_step_summary_is_bounded(tmp_path: Path) -> None:
    result = run(source_status("UNAVAILABLE"))
    summary_path = tmp_path / "summary.md"
    append_github_step_summary(summary_path, result)
    summary = summary_path.read_text(encoding="utf-8")
    assert "CONTROL_SOURCE_UNAVAILABLE" in summary
    assert "Transition posture: `BLOCKING`" in summary
    assert "Response bodies and transport errors are not copied" in summary


def test_cli_available_and_unavailable_outcomes(tmp_path: Path) -> None:
    for status, returncode, reason in (
        ("AVAILABLE", 0, "CONTROL_SOURCE_AVAILABLE"),
        ("UNAVAILABLE", 1, "CONTROL_SOURCE_UNAVAILABLE"),
    ):
        status_path = tmp_path / f"{status.lower()}.json"
        status_path.write_text(
            json.dumps(source_status(status), sort_keys=True) + "\n",
            encoding="utf-8",
        )
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "--status-file",
                str(status_path),
                "--expected-repository",
                REPOSITORY,
                "--expected-control-issue",
                str(CONTROL_ISSUE),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        assert completed.returncode == returncode
        output = json.loads(completed.stdout)
        assert output["reason_code"] == reason
        assert output["control_issue"] == CONTROL_ISSUE


def test_cli_rejects_duplicate_json_keys_without_echoing_values(tmp_path: Path) -> None:
    status_path = tmp_path / "duplicate.json"
    status_path.write_text(
        '{"schema_version":"1.0.0","repository":"'
        + REPOSITORY
        + '","control_issue":4233,"status":"AVAILABLE",'
        + '"status":"DO_NOT_ECHO"}\n',
        encoding="utf-8",
    )
    completed = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR_PATH),
            "--status-file",
            str(status_path),
            "--expected-repository",
            REPOSITORY,
            "--expected-control-issue",
            str(CONTROL_ISSUE),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 1
    assert json.loads(completed.stdout)["reason_code"] == "CONTROL_SOURCE_STATUS_INVALID"
    assert "DO_NOT_ECHO" not in completed.stdout


def test_workflow_uses_live_source_and_classifies_fetch_failure() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert 'KFM_CONTROL_ISSUE: "4233"' in workflow
    assert 'KFM_CONTROL_ISSUE: "1675"' not in workflow
    assert "validate_control_source_availability.py?ref=${KFM_BASE_SHA}" in workflow
    assert "validate_transition_authorization.py?ref=${KFM_BASE_SHA}" in workflow
    assert "if gh api \\" in workflow
    assert 'source_status="UNAVAILABLE"' in workflow
    assert 'source_status="AVAILABLE"' in workflow
    assert "repository-control-source-status.json" in workflow
    assert 'printf \'[]\\n\' > "${comments_path}"' in workflow
    assert '--expected-control-issue "${KFM_CONTROL_ISSUE}"' in workflow
    assert "Require live repository-control source" in workflow
    assert workflow.index("Require live repository-control source") < workflow.index(
        "Require an exact owner transition record"
    )
    assert "issues: read" in workflow
    assert "issues: write" not in workflow


def test_binding_note_names_successor_without_rewriting_history() -> None:
    binding = BINDING_PATH.read_text(encoding="utf-8")
    assert "issue #4233" in binding
    assert "deleted issue #1675" in binding
    assert "historical evidence" in binding
    assert "advisory" in binding
    assert "does not authorize a ruleset" in binding
