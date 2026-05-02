#!/usr/bin/env python3
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.recommissioning.soil._recommissioning_common import load_json
from tools.validators.soil.delivery_recommissioning_check import main as cmain

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--recommissioning-root',required=True)
 for n in ['resilience','closure','incident','observability','delivery','routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']: p.add_argument(f'--{n}-root',required=True)
 ns=p.parse_args(argv)
 rc=cmain(['--recommissioning-root',ns.recommissioning_root])
 cur=load_json(Path(ns.recommissioning_root)/'recommissioning/soil/current_delivery_recommissioning.json')
 cyc=load_json(Path(ns.recommissioning_root)/f"recommissioning/soil/cycles/{cur['active_recommissioning_id']}/delivery_recommissioning_manifest.json")
 allow=(rc==0 and cyc.get('recommissioning_state')=='recommissioned_active')
 print(json.dumps({'delivery_recommissioning_advertising_allowed':allow,'prior_release_id':cyc.get('prior_release_id'),'active_release_id':cyc.get('active_release_id'),'recommissioning_id':cur['active_recommissioning_id'],'recommissioning_state':cyc.get('recommissioning_state'),'decision':'pass' if allow else 'blocked'}))
 return 0 if allow else 1
if __name__=='__main__': raise SystemExit(main())
