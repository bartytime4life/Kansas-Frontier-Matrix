from __future__ import annotations

import copy
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.repository_control.validate_transition_authorization import (
    MARKER,
    evaluate,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests/fixtures/governance/repository_control"
EVENT_PATH = FIXTURES / "pull_request_target_event_ready.json"
COMMENTS_PATH = FIXTURES / "issue_comments_transition_authorization_valid.json"
SCHEMA_PATH = (
    ROOT
    / "schemas/contracts/v1/governance/repository_transition_authorization.schema.json"
)
VALIDATOR_PATH = (
    ROOT
    / "tools/validators/repository_control/validate_transition_authorization.py"
)
WORKFLOW_PATH = ROOT / ".github/workflows/repository-control.yml"
NOW = datetime(2026, 7, 30, 21, 0, tzinfo=timezone.utc)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def record(comments: list) -> dict:
    body = comments[0][0]["body"]
    payload = body.split(MARKER, 1)[1].split("-->", 1)[0].strip()
    return json.loads(payload)


def replace_record(comments: list, value: dict) -> None:
    comment = comments[0][0]
    prefix = comment["body"].split(MARKER, 1)[0]
    comment["body"] = (
        prefix
        + MARKER
        + "\n"
        + json.dumps(value, sort_keys=True, separators=(",", ":"))
        + "\n-->"
    )


def run(event: dict, comments: list):
    return evaluate(
        event,
        comments,
        control_issue=1675,
        authorized_login="bartytime4life",
        default_branch="main",
        now=NOW,
    )


def test_fixture_record_matches_schema() -> None:
    schema = load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    errors = list(
        Draft202012Validator(
            schema, format_checker=FormatChecker()
        ).iter_errors(record(load(COMMENTS_PATH)))
    )
    assert not errors


def test_exact_unedited_owner_record_passes() -> None:
    result = run(load(EVENT_PATH), load(COMMENTS_PATH))
    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "PASS",
        "TRANSITION_AUTHORIZED",
        0,
    )
    assert result.authorization_id == "kfm-rta-pr-9001-head-222222222222"
    assert result.comment_id == 9001001


def test_draft_pull_request_is_held_even_with_record() -> None:
    event = load(EVENT_PATH)
    event["pull_request"]["draft"] = True
    result = run(event, load(COMMENTS_PATH))
    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "EXPECTED_READINESS_HOLD",
        "PULL_REQUEST_IS_DRAFT",
        3,
    )


def test_missing_record_holds_ready_and_merge() -> None:
    result = run(load(EVENT_PATH), [])
    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "EXPECTED_READINESS_HOLD",
        "TRANSITION_AUTHORIZATION_MISSING",
        3,
    )


def test_non_owner_marker_cannot_authorize() -> None:
    comments = load(COMMENTS_PATH)
    comments[0][0]["user"]["login"] = "not-the-owner"
    comments[0][0]["author_association"] = "CONTRIBUTOR"
    result = run(load(EVENT_PATH), comments)
    assert result.reason_code == "TRANSITION_AUTHORIZATION_MISSING"


def test_edited_owner_comment_fails_closed() -> None:
    comments = load(COMMENTS_PATH)
    comments[0][0]["updated_at"] = "2026-07-30T20:01:00Z"
    result = run(load(EVENT_PATH), comments)
    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "REGRESSION",
        "MATCHING_AUTHORIZATION_INVALID",
        1,
    )


def test_head_and_base_are_bound_exactly() -> None:
    cases = (
        ("head_sha", "3" * 40, "AUTHORIZATION_HEAD_MISMATCH"),
        ("base_sha", "4" * 40, "AUTHORIZATION_BASE_MISMATCH"),
    )
    for field, value, reason in cases:
        comments = load(COMMENTS_PATH)
        value_record = record(comments)
        value_record[field] = value
        replace_record(comments, value_record)
        result = run(load(EVENT_PATH), comments)
        assert (result.outcome_class, result.reason_code) == (
            "EXPECTED_READINESS_HOLD",
            reason,
        )


def test_expired_or_overlong_authorization_is_rejected() -> None:
    cases = (
        ("2026-07-30T20:30:00Z", "EXPECTED_READINESS_HOLD", "AUTHORIZATION_EXPIRED"),
        (
            "2026-07-31T01:00:01Z",
            "REGRESSION",
            "MATCHING_AUTHORIZATION_INVALID",
        ),
    )
    for expires_at, outcome, reason in cases:
        comments = load(COMMENTS_PATH)
        value_record = record(comments)
        value_record["expires_at"] = expires_at
        replace_record(comments, value_record)
        result = run(load(EVENT_PATH), comments)
        assert (result.outcome_class, result.reason_code) == (outcome, reason)


