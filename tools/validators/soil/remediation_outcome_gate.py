#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.remediation.soil._outcome_common import load_json

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--outcome-root',required=True); ap.add_argument('--remediation-root'); ap.add_argument('--corrective-root'); ap.add_argument('--resolution-root'); ap.add_argument('--accountability-root'); ap.add_argument('--assurance-root'); ap.add_argument('--registry-root'); ap.add_argument('--certification-root'); ap.add_argument('--archive-root'); ap.add_argument('--preservation-root'); ap.add_argument('--reconciliation-root'); ap.add_argument('--federation-root'); ap.add_argument('--discovery-root'); ap.add_argument('--published-root'); ap.add_argument('--ops-root'); a=ap.parse_args(argv)
 p=subprocess.run([sys.executable,str(ROOT/'tools/validators/soil/remediation_outcome_check.py'),'--outcome-root',a.outcome_root],capture_output=True,text=True)
 data=json.loads(p.stdout or '{}') if p.stdout else {}
 ok=p.returncode==0
 certificate_status=None; error=None
 try:
  cur=load_json(Path(a.outcome_root)/'outcomes/soil/current_remediation_outcome.json')
  certificate_status=cur.get('certificate_status')
  if ok:
   man=load_json(Path(a.outcome_root)/cur['remediation_outcome_manifest_ref'])
   if man.get('certificate_status') in {'suspended','revoked','tombstoned'}: ok=False
 except Exception as e:
  ok=False; error=f'failed_to_load_remediation_outcome: {e}'
 out={'remediation_outcome_advertising_allowed':ok,'release_id':data.get('release_id'),'registry_id':data.get('registry_id'),'remediation_id':data.get('remediation_id'),'outcome_cycle_id':data.get('outcome_cycle_id'),'certificate_status':certificate_status,'decision':'pass' if ok else 'block'}
 if error is not None: out['error']=error
 print(json.dumps(out,sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
