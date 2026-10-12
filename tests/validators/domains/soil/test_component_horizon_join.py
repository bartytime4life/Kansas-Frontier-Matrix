from __future__ import annotations
import importlib.util, json, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
VALIDATOR=ROOT/"tools/validators/domains/soil/validate_component_horizon_join.py"
SPEC=importlib.util.spec_from_file_location("component_horizon_join_validator",VALIDATOR)
assert SPEC and SPEC.loader
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)
CASES=json.loads((ROOT/"fixtures/domains/soil/component_horizon_join/cases.json").read_text())["cases"]

class ComponentHorizonJoinTests(unittest.TestCase):
    def test_exact_fixture_matrix(self):
        for row in CASES:
            self.assertEqual(M.evaluate(row["candidate"]),(row["expected_outcome"],row["expected_findings"]),row["name"])
    def test_valid_join_is_inactive_and_unreleased(self):
        c=CASES[0]["candidate"]
        self.assertEqual(c["status"],"PROPOSED_INACTIVE")
        self.assertEqual(c["release_state"],"UNRELEASED")
        self.assertFalse(c["public_use_allowed"])
        self.assertEqual(c["effects"],M.FALSE_EFFECTS)
    def test_join_requires_mukey_cokey_chkey(self):
        self.assertEqual(CASES[1]["expected_findings"],["SOURCE_NATIVE_KEYS_INCOMPLETE"])
    def test_join_rejects_observation_support(self):
        self.assertEqual(CASES[2]["expected_findings"],["SUPPORT_TYPE_INVALID"])
    def test_join_does_not_persist_or_publish(self):
        self.assertFalse(any(CASES[0]["candidate"]["effects"].values()))

if __name__=="__main__": unittest.main()
