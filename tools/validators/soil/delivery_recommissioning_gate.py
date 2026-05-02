#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.soil.delivery_recommissioning_check import main as chk

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--recommissioning-root',required=True)
 for x in ['resilience-root','closure-root','incident-root','observability-root','delivery-root','routing-root','active-root','lineage-root','outcome-root','remediation-root','corrective-root','resolution-root','accountability-root','assurance-root','registry-root','certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']: p.add_argument('--'+x,required=True)
 a=p.parse_args(argv)
 rc=chk(['--recommissioning-root',a.recommissioning_root])
 if rc!=0: print(json.dumps({'delivery_recommissioning_advertising_allowed':False,'decision':'blocked'})); return 1
 print(json.dumps({'delivery_recommissioning_advertising_allowed':True,'recommissioning_state':'recommissioned_governance_only','decision':'pass'})); return 0
if __name__=='__main__': raise SystemExit(main())
