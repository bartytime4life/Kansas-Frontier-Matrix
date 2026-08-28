from __future__ import annotations

import ast
import copy
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
HASHING_SRC = ROOT / "packages" / "hashing" / "src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import JsonInputError
from tools.validators.evidence import validate_frontier_classification as validator


class FrontierClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixture_manifest()
        cls.raw_cases = {
            item["case_id"]: item for item in cls.manifest["cases"]
        }

    def context(self, case_id: str) -> validator.FixtureContext:
        return validator.materialize_case(self.manifest, self.raw_cases[case_id])

    def result(self, case_id: str) -> validator.Result:
        return validator.validate_context(self.context(case_id))

    def test_fixture_matrix_matches_all_expectations(self) -> None:
        self.assertEqual(validator.fixture_profile(), 0)

    def test_finite_classification_values_and_separate_postures(self) -> None:
        expected = {
            "all_criteria_frontier": ("FRONTIER", "CALCULATED", "REVIEW_CANDIDATE"),
            "all_criteria_not_frontier": (
                "NOT_FRONTIER",
                "CALCULATED",
                "REVIEW_CANDIDATE",
            ),
            "missing_observation_unclassified": ("UNCLASSIFIED", "ABSTAIN", "HOLD"),
        }
        for case_id, triple in expected.items():
            with self.subTest(case_id=case_id):
                context = self.context(case_id)
                self.assertEqual(validator.validate_context(context).outcome, "PASS")
                candidate = context.candidate
                self.assertEqual(
                    (
                        candidate["classification"]["value"],
                        candidate["posture"]["execution"],
                        candidate["posture"]["review"],
                    ),
                    triple,
                )
                self.assertNotIn(
                    candidate["classification"]["value"],
                    {"ANSWER", "ABSTAIN", "DENY", "ERROR"},
                )

    def test_all_and_any_criterion_semantics(self) -> None:
        expected = {
            "all_criteria_frontier": "FRONTIER",
            "all_criteria_not_frontier": "NOT_FRONTIER",
            "any_criterion_frontier": "FRONTIER",
            "any_criterion_not_frontier": "NOT_FRONTIER",
        }
        for case_id, value in expected.items():
            with self.subTest(case_id=case_id):
                context = self.context(case_id)
                self.assertEqual(context.candidate["classification"]["value"], value)
                self.assertEqual(validator.validate_context(context).outcome, "PASS")

    def test_missing_and_suppressed_never_become_not_frontier(self) -> None:
        for case_id in (
            "missing_observation_unclassified",
            "suppressed_observation_unclassified",
            "unresolved_geography_unclassified",
            "missing_crosswalk_unclassified",
        ):
            with self.subTest(case_id=case_id):
                context = self.context(case_id)
                self.assertEqual(
                    context.candidate["classification"]["value"], "UNCLASSIFIED"
                )
                self.assertEqual(context.candidate["posture"]["execution"], "ABSTAIN")
                self.assertEqual(validator.validate_context(context).outcome, "PASS")

    def test_same_version_crosswalk_and_time_alignment(self) -> None:
        same = self.context("same_version_geography_alignment")
        crosswalk = self.context("admitted_crosswalk_alignment")
        year_mismatch = self.context("observation_year_mismatch_unclassified")
        interval_mismatch = self.context("definition_interval_mismatch_unclassified")
        self.assertTrue(
            all(trace["geography_alignment"] == "SAME_VERSION" for trace in same.candidate["criteria"])
        )
        self.assertEqual(crosswalk.candidate["criteria"][0]["geography_alignment"], "CROSSWALK_REFERENCED")
        self.assertEqual(crosswalk.candidate["criteria"][0]["time_alignment"], "ALIGNED")
        self.assertEqual(year_mismatch.candidate["criteria"][0]["time_alignment"], "OUTSIDE_PANEL_YEAR")
        self.assertTrue(
            all(
                trace["time_alignment"] == "OUTSIDE_DEFINITION_INTERVAL"
                for trace in interval_mismatch.candidate["criteria"]
            )
        )

    def test_stale_superseded_withdrawn_and_pending_correction_abstain(self) -> None:
        expected_states = {
            "stale_input_unclassified": "STALE",
            "superseded_input_unclassified": "SUPERSEDED",
            "withdrawn_input_unclassified": "WITHDRAWN",
            "corrected_input_without_current_lineage_unclassified": "CORRECTED_PENDING",
        }
        for case_id, state in expected_states.items():
            with self.subTest(case_id=case_id):
                context = self.context(case_id)
                self.assertIn(state, {trace["observation_state"] for trace in context.candidate["criteria"]})
                self.assertEqual(context.candidate["classification"]["value"], "UNCLASSIFIED")
                self.assertEqual(validator.validate_context(context).outcome, "PASS")

    def test_evidence_uncertainty_and_threshold_mismatches_are_indeterminate(self) -> None:
        cases = (
            "evidence_ref_missing_unclassified",
            "evidence_bundle_identity_mismatch_unclassified",
            "evidence_bundle_member_mismatch_unclassified",
            "uncertainty_missing_unclassified",
            "uncertainty_crosses_threshold_unclassified",
            "uncertainty_exceeds_admitted_width_unclassified",
            "threshold_policy_missing_unclassified",
            "threshold_policy_indicator_mismatch_unclassified",
            "threshold_policy_operator_mismatch_unclassified",
            "threshold_policy_not_admitted_unclassified",
            "source_role_mirror_mismatch_unclassified",
        )
        for case_id in cases:
            with self.subTest(case_id=case_id):
                context = self.context(case_id)
                self.assertEqual(context.candidate["classification"]["value"], "UNCLASSIFIED")
                self.assertEqual(validator.validate_context(context).outcome, "PASS")

    def test_threshold_values_and_observation_values_are_not_copied_into_packet(self) -> None:
        candidate = self.context("all_criteria_frontier").candidate
        serialized = json.dumps(candidate, sort_keys=True)
        self.assertNotIn('"threshold_value"', serialized)
        self.assertNotIn('"observation_value"', serialized)
        self.assertNotIn('"lower"', serialized)
        self.assertNotIn('"upper"', serialized)
        for trace in candidate["criteria"]:
            self.assertNotIn("value", trace)

    def test_dependency_and_output_tampering_are_denied(self) -> None:
        expected_codes = {
            "panel_digest_binding_tamper_denied": "PANEL_BINDING_MISMATCH",
            "definition_digest_binding_tamper_denied": "DEFINITION_BINDING_MISMATCH",
            "classification_result_tamper_denied": "CLASSIFICATION_OUTPUT_MISMATCH",
            "extra_criterion_trace_denied": "CRITERION_TRACE_SET_MISMATCH",
            "missing_criterion_trace_denied": "SCHEMA_INVALID",
            "assessment_id_tamper_denied": "ASSESSMENT_ID_MISMATCH",
            "spec_hash_tamper_denied": "SPEC_HASH_MISMATCH",
        }
        for case_id, code in expected_codes.items():
            with self.subTest(case_id=case_id):
                result = self.result(case_id)
                self.assertEqual(result.outcome, "DENY")
                self.assertIn(code, {finding.code for finding in result.findings})

    def test_generated_at_is_non_identity_metadata(self) -> None:
        first_scenario = copy.deepcopy(self.manifest["base"])
        second_scenario = copy.deepcopy(self.manifest["base"])
        first_scenario["generated_at"] = "2026-08-16T12:00:00Z"
        second_scenario["generated_at"] = "2026-08-17T12:00:00Z"
        first = validator.materialize_scenario(first_scenario).candidate
        second = validator.materialize_scenario(second_scenario).candidate
        self.assertNotEqual(first["metadata"]["generated_at"], second["metadata"]["generated_at"])
        self.assertEqual(first["spec_hash"], second["spec_hash"])
        self.assertEqual(first["assessment_id"], second["assessment_id"])

    def test_correction_preserves_a_distinct_prior_assessment(self) -> None:
        context = self.context("corrected_assessment_preserves_prior")
        self.assertEqual(validator.validate_context(context).outcome, "PASS")
        self.assertIsNotNone(context.prior_assessment)
        assert context.prior_assessment is not None
        self.assertNotEqual(
            context.candidate["assessment_id"],
            context.prior_assessment["assessment_id"],
        )
        self.assertEqual(
            context.candidate["lineage"]["supersedes_assessment_ref"],
            validator._assessment_ref(context.prior_assessment),
        )
        missing = self.result("corrected_assessment_missing_predecessor_denied")
        self.assertEqual(missing.outcome, "DENY")
        self.assertIn(
            "CORRECTION_PREDECESSOR_REQUIRED",
            {finding.code for finding in missing.findings},
        )

    def test_real_subject_and_registry_failure_fail_closed(self) -> None:
        real = self.result("real_subject_attempt_denied")
        self.assertEqual(real.outcome, "DENY")
        self.assertIn("REAL_SUBJECT_DENIED", {finding.code for finding in real.findings})
        registry = self.result("fixture_registry_failure_errors")
        self.assertEqual(registry.outcome, "ERROR")
        self.assertEqual({finding.code for finding in registry.findings}, {"FIXTURE_REGISTRY_ERROR"})

    def test_no_network_or_model_imports_and_execution(self) -> None:
        source = validator.__file__
        assert source is not None
        source_path = Path(source)
        sources = [
            source_path,
            *sorted(source_path.parent.glob("_frontier_classification_*.py")),
        ]
        forbidden_roots = {
            "aiohttp",
            "anthropic",
            "boto3",
            "google",
            "httpx",
            "openai",
            "requests",
            "socket",
            "urllib",
        }
        imported = set()
        for candidate_source in sources:
            tree = ast.parse(candidate_source.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imported.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported.add(node.module.split(".")[0])
        self.assertTrue(imported.isdisjoint(forbidden_roots), imported & forbidden_roots)

        def blocked(*_args, **_kwargs):
            raise AssertionError("network access attempted")

        with mock.patch.object(socket, "socket", side_effect=blocked):
            context = self.context("all_criteria_frontier")
            self.assertEqual(validator.validate_context(context).outcome, "PASS")

    def test_schema_is_valid_and_closed(self) -> None:
        schema = json.loads(validator.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["criterion_trace"]["additionalProperties"])
        self.assertEqual(
            set(schema["$defs"]["classification"]["properties"]["value"]["enum"]),
            {"FRONTIER", "NOT_FRONTIER", "UNCLASSIFIED"},
        )

    def test_duplicate_key_fixture_manifest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            path.write_text('{"base":{},"base":{},"cases":[]}', encoding="utf-8")
            with self.assertRaises((JsonInputError, ValueError)):
                validator.load_fixture_manifest(path)

    def test_cli_case_output_is_bounded(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(validator.__file__),
                "--case",
                "all_criteria_frontier",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["classification"], "FRONTIER")
        self.assertNotIn("registry", payload)
        self.assertNotIn("threshold", payload)


if __name__ == "__main__":
    unittest.main()
