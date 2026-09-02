from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/domains/soil/validate_promotion_materiality.py"
FIXTURES = ROOT / "fixtures/domains/soil/promotion_materiality"
PROFILE = ROOT / "pipeline_specs/soil/promotion_materiality_profile.v1.json"
PROFILE_SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/promotion_materiality_profile.schema.json"
INPUT_SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/promotion_materiality_input.schema.json"

SPEC = importlib.util.spec_from_file_location("validate_soil_promotion_materiality", VALIDATOR)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

class SoilPromotionMaterialityTests(unittest.TestCase):
    def _input(self, name: str) -> Path:
        return FIXTURES / "inputs/valid" / f"{name}.json"

    def test_profile_schema_and_hash(self) -> None:
        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        schema = json.loads(PROFILE_SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(profile)))
        self.assertEqual(profile["spec_hash"], MODULE.compute_spec_hash({k:v for k,v in profile.items() if k != "spec_hash"}))
        self.assertFalse(profile["governance"]["promotion_authorized"])

    def test_input_schema_is_closed(self) -> None:
        schema = json.loads(INPUT_SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])

    def test_timestamp_only_change_is_non_event(self) -> None:
        result = MODULE.assess(self._input("timestamp_only"))
        self.assertTrue(result.ok)
        self.assertEqual(result.assessment["classification"], {"change_class":"BYTE_ONLY","material":False,"outcome":"NON_EVENT","reason_codes":["BYTE_ONLY_CHANGE","CANONICAL_EQUIVALENT"]})
        self.assertFalse(result.assessment["comparison"]["semantic_changed"])

    def test_substantive_change_is_candidate_not_authority(self) -> None:
        result = MODULE.assess(self._input("content_changed"))
        self.assertTrue(result.ok)
        self.assertEqual(result.assessment["classification"]["outcome"], "PROMOTION_CANDIDATE")
        self.assertTrue(result.assessment["classification"]["material"])
        self.assertFalse(result.assessment["governance"]["promotion_authorized"])
        self.assertFalse(result.assessment["governance"]["policy_evaluated"])

    def test_multiple_dimensions_preserve_each_criterion(self) -> None:
        result = MODULE.assess(self._input("multiple_dimensions_changed"))
        passed = [item["metric"] for item in result.assessment["criteria"] if item["result"] == "PASS" and item["metric"] != "substantive_hash_change_count"]
        self.assertEqual(passed, ["policy_hash", "schema_hash", "source_descriptor_hash"])

    def test_missing_baseline_and_evidence_hold(self) -> None:
        for name, reason in (("missing_baseline_hold","MISSING_BASELINE"),("insufficient_evidence_hold","INSUFFICIENT_EVIDENCE")):
            with self.subTest(name=name):
                result = MODULE.assess(self._input(name))
                self.assertTrue(result.ok)
                self.assertEqual(result.assessment["classification"]["outcome"], "HOLD")
                self.assertIn(reason, result.assessment["classification"]["reason_codes"])

    def test_manifest_exact_outputs_and_findings(self) -> None:
        manifest = json.loads((FIXTURES / "expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["cases"]), 10)
        for case in manifest["cases"]:
            result = MODULE.assess(FIXTURES / case["input"])
            outcome = "ERROR" if result.assessment is None else result.assessment["classification"]["outcome"]
            self.assertEqual(outcome, case["expected_outcome"], case["case_id"])
            self.assertEqual(sorted({item.code for item in result.findings}), case["expected_findings"], case["case_id"])
            if case.get("expected_assessment"):
                expected = json.loads((FIXTURES / case["expected_assessment"]).read_text(encoding="utf-8"))
                self.assertEqual(result.assessment, expected, case["case_id"])

    def test_duplicate_keys_and_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"; duplicate.write_text('{"assessment_id":"a","assessment_id":"b"}', encoding="utf-8")
            nonfinite = Path(directory) / "nonfinite.json"; nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            self.assertEqual({item.code for item in MODULE.assess(duplicate).findings}, {"JSON_DUPLICATE_KEY"})
            self.assertEqual({item.code for item in MODULE.assess(nonfinite).findings}, {"JSON_NONFINITE_NUMBER"})

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_symlink_input_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            real = Path(directory) / "real.json"; real.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            try: link.symlink_to(real)
            except OSError: self.skipTest("symlink creation unavailable")
            self.assertEqual({item.code for item in MODULE.assess(link).findings}, {"INPUT_SYMLINK_DENIED"})

    def test_no_network_and_deterministic_cli(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.assess(self._input("content_changed")).assessment
            second = MODULE.assess(self._input("content_changed")).assessment
        self.assertEqual(first, second)
        completed = subprocess.run([sys.executable, str(VALIDATOR), "--fixtures"], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 10)
        self.assertNotIn('"suite_match":false', completed.stdout)

if __name__ == "__main__":
    unittest.main()
