#!/usr/bin/env python
import argparse,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--rollforward-dir');p.add_argument('--maintenance-dir');p.add_argument('--assurance-dir');p.add_argument('--delivery-dir');p.add_argument('--as-of');a=p.parse_args();
text=''.join(f.read_text(errors='ignore').lower() for d in map(Path,a.dirs) for f in d.rglob('*.json*'))
bad=['data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/','secret','token','bearer ','https://','kubectl','terraform']
ok=not any(x in text for x in bad)
print('PASS' if ok else 'DENY'); sys.exit(0 if ok else 1)
