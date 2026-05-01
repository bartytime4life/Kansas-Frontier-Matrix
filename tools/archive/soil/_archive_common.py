#!/usr/bin/env python3
from __future__ import annotations
import datetime as dt, hashlib, json, os, re, tempfile
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from urllib.parse import urljoin, urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
PUBLIC_RIGHTS={"open","public","public_aggregate","public_safe","public_reviewed"}
load_json=lambda p: json.loads(Path(p).read_text(encoding='utf-8'))
def write_json_atomic(path,payload):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent));os.close(fd);Path(tmp).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n',encoding='utf-8');os.replace(tmp,p)
write_text_atomic=lambda path,text: write_json_atomic(path,json.loads(text)) if text.strip().startswith('{') else Path(path).write_text(text,encoding='utf-8')
sha256_file=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest(); sha256_bytes=lambda d: hashlib.sha256(d).hexdigest(); utc_now_iso=lambda: dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')
sanitize_id=lambda v: re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'
stable_payload_hash=lambda p: sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve()))
public_url_join=lambda b,p: urljoin(str(b).rstrip('/')+'/',str(p).lstrip('/'))
def validate_base_public_url(v):
 u=urlparse(str(v or '')); return (u.scheme=='https' and u.netloc and not u.username and not u.password) or (u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'} and not u.username and not u.password)
scan_text_for_forbidden_terms=lambda t: sorted({x for x in FORBIDDEN_TERMS if x.lower() in (t or '').lower()})
def has_private_path(v):
 s=str(v or ''); return s.startswith('/') or re.match(r'^[A-Za-z]:\\',s) is not None or 'file://' in s or '/../' in s or '..\\' in s
def scan_payload_for_forbidden_terms(p):
 s=json.dumps(p,sort_keys=True); f=scan_text_for_forbidden_terms(s)
 if has_private_path(s): f.append('private_path')
 return sorted(set(f))
is_public_rights=lambda r:(r or '').lower() in PUBLIC_RIGHTS
load_current_preservation=lambda r: load_json(Path(r)/'preservation/soil/current_preservation.json')
load_preservation_manifest=lambda r,p: load_json(Path(r)/f'preservation/soil/packages/{p}/preservation_manifest.json')
load_preservation_receipt=lambda r,p: load_json(Path(r)/f'preservation/soil/packages/{p}/preservation_receipt.json')
load_fixity_manifest=lambda r,p: load_json(Path(r)/f'preservation/soil/packages/{p}/fixity_manifest.json')
load_merkle_tree=lambda r,p: load_json(Path(r)/f'preservation/soil/packages/{p}/merkle_tree.json')
load_reconciliation_status=lambda r: load_json(Path(r)/'federation/soil/current_reconciliation.json')
load_operational_status=lambda r: load_json(Path(r)/'ops/soil/status/current_status.json')
def release_is_retracted(pub_root,release_id):
 p=Path(pub_root)/'published/soil/retractions'
 return p.exists() and any(load_json(x).get('release_id')==release_id and load_json(x).get('status')=='RETRACTED' for x in p.glob('*.retraction_notice.json'))
def load_withdrawal_reconciliation(r,release_id):
 p=Path(r)/f'federation/soil/withdrawals/{sanitize_id(release_id)}.withdrawal_receipt.json'; return load_json(p) if p.exists() else None
def recompute_merkle_root(leaves):
 cur=[x for x in leaves]
 if not cur: return ''
 while len(cur)>1:
  if len(cur)%2: cur.append(cur[-1])
  cur=[sha256_bytes((cur[i]+cur[i+1]).encode()) for i in range(0,len(cur),2)]
 return cur[0]
def validate_archive_inputs(manifest,receipt,ops):
 rs=[]
 if manifest.get('preservation_status')!='PRESERVATION_READY': rs.append('preservation_status not ready')
 if receipt.get('decision')!='pass' or not receipt.get('signatures'): rs.append('preservation receipt invalid')
 if receipt.get('live_archive_upload_performed') is not False: rs.append('live archive upload true')
 if receipt.get('live_doi_minting_performed') is not False: rs.append('live doi minting true')
 if not ops.get('public_access_allowed'): rs.append('public access blocked')
 if ops.get('latest_probe',{}).get('decision')!='pass': rs.append('latest probe not pass')
 for i in ops.get('active_incidents',[]):
  if i.get('severity') in {'critical','high'} and i.get('status')!='resolved': rs.append('unresolved incident')
 for r in manifest.get('records',[]):
  if r.get('sensitivity')!='public': rs.append('private sensitivity')
  if r.get('publication_status')!='PUBLISHED': rs.append('not published')
  if not is_public_rights(r.get('rights_status')): rs.append('rights not public')
  if not r.get('evidence_bundle_ref'): rs.append('missing evidence_bundle_ref')
 return sorted(set(rs))
