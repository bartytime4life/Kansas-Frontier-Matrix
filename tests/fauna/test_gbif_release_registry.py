import json, subprocess, sys
from pathlib import Path
FIX=Path("tests/fixtures/fauna/gbif/valid/review_release")
def test_approved_package_registers_release_entry(tmp_path):
 q=tmp_path/'q.json'; d=tmp_path/'d.json'; rr=tmp_path/'r.json'
 subprocess.check_call([sys.executable,'tools/review/fauna/kfm_gbif_review_queue.py','--package',str(FIX/'publication_package.json'),'--status',str(FIX/'publication_status.json'),'--replay-verification',str(FIX/'replay_verification.json'),'--audit-ledger-entry',str(FIX/'audit_ledger_entry.json'),'--output',str(q)])
 subprocess.check_call([sys.executable,'tools/review/fauna/kfm_gbif_review_decision.py','--review-item',str(q),'--decision','approve_publish','--decision-reason','ok','--reviewer','TEST_STEWARD','--reviewer-role','fauna_steward','--output',str(d)])
 subprocess.check_call([sys.executable,'tools/release/fauna/kfm_gbif_release_registry.py','--package',str(FIX/'publication_package.json'),'--status',str(FIX/'publication_status.json'),'--review-decision',str(d),'--release-channel','public','--output',str(rr)])
 assert json.loads(rr.read_text())['release_state']=='published'
