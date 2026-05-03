#!/usr/bin/env python3
from pathlib import Path
import sys
REQ=['REORG_SPRINT_MANIFEST.md','path_inventory.tsv','move_plan.tsv','reference_update_plan.tsv','authority_conflicts.md','validation_report.md','rollback_plan.sh']

def check(base='docs/registers/reorg'):
    b=Path(base)
    miss=[r for r in REQ if not (b/r).exists()]
    return miss

def main():
    base=sys.argv[1] if len(sys.argv)>1 else 'docs/registers/reorg'
    miss=check(base)
    if miss:
        print('MISSING',','.join(miss));sys.exit(1)
    print('OK: manifest bundle complete')

if __name__=='__main__':
    main()
