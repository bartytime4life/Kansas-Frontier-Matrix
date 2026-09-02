from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.directory_governance.validate_root_registry import (
    ADOPTED_DOCTRINE_SHA256,
    CANONICAL_ROOTS,
    FIXTURE_ROOT,
    REGISTER_PATH,
    REPO_ROOT,
    SCHEMA_PATH,
    resolve_registry,
    validate_register,
)


class RootRegistryValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def _valid_fixture(self) -> dict:
        path = FIXTURE_ROOT / "valid" / "root_classes.yaml"
        return json.loads(path.read_text(encoding="utf-8"))

    def _validate_payload(self, payload: dict):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.yaml"
            path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
            return validate_register(path, check_repo_roots=False, enforce_doctrine_parity=False)

    def test_valid_root_class_fixture_passes(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
        self.assertEqual(1, len(files))
        result = validate_register(files[0], check_repo_roots=False, enforce_doctrine_parity=False)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("PASS", result.outcome)

    def test_reviewed_invalid_fixture_fails_as_expected(self) -> None:
        manifest = json.loads((FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual({"canonical_not_active.yaml": ["ACTIVE_ROOT_STATUS_INVALID"]}, manifest)
        result = validate_register(
            FIXTURE_ROOT / "invalid" / "canonical_not_active.yaml",
            check_repo_roots=False,
            enforce_doctrine_parity=False,
        )
        self.assertFalse(result.ok)
        self.assertEqual(["ACTIVE_ROOT_STATUS_INVALID"], sorted({item.code for item in result.findings}))

    def test_root_class_invariants_fail_closed(self) -> None:
        cases = []
        candidate = self._valid_fixture()
        candidate["roots"][2].pop("canonical_target")
        cases.append((candidate, "CANONICAL_TARGET_REQUIRED"))

        candidate = self._valid_fixture()
        candidate["roots"][3]["validation_profiles"] = ["synthetic_fixture"]
        cases.append((candidate, "FROZEN_WRITE_PROFILE_REQUIRED"))

        candidate = self._valid_fixture()
        candidate["doctrine"]["sha256"] = "sha256:" + "0" * 64
        cases.append((candidate, "DOCTRINE_DIGEST_MISMATCH"))

        candidate = self._valid_fixture()
        candidate["roots"][1]["path"] = candidate["roots"][0]["path"]
        cases.append((candidate, "ROOT_PATH_DUPLICATE"))

        for payload, expected in cases:
            with self.subTest(expected=expected):
                result = self._validate_payload(payload)
                self.assertFalse(result.ok)
                self.assertIn(expected, {item.code for item in result.findings})

    def test_current_register_projects_exact_adopted_digest(self) -> None:
        register = resolve_registry(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
        expected = f"sha256:{ADOPTED_DOCTRINE_SHA256}"
        self.assertEqual(expected, register["doctrine"]["sha256"])
        self.assertTrue(all(entry["source_digest"] == expected for entry in register["roots"]))

    def test_current_register_contains_every_adopted_canonical_root(self) -> None:
        register = resolve_registry(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
        by_path = {entry["path"]: entry for entry in register["roots"]}
        self.assertTrue(set(CANONICAL_ROOTS).issubset(by_path))
        self.assertEqual("platform", by_path[".github/"]["class"])
        for path in CANONICAL_ROOTS:
            if path != ".github/":
                self.assertEqual("canonical", by_path[path]["class"])

    def test_current_register_passes_against_projected_root_tree(self) -> None:
        register = resolve_registry(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
        with tempfile.TemporaryDirectory() as directory:
            projected = Path(directory)
            for entry in register["roots"]:
                if entry["status"] != "RETIRED":
                    (projected / entry["path"]).mkdir(parents=True, exist_ok=True)
            result = validate_register(REGISTER_PATH, repo_root=projected)
        self.assertTrue(result.ok, result.findings)

    def test_unregistered_observed_root_is_new_drift(self) -> None:
        register = resolve_registry(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
        with tempfile.TemporaryDirectory() as directory:
            projected = Path(directory)
            for entry in register["roots"]:
                if entry["status"] != "RETIRED":
                    (projected / entry["path"]).mkdir(parents=True, exist_ok=True)
            (projected / "unregistered-domain-root").mkdir()
            result = validate_register(REGISTER_PATH, repo_root=projected)
        self.assertEqual("FAIL_NEW_DRIFT", result.outcome)
        self.assertIn("UNREGISTERED_ROOT", {item.code for item in result.findings})

    def test_missing_active_root_is_new_drift(self) -> None:
        register = resolve_registry(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
        with tempfile.TemporaryDirectory() as directory:
            projected = Path(directory)
            for entry in register["roots"]:
                if entry["status"] != "RETIRED" and entry["path"] != "contracts/":
                    (projected / entry["path"]).mkdir(parents=True, exist_ok=True)
            result = validate_register(REGISTER_PATH, repo_root=projected)
        self.assertEqual("FAIL_NEW_DRIFT", result.outcome)
        self.assertIn("REGISTERED_ACTIVE_ROOT_MISSING", {item.code for item in result.findings})

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "tools/validators/directory_governance/validate_root_registry.py", "--fixtures"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)

    def test_duplicate_keys_fail_closed_as_validator_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text('{"version":"v1","version":"v2"}', encoding="utf-8")
            result = validate_register(path, check_repo_roots=False, enforce_doctrine_parity=False)
        self.assertEqual("ERROR_VALIDATOR", result.outcome)
        self.assertEqual(["JSON_DUPLICATE_KEY"], sorted({item.code for item in result.findings}))

    def test_nonfinite_numbers_fail_closed_as_validator_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.yaml"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_register(path, check_repo_roots=False, enforce_doctrine_parity=False)
        self.assertEqual("ERROR_VALIDATOR", result.outcome)
        self.assertEqual(["JSON_NONFINITE_NUMBER"], sorted({item.code for item in result.findings}))

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-secret-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.yaml"
            path.write_text(json.dumps({"unexpected": marker}), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/directory_governance/validate_root_registry.py",
                    str(path),
                    "--skip-repo-roots",
                    "--skip-doctrine-parity",
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
