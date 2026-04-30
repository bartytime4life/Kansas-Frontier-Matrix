from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--entries',nargs='+',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 o={'schema_version':'1.0.0','object_type':'usda_plants_deployment_audit_ledger','domain':'flora','source_id':'usda_plants','snapshot_date':a.snapshot_date,'generated_at':a.generated_at,'ledger_id':f'kfm.deploy.audit.flora.usda_plants.{a.snapshot_date}','entries':[{'ref':e} for e in a.entries],'status':'pass','reason_codes':['USDA_PLANTS_DEPLOYMENT_AUDIT_LEDGER_PASS']}
 o['ledger_hash']=canonical_hash(o,'ledger_hash');validate(ROOT/'schemas/flora/usda_plants_deployment_audit_ledger.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
