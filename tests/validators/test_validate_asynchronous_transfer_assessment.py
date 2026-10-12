from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.source import validate_asynchronous_transfer_assessment as validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validators/source/validate_asynchronous_transfer_assessment.py"


class AsynchronousTransferAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_fixture_manifest_matches_exactly(self) -> None:
        self.assertEqual(20, len(self.manifest["cases"]))
        for case in self.manifest["cases"]:
            with self.subTest(case_id=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(self.manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_suite_spans_all_outcomes(self) -> None:
        outcomes = {
            validator.validate_payload(validator.materialize_case(self.manifest, case)).outcome
            for case in self.manifest["cases"]
        }
        self.assertEqual({"PASS", "ABSTAIN", "DENY", "ERROR"}, outcomes)

    def test_finite_decisions_are_covered(self) -> None:
        states = {
            validator.materialize_case(self.manifest, case)["decision"]["state"]
            for case in self.manifest["cases"]
        }
        self.assertEqual(
            {"WAITING", "RESUME_ELIGIBLE", "COMPLETE_CANDIDATE", "QUARANTINED", "TERMINAL_NO_ARTIFACT", "ERROR"},
            states,
        )

    def test_identity_is_deterministic_and_sensitive(self) -> None:
        case = self.manifest["cases"][0]
        first = validator.materialize_case(self.manifest, case)
        second = validator.materialize_case(self.manifest, case)
        self.assertEqual(first["assessment_id"], second["assessment_id"])
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        changed = copy.deepcopy(first)
        changed["checkpoint"]["sequence"] += 1
        digest, identifier = validator.canonical_identity(changed)
        self.assertNotEqual(first["spec_hash"], digest)
        self.assertNotEqual(first["assessment_id"], identifier)

    def test_parser_rejects_duplicate_keys_and_nonfinite_numbers(self) -> None:
        samples = [
            ('{"a":1,"a":2}', "ASYNC_TRANSFER_JSON_DUPLICATE_KEY"),
            ('{"a":NaN}', "ASYNC_TRANSFER_JSON_NONFINITE_NUMBER"),
        ]
        with tempfile.TemporaryDirectory() as directory:
            for index, (content, expected_code) in enumerate(samples):
                with self.subTest(expected_code=expected_code):
                    path = Path(directory) / f"sample-{index}.json"
                    path.write_text(content, encoding="utf-8")
                    value, findings = validator._read(path)
                    self.assertIsNone(value)
                    self.assertEqual(expected_code, findings[0].code)

    def test_parser_rejects_symlink_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            value, findings = validator._read(link)
            self.assertIsNone(value)
            self.assertEqual("ASYNC_TRANSFER_INPUT_SYMLINK_DENIED", findings[0].code)

    def test_complete_candidate_remains_non_authoritative(self) -> None:
        case = next(item for item in self.manifest["cases"] if item["case_id"] == "complete-size-and-digest-match")
        payload = validator.materialize_case(self.manifest, case)
        self.assertEqual("COMPLETE_CANDIDATE", payload["decision"]["state"])
        self.assertEqual("QUARANTINE_CANDIDATE", payload["ingest"]["state"])
        self.assertTrue(all(value is False for key, value in payload["governance"].items() if key != "execution_mode"))

    def test_serialized_result_declares_non_effects(self) -> None:
        result = validator.validate_payload(validator.materialize_case(self.manifest, self.manifest["cases"][0]))
        serialized = json.loads(validator.serialize(None, result))
        self.assertEqual("NONE", serialized["authority"])
        self.assertIn("no_network", serialized["non_effects"])
        self.assertIn("no_ingest", serialized["non_effects"])
        self.assertIn("no_publication", serialized["non_effects"])

    def test_validator_has_no_network_client_import(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        for forbidden in ("import requests", "import urllib", "import socket", "httpx", "aiohttp"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
