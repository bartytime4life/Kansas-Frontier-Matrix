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

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/policy/validate_policy_transform_plan_simulation.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/policy/policy_transform_plan_simulation.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/policy/policy_transform_plan_simulation"
REDUCTION_FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/policy/policy_obligation_reduction/valid"

SPEC = importlib.util.spec_from_file_location("validate_policy_transform_plan_simulation", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PolicyTransformPlanSimulationValidatorTests(unittest.TestCase):
    def _load(self, relative: str) -> dict[str, object]:
        return json.loads((FIXTURE_ROOT / relative).read_text(encoding="utf-8"))

    def test_schema_is_closed_fixture_only_profile(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")
        self.assertEqual(schema["x-kfm"]["algorithm"], "kfm-policy-transform-plan-dominance-v1")
        self.assertEqual(schema["x-kfm"]["lifecycle_phase"], "PROCESS_TO_CATALOG_SIMULATION")

    def test_all_valid_records_pass_even_when_plan_is_insufficient(self) -> None:
        paths = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertEqual(len(paths), 5)
        outcomes = set()
        for path in paths:
            with self.subTest(path=path.name):
                self.assertTrue(MODULE.validate_record(path).ok)
                outcomes.add(self._load(f"valid/{path.name}")["assessment"]["outcome"])
        self.assertEqual(outcomes, {"SATISFIES", "INSUFFICIENT"})

    def test_manifest_has_exact_reviewed_polarity(self) -> None:
        manifest = self._load("expected_findings_manifest.json")
        cases = manifest["cases"]
        self.assertEqual(manifest["case_count"], 20)
        self.assertEqual(len(cases), 20)
        self.assertEqual(len({case["case_id"] for case in cases}), len(cases))
        for case in cases:
            path = FIXTURE_ROOT / case["record"]
            with self.subTest(case=case["case_id"]):
                result = MODULE.validate_record(path)
                actual_outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
                actual_codes = sorted({finding.code for finding in result.findings})
                self.assertEqual(actual_outcome, case["expected_outcome"])
                self.assertEqual(actual_codes, case["expected_findings"])

    def test_schema_and_semantic_negative_names_do_not_collide(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        schema_invalid = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
        semantic_invalid = sorted((FIXTURE_ROOT / "invalid").glob("semantic_invalid_*.json"))
        self.assertEqual(len(schema_invalid), 5)
        self.assertEqual(len(semantic_invalid), 10)
        for path in schema_invalid:
            self.assertTrue(list(validator.iter_errors(json.loads(path.read_text(encoding="utf-8")))), path.name)
        for path in semantic_invalid:
            self.assertFalse(list(validator.iter_errors(json.loads(path.read_text(encoding="utf-8")))), path.name)

    def test_exact_plan_satisfies(self) -> None:
        candidate = self._load("valid/valid_exact_generalize.json")
        self.assertEqual(MODULE.assess_plan(candidate), {
            "outcome": "SATISFIES", "finding_codes": [], "unmet_dimensions": [],
        })

    def test_stronger_suppress_plan_preserves_every_dimension(self) -> None:
        candidate = self._load("valid/valid_stronger_suppress.json")
        self.assertEqual(MODULE.assess_plan(candidate)["outcome"], "SATISFIES")
        self.assertEqual(candidate["plan"]["record_action"], "SUPPRESS")
        self.assertEqual(candidate["plan"]["generalize_distance_m"], 7500)
        self.assertEqual(candidate["plan"]["date_fuzz_days"], 10000)
        self.assertEqual(candidate["plan"]["embargo_until"], "2040-12-31")

    def test_insufficient_plan_reports_all_dimensions_without_becoming_invalid(self) -> None:
        candidate = self._load("valid/valid_insufficient_multi.json")
        expected = {
            "outcome": "INSUFFICIENT",
            "finding_codes": [
                "TRANSFORM_TOO_WEAK",
                "GENERALIZE_DISTANCE_TOO_SMALL",
                "DATE_FUZZ_TOO_SMALL",
                "GEOMETRY_SUPPRESSION_REQUIRED",
                "EMBARGO_TOO_EARLY",
            ],
            "unmet_dimensions": [
                "TRANSFORM",
                "GENERALIZATION_DISTANCE",
                "DATE_FUZZ",
                "GEOMETRY_SUPPRESSION",
                "EMBARGO",
            ],
        }
        self.assertEqual(MODULE.assess_plan(candidate), expected)
        self.assertTrue(MODULE.validate_record(FIXTURE_ROOT / "valid/valid_insufficient_multi.json").ok)

    def test_assessment_is_order_independent_but_record_canonicality_is_separate(self) -> None:
        candidate = self._load("valid/valid_combined_stronger.json")
        baseline = MODULE.assess_plan(candidate)
        reordered = copy.deepcopy(candidate)
        reordered["source_reduction"]["required"]["reason_codes"].reverse()
        reordered["plan"]["reason_codes"].reverse()
        self.assertEqual(MODULE.assess_plan(reordered), baseline)

    def test_shared_hash_and_simulation_id_reproduce_fixture(self) -> None:
        candidate = self._load("valid/valid_combined_stronger.json")
        self.assertEqual(MODULE.compute_record_spec_hash(candidate), candidate["spec_hash"])
        self.assertEqual(MODULE.compute_simulation_id(candidate), candidate["simulation_id"])
        self.assertRegex(candidate["spec_hash"], r"^sha256:[0-9a-f]{64}$")

    def test_source_reduction_identity_and_result_projection_are_bound(self) -> None:
        candidate = self._load("valid/valid_combined_stronger.json")
        source = candidate["source_reduction"]
        self.assertEqual(
            MODULE.compute_source_reduction_id(source["spec_hash"]),
            source["reduction_id"],
        )
        self.assertEqual(
            MODULE.compute_required_result_spec_hash(source["required"]),
            source["result_spec_hash"],
        )

    def test_source_snapshots_match_landed_reduction_fixtures(self) -> None:
        pairs = {
            "valid_exact_generalize.json": "valid_single_generalize.json",
            "valid_combined_stronger.json": "valid_mixed_maxima.json",
            "valid_stronger_suppress.json": "valid_full_suppress.json",
        }
        for simulation_name, reduction_name in pairs.items():
            with self.subTest(simulation=simulation_name, reduction=reduction_name):
                simulation = self._load(f"valid/{simulation_name}")
                reduction = json.loads(
                    (REDUCTION_FIXTURE_ROOT / reduction_name).read_text(encoding="utf-8")
                )
                source = simulation["source_reduction"]
                self.assertEqual(source["reduction_id"], reduction["reduction_id"])
                self.assertEqual(source["spec_hash"], reduction["spec_hash"])
                self.assertEqual(source["required"], reduction["result"])
                self.assertEqual(
                    source["result_spec_hash"],
                    MODULE.compute_required_result_spec_hash(reduction["result"]),
                )

    def test_duplicate_json_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"object_type":"PolicyTransformPlanSimulation","object_type":"PolicyTransformPlanSimulation"}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertTrue(result.error)
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_DUPLICATE_KEY"})

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertTrue(result.error)
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(REPO_ROOT / "does-not-exist.json")
        self.assertTrue(result.error)
        self.assertEqual({finding.code for finding in result.findings}, {"FILE_NOT_FOUND"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = self._load("valid/valid_exact_generalize.json")
        untrusted = "UNTRUSTED_SUBJECT_VALUE_DO_NOT_ECHO"
        candidate["subject_ref"] = untrusted
        candidate["schema_negative_canary"] = True
        candidate["spec_hash"] = MODULE.compute_record_spec_hash(candidate)
        candidate["simulation_id"] = MODULE.compute_simulation_id(candidate)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            report = MODULE._serialize(path, MODULE.validate_record(path))
        self.assertNotIn(untrusted, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_fixture_suite_and_assessment_cli_are_no_network_and_deterministic(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network access denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network access denied")):
            ok, first_lines = MODULE.validate_fixture_suite()
            second_ok, second_lines = MODULE.validate_fixture_suite()
        self.assertTrue(ok)
        self.assertTrue(second_ok)
        self.assertEqual(first_lines, second_lines)

        suite = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT, check=False, capture_output=True, text=True,
        )
        self.assertEqual(suite.returncode, 0, suite.stdout + suite.stderr)
        self.assertEqual(len(suite.stdout.splitlines()), 20)
        self.assertNotIn('suite_match":false', suite.stdout)

        command = [
            sys.executable, str(VALIDATOR_PATH), "--assess",
            str(FIXTURE_ROOT / "valid/valid_insufficient_multi.json"),
        ]
        first = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn('"outcome":"INSUFFICIENT"', first.stdout)


if __name__ == "__main__":
    unittest.main()
