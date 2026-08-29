from __future__ import annotations

import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[4]
WORKFLOW = ROOT / ".github/workflows/hazards-evidence-bundle-convergence.yml"
SELF_PATH = (
    "tests/validators/domains/hazards/"
    "test_evidence_bundle_convergence_workflow_binding.py"
)
REQUIRED_TRIGGER_PATHS = {
    "schemas/contracts/v1/**",
    "fixtures/contracts/v1/evidence/evidence_bundle/**",
    "tools/validators/_common/jsonschema_runner.py",
    "tools/validators/_common/local_resolver.py",
    "tools/validators/validate_hazards_evidence_bundle_projection.py",
    "tests/validators/domains/hazards/test_evidence_bundle_schema_convergence.py",
    SELF_PATH,
    "tools/ci/install_python_ci.py",
    "tools/ci/python-test.lock",
    "pyproject.toml",
    ".github/workflows/hazards-evidence-bundle-convergence.yml",
}


class HazardsEvidenceBundleConvergenceWorkflowBindingTests(unittest.TestCase):
    def load_workflow(self) -> dict:
        return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))

    def test_direct_dependencies_trigger_pull_request_and_main_push(self) -> None:
        workflow = self.load_workflow()
        triggers = workflow["on"]

        for event in ("pull_request", "push"):
            with self.subTest(event=event):
                paths = set(triggers[event]["paths"])
                self.assertTrue(
                    REQUIRED_TRIGGER_PATHS.issubset(paths),
                    f"{event} must cover the complete local execution seam",
                )

        self.assertEqual(triggers["push"]["branches"], ["main"])
        self.assertIn("workflow_dispatch", triggers)

    def test_hosted_job_executes_the_binding_proof(self) -> None:
        workflow = self.load_workflow()
        commands = "\n".join(
            str(step.get("run", ""))
            for step in workflow["jobs"]["validate"]["steps"]
        )

        self.assertIn(
            "test_evidence_bundle_convergence_workflow_binding.py",
            commands,
        )
        self.assertIn("test_evidence_bundle_schema_convergence.py", commands)


if __name__ == "__main__":
    unittest.main()
