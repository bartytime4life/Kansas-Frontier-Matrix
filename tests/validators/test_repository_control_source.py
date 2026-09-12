from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from tools.validators.repository_control.validate_control_source_availability import (
    append_github_step_summary,
    evaluate as evaluate_source,
)
from tools.validators.repository_control.validate_transition_authorization import (
    evaluate as evaluate_transition,
)

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    ROOT
    / "tools/validators/repository_control/validate_control_source_availability.py"
)
WORKFLOW_PATH = ROOT / ".github/workflows/repository-control.yml"
BINDING_PATH = ROOT / "docs/governance/REPOSITORY_TRANSITION_CONTROL_SOURCE.md"
EVENT_PATH = (
    ROOT
    / "tests/fixtures/governance/repository_control/pull_request_target_event_ready.json"
)
REPOSITORY = "bartytime4life/Kansas-Frontier-Matrix"
CONTROL_ISSUE = 4024
TRANSITION_NOW = datetime(2026, 9, 3, 18, 0, tzinfo=timezone.utc)


def source_status(status: str = "AVAILABLE") -> dict[str, object]:
    return {
        "schema_version": "1.0.0",
        "repository": REPOSITORY,
        "control_issue": CONTROL_ISSUE,
        "status": status,
    }


def run(value: object):
    return evaluate_source(
        value,
        expected_repository=REPOSITORY,
        expected_control_issue=CONTROL_ISSUE,
    )


def transition_event(action: str, *, draft: bool = False) -> dict:
    event = json.loads(EVENT_PATH.read_text(encoding="utf-8"))
    event["action"] = action
    event["pull_request"]["draft"] = draft
    event["pull_request"]["state"] = "open"
    return event


def evaluate_event(event: dict):
    return evaluate_transition(
        event,
        [],
        control_issue=CONTROL_ISSUE,
        authorized_login="bartytime4life",
        default_branch="main",
        now=TRANSITION_NOW,
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
        + '","control_issue":4024,"status":"AVAILABLE",'
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
    assert 'KFM_CONTROL_ISSUE: "4024"' in workflow
    assert 'KFM_CONTROL_ISSUE: "1675"' not in workflow
    assert 'KFM_CONTROL_ISSUE: "4233"' not in workflow
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
    assert "pull-requests: read" in workflow
    assert "contents: write" not in workflow


def test_workflow_runs_draft_and_holds_both_non_draft_entry_paths() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "      - opened" in workflow
    assert "      - ready_for_review" in workflow
    assert "      - converted_to_draft" in workflow
    assert "if: ${{ !github.event.pull_request.draft }}" not in workflow

    draft_result = evaluate_event(transition_event("opened", draft=True))
    assert (draft_result.outcome_class, draft_result.reason_code, draft_result.exit_code) == (
        "EXPECTED_READINESS_HOLD",
        "PULL_REQUEST_IS_DRAFT",
        3,
    )

    for action in ("opened", "ready_for_review"):
        result = evaluate_event(transition_event(action))
        assert (result.outcome_class, result.reason_code, result.exit_code) == (
            "EXPECTED_READINESS_HOLD",
            "TRANSITION_AUTHORIZATION_MISSING",
            3,
        )


def test_binding_note_names_selected_source_without_rewriting_history() -> None:
    binding = BINDING_PATH.read_text(encoding="utf-8").lower()
    assert "issue #4024" in binding
    assert "issue #4233" not in binding
    assert "deleted issue #1675" in binding
    assert "historical evidence" in binding
    assert "pr #4234" in binding
    assert "pr #4235" in binding
    assert "ruleset `15484585`" in binding
    assert '"context": "authorize-ready-and-merge"' in binding
    assert '"integration_id": 15368' in binding
    assert '"strict_required_status_checks_policy": true' in binding
    assert "skipped-success" in binding
    assert "proposed and not applied" in binding
    assert "does not authorize a ruleset" in binding
