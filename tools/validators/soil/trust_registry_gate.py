#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from tools.validators.soil.trust_registry_check import main as rcheck
from tools.validators.soil.trust_certification_gate import main as cgate

def main(argv=None):
 a=argparse.ArgumentParser()
 for n in ['registry-root','certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']: a.add_argument(f'--{n}',required=True)
 x=a.parse_args(argv)
 reasons=[]
 if rcheck(['--registry-root',x.registry_root])!=0: reasons.append('trust_registry_check failed')
 if cgate(['--certification-root',x.certification_root,'--archive-root',x.archive_root,'--preservation-root',x.preservation_root,'--reconciliation-root',x.reconciliation_root,'--federation-root',x.federation_root,'--discovery-root',x.discovery_root,'--published-root',x.published_root,'--ops-root',x.ops_root])!=0: reasons.append('trust_certification_gate failed')
 ok=not reasons; print(json.dumps({'trust_registry_advertising_allowed':ok,'decision':'pass' if ok else 'fail','reasons':reasons},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
