from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--site-bundle-manifest',type=Path,required=True);p.add_argument('--provider-manifest',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();rc=[]
 for pth,c in ((a.site_bundle_manifest,'USDA_PLANTS_EXTERNAL_DEPLOY_SITE_BUNDLE_MISSING'),(a.provider_manifest,'USDA_PLANTS_EXTERNAL_DEPLOY_PROVIDER_MANIFEST_MISSING')):
  if not pth.exists(): rc.append(c)
 o={"schema_version":"1.0.0","object_type":"usda_plants_external_deployment_verification_report","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"mode":"local_dry_run","passed":not rc,"reason_codes":rc or ["USDA_PLANTS_EXTERNAL_DEPLOY_VERIFIED"]};o['verification_hash']=canonical_hash(o,'verification_hash');validate(ROOT/'schemas/flora/usda_plants_external_deployment_verification_report.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
