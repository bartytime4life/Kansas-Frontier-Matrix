#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.soil.remediation_handoff_check import main as cmain

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--remediation-root',required=True); a,_=ap.parse_known_args(argv)
 rc=cmain(['--remediation-root',a.remediation_root])
 if rc!=0: print(json.dumps({'remediation_handoff_advertising_allowed':False,'decision':'block'},sort_keys=True)); return 1
 print(json.dumps({'remediation_handoff_advertising_allowed':True,'certificate_status':'active','decision':'pass'},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
