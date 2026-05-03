#!/usr/bin/env python3
import argparse, pathlib, sys
req=['REORG_SPRINT_MANIFEST.md','path_inventory.tsv','move_plan.tsv','reference_update_plan.tsv','authority_conflicts.md','validation_report.md','rollback_plan.sh']
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('dir');ns=a.parse_args();d=pathlib.Path(ns.dir)
 miss=[x for x in req if not (d/x).exists()]
 if miss: print('MISSING',*miss,sep='\n');sys.exit(1)
 print('manifest files present')
