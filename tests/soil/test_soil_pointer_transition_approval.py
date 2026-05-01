import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def prep(tmp):
 p=tmp/'p/published/soil/receipts';p.mkdir(parents=True)
 (p/'soil-successor.publication_receipt.json').write_text(json.dumps({'decision':'pass'}))
 l=tmp/'l/lineage/soil';l.mkdir(parents=True);(l/'current_lineage.json').write_text(json.dumps({'lineage_id':'soil-lineage-test'}))
 return tmp/'l', tmp/'p', tmp/'a'

def run(args): return subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)

def test_valid_and_invalid(tmp_path):
 l,p,a=prep(tmp_path)
 s=ROOT/'tools/active_release/soil/record_pointer_transition_approval.py';f=ROOT/'tests/fixtures/soil/active_release/approvals'
 assert run([s,'--lineage-root',l,'--published-root',p,'--active-root',a,'--approval',f/'pointer_approval_valid_keep_prior.json']).returncode==0
 assert run([s,'--lineage-root',l,'--published-root',p,'--active-root',a,'--approval',f/'pointer_approval_invalid_missing_review.json']).returncode!=0
