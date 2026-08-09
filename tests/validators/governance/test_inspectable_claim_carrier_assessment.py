import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
PATH = ROOT / "tools/validators/governance/validate_inspectable_claim_carrier_assessment.py"
SPEC = importlib.util.spec_from_file_location("claim_carrier_validator", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)

class InspectableClaimCarrierAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.base = json.loads((MODULE.FIXTURES / "valid.json").read_text(encoding="utf-8"))
    def test_valid_fixture_passes(self): self.assertEqual(MODULE.validate(self.base), ("PASS", []))
    def test_missing_evidence_denies(self):
        item = copy.deepcopy(self.base); item["evidence_bundle_ref"] = ""; item["assessment_id"] = MODULE.expected_id(item)
        self.assertEqual(MODULE.validate(item)[0], "DENY")
    def test_public_carrier_requires_correction_states(self):
        item = copy.deepcopy(self.base); item["negative_states"] = ["ABSTAIN","DENY","ERROR","STALE"]; item["assessment_id"] = MODULE.expected_id(item)
        self.assertIn("PUBLIC_CORRECTION_STATE_MISSING", MODULE.validate(item)[1])
    def test_authority_overreach_denies(self):
        item = copy.deepcopy(self.base); item["effects"]["publishes"] = True; item["assessment_id"] = MODULE.expected_id(item)
        self.assertEqual(MODULE.validate(item)[0], "DENY")
    def test_identity_drift_errors(self):
        item = copy.deepcopy(self.base); item["assessment_id"] = "kfm:claim-carrier:" + "0" * 64
        self.assertEqual(MODULE.validate(item), ("ERROR", ["IDENTITY_MISMATCH"]))
    def test_fixture_matrix(self): self.assertEqual(MODULE.run_fixtures(), 0)

if __name__ == "__main__": unittest.main()
