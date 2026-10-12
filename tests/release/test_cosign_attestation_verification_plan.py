from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.release.validate_cosign_attestation_verification_plan import (
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_PATH,
    validate_plan,
)


class CosignAttestationVerificationPlanTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_valid_fixtures_pass(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertGreaterEqual(len(files), 2)
        for path in files:
            with self.subTest(path=path.name):
                result = validate_plan(path)
                self.assertTrue(result.ok, result.findings)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        lane = FIXTURE_ROOT / "invalid"
        manifest = json.loads(
            (lane / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
        files = sorted(lane.glob("invalid_*.json")) + sorted(
            lane.glob("semantic_invalid_*.json")
        )
        self.assertGreaterEqual(len(files), 12)
        self.assertEqual({path.name for path in files}, set(manifest))
        for path in files:
            with self.subTest(path=path.name):
                result = validate_plan(path)
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(set(manifest[path.name])),
                    sorted({item.code for item in result.findings}),
                )

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/release/validate_cosign_attestation_verification_plan.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertNotIn("synthetic-secret-must-not-echo", result.stdout)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"CosignAttestationVerificationPlan",'
                '"object_type":"synthetic-secret-must-not-echo"}',
                encoding="utf-8",
            )
            result = validate_plan(path)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({item.code for item in result.findings}),
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_plan(path)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({item.code for item in result.findings}),
        )

    def test_missing_file_fails_closed(self) -> None:
        result = validate_plan(Path("does-not-exist-cosign-plan.json"))
        self.assertEqual(
            ["FILE_NOT_FOUND"],
            sorted({item.code for item in result.findings}),
        )

    def test_symlink_input_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.json"
            link = root / "link.json"
            target.write_text("{}", encoding="utf-8")
            try:
                link.symlink_to(target)
            except OSError:
                self.skipTest("symlinks are unavailable")
            result = validate_plan(link)
        self.assertEqual(
            ["INPUT_SYMLINK_DENIED"],
            sorted({item.code for item in result.findings}),
        )

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "secret.json"
            path.write_text(
                json.dumps(
                    {
                        "object_type": "CosignAttestationVerificationPlan",
                        "unexpected": "synthetic-secret-must-not-echo",
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/release/validate_cosign_attestation_verification_plan.py",
                    str(path),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertNotIn("synthetic-secret-must-not-echo", result.stdout)
        self.assertIn("SCHEMA_INVALID", result.stdout)

    def test_validator_has_no_network_or_cosign_execution_surface(self) -> None:
        source = (
            REPO_ROOT
            / "tools/validators/release/validate_cosign_attestation_verification_plan.py"
        ).read_text(encoding="utf-8")
        for forbidden in (
            "import requests",
            "import urllib",
            "import socket",
            "import subprocess",
            "subprocess.run",
            "os.system",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
