from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/evidence/validate_historic_map_scan_lineage_assessment.py"
spec = importlib.util.spec_from_file_location("historic_map_scan_lineage_assessment", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class HistoricMapScanLineageAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_self_check(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        validator.Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        self.assertGreaterEqual(len(self.manifest["cases"]), 20)
        for case in self.manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(self.manifest, case))
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_assessment_state"], result.assessment_state)
                self.assertEqual(
                    case["expected_findings"],
                    [{"code": item.code, "path": item.path} for item in result.findings],
                )

    def test_positive_candidate_preserves_lineage_and_authority_boundaries(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("REVIEW_REQUIRED", result.assessment_state)
        self.assertNotEqual(value["original_map"]["original_map_ref"], value["scan"]["scan_artifact_ref"])
        self.assertEqual("CONTEXT_REPRESENTATION", value["derivative_use"]["source_role"])
        self.assertFalse(value["derivative_use"]["public_use_authorized"])
        self.assertTrue(all(not value["governance"][key] for key in value["governance"] if key != "fixture_only"))

    def test_catalog_only_candidate_can_preserve_no_georeference(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][1])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("NOT_ATTEMPTED", value["georeference"]["status"])
        self.assertIsNone(value["georeference"]["derivative_artifact_ref"])
        self.assertEqual(["CATALOG_ONLY"], value["derivative_use"]["permitted_uses"])

    def test_duplicate_key_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            self.assertEqual("HISTORIC_MAP_JSON_DUPLICATE_KEY", validator.validate_file(duplicate).findings[0].code)
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
            self.assertEqual("HISTORIC_MAP_JSON_NONFINITE_NUMBER", validator.validate_file(nonfinite).findings[0].code)
            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            self.assertEqual("HISTORIC_MAP_INPUT_SYMLINK_DENIED", validator.validate_file(symlink).findings[0].code)
            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * validator.MAX_BYTES + b"}")
            self.assertEqual("HISTORIC_MAP_INPUT_TOO_LARGE", validator.validate_file(oversized).findings[0].code)

    def test_validation_does_not_open_network(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        with patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)

    def test_serialization_does_not_echo_candidate_values(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        value["original_map"]["citation_ref"] = None
        value["spec_hash"], value["assessment_id"] = validator.canonical_identity(value)
        result = validator.validate_payload(value)
        output = validator._serialize(Path("candidate.json"), result)
        self.assertNotIn(value["original_map"]["original_map_ref"], output)
        self.assertIn("HISTORIC_MAP_ORIGINAL_CITATION_REQUIRED", output)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
