import json, subprocess, sys
from pathlib import Path
FIX=Path("tests/fixtures/fauna/gbif/valid/review_release")
def test_valid_scoped_rights_exception_emits_receipt(tmp_path):
 o=tmp_path/'e.json'
 subprocess.check_call([sys.executable,'tools/review/fauna/kfm_gbif_exception_receipt.py','--package',str(FIX/'publication_package.json'),'--exception-type','rights_exception','--allowed-effect','allow_public_release','--reason','x','--reviewer','TEST_STEWARD','--reviewer-role','fauna_steward','--output',str(o)])
 assert json.loads(o.read_text())['scope']['dataset_keys']==['TEST_DATASET_KEY']
