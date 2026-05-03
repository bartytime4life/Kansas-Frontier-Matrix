#!/usr/bin/env python3
import argparse, csv
from pathlib import Path

def read_tsv(p):
    with open(p,newline='') as f: return list(csv.DictReader(f,delimiter='\t'))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('dir'); args=ap.parse_args()
    d=Path(args.dir)
    req=['REORG_SPRINT_MANIFEST.md','path_inventory.tsv','move_plan.tsv','reference_update_plan.tsv','authority_conflicts.md','validation_report.md','rollback_plan.sh']
    missing=[x for x in req if not (d/x).exists()]
    if missing:
        print('MISSING:'+','.join(missing)); raise SystemExit(1)
    mv=read_tsv(d/'move_plan.tsv')
    rb=(d/'rollback_plan.sh').read_text()
    for r in mv:
        if r.get('old_path') and r['old_path'] not in rb: print('WARN rollback missing',r['old_path'])
    print('OK manifest basic checks passed')

if __name__=='__main__': main()
