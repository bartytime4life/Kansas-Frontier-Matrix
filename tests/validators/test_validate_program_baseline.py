from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.control_plane.validate_program_baseline import (
    BASELINE_PATH,
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_PATH,
    _read_pinned_blob,
    run_fixture_profile,
    validate_baseline,
    validate_candidate,
)


class ProgramBaselineValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_current_program_baseline_passes(self) -> None:
        result = validate_baseline(BASELINE_PATH)
        self.assertTrue(result.ok, result.findings)

    def test_fixture_profile_has_exact_positive_and_negative_polarity(self) -> None:
        document = json.loads((FIXTURE_ROOT / "cases.json").read_text(encoding="utf-8"))
        self.assertEqual(7, len(document["cases"]))
        self.assertEqual([], document["cases"][0]["expected_codes"])
        self.assertTrue(all(case["expected_codes"] for case in document["cases"][1:]))
        self.assertEqual(0, run_fixture_profile())

    def test_profile_keeps_inherited_and_not_run_states_explicit(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        observations = {item["id"]: item for item in baseline["validation_observations"]}
        self.assertEqual("NOT_RUN", observations["exact_main_hosted_checks"]["outcome"])
        self.assertEqual(
            ("FAIL", "INHERITED", 9),
            (
                observations["object_family_workflow_watch_tests"]["outcome"],
                observations["object_family_workflow_watch_tests"]["failure_class"],
                observations["object_family_workflow_watch_tests"]["finding_count"],
            ),
        )
        self.assertEqual(
            ("FAIL", "INHERITED", 9),
            (
                observations["repository_topology"]["outcome"],
                observations["repository_topology"]["failure_class"],
                observations["repository_topology"]["finding_count"],
            ),
        )

    def test_profile_binds_exact_overlap_and_empty_review_queue(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        self.assertEqual([], baseline["base"]["open_pull_requests"])
        self.assertEqual([2768, 2874, 3365], [item["number"] for item in baseline["tracker_snapshot"]])
        self.assertTrue(all(item["stale_at_base"] for item in baseline["tracker_snapshot"]))

    def test_profile_keeps_drive_lineage_non_authoritative_and_unmodified(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(3, len(baseline["drive_lineage"]))
        self.assertTrue(
            all(
                item["repository_authority"] is False and item["mutated"] is False
                for item in baseline["drive_lineage"]
            )
        )

    def test_unknown_field_fails_schema(self) -> None:
        candidate = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        candidate["self_approval"] = True
        result = validate_candidate(candidate, check_paths=False, check_git=False)
        self.assertIn("SCHEMA_INVALID", {item.code for item in result.findings})

    def test_duplicate_keys_and_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"schema_version":"1.0.0","schema_version":"2.0.0"}', encoding="utf-8")
            nonfinite = Path(directory) / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            duplicate_result = validate_baseline(duplicate, check_paths=False, check_git=False)
            nonfinite_result = validate_baseline(nonfinite, check_paths=False, check_git=False)
        self.assertEqual(["JSON_DUPLICATE_KEY"], sorted({item.code for item in duplicate_result.findings}))
        self.assertEqual(["JSON_NONFINITE_NUMBER"], sorted({item.code for item in nonfinite_result.findings}))

    def test_pinned_digest_replay_ignores_later_worktree_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "KFM fixture"], cwd=root, check=True)
            path = root / "control_plane/example.json"
            path.parent.mkdir(parents=True)
            path.write_bytes(b"pinned-program-baseline-bytes\n")
            subprocess.run(["git", "add", "control_plane/example.json"], cwd=root, check=True)
            subprocess.run(["git", "commit", "-q", "-m", "fixture baseline"], cwd=root, check=True)
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
                "control_plane/example.json",
                base_sha=base_sha,
                repo_root=root,
                field="/fixture/path",
                expected_prefixes=("control_plane/",),
                findings=findings,
            )
        self.assertEqual(b"pinned-program-baseline-bytes\n", observed)
        self.assertEqual([], findings)

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-sensitive-marker-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.json"
            path.write_text(json.dumps({"unexpected": marker}), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/control_plane/validate_program_baseline.py",
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


if __name__ == "__main__":
    unittest.main()
