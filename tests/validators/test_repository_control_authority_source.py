from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from tools.validators.repository_control.validate_transition_authorization import (
    MARKER,
    evaluate,
)

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = ROOT / ".github/workflows/repository-control.yml"
CONTRACT_PATH = ROOT / "contracts/governance/repository_control_state.md"
CONTROL_ISSUE = 4024
LEGACY_CONTROL_ISSUE = 1675
NOW = datetime(2026, 9, 3, 18, 0, tzinfo=timezone.utc)


def event() -> dict:
    return {
        "action": "ready_for_review",
        "repository": {
            "full_name": "bartytime4life/Kansas-Frontier-Matrix",
            "default_branch": "main",
            "owner": {"login": "bartytime4life"},
        },
        "pull_request": {
            "number": 9001,
            "state": "open",
            "draft": False,
            "base": {"ref": "main", "sha": "1" * 40},
            "head": {
                "ref": "governance/synthetic-authority-source",
                "sha": "2" * 40,
            },
        },
    }


def comments(control_issue: int) -> list[dict]:
    payload = {
        "schema_version": "1.0.0",
        "authorization_id": "kfm-rta-pr-9001-head-222222222222",
        "repository": "bartytime4life/Kansas-Frontier-Matrix",
        "control_issue": control_issue,
        "pr_number": 9001,
        "base_sha": "1" * 40,
        "head_sha": "2" * 40,
        "authorizing_actor": "bartytime4life",
        "decision": "ALLOW_READY_AND_MERGE",
        "expires_at": "2026-09-03T20:00:00Z",
        "reason": "Synthetic exact-source authority fixture.",
        "evidence_refs": [
            "fixture://repository-control/authority-source/issue-4024"
        ],
    }
    return [
        {
            "id": 9001001,
            "html_url": (
                "https://github.com/bartytime4life/Kansas-Frontier-Matrix/"
                f"issues/{control_issue}#issuecomment-9001001"
            ),
            "user": {"login": "bartytime4life"},
            "author_association": "OWNER",
            "created_at": "2026-09-03T17:00:00Z",
            "updated_at": "2026-09-03T17:00:00Z",
            "body": (
                MARKER
                + "\n"
                + json.dumps(payload, sort_keys=True, separators=(",", ":"))
                + "\n-->"
            ),
        }
    ]


def test_workflow_uses_selected_live_issue_and_preserves_trusted_base_boundary() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")

    assert 'KFM_CONTROL_ISSUE: "4024"' in workflow
    assert 'KFM_CONTROL_ISSUE: "1675"' not in workflow
    assert "pull_request_target:" in workflow
    assert "contents: read" in workflow
    assert "issues: read" in workflow
    assert "pull-requests: read" in workflow
    assert "actions: write" not in workflow
    assert "contents: write" not in workflow
    assert "pull-requests: write" not in workflow
    assert "actions/checkout" not in workflow
    assert "?ref=${KFM_BASE_SHA}" in workflow
    assert "/issues/${KFM_CONTROL_ISSUE}/comments?per_page=100" in workflow
    assert "set -euo pipefail" in workflow
    assert "|| true" not in workflow


def test_selected_issue_record_authorizes_only_its_exact_binding() -> None:
    result = evaluate(
        event(),
        comments(CONTROL_ISSUE),
        control_issue=CONTROL_ISSUE,
        authorized_login="bartytime4life",
        default_branch="main",
        now=NOW,
    )

    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "PASS",
        "TRANSITION_AUTHORIZED",
        0,
    )


def test_deleted_predecessor_issue_record_cannot_authorize_current_source() -> None:
    result = evaluate(
        event(),
        comments(LEGACY_CONTROL_ISSUE),
        control_issue=CONTROL_ISSUE,
        authorized_login="bartytime4life",
        default_branch="main",
        now=NOW,
    )

    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "EXPECTED_READINESS_HOLD",
        "TRANSITION_AUTHORIZATION_MISSING",
        3,
    )


def test_operating_contract_distinguishes_current_source_from_lineage() -> None:
    contract = CONTRACT_PATH.read_text(encoding="utf-8")

    assert "Issue #4024 is the selected live read location" in contract
    assert "Issue #1675 remains historical predecessor lineage only" in contract
    assert '"control_issue":4024' in contract
    assert "matching unedited #4024 record" in contract
