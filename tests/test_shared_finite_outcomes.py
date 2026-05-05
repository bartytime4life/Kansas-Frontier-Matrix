import json
import unittest
from pathlib import Path


class SharedFiniteOutcomeTests(unittest.TestCase):
    def test_required_shared_schemas_exist(self):
        for name in [
            "runtime_response_envelope.schema.json",
            "policy_decision.schema.json",
            "promotion_decision.schema.json",
            "validation_report.schema.json",
            "rollback_reference.schema.json",
            "evidence_bundle.schema.json",
        ]:
            self.assertTrue(Path("schemas/contracts/v1/shared", name).exists(), msg=name)

    def test_valid_fixture_uses_finite_values(self):
        d = json.loads(Path("fixtures/shared/finite_outcomes.valid.json").read_text())
        self.assertIn(d["runtime_response_envelope"]["outcome"], {"ANSWER", "ABSTAIN", "DENY", "ERROR"})
        self.assertIn(d["policy_decision"]["decision"], {"ALLOW", "ABSTAIN", "DENY", "ERROR"})
        self.assertIn(d["promotion_decision"]["decision"], {"ALLOW", "ABSTAIN", "DENY", "ERROR"})
        self.assertIn(d["validation_report"]["status"], {"PASS", "FAIL", "ABSTAIN", "ERROR"})
        self.assertIn(d["rollback_reference"]["decision"], {"ALLOW", "ABSTAIN", "DENY", "ERROR"})

    def test_invalid_fixture_has_out_of_set_values(self):
        d = json.loads(Path("fixtures/shared/finite_outcomes.invalid.json").read_text())
        self.assertNotIn(d["runtime_response_envelope"]["outcome"], {"ANSWER", "ABSTAIN", "DENY", "ERROR"})
        self.assertNotIn(d["policy_decision"]["decision"], {"ALLOW", "ABSTAIN", "DENY", "ERROR"})
        self.assertNotIn(d["promotion_decision"]["decision"], {"ALLOW", "ABSTAIN", "DENY", "ERROR"})
        self.assertNotIn(d["validation_report"]["status"], {"PASS", "FAIL", "ABSTAIN", "ERROR"})
        self.assertNotIn(d["rollback_reference"]["decision"], {"ALLOW", "ABSTAIN", "DENY", "ERROR"})


if __name__ == "__main__":
    unittest.main()
