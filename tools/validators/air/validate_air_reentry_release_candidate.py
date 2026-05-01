#!/usr/bin/env python
import argparse,json,sys
from pathlib import Path
BAD=['data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/','secret','token','bearer ','kubectl','terraform','http://','https://']
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--as-of');a=p.parse_args()
text='\n'.join(f.read_text(errors='ignore').lower() for d in a.dirs for f in Path(d).rglob('*.json*') if f.is_file())
ok=not any(b in text for b in BAD)
print('PASS' if ok else 'DENY')
sys.exit(0 if ok else 1)
