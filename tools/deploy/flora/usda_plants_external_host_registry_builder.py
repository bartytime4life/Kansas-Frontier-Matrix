from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--allow-cloudflare',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 o={"schema_version":"1.0.0","object_type":"usda_plants_external_host_registry","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"hosts":[{"host_id":"github_pages","allowed":True,"credential_model":"github_token_oidc"},{"host_id":"cloudflare_pages_guarded","allowed":bool(a.allow_cloudflare),"credential_model":"scoped_environment_secret"}],"reason_codes":["USDA_PLANTS_EXTERNAL_HOST_REGISTRY_BUILT"]}
 o["registry_hash"]=canonical_hash(o,'registry_hash');validate(ROOT/'schemas/flora/usda_plants_external_host_registry.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
