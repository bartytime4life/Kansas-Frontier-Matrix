from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--protected-environment',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args();o={"schema_version":"1.0.0","object_type":"usda_plants_cloudflare_pages_deployment_manifest","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"provider":"cloudflare_pages","deployment_mode":"direct_upload","credential_model":"scoped_environment_secret","secret_names":["CLOUDFLARE_ACCOUNT_ID","CLOUDFLARE_API_TOKEN"],"deploys":False,"protected_environment":a.protected_environment};o['provider_manifest_hash']=canonical_hash(o,'provider_manifest_hash');validate(ROOT/'schemas/flora/usda_plants_cloudflare_pages_deployment_manifest.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
