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
NORMALIZER_PATH = REPO_ROOT / "packages/domains/flora/normalizers/dwc_occurrence.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/flora/flora_occurrence_candidate.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/flora/flora_occurrence_candidate"

SPEC = importlib.util.spec_from_file_location("flora_dwc_normalizer_under_test", NORMALIZER_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FloraDwcOccurrenceNormalizerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema, format_checker=FormatChecker())
        cls.manifest = json.loads((FIXTURE_ROOT / "expected_outcomes.json").read_text(encoding="utf-8"))

    def test_schema_is_closed_proposed_draft_2020_12(self) -> None:
        self.assertFalse(self.schema["additionalProperties"])
        self.assertEqual(self.schema["x-kfm"]["status"], "PROPOSED")
        self.assertEqual(self.schema["x-kfm"]["authority"], "work_stage_normalization_candidate_only")

    def test_expected_candidates_match_exact_normalizer_output_and_schema(self) -> None:
        normalized = [case for case in self.manifest["cases"] if case["outcome"] == "NORMALIZED"]
        self.assertEqual(len(normalized), 3)
        for case in normalized:
            with self.subTest(input=case["input"]):
                result = MODULE.normalize_file(
                    FIXTURE_ROOT / case["input"],
                    source_profile=case["source_profile"],
                    source_id=case["source_id"],
                )
                expected = json.loads((FIXTURE_ROOT / case["expected_candidate"]).read_text(encoding="utf-8"))
                self.assertEqual(result.outcome, "NORMALIZED")
                self.assertEqual(result.candidate, expected)
                self.assertEqual(list(self.validator.iter_errors(result.candidate)), [])
                self.assertEqual(result.candidate["spec_hash"], MODULE.candidate_spec_hash(result.candidate))

    def test_negative_fixtures_match_exact_outcomes_and_findings(self) -> None:
        negative = [case for case in self.manifest["cases"] if case["outcome"] != "NORMALIZED"]
        self.assertEqual(len(negative), 5)
        for case in negative:
            with self.subTest(input=case["input"]):
                result = MODULE.normalize_file(
                    FIXTURE_ROOT / case["input"],
                    source_profile=case["source_profile"],
                    source_id=case["source_id"],
                )
                self.assertEqual(result.outcome, case["outcome"])
                self.assertIsNone(result.candidate)
                self.assertEqual(sorted({item.code for item in result.findings}), sorted(case["findings"]))

    def test_fixture_cli_replays_exact_profile(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(NORMALIZER_PATH), "--fixtures", str(FIXTURE_ROOT)],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertNotIn("FIXTURE_POLARITY_ERROR", completed.stdout + completed.stderr)
        self.assertNotIn("FIXTURE_CANDIDATE_MISMATCH", completed.stdout + completed.stderr)
        self.assertEqual(completed.stdout.count('"outcome":"NORMALIZED"'), 3)
        self.assertEqual(completed.stdout.count('"outcome":"ABSTAIN"'), 2)
        self.assertEqual(completed.stdout.count('"outcome":"ERROR"'), 3)

    def test_governance_is_fixed_to_work_and_non_authority(self) -> None:
        candidate = json.loads(
            (FIXTURE_ROOT / "expected/gbif_big_bluestem.candidate.json").read_text(encoding="utf-8")
        )
        governance = candidate["governance"]
        self.assertEqual(governance["lifecycle_state"], "WORK")
        for field in (
            "source_admitted",
            "evidence_bundle_resolved",
            "policy_evaluated",
            "review_completed",
            "promotion_authorized",
            "release_authorized",
            "publication_authorized",
            "public_use_allowed",
        ):
            self.assertIs(governance[field], False)
        self.assertIsNone(governance["release_ref"])
        self.assertEqual(candidate["source_context"]["source_role"], "OBSERVATION_CANDIDATE")
        self.assertEqual(candidate["spatial"]["coordinate_exposure"], "INTERNAL_EXACT")

    def test_candidate_identity_is_stable_and_source_scoped(self) -> None:
        record = json.loads((FIXTURE_ROOT / "input/gbif_big_bluestem.json").read_text(encoding="utf-8"))
        first = MODULE.normalize_record(record, source_profile="GBIF_DWC", source_id="gbif")
        second = MODULE.normalize_record(record, source_profile="GBIF_DWC", source_id="gbif")
        other_source = MODULE.normalize_record(record, source_profile="GBIF_DWC", source_id="other")
        self.assertEqual(first.candidate, second.candidate)
        self.assertNotEqual(first.candidate["candidate_id"], other_source.candidate["candidate_id"])

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"key":1,"key":2,"scientificName":"Synthetic"}', encoding="utf-8")
            result = MODULE.normalize_file(path, source_profile="GBIF_DWC", source_id="gbif")
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_DUPLICATE_KEY"})

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"key":1,"scientificName":"Synthetic","decimalLongitude":NaN,"decimalLatitude":1}', encoding="utf-8")
            result = MODULE.normalize_file(path, source_profile="GBIF_DWC", source_id="gbif")
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_unsupported_profile_and_empty_source_abstain(self) -> None:
        record = {"key": 1, "scientificName": "Synthetic plant"}
        result = MODULE.normalize_record(record, source_profile="UNKNOWN", source_id=" ")
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"SOURCE_ID_MISSING", "SOURCE_PROFILE_UNSUPPORTED"},
        )

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        untrusted = "UNTRUSTED_VALUE_DO_NOT_ECHO"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps({"scientificName": untrusted}), encoding="utf-8")
            result = MODULE.normalize_file(path, source_profile="GBIF_DWC", source_id="gbif")
            report = MODULE.serialize_result(path, result)
        self.assertNotIn(untrusted, report)
        self.assertIn("SOURCE_RECORD_ID_MISSING", report)


if __name__ == "__main__":
    unittest.main()
