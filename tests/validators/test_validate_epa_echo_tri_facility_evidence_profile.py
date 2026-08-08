from __future__ import annotations
import json, socket, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.validators import validate_epa_echo_tri_facility_evidence_profile as M
class Tests(unittest.TestCase):
    def test_schema_meta_valid(self): M.Draft202012Validator.check_schema(json.loads(M.SCHEMA_PATH.read_text()))
    def test_fixture_suite(self):
        ok,p=M.run_fixture_suite();self.assertTrue(ok,p);self.assertEqual(p["counts"],{"PASS":1,"ABSTAIN":3,"DENY":4,"ERROR":4})
    def test_deterministic(self):
        s=M.load_json_file(M.FIXTURE_PATH);d=M.build_case(s,s["cases"][0]);self.assertEqual(M.validate_document(d),M.validate_document(d))
    def test_no_network(self):
        old=socket.socket;socket.socket=lambda *a,**k: (_ for _ in ()).throw(AssertionError("network"))
        try:self.assertTrue(M.run_fixture_suite()[0])
        finally:socket.socket=old
    def test_input_error_exit(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"bad.json";p.write_text("{");self.assertEqual(M.main([str(p)]),2)
if __name__=="__main__":unittest.main()
