"""Check receipt contexts and fail-closed shell wiring, not source/release truth.

The shell tests execute committed run blocks with a recording Python substitute.
They do not execute the receipt validator or contact GitHub. Native integrity is
checked separately by the workflow at the actual checkout.
"""
from __future__ import annotations

import fnmatch
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/directory-root-registry.yml"
HELPER = "tools/validators/validate_generated_receipt.py"
PREFIX = "data/receipts/generated/"
HISTORICAL = PREFIX + "genrec-directory-root-registry-current-binding-20260815.json"
ANCESTOR = "8d235ebc6e7e80704c0f3f93d7c04e338af6a9a1"
CURRENT = (
    PREFIX + "genrec-topology-diagnostic-log-safety-20260911.json",
    PREFIX + "genrec-directory-root-registry-replay-20260911.json",
)
HISTORICAL_STEP = "Replay historical root-registry authoring receipt"
CURRENT_STEP = "Verify current diagnostic and workflow authoring receipts"


def _run(script: str, fail_at: int = -1) -> tuple[int, list[list[str]]]:
    """Record argv and inject one failure in a disposable, secret-free shell."""
    bash = shutil.which("bash")
    if bash is None:
        raise RuntimeError("Bash is required for the requested workflow test")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        shim = root / "python"
        shim.write_text(
            f"#!{sys.executable}\n"
            "import json, os, pathlib, sys\n"
            "p = pathlib.Path(os.environ['CALLS'])\n"
            "rows = p.read_text().splitlines() if p.exists() else []\n"
            "with p.open('a') as f: f.write(json.dumps(sys.argv[1:]) + '\\n')\n"
            "raise SystemExit(23 if len(rows) == int(os.environ['FAIL_AT']) else 0)\n",
            encoding="utf-8",
        )
        shim.chmod(0o700)
        calls = root / "calls.jsonl"
        completed = subprocess.run(
            [bash, "--noprofile", "--norc", "-e", "-o", "pipefail", "-c", script],
            cwd=root,
            env={"PATH": str(root), "HOME": str(root), "CALLS": str(calls),
                 "FAIL_AT": str(fail_at), "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True, text=True, timeout=10, check=False,
        )
        if completed.stderr:
            raise AssertionError(completed.stderr)
        rows = [json.loads(line) for line in calls.read_text().splitlines()] if calls.exists() else []
        return completed.returncode, rows


class DirectoryRootRegistryWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        cls.job = cls.workflow["jobs"]["validate-directory-root-registry"]
        cls.steps = {step["name"]: step for step in cls.job["steps"]}

    def test_read_only_event_and_job_boundary(self) -> None:
        self.assertEqual({"pull_request", "push", "workflow_dispatch"}, set(self.workflow["on"]))
        self.assertEqual(["main"], self.workflow["on"]["push"]["branches"])
        self.assertEqual({"contents": "read"}, self.workflow["permissions"])
        self.assertNotIn("permissions", self.job)
        self.assertEqual(10, self.job["timeout-minutes"])
        self.assertEqual("1", self.workflow["env"]["KFM_NO_NETWORK"])
        self.assertEqual({"validate-directory-root-registry"}, set(self.workflow["jobs"]))

    def test_history_is_available_without_switching_candidate_or_persisting_credentials(self) -> None:
        step = self.steps["Check out tested revision without persisted credentials"]
        self.assertEqual("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", step["uses"])
        self.assertEqual({"persist-credentials": False, "fetch-depth": 0}, step["with"])
        self.assertEqual(1, sum("actions/checkout@" in s.get("uses", "") for s in self.job["steps"]))

    def test_direct_inputs_trigger_both_event_lanes(self) -> None:
        inputs = [
            ".github/workflows/directory-root-registry.yml",
            "tests/ci/test_directory_root_registry_workflow.py", HELPER,
            "tools/validators/_common/local_resolver.py",
            "schemas/contracts/v1/receipts/generated_receipt.schema.json",
            "tools/ci/install_python_ci.py", "tools/ci/python-test.lock",
            "tools/ci/python-dependency-lock-migration.json", "pyproject.toml",
            "tests/validators/directory_governance/test_validate_output_security_topology.py",
            HISTORICAL, *CURRENT,
        ]
        for event in ("pull_request", "push"):
            patterns = self.workflow["on"][event]["paths"]
            self.assertEqual(len(patterns), len(set(patterns)))
            for path in inputs:
                with self.subTest(event=event, path=path):
                    self.assertTrue(any(fnmatch.fnmatchcase(path, pat) for pat in patterns), path)

    def test_existing_current_registry_checks_are_unchanged(self) -> None:
        expected = {
            "Validate fixture polarity": ["tools/validators/directory_governance/validate_root_registry.py", "--fixtures"],
            "Validate current register against current top-level roots": ["tools/validators/directory_governance/validate_root_registry.py"],
        }
        for name, args in expected.items():
            with self.subTest(name=name):
                code, calls = _run(self.steps[name]["run"])
                self.assertEqual((0, [args]), (code, calls))
        code, calls = _run(self.steps["Run focused deterministic no-network tests"]["run"])
        self.assertEqual((0, [["-m", "unittest", "discover", "--start-directory",
                              "tests/validators/directory_governance", "--pattern",
                              "test_validate_root_registry.py", "--verbose"]]), (code, calls))

    def test_workflow_regression_suite_is_not_optional(self) -> None:
        step = self.steps["Test receipt replay workflow boundary"]
        code, calls = _run(step["run"])
        self.assertEqual((0, [["-m", "unittest", "discover", "--start-directory", "tests/ci",
                              "--pattern", "test_directory_root_registry_workflow.py", "--verbose"]]),
                         (code, calls))
        self.assertNotIn("if", step)
        self.assertNotIn("continue-on-error", step)

    def test_historical_argv_is_exact_and_ancestor_pinned(self) -> None:
        code, calls = _run(self.steps[HISTORICAL_STEP]["run"])
        self.assertEqual((0, [[HELPER, HISTORICAL, "--repo-root", ".", "--artifact-git-ref", ANCESTOR]]),
                         (code, calls))

    def test_current_artifacts_never_use_historical_replay(self) -> None:
        code, calls = _run(self.steps[CURRENT_STEP]["run"])
        self.assertEqual((0, [[HELPER, p, "--repo-root", "."] for p in CURRENT]), (code, calls))

    def test_every_receipt_failure_propagates_and_stops_later_commands(self) -> None:
        for name, count in ((HISTORICAL_STEP, 1), (CURRENT_STEP, 2)):
            for fail_at in range(count):
                with self.subTest(step=name, fail_at=fail_at):
                    code, calls = _run(self.steps[name]["run"], fail_at)
                    self.assertEqual(23, code)
                    self.assertEqual(fail_at + 1, len(calls))

    def test_receipt_checks_cannot_be_skipped_or_soft_failed(self) -> None:
        for name in (HISTORICAL_STEP, CURRENT_STEP):
            step = self.steps[name]
            self.assertNotIn("if", step)
            self.assertNotIn("continue-on-error", step)
            self.assertTrue(step["run"].startswith("set -euo pipefail\n"))
        names = [s["name"] for s in self.job["steps"]]
        self.assertLess(names.index(HISTORICAL_STEP), names.index(CURRENT_STEP))
        self.assertLess(names.index(CURRENT_STEP), names.index("Record trust boundary"))

    def test_current_receipt_binds_the_actual_workflow_and_test_bytes(self) -> None:
        import hashlib
        receipt = json.loads((ROOT / CURRENT[1]).read_text(encoding="utf-8"))
        paths = [".github/workflows/directory-root-registry.yml",
                 "tests/ci/test_directory_root_registry_workflow.py"]
        self.assertEqual(paths, receipt["artifact_paths"])
        self.assertEqual(set(paths), set(receipt["artifact_hashes"]))
        for path in paths:
            self.assertEqual("sha256:" + hashlib.sha256((ROOT / path).read_bytes()).hexdigest(),
                             receipt["artifact_hashes"][path])


if __name__ == "__main__":
    unittest.main()
