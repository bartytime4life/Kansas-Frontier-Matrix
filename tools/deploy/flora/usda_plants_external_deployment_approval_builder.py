from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--approver',required=True);p.add_argument('--approver-type',default='human');p.add_argument('--decision',default='approved');p.add_argument('--out',type=Path,required=True);a=p.parse_args();o={"schema_version":"1.0.0","object_type":"usda_plants_external_deployment_approval","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"approver":a.approver,"approver_type":a.approver_type,"decision":a.decision,"usable_by_plan":a.decision=='approved' and a.approver_type=='human'};o['approval_hash']=canonical_hash(o,'approval_hash');validate(ROOT/'schemas/flora/usda_plants_external_deployment_approval.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
