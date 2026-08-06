from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[5]
CLASSIFIER_PATH = REPO_ROOT / "packages/domains/flora/normalizers/intake_governance.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/flora/flora_occurrence_intake_decision.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/flora/flora_occurrence_intake_decision"
CANDIDATE_ROOT = REPO_ROOT / "fixtures/domains/flora/flora_occurrence_candidate"

SPEC = importlib.util.spec_from_file_location("flora_intake_governance_under_test", CLASSIFIER_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FloraOccurrenceIntakeGovernanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema, format_checker=FormatChecker())
        cls.manifest = json.loads((FIXTURE_ROOT / "expected_outcomes.json").read_text(encoding="utf-8"))

    @staticmethod
    def _candidate(path: str) -> dict:
        if path.startswith("../flora_occurrence_candidate/"):
            relative = path.removeprefix("../flora_occurrence_candidate/")
            return json.loads((CANDIDATE_ROOT / relative).read_text(encoding="utf-8"))
        return json.loads((FIXTURE_ROOT / path).read_text(encoding="utf-8"))

    @staticmethod
    def _peers(path: str) -> list[dict]:
        return json.loads((FIXTURE_ROOT / path).read_text(encoding="utf-8"))

    def test_schema_is_closed_proposed_draft_2020_12(self) -> None:
        self.assertFalse(self.schema["additionalProperties"])
        self.assertEqual(self.schema["x-kfm"]["status"], "PROPOSED")
        self.assertEqual(self.schema["x-kfm"]["authority"], "bounded_intake_classification_only")

    def test_valid_decisions_match_exact_expected_objects_and_schema(self) -> None:
        valid = [case for case in self.manifest["cases"] if case["expected_decision"]]
        self.assertEqual(len(valid), 7)
        for case in valid:
            with self.subTest(case=case["name"]):
                result = MODULE.classify_candidate(
                    self._candidate(case["candidate"]), self._peers(case["peers"])
                )
                expected = json.loads((FIXTURE_ROOT / case["expected_decision"]).read_text(encoding="utf-8"))
                self.assertEqual(result.outcome, case["outcome"])
                self.assertEqual(result.decision, expected)
                self.assertEqual(list(self.validator.iter_errors(result.decision)), [])
                self.assertEqual(result.decision["spec_hash"], MODULE.decision_spec_hash(result.decision))

    def test_error_fixtures_match_exact_findings(self) -> None:
        errors = [case for case in self.manifest["cases"] if case["outcome"] == "ERROR"]
        self.assertEqual(len(errors), 3)
        for case in errors:
            with self.subTest(case=case["name"]):
                result = MODULE.classify_candidate(
                    self._candidate(case["candidate"]), self._peers(case["peers"])
                )
                self.assertEqual(result.outcome, "ERROR")
                self.assertIsNone(result.decision)
                self.assertEqual(sorted({item.code for item in result.findings}), sorted(case["findings"]))

    def test_fixture_cli_replays_exact_profile(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(CLASSIFIER_PATH), "--fixtures", str(FIXTURE_ROOT)],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertNotIn("FIXTURE_POLARITY_ERROR", completed.stdout + completed.stderr)
        self.assertNotIn("FIXTURE_DECISION_MISMATCH", completed.stdout + completed.stderr)
        reports = [json.loads(line) for line in completed.stdout.splitlines() if line.strip()]
        outcomes = [report["outcome"] for report in reports]
        self.assertEqual(outcomes.count("ACCEPT_FOR_WORK"), 2)
        self.assertEqual(outcomes.count("QUARANTINE"), 2)
        self.assertEqual(outcomes.count("HOLD_FOR_REVIEW"), 1)
        self.assertEqual(outcomes.count("DEDUPLICATE"), 2)
        self.assertEqual(outcomes.count("ERROR"), 3)

    def test_primary_identity_precedes_fallback(self) -> None:
        candidate = self._candidate("../flora_occurrence_candidate/expected/gbif_big_bluestem.candidate.json")
        primary = self._peers("peers/primary_duplicate_peers.json")[0]
        fallback = self._peers("peers/fallback_duplicate_peers.json")[0]
        result = MODULE.classify_candidate(candidate, [fallback, primary])
        self.assertEqual(result.outcome, "DEDUPLICATE")
        self.assertEqual(result.decision["duplicate"]["method"], "PRIMARY_INSTITUTION_CATALOG")
        self.assertEqual(result.decision["duplicate"]["duplicate_of_candidate_ref"], primary["candidate_id"])

    def test_peer_order_does_not_change_decision(self) -> None:
        candidate = self._candidate("../flora_occurrence_candidate/expected/gbif_big_bluestem.candidate.json")
        primary = self._peers("peers/primary_duplicate_peers.json")[0]
        fallback = self._peers("peers/fallback_duplicate_peers.json")[0]
        first = MODULE.classify_candidate(candidate, [primary, fallback])
        second = MODULE.classify_candidate(candidate, [fallback, primary])
        self.assertEqual(first.decision, second.decision)

    def test_unknown_and_conditional_license_fail_closed_to_quarantine(self) -> None:
        for fixture, expected_class, expected_reason in (
            ("candidates/missing_license.candidate.json", "UNKNOWN", "LICENSE_MISSING"),
            ("candidates/conditional_license.candidate.json", "RESTRICTED_OR_CONDITIONAL", "LICENSE_REQUIRES_STEWARD_REVIEW"),
        ):
            with self.subTest(fixture=fixture):
                result = MODULE.classify_candidate(self._candidate(fixture), [])
                self.assertEqual(result.outcome, "QUARANTINE")
                self.assertEqual(result.decision["rights"]["license_class"], expected_class)
                self.assertIn(expected_reason, result.decision["rights"]["reason_codes"])
                self.assertEqual(result.decision["decision"]["proposed_target_lifecycle"], "QUARANTINE")

    def test_source_sensitivity_hint_holds_exact_geometry(self) -> None:
        candidate = self._candidate("../flora_occurrence_candidate/expected/idigbio_milkweed.candidate.json")
        result = MODULE.classify_candidate(candidate, [])
        self.assertEqual(result.outcome, "HOLD_FOR_REVIEW")
        self.assertTrue(result.decision["sensitivity"]["exact_geometry_present"])
        self.assertEqual(result.decision["sensitivity"]["disposition"], "GENERALIZE_REQUIRED")
        self.assertFalse(result.decision["governance"]["lifecycle_transition_executed"])

    def test_decisions_never_create_authority(self) -> None:
        decision = json.loads((FIXTURE_ROOT / "expected/accept_open.decision.json").read_text(encoding="utf-8"))
        governance = decision["governance"]
        for field in (
            "source_admission_decided",
            "legal_rights_decided",
            "policy_evaluated",
            "review_completed",
            "lifecycle_transition_executed",
            "promotion_authorized",
            "release_authorized",
            "publication_authorized",
            "public_use_allowed",
        ):
            self.assertIs(governance[field], False)
        self.assertIsNone(governance["release_ref"])

    def test_duplicate_json_and_nonfinite_input_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"object_type":"FloraOccurrenceCandidate","object_type":"FloraOccurrenceCandidate"}', encoding="utf-8")
            result = MODULE.classify_files(duplicate)
            self.assertEqual({item.code for item in result.findings}, {"JSON_DUPLICATE_KEY"})
            nonfinite = Path(directory) / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            result = MODULE.classify_files(nonfinite)
            self.assertEqual({item.code for item in result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        untrusted = "UNTRUSTED_VALUE_DO_NOT_ECHO"
        candidate = self._candidate("../flora_occurrence_candidate/expected/gbif_big_bluestem.candidate.json")
        candidate["candidate_id"] = untrusted
        candidate["spec_hash"] = MODULE.candidate_spec_hash(candidate)
        result = MODULE.classify_candidate(candidate, [])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            report = MODULE.serialize_result(path, result)
        self.assertNotIn(untrusted, report)
        self.assertIn("CANDIDATE_ID_INVALID", report)


if __name__ == "__main__":
    unittest.main()
