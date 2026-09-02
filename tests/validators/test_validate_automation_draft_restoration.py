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
            self.assertFalse(schema["properties"]["restore_to_draft"]["const"])
            self.assertFalse(schema["properties"][field]["const"])
uçízËojX¦º)¢Æ¥ŠÇŞµÈ^–("nW§¢Ü+Š×–("nW¬zWÍ¢w«zË¥¶ö¥‰Ö­zšè¦‹–šè¦‹–Ç¥}«,z»Dªæ¥­ë.–Ú.µÊ&z·¬º[_z×!zX ‰¹^­ë.–Ü+Š×–("nW$“®ç…j[uçízË^Å§-–+Ş­æÉëŞØ¬Â¸­yéb‚&åzÇ¥|Ú'z·¬º[