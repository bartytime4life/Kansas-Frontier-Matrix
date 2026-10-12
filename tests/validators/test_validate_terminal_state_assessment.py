from __future__ import annotations
import importlib.util, json, os, socket, subprocess, sys, tempfile, unittest
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2]
TOOL=ROOT/"tools/validators/governance/validate_terminal_state_assessment.py"; FIX=ROOT/"fixtures/contracts/v1/governance/terminal_state_assessment/cases.json"; SCHEMA=ROOT/"schemas/contracts/v1/governance/terminal_state_assessment.schema.json"
spec=importlib.util.spec_from_file_location("terminal_validator",TOOL); M=importlib.util.module_from_spec(spec); sys.modules[spec.name]=M; spec.loader.exec_module(M)
class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.manifest=json.loads(FIX.read_text()); cls.cases={c["case_id"]:c for c in cls.manifest["cases"]}
 def result(self,c): return M.validate_payload(M.materialize_case(self.manifest,self.cases[c]))
 def test_schema(self): Draft202012Validator.check_schema(json.loads(SCHEMA.read_text()))
 def test_polarity(self):
  outcomes=[c["expected_outcome"] for c in self.manifest["cases"]]; self.assertEqual((outcomes.count("PASS"),outcomes.count("ABSTAIN"),outcomes.count("DENY")),(3,3,8))
 def test_all_cases(self):
  for c in self.manifest["cases"]:
   with self.subTest(c=c["case_id"]):
    r=self.result(c["case_id"]); self.assertEqual(r.outcome,c["expected_outcome"]); self.assertEqual([{"code":x.code,"path":x.path} for x in r.findings],c["expected_findings"])
 def test_identity_deterministic(self): self.assertEqual(M.materialize_case(self.manifest,self.cases["draft-within-ceiling"]),M.materialize_case(self.manifest,self.cases["draft-within-ceiling"]))
 def test_no_network(self):
  old=socket.socket; socket.socket=lambda *_a,**_k: (_ for _ in ()).throw(AssertionError("network denied"))
  try:
   for c in self.cases: self.result(c)
  finally: socket.socket=old
 def test_diagnostics_do_not_echo_values(self):
  r=self.result("head-sha-mismatch"); s=M.serialize(None,r); self.assertNotIn("cccccccc",s); self.assertIn("TERMINAL_HEAD_SHA_MISMATCH",s)
 def test_cli(self):
  d=M.materialize_case(self.manifest,self.cases["draft-within-ceiling"])
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/"x.json"; p.write_text(json.dumps(d)); env=os.environ.copy(); env["KFM_NO_NETWORK"]="1"; cp=subprocess.run([sys.executable,str(TOOL),str(p)],cwd=ROOT,env=env,capture_output=True,text=True)
  self.assertEqual(cp.returncode,0,cp.stderr); self.assertIn('"outcome":"PASS"',cp.stdout)
 def test_fixture_cli(self):
  cp=subprocess.run([sys.executable,str(TOOL),"--fixtures"],cwd=ROOT,capture_output=True,text=True); self.assertEqual(cp.returncode,0,cp.stderr)
if __name__=="__main__": unittest.main()
