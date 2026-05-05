#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.validators.soil.reconciliation_check import main as rcheck
from tools.federation.soil._reconciliation_common import load_json, release_is_retracted

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--reconciliation-root',required=True);a.add_argument('--federation-root',required=True);a.add_argument('--discovery-root',required=True);a.add_argument('--published-root',required=True);a.add_argument('--ops-root',required=True);x=a.parse_args(argv)
 rs=[]
 if rcheck(['--reconciliation-root',x.reconciliation_root])!=0: rs.append('reconciliation_check failed')
 cp=load_json(Path(x.reconciliation_root)/'federation/soil/current_reconciliation.json'); rr=load_json(Path(x.reconciliation_root)/f"federation/soil/reconciliations/{cp['active_reconciliation_id']}/reconciliation_manifest.json")
 if load_json(Path(x.federation_root)/'federation/soil/current_federation.json')['active_federation_id']!=rr['federation_id']: rs.append('non-current federation')
 if load_json(Path(x.discovery_root)/'discovery/soil/current_discovery.json')['active_discovery_id']!=rr['discovery_id']: rs.append('non-current discovery')
 if load_json(Path(x.published_root)/'published/soil/current.json')['current_release_id']!=rr['release_id']: rs.append('non-current release')
 if release_is_retracted(x.published_root,rr['release_id']): rs.append('release retracted')
 out={'external_federation_advertising_allowed':not rs,'release_id':rr['release_id'],'discovery_id':rr['discovery_id'],'federation_id':rr['federation_id'],'reconciliation_id':cp['active_reconciliation_id'],'decision':'pass' if not rs else 'fail'}
 if rs: out['reasons']=rs
 print(json.dumps(out,sort_keys=True)); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
