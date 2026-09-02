"""Deterministic no-network tests for k-anonymity assessment fixtures."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.governance.k_anonymity_assessment_core import SCHEMA_PATH, validate_document
from tools.validators.governance.validate_k_anonymity_assessment import (
    load_fixture_cases,
    main,
    run_fixture_suite,
    validate_file,
)


def _deny_network(*_args, **_kwargs):
    raise AssertionError("network access attempted")


class KAnonymityAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases, findings = load_fixture_cases()
        assert not findings, findings
        cls.by_id = {case["case_id"]: case for case in cls.cases}

    def document(self, case_id: str) -> dict[str, object]:
        return copy.deepcopy(self.by_id[case_id]["document"])

    def test_schema_is_closed_and_has_no_k_default(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        policy = schema["$defs"]["policy_selection"]
        self.assertFalse(policy["additionalProperties"])
        self.assertNotIn("default", policy["properties"]["selected_k"])
        self.assertEqual("policy_profile", policy["properties"]["selected_k_source"]["const"])

    def test_exact_fixture_outcomes_and_findings(self) -> None:
        self.assertEqual(14, len(self.cases))
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                result = validate_document(case["document"])
                actual = [{"code": finding.code, "path": finding.path} for finding in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_runner_preserves_no_authority_boundary(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual({"PASS": 1, "ABSTAIN": 2, "DENY": 7, "ERROR": 4}, payload["counts"])
        self.assertEqual("NONE", payload["authority"])
        self.assertIn("no_privacy_proof", payload["non_effects"])
        self.assertIn("no_release_or_publication", payload["non_effects"])

    def test_policy_support_abstains_small_class_denies_and_arithmetic_errors(self) -> None:
        expectations = {
            "abstain_missing_policy_decision": ("ABSTAIN", "KANON_SUPPORT_INCOMPLETE"),
            "deny_equivalence_class_below_k": ("DENY", "KANON_THRESHOLD_NOT_MET"),
            "error_unexplained_generalization": ("ERROR", "KANON_GENERALIZATION_UNEXPLAINED"),
            "error_unexplained_suppression": ("ERROR", "KANON_SUPPRESSION_UNEXPLAINED"),
            "error_row_count_closure": ("ERROR", "KANON_ROW_COUNT_CLOSURE_INVALID"),
        }
        for case_id, (outcome, code) in expectations.items():
            with self.subTest(case=case_id):
                result = validate_document(self.document(case_id))
                self.assertEqual(outcome, result.outcome)
                self.assertIn(code, {finding.code for finding in result.findings})

    def test_no_network_deterministic_non_echoing_output(self) -> None:
        candidate = self.document("valid_policy_selected_k5")
        with mock.patch.object(socket.socket, "connect", _deny_network), mock.patch.object(socket, "create_connection", _deny_network), mock.patch.object(urllib.request, "urlopen", _deny_network):
            self.assertEqual("PASS", validate_document(candidate).outcome)
        marker = "sensitive-marker-must-not-echo"
        candidate["subject"]["policy_label"] = marker
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            outputs = []
            for _ in range(2):
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    self.assertEqual(1, main([str(path)]))
                outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(marker, outputs[0])

    def test_bounded_loader_and_finite_cli_codes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "candidate.json"
            values = [
                (self.document("valid_policy_selected_k5"), 0),
                (self.document("deny_equivalence_class_below_k"), 1),
                (self.document("abstain_missing_evidence_support"), 3),
            ]
            for value, code in values:
                path.write_text(json.dumps(value), encoding="utf-8")
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(code, main([str(path)]))
            path.write_text("{not-json}\n", encoding="utf-8")
            self.assertEqual("ERROR", validate_file(path).outcome)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(2, main([str(path)]))
            oversized = root / "oversized.json"
            oversized.write_bytes(b" " * 1_000_001)
            self.assertEqual("ERROR", validate_file(oversized).outcome)

    def test_multi_file_cli_uses_highest_severity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = []
            for name, case_id in (("abstain.json", "abstain_missing_evidence_support"), ("deny.json", "deny_equivalence_class_below_k")):
                path = root / name
                path.write_text(json.dumps(self.document(case_id)), encoding="utf-8")
                paths.append(path)
            invalid = root / "invalid.json"
            invalid.write_text("{not-json}\n", encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(1, main([str(paths[0]), str(paths[1])]))
                self.assertEqual(2, main([str(paths[1]), str(invalid)]))


if __name__ == "__main__":
    unittest.main()
