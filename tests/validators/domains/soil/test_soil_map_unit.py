from __future__ import annotations
import importlib.util, json, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
VALIDATOR=ROOT/"tools/validators/domains/soil/validate_soil_map_unit.py"
SPEC=importlib.util.spec_from_file_location("soil_map_unit_validator",VALIDATOR)
assert SPEC and SPEC.loader
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)
CASES=json.loads((ROOT/"fixtures/domains/soil/soil_map_unit/cases.json").read_text())["cases"]

class SoilMapUnitTests(unittest.TestCase):
    def test_exact_fixture_matrix(self):
        for row in CASES:
            self.assertEqual(M.evaluate(row["candidate"]),(row["expected_outcome"],row["expected_findings"]),row["name"])
    def test_valid_candidate_is_unreleased_and_nonpublic(self):
        c=CASES[0]["candidate"]
        self.assertEqual(c["release_state"],"UNRELEASED")
        self.assertFalse(c["public_use_allowed"])
        self.assertEqual(c["effects"],M.FALSE_EFFECTS)
    def test_static_map_unit_requires_mukey_key_family(self):
        c=dict(CASES[0]["candidate"]); c["source_native_key_family"]="PARCEL_ID"
        out,find=M.evaluate(c)
        self.assertIn("SOURCE_KEY_FAMILY_MISMATCH",find)
        self.assertIn(out,{"DENY","ERROR"})
    def test_map_unit_cannot_claim_current_condition(self):
        self.assertEqual(CASES[2]["expected_findings"],["CURRENT_CONDITION_OVERCLAIM"])
    def test_map_unit_cannot_claim_parcel_boundary(self):
        self.assertEqual(CASES[1]["expected_findings"],["PARCEL_BOUNDARY_OVERCLAIM"])

if __name__=="__main__": unittest.main()
