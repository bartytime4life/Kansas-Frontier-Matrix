#!/usr/bin/env python3
import argparse,sys
from pathlib import Path
BAD=['data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/','secret','token','bearer ','slack','pagerduty','calendar','kubectl','terraform','http://','https://']
REQ=['reentry_gate_d_attestation.json','reentry_aqs_reconciliation_refresh.json','reentry_publication_boundary_review.json','reentry_publication_eligibility_decision.json','reentry_publication_candidate_manifest.json','reentry_publication_manifest_candidate.json','reentry_publication_lineage_bridge.json']
def main():
 p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--as-of');a=p.parse_args();ok=True
 for d in a.dirs:
  dp=Path(d)
  if dp.is_dir():
   for f in dp.rglob('*.json*'):
    t=f.read_text(errors='ignore').lower()
    if any(b in t for b in BAD): ok=False
 for r in REQ:
  if not any((Path(d)/r).exists() for d in a.dirs): ok=False
 print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
if __name__=='__main__': main()
