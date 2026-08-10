from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validators/source/validate_source_terms_drift_disposition.py"
spec = importlib.util.spec_from_file_location("source_terms_drift_validator", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class SourceTermsDriftDispositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_self_check(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        validator.Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        self.assertGreaterEqual(len(self.manifest["cases"]), 18)
        outcomes: set[str] = set()
        states: set[str] = set()
        for case in self.manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(
                    validator.materialize_case(self.manifest, case)
                )
                outcomes.add(result.outcome)
                if result.state is not None:
                    states.add(result.state)
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_state"], result.state)
                self.assertEqual(
                    case["expected_findings"],
                    [
                        {"code": finding.code, "path": finding.path}
                        for finding in result.findings
                    ],
                )
        self.assertEqual({"PASS", "DENY"}, outcomes)
        self.assertEqual({"NO_ACTION", "REASSESS", "HOLD", "ERROR"}, states)

    def test_valid_no_change_is_non_authorizing(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("NO_ACTION", result.state)
        self.assertFalse(value["boundary"]["legal_determination_made"])
        self.assertFalse(value["boundary"]["hold_executed"])
        self.assertFalse(value["boundary"]["withdrawal_executed"])
        self.assertFalse(value["boundary"]["publication_authorized"])

    def test_restrictive_change_routes_review_without_execution(self) -> None:
        case = next(
            item
            for item in self.manifest["cases"]
            if item["case_id"] == "valid_restrictive_redistribution_change"
        )
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("HOLD", result.state)
        self.assertEqual(
            ["RECOMPUTE_REVIEW", "WITHDRAWAL_REVIEW"],
            [item["proposed_action"] for item in value["downstream_dependencies"]],
        )
        self.assertFalse(value["boundary"]["recomputation_executed"])
        self.assertFalse(value["boundary"]["withdrawal_executed"])

    def test_snapshot_and_assessment_identity_are_deterministic(self) -> None:
        case = self.manifest["cases"][0]
        first = validator.materialize_case(self.manifest, case)
        second = validator.materialize_case(self.manifest, case)
        self.assertEqual(first["prior_snapshot"]["snapshot_hash"], second["prior_snapshot"]["snapshot_hash"])
        self.assertEqual(first["current_snapshot"]["snapshot_hash"], second["current_snapshot"]["snapshot_hash"])
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        self.assertEqual(first["assessment_id"], second["assessment_id"])

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            self.assertEqual(
                "TERMS_DRIFT_JSON_DUPLICATE_KEY",
                validator.validate_file(duplicate).findings[0].code,
            )
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
            self.assertEqual(
                "TERMS_DRIFT_JSON_NONFINITE_NUMBER",
                validator.validate_file(nonfinite).findings[0].code,
            )
            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            self.assertEqual(
                "TERMS_DRIFT_INPUT_SYMLINK_DENIED",
                validator.validate_file(symlink).findings[0].code,
            )
            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * validator.MAX_BYTES + b"}")
            self.assertEqual(
                "TERMS_DRIFT_INPUT_TOO_LARGE",
                validator.validate_file(oversized).findings[0].code,
            )

    def test_validation_does_not_open_network(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        with patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)

    def test_serialization_does_not_echo_terms_or_dependency_values(self) -> None:
        case = next(
            item
            for item in self.manifest["cases"]
            if item["case_id"] == "downstream_action_underreacts"
        )
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        output = validator._serialize(Path("candidate.json"), result)
        self.assertNotIn("example-dataset-2026-04", output)
        self.assertNotIn("LicenseRef-Agency-Open-v1", output)
        self.assertIn("TERMS_DRIFT_DOWNSTREAM_ACTION_MISMATCH", output)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
