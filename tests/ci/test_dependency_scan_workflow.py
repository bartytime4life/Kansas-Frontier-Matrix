"""Exercise CI-lock and crop-lock audit wiring and failure propagation without network access."""
from __future__ import annotations

import os
from pathlib import Path
import shlex
import subprocess
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/dependency-scan.yml"
LOCK = "pipelines/domains/soil/crop_casma_tiles/requirements-tiles.lock"


def assert_audit_shell_propagates_status(case: unittest.TestCase, audit: str) -> None:
    """Run the workflow's audit command against a stub interpreter for each exit status."""
    with tempfile.TemporaryDirectory() as directory:
        binary = Path(directory) / "python"
        binary.write_text('#!/bin/sh\nprintf "%s\\n" "$@" > "$AUDIT_ARGS"\nexit "$AUDIT_STATUS"\n')
        binary.chmod(0o700)
        args_path = Path(directory) / "args"
        for status in (0, 1, 2):
            with case.subTest(status=status):
                env = dict(os.environ, PATH=directory + os.pathsep + os.environ["PATH"],
                           AUDIT_ARGS=str(args_path), AUDIT_STATUS=str(status))
                result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", audit],
                                        env=env, capture_output=True, text=True, timeout=5)
                case.assertEqual(result.returncode, status)
                case.assertEqual(args_path.read_text().splitlines(), shlex.split(audit)[1:])


class CiLockAuditWorkflowTest(unittest.TestCase):
    """Every tools/ci/*.lock is audited; Dependabot does not parse these files."""

    def setUp(self):
        self.workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        self.job = self.workflow["jobs"]["pip-audit"]
        self.audit = next(step["run"] for step in self.job["steps"]
                          if "-m pip_audit" in step.get("run", ""))

    def test_audit_covers_every_ci_lock_without_installing(self):
        locks = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "tools/ci").glob("*.lock"))
        self.assertGreaterEqual(len(locks), 6)
        argv = shlex.split(self.audit)
        audited = [argv[index + 1] for index, arg in enumerate(argv) if arg == "--requirement"]
        self.assertEqual(audited, locks, "add each new tools/ci/*.lock to the pip-audit step")
        self.assertEqual(argv[:3], ["python", "-m", "pip_audit"])
        self.assertEqual(argv[3 + 2 * len(locks):], [
            "--require-hashes", "--disable-pip", "--strict",
            "--progress-spinner", "off", "--desc", "off", "--format", "columns",
        ])
        self.assertNotIn("--no-deps", argv, "--no-deps makes pip-audit dry-run install every lock")
        runs = [step["run"] for step in self.job["steps"] if "run" in step]
        self.assertIn("python tools/ci/install_python_ci.py audit-tool", runs)
        self.assertNotIn("continue-on-error", self.job)
        for step in self.job["steps"]:
            self.assertNotIn("continue-on-error", step)

    def test_actual_audit_shell_propagates_findings_and_scanner_errors(self):
        assert_audit_shell_propagates_status(self, self.audit)


class CropCasmaAuditWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        self.job = self.workflow["jobs"]["pip-audit-crop-casma"]

    def test_audit_uses_exact_lock_in_supported_read_only_runtime(self):
        self.assertEqual(self.workflow["permissions"], {"contents": "read"})
        self.assertNotIn("permissions", self.job)
        self.assertNotIn("if", self.job)
        self.assertNotIn("continue-on-error", self.job)
        runtimes = [step["with"]["python-version"] for step in self.job["steps"]
                    if str(step.get("uses", "")).startswith("actions/setup-python@")]
        self.assertEqual(runtimes, ["3.12"])
        for step in self.job["steps"]:
            self.assertNotIn("continue-on-error", step)
            if "uses" in step:
                self.assertRegex(step["uses"], r"@[0-9a-f]{40}$")
            if str(step.get("uses", "")).startswith("actions/checkout@"):
                self.assertIs(step["with"]["persist-credentials"], False)
        runs = [step["run"] for step in self.job["steps"] if "run" in step]
        self.assertIn("python tools/ci/install_python_ci.py audit-tool", runs)
        audit = [run for run in runs if "-m pip_audit" in run]
        self.assertEqual(len(audit), 1)
        self.assertEqual(shlex.split(audit[0]), [
            "python", "-m", "pip_audit", "--requirement", LOCK,
            "--require-hashes", "--disable-pip", "--strict",
            "--progress-spinner", "off", "--desc", "off", "--format", "columns",
        ])
        self.assertIn("pillow==13.0.0", (ROOT / LOCK).read_text().lower())

    def test_actual_audit_shell_propagates_findings_and_scanner_errors(self):
        audit = next(step["run"] for step in self.job["steps"]
                     if "-m pip_audit" in step.get("run", ""))
        assert_audit_shell_propagates_status(self, audit)

    def test_regression_is_wired_for_workflow_only_changes(self):
        path = ROOT / ".github/workflows/python-dependency-lock.yml"
        text = path.read_text(encoding="utf-8")
        workflow = yaml.safe_load(text)
        events = workflow.get("on", workflow.get(True))
        for event in ("pull_request", "push"):
            self.assertIn(".github/workflows/dependency-scan.yml", events[event]["paths"])
        self.assertIn("python -m unittest discover -s tests/ci -p 'test_dependency_scan_workflow.py' -v", text)


if __name__ == "__main__":
    unittest.main()
