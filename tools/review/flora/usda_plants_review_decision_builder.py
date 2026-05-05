from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; sys.path.insert(0, str(ROOT))
from tools.quality.flora.usda_common import canonical_hash, write_json, validate

REASON = {"approved_for_preflight":"USDA_PLANTS_REVIEW_APPROVED_FOR_PREFLIGHT","rejected":"USDA_PLANTS_REVIEW_REJECTED","needs_changes":"USDA_PLANTS_REVIEW_NEEDS_CHANGES","abstain":"USDA_PLANTS_REVIEW_ABSTAIN"}

def main():
    p=argparse.ArgumentParser();
    p.add_argument('--release-candidate',type=Path,required=True);p.add_argument('--change-alert',type=Path,required=True);p.add_argument('--reviewer-queue',type=Path,required=True);p.add_argument('--pr-handoff',type=Path,required=True)
    p.add_argument('--reviewer-id',required=True);p.add_argument('--reviewer-type',default='human',choices=['human','system']);p.add_argument('--decision',required=True,choices=list(REASON));p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args(); refs=[a.release_candidate,a.change_alert,a.reviewer_queue,a.pr_handoff]
    missing=[str(x) for x in refs if not x.exists()]
    if a.decision=='approved_for_preflight' and a.reviewer_type!='human': raise SystemExit('USDA_PLANTS_REVIEW_NON_HUMAN_APPROVAL_REFUSED')
    if missing: raise SystemExit('USDA_PLANTS_REVIEW_SCOPE_INCOMPLETE: '+';'.join(missing))
    o={"schema_version":"1.0.0","object_type":"usda_plants_review_decision","review_decision_id":f"kfm.review_decision.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"reviewer":{"reviewer_id":a.reviewer_id,"reviewer_type":a.reviewer_type,"attestation":"reviewed"},"review_scope":{"release_candidate_ref":str(a.release_candidate),"change_alert_ref":str(a.change_alert),"reviewer_queue_ref":str(a.reviewer_queue),"pr_handoff_ref":str(a.pr_handoff)},"decision":a.decision,"decision_reason_codes":[REASON[a.decision]],"conditions":["No publication requested.","No promotion requested.","Promotion-preflight only."],"blocked_actions":["publish","promote","auto_merge","auto_pr"],"publication_state":"not_published","promotion_state":"not_promoted","status":"pass"}
    o['decision_hash']=canonical_hash(o,'decision_hash'); validate(ROOT/'schemas/flora/usda_plants_review_decision.schema.json',o); write_json(a.out,o)
if __name__=='__main__': main()
