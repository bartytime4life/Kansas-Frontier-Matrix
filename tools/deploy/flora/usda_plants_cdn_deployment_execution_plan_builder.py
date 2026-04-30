from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--site-bundle-manifest',type=Path,required=True);p.add_argument('--request',type=Path,required=True);p.add_argument('--approval',type=Path,required=True);p.add_argument('--protected-environment',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args();req=json.loads(a.request.read_text());ap=json.loads(a.approval.read_text());refs=[str(a.site_bundle_manifest)];rc=[]
 if not req.get('target_host_id'): rc.append('USDA_PLANTS_EXTERNAL_DEPLOY_HOST_NOT_ALLOWED')
 if ap.get('usable_by_plan')!=True: rc.append('USDA_PLANTS_EXTERNAL_DEPLOY_APPROVAL_MISSING')
 if not a.protected_environment: rc.append('USDA_PLANTS_EXTERNAL_DEPLOY_UNPROTECTED_ENV')
 for r in refs:
  if '/raw/' in r: rc.append('USDA_PLANTS_EXTERNAL_DEPLOY_RAW_REF_LEAK')
  if '/work/' in r: rc.append('USDA_PLANTS_EXTERNAL_DEPLOY_WORK_REF_LEAK')
  if '/quarantine/' in r: rc.append('USDA_PLANTS_EXTERNAL_DEPLOY_QUARANTINE_REF_LEAK')
 o={"schema_version":"1.0.0","object_type":"usda_plants_cdn_deployment_execution_plan","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"dry_run":True,"deploys":False,"protected_environment":a.protected_environment,"site_bundle_manifest_ref":str(a.site_bundle_manifest),"auto_merge":False,"reason_codes":sorted(set(rc)) or ["USDA_PLANTS_EXTERNAL_DEPLOY_PLAN_READY"]};o['plan_hash']=canonical_hash(o,'plan_hash');validate(ROOT/'schemas/flora/usda_plants_cdn_deployment_execution_plan.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
