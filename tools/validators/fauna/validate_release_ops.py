#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
DENIED={"decimallatitude","decimallongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry"}

def fail(m): print(f"ERROR: {m}",file=sys.stderr); raise SystemExit(2)

def scan(o):
    if isinstance(o,dict):
        for k,v in o.items():
            lk=k.lower()
            if lk in DENIED: return True
            if scan(v): return True
    if isinstance(o,list):
        return any(scan(x) for x in o)
    return False

obj=json.loads(Path(sys.argv[1]).read_text())
if obj.get('exact_points')!='restricted': fail('exact_points must be restricted')
if obj.get('public_safe') is False: fail('public_safe must not be false')
if scan(obj): fail('contains denied coordinate/geometry fields')
print('ok')
