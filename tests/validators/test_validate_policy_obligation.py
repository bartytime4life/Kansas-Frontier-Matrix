from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/policy/validate_policy_obligation.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/policy/policy_obligation.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/policy/policy_obligation"
REGISTRY_PATH = REPO_ROOT / "policy/decision/vocabulary.v1.json"

SPEC = importlib.util.spec_from_file_location("validate_policy_obligation", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PolicyObligationValidatorTests(unittest.TestCase):
    def _load(self, relative: str) -> dict[str, object]:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def test_schema_is_closed_inactive_profile(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")

    def test_registry_contains_pass7_obligation_codes_in_canonical_order(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        codes = [entry["code"] for entry in registry["obligation_codes"]]
        self.assertEqual(codes, sorted(set(codes)))
        self.assertTrue({"AGGREGATE_ONLY", "RETAIN_UNTIL", "SHARE_ALIKE"}.issubset(codes))

    def test_all_valid_fixtures_pass(self) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertEqual(len(paths), 4)
        for path in paths:
            with self.subTest(path=path.name):
                self.assertTrue(MODULE.validate_record(path).ok)

    def test_manifest_has_exact_reviewed_polarity(self) -> None:
        manifest = self._load("expected_findings_manifest.json")
        cases = manifest["cases"]
        self.assertEqual(len(cases), 11)
        self.assertEqual(len({case["case_id"] for case in cases}), len(cases))
        for case in cases:
            path = FIXTURE_ROOT / case["record"]
            with self.subTest(case=case["case_id"]):
                result = MODULE.validate_record(path)
                actual_outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
                actual_codes = sorted({finding.code for finding in result.findings})
                self.assertEqual(actual_outcome, case["expected_outcome"])
                self.assertEqual(actual_codes, case["expected_findings"])

    def test_spec_hash_reproduces_valid_fixture(self) -> None:
        candidate = self._load("valid/valid_generalize_satisfied.json")
        self.assertEqual(MODULE.compute_record_spec_hash(candidate), candidate["spec_hash"])

    def test_code_specific_parameter_rule_is_enforced(self) -> None:
        candidate = self._load("valid/valid_generalize_satisfied.json")
        candidate["parameters"]["generalize_distance_m"] = None
        candidate["spec_hash"] = MODULE.compute_record_spec_hash(candidate)
        result = MODULE.validate_payload(candidate)
        self.assertEqual({finding.code for finding in result.findings}, {"REQUIRED_PARAMETER_MISSING"})

    def test_enforcement_state_cannot_claim_satisfied_without_evidence(self) -> None:
        candidate = self._load("valid/valid_generalize_satisfied.json")
        candidate["enforcement"]["evidence_refs"] = []
        candidate["spec_hash"] = MODULE.compute_record_spec_hash(candidate)
        result = MODULE.validate_payload(candidate)
        self.assertIn("ENFORCEMENT_STATE_INCOHERENT", {finding.code for finding in result.findings})

    def test_valid_time_reversal_fails(self) -> None:
        candidate = self._load("valid/valid_attach_citations_pending.json")
        candidate["valid_time"]["effective_until"] = "2026-08-07T00:00:00Z"
        candidate["spec_hash"] = MODULE.compute_record_spec_hash(candidate)
        result = MODULE.validate_payload(candidate)
        self.assertIn("VALID_TIME_REVERSED", {finding.code for finding in result.findings})

    def test_duplicate_keys_and_nonfinite_values_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"object_type":"PolicyObligation","object_type":"PolicyObligation"}', encoding="utf-8")
            nonfinite = Path(directory) / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            duplicate_result = MODULE.validate_record(duplicate)
            nonfinite_result = MODULE.validate_record(nonfinite)
        self.assertTrue(duplicate_result.error)
        self.assertEqual({finding.code for finding in duplicate_result.findings}, {"JSON_DUPLICATE_KEY"})
        self.assertTrue(nonfinite_result.error)
        self.assertEqual({finding.code for finding in nonfinite_result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = self._load("valid/valid_attach_citations_pending.json")
        untrusted = "UNTRUSTED_SECRET_VALUE_DO_NOT_ECHO"
        candidate["operation"] = untrusted
        candidate["spec_hash"] = MODULE.compute_record_spec_hash(candidate)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            report = MODULE.serialize(path, MODULE.validate_record(path))
        self.assertNotIn(untrusted, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_fixture_suite_is_no_network_and_cli_is_deterministic(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            ok, first = MODULE.validate_fixture_suite()
            second_ok, second = MODULE.validate_fixture_suite()
        self.assertTrue(ok)
        self.assertTrue(second_ok)
        self.assertEqual(first, second)

        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 11)
        self.assertNotIn('suite_match":false', completed.stdout)

    def test_validator_does_not_mutate_payload(self) -> None:
        candidate = self._load("valid/valid_aggregate_only_pending.json")
        original = copy.deepcopy(candidate)
        MODULE.validate_payload(candidate)
        self.assertEqual(candidate, original)


if __name__ == "__main__":
    unittest.main()
