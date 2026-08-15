from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
WORKFLOW = ROOT / ".github/workflows/validator-suite.yml"


class ValidatorSuiteGuardrailAttributionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = WORKFLOW.read_text(encoding="utf-8")
        workflow = yaml.safe_load(self.text)
        self.steps = workflow["jobs"]["run-validators"]["steps"]

    @staticmethod
    def _run_lines(step: dict) -> list[str]:
        return [
            line.strip()
            for line in str(step.get("run", "")).splitlines()
            if line.strip()
        ]

    def test_guardrails_are_separate_fail_closed_steps(self) -> None:
        expected = [
            ("Validate canonical validator registry", "make validator-registry-check"),
            ("Enforce workflow-security ratchet", "make workflow-security"),
            ("Enforce repository-topology ratchet", "make repository-topology"),
        ]

        step_names = [step.get("name") for step in self.steps]
        positions = []
        executed_lines = [
            line
            for step in self.steps
            for line in self._run_lines(step)
        ]

        for step_name, command in expected:
            self.assertEqual(1, step_names.count(step_name), step_name)
            position = step_names.index(step_name)
            positions.append(position)
            self.assertIn(command, self._run_lines(self.steps[position]))
            self.assertEqual(1, executed_lines.count(command), command)

        self.assertEqual(sorted(positions), positions)
        self.assertNotIn("make repository-guardrails", executed_lines)

    def test_topology_step_preserves_trusted_base_ref_binding(self) -> None:
        step_names = [step.get("name") for step in self.steps]
        topology_step = self.steps[
            step_names.index("Enforce repository-topology ratchet")
        ]

        environment = topology_step.get("env", {})
        trusted_base_ref = str(environment.get("KFM_TRUSTED_BASE_REF", ""))

        self.assertIn("github.event.pull_request.base.sha", trusted_base_ref)
        self.assertIn("github.event.before", trusted_base_ref)
        self.assertIn("make repository-topology", self._run_lines(topology_step))

    def test_workflow_identity_and_read_only_permissions_are_unchanged(self) -> None:
        workflow = yaml.safe_load(self.text)

        self.assertEqual("validator-suite", workflow["name"])
        self.assertEqual("run-validators", workflow["jobs"]["run-validators"]["name"])
        self.assertEqual("ensure-fail-closed", workflow["jobs"]["ensure-fail-closed"]["name"])
        self.assertEqual({"contents": "read"}, workflow["permissions"])


if __name__ == "__main__":
    unittest.main()
