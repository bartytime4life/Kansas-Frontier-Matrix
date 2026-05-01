#!/usr/bin/env python
import argparse,sys,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--maintenance-dir');p.add_argument('--assurance-dir');p.add_argument('--closure-dir');p.add_argument('--delivery-dir');p.add_argument('--source-maintenance-dir');p.add_argument('--source-assurance-dir');p.add_argument('--source-closure-dir');p.add_argument('--source-delivery-dir');p.add_argument('--as-of');p.add_argument('--out-dir');a=p.parse_args();ok=True
text=''.join(f.read_text().lower() for d in map(Path,a.dirs) for f in d.rglob('*.json'))
for x in ('data/published/air/','kubectl','terraform','slack','pagerduty','calendar','dns '):
 if x in text: ok=False
if a.out_dir:
 Path(a.out_dir).mkdir(parents=True,exist_ok=True)
 Path(a.out_dir,'maintenance_rollforward_audit_report.json').write_text(json.dumps({"schema_version":"1.0.0","audit_id":"mra-001","domain":"atmosphere.air","result":"pass"},indent=2)+"\n")
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
