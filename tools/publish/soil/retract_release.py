#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, datetime as dt, hashlib, json, os, tempfile
from pathlib import Path
from tools.audit.soil._published_common import load_json, sanitize_id, sha256_file, validate_published_release

def atomic_write(path:Path,payload:dict):
 path.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix='.tmp_',dir=str(path.parent))
 with os.fdopen(fd,'w',encoding='utf-8') as f:f.write(json.dumps(payload,sort_keys=True,indent=2)+'\n')
 os.replace(tmp,path)

def valid_reason(r):
 t={"errata","retraction","rights","provenance","quality","security"};s={"low","medium","high","critical"}
 return r.get('schema_version')=='kfm.v1' and r.get('reason_type') in t and r.get('severity') in s and r.get('requested_by') and r.get('reason') and isinstance(r.get('evidence_refs'),list) and (r.get('steward_review') or {}).get('required') is True and (r.get('steward_review') or {}).get('decision')=='approved'

def main(argv=None):
 ap=argparse.ArgumentParser();ap.add_argument('--published-root',required=True);ap.add_argument('--release-id',required=True);ap.add_argument('--replacement-release-id');ap.add_argument('--reason',required=True);a=ap.parse_args(argv)
 root=Path(a.published_root);rid=a.release_id
 try:
  reason=load_json(Path(a.reason))
  if not valid_reason(reason): raise ValueError('invalid reason file')
  src=validate_published_release(root,rid)
  if not src['valid']: raise ValueError('source release invalid')
  replacement=None
  if a.replacement_release_id:
   replacement=validate_published_release(root,a.replacement_release_id)
   if not replacement['valid']: raise ValueError('invalid replacement release')
  rel=src['release_dir'];pub_receipt=rel/'publication_receipt.json'
  notice={'schema_version':'kfm.v1','object_type':'RetractionNotice','domain':'soil','release_id':rid,'replacement_release_id':a.replacement_release_id or None,'status':'RETRACTED','reason_type':reason['reason_type'],'severity':reason['severity'],'reason':reason['reason'],'evidence_refs':reason['evidence_refs'],'created':dt.datetime.now(dt.timezone.utc).isoformat(),'public_message':f"Release {rid} has been retracted."}
  n_hash=hashlib.sha256(json.dumps(notice,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  cur=root/'published/soil/current.json';current=load_json(cur);pointer_updated=False
  if current.get('current_release_id')==rid:
   pointer_updated=True
   if a.replacement_release_id: current={'schema_version':'kfm.v1','domain':'soil','current_release_id':a.replacement_release_id,'release_ref':f'releases/{a.replacement_release_id}'}
   else: current={'schema_version':'kfm.v1','domain':'soil','current_release_id':None,'release_ref':None,'public_read_available':False}
  receipt={'schema_version':'kfm.v1','receipt_type':'RetractionReceipt','from_state':'PUBLISHED','to_state':'RETRACTED','decision':'approved','release_id':rid,'replacement_release_id':a.replacement_release_id or None,'source_publication_receipt_hash':sha256_file(pub_receipt),'retraction_notice_hash':n_hash,'current_pointer_updated':pointer_updated,'policy_checks':{'steward_review_checked':True,'immutable_release_preserved':True,'replacement_audited':bool(a.replacement_release_id),'public_read_safeguard_updated':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
  rdir=root/'published/soil/retractions';np=rdir/f'{sanitize_id(rid)}.retraction_notice.json';rp=rdir/f'{sanitize_id(rid)}.retraction_receipt.json'
  atomic_write(np,notice);atomic_write(rp,receipt)
  if pointer_updated: atomic_write(cur,current)
  print(json.dumps({'retraction_recorded':True,'release_id':rid,'replacement_release_id':a.replacement_release_id if a.replacement_release_id else None,'outputs':{'notice':str(np),'receipt':str(rp),'current':str(cur) if pointer_updated else None}},sort_keys=True));return 0
 except Exception as e:
  print(json.dumps({'retraction_recorded':False,'release_id':rid,'reasons':[str(e)]},sort_keys=True));return 1
if __name__=='__main__': raise SystemExit(main())
