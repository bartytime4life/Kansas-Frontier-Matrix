#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from tools.restoration.soil._delivery_restoration_common import load_json
from tools.validators.soil.delivery_restoration_check import main as cmain

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--restoration-root',required=True); p.add_argument('--recommissioning-root',required=True)
 for n in ['resilience','closure','incident','observability','delivery','routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']: p.add_argument(f'--{n}-root',required=True)
 ns=p.parse_args(argv)
 rc=cmain(['--restoration-root',ns.restoration_root])
 cur=load_json(Path(ns.restoration_root)/'restoration/soil/current_delivery_restoration.json'); rid=cur['active_restoration_id']; m=load_json(Path(ns.restoration_root)/f'restoration/soil/cycles/{rid}/delivery_restoration_manifest.json')
 allow=(rc==0 and m.get('active_public_delivery_restored') is True)
 print(json.dumps({'delivery_restoration_advertising_allowed':allow,'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'restoration_id':rid,'restoration_state':m.get('restoration_state'),'decision':'pass' if allow else 'blocked'}))
 return 0 if allow else 1
if __name__=='__main__': raise SystemExit(main())
