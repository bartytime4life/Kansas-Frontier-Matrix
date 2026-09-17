from __future__ import annotations

import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from tools.validators.governance.validate_automation_pr_live_binding import validate_live_binding

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/governance/validate_automation_pr_proposal.py"
spec = importlib.util.spec_from_file_location("automation_pr_proposal", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)

FIXTURES = ROOT / "fixtures/contracts/v1/governance/automation_pr_proposal"


def load(relative: str):
    return json.loads((FIXTURES / relative).read_text(encoding="utf-8"))


class AutomationPrProposalTests(unittest.TestCase):
    def test_pass_fixture_is_write_eligible(self):
        result = module.validate(load("valid/valid_pass.json"))
        self.assertEqual("PASS", result["outcome"])
        self.assertTrue(result["write_eligible"])
        self.assertEqual([], result["reason_codes"])

    def test_hold_fixture_is_valid_but_not_write_eligible(self):
        result = module.validate(load("valid/valid_hold.json"))
        self.assertEqual("HOLD", result["outcome"])
        self.assertFalse(result["write_eligible"])
        self.assertIn("POLICY_HOLD", result["reason_codes"])

    def test_publish_capability_is_rejected(self):
        result = module.validate(load("invalid/invalid_publish_allowed.json"))
        self.assertEqual("ERROR", result["outcome"])
        self.assertFalse(result["write_eligible"])
        self.assertIn("PUBLISH_MUST_BE_FALSE", result["reason_codes"])

    def test_path_escape_is_rejected(self):
        result = module.validate(load("invalid/invalid_path_escape.json"))
        self.assertEqual("ERROR", result["outcome"])
        self.assertFalse(result["write_eligible"])
        self.assertIn("UNSAFE_CHANGED_PATH", result["reason_codes"])

    def test_artifact_binding_is_exact(self):
        payload = load("valid/valid_pass.json")
        payload["artifacts"][0]["path"] = "data/work/automation/other.json"
        result = module.validate(payload)
        self.assertEqual("ERROR", result["outcome"])
        self.assertIn("ARTIFACT_PATH_BINDING_MISMATCH", result["reason_codes"])

    def test_unknown_field_is_rejected(self):
        payload = load("valid/valid_pass.json")
        payload["extra"] = "nope"
        result = module.validate(payload)
        self.assertEqual("ERROR", result["outcome"])
        self.assertIn("INVALID_FIELD_SET", result["reason_codes"])

    def test_malformed_json_field_types_fail_closed(self):
        cases = (
            ("changed_paths", "INVALID_CHANGED_PATHS", True),
            ("policy_reasons", "INVALID_POLICY_REASON", True),
            ("policy_outcome", "INVALID_POLICY_OUTCOME", False),
        )
        for field, reason, wrap_in_list in cases:
            for value in ({"untrusted": "must-not-appear"}, [], None, True, 7, 1.5):
                with self.subTest(field=field, value=value):
                    payload = load("valid/valid_pass.json")
                    payload[field] = [value] if wrap_in_list else value
                    result = module.validate(payload)
                    self.assertEqual("ERROR", result["outcome"])
                    self.assertFalse(result["write_eligible"])
                    self.assertIn(reason, result["reason_codes"])
                    self.assertNotIn("must-not-appear", json.dumps(result))

    def test_duplicate_lists_still_fail_closed(self):
        for field, value, reason in (
            ("changed_paths", "data/work/automation/example.json", "INVALID_CHANGED_PATHS"),
            ("policy_reasons", "REVIEW_REQUIRED", "INVALID_POLICY_REASONS"),
        ):
            with self.subTest(field=field):
                payload = load("valid/valid_pass.json")
                payload[field] = [value, value]
                result = module.validate(payload)
                self.assertEqual("ERROR", result["outcome"])
                self.assertFalse(result["write_eligible"])
                self.assertIn(reason, result["reason_codes"])

    def test_malformed_proposal_cli_returns_finite_json_failure(self):
        for field, value, reason in (
            ("changed_paths", [{}], "INVALID_CHANGED_PATHS"),
            ("policy_reasons", [[]], "INVALID_POLICY_REASON"),
            ("policy_outcome", {}, "INVALID_POLICY_OUTCOME"),
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                payload = load("valid/valid_pass.json")
                payload[field] = value
                path = pathlib.Path(directory) / "proposal.json"
                path.write_text(json.dumps(payload), encoding="utf-8")
                result = subprocess.run(
                    [sys.executable, str(MODULE_PATH), str(path)],
                    capture_output=True, text=True, timeout=10, check=False,
                )
                self.assertEqual(1, result.returncode)
                self.assertEqual("", result.stderr)
                report = json.loads(result.stdout)
                self.assertEqual("ERROR", report["outcome"])
                self.assertFalse(report["write_eligible"])
                self.assertIn(reason, report["reason_codes"])

    def test_malformed_proposal_stops_before_git_binding(self):
        for field, value in (
            ("changed_paths", [{}]),
            ("policy_reasons", [[]]),
            ("policy_outcome", {}),
        ):
            with self.subTest(field=field), patch(
                "tools.validators.governance.validate_automation_pr_live_binding._git"
            ) as git:
                payload = load("valid/valid_pass.json")
                payload[field] = value
                result = validate_live_binding(
                    payload, repo_root=ROOT, base_ref="main", head_ref="untrusted",
                )
                self.assertEqual("ERROR", result["outcome"])
                self.assertFalse(result["write_eligible"])
                self.assertEqual(["PROPOSAL_NOT_WRITE_ELIGIBLE"], result["reason_codes"])
                git.assert_not_called()


if __name__ == "__main__":
    unittest.main()
