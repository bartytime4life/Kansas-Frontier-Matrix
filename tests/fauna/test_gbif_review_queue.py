import json, subprocess, sys
from pathlib import Path
FIX=Path("tests/fixtures/fauna/gbif/valid/review_release")
def test_valid_publication_package_creates_review_queue_item(tmp_path):
 o=tmp_path/'q.json'
 subprocess.check_call([sys.executable,'tools/review/fauna/kfm_gbif_review_queue.py','--package',str(FIX/'publication_package.json'),'--status',str(FIX/'publication_status.json'),'--replay-verification',str(FIX/'replay_verification.json'),'--audit-ledger-entry',str(FIX/'audit_ledger_entry.json'),'--output',str(o)])
 d=json.loads(o.read_text()); assert d['publication_package_id']=='gbif_pubpkg_TEST_001'
