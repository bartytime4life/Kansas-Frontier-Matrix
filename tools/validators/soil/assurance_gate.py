#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from tools.validators.soil.assurance_check import main as assurance_check
from tools.validators.soil.trust_registry_gate import main as trust_registry_gate

def main(argv=None):
 a=argparse.ArgumentParser()
 for n in ['assurance-root','registry-root','certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']: a.add_argument(f'--{n}',required=True)
 x=a.parse_args(argv)
 reasons=[]
 if assurance_check(['--assurance-root',x.assurance_root])!=0: reasons.append('assurance_check failed')
 if trust_registry_gate(['--registry-root',x.registry_root,'--certification-root',x.certification_root,'--archive-root',x.archive_root,'--preservation-root',x.preservation_root,'--reconciliation-root',x.reconciliation_root,'--federation-root',x.federation_root,'--discovery-root',x.discovery_root,'--published-root',x.published_root,'--ops-root',x.ops_root])!=0: reasons.append('trust_registry_gate failed')
 ok=not reasons
 print(json.dumps({'assurance_advertising_allowed':ok,'decision':'pass' if ok else 'fail','reasons':reasons},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
