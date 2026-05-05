#!/usr/bin/env python3
import argparse, json
from tools.validators.soil.delivery_incident_closure_check import main as chk
from tools.incident_closure.soil._incident_closure_common import load_json
from pathlib import Path

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--closure-root',required=True); ap.add_argument('--incident-root',required=True); ap.add_argument('--observability-root',required=True); ap.add_argument('--delivery-root',required=True); ap.add_argument('--routing-root',required=True); ap.add_argument('--active-root',required=True); ap.add_argument('--lineage-root',required=True); ap.add_argument('--outcome-root',required=True); ap.add_argument('--remediation-root',required=True); ap.add_argument('--corrective-root',required=True); ap.add_argument('--resolution-root',required=True); ap.add_argument('--accountability-root',required=True); ap.add_argument('--assurance-root',required=True); ap.add_argument('--registry-root',required=True); ap.add_argument('--certification-root',required=True); ap.add_argument('--archive-root',required=True); ap.add_argument('--preservation-root',required=True); ap.add_argument('--reconciliation-root',required=True); ap.add_argument('--federation-root',required=True); ap.add_argument('--discovery-root',required=True); ap.add_argument('--published-root',required=True); ap.add_argument('--ops-root',required=True); a=ap.parse_args(argv)
 rc=chk(['--closure-root',a.closure_root])
 c=load_json(Path(a.closure_root)/'incident_closure/soil/current_delivery_incident_closure.json')
 m=load_json(Path(a.closure_root)/c['delivery_incident_closure_manifest_ref'])
 allowed=(rc==0 and m.get('closure_state') not in {'blocked','open_governance_only'})
 out={'delivery_incident_closure_advertising_allowed':allowed,'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'closure_id':c.get('active_closure_id'),'closure_state':m.get('closure_state'),'decision':'pass' if allowed else 'blocked'}
 print(json.dumps(out)); return 0 if allowed else 1
if __name__=='__main__': raise SystemExit(main())
