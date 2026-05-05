from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--publication-request',type=Path,required=True);p.add_argument('--approver-id',required=True);p.add_argument('--approver-type',default='human');p.add_argument('--decision',choices=['approved','rejected','needs_changes','abstain'],required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.approver_type!='human':raise SystemExit('USDA_PLANTS_PUBLICATION_NON_HUMAN_APPROVAL_REFUSED')
 state='approved' if a.decision=='approved' else a.decision
 o={"schema_version":"1.0.0","object_type":"usda_plants_publication_approval","publication_approval_id":f"kfm.publication_approval.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"publication_request_ref":str(a.publication_request),"approver":{"approver_id":a.approver_id,"approver_type":"human","attestation":a.decision},"decision":a.decision,"decision_reason_codes":[f"USDA_PLANTS_PUBLICATION_{a.decision.upper()}"],"approval_conditions":["No precise coordinates.","No county geometry.","No vector tiles.","Public outputs must carry source attribution."],"publication_state":state,"status":"pass"}
 o['approval_hash']=canonical_hash(o,'approval_hash');validate(ROOT/'schemas/flora/usda_plants_publication_approval.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
