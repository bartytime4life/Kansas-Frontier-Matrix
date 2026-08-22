from __future__ import annotations

import fnmatch
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.control_plane.validate_object_family_register import (
    FIXTURE_ROOT,
    REGISTER_PATH,
    REQUIRED_FAMILIES,
    REPO_ROOT,
    SCHEMA_PATH,
    validate_register,
)


class ObjectFamilyRegisterValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_current_register_passes_with_real_repository_paths(self) -> None:
        result = validate_register(REGISTER_PATH)
        self.assertTrue(result.ok, result.findings)

    def test_workflow_watches_every_declared_catalog_surface(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        workflow = (
            REPO_ROOT / ".github/workflows/object-family-register.yml"
        ).read_text(encoding="utf-8")
        patterns = re.findall(r'^\s+- "([^"]+)"\s*$', workflow, flags=re.MULTILINE)
        path_roles = (
            "contract_paths",
            "schema_paths",
            "policy_paths",
            "fixture_paths",
            "validator_paths",
            "test_paths",
            "workflow_paths",
            "emitter_paths",
        )
        for entry in register["entries"]:
            for role in path_roles:
                for path in entry[role]:
                    with self.subTest(family_id=entry["family_id"], role=role, path=path):
                        matched = sum(
                            1 for pattern in patterns if fnmatch.fnmatchcase(path, pattern)
                        )
                        self.assertGreaterEqual(
                            matched,
                            2,
                            f"{path} is not watched by both pull_request and push filters",
                        )

    def test_current_catalog_has_exact_milestone_family_set(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        required = {
            entry["family_id"]: entry["display_name"]
            for entry in register["entries"]
            if entry["required_by_milestone"]
        }
        self.assertEqual(REQUIRED_FAMILIES, required)
        self.assertEqual(16, register["required_registered_count"])
        self.assertEqual(3, register["other_registered_count"])

    def test_current_catalog_keeps_conflicts_and_gaps_explicit(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        by_id = {entry["family_id"]: entry for entry in register["entries"]}
        conflicted = {
            entry["family_id"]
            for entry in register["entries"]
            if entry["required_by_milestone"]
            and entry["implementation_status"] == "CONFLICTED"
        }
        self.assertEqual(11, len(conflicted))
        self.assertEqual(11, register["conflicted_required_count"])
        self.assertEqual("PARTIAL", by_id["withdrawal_notice"]["implementation_status"])
        self.assertEqual([], by_id["withdrawal_notice"]["validator_paths"])
        for family_id in conflicted:
            with self.subTest(family_id=family_id):
                compatibility = by_id[family_id]["compatibility"]
                self.assertEqual(
                    "multiple_candidates_unresolved",
                    compatibility["posture"],
                )
                self.assertGreaterEqual(len(compatibility["candidate_paths"]), 2)

    def test_current_relationships_are_closed_and_non_self_referential(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        ids = {entry["family_id"] for entry in register["entries"]}
        roles = (
            "dependency_family_ids",
            "evidence_family_ids",
            "release_family_ids",
            "correction_family_ids",
            "rollback_family_ids",
        )
        for entry in register["entries"]:
            for role in roles:
                with self.subTest(family_id=entry["family_id"], role=role):
                    self.assertEqual(sorted(set(entry[role])), entry[role])
                    self.assertTrue(set(entry[role]).issubset(ids))
                    self.assertNotIn(entry["family_id"], entry[role])

    def test_valid_fixture_passes(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
        self.assertEqual(1, len(files))
        result = validate_register(files[0], check_paths=False)
        self.assertTrue(result.ok, result.findings)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        manifest = json.loads(
            (FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(7, len(manifest))
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_register(
                    FIXTURE_ROOT / "invalid" / name,
                    check_paths=False,
                )
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(expected),
                    sorted({finding.code for finding in result.findings}),
                )

    def test_current_register_passes_with_projected_paths(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        path_roles = (
            "contract_paths",
            "schema_paths",
            "policy_paths",
            "fixture_paths",
            "validator_paths",
            "test_paths",
            "workflow_paths",
            "emitter_paths",
        )
        with tempfile.TemporaryDirectory() as directory:
            projected = Path(directory)
            for entry in register["entries"]:
                for role in path_roles:
                    for relative in entry[role]:
                        target = projected / relative
                        if Path(relative).suffix:
                            target.parent.mkdir(parents=True, exist_ok=True)
                            target.write_text("placeholder\n", encoding="utf-8")
                        else:
                            target.mkdir(parents=True, exist_ok=True)
            result = validate_register(REGISTER_PATH, repo_root=projected)
        self.assertTrue(result.ok, result.findings)

    def test_missing_declared_path_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = validate_register(REGISTER_PATH, repo_root=Path(directory))
        self.assertIn("PATH_NOT_FOUND", {finding.code for finding in result.findings})

    def test_impossible_implementation_status_fails_closed(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        register["entries"][0]["implementation_status"] = "IMPLEMENTED"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "impossible.yaml"
            path.write_text(json.dumps(register), encoding="utf-8")
            result = validate_register(path, check_paths=False)
        self.assertIn(
            "IMPLEMENTATION_STATUS_MISMATCH",
            {finding.code for finding in result.findings},
        )

    def test_self_relationship_fails_closed(self) -> None:
        register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
        family_id = register["entries"][0]["family_id"]
        register["entries"][0]["dependency_family_ids"] = [family_id]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "self-relationship.yaml"
            path.write_text(json.dumps(register), encoding="utf-8")
            result = validate_register(path, check_paths=False)
        self.assertIn("SELF_RELATIONSHIP", {finding.code for finding in result.findings})

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/control_plane/validate_object_family_register.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertIn("SELF_AUTHORITY_CLAIM", result.stdout)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text('{"version":"v1","version":"v2"}', encoding="utf-8")
            result = validate_register(path, check_paths=False)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({finding.code for finding in result.findings}),
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.yaml"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_register(path, check_paths=False)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({finding.code for finding in result.findings}),
        )

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-secret-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.yaml"
            path.write_text(json.dumps({"unexpected": marker}), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/control_plane/validate_object_family_register.py",
                    str(path),
                    "--skip-path-existence",
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
