import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def run(a): return subprocess.run([sys.executable,*map(str,a)],capture_output=True,text=True)
def test_builder(tmp_path):
 l=tmp_path/'l/lineage/soil';l.mkdir(parents=True);(l/'current_lineage.json').write_text(json.dumps({'lineage_id':'soil-lineage-test'}))
 p=tmp_path/'p/published/soil/receipts';p.mkdir(parents=True);(p/'soil-successor.publication_receipt.json').write_text(json.dumps({'decision':'pass'}))
 a=tmp_path/'a'
 rec=ROOT/'tools/active_release/soil/record_pointer_transition_approval.py';b=ROOT/'tools/active_release/soil/build_active_release_pointer.py';f=ROOT/'tests/fixtures/soil/active_release/approvals/pointer_approval_valid_keep_prior.json'
 assert run([rec,'--lineage-root',tmp_path/'l','--published-root',tmp_path/'p','--active-root',a,'--approval',f]).returncode==0
 args=[b,'--lineage-root',tmp_path/'l','--outcome-root',tmp_path,'--remediation-root',tmp_path,'--corrective-root',tmp_path,'--resolution-root',tmp_path,'--accountability-root',tmp_path,'--assurance-root',tmp_path,'--registry-root',tmp_path,'--certification-root',tmp_path,'--archive-root',tmp_path,'--preservation-root',tmp_path,'--reconciliation-root',tmp_path,'--federation-root',tmp_path,'--discovery-root',tmp_path,'--published-root',tmp_path/'p','--ops-root',tmp_path,'--out-root',a,'--base-public-url','https://example.invalid/kfm/soil']
 r=run(args); assert r.returncode==0
