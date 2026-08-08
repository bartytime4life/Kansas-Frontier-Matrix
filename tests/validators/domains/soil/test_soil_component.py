from __future__ import annotations
import importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
VALIDATOR=ROOT/"tools/validators/domains/soil/validate_soil_component.py"
SPEC=importlib.util.spec_from_file_location("soil_component_validator",VALIDATOR)
assert SPEC and SPEC.loader
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)
CASES=json.loads((ROOT/"fixtures/domains/soil/soil_component/cases.json").read_text())["cases"]
class SoilComponentTests(unittest.TestCase):
    def test_exact_fixture_matrix(self):
        for row in CASES:
            self.assertEqual(M.evaluate(row["candidate"]),(row["expected_outcome"],row["expected_findings"]),row["name"])
    def test_component_stays_inside_map_unit_boundary(self):
        self.assertEqual(CASES[2]["expected_findings"],["MAP_UNIT_REF_MISSING"])
    def test_component_percent_is_bounded(self):
        self.assertEqual(CASES[1]["expected_findings"],["COMPONENT_PERCENT_INVALID"])
    def test_observation_support_cannot_masquerade_as_component(self):
        self.assertEqual(CASES[3]["expected_findings"],["SUPPORT_TYPE_INVALID"])
    def test_valid_component_has_no_authority_effects(self):
        c=CASES[0]["candidate"]
        self.assertFalse(c["public_use_allowed"])
        self.assertFalse(any(c["effects"].values()))
if __name__=="__main__": unittest.main()
