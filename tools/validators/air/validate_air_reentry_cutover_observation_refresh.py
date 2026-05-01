#!/usr/bin/env python
import argparse, json, sys
from pathlib import Path
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/","data/published/air/","data/published/air/read_model/")

def main():
 p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--as-of');a=p.parse_args()
 ok=True
 for d in a.dirs:
  t=json.dumps(json.loads(Path(d).joinpath('reentry_cutover_observation_refresh_record.json').read_text())) if Path(d,'reentry_cutover_observation_refresh_record.json').exists() else ''
  if any(b in t.lower() for b in BAD): ok=False
 print('PASS' if ok else 'DENY')
 return 0 if ok else 1
if __name__=='__main__': sys.exit(main())
