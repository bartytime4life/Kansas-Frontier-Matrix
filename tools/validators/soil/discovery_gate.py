#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from tools.discovery.soil._discovery_common import *
from tools.validators.soil.discovery_check import main as check_main

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--discovery-root',required=True);a.add_argument('--published-root',required=True);a.add_argument('--ops-root',required=True);x=a.parse_args(argv)
 if check_main(['--discovery-root',x.discovery_root])!=0:
  print(json.dumps({'discovery_advertising_allowed':False,'decision':'fail','reasons':['discovery_check failed']},sort_keys=True)); return 1
 cur=load_current_release(x.published_root); ptr=load_json(Path(x.discovery_root)/'discovery/soil/current_discovery.json'); rid=ptr['release_id']; reasons=[]
 if rid!=cur: reasons.append('non-current release')
 reasons += [z for z in validate_discovery_inputs(x.published_root,x.ops_root,rid) if z not in {'forbidden terms in public index'}]
 out={'discovery_advertising_allowed':not reasons,'release_id':rid,'discovery_id':ptr['active_discovery_id'],'decision':'pass' if not reasons else 'fail'}
 if reasons: out['reasons']=sorted(set(reasons))
 print(json.dumps(out,sort_keys=True)); return 0 if not reasons else 1
if __name__=='__main__': raise SystemExit(main())
