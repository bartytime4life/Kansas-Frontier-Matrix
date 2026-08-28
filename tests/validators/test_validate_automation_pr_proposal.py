from __future__ import annotations

import importlib.util
import json
import pathlib
import unittest

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


if __name__ == "__main__":
    unittest.main()
