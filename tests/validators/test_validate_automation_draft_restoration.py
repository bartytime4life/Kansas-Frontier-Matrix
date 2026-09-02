from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from tools.validators.governance.validate_automation_draft_restoration import (
    AUTHORITY_BOUNDARY,
    DRAFT_ONLY_MARKER,
    validate_live,
    validate_proposal,
    verify_post_state,
)

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/governance/validate_automation_draft_restoration.py"
SCHEMA = ROOT / "schemas/contracts/v1/governance/automation_draft_restoration.schema.json"
WORKFLOW = ROOT / ".github/workflows/automation-draft-pr-restorer.yml"
NOW = datetime(2026, 9, 2, 15, 0, tzinfo=timezone.utc)


def proposal() -> dict:
    return {
        "profile": "kfm.automation.draft-restoration.v1",
        "incident_id": "kfm-4024-pr-9001-ready-20260902t145500z",
        "repository": "bartytime4life/Kansas-Frontier-Matrix",
        "control_issue": 4024,
        "pr_number": 9001,
        "expected_base_ref": "main",
        "expected_base_sha": "1" * 40,
        "expected_head_branch": "automation/draft-delivery/synthetic-restoration-20260902",
        "expected_head_sha": "2" * 40,
        "ready_event_at": "2026-09-02T14:55:00Z",
        "ready_actor": "bartytime4life",
        "ready_performed_via_app": None,
        "draft_only_marker": DRAFT_ONLY_MARKER,
        "restore_to_draft": True,
        "close_on_restore_failure": True,
        "fallback": "CLOSE_UNMERGED",
        "merge_allowed": False,
        "release_allowed": False,
        "deploy_allowed": False,
        "publish_allowed": False,
        "settings_change_allowed": False,
        "reason": "Synthetic unauthorized ready transition for deterministic testing.",
    }


def live_pr(*, draft: bool = False, state: str = "open", merged: bool = False) -> dict:
    return {
        "number": 9001,
        "node_id": "PR_kwDOPyBy4c8AAAABsynthetic",
        "state": state,
        "draft": draft,
        "merged": merged,
        "merged_at": "2026-09-02T14:56:00Z" if merged else None,
        "body": DRAFT_ONLY_MARKER + "\n\nDraft-only synthetic review surface.\n",
        "user": {"login": "bartytime4life"},
        "base": {"ref": "main", "sha": "1" * 40},
        "head": {
            "ref": "automation/draft-delivery/synthetic-restoration-20260902",
            "sha": "2" * 40,
            "repo": {"full_name": "bartytime4life/Kansas-Frontier-Matrix"},
        },
    }


def ready_event(**updates) -> dict:
    event = {
        "event": "ready_for_review",
        "created_at": "2026-09-02T14:55:00Z",
        "actor": {"login": "bartytime4life"},
        "performed_via_github_app": None,
        "issue": {"number": 9001},
    }
    event.update(updates)
    return event


