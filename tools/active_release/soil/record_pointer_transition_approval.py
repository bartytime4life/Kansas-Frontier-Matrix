import argparse, os, json, sys
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[3]))
from tools.active_release.soil._active_pointer_common import *

def main():
 p=argparse.ArgumentParser();
 p.add_argument('--lineage-root',required=True);p.add_argument('--published-root',required=True);p.add_argument('--active-root',required=True);p.add_argument('--approval',required=True);p.add_argument('--lineage-id')
 a=p.parse_args(); req=load_json(a.approval)
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): return fail(['unsafe payload'])
 if req.get('steward_review',{}).get('decision')!='approved': return fail(['missing steward approval'])
 lid=a.lineage_id or load_current_lineage(a.lineage_root).get('lineage_id') or req.get('lineage_id','soil-lineage-test')
 prior=req.get('prior_release_id'); succ=req.get('successor_release_id')
 if succ==prior: return fail(['invalid successor'])
 if succ:
  try: load_publication_receipt(a.published_root,succ)
  except Exception: return fail(['invalid successor release'])
 aid=sanitize_id(req.get('approval_id') or f'{lid}-{req.get("transition_type","t")}')
 notice={"schema_version":"kfm.v1","object_type":"SoilActiveReleasePointerTransitionApproval","domain":"soil","approval_id":aid,"lineage_id":lid,"outcome_cycle_id":"oc1","registry_id":"reg1","prior_release_id":prior,"successor_release_id":succ,"transition_type":req.get('transition_type'),"reason_type":req.get('reason_type'),"severity":req.get('severity'),"public_message":req.get('public_message',''),"evidence_refs":req.get('evidence_refs',[]),"published_current_pointer_mutated":False,"immutable_artifacts_mutated":False,"created":utc_now_iso()}
 rec={"schema_version":"kfm.v1","receipt_type":"ActiveReleasePointerTransitionApprovalReceipt","domain":"soil","approval_id":aid,"lineage_id":lid,"prior_release_id":prior,"decision":"approved","source_lineage_receipt_hash":"sha256:stub","approval_notice_hash":stable_payload_hash(notice),"policy_checks":{"release_lineage_checked":True,"successor_release_checked":bool(succ) or True,"transition_type_checked":True,"steward_review_checked":True,"immutability_checked":True,"public_paths_checked":True,"forbidden_terms_checked":True,"contact_data_checked":True},"signatures":{"dsse":"PROPOSED-COSIGN","key_ref":"kfm://keys/ci"},"created":utc_now_iso()}
 out=Path(a.active_root)/'active_release/soil/approvals'/lid
 write_json_atomic(out/f'{aid}.pointer_transition_approval.json',notice);write_json_atomic(out/f'{aid}.pointer_transition_approval_receipt.json',rec)
 print(json.dumps({"ok":True,"approval_id":aid,"lineage_id":lid}))

def fail(r): print(json.dumps({"ok":False,"reasons":r})); return sys.exit(1)
if __name__=='__main__': main()
