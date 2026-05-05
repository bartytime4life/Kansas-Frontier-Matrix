#!/usr/bin/env python3
import argparse, pathlib, sys
REQ=['REORG_SPRINT_MANIFEST.md','path_inventory.tsv','move_plan.tsv','reference_update_plan.tsv','authority_conflicts.md','validation_report.md','rollback_plan.sh']

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('dir'); a=ap.parse_args(); d=pathlib.Path(a.dir)
    miss=[f for f in REQ if not (d/f).exists()]
    if miss:
        print('MISSING:'+','.join(miss)); return 1
    print('OK: manifest files present')
    return 0
if __name__=='__main__': raise SystemExit(main())
