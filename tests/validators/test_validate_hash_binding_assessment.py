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
VALIDATOR = ROOT / "tools/validators/validate_hash_binding_assessment.py"
BASELINE = ROOT / "fixtures/contracts/v1/common/hash_binding_assessment/valid_assessment.json"
CASES = ROOT / "fixtures/contracts/v1/common/hash_binding_assessment/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/common/hash_binding_assessment.schema.json"
MATRIX = ROOT / "control_plane/hash_profile_readiness_matrix.json"
SPEC = importlib.util.spec_from_file_location("validate_hash_binding_assessment", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HashBindingAssessmentTests(unittest.TestCase):
    def test_schema_is_closed_and_valid(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["binding"]["additionalProperties"])
        self.assertFalse(schema["$defs"]["purposeGap"]["additionalProperties"])

    def test_repository_baseline_passes(self) -> None:
        result = MODULE.validate(BASELINE)
        self.assertTrue(result.ok, result.findings)

    def test_bindings_close_exactly_over_readiness_matrix(self) -> None:
        baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
        self.assertEqual(
            [binding["profile_id"] for binding in baseline["bindings"]],
            sorted(profile["profile_id"] for profile in matrix["profiles"]),
        )
        self.assertEqual(baseline["readiness_matrix_spec_hash"], matrix["spec_hash"])
        self.assertEqual(
            [gap["status"] for gap in baseline["purpose_gaps"]],
            ["HOLD_NO_PROFILE", "HOLD_NO_PROFILE"],
        )

    def test_all_authority_effects_are_false(self) -> None:
        baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        self.assertTrue(baseline["authority_effects"])
        self.assertFalse(any(baseline["authority_effects"].values()))

    def test_fixture_manifest_has_exact_polarity(self) -> None:
        cases = json.loads(CASES.read_text(encoding="utf-8"))
        self.assertEqual(len(cases["cases"]), 13)
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR), "--fixtures"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 13)
        self.assertNotIn('"suite_match":false', completed.stdout)

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


if __name__ == "__main__":
    unittest.main()
