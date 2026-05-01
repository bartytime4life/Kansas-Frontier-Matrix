import json, subprocess, sys
from pathlib import Path
FIX=Path("tests/fixtures/fauna/gbif/valid/review_release")
def test_valid_full_chain_passes(tmp_path):
 q=tmp_path/'q.json'; d=tmp_path/'d.json'; rr=tmp_path/'r.json'; m=tmp_path/'m.json'; g=tmp_path/'g.json'
 subprocess.check_call([sys.executable,'tools/review/fauna/kfm_gbif_review_queue.py','--package',str(FIX/'publication_package.json'),'--status',str(FIX/'publication_status.json'),'--replay-verification',str(FIX/'replay_verification.json'),'--audit-ledger-entry',str(FIX/'audit_ledger_entry.json'),'--output',str(q)])
 subprocess.check_call([sys.executable,'tools/review/fauna/kfm_gbif_review_decision.py','--review-item',str(q),'--decision','approve_publish','--decision-reason','ok','--reviewer','TEST_STEWARD','--reviewer-role','fauna_steward','--output',str(d)])
 subprocess.check_call([sys.executable,'tools/release/fauna/kfm_gbif_release_registry.py','--package',str(FIX/'publication_package.json'),'--status',str(FIX/'publication_status.json'),'--review-decision',str(d),'--release-channel','public','--output',str(rr)])
 subprocess.check_call([sys.executable,'tools/release/fauna/kfm_gbif_public_manifest.py','--release-registry',str(rr),'--package',str(FIX/'publication_package.json'),'--output',str(m)])
 subprocess.check_call([sys.executable,'tools/ci/fauna/kfm_gbif_release_gate.py','--package',str(FIX/'publication_package.json'),'--review-item',str(q),'--review-decision',str(d),'--release-registry',str(rr),'--manifest',str(m),'--output',str(g)])
 assert json.loads(g.read_text())['gate_posture']=='passed'
