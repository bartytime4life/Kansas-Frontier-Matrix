import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.routing.soil._public_routing_common import load_json,sha256_file


def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('--routing-root',required=True);p.add_argument('--routing-id');a=p.parse_args(argv)
 root=Path(a.routing_root)/'routing/soil'; cur=load_json(root/'current_public_routing.json'); rid=a.routing_id or cur['active_routing_id']; d=root/'routes'/rid
 try:
  man=load_json(d/'public_routing_manifest.json'); r=load_json(d/'public_routing_receipt.json'); pol=load_json(d/'route_policy_matrix.json'); cut=load_json(d/'route_cutover_simulation.json'); ver=load_json(d/'route_verification_report.json')
 except Exception:
  print(json.dumps({'public_routing_valid':False,'routing_id':rid,'failure_reasons':['missing artifact']})); return 1
 fails=[]
 if man.get('object_type')!='SoilPublicRoutingManifest': fails.append('bad manifest type')
 if r.get('receipt_type')!='PublicRoutingReceipt': fails.append('bad receipt')
 for k,h in r.get('generated_artifacts',{}).items():
  if k=='public_routing_manifest.json':
   continue
  if sha256_file(d/k)!=h: fails.append('hash mismatch'); break
 if any(x.get('status')!='pass' for x in pol.get('policies',[]) if x.get('required')): fails.append('policy fail')
 if not cut.get('simulation_passed'): fails.append('simulation fail')
 if not ver.get('verification_passed'): fails.append('verification fail')
 out={'public_routing_valid':not fails,'routing_id':rid,'pointer_transition_id':man.get('pointer_transition_id'),'prior_release_id':man.get('prior_release_id'),'active_release_id':man.get('active_release_id'),'routing_state':man.get('routing_state'),'failure_reasons':fails}
 print(json.dumps(out)); return 0 if not fails else 1
if __name__=='__main__': raise SystemExit(main())