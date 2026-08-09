import importlib.util, json, sys, unittest
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'tools/validators/ai/validate_ai_evaluator_harness.py'
spec=importlib.util.spec_from_file_location('evalh',P); m=importlib.util.module_from_spec(spec); sys.modules[spec.name]=m; spec.loader.exec_module(m)
class EvaluatorHarnessTests(unittest.TestCase):
 def test_schema(self): Draft202012Validator.check_schema(json.loads(m.SCHEMA.read_text()))
 def test_fixture_replay(self): self.assertEqual([],m.replay())
 def test_fixture_count(self): self.assertEqual(13,len(json.loads(m.FIXTURES.read_text())['cases']))
 def test_pass_requires_allow(self):
  r={'evaluation_id':'x','artifact_kind':'vector','candidate_ref':'c','evidence_refs':['e'],'metrics':[{'name':'m','value':1,'threshold':1,'comparison':'gte'}],'policy_outcome':'HOLD','deterministic':True,'network_access':False,'result':'PASS','reason_codes':[],'spec_hash':'sha256:'+'a'*64}
  self.assertEqual('HOLD',m.evaluate(r))
 def test_network_is_denied(self):
  r={'evaluation_id':'x','artifact_kind':'vector','candidate_ref':'c','evidence_refs':['e'],'metrics':[{'name':'m','value':1,'threshold':1,'comparison':'gte'}],'policy_outcome':'ALLOW','deterministic':True,'network_access':True,'result':'PASS','reason_codes':[],'spec_hash':'sha256:'+'a'*64}
  self.assertEqual('DENY',m.evaluate(r))
 def test_raster_profile_derives_metrics(self):
  r=next(c['record'] for c in json.loads(m.FIXTURES.read_text())['cases'] if c['name']=='public_raster_fail_thresholds')
  metrics,gate,result,codes=m.derive_public(r); self.assertEqual('FAIL',gate); self.assertIn('RASTER_RMSE_EXCEEDED',codes); self.assertEqual(r['metrics'],metrics)
 def test_sensitive_text_denies(self):
  r=next(c['record'] for c in json.loads(m.FIXTURES.read_text())['cases'] if c['name']=='public_text_deny_sensitive')
  self.assertEqual('DENY',m.evaluate(r))
 def test_profile_hash_replays(self):
  r=next(c['record'] for c in json.loads(m.FIXTURES.read_text())['cases'] if c['name']=='public_text_pass')
  self.assertEqual(r['profile_spec_hash'],m.profile_hash(r))
if __name__=='__main__': unittest.main()
