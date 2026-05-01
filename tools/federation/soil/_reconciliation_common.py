#!/usr/bin/env python3
from __future__ import annotations
import datetime as dt, hashlib, json, os, re, tempfile
from pathlib import Path
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
PUBLIC_RIGHTS={"open","public","public_aggregate","public_safe","public_reviewed"}
ACK_STATUSES={"accepted","rejected","pending","withdrawn"}
TARGETS={"dcat","ckan","data_gov","stac","ogc_records","schemaorg","mirror","notifications"}
load_json=lambda p: json.loads(Path(p).read_text(encoding='utf-8'))
def write_json_atomic(path,payload):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent));os.close(fd);Path(tmp).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n',encoding='utf-8');os.replace(tmp,p)
def write_text_atomic(path,text):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent));os.close(fd);Path(tmp).write_text(text,encoding='utf-8');os.replace(tmp,p)
sha256_file=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest(); sha256_bytes=lambda d: hashlib.sha256(d).hexdigest(); utc_now_iso=lambda: dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')
sanitize_id=lambda v: re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve()))
scan_text_for_forbidden_terms=lambda t: sorted({x for x in FORBIDDEN_TERMS if x.lower() in (t or '').lower()})
def has_private_path(v):
 s=str(v or ''); return s.startswith('/') or re.match(r'^[A-Za-z]:\\',s) is not None or 'file://' in s or '/../' in s or '..\\' in s
def scan_payload_for_forbidden_terms(p):
 s=json.dumps(p,sort_keys=True);f=scan_text_for_forbidden_terms(s);return sorted(set(f+(["private_path"] if has_private_path(s) else [])))
is_public_rights=lambda r:(r or '').lower() in PUBLIC_RIGHTS
stable_payload_hash=lambda p: sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
def load_current_federation(root): return load_json(Path(root)/'federation/soil/current_federation.json')
def load_federation_manifest(root,fid): return load_json(Path(root)/f'federation/soil/releases/{fid}/federation_manifest.json')
def load_federation_receipt(root,fid): return load_json(Path(root)/f'federation/soil/releases/{fid}/federation_receipt.json')
def load_mock_submission_receipts(root,fid):
 p=Path(root)/f'federation/soil/submissions/{fid}'; out={}
 for r in sorted(p.glob('*.submission_receipt.json')): out[r.name.split('.')[0]]=load_json(r)
 return out
def load_acknowledgement_receipts(root,fid):
 p=Path(root)/f'federation/soil/acks/{fid}'; out={}
 for r in sorted(p.glob('*.ack_receipt.json')): out[r.name.split('.')[0]]=load_json(r)
 return out
def load_withdrawal_receipts(root,release_id):
 p=Path(root)/'federation/soil/withdrawals'/f'{sanitize_id(release_id)}.withdrawal_receipt.json'; return load_json(p) if p.exists() else None
def release_is_retracted(pub_root,release_id):
 p=Path(pub_root)/'published/soil/retractions'
 if not p.exists(): return False
 for n in p.glob('*.retraction_notice.json'):
  j=load_json(n)
  if j.get('release_id')==release_id and j.get('status')=='RETRACTED': return True
 return False
def validate_external_url(u):
 uu=urlparse(str(u or ''))
 if uu.scheme=='https' and uu.netloc and not uu.username and not uu.password: return True
 if uu.scheme=='http' and uu.hostname in {'localhost','127.0.0.1'} and not uu.username and not uu.password: return True
 return False
def validate_reconciliation_inputs(fed,disc,pub,ops,fid):
 rs=[]; m=load_federation_manifest(fed,fid); r=load_federation_receipt(fed,fid)
 if m.get('federation_status')!='FEDERATION_READY': rs.append('federation_status not FEDERATION_READY')
 if r.get('decision')!='pass' or not r.get('signatures'): rs.append('invalid federation receipt')
 if scan_payload_for_forbidden_terms(m): rs.append('forbidden terms in federation payload')
 return rs,m,r
