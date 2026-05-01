#!/usr/bin/env python
import argparse,sys,json
from pathlib import Path
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/")
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--as-of');p.add_argument('--closure-dir');p.add_argument('--handoff-dir');p.add_argument('--cutover-dir');p.add_argument('--authorization-dir');p.add_argument('--deployment-readiness-dir');p.add_argument('--delivery-dir');a=p.parse_args();ok=True
for d in map(Path,a.dirs):
 for f in d.glob('*.json'):
  t=f.read_text().lower();
  if any(x in t for x in BAD): ok=False
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
