#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from tools.certification.soil._certification_common import *
from tools.validators.soil.certification_check import main as cmain

def main(argv=None):
 a=argparse.ArgumentParser()
 for n in ['certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']: a.add_argument(f'--{n}',required=True)
 x=a.parse_args(argv)
 if cmain(['--certification-root',x.certification_root])!=0: print(json.dumps({'trust_certification_advertising_allowed':False,'decision':'fail','reasons':['certification invalid']})); return 1
 ptr=load_json(Path(x.certification_root)/'certification/soil/current_certification.json');cid=ptr['active_certification_id']
 m=load_json(Path(x.certification_root)/f'certification/soil/certifications/{cid}/certification_manifest.json')
 reasons=[]
 if load_current_archive_package(x.archive_root)['active_archive_package_id']!=m.get('archive_package_id'): reasons.append('archive mismatch')
 if load_current_preservation(x.preservation_root)['active_preservation_id']!=m.get('preservation_id'): reasons.append('preservation mismatch')
 if load_current_release(x.published_root)['current_release_id']!=m.get('release_id'): reasons.append('release mismatch')
 if release_is_retracted(x.published_root,m.get('release_id')): reasons.append('retracted')
 ok=not reasons; print(json.dumps({'trust_certification_advertising_allowed':ok,'release_id':m.get('release_id'),'certification_id':cid,'decision':'pass' if ok else 'fail','reasons':reasons},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
