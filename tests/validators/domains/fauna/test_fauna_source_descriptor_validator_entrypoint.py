#!/usr/bin/env python3
"""Regression proof for the Fauna SourceDescriptor validator entrypoint.

The shared SourceDescriptor schema and its structural/fail-closed behavior
are already proven exhaustively by
``tests/validators/test_validate_source_descriptor_entrypoints.py`` and the
People/DNA/Land-style entrypoint tests elsewhere in this repo. This suite
proves only what this domain adapter adds: the optional ``domain_scope``
membership check.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
import json as _json


REPO_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR = REPO_ROOT / "tools/validators/domains/fauna/validate_source_descriptor.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/fauna/source_descriptor"
VALID_FIXTURE = FIXTURE_ROOT / "valid/valid_1.json"
MISMATCH_FIXTURE = FIXTURE_ROOT / "invalid/invalid_domain_scope_mismatch.json"


class FaunaSourceDescriptorEntrypointTests(unittest.TestCase):
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
        result = self._run("--fixtures", str(MISMATCH_FIXTURE))

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("Cannot combine --fixtures with explicit files", result.stderr)

    def test_missing_arguments_is_usage_error(self) -> None:
        result = self._run()

        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertIn("No files provided", result.stderr)

    def test_in_scope_candidate_passes(self) -> None:
        result = self._run(str(VALID_FIXTURE))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"OK {VALID_FIXTURE}", result.stdout)

    def test_out_of_scope_candidate_fails_closed(self) -> None:
        result = self._run(str(MISMATCH_FIXTURE))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("domain_scope does not include", result.stdout)
        self.assertIn("'fauna'", result.stdout)

    def test_missing_domain_scope_is_not_a_failure(self) -> None:
        """domain_scope remains optional; its absence alone must not fail closed."""

        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "no-scope-declared.json"
            base = VALID_FIXTURE.read_text(encoding="utf-8")
            document = _json.loads(base)
            document.pop("domain_scope", None)
            candidate.write_text(_json.dumps(document), encoding="utf-8")
            result = self._run(str(candidate))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"OK {candidate}", result.stdout)

    def test_legacy_domain_alias_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "legacy-domain-mismatch.json"
            base = VALID_FIXTURE.read_text(encoding="utf-8")
            document = _json.loads(base)
            document.pop("domain_scope", None)
            document["domain"] = "not-a-real-domain"
            candidate.write_text(_json.dumps(document), encoding="utf-8")
            result = self._run(str(candidate))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("legacy domain", result.stdout)


if __name__ == "__main__":
    unittest.main()
