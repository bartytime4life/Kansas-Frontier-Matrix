from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_trace_receipt_link.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/telemetry/trace_receipt_link"
VALID_ROOT = FIXTURE_ROOT / "valid"
INVALID_ROOT = FIXTURE_ROOT / "invalid"
MANIFEST_PATH = INVALID_ROOT / "expected_findings_manifest.json"

SPEC = importlib.util.spec_from_file_location("validate_trace_receipt_link", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"{path.name} must contain a JSON object")
    return value


class TraceReceiptLinkTests(unittest.TestCase):
    def test_fixture_inventory_is_exact(self) -> None:
        self.assertEqual(
            ["valid_linked.json", "valid_linked_restricted.json"],
            sorted(path.name for path in VALID_ROOT.glob("*.json")),
        )
        expected = load_json(MANIFEST_PATH)
        self.assertEqual(
            sorted(expected),
            sorted(
                path.name
                for path in INVALID_ROOT.glob("*.json")
                if path.name != MANIFEST_PATH.name
            ),
        )

    def test_valid_fixtures_pass(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                self.assertTrue(validator.validate_link(path).ok)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        expected = load_json(MANIFEST_PATH)
        for path in sorted(
            item for item in INVALID_ROOT.glob("*.json") if item.name != MANIFEST_PATH.name
        ):
            with self.subTest(path=path.name):
                result = validator.validate_link(path)
                actual = sorted({finding.code for finding in result.findings})
                self.assertEqual(expected[path.name], actual)

    def test_semantic_negative_vectors_remain_schema_valid(self) -> None:
        for path in sorted(INVALID_ROOT.glob("semantic_invalid_*.json")):
            with self.subTest(path=path.name):
                self.assertEqual([], validator._schema_findings(load_json(path)))

    def test_schema_negative_vector_fails_shape_before_semantics(self) -> None:
        path = INVALID_ROOT / "schema_invalid_missing_evidence_digest.json"
        result = validator.validate_link(path)
        self.assertEqual(["SCHEMA_INVALID"], sorted({item.code for item in result.findings}))

    def test_fixture_entrypoint_passes(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.assertEqual(0, validator.validate_fixtures())
        self.assertIn(
            "CONFIRMED: 2 valid and 13 invalid trace receipt link fixtures passed exact polarity.",
            stdout.getvalue(),
        )

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"object_type":"TraceReceiptLink","object_type":"other"}', encoding="utf-8")
            result = validator.validate_link(path)
            self.assertIn("JSON_DUPLICATE_KEY", {finding.code for finding in result.findings})
            self.assertTrue(result.error)

    def test_cli_does_not_echo_candidate_values(self) -> None:
        marker = "TRACE_LINK_PRIVATE_VALUE_SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps({"private_url": marker}), encoding="utf-8")
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

    def test_link_identity_is_deterministic(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            with self.subTest(path=path.name):
                candidate = load_json(path)
                expected = validator.canonical_link_id(candidate)
                self.assertEqual(candidate["link_id"], expected)
                self.assertEqual(expected, validator.canonical_link_id(candidate))

    def test_delay_values_are_derived_from_timestamps(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            candidate = load_json(path)
            run = candidate["run_anchor"]
            receipt = candidate["run_receipt"]
            evidence = candidate["evidence_bundle"]
            assessment = candidate["assessment"]
            start = validator._time(run["started_at"])
            receipt_time = validator._time(receipt["emitted_at"])
            evidence_time = validator._time(evidence["recorded_at"])
            assert start and receipt_time and evidence_time
            self.assertEqual(
                assessment["receipt_delay_seconds"],
                int((receipt_time - start).total_seconds()),
            )
            self.assertEqual(
                assessment["evidence_delay_seconds"],
                int((evidence_time - start).total_seconds()),
            )

    def test_valid_records_create_no_authority(self) -> None:
        for path in sorted(VALID_ROOT.glob("*.json")):
            governance = load_json(path)["governance"]
            self.assertTrue(all(value is False for value in governance.values()))

    def test_validator_has_no_network_client_surface(self) -> None:
        source = MODULE_PATH.read_text(encoding="utf-8")
        self.assertNotIn("import requests", source)
        self.assertNotIn("import urllib", source)
        self.assertNotIn("import socket", source)
        self.assertNotIn("urlopen(", source)
        self.assertNotIn("requests.", source)

    def test_cli_accepts_valid_and_rejects_invalid(self) -> None:
        valid = subprocess.run(
            [sys.executable, str(MODULE_PATH), str(VALID_ROOT / "valid_linked.json")],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        invalid = subprocess.run(
            [sys.executable, str(MODULE_PATH), str(INVALID_ROOT / "semantic_invalid_trace_mismatch.json")],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, valid.returncode)
        self.assertNotEqual(0, invalid.returncode)
        self.assertIn('"outcome":"PASS"', valid.stdout)
        self.assertIn('"outcome":"FAIL"', invalid.stdout)


if __name__ == "__main__":
    unittest.main()
