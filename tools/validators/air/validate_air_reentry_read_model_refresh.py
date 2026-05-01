#!/usr/bin/env python3
import argparse,sys
from pathlib import Path
BAD=['data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/','data/published/air/read_model/','secret','token','bearer ','http://','https://']
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--materialization-dir');p.add_argument('--publication-boundary-dir');p.add_argument('--source-read-model-dir');p.add_argument('--delivery-dir');p.add_argument('--as-of');a=p.parse_args();ok=True
 for d in a.dirs:
  for f in Path(d).rglob('*.json*'):
   t=f.read_text(errors='ignore').lower()
   if any(b in t for b in BAD): ok=False
 print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
