#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.archive.soil._archive_common import *
from tools.validators.soil.archive_package_check import main as pkg_check

def main(argv=None):
 a=argparse.ArgumentParser();
 for n in ['archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']: a.add_argument(f'--{n}',required=True)
 x=a.parse_args(argv)
 rs=[]
 if pkg_check(['--archive-root',x.archive_root])!=0: rs.append('archive invalid')
 ar=Path(x.archive_root)/'archive/soil'; aid=load_json(ar/'current_archive_package.json')['active_archive_package_id']; m=load_json(ar/f'packages/{aid}/archive_manifest.json')
 if load_current_preservation(x.preservation_root).get('active_preservation_id')!=m.get('preservation_id'): rs.append('current preservation mismatch')
 if load_json(Path(x.published_root)/'published/soil/current.json').get('current_release_id')!=m.get('release_id'): rs.append('current release mismatch')
 cs=load_json(ar/'status/current_custody_status.json')
 if not cs.get('public_advertising_allowed'): rs.append('advertising blocked')
 if release_is_retracted(x.published_root,m.get('release_id')): rs.append('retracted')
 out={'archive_custody_advertising_allowed':not rs,'release_id':m.get('release_id'),'archive_package_id':aid,'decision':'pass' if not rs else 'fail','reasons':rs}
 print(json.dumps(out,sort_keys=True)); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
