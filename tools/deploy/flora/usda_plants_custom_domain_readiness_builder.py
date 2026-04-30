from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--custom-domain',default=None);p.add_argument('--out',type=Path,required=True);a=p.parse_args();o={"schema_version":"1.0.0","object_type":"usda_plants_custom_domain_readiness","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"custom_domain":a.custom_domain,"dns_change_requested":False,"status":"not_configured"};o['readiness_hash']=canonical_hash(o,'readiness_hash');validate(ROOT/'schemas/flora/usda_plants_custom_domain_readiness.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
