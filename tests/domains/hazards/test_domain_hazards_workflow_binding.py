from __future__ import annotations

import shlex
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
WORKFLOW = ROOT / ".github/workflows/domain-hazards.yml"


class DomainHazardsWorkflowBindingTests(unittest.TestCase):
    def load_workflow(self) -> dict:
        return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))

    def test_hosted_events_and_no_network_environment_remain_bounded(self) -> None:
        workflow = self.load_workflow()
        triggers = workflow["on"]

        self.assertIn("pull_request", triggers)
        self.assertEqual(triggers["push"]["branches"], ["main"])
        self.assertIn("workflow_dispatch", triggers)
        self.assertEqual(
            {
                key: workflow["env"][key]
                for key in (
                    "KFM_NO_NETWORK",
                    "PYTHONDONTWRITEBYTECODE",
                    "PYTHONHASHSEED",
                    "TZ",
                )
            },
            {
                "KFM_NO_NETWORK": "1",
                "PYTHONDONTWRITEBYTECODE": "1",
                "PYTHONHASHSEED": "0",
                "TZ": "UTC",
            },
        )

    def test_hosted_validation_executes_materiality_and_binding_proofs(self) -> None:
        workflow = self.load_workflow()
        steps = {
            str(step.get("name", "")): str(step.get("run", ""))
            for step in workflow["jobs"]["validate-hazards"]["steps"]
        }
        validation_lines = {
            line.strip()
            for line in steps["Validate bounded Hazards materiality lane"].splitlines()
        }

        self.assertIn(
            "python -m unittest -v tests.domains.hazards.test_hazards_smoke",
            validation_lines,
        )
        self.assertIn("make hazards-validate", validation_lines)
        self.assertEqual(
            shlex.split(steps["Prove hosted Hazards workflow binding"]),
            [
                "python",
                "-m",
                "unittest",
                "tests.domains.hazards.test_domain_hazards_workflow_binding",
                "-v",
            ],
        )
        summary = steps["Record Hazards validation scope"]
        self.assertIn(
            "python -m unittest "
            "tests.domains.hazards.test_domain_hazards_workflow_binding -v",
            summary,
        )
        self.assertIn(
            "hosted trigger, environment, command, proof-hold, and release-hold "
            "workflow bindings",
            summary,
        )

    def test_proof_and_release_jobs_remain_explicit_holds(self) -> None:
        workflow = self.load_workflow()
        expected = {
            "build-proof-hazards": (
                "Evaluate Hazards proof readiness",
                "WORKFLOW_HOLD: no accepted Hazards proof producer or deterministic proof command",
            ),
            "publish-dry-run-hazards": (
                "Evaluate Hazards release dry-run readiness",
                "WORKFLOW_HOLD: no accepted Hazards release dry-run command or candidate manifest contract",
            ),
        }

        for job_name, (step_name, marker) in expected.items():
            with self.subTest(job=job_name):
                steps = {
                    str(step.get("name", "")): str(step.get("run", ""))
                    for step in workflow["jobs"][job_name]["steps"]
                }
                self.assertIn(marker, steps[step_name])


if __name__ == "__main__":
    unittest.main()
