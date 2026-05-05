#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT)) if str(ROOT) not in sys.path else None
from tools.validators.soil.public_observability_check import main as chk
from tools.observability.soil._delivery_observability_common import load_json

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--observability-root',required=True)
 for k in ['delivery-root','routing-root','active-root','lineage-root','outcome-root','remediation-root','corrective-root','resolution-root','accountability-root','assurance-root','registry-root','certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']:
  ap.add_argument('--'+k,required=True)
 x=ap.parse_args(argv)
 if chk(['--observability-root',x.observability_root])!=0:
  print(json.dumps({'public_observability_advertising_allowed':False,'decision':'fail'})); return 1
 cur=load_json(Path(x.observability_root)/'observability/soil/current_public_observability.json')
 print(json.dumps({'public_observability_advertising_allowed':True,'prior_release_id':cur.get('prior_release_id'),'active_release_id':cur.get('active_release_id'),'observability_id':cur.get('active_observability_id'),'observability_state':cur.get('observability_state'),'decision':'pass'})); return 0
if __name__=='__main__': raise SystemExit(main())
