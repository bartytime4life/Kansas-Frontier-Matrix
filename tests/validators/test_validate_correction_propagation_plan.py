from __future__ import annotations
import importlib.util,json,os,socket,subprocess,sys,tempfile,unittest
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2];TOOL=ROOT/"tools/validators/correction/validate_correction_propagation_plan.py";FIX=ROOT/"fixtures/contracts/v1/correction/correction_propagation_plan/cases.json";SCHEMA=ROOT/"schemas/contracts/v1/correction/correction_propagation_plan.schema.json"
spec=importlib.util.spec_from_file_location("corr",TOOL);M=importlib.util.module_from_spec(spec);sys.modules[spec.name]=M;spec.loader.exec_module(M)
class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.m=json.loads(FIX.read_text());cls.c={x["case_id"]:x for x in cls.m["cases"]}
 def r(self,n):return M.validate_payload(M.materialize_case(self.m,self.c[n]))
 def test_schema(self):Draft202012Validator.check_schema(json.loads(SCHEMA.read_text()))
 def test_polarity(self):
  o=[x["expected_outcome"] for x in self.m["cases"]];self.assertEqual((o.count("PASS"),o.count("ABSTAIN"),o.count("ERROR"),o.count("DENY")),(2,1,1,11))
 def test_cases(self):
  for c in self.m["cases"]:
   with self.subTest(c=c["case_id"]):
    r=self.r(c["case_id"]);self.assertEqual(r.outcome,c["expected_outcome"]);self.assertEqual([{"code":x.code,"path":x.path} for x in r.findings],c["expected_findings"])
 def test_no_network(self):
  old=socket.socket;socket.socket=lambda *_a,**_k:(_ for _ in ()).throw(AssertionError("network"))
  try:
   for c in self.c:self.r(c)
  finally:socket.socket=old
 def test_no_execution_flags(self):
  d=M.materialize_case(self.m,self.c["ready-plan"]);self.assertFalse(any(v for k,v in d["governance"].items() if k!="execution_mode"))
 def test_identity(self):self.assertEqual(M.materialize_case(self.m,self.c["ready-plan"]),M.materialize_case(self.m,self.c["ready-plan"]))
 def test_cli(self):
  d=M.materialize_case(self.m,self.c["ready-plan"])
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/"x.json";p.write_text(json.dumps(d));cp=subprocess.run([sys.executable,str(TOOL),str(p)],cwd=ROOT,capture_output=True,text=True)
  self.assertEqual(cp.returncode,0,cp.stderr)
 def test_fixture_cli(self):self.assertEqual(subprocess.run([sys.executable,str(TOOL),"--fixtures"],cwd=ROOT,capture_output=True,text=True).returncode,0)
if __name__=="__main__":unittest.main()
