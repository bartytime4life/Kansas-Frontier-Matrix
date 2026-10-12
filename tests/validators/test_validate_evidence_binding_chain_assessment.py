from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/validate_evidence_binding_chain_assessment.py"
SCHEMA = ROOT / "schemas/contracts/v1/evidence/evidence_binding_chain_assessment.schema.json"
BASELINE = ROOT / "fixtures/contracts/v1/evidence/evidence_binding_chain_assessment/valid_assessment.json"
CASES = ROOT / "fixtures/contracts/v1/evidence/evidence_binding_chain_assessment/cases.json"
SPEC = importlib.util.spec_from_file_location("validate_evidence_binding_chain_assessment", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class EvidenceBindingChainAssessmentTests(unittest.TestCase):
    def test_schema_is_closed_and_meta_valid(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["parseResult"]["additionalProperties"])
        self.assertFalse(schema["$defs"]["evidenceResolution"]["additionalProperties"])

    def test_repository_baseline_passes(self) -> None:
        result = MODULE.validate(BASELINE)
        self.assertEqual(result.outcome, "PASS", result.findings)

    def test_baseline_closes_exact_references_without_bundle(self) -> None:
        value = json.loads(BASELINE.read_text(encoding="utf-8"))
        artifact_ref = value["source_artifact"]["artifact_id"]
        parse_ref = value["parse_result"]["parse_result_ref"]
        evidence_ref = value["evidence_ref"]["ref"]
        self.assertEqual(value["parse_result"]["source_artifact_ref"], artifact_ref)
        self.assertEqual(value["evidence_resolution"]["source_artifact_ref"], artifact_ref)
        self.assertEqual(value["evidence_resolution"]["parse_result_ref"], parse_ref)
        self.assertEqual(value["claim_field_binding"]["source_artifact_ref"], artifact_ref)
        self.assertEqual(value["evidence_resolution"]["evidence_ref"], evidence_ref)
        self.assertEqual(value["claim_field_binding"]["evidence_ref"], evidence_ref)
        self.assertNotIn("bundle_ref", value["evidence_ref"])
        self.assertIsNone(value["evidence_bundle_ref"])

    def test_executable_parse_result_model_is_exercised(self) -> None:
        value = json.loads(BASELINE.read_text(encoding="utf-8"))
        model = MODULE._parse_result_model(value["parse_result"])
        self.assertEqual(model.outcome.value, "PARSED")
        self.assertEqual(model.record_count, 1)
        self.assertFalse(model.evidence_created)
        self.assertFalse(model.publication_authorized)

    def test_fixture_manifest_has_exact_finite_outcomes(self) -> None:
        cases = json.loads(CASES.read_text(encoding="utf-8"))
        self.assertEqual(len(cases["cases"]), 17)
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR), "--fixtures"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        rows = [json.loads(line) for line in completed.stdout.splitlines()]
        self.assertEqual(len(rows), 17)
        self.assertEqual({row["outcome"] for row in rows}, {"PASS", "ABSTAIN", "DENY", "ERROR"})
        self.assertTrue(all(row["suite_match"] for row in rows))

    def test_all_authority_effects_are_false(self) -> None:
        value = json.loads(BASELINE.read_text(encoding="utf-8"))
        self.assertEqual(value["effects"], MODULE.FALSE_EFFECTS)
        self.assertFalse(value["public_use_allowed"])
        self.assertIsNone(value["release_ref"])

    def test_deterministic_with_network_denied(self) -> None:
        with (
            mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")),
            mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")),
        ):
            self.assertEqual(MODULE.validate(BASELINE), MODULE.validate(BASELINE))

    def test_fixture_replay_has_no_candidate_file_write(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        self.assertNotIn(".fixture-candidate", source)
        self.assertNotIn("write_text(", source)
        self.assertNotIn("write_bytes(", source)


if __name__ == "__main__":
    unittest.main()
