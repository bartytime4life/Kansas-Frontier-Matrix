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
sha256_file=lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest(); sha256_bytes=lambda data: hashlib.sha256(data).hexdigest(); utc_now_iso=lambda: dt.datetime.now(dt.timezone.utc).isoformat(); sanitize_id=lambda v: re.sub(r'[^A-Za-z0-9._-]','_',v or '') or 'id'; public_url_join=lambda b,p:b.rstrip('/')+'/'+p.lstrip('/'); safe_rel_ref=lambda p,r:str(Path(p).resolve().relative_to(Path(r).resolve()))
def validate_base_public_url(value):
 u=urlparse(value or '');
 return bool(value and u.scheme in {'https','http'} and not u.username and not u.password and (u.scheme!='http' or u.hostname in {'localhost','127.0.0.1'}))
scan_text_for_forbidden_terms=lambda t: sorted({x for x in FORBIDDEN_TERMS if x.lower() in (t or '').lower()})
def has_private_path(value):
 s=str(value or ''); return s.startswith('/') or re.match(r'^[A-Za-z]:\\',s) is not None or 'file://' in s or '/../' in s

def scan_payload_for_forbidden_terms(payload):
 s=json.dumps(payload,sort_keys=True); f=scan_text_for_forbidden_terms(s); return sorted(set(f+(['private_path'] if has_private_path(s) else [])))
is_public_rights=lambda r:(r or '').lower() in PUBLIC_RIGHTS
load_current_discovery=lambda root: load_json(Path(root)/'discovery/soil/current_discovery.json')
load_discovery_manifest=lambda root,did: load_json(Path(root)/f'discovery/soil/releases/{did}/discovery_manifest.json')
load_discovery_receipt=lambda root,did: load_json(Path(root)/f'discovery/soil/releases/{did}/discovery_receipt.json')
load_current_release=lambda root: load_json(Path(root)/'published/soil/current.json')
load_operational_status=lambda root: load_json(Path(root)/'ops/soil/status/current_status.json')
load_status_receipt=lambda root: load_json(Path(root)/'ops/soil/status/status_receipt.json')
def load_retraction_notices(root):
 p=Path(root)/'published/soil/retractions'; return [load_json(x) for x in sorted(p.glob('*.retraction_notice.json'))] if p.exists() else []
def release_is_retracted(root,release_id): return any(n.get('release_id')==release_id and n.get('status')=='RETRACTED' for n in load_retraction_notices(root))
def stable_payload_hash(payload): return sha256_bytes(json.dumps(payload,sort_keys=True,separators=(',',':')).encode())
def deterministic_federation_id(inputs): return 'soil-federation-'+sha256_bytes(json.dumps(inputs,sort_keys=True).encode())[:16]
def validate_federation_inputs(discovery_root,published_root,ops_root,discovery_id):
 r=[]; d=load_discovery_manifest(discovery_root,discovery_id); dr=load_discovery_receipt(discovery_root,discovery_id); st=load_operational_status(ops_root); sr=load_status_receipt(ops_root); cur=load_current_release(published_root)
 rid=d.get('release_id')
 if d.get('discovery_status')!='DISCOVERABLE': r.append('discovery_status not DISCOVERABLE')
 if dr.get('decision')!='pass' or not dr.get('signatures'): r.append('discovery receipt blocked')
 if cur.get('current_release_id')!=rid: r.append('current published release mismatch')
 if release_is_retracted(published_root,rid): r.append('release retracted')
 if st.get('latest_probe_decision')!='pass' or st.get('public_access_allowed') is not True: r.append('status blocked')
 if not sr.get('signatures'): r.append('status receipt signatures missing')
 ai=st.get('active_incidents',[])
 if any(i.get('status')!='resolved' and i.get('severity')=='critical' for i in ai): r.append('unresolved critical incident')
 if any(i.get('status')!='resolved' and i.get('severity')=='high' and i.get('category') in {'security','rights'} for i in ai): r.append('unresolved high security/rights incident')
 for rec in d.get('records',[]):
  if rec.get('sensitivity')!='public': r.append('private sensitivity')
  if rec.get('publication_status')!='PUBLISHED': r.append('publication_status not PUBLISHED')
  if not is_public_rights(rec.get('rights_status')): r.append('unknown rights')
  if not rec.get('policy_label'): r.append('missing policy_label')
  for k in ['evidence_bundle_ref','stac_ref','dcat_ref','prov_ref','triplet_ref']:
   if not rec.get(k): r.append(f'missing {k}')
 if scan_payload_for_forbidden_terms(d): r.append('forbidden terms in discovery payload')
 return sorted(set(r)),d,dr,st,sr
