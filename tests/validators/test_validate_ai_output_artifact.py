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
VALIDATOR_PATH = REPO_ROOT / "tools/validators/ai/validate_ai_output_artifact.py"
ARTIFACT_SCHEMA = REPO_ROOT / "schemas/contracts/v1/runtime/ai_output_artifact.schema.json"
BATCH_SCHEMA = REPO_ROOT / "schemas/contracts/v1/runtime/ai_output_batch_manifest.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/runtime/ai_output_artifact"

SPEC = importlib.util.spec_from_file_location("validate_ai_output_artifact", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AIOutputArtifactValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = []
        for path in sorted((FIXTURE_ROOT / "cases").glob("*.json")):
            cls.cases.extend(json.loads(path.read_text(encoding="utf-8"))["cases"])
        cls.by_id = {case["case_id"]: case for case in cls.cases}

    def _payload(self, case_id: str) -> dict[str, object]:
        return copy.deepcopy(self.by_id[case_id]["payload"])

    def test_schemas_are_closed_draft_2020_12_profiles(self) -> None:
        for path, object_type in (
            (ARTIFACT_SCHEMA, "AIOutputArtifact"),
            (BATCH_SCHEMA, "AIOutputBatchManifest"),
        ):
            with self.subTest(path=path.name):
                schema = json.loads(path.read_text(encoding="utf-8"))
                Draft202012Validator.check_schema(schema)
                self.assertFalse(schema["additionalProperties"])
                self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
                self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")
                self.assertEqual(schema["properties"]["object_type"]["const"], object_type)

    def test_all_valid_fixtures_pass(self) -> None:
        cases = [case for case in self.cases if case["expected_outcome"] == "PASS"]
        self.assertEqual(len(cases), 8)
        for case in cases:
            with self.subTest(case=case["case_id"]):
                self.assertTrue(MODULE.validate_payload(case["payload"]).ok)

    def test_manifest_has_exact_reviewed_polarity(self) -> None:
        self.assertEqual(len(self.cases), 26)
        self.assertEqual(len({case["case_id"] for case in self.cases}), len(self.cases))
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                result = MODULE.validate_payload(case["payload"])
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(
                    sorted({finding.code for finding in result.findings}),
                    case["expected_findings"],
                )

    def test_semantic_negative_fixtures_are_schema_valid(self) -> None:
        schemas = {
            "AIOutputArtifact": Draft202012Validator(json.loads(ARTIFACT_SCHEMA.read_text(encoding="utf-8"))),
            "AIOutputBatchManifest": Draft202012Validator(json.loads(BATCH_SCHEMA.read_text(encoding="utf-8"))),
        }
        cases = [
            case for case in self.cases
            if case["case_id"].startswith("semantic-invalid-")
        ]
        self.assertEqual(len(cases), 15)
        for case in cases:
            candidate = case["payload"]
            with self.subTest(case=case["case_id"]):
                self.assertFalse(list(schemas[candidate["object_type"]].iter_errors(candidate)))

    def test_artifact_identity_reproduces_fixture(self) -> None:
        candidate = self._payload("valid-answer-active")
        self.assertEqual(MODULE.compute_artifact_spec_hash(candidate), candidate["spec_hash"])
        self.assertEqual(MODULE.compute_artifact_id(candidate), candidate["artifact_id"])

    def test_batch_identity_and_counts_reproduce_fixture(self) -> None:
        candidate = self._payload("valid-batch-partial-revocation")
        self.assertEqual(MODULE.compute_batch_spec_hash(candidate), candidate["spec_hash"])
        self.assertEqual(MODULE.compute_batch_id(candidate), candidate["manifest_id"])
        self.assertEqual(MODULE._batch_counts(candidate["artifacts"]), candidate["counts"])
        self.assertEqual(MODULE._batch_status(candidate["artifacts"]), "PARTIALLY_REVOKED")

    def test_partial_revocation_preserves_unaffected_artifact_identity(self) -> None:
        active = self._payload("valid-batch-active")
        partial = self._payload("valid-batch-partial-revocation")
        active_by_input = {item["input_ref"]: item for item in active["artifacts"]}
        partial_by_input = {item["input_ref"]: item for item in partial["artifacts"]}
        shared = sorted(set(active_by_input).intersection(partial_by_input))
        self.assertEqual(shared, ["input:synthetic:0001"])
        for input_ref in shared:
            self.assertEqual(active_by_input[input_ref]["artifact_id"], partial_by_input[input_ref]["artifact_id"])
            self.assertEqual(active_by_input[input_ref]["artifact_spec_hash"], partial_by_input[input_ref]["artifact_spec_hash"])
        self.assertNotEqual(active["manifest_id"], partial["manifest_id"])

    def test_negative_outcomes_do_not_expose_result_reference(self) -> None:
        for case_id in ("valid-abstain-active", "valid-deny-active", "valid-error-active"):
            candidate = self._payload(case_id)
            with self.subTest(case=case_id):
                self.assertIsNone(candidate["output"]["result_ref"])
                self.assertIsNone(candidate["output"]["media_type"])

    def test_duplicate_json_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"object_type":"AIOutputArtifact","object_type":"AIOutputArtifact"}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_DUPLICATE_KEY"})

    def test_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"object_type":"AIOutputArtifact","value":NaN}', encoding="utf-8")
            result = MODULE.validate_record(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual({finding.code for finding in result.findings}, {"JSON_NONFINITE_NUMBER"})

    def test_missing_file_is_error(self) -> None:
        result = MODULE.validate_record(REPO_ROOT / "does-not-exist.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual({finding.code for finding in result.findings}, {"FILE_NOT_FOUND"})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        candidate = self._payload("valid-answer-active")
        untrusted = "UNTRUSTED_PRIVATE_VALUE_DO_NOT_ECHO"
        candidate["input"]["input_ref"] = untrusted
        candidate["chain_of_thought"] = untrusted
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            report = MODULE.serialize(path, MODULE.validate_record(path))
        self.assertNotIn(untrusted, report)
        self.assertIn("SCHEMA_INVALID", report)

    def test_fixture_suite_is_no_network_and_deterministic(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first_ok, first_lines = MODULE.validate_fixture_suite()
            second_ok, second_lines = MODULE.validate_fixture_suite()
        self.assertTrue(first_ok)
        self.assertTrue(second_ok)
        self.assertEqual(first_lines, second_lines)
        self.assertEqual(len(first_lines), 26)

    def test_cli_fixture_profile_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 26)
        self.assertNotIn('"suite_match":false', completed.stdout)


if __name__ == "__main__":
    unittest.main()
