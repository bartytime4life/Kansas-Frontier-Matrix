import json, subprocess, sys
from pathlib import Path
FIX=Path("tests/fixtures/fauna/gbif/valid/review_release")
def test_valid_release_registry_emits_public_manifest(tmp_path):
 rr=tmp_path/'r.json'; m=tmp_path/'m.json'
 # synthetic registry fixture
 rr.write_text(json.dumps({'release_registry_entry_id':'gbif_release_TEST_001','kfm:spec_hash':'sha256:x'}))
 subprocess.check_call([sys.executable,'tools/release/fauna/kfm_gbif_public_manifest.py','--release-registry',str(rr),'--package',str(FIX/'publication_package.json'),'--output',str(m)])
 assert json.loads(m.read_text())['citation_index']
