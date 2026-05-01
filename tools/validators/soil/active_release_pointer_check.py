import argparse, os,json,sys
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[3]))
from tools.active_release.soil._active_pointer_common import load_json,sha256_file,scan_payload_for_forbidden_terms,scan_payload_for_contact_or_secret_terms

def main():
 p=argparse.ArgumentParser();p.add_argument('--active-root',required=True);p.add_argument('--pointer-transition-id');a=p.parse_args()
 cur=load_json(Path(a.active_root)/'active_release/soil/current_active_release.json')
 tid=a.pointer_transition_id or cur['active_pointer_transition_id']
 t=Path(a.active_root)/'active_release/soil/transitions'/tid
 man=load_json(t/'active_release_pointer_manifest.json'); rec=load_json(t/'active_release_pointer_receipt.json')
 ok=[]
 if man.get('object_type')!='SoilActiveReleasePointerManifest': ok.append('bad manifest')
 if rec.get('receipt_type')!='ActiveReleasePointerReceipt': ok.append('bad receipt')
 for n,h in rec.get('generated_artifacts',{}).items():
  if not (t/n).exists() or sha256_file(t/n)!=h: ok.append('hash mismatch')
 if not rec.get('signatures'): ok.append('missing sig')
 for fn in ['public_active_release_report.json','public_routing_table.json']:
  pl=load_json(t/fn)
  if scan_payload_for_forbidden_terms(pl) or scan_payload_for_contact_or_secret_terms(pl): ok.append('unsafe payload')
 out={"active_release_pointer_valid":not ok,"pointer_transition_id":tid,"lineage_id":man.get('lineage_id'),"prior_release_id":man.get('prior_release_id'),"active_release_id":man.get('active_release_id'),"pointer_state":man.get('pointer_state'),"failure_reasons":ok}
 print(json.dumps(out)); sys.exit(0 if not ok else 1)
if __name__=='__main__': main()
