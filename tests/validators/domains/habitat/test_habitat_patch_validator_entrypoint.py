#!/usr/bin/env python3
"""Regression proof for the HabitatPatch validator entrypoint.

HabitatPatch has no field-level schema yet (see
``fixtures/domains/habitat/patch/README.md``); this suite proves the
structural properties the current scaffold and shared JSON Schema runner
actually enforce, plus the one additional rule the validator adds:
reference-string hygiene (sorted, unique, grammar-bounded, no
internal-lifecycle prefixes) on the optional ``connectivity_edge_refs`` and
``corridor_refs`` fields. It does not assert any other HabitatPatch field
name, source role, or enum value as settled shape, and it never resolves
those references to a real ConnectivityEdge or Corridor object.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR = REPO_ROOT / "tools/validators/domains/habitat/validate_habitat_patch.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/habitat/patch"
VALID_FIXTURE = FIXTURE_ROOT / "valid/valid_1.json"
INVALID_FIXTURE = FIXTURE_ROOT / "invalid/invalid_root_not_object.json"


class HabitatPatchEntrypointTests(unittest.TestCase):
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
            missing = Path(directory) / "missing-habitat-patch.json"
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

    def test_connectivity_refs_are_optional(self) -> None:
        """A candidate with neither connectivity field is unaffected by the hygiene check."""

        result = self._run(str(FIXTURE_ROOT / "valid/valid_1.json"))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_well_formed_connectivity_refs_pass(self) -> None:
        result = self._run(str(FIXTURE_ROOT / "valid/valid_3.json"))

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unsorted_or_duplicate_connectivity_edge_refs_fail_closed(self) -> None:
        path = FIXTURE_ROOT / "invalid/invalid_connectivity_edge_refs_unsorted.json"
        result = self._run(str(path))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("must be sorted and unique", result.stdout)

    def test_internal_lifecycle_prefix_in_corridor_refs_fails_closed(self) -> None:
        path = FIXTURE_ROOT / "invalid/invalid_corridor_refs_internal_prefix.json"
        result = self._run(str(path))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("lifecycle-private reference", result.stdout)

    def test_ungrammatical_connectivity_edge_ref_fails_closed(self) -> None:
        path = FIXTURE_ROOT / "invalid/invalid_connectivity_edge_refs_bad_grammar.json"
        result = self._run(str(path))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("violates the bounded grammar", result.stdout)

    def test_empty_connectivity_ref_array_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "empty-connectivity-edge-refs.json"
            candidate.write_text('{"connectivity_edge_refs": []}', encoding="utf-8")
            result = self._run(str(candidate))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("must be a non-empty array of strings", result.stdout)

    def test_non_string_connectivity_ref_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "non-string-corridor-refs.json"
            candidate.write_text('{"corridor_refs": [1, 2]}', encoding="utf-8")
            result = self._run(str(candidate))

        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("must be a non-empty array of strings", result.stdout)


if __name__ == "__main__":
    unittest.main()
