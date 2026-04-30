from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--site-bundle-manifest',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 o={'schema_version':'1.0.0','object_type':'usda_plants_deployment_execution_plan','domain':'flora','source_id':'usda_plants','snapshot_date':a.snapshot_date,'generated_at':a.generated_at,'execution_plan_id':f'kfm.deploy.exec.flora.usda_plants.{a.snapshot_date}','target_host':'artifact_only','site_bundle_manifest_ref':str(a.site_bundle_manifest),'status':'pass','reason_codes':['USDA_PLANTS_DEPLOYMENT_EXECUTION_PLAN_PASS']}
 o['plan_hash']=canonical_hash(o,'plan_hash');validate(ROOT/'schemas/flora/usda_plants_deployment_execution_plan.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
