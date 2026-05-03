#!/usr/bin/env python3
from __future__ import annotations
import argparse, pathlib, csv, sys

def check(dirp:pathlib.Path)->int:
    required=['REORG_SPRINT_MANIFEST.md','path_inventory.tsv','move_plan.tsv','reference_update_plan.tsv','authority_conflicts.md','validation_report.md','rollback_plan.sh']
    missing=[f for f in required if not (dirp/f).exists()]
    if missing:
        print('MISSING', ','.join(missing)); return 1
    inv=list(csv.DictReader((dirp/'path_inventory.tsv').open(), delimiter='\t'))
    if not inv:
        print('inventory empty'); return 1
    for n in ['old_path','new_path','status']:
        if n not in csv.DictReader((dirp/'move_plan.tsv').open(), delimiter='\t').fieldnames:
            print('move_plan missing columns'); return 1
    print(f'OK manifest_dir={dirp} inventory_rows={len(inv)}')
    return 0

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('manifest_dir')
    args=ap.parse_args(); sys.exit(check(pathlib.Path(args.manifest_dir)))
