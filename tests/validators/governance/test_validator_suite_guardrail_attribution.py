"""Fail-closed scheduling and shell-contract checks for validator-suite.

The four guardrails are independent diagnostics, not dependencies of each other.
Their exact !cancelled() condition overrides Actions' default success() gate and
still permits cancellation. A later pass must never neutralize an earlier failure.

Shell tests execute the workflow bodies with a bounded, argv-recording make
substitute. They prove dispatch and exit propagation, not real validator behavior,
GitHub expression evaluation, runner egress isolation, or repository conformance.
"""

from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
WORKFLOW = ROOT / ".github/workflows/validator-suite.yml"
BASH = shutil.which("bash")
GUARDRAILS = (
    ("Validate canonical validator registry", "make validator-registry-check"),
    (
        "Enforce critical-document structure sentinel",
        "make docs-critical-structure",
    ),
    ("Enforce workflow-security ratchet", "make workflow-security"),
    ("Enforce repository-topology ratchet", "make repository-topology"),
)


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
        expected = GUARDRAILS

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
            step = self.steps[position]
            self.assertEqual("bash", step.get("shell"))
            self.assertEqual(
                ["set -euo pipefail", command], self._run_lines(step)
            )
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

    def test_independent_validation_stages_survive_prior_failure(self) -> None:
        expected_steps = [
            "Validate canonical validator registry",
            "Enforce critical-document structure sentinel",
            "Enforce workflow-security ratchet",
            "Enforce repository-topology ratchet",
            "Require a non-vacuous aggregate validator inventory",
            "Test shared JSON Schema runner fixture semantics",
            "Test generated-receipt shape and artifact integrity",
            "Test material-change assessment profile",
            "Run repository aggregate validators",
        ]
        steps_by_name = {step.get("name"): step for step in self.steps}

        for step_name in expected_steps:
            with self.subTest(step=step_name):
                self.assertIn(step_name, steps_by_name)
                self.assertEqual(
                    "${{ !cancelled() }}",
                    str(steps_by_name[step_name].get("if", "")),
                )

        summary_step = steps_by_name["Record aggregate-validator boundary"]
        self.assertEqual("always()", str(summary_step.get("if", "")))

    def test_failures_cannot_be_neutralized_by_continue_on_error(self) -> None:
        workflow = yaml.safe_load(self.text)
        for job_name, job in workflow["jobs"].items():
            with self.subTest(job=job_name):
                self.assertIs(False, job.get("continue-on-error", False))
            for step in job["steps"]:
                with self.subTest(job=job_name, step=step.get("name")):
                    self.assertIs(False, step.get("continue-on-error", False))

    def test_attribution_test_is_mandatory_before_guardrails(self) -> None:
        step_names = [step.get("name") for step in self.steps]
        name = "Test validator-suite guardrail attribution"
        self.assertEqual(1, step_names.count(name))
        position = step_names.index(name)
        step = self.steps[position]
        self.assertNotIn("if", step)  # Normal bootstrap-success gating only.
        self.assertEqual("bash", step.get("shell"))
        self.assertEqual(
            [
                "python -m unittest "
                "tests.validators.governance.test_validator_suite_guardrail_attribution "
                "--verbose"
            ],
            self._run_lines(step),
        )
        for guardrail, _ in GUARDRAILS:
            self.assertLess(position, step_names.index(guardrail))

    @unittest.skipUnless(BASH, "Bash is required for workflow shell execution")
    def test_guardrail_shells_preserve_make_exit_codes(self) -> None:
        steps_by_name = {step.get("name"): step for step in self.steps}
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake_make = root / "make"
            calls = root / "calls.txt"
            fake_make.write_text(
                '#!/bin/sh\n'
                'printf "%s\\n" "$*" >> "$KFM_TEST_CALLS"\n'
                'exit "$KFM_TEST_EXIT"\n',
                encoding="utf-8",
            )
            fake_make.chmod(0o700)
            for step_name, command in GUARDRAILS:
                step = steps_by_name[step_name]
                # Execute only the closed two-line contract, never arbitrary YAML.
                self.assertEqual(
                    ["set -euo pipefail", command], self._run_lines(step)
                )
                for exit_code in (0, 1, 7):
                    with self.subTest(step=step_name, exit_code=exit_code):
                        calls.unlink(missing_ok=True)
                        result = subprocess.run(
                            [
                                BASH, "--noprofile", "--norc", "-e", "-o",
                                "pipefail", "-c", step["run"],
                            ],
                            cwd=root,
                            env={
                                "PATH": str(root),
                                "KFM_TEST_CALLS": str(calls),
                                "KFM_TEST_EXIT": str(exit_code),
                            },
                            capture_output=True,
                            text=True,
                            timeout=5,
                            check=False,
                        )
                        self.assertEqual(
                            exit_code, result.returncode,
                            (result.stdout, result.stderr),
                        )
                        self.assertEqual(
                            [command.removeprefix("make ")],
                            calls.read_text(encoding="utf-8").splitlines(),
                        )

    def test_workflow_identity_and_read_only_permissions_are_unchanged(self) -> None:
        workflow = yaml.safe_load(self.text)

        self.assertEqual("validator-suite", workflow["name"])
        self.assertEqual("run-validators", workflow["jobs"]["run-validators"]["name"])
        self.assertEqual("ensure-fail-closed", workflow["jobs"]["ensure-fail-closed"]["name"])
        self.assertEqual({"contents": "read"}, workflow["permissions"])


if __name__ == "__main__":
    unittest.main()
