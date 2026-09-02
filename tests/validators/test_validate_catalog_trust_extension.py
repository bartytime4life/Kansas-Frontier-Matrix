"""Deterministic no-network tests for CatalogTrustExtension."""
from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT
    / "tools"
    / "validators"
    / "catalog_trust_extension"
    / "validate_catalog_trust_extension.py"
)
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "data"
    / "catalog_trust_extension.schema.json"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures" / "data" / "catalog_trust_extension"
MANIFEST_PATH = FIXTURE_ROOT / "expected_findings_manifest.json"

SPEC = importlib.util.spec_from_file_location(
    "catalog_trust_extension_under_test",
    VALIDATOR_PATH,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("catalog trust validation attempted network access")


class CatalogTrustExtensionTests(unittest.TestCase):
    def setUp(self) -> None:
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def _manifest(self) -> dict:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_schema_is_closed_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "DRAFT_SCHEMA")
        self.assertEqual(schema["x-kfm"]["source_card"], "KFM-P3-IDEA-0004")

    def test_source_role_vocabulary_is_exact(self) -> None:
        self.assertEqual(
            MODULE.SOURCE_ROLES,
            {
                "observed",
                "regulatory",
                "modeled",
                "aggregate",
                "administrative",
                "candidate",
                "synthetic",
            },
        )

    def test_manifest_inventory_is_exact(self) -> None:
        manifest = self._manifest()
        declared = {case["path"] for case in manifest["cases"]}
        discovered = {
            path.relative_to(FIXTURE_ROOT).as_posix()
            for directory in ("valid", "invalid")
            for path in (FIXTURE_ROOT / directory).glob("*.json")
        }
        self.assertEqual(declared, discovered)
        self.assertEqual(
            len([path for path in declared if path.startswith("valid/")]),
            4,
        )
        self.assertEqual(
            len([path for path in declared if path.startswith("invalid/")]),
            7,
        )

    def test_fixture_cases_match_exact_outcomes_and_findings(self) -> None:
        for case in self._manifest()["cases"]:
            with self.subTest(path=case["path"]):
                result = MODULE.validate_record(FIXTURE_ROOT / case["path"])
                actual = [
                    {"code": finding.code, "field": finding.field}
                    for finding in result.findings
                ]
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(actual, case["expected_findings"])

    def test_fixture_cli_replays_exact_profile(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            completed.returncode,
            0,
            completed.stdout + completed.stderr,
        )
        self.assertNotIn(
            "FIXTURE_POLARITY_ERROR",
            completed.stdout + completed.stderr,
        )
        self.assertEqual(completed.stdout.count('"outcome":"PASS"'), 4)
        self.assertEqual(completed.stdout.count('"outcome":"FAIL"'), 7)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"CatalogTrustExtension",'
                '"object_type":"CatalogTrustExtension"}',
                encoding="utf-8",
            )
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"JSON_DUPLICATE_KEY"},
        )

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"JSON_NONFINITE_NUMBER"},
        )

    def test_oversized_file_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "oversized.json"
            path.write_bytes(b" " * (MODULE.MAX_FILE_BYTES + 1))
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"FILE_TOO_LARGE"},
        )

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(REPO_ROOT / "does-not-exist.json")
        self.assertTrue(result.error)
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"FILE_NOT_FOUND"},
        )

    def test_spec_hash_is_key_order_independent(self) -> None:
        payload = json.loads(
            (
                FIXTURE_ROOT
                / "valid"
                / "valid_stac_receipt.json"
            ).read_text(encoding="utf-8")
        )
        subject = dict(payload)
        subject.pop("spec_hash")
        forward = MODULE.compute_spec_hash(subject)
        reverse = MODULE.compute_spec_hash(
            dict(reversed(list(subject.items())))
        )
        self.assertEqual(forward, reverse)
        self.assertEqual(payload["spec_hash"], forward)

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        payload = json.loads(
            (
                FIXTURE_ROOT
                / "valid"
                / "valid_stac_receipt.json"
            ).read_text(encoding="utf-8")
        )
        canary = "UNTRUSTED_VALUE_DO_NOT_ECHO"
        payload[canary] = canary
        subject = dict(payload)
        subject.pop("spec_hash")
        payload["spec_hash"] = MODULE.compute_spec_hash(subject)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            report = MODULE._serialize(
                path,
                MODULE.validate_record(path),
            )
        self.assertNotIn(canary, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_replay_is_deterministic_and_no_network(self) -> None:
        path = FIXTURE_ROOT / "valid" / "valid_prov_proof.json"
        first = MODULE._serialize(path, MODULE.validate_record(path))
        second = MODULE._serialize(path, MODULE.validate_record(path))
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
