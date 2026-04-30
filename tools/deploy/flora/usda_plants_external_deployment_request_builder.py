from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--registry',type=Path,required=True);p.add_argument('--target-host-id',required=True);p.add_argument('--requester',required=True);p.add_argument('--requester-type',default='human');p.add_argument('--out',type=Path,required=True);a=p.parse_args();r=json.loads(a.registry.read_text())
 allowed=False
 for h in r.get('hosts',[]):
  if h['host_id']==a.target_host_id: allowed=h.get('allowed',False)
 rc=[]
 if a.requester_type!='human': rc.append('USDA_PLANTS_EXTERNAL_DEPLOY_NON_HUMAN_REQUESTER')
 if not allowed: rc.append('USDA_PLANTS_EXTERNAL_DEPLOY_HOST_NOT_ALLOWED')
 o={"schema_version":"1.0.0","object_type":"usda_plants_external_deployment_request","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"requester":a.requester,"requester_type":a.requester_type,"target_host_id":a.target_host_id,"reviewable":True,"reason_codes":rc or ["USDA_PLANTS_EXTERNAL_DEPLOY_REQUEST_READY"]}
 o['request_hash']=canonical_hash(o,'request_hash');validate(ROOT/'schemas/flora/usda_plants_external_deployment_request.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
