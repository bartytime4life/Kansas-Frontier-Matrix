from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();o={"schema_version":"1.0.0","object_type":"usda_plants_cache_invalidation_plan","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"dry_run":True,"purges_cache":False};o['cache_plan_hash']=canonical_hash(o,'cache_plan_hash');validate(ROOT/'schemas/flora/usda_plants_cache_invalidation_plan.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
