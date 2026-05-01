#!/usr/bin/env python
import argparse,sys
from pathlib import Path
BAD=('data/raw/','data/work/','data/quarantine/','data/processed/air/','http://','https://','bearer ','token','secret','slack','pagerduty','calendar')
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--assurance-dir');p.add_argument('--closure-dir');p.add_argument('--handoff-dir');p.add_argument('--cutover-dir');p.add_argument('--delivery-dir');p.add_argument('--as-of');a=p.parse_args();ok=True
for d in map(Path,a.dirs):
 for f in d.rglob('*.json'):
  t=f.read_text().lower()
  if any(x in t for x in BAD): ok=False
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
