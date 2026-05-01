#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from tools.preservation.soil._preservation_common import *
from tools.validators.soil.preservation_check import main as pchk

def main(argv=None):
 a=argparse.ArgumentParser();
 for k in ['preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']: a.add_argument(f'--{k}',required=True)
 x=a.parse_args(argv); rs=[]
 if pchk(['--preservation-root',x.preservation_root])!=0: rs.append('preservation invalid')
 cur=load_json(Path(x.preservation_root)/'preservation/soil/current_preservation.json'); pid=cur['active_preservation_id']; m=load_json(Path(x.preservation_root)/f'preservation/soil/packages/{pid}/preservation_manifest.json')
 if load_current_reconciliation(x.reconciliation_root)['active_reconciliation_id']!=m['reconciliation_id']: rs.append('reconciliation mismatch')
 if release_is_retracted(x.published_root,m['release_id']): rs.append('release retracted')
 if not load_operational_status(x.ops_root).get('public_access_allowed'): rs.append('ops blocked')
 out={'preservation_advertising_allowed':not rs,'release_id':m['release_id'],'preservation_id':pid,'decision':'pass' if not rs else 'fail','reasons':rs}; print(json.dumps(out,sort_keys=True)); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