def test_unknown_or_duplicate_fields_fail_closed() -> None:
    comments = load(COMMENTS_PATH)
    value_record = record(comments)
    value_record["unexpected"] = True
    replace_record(comments, value_record)
    result = run(load(EVENT_PATH), comments)
    assert result.reason_code == "MATCHING_AUTHORIZATION_INVALID"

    comments = load(COMMENTS_PATH)
    comment = comments[0][0]
    payload = comment["body"].split(MARKER, 1)[1].split("-->", 1)[0].strip()
    payload = payload.replace(
        '"schema_version":"1.0.0"',
        '"schema_version":"1.0.0","schema_version":"1.0.0"',
    )
    comment["body"] = MARKER + "\n" + payload + "\n-->"
    result = run(load(EVENT_PATH), comments)
    assert result.reason_code == "MATCHING_AUTHORIZATION_INVALID"


def test_runtime_shape_rejects_short_id_and_non_rfc3339_expiry() -> None:
    cases = (
        ("authorization_id", "x"),
        ("expires_at", "2026-07-30T22:00:00"),
    )
    for field, value in cases:
        comments = load(COMMENTS_PATH)
        value_record = record(comments)
        value_record[field] = value
        replace_record(comments, value_record)
        result = run(load(EVENT_PATH), comments)
        assert result.reason_code == "MATCHING_AUTHORIZATION_INVALID"


def test_invalid_record_does_not_echo_comment_fields() -> None:
    comments = load(COMMENTS_PATH)
    value_record = record(comments)
    value_record["SENSITIVE_UNTRUSTED_FIELD"] = "do-not-echo"
    replace_record(comments, value_record)

    result = run(load(EVENT_PATH), comments)

    rendered = json.dumps(result.as_dict(), sort_keys=True)
    assert result.reason_code == "MATCHING_AUTHORIZATION_INVALID"
    assert "SENSITIVE_UNTRUSTED_FIELD" not in rendered
    assert "do-not-echo" not in rendered


def test_workflow_keeps_event_metadata_out_of_shell_source() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "KFM_AUTHORIZED_LOGIN: ${{ github.event.repository.owner.login }}" in workflow
    assert "KFM_DEFAULT_BRANCH: ${{ github.event.repository.default_branch }}" in workflow
    assert '--authorized-login "${KFM_AUTHORIZED_LOGIN}"' in workflow
    assert '--default-branch "${KFM_DEFAULT_BRANCH}"' in workflow
    assert '--authorized-login "${{ github.' not in workflow
    assert '--default-branch "${{ github.' not in workflow


def test_workflow_keeps_expected_readiness_hold_blocking() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert 'status=$?' not in workflow
    assert 'if [ "$status" -eq 3 ]; then' not in workflow
    assert 'Expected readiness hold; repository transition is not yet authorized.' not in workflow
    assert 'An expected readiness hold remains nonzero and merge-blocking' in workflow


def test_non_default_target_is_not_applicable() -> None:
    event = load(EVENT_PATH)
    event["pull_request"]["base"]["ref"] = "maintenance"
    result = run(event, load(COMMENTS_PATH))
    assert (result.outcome_class, result.reason_code, result.exit_code) == (
        "NOT_APPLICABLE",
        "NON_DEFAULT_BRANCH_TARGET",
        0,
    )


def test_cli_exit_and_output_are_bounded(tmp_path: Path) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR_PATH),
            "--event",
            str(EVENT_PATH),
            "--comments",
            str(COMMENTS_PATH),
            "--control-issue",
            "1675",
            "--authorized-login",
            "bartytime4life",
            "--default-branch",
            "main",
            "--now",
            "2026-07-30T21:00:00Z",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0
    output = json.loads(completed.stdout)
    assert output["outcome_class"] == "PASS"
    assert output["head_sha"] == "2" * 40
    assert "Synthetic exact-head transition fixture" not in completed.stdout


def test_cli_missing_authorization_remains_blocking(tmp_path: Path) -> None:
    comments_path = tmp_path / "comments.json"
    comments_path.write_text("[]\n", encoding="utf-8")
    completed = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR_PATH),
            "--event",
            str(EVENT_PATH),
            "--comments",
            str(comments_path),
            "--control-issue",
            "1675",
            "--authorized-login",
            "bartytime4life",
            "--default-branch",
            "main",
            "--now",
            "2026-07-30T21:00:00Z",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 3
    output = json.loads(completed.stdout)
    assert output["outcome_class"] == "EXPECTED_READINESS_HOLD"
    assert output["reason_code"] == "TRANSITION_AUTHORIZATION_MISSING"


def test_pr_1869_without_transition_record_would_hold() -> None:
    event = copy.deepcopy(load(EVENT_PATH))
    event["pull_request"].update(
        number=1869,
        base={
            "ref": "main",
            "sha": "426b8db9b423f180f3f5121e3cf40e1e82d5d357",
        },
        head={
            "ref": "agent/modernize-planning-region-contract-20260730",
            "sha": "30e28f6f9685f240158e24630cbac5a6990410eb",
        },
    )
    result = run(event, [])
    assert (result.outcome_class, result.reason_code) == (
        "EXPECTED_READINESS_HOLD",
        "TRANSITION_AUTHORIZATION_MISSING",
    )
