from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def load(p:Path): return json.loads(p.read_text())

def rel(out_root:Path,p:Path)->str:
    return p.resolve().relative_to(out_root.resolve()).as_posix()

def main():
 p=argparse.ArgumentParser();p.add_argument('--release-candidate',type=Path,required=True);p.add_argument('--promotion-preflight',type=Path,required=True);p.add_argument('--review-audit-ledger',type=Path,required=True);p.add_argument('--requester-id',required=True);p.add_argument('--requester-type',default='human');p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.requester_type!='human': raise SystemExit('USDA_PLANTS_PROMOTION_REQUEST_NON_HUMAN_REFUSED')
 pre=load(a.promotion_preflight)
 if pre.get('status')!='pass': raise SystemExit('USDA_PLANTS_PROMOTION_REQUEST_PREFLIGHT_NOT_PASS')
 if not pre.get('eligibility',{}).get('eligible_for_future_promotion_request'): raise SystemExit('USDA_PLANTS_PROMOTION_REQUEST_NOT_ELIGIBLE')
 out_root=a.out.parents[5]
 o={"schema_version":"1.0.0","object_type":"usda_plants_promotion_request","promotion_request_id":f"kfm.promotion_request.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"requested_by":{"requester_id":a.requester_id,"requester_type":"human"},"scope":{"release_candidate_ref":rel(out_root,a.release_candidate),"promotion_preflight_ref":rel(out_root,a.promotion_preflight),"review_audit_ledger_ref":rel(out_root,a.review_audit_ledger)},"intent":"promote_internal_package","target_stage":"promoted_package","publication_state":"not_published","promotion_state":"requested","blocked_actions":["publish","auto_merge","public_map_release","public_tile_generation"],"conditions":["Promotion-preflight must be pass.","Publication remains blocked.","Human promotion approval required."],"status":"requested","reason_codes":["USDA_PLANTS_PROMOTION_REQUESTED"]}
 o['request_hash']=canonical_hash(o,'request_hash');validate(ROOT/'schemas/flora/usda_plants_promotion_request.schema.json',o);write_json(a.out,o)
if __name__=='__main__': main()
