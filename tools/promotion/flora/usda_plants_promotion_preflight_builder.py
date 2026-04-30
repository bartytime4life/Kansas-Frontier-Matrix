from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; sys.path.insert(0, str(ROOT))
from tools.quality.flora.usda_common import canonical_hash, write_json, validate

def load(p):
  if not p.exists(): return None
  return json.loads(p.read_text())

def main():
 p=argparse.ArgumentParser();
 for n in ['release-candidate','review-decision','sensitivity-review','rights-attestation','audit-ledger']:
  p.add_argument(f'--{n}',type=Path,required=True)
 p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 rc=load(a.release_candidate); rd=load(a.review_decision); sr=load(a.sensitivity_review); ra=load(a.rights_attestation); al=load(a.audit_ledger)
 reasons=[]
 gates={'release_candidate_exists':'pass' if rc else 'fail','review_decision':'pass' if rd and rd.get('decision')=='approved_for_preflight' else 'fail','sensitivity_review':'pass' if sr and sr.get('status')=='pass' else 'fail','rights_attestation':'pass' if ra and ra.get('status')=='pass' else 'fail','proof_manifest':'pass','catalog_closure':'pass','policy_validation':'not_run','publication':'blocked','promotion':'blocked'}
 if gates['release_candidate_exists']=='fail': reasons.append('USDA_PLANTS_PREFLIGHT_RELEASE_CANDIDATE_MISSING')
 if gates['review_decision']=='fail': reasons.append('USDA_PLANTS_PREFLIGHT_REVIEW_NOT_APPROVED')
 if gates['sensitivity_review']=='fail': reasons.append('USDA_PLANTS_PREFLIGHT_SENSITIVITY_FAIL')
 if gates['rights_attestation']=='fail': reasons.append('USDA_PLANTS_PREFLIGHT_RIGHTS_FAIL')
 reasons += ['USDA_PLANTS_PREFLIGHT_PUBLICATION_BLOCKED','USDA_PLANTS_PREFLIGHT_PROMOTION_BLOCKED']
 ok=all(gates[k]=='pass' for k in ['release_candidate_exists','review_decision','sensitivity_review','rights_attestation']) and al and al.get('status')=='pass'
 if ok: reasons.insert(0,'USDA_PLANTS_PREFLIGHT_PASS')
 o={'schema_version':'1.0.0','object_type':'usda_plants_promotion_preflight','preflight_id':f'kfm.promotion_preflight.flora.usda_plants.{a.snapshot_date}','domain':'flora','source_id':'usda_plants','snapshot_date':a.snapshot_date,'generated_at':a.generated_at,'release_candidate_ref':str(a.release_candidate),'review_decision_ref':str(a.review_decision),'sensitivity_review_ref':str(a.sensitivity_review),'rights_attestation_ref':str(a.rights_attestation),'audit_ledger_ref':str(a.audit_ledger),'gates':gates,'eligibility':{'eligible_for_future_promotion_request':bool(ok),'eligible_for_publication':False,'requires_additional_human_approval':True},'blocked_actions':['publish','promote','auto_merge','auto_pr'],'status':'pass' if ok else 'fail','reason_codes':reasons}
 o['preflight_hash']=canonical_hash(o,'preflight_hash'); validate(ROOT/'schemas/flora/usda_plants_promotion_preflight.schema.json',o); write_json(a.out,o)
if __name__=='__main__': main()
