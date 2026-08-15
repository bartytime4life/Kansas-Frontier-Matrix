from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]
WORKFLOW = ROOT / ".github/workflows/validator-suite.yml"


class ValidatorSuiteGuardrailAttributionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = WORKFLOW.read_text(encoding="utf-8")

    def test_guardrails_are_separate_fail_closed_steps(self) -> None:
        expected = [
            ("Validate canonical validator registry", "make validator-registry-check"),
            ("Enforce workflow-security ratchet", "make workflow-security"),
            ("Enforce repository-topology ratchet", "make repository-topology"),
        ]

        positions = []
        for step_name, command in expected:
            step_marker = f"- name: {step_name}"
            self.assertEqual(1, self.text.count(step_marker), step_marker)
            self.assertEqual(1, self.text.count(command), command)
            positions.append(self.text.index(step_marker))

        self.assertEqual(sorted(positions), positions)
        self.assertNotIn("make repository-guardrails", self.text)

    def test_topology_step_preserves_trusted_base_ref_binding(self) -> None:
        topology_start = self.text.index("- name: Enforce repository-topology ratchet")
        inventory_start = self.text.index(
            "- name: Require a non-vacuous aggregate validator inventory"
        )
        topology_step = self.text[topology_start:inventory_start]

        self.assertIn("KFM_TRUSTED_BASE_REF:", topology_step)
        self.assertIn("github.event.pull_request.base.sha", topology_step)
        self.assertIn("github.event.before", topology_step)
        self.assertIn("make repository-topology", topology_step)

    def test_workflow_identity_and_read_only_permissions_are_unchanged(self) -> None:
        self.assertIn("name: validator-suite", self.text)
        self.assertIn("  run-validators:\n    name: run-validators", self.text)
        self.assertIn("  ensure-fail-closed:\n    name: ensure-fail-closed", self.text)
        self.assertIn("permissions:\n  contents: read", self.text)


if __name__ == "__main__":
    unittest.main()
