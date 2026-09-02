from __future__ import annotations
import copy, hashlib, importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[3]
VP=ROOT/'tools/validators/directory_governance/validate_cross_domain_seam_register.py';RP=ROOT/'control_plane/cross_domain_seam_register.yaml'
spec=importlib.util.spec_from_file_location('seams',VP);assert spec and spec.loader
v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)
def load():return yaml.safe_load(RP.read_text())
def write(p,value):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,separators=(',',':'))+'\n')
def codes(r):return {f.code for f in r.findings}
class Tests(unittest.TestCase):
 def candidate(self,value):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);p=root/'candidate.yaml';write(p,value);write(root/'control_plane/domain_lane_register.yaml',{'entries':[{'lane_id':x} for x in v.LANES_FOR_TEST]})
   return v.validate(p,repo_root=root,check_repository=False,check_bindings=False)
 def test_current_projection(self):
  r=v.validate(RP,check_repository=False,check_bindings=False);self.assertTrue(r.ok,r.findings);self.assertEqual(r.outcome,'PASS')
 def test_schema_self_check(self):
  schema=json.loads(v.SCHEMA.read_text());v.Draft202012Validator.check_schema(schema)
 def test_fixture_matrix(self):
  root=ROOT/'fixtures/contracts/v1/governance/cross_domain_seam_register';valid=sorted((root/'valid').glob('*.json'));invalid=sorted(p for p in (root/'invalid').glob('*.json') if p.name!='expected_findings.json');expected=json.loads((root/'invalid/expected_findings.json').read_text())
  self.assertTrue(valid);self.assertTrue(invalid)
  for p in valid:
   with self.subTest(p=p.name):self.assertTrue(self.candidate(json.loads(p.read_text())).ok)
  for p in invalid:
   with self.subTest(p=p.name):self.assertTrue(set(expected[p.name]).issubset(codes(self.candidate(json.loads(p.read_text())))))
 def test_unknown_domain_is_new_drift(self):
  x=load();x['entries'][0]['participants'][0]='invented';r=self.candidate(x);self.assertIn('UNKNOWN_DOMAIN_CONTEXT',codes(r));self.assertEqual(r.outcome,'FAIL_NEW_DRIFT')
 def test_participant_and_seam_identity(self):
  x=load();x['entries'][0]['participants']=list(reversed(x['entries'][0]['participants']));r=self.candidate(x);self.assertIn('PARTICIPANTS_NOT_CANONICAL',codes(r));self.assertIn('SEAM_ID_PARTICIPANT_MISMATCH',codes(r))
 def test_authority_allocation(self):
  x=load();x['entries'][0]['authority_allocations'][0]['context_id']=x['entries'][0]['participants'][1];self.assertIn('AUTHORITY_ALLOCATION_INCOMPLETE',codes(self.candidate(x)))
  x=load();x['entries'][0]['authority_allocations'][0]['may_modify_other_context']=True;self.assertIn('SCHEMA_INVALID',codes(self.candidate(x)))
 def test_trust_defaults_fail_closed(self):
  for key,value in [('source_role_rule','COLLAPSE'),('sensitivity_rule','LEAST_RESTRICTIVE'),('policy_rule','LEAST_RESTRICTIVE'),('release_rule','ONE_PARTICIPANT_ONLY')]:
   with self.subTest(key=key):x=load();x['defaults'][key]=value;self.assertIn('SCHEMA_INVALID',codes(self.candidate(x)))
 def test_public_join_and_status_overclaim(self):
  x=load();x['entries'][0]['public_join_allowed']=True;self.assertIn('SCHEMA_INVALID',codes(self.candidate(x)))
  x=load();x['entries'][0]['status']='ACTIVE';self.assertIn('SCHEMA_INVALID',codes(self.candidate(x)))
 def test_duplicate_and_alias_yaml_denied(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);p=root/'x.yaml';p.write_text('version: v1\nversion: v2\n');self.assertIn('YAML_DUPLICATE_KEY',codes(v.validate(p,repo_root=root,check_repository=False,check_bindings=False)))
   p.write_text('a: &x {}\nb: *x\n');self.assertIn('YAML_ALIAS_DENIED',codes(v.validate(p,repo_root=root,check_repository=False,check_bindings=False)))
 def test_repository_root_drift(self):
  x=load()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);write(root/'control_plane/domain_lane_register.yaml',{'entries':[{'lane_id':q} for q in v.LANES_FOR_TEST]});(root/x['entries'][0]['seam_id']).mkdir();p=root/'candidate.yaml';write(p,x);r=v.validate(p,repo_root=root,check_bindings=False);self.assertIn('UNEXPECTED_SEAM_ROOT',codes(r));self.assertEqual(r.outcome,'FAIL_NEW_DRIFT')
 def test_bindings_detect_drift(self):
  x=load()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);files={'docs/doctrine/directory-rules.md':b'd\n','control_plane/domain_lane_register.yaml':json.dumps({'entries':[{'lane_id':q} for q in v.LANES_FOR_TEST]}).encode()+b'\n','docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md':b'a\n'}
   for rel,raw in files.items():p=root/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
   x['doctrine']['sha256']='sha256:'+hashlib.sha256(files['docs/doctrine/directory-rules.md']).hexdigest();raw=files['control_plane/domain_lane_register.yaml'];x['domain_lane_register']['git_blob']=hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest();p=root/'candidate.yaml';write(p,x);self.assertNotIn('AUTHORITY_DIGEST_MISMATCH',codes(v.validate(p,repo_root=root,check_repository=False)))
   (root/'control_plane/domain_lane_register.yaml').write_text('entries: []\n');self.assertIn('AUTHORITY_DIGEST_MISMATCH',codes(v.validate(p,repo_root=root,check_repository=False)))
 def test_non_echo(self):
  x=load();marker='secret-do-not-echo';x['entries'][0]['participants'][0]=marker
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);p=root/'candidate.yaml';write(p,x);write(root/'control_plane/domain_lane_register.yaml',{'entries':[{'lane_id':q} for q in v.LANES_FOR_TEST]});payload=v.serialize(p,v.validate(p,repo_root=root,check_repository=False,check_bindings=False))
  self.assertNotIn(marker,payload);self.assertIn('UNKNOWN_DOMAIN_CONTEXT',payload)
 def test_cli_deterministic(self):
  command=[sys.executable,str(VP),str(RP),'--no-repository-checks','--no-binding-checks'];a=subprocess.run(command,capture_output=True,text=True);b=subprocess.run(command,capture_output=True,text=True);self.assertEqual(a.returncode,0,a.stdout+a.stderr);self.assertEqual(a.stdout,b.stdout)
if __name__=='__main__':unittest.main()
