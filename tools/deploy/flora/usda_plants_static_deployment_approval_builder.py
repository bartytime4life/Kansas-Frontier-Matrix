from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file


def main():
 p=argparse.ArgumentParser();p.add_argument('--deployment-request',type=Path,required=True);p.add_argument('--generated-at',required=True);p.add_argument('--approved-by',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();r=json.loads(a.deployment_request.read_text())
 o={'schema_version':'1.0.0','object_type':'usda_plants_static_deployment_approval','domain':'flora','source_id':'usda_plants','snapshot_date':r['snapshot_date'],'generated_at':a.generated_at,'approval_id':f"kfm.static_deploy.approval.flora.usda_plants.{r['snapshot_date']}",'deployment_request_ref':str(a.deployment_request),'decision':'approved','approval_actor_type':'human','approved_by':a.approved_by,'status':'pass','reason_codes':['USDA_PLANTS_STATIC_DEPLOYMENT_APPROVAL_PASS']}
 o['approval_hash']=canonical_hash(o,'approval_hash');validate(ROOT/'schemas/flora/usda_plants_static_deployment_approval.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
