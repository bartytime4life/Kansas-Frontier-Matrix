from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.directory_governance.validate_path_decision_record import (
    FIXTURE_ROOT,
    REGISTER_PATH,
    REPO_ROOT,
    SCHEMA_PATH,
    validate_record,
)


class PathDecisionRecordValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_all_finite_outcome_fixtures_pass(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
        self.assertEqual(6, len(files))
        semantic_outcomes = set()
        for path in files:
            with self.subTest(path=path.name):
                candidate = json.loads(path.read_text(encoding="utf-8"))
                semantic_outcomes.add(candidate["outcome"])
                result = validate_record(path)
                self.assertTrue(result.ok, result.findings)
                self.assertEqual("PASS", result.outcome)
        self.assertEqual({"PLACE", "SPLIT", "MIGRATE", "MIRROR", "HOLD", "DENY"}, semantic_outcomes)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        manifest = json.loads((FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(6, len(manifest))
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_record(FIXTURE_ROOT / "invalid" / name)
                self.assertFalse(result.ok)
                self.assertEqual(sorted(expected), sorted({finding.code for finding in result.findings}))

    def test_valid_fixtures_bind_current_root_registry_digest(self) -> None:
        digest = "sha256:" + hashlib.sha256(REGISTER_PATH.read_bytes()).hexdigest()
        for path in sorted((FIXTURE_ROOT / "valid").glob("*.yaml")):
            with self.subTest(path=path.name):
                candidate = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(digest, candidate["registry"]["digest"])

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "tools/validators/directory_governance/validate_path_decision_record.py", "--fixtures"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(12, sum(1 for line in result.stdout.splitlines() if line.strip()))
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertIn('"outcome":"FAIL_INVARIANT"', result.stdout)

    def test_cli_valid_record_emits_non_authoritative_boundary(self) -> None:
        path = FIXTURE_ROOT / "valid" / "place_contract.yaml"
        result = subprocess.run(
            [sys.executable, "tools/validators/directory_governance/validate_path_decision_record.py", str(path)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual("PASS", payload["outcome"])
        self.assertEqual(
            {
                "accepts_adr": False,
                "authorizes_path": False,
                "grants_writes": False,
                "moves_bytes": False,
                "publishes": False,
                "releases": False,
            },
            payload["authority"],
        )

    def test_cli_invariant_failure_returns_one(self) -> None:
        path = FIXTURE_ROOT / "invalid" / "place_public_raw.yaml"
        result = subprocess.run(
            [sys.executable, "tools/validators/directory_governance/validate_path_decision_record.py", str(path)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertEqual("FAIL_INVARIANT", json.loads(result.stdout)["outcome"])

    def test_duplicate_keys_fail_closed_as_validator_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text('{"version":"v1","version":"v2"}', encoding="utf-8")
            result = validate_record(path)
        self.assertEqual("ERROR_VALIDATOR", result.outcome)
        self.assertEqual(["JSON_DUPLICATE_KEY"], sorted({finding.code for finding in result.findings}))

    def test_nonfinite_numbers_fail_closed_as_validator_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.yaml"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_record(path)
        self.assertEqual("ERROR_VALIDATOR", result.outcome)
        self.assertEqual(["JSON_NONFINITE_NUMBER"], sorted({finding.code for finding in result.findings}))

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-secret-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.yaml"
            path.write_text(json.dumps({"unexpected": marker}), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "tools/validators/directory_governance/validate_path_decision_record.py", str(path)],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertNotIn(marker, result.stdout + result.stderr)
        self.assertIn("SCHEMA_INVALID", result.stdout)

    def test_registry_digest_mismatch_is_not_parser_error(self) -> None:
        result = validate_record(FIXTURE_ROOT / "invalid" / "registry_digest_mismatch.yaml")
        self.assertEqual("FAIL_INVARIANT", result.outcome)
        self.assertEqual(["REGISTRY_DIGEST_MISMATCH"], sorted({finding.code for finding in result.findings}))

    def test_place_cannot_use_compatibility_root_for_trust_authority(self) -> None:
        result = validate_record(FIXTURE_ROOT / "invalid" / "place_in_artifacts_trust.yaml")
        codes = {finding.code for finding in result.findings}
        self.assertIn("ARTIFACTS_TRUST_AUTHORITY_DENIED", codes)
        self.assertIn("TARGET_ROOT_NOT_WRITABLE_CANONICAL", codes)


if __name__ == "__main__":
    unittest.main()
