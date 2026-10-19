from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from tools.validators.directory_governance import (
    validate_repository_governance_parity as parity,
    validate_root_registry as root_registry,
)


class RepositoryGovernanceParityTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(parity._load_schema())

    def test_instance_has_exact_lane_and_coverage_bindings(self) -> None:
        instance = parity._load_yaml(parity.INSTANCE_PATH)
        findings = parity._validate_shape(instance, parity._load_schema())
        self.assertEqual([], findings)
        self.assertEqual(
            sorted(parity.LANE_SPECS),
            [item["lane_id"] for item in instance["lanes"]],
        )
        self.assertEqual(
            sorted(parity.EXPECTED_COVERAGE),
            [item["criterion_id"] for item in instance["coverage"]],
        )

    def test_current_profile_passes_without_claiming_conformance(self) -> None:
        findings, report = parity.validate_current()
        self.assertEqual([], findings)
        self.assertEqual("PASS", report["profile_integrity_outcome"])
        self.assertEqual("HOLD_INHERITED", report["conformance_outcome"])
        self.assertEqual(0, report["topology"]["introduced_finding_count"])
        self.assertEqual(0, report["topology"]["fail_new_drift"])
        self.assertEqual(89, report["topology"]["baselined_warning"])
        self.assertEqual(0, report["topology"]["stale_fingerprints"])

    def test_valid_and_invalid_fixtures_match_reviewed_codes(self) -> None:
        ok, results = parity.validate_fixtures()
        self.assertTrue(ok)
        self.assertEqual(7, len(results))
        self.assertEqual(
            [
                "BASELINE_GROWTH",
                "LANE_NOT_RUN",
                "LANE_OUTCOME_MISMATCH",
                "TOPOLOGY_HOLD_MISCLASSIFIED",
                "TOPOLOGY_INTRODUCED_DRIFT",
                "COVERAGE_SET_INVALID",
            ],
            [item["finding_codes"][0] for item in results if item["finding_codes"]],
        )

    def test_not_run_is_never_classified_as_pass(self) -> None:
        case = parity._load_yaml(parity.FIXTURE_ROOT / "invalid/check_not_run.yaml")
        self.assertIn("LANE_NOT_RUN", {item.code for item in parity.classify_fixture(case)})

    def test_nested_lane_cache_does_not_contaminate_root_registry(self) -> None:
        register = root_registry.resolve_registry(
            json.loads(root_registry.REGISTER_PATH.read_text(encoding="utf-8"))
        )
        with tempfile.TemporaryDirectory() as directory:
            projected = Path(directory)
            for entry in register["roots"]:
                if entry["status"] != "RETIRED":
                    (projected / entry["path"]).mkdir(parents=True, exist_ok=True)

            command = (
                sys.executable,
                "-c",
                "import os; from pathlib import Path; "
                "from hypothesis.database import DirectoryBasedExampleDatabase; "
                "DirectoryBasedExampleDatabase(Path(os.environ['HYPOTHESIS_STORAGE_DIRECTORY']) / 'examples').save(b'kfm-cache-probe', b'value')",
            )
            self.assertEqual("PASS", parity._run_lane(command, projected))
            self.assertFalse((projected / ".hypothesis").exists())

            result = root_registry.validate_register(
                root_registry.REGISTER_PATH,
                repo_root=projected,
            )

        self.assertTrue(result.ok, result.findings)
        self.assertEqual("PASS", result.outcome)

    def test_inherited_failure_cannot_be_mislabeled_pass(self) -> None:
        case = parity._load_yaml(parity.FIXTURE_ROOT / "invalid/hold_as_pass.yaml")
        self.assertIn(
            "TOPOLOGY_HOLD_MISCLASSIFIED",
            {item.code for item in parity.classify_fixture(case)},
        )

    def test_duplicate_yaml_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text("a: 1\na: 2\n", encoding="utf-8")
            with self.assertRaises(parity.ParityError):
                parity._load_yaml(path)

    def test_pinned_blob_replay_ignores_worktree_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "KFM Fixture"], cwd=root, check=True)
            target = root / "governing.md"
            target.write_text("pinned\n", encoding="utf-8")
            subprocess.run(["git", "add", "governing.md"], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "fixture"], cwd=root, check=True)
            sha = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            target.write_text("mutated\n", encoding="utf-8")
            blob = parity._read_pinned_blob(root, sha, "governing.md")
            self.assertEqual(b"pinned\n", blob)
            self.assertNotEqual(
                hashlib.sha256(target.read_bytes()).hexdigest(),
                hashlib.sha256(blob).hexdigest(),
            )

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "DO_NOT_ECHO_MRTS04_FIXTURE"
        instance = parity._load_yaml(parity.INSTANCE_PATH)
        instance["untrusted"] = marker
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.yaml"
            path.write_text(json.dumps(instance), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(Path(parity.__file__)), "--instance", str(path)],
                cwd=parity.REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(1, result.returncode)
        self.assertNotIn(marker, result.stdout + result.stderr)
        self.assertIn("SCHEMA_INVALID", result.stdout)

    def test_cli_rejects_an_unresolvable_trusted_base(self) -> None:
        environment = os.environ.copy()
        environment["KFM_TRUSTED_BASE_REF"] = "0" * 40
        result = subprocess.run(
            [sys.executable, str(Path(parity.__file__))],
            cwd=parity.REPO_ROOT,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn('"profile_integrity_outcome":"ERROR"', result.stdout)

    def test_report_has_constant_non_authority_boundary(self) -> None:
        report = parity._report([], {"repository-topology": "HOLD_INHERITED"}, {})
        self.assertFalse(report["authority"]["authorizes_baseline_expansion"])
        self.assertFalse(report["authority"]["authorizes_migration_or_deletion"])
        self.assertFalse(report["authority"]["authorizes_release"])
        self.assertFalse(report["authority"]["publishes"])

    def test_topology_delta_treats_strict_evidence_shrink_as_resolution(self) -> None:
        prior = parity.topology._finding(
            "KFM-TOPO-009",
            "scaffold-only-leaf-directories",
            ["fixtures/a", "fixtures/b"],
        )
        shrunk = parity.topology._finding(
            "KFM-TOPO-009",
            "scaffold-only-leaf-directories",
            ["fixtures/b"],
        )

        introduced, resolved = parity._classify_topology_delta(
            [shrunk],
            [prior],
        )

        self.assertEqual([], introduced)
        self.assertEqual([prior.fingerprint], resolved)


class GovernanceParityWorkflowTests(unittest.TestCase):
    """Exercise the actual workflow shell against disposable Git history."""

    def setUp(self) -> None:
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        self.git("init", "--quiet")
        self.commit()
        self.first_commit = self.git("rev-parse", "HEAD").strip()
        self.commit()
        self.head_commit = self.git("rev-parse", "HEAD").strip()
        workflow = parity.REPO_ROOT / ".github/workflows/repository-governance-parity.yml"
        steps = yaml.safe_load(workflow.read_text())["jobs"][
            "validate-repository-governance-parity"
        ]["steps"]
        step = next(s for s in steps if s["name"] == "Run deterministic MRTS-04 parity profile")
        self.assertEqual("${{ github.event.pull_request.base.sha }}", step["env"]["KFM_PR_BASE_SHA"])
        self.script = step["run"]
        self.bin = self.root / "bin"
        self.bin.mkdir()
        make = self.bin / "make"
        make.write_text('#!/bin/sh\nprintf "%s\\n%s\\n" "$KFM_TRUSTED_BASE_REF" "$*" > "$PARITY_TEST_LOG"\n')
        make.chmod(0o700)
        self.log = self.root / "invocation.txt"

    def git(self, *args: str) -> str:
        return subprocess.check_output(["git", *args], cwd=self.root, text=True)

    def commit(self) -> None:
        self.git("-c", "user.name=Parity test", "-c", "user.email=parity@example.invalid",
                 "commit", "--quiet", "--allow-empty", "-m", "Test history")

    def run_step(self, pr_base: str = "") -> subprocess.CompletedProcess[str]:
        env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ["PATH"],
                   KFM_PR_BASE_SHA=pr_base, PARITY_TEST_LOG=str(self.log))
        return subprocess.run(["bash", "-c", self.script], cwd=self.root, env=env,
                              capture_output=True, text=True, timeout=10)

    def test_push_resolves_parent_before_calling_validator(self) -> None:
        result = self.run_step()
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual([self.first_commit, "repository-governance-parity"], self.log.read_text().splitlines())

    def test_pull_request_retains_exact_trusted_base(self) -> None:
        result = self.run_step(self.head_commit)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(self.head_commit, self.log.read_text().splitlines()[0])

    def test_symbolic_or_malformed_pr_base_fails_before_make(self) -> None:
        for value in ("HEAD^", "a" * 39, "a" * 40 + "; printf unsafe"):
            with self.subTest(value=value):
                result = self.run_step(value)
                self.assertNotEqual(0, result.returncode)
                self.assertFalse(self.log.exists())

    def test_missing_parent_fails_before_make(self) -> None:
        # Rewind disposable test history only; never the project checkout.
        self.git("reset", "--quiet", "--hard", self.first_commit)
        result = self.run_step()
        self.assertNotEqual(0, result.returncode)
        self.assertFalse(self.log.exists())


if __name__ == "__main__":
    unittest.main()
