from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--execution-plan',type=Path,required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();ep=json.loads(a.execution_plan.read_text())
 o={'schema_version':'1.0.0','object_type':'usda_plants_deployment_rollback_plan','domain':'flora','source_id':'usda_plants','snapshot_date':ep['snapshot_date'],'generated_at':a.generated_at,'rollback_plan_id':f"kfm.deploy.rollback.flora.usda_plants.{ep['snapshot_date']}",'execution_plan_ref':str(a.execution_plan),'rollback_steps':['No-op rollback: artifact_only target_host has no remote deployment state.'],'status':'pass','reason_codes':['USDA_PLANTS_DEPLOYMENT_ROLLBACK_PLAN_PASS']}
 o['plan_hash']=canonical_hash(o,'plan_hash');validate(ROOT/'schemas/flora/usda_plants_deployment_rollback_plan.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