class AutomationDraftRestorationTests(unittest.TestCase):
    def test_schema_has_closed_exact_authority_shape(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["properties"]["control_issue"]["const"], 4024)
        self.assertTrue(schema["properties"]["restore_to_draft"]["const"])
        self.assertTrue(schema["properties"]["close_on_restore_failure"]["const"])
        for field in (
            "merge_allowed",
            "release_allowed",
            "deploy_allowed",
            "publish_allowed",
            "settings_change_allowed",
        ):
            self.assertFalse(schema["properties"][field]["const"])

    def test_valid_proposal_is_fetch_eligible_not_write_eligible(self) -> None:
        result = validate_proposal(proposal())
        self.assertEqual((result.outcome, result.fetch_eligible, result.write_eligible), ("PASS", True, False))

    def test_exact_live_ready_event_is_write_eligible(self) -> None:
        result = validate_live(proposal(), live_pr(), [[ready_event()]], now=NOW)
        self.assertEqual(result.outcome, "PASS")
        self.assertTrue(result.write_eligible)
        self.assertEqual(result.pr_node_id, "PR_kwDOPyBy4c8AAAABsynthetic")

    def test_ready_event_issue_field_is_optional_for_scoped_endpoint(self) -> None:
        event = ready_event()
        event.pop("issue")
        result = validate_live(proposal(), live_pr(), [[event]], now=NOW)
        self.assertEqual(result.outcome, "PASS")
        self.assertTrue(result.write_eligible)

    def test_missing_marker_is_no_action(self) -> None:
        live = live_pr()
        live["body"] = "Draft-only prose without the machine marker."
        result = validate_live(proposal(), live, [ready_event()], now=NOW)
        self.assertEqual((result.outcome, result.reason_codes), ("NO_ACTION", ("DRAFT_ONLY_MARKER_REMOVED",)))

    def test_duplicate_marker_fails_closed(self) -> None:
        live = live_pr()
        live["body"] = DRAFT_ONLY_MARKER + "\n" + DRAFT_ONLY_MARKER
        result = validate_live(proposal(), live, [ready_event()], now=NOW)
        self.assertEqual((result.outcome, result.reason_codes), ("DENY", ("DRAFT_ONLY_MARKER_NONCANONICAL",)))

    def test_already_draft_closed_or_merged_is_no_action(self) -> None:
        cases = (
            (live_pr(draft=True), "PULL_REQUEST_ALREADY_DRAFT"),
            (live_pr(state="closed"), "PULL_REQUEST_ALREADY_CLOSED"),
            (live_pr(state="closed", merged=True), "PULL_REQUEST_ALREADY_MERGED"),
        )
        for live, reason in cases:
            with self.subTest(reason=reason):
                result = validate_live(proposal(), live, [ready_event()], now=NOW)
                self.assertEqual((result.outcome, result.reason_codes), ("NO_ACTION", (reason,)))

    def test_identity_drift_fork_and_author_mismatch_are_denied(self) -> None:
        cases = []
        head = live_pr()
        head["head"]["sha"] = "3" * 40
        cases.append((head, "HEAD_SHA_MISMATCH"))
        fork = live_pr()
        fork["head"]["repo"]["full_name"] = "someone/fork"
        cases.append((fork, "HEAD_REPOSITORY_MISMATCH"))
        author = live_pr()
        author["user"]["login"] = "someone-else"
        cases.append((author, "PR_AUTHOR_MISMATCH"))
        for live, reason in cases:
            with self.subTest(reason=reason):
                result = validate_live(proposal(), live, [ready_event()], now=NOW)
                self.assertEqual(result.outcome, "DENY")
                self.assertIn(reason, result.reason_codes)

    def test_actor_app_timestamp_and_issue_are_bound(self) -> None:
        cases = (
            ready_event(actor={"login": "someone-else"}),
            ready_event(performed_via_github_app={"slug": "unexpected-app"}),
            ready_event(created_at="2026-09-02T14:54:59Z"),
            ready_event(issue={"number": 9002}),
        )
        for event in cases:
            with self.subTest(event=event):
                result = validate_live(proposal(), live_pr(), [event], now=NOW)
                self.assertEqual((result.outcome, result.reason_codes), ("DENY", ("READY_EVENT_NOT_FOUND",)))

    def test_later_transition_prevents_replay(self) -> None:
        later = {
            "event": "converted_to_draft",
            "created_at": "2026-09-02T14:55:01Z",
        }
        result = validate_live(proposal(), live_pr(), [ready_event(), later], now=NOW)
        self.assertEqual((result.outcome, result.reason_codes), ("DENY", ("LATER_TRANSITION_PRESENT",)))

    def test_stale_and_future_events_are_denied(self) -> None:
        stale = proposal()
        stale["ready_event_at"] = "2026-09-02T10:59:59Z"
        self.assertEqual(validate_live(stale, live_pr(), [ready_event(created_at=stale["ready_event_at"])], now=NOW).reason_codes, ("READY_EVENT_STALE",))
        future = proposal()
        future["ready_event_at"] = "2026-09-02T15:05:01Z"
        self.assertEqual(validate_live(future, live_pr(), [ready_event(created_at=future["ready_event_at"])], now=NOW).reason_codes, ("READY_EVENT_FROM_FUTURE",))

    def test_post_action_verifies_exact_draft_and_closed_states(self) -> None:
        restored = verify_post_state(proposal(), live_pr(draft=True), "draft")
        closed = verify_post_state(proposal(), live_pr(state="closed"), "closed")
        wrong = verify_post_state(proposal(), live_pr(), "draft")
        self.assertEqual(restored.reason_codes, ("RESTORED_DRAFT_VERIFIED",))
        self.assertEqual(closed.reason_codes, ("CLOSED_UNMERGED_VERIFIED",))
        self.assertEqual((wrong.outcome, wrong.reason_codes), ("DENY", ("POST_ACTION_STATE_MISMATCH",)))

    def test_terminal_authority_cannot_be_expanded(self) -> None:
        for field in (
            "merge_allowed",
            "release_allowed",
            "deploy_allowed",
            "publish_allowed",
            "settings_change_allowed",
        ):
            candidate = proposal()
            candidate[field] = True
            result = validate_proposal(candidate)
            self.assertEqual(result.outcome, "ERROR")
            self.assertIn("TERMINAL_LIMITS_INVALID", result.reason_codes)

    def test_cli_rejects_option_abbreviations(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "proposal.json"
            path.write_text(json.dumps(proposal()) + "\n", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR), str(path), "--live-p", str(path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("unrecognized arguments", completed.stderr)

    def test_cli_rejects_duplicate_json_members_without_echoing_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "proposal.json"
            payload = json.dumps(proposal(), separators=(",", ":"))
            payload = payload.replace('"profile":', '"SENSITIVE_DO_NOT_ECHO":"secret","profile":"duplicate","profile":', 1)
            path.write_text(payload + "\n", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR), str(path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(completed.returncode, 2)
        rendered = completed.stdout + completed.stderr
        self.assertNotIn("SENSITIVE_DO_NOT_ECHO", rendered)
        self.assertNotIn("secret", rendered)

    def test_result_never_echoes_body_or_reason(self) -> None:
        candidate = proposal()
        candidate["reason"] = "SENSITIVE_REASON_DO_NOT_ECHO"
        live = live_pr()
        live["body"] += "SENSITIVE_BODY_DO_NOT_ECHO"
        rendered = json.dumps(validate_live(candidate, live, [ready_event()], now=NOW).as_dict())
        self.assertNotIn("SENSITIVE_REASON_DO_NOT_ECHO", rendered)
        self.assertNotIn("SENSITIVE_BODY_DO_NOT_ECHO", rendered)
        self.assertIn("no ready", AUTHORITY_BOUNDARY)

    def test_privileged_workflow_is_dispatch_only_and_never_executes_head(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        active = "\n".join(
            line.strip()
            for line in text.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )
        self.assertIn("repository_dispatch:", active)
        self.assertIn("automation-draft-restoration-v1", active)
        self.assertIn("workflow_dispatch:", active)
        self.assertIn("proposal_json:", active)
        self.assertIn("github.event.client_payload.proposal", active)
        self.assertIn("inputs.proposal_json", active)
        self.assertEqual(active.count("pull-requests: write"), 1)
        self.assertNotIn("pull_request_target:", active)
        self.assertNotIn("actions/checkout@", active)
        self.assertIn("convertPullRequestToDraft", active)
        self.assertIn("-f state=closed", active)
        self.assertNotIn("gh pr merge", active)
        self.assertNotIn("contents: write", active)


if __name__ == "__main__":
    unittest.main()
