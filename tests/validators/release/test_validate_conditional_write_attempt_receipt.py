from __future__ import annotations

import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path

from tools.validators._common.jsonschema_runner import load_validator
from tools.validators.release import validate_conditional_write_attempt_receipt as validator
from tools.validators.release._conditional_write_attempt_receipt_model import (
    CASES_PATH,
    FIXTURE_ROOT,
    SCHEMA_PATH,
    build_candidate,
)
from tools.validators.release.validate_conditional_write_preflight import validate_document as validate_preflight

class ConditionalWriteAttemptReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        value = validator.load_json_file(CASES_PATH)
        cls.cases = {case["case_id"]: case for case in value["cases"]}

    def load_json(self, relative: str) -> dict:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def test_schema_is_closed_and_no_authority(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["properties"]["execution_mode"]["const"], "FIXTURE_ONLY_DECLARATION")
        claims = schema["$defs"]["claims"]["properties"]
        for field in (
            "validator_network_accessed", "external_state_authenticated",
            "preflight_authority_verified", "subject_execution_authenticated",
            "write_verified", "lifecycle_write_verified", "release_created",
            "published", "public_use_authorized",
        ):
            self.assertFalse(claims[field]["const"], field)

    def test_all_cases_build_deterministically_and_match_expected(self) -> None:
        for case_id, case in self.cases.items():
            with self.subTest(case_id=case_id):
                first = build_candidate(case)
                second = build_candidate(case)
                self.assertEqual(first, second)
                self.assertEqual(validate_preflight(first["preflight_candidate"]).outcome, "PASS")
                result = validator.validate_document(first)
                self.assertEqual(result.outcome, "PASS", result.findings)
                self.assertEqual(
                    {"outcome": first["result"]["outcome"], "reason_codes": first["result"]["reason_codes"]},
                    case["expected"],
                )

    def test_valid_fixture_replays_create_applied(self) -> None:
        expected = build_candidate(self.cases["create_applied"])
        fixture = self.load_json("valid/valid_applied.json")
        self.assertEqual(fixture, expected)
        self.assertEqual(list(load_validator(SCHEMA_PATH).iter_errors(fixture)), [])
        self.assertEqual(validator.validate_document(fixture).outcome, "PASS")

    def test_schema_invalid_authority_overreach_is_denied(self) -> None:
        candidate = self.load_json("invalid/invalid_authority_overreach.json")
        self.assertTrue(list(load_validator(SCHEMA_PATH).iter_errors(candidate)))
        result = validator.validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertTrue(any(finding.code == "SCHEMA_INVALID" for finding in result.findings))

    def test_preflight_identity_mutation_is_denied(self) -> None:
        candidate = self.load_json("valid/valid_applied.json")
        candidate["preflight_candidate"]["spec_hash"] = "sha256:" + "0" * 64
        result = validator.validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertTrue(any(finding.code == "PREFLIGHT_CANDIDATE_INVALID" for finding in result.findings))

    def test_result_mutation_is_denied(self) -> None:
        candidate = self.load_json("valid/valid_applied.json")
        candidate["result"]["outcome"] = "NO_ACTION"
        result = validator.validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertTrue(any(finding.code == "RESULT_DERIVATION_MISMATCH" for finding in result.findings))

    def test_attempt_fingerprint_mutation_is_denied(self) -> None:
        candidate = self.load_json("valid/valid_applied.json")
        candidate["result"]["attempt_fingerprint"] = "sha256:" + "1" * 64
        result = validator.validate_document(candidate)
        codes = {finding.code for finding in result.findings}
        self.assertIn("ATTEMPT_FINGERPRINT_MISMATCH", codes)
        self.assertIn("RESULT_DERIVATION_MISMATCH", codes)

    def test_spec_hash_and_receipt_id_mutations_are_denied(self) -> None:
        candidate = self.load_json("valid/valid_applied.json")
        candidate["spec_hash"] = "sha256:" + "2" * 64
        candidate["receipt_id"] = "kfm:conditional-write-attempt-receipt:" + "3" * 64
        codes = {finding.code for finding in validator.validate_document(candidate).findings}
        self.assertIn("SPEC_HASH_MISMATCH", codes)
        self.assertIn("RECEIPT_ID_MISMATCH", codes)

    def test_no_action_never_declares_request(self) -> None:
        candidate = build_candidate(self.cases["existing_content_no_action"])
        self.assertEqual(candidate["result"]["outcome"], "NO_ACTION")
        self.assertFalse(candidate["attempt"]["request_emitted"])
        self.assertEqual(candidate["attempt"]["transport"], "NONE")
        self.assertFalse(candidate["claims"]["write_verified"])

    def test_upstream_hold_dominates_attempt(self) -> None:
        candidate = build_candidate(self.cases["upstream_hold"])
        self.assertEqual(candidate["preflight_candidate"]["preflight"]["outcome"], "HOLD")
        self.assertEqual(candidate["result"]["outcome"], "HOLD")
        self.assertFalse(candidate["attempt"]["request_emitted"])

    def test_precondition_failure_is_conflict_not_applied(self) -> None:
        candidate = build_candidate(self.cases["precondition_failed"])
        self.assertEqual(candidate["attempt"]["response_status"], 412)
        self.assertEqual(candidate["result"]["outcome"], "CONFLICT")
        self.assertEqual(candidate["result"]["reason_codes"], ["PRECONDITION_FAILED"])

    def test_applied_result_still_has_no_execution_authority(self) -> None:
        candidate = build_candidate(self.cases["create_applied"])
        self.assertEqual(candidate["result"]["outcome"], "APPLIED")
        self.assertFalse(candidate["claims"]["subject_execution_authenticated"])
        self.assertFalse(candidate["claims"]["write_verified"])
        self.assertFalse(candidate["claims"]["published"])

    def test_transport_error_is_explicit_error(self) -> None:
        candidate = build_candidate(self.cases["transport_timeout"])
        self.assertEqual(candidate["result"]["outcome"], "ERROR")
        self.assertEqual(candidate["result"]["reason_codes"], ["TRANSPORT_ERROR"])
        self.assertEqual(candidate["attempt"]["after_state"]["state"], "UNKNOWN")

    def test_static_no_network_or_writer_surface(self) -> None:
        paths = [
            Path(validator.__file__),
            Path(__file__).resolve().parents[3] / "tools/validators/release/_conditional_write_attempt_receipt_model.py",
        ]
        denied = (
            "import requests", "from requests", "import socket", "from socket",
            "import urllib", "from urllib", "import subprocess", "from subprocess",
            "boto3", "httpx", "requests.put", "urlopen(", "KFM_PUBLISH_URL",
        )
        for path in paths:
            source = path.read_text(encoding="utf-8")
            for fragment in denied:
                with self.subTest(path=path.name, fragment=fragment):
                    self.assertNotIn(fragment, source)

    def test_invalid_json_cli_does_not_echo_canary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad.json"
            canary = "PRIVATE-CANARY-WRITE-TOKEN"
            path.write_text('{"value":"' + canary + '",}', encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = validator.main([str(path)])
            self.assertEqual(code, 2)
            self.assertNotIn(canary, output.getvalue())

    def test_fixture_suite_cli(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = validator.main(["--fixtures"])
        self.assertEqual(code, 0)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)
