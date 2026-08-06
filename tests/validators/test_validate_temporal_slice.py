from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_temporal_slice.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/data/temporal_slice"
VALID_ROOT = FIXTURE_ROOT / "valid"
INVALID_ROOT = FIXTURE_ROOT / "invalid"
MANIFEST_PATH = INVALID_ROOT / "expected_findings_manifest.json"

SPEC = importlib.util.spec_from_file_location("validate_temporal_slice", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"{path.name} must contain a JSON object")
    return value


class TemporalSliceTests(unittest.TestCase):
    def test_fixture_inventory_is_exact(self) -> None:
        self.assertEqual(
            ["valid_baseline_slice.json", "valid_changed_slice.json"],
            sorted(path.name for path in VALID_ROOT.glob("*.json")),
        )
        self.assertEqual(
            [
                "expected_findings_manifest.json",
                "invalid_missing_evidence_bundle.json",
                "semantic_invalid_catalog_without_gate.json",
                "semantic_invalid_change_without_previous.json",
                "semantic_invalid_changed_without_support.json",
                "semantic_invalid_refs_not_canonical.json",
                "semantic_invalid_self_previous.json",
                "semantic_invalid_slice_id.json",
                "semantic_invalid_temporal_order.json",
            ],
            sorted(path.name for path in INVALID_ROOT.glob("*.json")),
        )

    def test_valid_fixtures_pass(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                self.assertTrue(validator.validate_slice(path).ok)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        expected = load_json(MANIFEST_PATH)
        invalid_paths = sorted(
            path
            for path in INVALID_ROOT.glob("*.json")
            if path.name != MANIFEST_PATH.name
        )
        self.assertEqual(sorted(expected), [path.name for path in invalid_paths])
        for path in invalid_paths:
            with self.subTest(path=path.name):
                result = validator.validate_slice(path)
                actual = sorted({finding.code for finding in result.findings})
                self.assertEqual(expected[path.name], actual)

    def test_schema_and_semantic_negative_lanes_are_explicit(self) -> None:
        schema_invalid = INVALID_ROOT / "invalid_missing_evidence_bundle.json"
        schema_validator = validator._schema_validator()
        self.assertNotEqual(
            [],
            validator._schema_findings(schema_validator, load_json(schema_invalid)),
        )
        for path in sorted(INVALID_ROOT.glob("semantic_invalid_*.json")):
            with self.subTest(path=path.name):
                self.assertEqual(
                    [],
                    validator._schema_findings(schema_validator, load_json(path)),
                )

    def test_fixture_entrypoint_passes(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.assertEqual(0, validator.validate_fixtures())
        self.assertIn(
            "CONFIRMED: 2 valid and 8 invalid TemporalSlice fixtures passed exact polarity.",
            stdout.getvalue(),
        )

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"TemporalSlice","object_type":"other"}',
                encoding="utf-8",
            )
            result = validator.validate_slice(path)
            self.assertIn(
                "JSON_DUPLICATE_KEY",
                {finding.code for finding in result.findings},
            )
            self.assertTrue(result.error)

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"delta":NaN}', encoding="utf-8")
            result = validator.validate_slice(path)
            self.assertIn(
                "JSON_NONFINITE_NUMBER",
                {finding.code for finding in result.findings},
            )
            self.assertTrue(result.error)

    def test_cli_does_not_echo_candidate_values(self) -> None:
        marker = "UNIQUE_TEMPORAL_SLICE_ECHO_SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps({"marker": marker}), encoding="utf-8")
            run = subprocess.run(
                [sys.executable, str(MODULE_PATH), str(path)],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(0, run.returncode)
            self.assertNotIn(marker, run.stdout)
            self.assertNotIn(marker, run.stderr)

    def test_identity_is_deterministic(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                candidate = load_json(path)
                expected = validator.canonical_slice_id(candidate)
                self.assertEqual(candidate["slice_id"], expected)
                self.assertEqual(expected, validator.canonical_slice_id(candidate))

    def test_validation_performs_no_network_access(self) -> None:
        with mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network access is forbidden"),
        ):
            for path in sorted(VALID_ROOT.glob("*.json")):
                with self.subTest(path=path.name):
                    self.assertTrue(validator.validate_slice(path).ok)


if __name__ == "__main__":
    unittest.main()
