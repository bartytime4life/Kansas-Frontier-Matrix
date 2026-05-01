#!/usr/bin/env python3
from __future__ import annotations
import datetime as dt, hashlib, json, os, re, tempfile
from pathlib import Path
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
PUBLIC_RIGHTS={"open","public","public_aggregate","public_safe","public_reviewed"}
load_json=lambda path: json.loads(Path(path).read_text(encoding='utf-8'))

def write_json_atomic(path,payload):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent));os.close(fd);Path(tmp).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n',encoding='utf-8');os.replace(tmp,p)
def write_text_atomic(path,text):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent));os.close(fd);Path(tmp).write_text(text,encoding='utf-8');os.replace(tmp,p)
sha256_file=lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
sha256_bytes=lambda data: hashlib.sha256(data).hexdigest()
utc_now_iso=lambda: dt.datetime.now(dt.timezone.utc).isoformat()
sanitize_id=lambda value: re.sub(r'[^A-Za-z0-9._-]','_',value or '') or 'id'
public_url_join=lambda base_url,path: base_url.rstrip('/')+'/'+path.lstrip('/')
safe_rel_ref=lambda path,root: str(Path(path).resolve().relative_to(Path(root).resolve()))
scan_text_for_forbidden_terms=lambda text: sorted({x for x in FORBIDDEN_TERMS if x.lower() in (text or '').lower()})
has_private_path=lambda value: str(value or '').startswith('/') or re.match(r'^[A-Za-z]:\\',str(value or '')) is not None or 'file://' in str(value or '')

def scan_payload_for_forbidden_terms(payload):
 s=json.dumps(payload,sort_keys=True); f=scan_text_for_forbidden_terms(s)
 return sorted(set(f+(['private_path'] if has_private_path(s) else [])))

is_public_rights=lambda rights_status: (rights_status or '').lower() in PUBLIC_RIGHTS

def _validate_base_public_url(url):
 u=urlparse(url or '')
 return bool(url and u.scheme in {'https','http'} and not u.username and not u.password and (u.scheme!='http' or u.hostname in {'localhost','127.0.0.1'}))

def load_current_release(published_root): return load_json(Path(published_root)/'published/soil/current.json')['current_release_id']
load_published_manifest=lambda published_root,release_id: load_json(Path(published_root)/f'published/soil/releases/{release_id}/manifest.json')
load_published_index=lambda published_root,release_id: load_json(Path(published_root)/f'published/soil/releases/{release_id}/index.json')
load_publication_receipt=lambda published_root,release_id: load_json(Path(published_root)/f'published/soil/releases/{release_id}/publication_receipt.json')
load_operational_status=lambda ops_root: load_json(Path(ops_root)/'ops/soil/status/current_status.json')
load_status_receipt=lambda ops_root: load_json(Path(ops_root)/'ops/soil/status/status_receipt.json')
def load_retraction_notices(published_root):
 p=Path(published_root)/'published/soil/retractions'; return [load_json(x) for x in sorted(p.glob('*.retraction_notice.json'))] if p.exists() else []
def release_is_retracted(published_root, release_id): return any(n.get('release_id')==release_id and n.get('status')=='RETRACTED' for n in load_retraction_notices(published_root))

def validate_discovery_inputs(published_root, ops_root, release_id, base_public_url=None):
 r=[]
 if base_public_url is not None and not _validate_base_public_url(base_public_url): r.append('invalid base_public_url')
 try: m=load_published_manifest(published_root,release_id); idx=load_published_index(published_root,release_id); pr=load_publication_receipt(published_root,release_id)
 except Exception as e: return [f'missing published inputs: {e}']
 if m.get('state')!='PUBLISHED': r.append('release state not PUBLISHED')
 if pr.get('decision')!='pass': r.append('publication receipt decision not pass')
 if release_is_retracted(published_root,release_id): r.append('release retracted')
 try: st=load_operational_status(ops_root); sr=load_status_receipt(ops_root)
 except Exception as e: return r+[f'missing operational status inputs: {e}']
 if st.get('latest_probe_decision')!='pass': r.append('latest probe not pass')
 if st.get('service_state') not in {'operational','degraded'}: r.append('service_state blocked')
 if st.get('public_access_allowed') is not True: r.append('public_access disallowed')
 if not sr.get('signatures'): r.append('status receipt signatures missing')
 ai=st.get('active_incidents',[])
 if any(i.get('status')!='resolved' and i.get('severity')=='critical' for i in ai): r.append('unresolved critical incident')
 if any(i.get('status')!='resolved' and i.get('severity')=='high' and i.get('category') in {'security','rights'} for i in ai): r.append('unresolved high security/rights incident')
 for rec in idx.get('records',[]):
  if rec.get('sensitivity')!='public': r.append('private sensitivity'); break
  if not is_public_rights(rec.get('rights_status')): r.append('unknown rights'); break
  if not rec.get('policy_label'): r.append('missing policy_label'); break
  for k in ['evidence_bundle_ref','stac_ref','dcat_ref','prov_ref','triplet_ref']:
   if not rec.get(k): r.append(f'missing {k}')
 if scan_payload_for_forbidden_terms(idx): r.append('forbidden terms in public index')
 return sorted(set(r))
