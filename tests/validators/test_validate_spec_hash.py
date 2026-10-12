"""Deterministic tests for the common KFM spec-hash implementation."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(PACKAGE_SRC))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    canonicalize_json,
    compute_spec_hash,
    load_json_file,
    verify_spec_hash,
)
from tools.validators.validate_spec_hash import (  # noqa: E402
    FIXTURE_ROOT,
    Finding,
    validate_document,
    validate_file,
    validate_fixture_tree,
)


class SpecHashTests(unittest.TestCase):
    def test_canonical_bytes_are_key_order_invariant(self) -> None:
        left = {"b": 1, "a": [True, None, "x"]}
        right = {"a": [True, None, "x"], "b": 1}
        expected = b'{"a":[true,null,"x"],"b":1}'
        self.assertEqual(canonicalize_json(left), expected)
        self.assertEqual(canonicalize_json(left), canonicalize_json(right))
        self.assertEqual(compute_spec_hash(left), compute_spec_hash(right))

    def test_hash_matches_sha256_of_rfc8785_bytes(self) -> None:
        subject = {"b": 1, "a": 2}
        canonical = b'{"a":2,"b":1}'
        expected = "sha256:" + hashlib.sha256(canonical).hexdigest()
        self.assertEqual(canonicalize_json(subject), canonical)
        self.assertEqual(compute_spec_hash(subject), expected)
        self.assertTrue(verify_spec_hash(subject, expected).matches)

    def test_existing_fixture_matrix_has_exact_polarity(self) -> None:
        self.assertEqual(validate_fixture_tree(), ())
        for path in sorted((FIXTURE_ROOT / "valid").glob("*.json")):
            with self.subTest(path=path):
                self.assertTrue(validate_file(path).ok)
        for path in sorted((FIXTURE_ROOT / "invalid").glob("*.json")):
            with self.subTest(path=path):
                self.assertFalse(validate_file(path).ok)

    def test_subject_recomputation_detects_match_and_mismatch(self) -> None:
        subject = {"name": "kfm", "version": 1}
        expected = compute_spec_hash(subject)
        matching = validate_document({"value": expected}, subject=subject)
        self.assertTrue(matching.ok, matching.findings)
        self.assertEqual(matching.expected, expected)
        self.assertEqual(matching.actual, expected)

        mismatching = validate_document(
            {"value": "sha256:" + "a" * 64}, subject=subject
        )
        self.assertIn(Finding("SPEC_HASH_MISMATCH", "/value"), mismatching.findings)
        self.assertEqual(mismatching.outcome, "DENY")

    def test_input_is_not_mutated(self) -> None:
        subject = {"nested": [{"value": 1.0}]}
        snapshot = copy.deepcopy(subject)
        compute_spec_hash(subject)
        self.assertEqual(subject, snapshot)

    def test_unsafe_integer_fails_canonicalization(self) -> None:
        with self.assertRaises(CanonicalizationFailure):
            compute_spec_hash({"too_large": 2**53})

    def test_duplicate_json_keys_fail_safely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"a":1,"a":2}', encoding="utf-8")
            with self.assertRaises(JsonInputError):
                load_json_file(path)

    def test_nonfinite_json_numbers_fail_safely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            with self.assertRaises(JsonInputError):
                load_json_file(path)

    def test_cli_compute_and_verify_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subject_path = root / "subject.json"
            subject_path.write_text('{"b":1,"a":2}\n', encoding="utf-8")
            expected = compute_spec_hash({"a": 2, "b": 1})
            hash_path = root / "hash.json"
            hash_path.write_text(
                json.dumps({"value": expected}) + "\n", encoding="utf-8"
            )

            compute_cmd = [
                sys.executable,
                str(REPO_ROOT / "tools/spec_hash/spec_hash.py"),
                "compute",
                str(subject_path),
            ]
            first = subprocess.run(compute_cmd, check=False, capture_output=True, text=True)
            second = subprocess.run(compute_cmd, check=False, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(first.stdout, second.stdout)
            self.assertEqual(json.loads(first.stdout)["spec_hash"], expected)

            verify = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "tools/spec_hash/spec_hash.py"),
                    "verify",
                    str(subject_path),
                    str(hash_path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(verify.returncode, 0, verify.stderr)
            self.assertEqual(json.loads(verify.stdout)["status"], "SPEC_HASH_MATCH")

    def test_validator_cli_fixture_suite(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "tools/validators/validate_spec_hash.py"),
                "--fixtures",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["findings"], [])


if __name__ == "__main__":
    unittest.main()
