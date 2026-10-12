from __future__ import annotations
import importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
VALIDATOR=ROOT/'tools/validators/domains/soil/validate_domain_feature_identity.py'
CASES=ROOT/'fixtures/domains/soil/domain_feature_identity/cases.json'
SCHEMA=ROOT/'schemas/contracts/v1/domains/soil/domain_feature_identity.schema.json'
SPEC=importlib.util.spec_from_file_location('soil_domain_feature_identity_validator',VALIDATOR); assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)
class SoilDomainFeatureIdentityTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.cases=json.loads(CASES.read_text())['cases']; cls.schema=json.loads(SCHEMA.read_text())
 def test_schema_closed_and_inactive(self):
  self.assertFalse(self.schema['additionalProperties']);self.assertEqual(self.schema['properties']['profile']['const'],'kfm.domains.soil.domain-feature-identity.v1');self.assertFalse(self.schema['properties']['public_use_allowed']['const']);self.assertFalse(self.schema['x-kfm']['public_release_authority'])
 def test_exact_fixture_matrix(self):
  for case in self.cases:
   with self.subTest(case=case['name']):self.assertEqual(MODULE.evaluate(case['candidate']),(case['expected_outcome'],case['expected_findings']))
 def test_identity_rule_is_deterministic(self):
  c=self.cases[0]['candidate'];d=MODULE.canonical_hash(c);self.assertEqual(c['spec_hash'],f'sha256:{d}');self.assertEqual(c['id'],f'soil-identity:{d[:24]}')
 def test_support_type_cannot_relabel_object_role(self):
  self.assertIn('SURVEY_FEATURE',MODULE.SUPPORT_ROLES['authoritative_static_soil']);self.assertNotIn('SURVEY_FEATURE',MODULE.SUPPORT_ROLES['satellite_soil_moisture_grid'])
 def test_identity_candidate_cannot_claim_release_or_public_authority(self):
  by={x['name']:x for x in self.cases};self.assertEqual(MODULE.evaluate(by['public_overclaim']['candidate'])[0],'DENY');self.assertEqual(MODULE.evaluate(by['effect_overclaim']['candidate'])[0],'DENY')
if __name__=='__main__':unittest.main()
