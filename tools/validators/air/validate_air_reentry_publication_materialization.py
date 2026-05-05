#!/usr/bin/env python3
import argparse, json, sys
import hashlib
from pathlib import Path
BAD=['data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/','data/published/air/read_model/','secret','token','bearer ','slack','pagerduty','calendar','kubectl','terraform']
REQ=['reentry_publication_materialization_plan.json','reentry_publication_artifact_preview_manifest.json','reentry_publication_manifest_finalization_candidate.json','reentry_publication_receipt_candidate.json','reentry_public_read_model_refresh_request.json','reentry_publication_delta_seed.json','reentry_publication_materialization_ledger_manifest.json']

def sha(p: Path) -> str:
 return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--publication-boundary-dir');p.add_argument('--release-candidate-dir');p.add_argument('--delivery-dir');p.add_argument('--as-of');a=p.parse_args();ok=True
 for d in a.dirs:
  for f in Path(d).rglob('*.json*'):
   t=f.read_text(errors='ignore').lower()
   if any(b in t for b in BAD): ok=False
 # required core artifacts may be spread across input dirs
 for r in REQ:
  if not any((Path(d)/r).exists() for d in a.dirs): ok=False
 # finalization must never claim published
 fin = next((Path(d)/'reentry_publication_manifest_finalization_candidate.json' for d in a.dirs if (Path(d)/'reentry_publication_manifest_finalization_candidate.json').exists()), None)
 if fin:
  j=json.loads(fin.read_text())
  if str(j.get('status','')).lower()=='published': ok=False
 # receipt must remain non-production
 rc = next((Path(d)/'reentry_publication_receipt_candidate.json' for d in a.dirs if (Path(d)/'reentry_publication_receipt_candidate.json').exists()), None)
 if rc:
  j=json.loads(rc.read_text())
  if j.get('execution_mode')=='production_execution': ok=False
 # preview manifest hash integrity
 pm = next((Path(d)/'reentry_publication_artifact_preview_manifest.json' for d in a.dirs if (Path(d)/'reentry_publication_artifact_preview_manifest.json').exists()), None)
 if pm:
  m=json.loads(pm.read_text())
  for item in m.get('preview_artifacts',[]):
   pth=Path(item.get('path',''))
   if pth.exists() and item.get('sha256') and sha(pth)!=item['sha256']:
    ok=False
 print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
if __name__=='__main__': main()
