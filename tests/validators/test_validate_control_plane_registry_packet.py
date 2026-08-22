from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from tools.validators.control_plane.validate_control_plane_registry_packet import (
    FIXTURE_ROOT,
    REGISTRY_PATHS,
    REPO_ROOT,
    SCHEMA_PATH,
    validate_registry,
)


class ControlPlaneRegistryPacketValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_packet_contains_exactly_the_seven_existing_registry_paths(self) -> None:
        self.assertEqual(
            {
                "contradiction_register",
                "deprecation_register",
                "document_registry",
                "policy_gate_register",
                "release_state_register",
                "source_authority_register",
                "verification_backlog",
            },
            set(REGISTRY_PATHS),
        )
        self.assertEqual(
            {f"control_plane/{registry_id}.yaml" for registry_id in REGISTRY_PATHS},
            {path.relative_to(REPO_ROOT).as_posix() for path in REGISTRY_PATHS.values()},
        )

    def test_current_packet_passes(self) -> None:
        for registry_id, path in sorted(REGISTRY_PATHS.items()):
            with self.subTest(registry_id=registry_id):
                result = validate_registry(path, expected_registry_id=registry_id)
                self.assertTrue(result.ok, result.findings)

    def test_valid_fixture_passes_and_preserves_unknown_owner(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
        self.assertEqual(1, len(files))
        candidate = yaml.safe_load(files[0].read_text(encoding="utf-8"))
        self.assertEqual("UNKNOWN", candidate["owner_role"])
        result = validate_registry(files[0], check_paths=True, check_git=False)
        self.assertTrue(result.ok, result.findings)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        manifest = json.loads(
            (FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(5, len(manifest))
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_registry(
                    FIXTURE_ROOT / "invalid" / name,
                    check_paths=True,
                    check_git=False,
                )
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(expected),
                    sorted({finding.code for finding in result.findings}),
                )

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/control_plane/validate_control_plane_registry_packet.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertIn("ENTRY_ID_DUPLICATE", result.stdout)

    def test_duplicate_yaml_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text("schema_version: 1.0.0\nschema_version: 2.0.0\n", encoding="utf-8")
            result = validate_registry(path, check_paths=False, check_git=False)
        self.assertEqual(
            ["YAML_DUPLICATE_KEY"],
            sorted({finding.code for finding in result.findings}),
        )

    def test_nonfinite_yaml_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.yaml"
            path.write_text("value: .nan\n", encoding="utf-8")
            result = validate_registry(path, check_paths=False, check_git=False)
        self.assertIn(
            "YAML_NONFINITE_OR_COMPLEX",
            {finding.code for finding in result.findings},
        )

    def test_missing_declared_paths_fail_closed(self) -> None:
        fixture = FIXTURE_ROOT / "valid/valid_minimal.yaml"
        with tempfile.TemporaryDirectory() as directory:
            result = validate_registry(
                fixture,
                repo_root=Path(directory),
                check_paths=True,
                check_git=False,
            )
        self.assertIn("PATH_NOT_FOUND", {finding.code for finding in result.findings})

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-sensitive-value-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.yaml"
            path.write_text(f"unexpected: {marker}\n", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/control_plane/validate_control_plane_registry_packet.py",
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

    def test_document_registry_keeps_authority_conflict_explicit(self) -> None:
        candidate = yaml.safe_load(
            REGISTRY_PATHS["document_registry"].read_text(encoding="utf-8")
        )
        self.assertEqual("PARTIAL", candidate["implementation_status"])
        self.assertEqual("CONFLICTED", candidate["entries"][0]["authority_status"])
        self.assertIn(
            "prior_entry_claimed_confirmed",
            candidate["entries"][0]["reason_codes"],
        )


if __name__ == "__main__":
    unittest.main()
