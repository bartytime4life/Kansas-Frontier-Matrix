from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_runtime_response_envelope.py"
SPEC = importlib.util.spec_from_file_location("runtime_response_validator", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
validator_module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator_module
SPEC.loader.exec_module(validator_module)


class RuntimeResponsePrecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = validator_module._validator()
        cls.fixture_root = REPO_ROOT / "fixtures/contracts/v1/runtime/runtime_response_envelope"
        cls.answer = json.loads((cls.fixture_root / "valid/valid_2.json").read_text(encoding="utf-8"))

    def _temporary_findings(self, value: dict[str, object]) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "case.json"
            path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
            return validator_module.validate_path(path, self.validator)

    def test_answer_discloses_requested_and_actual_precision(self) -> None:
        self.assertEqual(
            validator_module.validate_path(self.fixture_root / "valid/valid_2.json", self.validator),
            [],
        )
        actual = self.answer["precision_actually_used"]
        self.assertEqual(actual["spatial"]["resolution"], "250 m modeled grid")
        self.assertEqual(actual["requested_precision"]["spatial"], "30 m")

    def test_answer_without_precision_fails_schema(self) -> None:
        value = copy.deepcopy(self.answer)
        value.pop("precision_actually_used")
        self.assertEqual(self._temporary_findings(value), ["SCHEMA_INVALID"])

    def test_negative_outcome_cannot_leak_precision(self) -> None:
        value = copy.deepcopy(self.answer)
        value["outcome"] = "ABSTAIN"
        value["reason_code"] = "INSUFFICIENT_EVIDENCE"
        value["evidence_refs"] = []
        self.assertEqual(self._temporary_findings(value), ["SCHEMA_INVALID"])

    def test_precision_evidence_must_be_top_level(self) -> None:
        value = copy.deepcopy(self.answer)
        value["precision_actually_used"]["evidence_refs"][0]["ref"] = "obs:2"
        self.assertEqual(
            self._temporary_findings(value),
            ["PRECISION_EVIDENCE_NOT_TOP_LEVEL"],
        )

    def test_generalization_requires_transform_receipt(self) -> None:
        value = copy.deepcopy(self.answer)
        value["precision_actually_used"]["spatial"]["generalization_applied"] = True
        self.assertEqual(
            self._temporary_findings(value),
            ["GENERALIZATION_RECEIPT_REQUIRED"],
        )
        value["precision_actually_used"]["transform_receipt_refs"] = [
            "urn:kfm:transform-receipt:synthetic-generalization-v1"
        ]
        self.assertEqual(self._temporary_findings(value), [])

    def test_precision_interval_must_not_be_inverted(self) -> None:
        value = copy.deepcopy(self.answer)
        interval = value["precision_actually_used"]["temporal"]["observation_interval"]
        interval["start"], interval["end"] = interval["end"], interval["start"]
        self.assertEqual(
            self._temporary_findings(value),
            ["PRECISION_INTERVAL_INVERTED"],
        )

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"id":"a","id":"b"}\n', encoding="utf-8")
            self.assertEqual(validator_module.validate_path(path, self.validator), ["JSON_DUPLICATE_KEY"])

    def test_fixture_cli_passes_existing_fixture_lanes(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(MODULE_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("EXPECTED_FAIL", completed.stdout)


if __name__ == "__main__":
    unittest.main()
