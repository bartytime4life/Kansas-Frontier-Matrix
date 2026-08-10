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
VALIDATOR_PATH = ROOT / "tools/validators/runtime/validate_worker_integrity_launch_readiness.py"
spec = importlib.util.spec_from_file_location("worker_launch_readiness_validator", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class WorkerIntegrityLaunchReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_self_check(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        validator.Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        self.assertGreaterEqual(len(self.manifest["cases"]), 20)
        outcomes: set[str] = set()
        for case in self.manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(
                    validator.materialize_case(self.manifest, case)
                )
                outcomes.add(result.outcome)
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_state"], result.state)
                self.assertEqual(
                    case["expected_findings"],
                    [
                        {"code": finding.code, "path": finding.path}
                        for finding in result.findings
                    ],
                )
        self.assertEqual({"PASS", "ABSTAIN", "DENY"}, outcomes)

    def test_ready_candidate_is_review_required_and_non_authorizing(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("REVIEW_REQUIRED", result.state)
        self.assertFalse(value["readiness"]["worker_launch_authorized"])
        self.assertFalse(value["boundary"]["worker_started"])
        self.assertFalse(value["boundary"]["proof_resolved"])
        self.assertFalse(value["boundary"]["runtime_proof_emitted"])
        self.assertFalse(value["boundary"]["release_authorized"])

    def test_declared_proof_outcomes_remain_separate_from_validation(self) -> None:
        mismatch = next(
            case for case in self.manifest["cases"] if case["case_id"] == "integrity_mismatch_denies"
        )
        value = validator.materialize_case(self.manifest, mismatch)
        result = validator.validate_payload(value)
        self.assertEqual("DENY", result.outcome)
        self.assertEqual("REVIEW_REQUIRED", result.state)
        self.assertEqual((), result.findings)
        self.assertEqual("MISMATCH", value["verification"]["declared_outcome"])

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            self.assertEqual(
                "WORKER_READINESS_JSON_DUPLICATE_KEY",
                validator.validate_file(duplicate).findings[0].code,
            )

            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
            self.assertEqual(
                "WORKER_READINESS_JSON_NONFINITE_NUMBER",
                validator.validate_file(nonfinite).findings[0].code,
            )

            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            self.assertEqual(
                "WORKER_READINESS_INPUT_SYMLINK_DENIED",
                validator.validate_file(symlink).findings[0].code,
            )

            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * validator.MAX_BYTES + b"}")
            self.assertEqual(
                "WORKER_READINESS_INPUT_TOO_LARGE",
                validator.validate_file(oversized).findings[0].code,
            )

    def test_validation_does_not_open_network(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        with patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)

    def test_serialization_does_not_echo_candidate_values(self) -> None:
        case = next(
            item
            for item in self.manifest["cases"]
            if item["case_id"] == "proof_ref_without_outcome_denied"
        )
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        output = validator._serialize(Path("candidate.json"), result)
        self.assertNotIn(value["verification"]["proof_ref"], output)
        self.assertIn("WORKER_READINESS_PROOF_BINDING_INVALID", output)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
