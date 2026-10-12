from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    ROOT
    / "tools/validators/governance/validate_temporal_retention_disposition_assessment.py"
)
SPEC = importlib.util.spec_from_file_location(
    "validate_temporal_retention_disposition_assessment", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TemporalRetentionDispositionAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        manifest = json.loads(MODULE.FIXTURES.read_text(encoding="utf-8"))
        cls.cases = {case["case_id"]: case for case in manifest["cases"]}

    def _candidate(self, case_id: str) -> dict[str, object]:
        return copy.deepcopy(self.cases[case_id]["candidate"])

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(
            json.loads(MODULE.SCHEMA.read_text(encoding="utf-8"))
        )

    def test_exact_fixture_matrix(self) -> None:
        for case_id, case in self.cases.items():
            with self.subTest(case_id=case_id):
                result = MODULE.validate_payload(case["candidate"])
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(
                    [finding.code for finding in result.findings],
                    case["expected_findings"],
                )

    def test_finite_outcomes_are_covered(self) -> None:
        outcomes = {
            MODULE.validate_payload(case["candidate"]).outcome
            for case in self.cases.values()
        }
        self.assertEqual(outcomes, {"PASS", "ABSTAIN", "DENY", "ERROR"})

    def test_only_retain_archive_and_compact_can_pass(self) -> None:
        passing = {
            case["candidate"]["subject"]["disposition"]
            for case in self.cases.values()
            if MODULE.validate_payload(case["candidate"]).outcome == "PASS"
        }
        self.assertEqual(passing, {"RETAIN", "ARCHIVE", "COMPACT"})

    def test_erasure_never_passes_local_assessment(self) -> None:
        erasure_results = {
            MODULE.validate_payload(case["candidate"]).outcome
            for case in self.cases.values()
            if case["candidate"]["subject"]["disposition"] == "ERASE"
        }
        self.assertTrue(erasure_results)
        self.assertNotIn("PASS", erasure_results)

    def test_every_fixture_denies_all_authority(self) -> None:
        for case_id, case in self.cases.items():
            with self.subTest(case_id=case_id):
                self.assertFalse(any(case["candidate"]["authority"].values()))
                self.assertFalse(case["candidate"]["decision"]["execution_authorized"])

    def test_identity_binds_disposition_semantics(self) -> None:
        candidate = self._candidate("pass_retain_complete_history")
        digest, assessment_id = MODULE.canonical_identity(candidate)
        self.assertEqual(candidate["spec_hash"], digest)
        self.assertEqual(candidate["assessment_id"], assessment_id)
        changed = copy.deepcopy(candidate)
        changed["retention_controls"]["proof_preservation"] = "DIGEST_ONLY"
        self.assertNotEqual(digest, MODULE.canonical_identity(changed)[0])

    def test_noncanonical_decision_fails_closed(self) -> None:
        candidate = self._candidate("pass_archive_complete_history")
        candidate["decision"]["recommendation"] = "REJECT"
        candidate["spec_hash"], candidate["assessment_id"] = MODULE.canonical_identity(
            candidate
        )
        result = MODULE.validate_payload(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            [finding.code for finding in result.findings],
            ["RETENTION_DECISION_MISMATCH"],
        )

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            self.assertEqual(
                [finding.code for finding in MODULE.validate_file(duplicate).findings],
                ["RETENTION_JSON_DUPLICATE_KEY"],
            )
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            self.assertEqual(
                [finding.code for finding in MODULE.validate_file(nonfinite).findings],
                ["RETENTION_JSON_NONFINITE_NUMBER"],
            )

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = [
                MODULE.validate_payload(case["candidate"])
                for case in self.cases.values()
            ]
            second = [
                MODULE.validate_payload(case["candidate"])
                for case in self.cases.values()
            ]
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
