from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.validators.governance.validate_automation_pr_live_binding import (
    validate_live_binding,
)


class AutomationPrLiveBindingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        self._git("init", "-b", "main")
        self._git("config", "user.email", "fixture@example.invalid")
        self._git("config", "user.name", "KFM Fixture")
        (self.repo / "README.md").write_text("fixture\n", encoding="utf-8")
        self._git("add", "README.md")
        self._git("commit", "-m", "base")
        self.base_sha = self._git("rev-parse", "HEAD")
        self._git("checkout", "-b", "automation/pass12-live-binding")
        candidate = self.repo / "data/work/automation/example.json"
        candidate.parent.mkdir(parents=True)
        candidate.write_text('{"candidate":true}\n', encoding="utf-8")
        self._git("add", candidate.relative_to(self.repo).as_posix())
        self._git("commit", "-m", "candidate")
        self.head_sha = self._git("rev-parse", "HEAD")
        self.digest = "sha256:" + hashlib.sha256(candidate.read_bytes()).hexdigest()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _git(self, *args: str) -> str:
        return subprocess.check_output(["git", *args], cwd=self.repo, text=True).strip()

    def _proposal(self) -> dict[str, object]:
        return {
            "profile": "kfm.automation.pr-proposal.v1",
            "proposal_id": "pass12-live-001",
            "base_ref": "main",
            "base_sha": self.base_sha,
            "head_branch": "automation/pass12-live-binding",
            "title": "chore(automation): propose bounded candidate",
            "changed_paths": ["data/work/automation/example.json"],
            "artifacts": [
                {
                    "path": "data/work/automation/example.json",
                    "sha256": self.digest,
                }
            ],
            "receipt_ref": "receipt:automation:pass12-live-001",
            "policy_outcome": "PASS",
            "policy_reasons": [],
            "draft": True,
            "merge_allowed": False,
            "release_allowed": False,
            "deploy_allowed": False,
            "promote_allowed": False,
            "publish_allowed": False,
        }

    def _validate(self, proposal: dict[str, object]) -> dict[str, object]:
        return validate_live_binding(
            proposal,
            repo_root=self.repo,
            base_ref="main",
            head_ref="automation/pass12-live-binding",
        )

    def test_valid_live_binding_passes(self) -> None:
        result = self._validate(self._proposal())
        self.assertEqual(result["outcome"], "PASS")
        self.assertTrue(result["write_eligible"])
        self.assertEqual(result["reason_codes"], [])
        self.assertEqual(result["base_sha"], self.base_sha)
        self.assertEqual(result["head_sha"], self.head_sha)

    def test_digest_mismatch_fails(self) -> None:
        proposal = self._proposal()
        proposal["artifacts"] = [
            {
                "path": "data/work/automation/example.json",
                "sha256": "sha256:" + "0" * 64,
            }
        ]
        result = self._validate(proposal)
        self.assertIn("ARTIFACT_DIGEST_MISMATCH", result["reason_codes"])
        self.assertFalse(result["write_eligible"])

    def test_live_path_mismatch_fails(self) -> None:
        extra = self.repo / "data/work/automation/extra.json"
        extra.write_text("{}\n", encoding="utf-8")
        self._git("add", extra.relative_to(self.repo).as_posix())
        self._git("commit", "-m", "extra candidate")
        result = self._validate(self._proposal())
        self.assertIn("LIVE_CHANGED_PATH_MISMATCH", result["reason_codes"])

    def test_outside_work_lane_fails(self) -> None:
        outside = self.repo / "docs/escape.md"
        outside.parent.mkdir(parents=True)
        outside.write_text("escape\n", encoding="utf-8")
        self._git("add", outside.relative_to(self.repo).as_posix())
        self._git("commit", "-m", "outside path")
        result = self._validate(self._proposal())
        self.assertIn("UNSAFE_LIVE_CHANGED_PATH", result["reason_codes"])
        self.assertIn("LIVE_CHANGED_PATH_MISMATCH", result["reason_codes"])

    def test_base_drift_fails(self) -> None:
        self._git("checkout", "main")
        (self.repo / "BASE_DRIFT.md").write_text("drift\n", encoding="utf-8")
        self._git("add", "BASE_DRIFT.md")
        self._git("commit", "-m", "advance main")
        self._git("checkout", "automation/pass12-live-binding")
        result = self._validate(self._proposal())
        self.assertIn("BASE_SHA_MISMATCH", result["reason_codes"])
        self.assertIn("HEAD_NOT_BASED_ON_CURRENT_MAIN", result["reason_codes"])

    def test_non_pass_policy_is_not_write_eligible(self) -> None:
        proposal = self._proposal()
        proposal["policy_outcome"] = "HOLD"
        proposal["policy_reasons"] = ["REVIEW_REQUIRED"]
        result = self._validate(proposal)
        self.assertEqual(result["reason_codes"], ["PROPOSAL_NOT_WRITE_ELIGIBLE"])
        self.assertFalse(result["write_eligible"])

    def test_executable_candidate_is_denied(self) -> None:
        self._git("update-index", "--chmod=+x", "data/work/automation/example.json")
        self._git("commit", "-m", "make candidate executable")
        result = self._validate(self._proposal())
        self.assertIn("UNSAFE_CANDIDATE_BLOB_MODE", result["reason_codes"])


if __name__ == "__main__":
    unittest.main()
