from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validators/validate_measurement_support_reconciliation.py"
SCHEMA_PATH = ROOT / "schemas/contracts/v1/common/measurement_support_reconciliation.schema.json"

SPEC = importlib.util.spec_from_file_location("measurement_support_reconciliation_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class MeasurementSupportReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_fixture_matrix_is_exact(self) -> None:
        outcomes: set[str] = set()
        for case in self.manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(self.manifest, case))
                outcomes.add(result.outcome)
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_profile_state"], result.profile_state)
                self.assertEqual(case["expected_findings"], [{"code": item.code, "path": item.path} for item in result.findings])
        self.assertEqual({"PASS", "ABSTAIN", "DENY"}, outcomes)

    def test_positive_candidate_preserves_role_and_support_qualifications(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("QUALIFIED", value["reconciliation"]["outcome"])
        self.assertEqual("MODELED", value["supports"][0]["knowledge_character"])
        self.assertEqual("MEASURED", value["supports"][1]["knowledge_character"])
        self.assertIn("UNIT_CONVERSION_APPLIED", value["reconciliation"]["reason_codes"])
        self.assertFalse(value["governance"]["publication_authorized"])

    def test_unsupported_support_abstains_without_semantic_findings(self) -> None:
        case = next(item for item in self.manifest["cases"] if item["case_id"] == "vertical_mismatch_hold")
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        self.assertEqual("ABSTAIN", result.outcome)
        self.assertEqual("HOLD", result.profile_state)
        self.assertEqual((), result.findings)
        self.assertIn("VERTICAL_SUPPORT_MISMATCH", value["reconciliation"]["reason_codes"])

    def test_identity_is_content_addressed(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        self.assertEqual((value["spec_hash"], value["assessment_id"]), validator.canonical_identity(value))

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            self.assertEqual("MEASUREMENT_JSON_DUPLICATE_KEY", validator.validate_file(duplicate).findings[0].code)
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
            self.assertEqual("MEASUREMENT_JSON_NONFINITE_NUMBER", validator.validate_file(nonfinite).findings[0].code)
            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            self.assertEqual("MEASUREMENT_INPUT_SYMLINK_DENIED", validator.validate_file(symlink).findings[0].code)
            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * validator.MAX_BYTES + b"}")
            self.assertEqual("MEASUREMENT_INPUT_TOO_LARGE", validator.validate_file(oversized).findings[0].code)

    def test_validation_does_not_open_network(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        with patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)

    def test_serialization_does_not_echo_candidate_values(self) -> None:
        case = {"mutations": [{"path": "/unit_transform/transformed_value", "value": 999.0}]}
        value = validator.materialize_case(self.manifest, case)
        output = validator._serialize(Path("candidate.json"), validator.validate_payload(value))
        self.assertNotIn("999", output)
        self.assertIn("MEASUREMENT_TRANSFORM_VALUE_MISMATCH", output)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
