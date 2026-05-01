import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
from tools.deployments.air.lib_air_deploy import J,et
REQ=['deployment_environment.json','static_hosting_manifest.json','delivery_deployment_plan.json','synthetic_probe_spec.json','cache_invalidation_plan.json','deployment_rollback_plan.json','deployment_change_records.jsonl']
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('dirs',nargs='+');a.add_argument('--delivery-dir');a.add_argument('--as-of');x=a.parse_args();rc=0
 all_files=set()
 for dd in x.dirs:
  d=Path(dd)
  for f in d.glob('*'): all_files.add(f.name)
 miss=[f for f in REQ if f not in all_files]
 if miss: print('DENY missing',','.join(miss)); rc=1
 for dd in x.dirs:
  d=Path(dd)
  if x.delivery_dir and (Path(x.delivery_dir)/'static_response_bundle.json').exists():
   b=J(Path(x.delivery_dir)/'static_response_bundle.json'); c=J(Path(x.delivery_dir)/'client_cache_manifest.json'); ce={e['artifact_ref']:e for e in c.get('entries',[])}
   for r in b.get('responses',[]):
    p=Path(x.delivery_dir)/r['response_ref']; s=hashlib.sha256(p.read_bytes()).hexdigest()
    if s!=r.get('sha256') or ce.get(r['response_ref'],{}).get('etag')!=et(s): rc=1; print('DENY',d,'hash/etag mismatch'); break
  print('PASS',d)
 raise SystemExit(rc)
