#!/usr/bin/env python3
import argparse,sys
from pathlib import Path
BAD=['data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/','data/published/air/read_model/','secret','token','bearer ','slack','pagerduty','calendar','kubectl','terraform','http://','https://']
REQ=['reentry_publication_materialization_plan.json','reentry_publication_artifact_preview_manifest.json','reentry_publication_manifest_finalization_candidate.json','reentry_publication_receipt_candidate.json','reentry_public_read_model_refresh_request.json','reentry_publication_delta_seed.json','reentry_publication_materialization_ledger_manifest.json']
def main():
 p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--publication-boundary-dir');p.add_argument('--release-candidate-dir');p.add_argument('--delivery-dir');p.add_argument('--as-of');a=p.parse_args();ok=True
 for d in a.dirs:
  for f in Path(d).rglob('*.json*'):
   t=f.read_text(errors='ignore').lower()
   if any(b in t for b in BAD): ok=False
 for r in REQ:
  if not any((Path(d)/r).exists() for d in a.dirs): ok=False
 print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
if __name__=='__main__': main()
