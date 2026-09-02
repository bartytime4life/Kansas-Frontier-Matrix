from __future__ import annotations
import importlib.util, json, socket, subprocess, sys, unittest
from pathlib import Path
from unittest import mock
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/validate_source_intake_record.py"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_intake_record"
INTAKE_SCHEMA = ROOT / "schemas/contracts/v1/source/source_intake_record.schema.json"
DRIFT_SCHEMA = ROOT / "schemas/contracts/v1/source/drift_summary.schema.json"
SPEC = importlib.util.spec_from_file_location("validate_source_intake_record", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name] = MODULE; SPEC.loader.exec_module(MODULE)

class SourceIntakeRecordTests(unittest.TestCase):
    def test_schemas_are_closed_and_well_formed(self) -> None:
        for path in (INTAKE_SCHEMA, DRIFT_SCHEMA):
            schema = json.loads(path.read_text(encoding="utf-8")); Draft202012Validator.check_schema(schema)
            self.assertFalse(schema["additionalProperties"])

    def test_fixture_manifest_polarity(self) -> None:
        manifest = json.loads((FIXTURES / "expected_findings_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["cases"]), 7)
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = MODULE.validate(FIXTURES / case["input"])
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(sorted({f.code for f in result.findings}), case["expected_findings"])

    def test_candidate_delta_is_downstream_only(self) -> None:
        valid = MODULE.validate(FIXTURES / "valid/valid_proposed_work_record.json")
        invalid = MODULE.validate(FIXTURES / "semantic_invalid/semantic_candidate_delta_on_no_change.json")
        self.assertTrue(valid.ok)
        self.assertIn("CANDIDATE_DELTA_DISPOSITION_INVALID", {f.code for f in invalid.findings})

    def test_direct_publication_is_rejected(self) -> None:
        result = MODULE.validate(FIXTURES / "invalid/invalid_direct_publish.json")
        self.assertFalse(result.ok)
        self.assertEqual({f.code for f in result.findings}, {"SCHEMA_INVALID"})

    def test_legacy_placeholders_are_read_only_pointers(self) -> None:
        for name, canonical in (("source-intake-record.json", "source_intake_record.schema.json"), ("drift-summary.json", "drift_summary.schema.json")):
            value = json.loads((ROOT / "schemas/contracts/v1/source" / name).read_text(encoding="utf-8"))
            self.assertEqual(value["status"], "DEPRECATED_COMPATIBILITY_POINTER")
            self.assertFalse(value["writes_allowed"])
            self.assertTrue((ROOT / value["canonical_schema"]).is_file())
            self.assertTrue(value["canonical_schema"].endswith(canonical))

    def test_no_network_and_deterministic_cli(self) -> None:
        path = FIXTURES / "valid/valid_proposed_work_record.json"
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            self.assertEqual(MODULE.validate(path), MODULE.validate(path))
        completed = subprocess.run([sys.executable, str(VALIDATOR), "--fixtures"], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 7)
        self.assertNotIn('"suite_match":false', completed.stdout)

if __name__ == "__main__": unittest.main()
