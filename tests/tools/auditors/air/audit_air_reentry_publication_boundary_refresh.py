#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from _reentry_publication_boundary_refresh_lib import has_unsafe_obj
ap=argparse.ArgumentParser(); ap.add_argument('dirs',nargs='+'); ap.add_argument('--out-dir'); ap.add_argument('--as-of')
a=ap.parse_args(); errs=[]
for d in a.dirs:
 for p in Path(d).glob('*.json'):
  o=json.loads(p.read_text())
  if has_unsafe_obj(o): errs.append(f'unsafe {p}')
res={'schema_version':'v1','domain':'atmosphere.air','result':'deny' if errs else 'pass','checks':{'unsafe':not bool(errs)},'findings':errs}
if a.out_dir: Path(a.out_dir).mkdir(parents=True,exist_ok=True); (Path(a.out_dir)/'reentry_publication_boundary_refresh_audit_report.json').write_text(json.dumps(res,indent=2)+'\n')
print('DENY' if errs else 'PASS')
raise SystemExit(1 if errs else 0)
