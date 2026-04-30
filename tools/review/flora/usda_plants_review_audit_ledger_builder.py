from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; sys.path.insert(0, str(ROOT))
from tools.quality.flora.usda_common import canonical_hash, write_json, validate, sha256_file

def main():
 p=argparse.ArgumentParser();
 for n in ['release-candidate','review-decision','sensitivity-review','rights-attestation']:
  p.add_argument(f'--{n}',type=Path,required=True)
 p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 items=[('001','release_candidate',a.release_candidate),('002','review_decision',a.review_decision),('003','sensitivity_review',a.sensitivity_review),('004','rights_attestation',a.rights_attestation)]
 entries=[]
 for eid,etype,path in items:
  if not path.exists(): raise SystemExit('USDA_PLANTS_LEDGER_REF_MISSING')
  if 'published/' in str(path): raise SystemExit('USDA_PLANTS_LEDGER_REF_UNDER_PUBLISHED')
  entries.append({'entry_id':eid,'entry_type':etype,'ref':str(path),'sha256':sha256_file(path),'status':'recorded'})
 o={'schema_version':'1.0.0','object_type':'usda_plants_review_audit_ledger','ledger_id':f'kfm.review_audit_ledger.flora.usda_plants.{a.snapshot_date}','domain':'flora','source_id':'usda_plants','snapshot_date':a.snapshot_date,'generated_at':a.generated_at,'entries':sorted(entries,key=lambda e:e['entry_id']),'publication_state':'not_published','promotion_state':'not_promoted','status':'pass','reason_codes':['USDA_PLANTS_LEDGER_HASH_RECORDED']}
 o['ledger_hash']=canonical_hash(o,'ledger_hash'); validate(ROOT/'schemas/flora/usda_plants_review_audit_ledger.schema.json',o); write_json(a.out,o)
if __name__=='__main__': main()
