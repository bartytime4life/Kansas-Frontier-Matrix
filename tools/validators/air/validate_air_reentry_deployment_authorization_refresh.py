#!/usr/bin/env python3
import sys,json
from pathlib import Path
BAD=["data/raw/","data/work/","data/quarantine/","data/processed/air/","data/published/air/"]
for d in sys.argv[1:]:
 p=Path(d)
 if p.is_dir():
  for f in p.rglob('*.json'):
   t=f.read_text().lower()
   if any(b in t for b in BAD): raise SystemExit(f'DENY: bad path in {f}')
print('PASS')
