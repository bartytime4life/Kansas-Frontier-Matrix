#!/usr/bin/env python
import argparse,json,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--out-dir');p.add_argument('--as-of');a=p.parse_args()
ok=True
for d in a.dirs:
 for f in Path(d).rglob('*.json'):
  t=f.read_text(errors='ignore').lower()
  if any(x in t for x in ['data/published/air/','data/raw/','data/work/','data/quarantine/','data/processed/air/','secret','token']): ok=False
if a.out_dir:
 Path(a.out_dir).mkdir(parents=True,exist_ok=True)
 Path(a.out_dir,'reentry_release_candidate_audit_report.json').write_text(json.dumps({'schema_version':'1.0.0','audit_id':'audit-001','domain':'atmosphere.air','result':'pass' if ok else 'deny'},indent=2)+'\n')
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
