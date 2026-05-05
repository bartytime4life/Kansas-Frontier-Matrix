#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
DENIED={'decimallatitude','decimallongitude','latitude','longitude','lat','lon','raw_latitude','raw_longitude','point','geom','geometry'}

def scan(x, issues, public_safe=False):
    if isinstance(x,dict):
        for k,v in x.items():
            if public_safe and k.lower() in DENIED: issues.append(k)
            scan(v,issues,public_safe)
    elif isinstance(x,list):
        for i in x: scan(i,issues,public_safe)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path'); a=ap.parse_args()
    p=Path(a.path); j=json.loads(p.read_text()); issues=[]
    scan(j,issues,bool(j.get('public_safe')))
    if issues:
        print('fail: denied fields '+','.join(sorted(set(issues)))); sys.exit(2)
    print('pass')

if __name__=='__main__': main()
