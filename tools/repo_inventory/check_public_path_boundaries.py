#!/usr/bin/env python3
from __future__ import annotations
import pathlib,re,sys
roots=['apps/web/src','apps/ui','apps/governed_api/routes']
bad=[]
pat=re.compile(r'data/(raw|work|quarantine)/')
for r in roots:
    p=pathlib.Path(r)
    if not p.exists():
        continue
    for f in p.rglob('*'):
        if f.is_file() and f.suffix in {'.js','.ts','.tsx','.py','.md','.json'}:
            t=f.read_text(errors='ignore')
            if pat.search(t): bad.append(str(f))
if bad:
    print('\n'.join(bad)); sys.exit(1)
print('OK no direct public raw/work/quarantine refs')
