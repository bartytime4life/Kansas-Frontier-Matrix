#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.preservation.soil._preservation_common import *
from tools.validators.soil.preservation_check import main as pchk

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--preservation-root',required=True);a.add_argument('--pid-fixture',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 if pchk(['--preservation-root',x.preservation_root])!=0: return 1
 f=load_json(x.pid_fixture); root=Path(x.preservation_root)/'preservation/soil'; pid=load_json(root/'current_preservation.json')['active_preservation_id']
 if f.get('decision')!='accept' or not f.get('pid') or not validate_base_public_url(f.get('landing_url')) or scan_payload_for_forbidden_terms(f): print(json.dumps({'pid_reserved':False})); return 1
 d=Path(x.out_root)/'preservation/soil/pids'; d.mkdir(parents=True,exist_ok=True)
 write_json_atomic(d/f'{pid}.pid_notice.json',{'preservation_id':pid,'pid':f['pid'],'landing_url':f['landing_url'],'pid_is_mock':True,'live_pid_registration_performed':False})
 write_json_atomic(d/f'{pid}.pid_receipt.json',{'preservation_id':pid,'decision':'pass','pid_is_mock':True,'live_pid_registration_performed':False,'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}})
 print(json.dumps({'pid_reserved':True,'preservation_id':pid,'pid':f['pid']},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
