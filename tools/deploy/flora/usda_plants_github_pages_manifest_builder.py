from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--deployment-plan-ref',required=True);p.add_argument('--site-bundle-manifest-ref',required=True);p.add_argument('--artifact-path',required=True);p.add_argument('--deploy-to-pages',default='false',choices=['true','false']);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 o={'schema_version':'1.0.0','object_type':'usda_plants_github_pages_deployment_manifest','domain':'flora','source_id':'usda_plants','snapshot_date':a.snapshot_date,'generated_at':a.generated_at,'deployment_manifest_id':f'kfm.deploy.github_pages.flora.usda_plants.{a.snapshot_date}','deployment_plan_ref':a.deployment_plan_ref,'site_bundle_manifest_ref':a.site_bundle_manifest_ref,'artifact_name':'github-pages','artifact_path':a.artifact_path,'environment':'github-pages','required_permissions':{'contents':'read','pages':'write','id-token':'write'},'uses_long_lived_secrets':False,'requires_environment_protection':True,'deploys':a.deploy_to_pages=='true','claims':{'auto_merge':False},'status':'pass','reason_codes':['USDA_PLANTS_GITHUB_PAGES_DEPLOYMENT_MANIFEST_PASS']}
 o['manifest_hash']=canonical_hash(o,'manifest_hash');validate(ROOT/'schemas/flora/usda_plants_github_pages_deployment_manifest.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
