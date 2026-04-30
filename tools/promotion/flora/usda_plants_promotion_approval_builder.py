from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--promotion-request',type=Path,required=True);p.add_argument('--approver-id',required=True);p.add_argument('--approver-type',default='human');p.add_argument('--decision',required=True,choices=['approved','rejected','needs_changes','abstain']);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.approver_type!='human': raise SystemExit('USDA_PLANTS_PROMOTION_NON_HUMAN_APPROVAL_REFUSED')
 reason={'approved':'USDA_PLANTS_PROMOTION_APPROVED','rejected':'USDA_PLANTS_PROMOTION_REJECTED','needs_changes':'USDA_PLANTS_PROMOTION_NEEDS_CHANGES','abstain':'USDA_PLANTS_PROMOTION_ABSTAIN'}[a.decision]
 o={"schema_version":"1.0.0","object_type":"usda_plants_promotion_approval","promotion_approval_id":f"kfm.promotion_approval.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"promotion_request_ref":str(a.promotion_request),"approver":{"approver_id":a.approver_id,"approver_type":"human","attestation":a.decision},"decision":a.decision,"decision_reason_codes":[reason],"approval_conditions":["No publication in this layer.","No writes to published/.","Rollback plan required before execution."],"publication_state":"not_published","promotion_state":a.decision if a.decision!='approved' else 'approved',"status":"pass"}
 o['approval_hash']=canonical_hash(o,'approval_hash');validate(ROOT/'schemas/flora/usda_plants_promotion_approval.schema.json',o);write_json(a.out,o)
if __name__=='__main__': main()
