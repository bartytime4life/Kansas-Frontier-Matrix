#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.resolution.soil._resolution_common import *

def main(argv=None):
 a=argparse.ArgumentParser();
 for n in ['resolution-root','accountability-root','assurance-root','registry-root','certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']: a.add_argument('--'+n,required=True)
 x=a.parse_args(argv)
 rc=subprocess.run([sys.executable,'tools/validators/soil/resolution_check.py','--resolution-root',x.resolution_root],capture_output=True,text=True)
 data=json.loads(rc.stdout.strip() or '{}'); reasons=[]
 if rc.returncode!=0: reasons+=data.get('failure_reasons',['resolution_check failed'])
 rid=load_json(Path(x.resolution_root)/'resolution/soil/current_resolution.json')['active_resolution_id']; m=load_json(Path(x.resolution_root)/f'resolution/soil/cycles/{rid}/resolution_manifest.json'); p=load_json(Path(x.resolution_root)/f'resolution/soil/cycles/{rid}/public_resolution_report.json')
 if p.get('recommended_certificate_action') in {'suspend','revoke','tombstone'} and p.get('public_advertising_allowed',True): reasons.append('certificate action blocks advertising')
 ok=not reasons
 print(json.dumps({'resolution_advertising_allowed':ok,'release_id':m.get('release_id'),'registry_id':m.get('registry_id'),'accountability_id':m.get('accountability_id'),'resolution_id':rid,'certificate_status':m.get('certificate_status'),'decision':'pass' if ok else 'block','reasons':reasons},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
