#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from _reentry_publication_boundary_refresh_lib import has_unsafe_obj
ap=argparse.ArgumentParser(); ap.add_argument('dirs',nargs='+'); ap.add_argument('--as-of'); ap.add_argument('--release-candidate-refresh-dir'); ap.add_argument('--candidate-reentry-refresh-dir'); ap.add_argument('--client-delivery-refresh-dir'); ap.add_argument('--read-model-refresh-dir')
a=ap.parse_args()
req=['reentry_gate_d_refresh_attestation.json','reentry_aqs_reconciliation_refresh_checkpoint.json','reentry_publication_boundary_refresh_review.json','reentry_publication_eligibility_refresh_decision.json','reentry_publication_candidate_refresh_manifest.json','reentry_publication_manifest_refresh_candidate.json','reentry_publication_boundary_refresh_lineage_bridge.json','reentry_publication_boundary_refresh_manifest.json','reentry_publication_boundary_refresh_ledger_manifest.json']
found={}
for d in a.dirs:
 for f in Path(d).glob('*.json'): found[f.name]=f
errs=[]
for r in req:
 if r not in found: errs.append(f'missing {r}')
for n,p in found.items():
 obj=json.loads(p.read_text())
 if has_unsafe_obj(obj): errs.append(f'unsafe content {n}')
 if obj.get('status')=='published': errs.append(f'published status not allowed {n}')
print('DENY' if errs else 'PASS')
for e in errs: print(e)
raise SystemExit(1 if errs else 0)
