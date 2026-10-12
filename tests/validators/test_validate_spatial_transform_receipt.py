import importlib.util, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/"tools/validators/evidence/validate_spatial_transform_receipt.py"
spec=importlib.util.spec_from_file_location("strv",P)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

class SpatialTransformReceiptTests(unittest.TestCase):
    def test_fixture_replay(self): self.assertEqual([],m.replay())
    def test_identical_refs_denied(self):
        r={"receipt_id":"x","input_ref":"a","output_ref":"a","source_crs":"EPSG:4326","target_crs":"EPSG:5070","operations":["reproject"],"input_digest":"sha256:"+"1"*64,"output_digest":"sha256:"+"2"*64,"changed":True,"evidence_refs":["e"],"network_access":False,"outcome":"PASS","reason_codes":[]}
        self.assertEqual("DENY",m.validate(r))
    def test_error_is_not_pass(self):
        r={"receipt_id":"x","input_ref":"a","output_ref":"b","source_crs":"EPSG:4326","target_crs":"EPSG:5070","operations":["reproject"],"input_digest":"sha256:"+"1"*64,"output_digest":"sha256:"+"2"*64,"changed":True,"evidence_refs":["e"],"network_access":False,"outcome":"ERROR","reason_codes":["TOOL_ERROR"]}
        self.assertEqual("ERROR",m.validate(r))

    def test_cli_exit_code_tracks_outcome(self):
        import json, subprocess, sys, tempfile
        ok={"receipt_id":"x","input_ref":"a","output_ref":"b","source_crs":"EPSG:4326","target_crs":"EPSG:5070","operations":["reproject"],"input_digest":"sha256:"+"1"*64,"output_digest":"sha256:"+"2"*64,"changed":True,"evidence_refs":["e"],"network_access":False,"outcome":"PASS","reason_codes":[]}
        cases={"pass":(json.dumps(ok),"PASS",0),"deny":(json.dumps({**ok,"network_access":True}),"DENY",1),"list_root":("[]","ERROR",1),"truncated":('{"receipt_id": ',"ERROR",1),"missing":(None,"ERROR",1)}
        with tempfile.TemporaryDirectory() as tmp:
            for name,(text,outcome,code) in cases.items():
                path=Path(tmp)/f"{name}.json"
                if text is not None: path.write_text(text,encoding="utf-8")
                with self.subTest(case=name):
                    r=subprocess.run([sys.executable,str(P),str(path)],capture_output=True,text=True,check=False)
                    self.assertNotIn("Traceback",r.stderr)
                    self.assertEqual(outcome,r.stdout.strip())
                    self.assertEqual(code,r.returncode)

if __name__=="__main__": unittest.main()
