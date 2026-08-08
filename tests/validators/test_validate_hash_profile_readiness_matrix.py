from __future__ import annotations
import importlib.util, json, socket, subprocess, sys, unittest
from pathlib import Path
from unittest import mock
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/validate_hash_profile_readiness_matrix.py"
MATRIX = ROOT / "control_plane/hash_profile_readiness_matrix.json"
SCHEMA = ROOT / "schemas/contracts/v1/common/hash_profile_readiness_matrix.schema.json"
CASES = ROOT / "fixtures/contracts/v1/common/hash_profile_readiness_matrix/cases.json"
SPEC = importlib.util.spec_from_file_location("validate_hash_profile_readiness_matrix", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name] = MODULE; SPEC.loader.exec_module(MODULE)

class HashProfileReadinessMatrixTests(unittest.TestCase):
    def test_schema_closed(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8")); Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])

    def test_repository_matrix_passes(self) -> None:
        result = MODULE.validate(MATRIX)
        self.assertTrue(result.ok, result.findings)

    def test_only_spec_hash_is_executable_baseline(self) -> None:
        value = json.loads(MATRIX.read_text(encoding="utf-8"))
        baseline = [p for p in value["profiles"] if p["activation_state"] == "BASELINE"]
        self.assertEqual(len(baseline), 1)
        self.assertEqual(baseline[0]["hash_role"], "spec_hash")
        self.assertEqual(baseline[0]["implementation_state"], "EXECUTABLE")
        range_profile = next(p for p in value["profiles"] if p["hash_role"] == "range_hash")
        self.assertEqual(range_profile["activation_state"], "INACTIVE")
        self.assertEqual(range_profile["implementation_state"], "UNAVAILABLE")

    def test_fixture_manifest_polarity(self) -> None:
        cases = json.loads(CASES.read_text(encoding="utf-8"))
        self.assertEqual(len(cases["cases"]), 6)
        completed = subprocess.run([sys.executable, str(VALIDATOR), "--fixtures"], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 6)
        self.assertNotIn('"suite_match":false', completed.stdout)

    def test_no_network_and_deterministic(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            self.assertEqual(MODULE.validate(MATRIX), MODULE.validate(MATRIX))

if __name__ == "__main__": unittest.main()
