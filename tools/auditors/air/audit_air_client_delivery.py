#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
import importlib.util
vp=Path(__file__).resolve().parents[2]/'validators/air/validate_air_client_delivery.py'
spec=importlib.util.spec_from_file_location('v',vp);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);vcheck=m.check

def J(p): return json.loads(Path(p).read_text())
def snap(d):
 m={}
 for p in sorted(Path(d).rglob('*.json')): m[str(p.relative_to(d))]=hashlib.sha256(p.read_bytes()).hexdigest()
 return m
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('dirs',nargs='+');a.add_argument('--source-read-model-dir');a.add_argument('--as-of');a.add_argument('--out-dir');x=a.parse_args();
 rc=0
 ss=snap(x.source_read_model_dir) if x.source_read_model_dir else None
 for d in x.dirs:
  d=Path(d); r={'schema_version':'v1','audit_id':'audit-1','domain':'atmosphere.air','generated_at':x.as_of or '2026-04-30T00:00:00Z','as_of':x.as_of or '2026-04-30T00:00:00Z','delivery_manifest_ref':'client_delivery_manifest.json','checks':[],'hash_checks':[],'route_checks':[],'cache_checks':[],'delta_cursor_checks':[],'path_safety_checks':[],'semantic_checks':[],'result':'pass'}
  if vcheck(d)!=0: r['result']='deny'; rc=1
  if ss and ss!=snap(x.source_read_model_dir): r['result']='deny'; r['checks'].append('source mutated'); rc=1
  od=Path(x.out_dir) if x.out_dir else d
  od.mkdir(parents=True,exist_ok=True); (od/'client_delivery_audit_report.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
  print(('PASS' if r['result']=='pass' else 'DENY'),d)
 raise SystemExit(rc)
