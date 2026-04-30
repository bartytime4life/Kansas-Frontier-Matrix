from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file


def main():
 p=argparse.ArgumentParser();p.add_argument('--deployment-request',type=Path,required=True);p.add_argument('--deployment-approval',type=Path,required=True);p.add_argument('--site-root',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();r=json.loads(a.deployment_request.read_text());ap=json.loads(a.deployment_approval.read_text())
 if ap.get('approval_actor_type')!='human':raise SystemExit('USDA_PLANTS_STATIC_SITE_BUILD_PLAN_NON_HUMAN_APPROVAL')
 o={'schema_version':'1.0.0','object_type':'usda_plants_static_site_build_plan','domain':'flora','source_id':'usda_plants','snapshot_date':r['snapshot_date'],'generated_at':a.generated_at,'plan_id':f"kfm.static_site.plan.flora.usda_plants.{r['snapshot_date']}",'deployment_request_ref':str(a.deployment_request),'deployment_approval_ref':str(a.deployment_approval),'site_root':a.site_root,'inputs':r['artifacts'],'outputs':[f"{a.site_root}/index.html",f"{a.site_root}/manifest.json",f"{a.site_root}/assets/kfm-usda-plants.js",f"{a.site_root}/assets/kfm-usda-plants.css",f"{a.site_root}/static_site_bundle_manifest.json"],'status':'pass','reason_codes':['USDA_PLANTS_STATIC_SITE_BUILD_PLAN_PASS']}
 o['plan_hash']=canonical_hash(o,'plan_hash');validate(ROOT/'schemas/flora/usda_plants_static_site_build_plan.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
