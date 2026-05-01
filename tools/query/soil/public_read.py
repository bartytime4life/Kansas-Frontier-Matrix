#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
BLOCK={"RAW","WORK","QUARANTINE","PROCESSED"}

def load(p:Path):
    d=json.loads(p.read_text())
    if not isinstance(d,dict): raise ValueError('invalid object')
    return d

def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--published-root',required=True);g=ap.add_mutually_exclusive_group(required=True);g.add_argument('--list',action='store_true');g.add_argument('--bundle-id')
    a=ap.parse_args(argv)
    try:
      root=Path(a.published_root)/'published/soil'
      cur=load(root/'current.json');rid=cur.get('current_release_id')
      if not rid: raise ValueError('missing current release')
      rel=root/'releases'/rid
      idx=load(rel/'index.json');rec=load(rel/'publication_receipt.json')
      if rec.get('decision')!='pass' or idx.get('object_type')!='SoilPublicReadModel': raise ValueError('invalid published release')
      rows=idx.get('records') or []
      for r in rows:
        if r.get('publication_status')!='PUBLISHED': raise ValueError('non published record')
        if any(x in json.dumps(r) for x in BLOCK): raise ValueError('forbidden path leak')
      if a.list:
        print(json.dumps({'release_id':rid,'records':[{'bundle_id':r['bundle_id'],'publication_status':r['publication_status'],'rights_status':r.get('rights_status')} for r in rows]},sort_keys=True));return 0
      row=next((r for r in rows if r.get('bundle_id')==a.bundle_id),None)
      if not row: print(json.dumps({'error':'bundle_not_found','bundle_id':a.bundle_id},sort_keys=True));return 1
      print(json.dumps({'release_id':rid,'record':row,'evidence_refs':{'evidence_bundle_ref':row.get('evidence_bundle_ref'),'stac_ref':row.get('stac_ref'),'dcat_ref':row.get('dcat_ref'),'prov_ref':row.get('prov_ref'),'triplet_ref':row.get('triplet_ref')}},sort_keys=True));return 0
    except Exception as e:
      print(json.dumps({'error':'read_blocked','reason':str(e)},sort_keys=True));return 1
if __name__=='__main__': raise SystemExit(main())
