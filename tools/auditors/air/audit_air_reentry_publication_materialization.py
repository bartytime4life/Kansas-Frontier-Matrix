#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
BAD=['data/published/air/','data/published/air/read_model/','data/raw/','data/work/','data/quarantine/','data/processed/air/','secret','token','bearer ','slack','pagerduty','calendar','http://','https://']
def main():
 p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--publication-boundary-dir');p.add_argument('--release-candidate-dir');p.add_argument('--delivery-dir');p.add_argument('--source-publication-boundary-dir');p.add_argument('--source-release-candidate-dir');p.add_argument('--source-delivery-dir');p.add_argument('--as-of');p.add_argument('--out-dir');a=p.parse_args();ok=True
 for d in a.dirs:
  for f in Path(d).rglob('*.json*'):
   if any(b in f.read_text(errors='ignore').lower() for b in BAD): ok=False
 if a.out_dir:
  o=Path(a.out_dir);o.mkdir(parents=True,exist_ok=True)
  (o/'reentry_publication_materialization_audit_report.json').write_text(json.dumps({'schema_version':'v1','audit_id':'audit-1','domain':'atmosphere.air','generated_at':'2026-04-30T00:00:00Z','as_of':a.as_of or '2026-04-30T00:00:00Z','result':'pass' if ok else 'deny'},indent=2)+'\n')
 print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
if __name__=='__main__': main()
