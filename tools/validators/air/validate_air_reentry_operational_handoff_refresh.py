#!/usr/bin/env python
import argparse,sys
from pathlib import Path
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/","data/published/air/")
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--as-of');p.add_argument('--cutover-refresh-dir');p.add_argument('--deployment-authorization-refresh-dir');p.add_argument('--deployment-readiness-refresh-dir');p.add_argument('--client-delivery-refresh-dir');p.add_argument('--read-model-refresh-dir');a=p.parse_args();ok=True
for d in map(Path,a.dirs):
 for f in d.glob('*.json'):
  t=f.read_text().lower()
  if any(x in t for x in BAD): ok=False
print('PASS' if ok else 'DENY'); sys.exit(0 if ok else 1)
