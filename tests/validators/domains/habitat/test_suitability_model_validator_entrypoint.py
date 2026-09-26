#!/usr/bin/env python3
"""Regression proof for the SuitabilityModel validator entrypoint.

SuitabilityModel has no field-level schema yet (see
``fixtures/domains/habitat/suitability_model/README.md``); this suite proves
only the structural properties the current scaffold and shared JSON Schema
runner actually enforce, plus the one additional, well-grounded rule the
validator adds: optional ``model_card_ref`` linkage to the real,
already-implemented governance ModelCardEnvelope validator. It does not
assert any other SuitabilityModel field name, model-card topic, or enum
value as settled shape.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR = REPO_ROOT / "tools/validators/domains/habitat/validate_suitability_model.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/habitat/suitability_model"
VALID_FIXTURE = FIXTURE_ROOT / "valid/valid_1.json"
INVALID_FIXTURE = FIXTURE_ROOT / "invalid/invalid_root_not_object.json"


class SuitabilityModelEntrypointTests(unittest.TestCase):
    """Prove shared fixture polarity and fail-closed argument/JSON handling."""

    def _run(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            return subprocess.run(
                [sys.executable, str(VALIDATOR), *arguments],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )

    def test_shared_fixture_profile_preserves_positive_and_negative_polarity(self) -> None:
        result = self._run("--fixtures")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)
        self.assertIn("EXPECTED_FAIL ", result.stdout)

    def test_fixture_profile_cannot_ignore_an_explicit_file(self) -> None:
        result = self._run("--fixtures", str(INVALID_FIXTURE))

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("Cannot combine --fixtures with explicit files", result.stderr)

    def test_explicit_valid_file_passes_from_unrelated_working_directory(self) -> None:
        result = self._run(str(VALID_FIXTURE))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"OK {VALID_FIXTURE}", result.stdout)

    def test_explicit_invalid_file_fails_from_unrelated_working_directory(self) -> None:
        result = self._run(str(INVALID_FIXTURE))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"FAIL {INVALID_FIXTURE}", result.stdout)

    def test_missing_arguments_is_usage_error(self) -> None:
        result = self._run()

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("No files provided", result.stderr)

    def test_missing_explicit_file_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing-suitability-model.json"
            result = self._run(str(missing))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"FAIL {missing}", result.stdout)

    def test_duplicate_keys_and_nonfinite_numbers_fail_before_schema_validation(self) -> None:
        malformed_instances = {
            "duplicate-key.json": '{"note":"first","note":"second"}',
            "nonfinite-number.json": '{"value":NaN}',
        }

        with tempfile.TemporaryDirectory() as directory:
            fixture_root = Path(directory)
            for name, fixture_content in malformed_instances.items():
                with self.subTest(name=name):
                    path = fixture_root / name
                    path.write_text(fixture_content, encoding="utf-8")
                    result = self._run(str(path))

                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertIn(f"FAIL {path}", result.stdout)

    def test_arbitrary_well_formed_object_passes_the_permissive_scaffold(self) -> None:
        """The scaffold has no field constraints, so any JSON object is accepted."""

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "arbitrary-object.json"
            path.write_text('{"anything": ["is", "accepted", 1, true, null]}', encoding="utf-8")
            result = self._run(str(path))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"OK {path}", result.stdout)

    def test_model_card_ref_is_optional(self) -> None:
        """A candidate with no model_card_ref at all is unaffected by the linkage check."""

        result = self._run(str(FIXTURE_ROOT / "valid/valid_1.json"))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_model_card_ref_pointing_at_a_passing_envelope_passes(self) -> None:
        result = self._run(str(FIXTURE_ROOT / "valid/valid_3.json"))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_model_card_ref_pointing_at_a_failing_envelope_fails_closed(self) -> None:
        path = FIXTURE_ROOT / "invalid/invalid_model_card_ref_fails.json"
        result = self._run(str(path))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("ModelCardEnvelope validation", result.stdout)
        self.assertIn("SPEC_HASH_MISMATCH", result.stdout)

    def test_model_card_ref_pointing_at_a_missing_file_fails_closed(self) -> None:
        path = FIXTURE_ROOT / "invalid/invalid_model_card_ref_missing.json"
        result = self._run(str(path))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("does not resolve to a regular file", result.stdout)

    def test_model_card_ref_with_wrong_type_fails_closed(self) -> None:
        path = FIXTURE_ROOT / "invalid/invalid_model_card_ref_wrong_type.json"
        result = self._run(str(path))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("must be a non-empty string path", result.stdout)

    def test_model_card_ref_rejects_symlinked_target(self) -> None:
        target = FIXTURE_ROOT / "support/model_card_pass.json"

        with tempfile.TemporaryDirectory() as directory:
            link = Path(directory) / "linked.json"
            link.symlink_to(target)
            candidate = Path(directory) / "candidate.json"
            candidate.write_text(
                f'{{"model_card_ref": "{link}"}}',
                encoding="utf-8",
            )
            result = self._run(str(candidate))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("does not resolve to a regular file", result.stdout)


if __name__ == "__main__":
    unittest.main()
