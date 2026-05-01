#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse,json
from pathlib import Path
from tools.audit.soil._published_common import is_retracted, load_json

def blocked(reason):
 print(json.dumps({'error':'read_blocked','reason':reason},sort_keys=True));return 1

def main(argv=None):
 ap=argparse.ArgumentParser();ap.add_argument('--published-root',required=True);g=ap.add_mutually_exclusive_group(required=True);g.add_argument('--list',action='store_true');g.add_argument('--bundle-id');a=ap.parse_args(argv)
 root=Path(a.published_root)/'published/soil'
 try:
  cur=load_json(root/'current.json');rid=cur.get('current_release_id')
  if not rid: return blocked('no_active_current_release')
  if is_retracted(Path(a.published_root),rid): return blocked('current_release_retracted')
  rel=root/'releases'/rid
  idx=load_json(rel/'index.json')
  if idx.get('object_type')!='SoilPublicReadModel': return blocked('invalid_public_index')
  rows=idx.get('records') or []
  for r in rows:
   if r.get('publication_status')!='PUBLISHED': return blocked('non_published_record_present')
  if a.list:
   print(json.dumps({'release_id':rid,'records':[{'bundle_id':r['bundle_id'],'publication_status':r['publication_status'],'rights_status':r.get('rights_status')} for r in rows]},sort_keys=True));return 0
  row=next((r for r in rows if r.get('bundle_id')==a.bundle_id),None)
  if not row: print(json.dumps({'error':'bundle_not_found','bundle_id':a.bundle_id},sort_keys=True));return 1
  print(json.dumps({'release_id':rid,'record':row},sort_keys=True));return 0
 except Exception as e:
  return blocked(str(e))
if __name__=='__main__': raise SystemExit(main())
