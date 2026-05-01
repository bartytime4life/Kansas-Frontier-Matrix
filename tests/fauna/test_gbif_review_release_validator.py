import json, subprocess, sys
from pathlib import Path
FIX=Path("tests/fixtures/fauna/gbif/valid/review_release")
def test_valid_fixture_validator_ok(tmp_path):
 q=tmp_path/'q.json'
 subprocess.check_call([sys.executable,'tools/review/fauna/kfm_gbif_review_queue.py','--package',str(FIX/'publication_package.json'),'--status',str(FIX/'publication_status.json'),'--replay-verification',str(FIX/'replay_verification.json'),'--audit-ledger-entry',str(FIX/'audit_ledger_entry.json'),'--output',str(q)])
 subprocess.check_call([sys.executable,'tools/validators/fauna/gbif_review_release_validator.py','--kind','review_queue_item','--input',str(q)])
