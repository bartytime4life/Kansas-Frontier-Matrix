#!/usr/bin/env python3
import argparse, json
from pathlib import Path
BAD=['data/raw/','data/work/','data/quarantine/','data/processed/air/','token','private key','bearer ']
REQ=['deployment_authorization.json','change_control_handoff.json','release_cutover_checklist.json','post_deploy_verification_plan.json','local_deployment_simulation.json','deployment_execution_receipt.json','post_deploy_verification_report.json']
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('dirs',nargs='+');a.add_argument('--deployment-readiness-dir');a.add_argument('--delivery-dir');a.add_argument('--as-of');x=a.parse_args();rc=0
 files={}
 for d in x.dirs:
  p=Path(d)
  for f in p.glob('*.json'): files[f.name]=f
 for r in REQ:
  if r not in files: print('DENY missing',r); rc=1
 for f in files.values():
  t=f.read_text().lower()
  if any(b in t for b in BAD): print('DENY unsafe',f); rc=1
 if 'deployment_authorization.json' in files:
  j=json.loads(files['deployment_authorization.json'].read_text())
  if j.get('authorized_environment') in ['production','production_proposed']: print('DENY production'); rc=1
 print('PASS' if rc==0 else 'DENY')
 raise SystemExit(rc)
