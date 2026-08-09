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

if __name__=="__main__": unittest.main()
