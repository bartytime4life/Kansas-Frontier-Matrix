from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.control_plane.validate_trust_spine_baseline import (
    BASELINE_PATH,
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_PATH,
    _read_pinned_blob,
    validate_baseline,
)


class TrustSpineBaselineValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_current_baseline_passes_with_paths_digests_and_base_commit(self) -> None:
        result = validate_baseline(BASELINE_PATH)
        self.assertTrue(result.ok, result.findings)

    def test_current_baseline_replays_pinned_tree_not_mutable_worktree(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        projection = next(
            item
            for item in baseline["control_plane_projections"]
            if item["id"] == "document_registry"
        )
        current_digest = "sha256:" + hashlib.sha256(
            (REPO_ROOT / projection["path"]).read_bytes()
        ).hexdigest()
        self.assertNotEqual(projection["sha256"], current_digest)
        result = validate_baseline(BASELINE_PATH)
        self.assertTrue(result.ok, result.findings)

    def test_valid_fixture_passes(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
        self.assertEqual(1, len(files))
        result = validate_baseline(files[0], check_paths=True, check_git=False)
        self.assertTrue(result.ok, result.findings)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        manifest = json.loads(
            (FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(5, len(manifest))
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_baseline(
                    FIXTURE_ROOT / "invalid" / name,
                    check_paths=True,
                    check_git=False,
                )
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(expected),
                    sorted({finding.code for finding in result.findings}),
                )

    def test_missing_declared_paths_fail_closed(self) -> None:
        fixture = FIXTURE_ROOT / "valid/valid_minimal.yaml"
        with tempfile.TemporaryDirectory() as directory:
            result = validate_baseline(
                fixture,
                repo_root=Path(directory),
                check_paths=True,
                check_git=False,
            )
        self.assertIn("PATH_NOT_FOUND", {finding.code for finding in result.findings})

    def test_pinned_digest_replay_ignores_later_worktree_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(
                ["git", "config", "user.email", "fixture@example.invalid"],
                cwd=root,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "KFM fixture"],
                cwd=root,
                check=True,
            )
            path = root / "control_plane/example.yaml"
            path.parent.mkdir(parents=True)
            path.write_bytes(b"pinned-baseline-bytes\n")
            subprocess.run(
                ["git", "add", "control_plane/example.yaml"],
                cwd=root,
                check=True,
            )
            subprocess.run(
                ["git", "commit", "-q", "-m", "fixture baseline"],
                cwd=root,
                check=True,
            )
            base_sha = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            path.write_bytes(b"later-worktree-bytes\n")
            findings = []

            observed = _read_pinned_blob(
                "control_plane/example.yaml",
                base_sha=base_sha,
                repo_root=root,
                field="/fixture/path",
                expected_prefixes=("control_plane/",),
                findings=findings,
            )

        self.assertEqual(b"pinned-baseline-bytes\n", observed)
        self.assertEqual([], findings)

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/control_plane/validate_trust_spine_baseline.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertIn("DIGEST_MISMATCH", result.stdout)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text('{"schema_version":"1.0.0","schema_version":"2.0.0"}', encoding="utf-8")
            result = validate_baseline(path, check_paths=False, check_git=False)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({finding.code for finding in result.findings}),
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.yaml"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_baseline(path, check_paths=False, check_git=False)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({finding.code for finding in result.findings}),
        )

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-sensitive-value-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.yaml"
            path.write_text(json.dumps({"unexpected": marker}), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/control_plane/validate_trust_spine_baseline.py",
                    str(path),
                    "--skip-path-existence",
                    "--skip-git-commit",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertNotIn(marker, result.stdout + result.stderr)
        self.assertIn("SCHEMA_INVALID", result.stdout)

    def test_projection_keeps_known_gaps_explicit(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        catalog = baseline["trust_object_catalog"]
        topology = next(
            item
            for item in baseline["validation_observations"]
            if item["id"] == "repository_topology"
        )
        self.assertEqual("PARTIAL", baseline["implementation_status"])
        self.assertEqual(13, len(catalog["unregistered_required_families"]))
        self.assertEqual("FAIL", topology["outcome"])
        self.assertEqual(9, topology["finding_counts"]["fail_new_drift"])


if __name__ == "__main__":
    unittest.main()
