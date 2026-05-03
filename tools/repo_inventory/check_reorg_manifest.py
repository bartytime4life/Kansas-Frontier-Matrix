#!/usr/bin/env python3
from pathlib import Path
import csv,sys

def req(path):
    p=Path(path)
    return p.exists() and p.stat().st_size>0

base=Path(sys.argv[1] if len(sys.argv)>1 else "docs/registers/reorg")
required=["REORG_SPRINT_MANIFEST.md","path_inventory.tsv","move_plan.tsv","reference_update_plan.tsv","authority_conflicts.md","validation_report.md","rollback_plan.sh"]
missing=[r for r in required if not req(base/r)]
if missing:
    print("MISSING:", ", ".join(missing))
    sys.exit(1)
# basic tsv shape
for name,cols in [("path_inventory.tsv",2),("move_plan.tsv",4),("reference_update_plan.tsv",4)]:
    with (base/name).open() as f:
        rows=list(csv.reader(f,delimiter='\t'))
    if not rows or any(len(r)<cols for r in rows[1:]):
        print(f"INVALID {name}")
        sys.exit(1)
print("OK")
