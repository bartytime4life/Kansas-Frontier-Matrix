from __future__ import annotations
import unittest
from pathlib import Path
from tools.validators.governance.validate_verification_convergence_plan import validate
ROOT=Path(__file__).resolve().parents[3]
FIXTURES=ROOT/'fixtures/contracts/v1/governance/verification_convergence_plan'
class VerificationConvergencePlanTests(unittest.TestCase):
    def test_valid_profiles(self):
        expected={'ready.json':'READY','hold.json':'HOLD'}
        for path in sorted((FIXTURES/'valid').glob('*.json')):
            with self.subTest(path=path.name):
                result=validate(path); self.assertTrue(result.ok); self.assertEqual(result.outcome,expected[path.name])
    def test_invalid_profiles_fail_closed(self):
        expected={'digest-mismatch.json':'PLAN_DIGEST_MISMATCH','over-capacity.json':'SELECTION_CAPACITY_EXCEEDED','unmet-dependency.json':'SELECTED_DEPENDENCY_UNMET','unjustified-priority-skip.json':'DEFER_REASON_REQUIRED'}
        for path in sorted((FIXTURES/'invalid').glob('*.json')):
            with self.subTest(path=path.name):
                result=validate(path); self.assertFalse(result.ok); self.assertEqual(result.outcome,'ERROR'); self.assertIn(expected[path.name],{f.code for f in result.findings})
    def test_profile_never_grants_authority(self):
        for path in FIXTURES.rglob('*.json'):
            text=path.read_text()
            for field in ('authority_created','repository_mutation_allowed','release_authorized','publication_authorized','public_use_allowed'):
                self.assertIn(f'"{field}": false',text)
if __name__=='__main__': unittest.main(verbosity=2)
