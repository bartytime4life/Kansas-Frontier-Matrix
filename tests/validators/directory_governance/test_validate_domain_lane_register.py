from __future__ import annotations
import copy, hashlib, importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
VP=ROOT/'tools/validators/directory_governance/validate_domain_lane_register.py';RP=ROOT/'control_plane/domain_lane_register.yaml'
spec=importlib.util.spec_from_file_location('dlr',VP);assert spec and spec.loader
v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)
def load():return json.loads(RP.read_text())
def write(p,value):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,separators=(',',':'))+'\n')
def codes(r):return {f.code for f in r.findings}
class Tests(unittest.TestCase):
 def candidate(self,value):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'x.yaml';write(p,value);return v.validate(p,check_repository=False,check_bindings=False)
 def test_current(self):
  r=v.validate(RP,check_repository=False,check_bindings=False);self.assertTrue(r.ok,r.findings);self.assertEqual(r.outcome,'PASS')
 def test_schema(self):
  s=json.loads(v.SCHEMA.read_text());v.Draft202012Validator.check_schema(s)
 def test_lane_set(self):
  x=load();x['lanes']=x['lanes'][:-1];r=self.candidate(x);self.assertIn('CANONICAL_LANE_MISSING',codes(r));self.assertEqual(r.outcome,'FAIL_NEW_DRIFT')
  x=load();e=copy.deepcopy(x['lanes'][0]);e.update(lane_id='invented',display_name='Invented',documentation_path='docs/domains/invented/',code_alias='invented');x['lanes'].append(e);x['lanes'].sort(key=lambda z:z['lane_id']);self.assertIn('UNEXPECTED_DOMAIN_LANE',codes(self.candidate(x)))
 def test_order_path_alias(self):
  x=load();x['lanes']=list(reversed(x['lanes']));self.assertIn('LANES_NOT_CANONICAL',codes(self.candidate(x)))
  x=load();x['lanes'][0]['documentation_path']='docs/domains/wrong/';self.assertIn('DOCUMENTATION_PATH_MISMATCH',codes(self.candidate(x)))
  x=load();x['lanes'][0]['code_alias']='wrong';self.assertIn('CODE_ALIAS_MISMATCH',codes(self.candidate(x)))
 def test_owner_overclaim(self):
  x=load();x['lane_defaults']['owner_identity']='@invented';self.assertIn('OWNER_IDENTITY_OVERCLAIM',codes(self.candidate(x)))
 def test_cross_cutting_and_aliases(self):
  x=load();x['cross_cutting_exclusions'].pop();self.assertIn('CROSS_CUTTING_SET_MISMATCH',codes(self.candidate(x)))
  x=load();x['unresolved_aliases']['air']='invented';self.assertIn('ALIAS_SET_MISMATCH',codes(self.candidate(x)))
 def test_duplicate_json(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'x.yaml';p.write_text('{"version":"v1","version":"v2"}\n');self.assertIn('JSON_DUPLICATE_KEY',codes(v.validate(p,check_repository=False,check_bindings=False)))
 def test_repository(self):
  x=load()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)
   for lane in x['lanes']:(root/lane['documentation_path']).mkdir(parents=True)
   self.assertTrue(v.validate(RP,repo_root=root,check_bindings=False).ok)
   (root/'hydrology').mkdir();r=v.validate(RP,repo_root=root,check_bindings=False);self.assertIn('DOMAIN_ROOT_PRESENT',codes(r));self.assertEqual(r.outcome,'FAIL_NEW_DRIFT')
 def test_missing_docs_holds(self):
  x=load()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)
   for lane in x['lanes'][1:]:(root/lane['documentation_path']).mkdir(parents=True)
   r=v.validate(RP,repo_root=root,check_bindings=False)
  self.assertIn('DOMAIN_DOCUMENTATION_MISSING',codes(r));self.assertEqual(r.outcome,'HOLD_UNRESOLVED')
 def test_bindings(self):
  x=load()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);files={'docs/doctrine/directory-rules.md':b'd\n','docs/registers/DOMAIN_LANE.md':b'n\n','control_plane/root_registry.yaml':b'{}\n','docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md':b'a\n'}
   for rel,raw in files.items():p=root/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
   x['doctrine']['sha256']='sha256:'+hashlib.sha256(files['docs/doctrine/directory-rules.md']).hexdigest()
   for key,rel in [('narrative_register','docs/registers/DOMAIN_LANE.md'),('root_registry','control_plane/root_registry.yaml')]:raw=files[rel];x[key]['git_blob']=hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()
   p=root/'x.yaml';write(p,x);self.assertNotIn('AUTHORITY_DIGEST_MISMATCH',codes(v.validate(p,repo_root=root,check_repository=False)))
   (root/'docs/registers/DOMAIN_LANE.md').write_text('changed\n');self.assertIn('AUTHORITY_DIGEST_MISMATCH',codes(v.validate(p,repo_root=root,check_repository=False)))
 def test_non_echo(self):
  x=load();marker='@secret-do-not-echo';x['lane_defaults']['owner_identity']=marker
  with tempfile.TemporaryDirectory() as d:p=Path(d)/'x.yaml';write(p,x);payload=v.serialize(p,v.validate(p,check_repository=False,check_bindings=False))
  self.assertNotIn(marker,payload);self.assertIn('OWNER_IDENTITY_OVERCLAIM',payload)
 def test_cli_deterministic(self):
  c=[sys.executable,str(VP),str(RP),'--no-repository-checks','--no-binding-checks'];a=subprocess.run(c,capture_output=True,text=True);b=subprocess.run(c,capture_output=True,text=True);self.assertEqual(a.returncode,0);self.assertEqual(a.stdout,b.stdout)
if __name__=='__main__':unittest.main()
