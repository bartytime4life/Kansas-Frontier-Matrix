#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from tools.federation.soil._federation_common import *
from tools.validators.soil.federation_check import main as fcheck

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--federation-root',required=True);a.add_argument('--discovery-root',required=True);a.add_argument('--published-root',required=True);a.add_argument('--ops-root',required=True);x=a.parse_args(argv)
 if fcheck(['--federation-root',x.federation_root])!=0:
  print(json.dumps({'federation_advertising_allowed':False,'decision':'fail','reasons':['federation_check failed']})); return 1
 ptr=load_json(Path(x.federation_root)/'federation/soil/current_federation.json'); fid=ptr['active_federation_id'];m=load_json(Path(x.federation_root)/f'federation/soil/releases/{fid}/federation_manifest.json')
 rs=[]
 if load_current_discovery(x.discovery_root)['active_discovery_id']!=m['discovery_id']: rs.append('non-current discovery')
 if load_current_release(x.published_root)['current_release_id']!=m['release_id']: rs.append('non-current release')
 if release_is_retracted(x.published_root,m['release_id']): rs.append('release retracted')
 st=load_operational_status(x.ops_root)
 if st.get('public_access_allowed') is not True or st.get('latest_probe_decision')!='pass': rs.append('status blocked')
 out={'federation_advertising_allowed':not rs,'release_id':m['release_id'],'discovery_id':m['discovery_id'],'federation_id':fid,'decision':'pass' if not rs else 'fail'}
 if rs: out['reasons']=rs
 print(json.dumps(out,sort_keys=True)); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
