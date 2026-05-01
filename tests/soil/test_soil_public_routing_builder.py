import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def run(cmd): return subprocess.run([str(x) for x in cmd],capture_output=True,text=True)

def setup_all(tmp):
 fix=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'
 c=tmp/'c'; p=tmp/'p'; l=tmp/'l'; a=tmp/'a'; r=tmp/'r'
 assert run([sys.executable,ROOT/'tools/catalog/soil/build_catalog.py','--receipt',fix,'--out-root',c]).returncode==0
 assert run([sys.executable,ROOT/'tools/publish/soil/build_release.py','--catalog-root',c,'--out-root',p,'--release-id','soil-test-release']).returncode==0
 (l/'lineage/soil').mkdir(parents=True); (l/'lineage/soil/current_lineage.json').write_text(json.dumps({'lineage_id':'soil-lineage-test'}))
 appr=ROOT/'tests/fixtures/soil/active_release/approvals/pointer_approval_valid_keep_prior.json'
 assert run([sys.executable,ROOT/'tools/active_release/soil/record_pointer_transition_approval.py','--lineage-root',l,'--published-root',p,'--active-root',a,'--approval',appr]).returncode==0
 args=[sys.executable,ROOT/'tools/active_release/soil/build_active_release_pointer.py','--lineage-root',l,'--outcome-root',tmp,'--remediation-root',tmp,'--corrective-root',tmp,'--resolution-root',tmp,'--accountability-root',tmp,'--assurance-root',tmp,'--registry-root',tmp,'--certification-root',tmp,'--archive-root',tmp,'--preservation-root',tmp,'--reconciliation-root',tmp,'--federation-root',tmp,'--discovery-root',tmp,'--published-root',p,'--ops-root',tmp,'--out-root',a,'--pointer-transition-id','soil-active-pointer-test','--base-public-url','https://example.invalid/kfm/soil']
 assert run(args).returncode==0
 return p,l,a,r

def test_builder_and_check(tmp_path):
 p,l,a,r=setup_all(tmp_path)
 ap=ROOT/'tests/fixtures/soil/routing/approvals/route_activation_approval_valid_active.json'
 assert run([sys.executable,ROOT/'tools/routing/soil/record_route_activation_approval.py','--active-root',a,'--published-root',p,'--routing-root',r,'--approval',ap]).returncode==0
 b=[sys.executable,ROOT/'tools/routing/soil/build_public_routing.py','--active-root',a,'--lineage-root',l,'--outcome-root',tmp_path,'--remediation-root',tmp_path,'--corrective-root',tmp_path,'--resolution-root',tmp_path,'--accountability-root',tmp_path,'--assurance-root',tmp_path,'--registry-root',tmp_path,'--certification-root',tmp_path,'--archive-root',tmp_path,'--preservation-root',tmp_path,'--reconciliation-root',tmp_path,'--federation-root',tmp_path,'--discovery-root',tmp_path,'--published-root',p,'--ops-root',tmp_path,'--out-root',r,'--base-public-url','https://example.invalid/kfm/soil','--routing-id','soil-routing-test']
 rb=run(b); assert rb.returncode==0
 rc=run([sys.executable,ROOT/'tools/validators/soil/public_routing_check.py','--routing-root',r,'--routing-id','soil-routing-test']); assert rc.returncode==0
