from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validators/stac/validate_kfm_profile_v1.py"
SCHEMA_PATH = ROOT / "schemas/contracts/v1/stac/kfm-profile-v1.schema.json"
FIXTURE_ROOT = ROOT / "fixtures/contracts/v1/stac/kfm-profile-v1"
MANIFEST_PATH = FIXTURE_ROOT / "fixture_manifest.json"

SPEC = importlib.util.spec_from_file_location("kfm_stac_profile_under_test", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class KfmStacTrustProfileTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertEqual(schema["x-kfm"]["status"], "DRAFT_SCHEMA")
        self.assertEqual(
            schema["x-kfm"]["authority"],
            "catalog_trust_projection_only",
        )

    def test_valid_fixtures_pass_exact_profile(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        paths = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
        self.assertEqual(len(paths), 3)
        self.assertEqual(set(manifest["valid"]), {path.name for path in paths})
        for path in paths:
            with self.subTest(path=path.name):
                result = MODULE.validate_record(path)
                self.assertEqual(result.outcome, "PASS")
                self.assertEqual(result.findings, ())

    def test_invalid_fixtures_match_exact_codes(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        paths = sorted((FIXTURE_ROOT / "invalid").glob("*.json"))
        self.assertEqual(len(paths), 6)
        self.assertEqual(set(manifest["invalid"]), {path.name for path in paths})
        for path in paths:
            with self.subTest(path=path.name):
                result = MODULE.validate_record(path)
                actual = sorted({finding.code for finding in result.findings})
                self.assertEqual(result.outcome, manifest["invalid"][path.name]["outcome"])
                self.assertEqual(actual, sorted(manifest["invalid"][path.name]["findings"]))

    def test_fixture_cli_replays_exact_manifest(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertNotIn("FIXTURE_POLARITY_ERROR", completed.stdout + completed.stderr)
        self.assertEqual(completed.stdout.count('"outcome":"PASS"'), 3)
        self.assertEqual(completed.stdout.count('"outcome":"FAIL"'), 6)

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"type":"Feature","type":"Feature"}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"JSON_DUPLICATE_KEY"},
        )

    def test_unknown_kfm_property_is_rejected(self) -> None:
        candidate = json.loads(
            (FIXTURE_ROOT / "valid/valid_receipt_bound_candidate.json").read_text(
                encoding="utf-8"
            )
        )
        candidate["properties"]["kfm:undeclared_authority"] = True
        candidate["properties"]["kfm:spec_hash"] = MODULE.compute_item_spec_hash(candidate)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "FAIL")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"SCHEMA_INVALID"},
        )

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = json.loads(
            (FIXTURE_ROOT / "valid/valid_receipt_bound_candidate.json").read_text(
                encoding="utf-8"
            )
        )
        canary = "DO_NOT_ECHO_PROTECTED_OR_UNTRUSTED_VALUE"
        candidate["properties"]["kfm:unknown_field"] = canary
        candidate["properties"]["kfm:spec_hash"] = MODULE.compute_item_spec_hash(candidate)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            result = MODULE.validate_record(path)
            report = MODULE._serialize(path, result)
        self.assertNotIn(canary, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_replay_and_identity_are_deterministic(self) -> None:
        path = FIXTURE_ROOT / "valid/valid_release_linked_not_published.json"
        candidate = json.loads(path.read_text(encoding="utf-8"))
        first_hash = MODULE.compute_item_spec_hash(candidate)
        second_hash = MODULE.compute_item_spec_hash(copy.deepcopy(candidate))
        first_report = MODULE._serialize(path, MODULE.validate_record(path))
        second_report = MODULE._serialize(path, MODULE.validate_record(path))
        self.assertEqual(first_hash, second_hash)
        self.assertEqual(first_report, second_report)


if __name__ == "__main__":
    unittest.main()
