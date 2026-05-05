from __future__ import annotations
import hashlib, json, os, re, tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlparse
from tools.certification.soil._certification_common import FORBIDDEN_TERMS, PUBLIC_RIGHTS

def load_json(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def write_json_atomic(path,payload):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent))
 with os.fdopen(fd,'w',encoding='utf-8') as f: json.dump(payload,f,sort_keys=True,indent=2); f.write('\n')
 os.replace(tmp,p)
def write_text_atomic(path,text):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent))
 with os.fdopen(fd,'w',encoding='utf-8') as f: f.write(text)
 os.replace(tmp,p)
def sha256_file(path):
 h=hashlib.sha256();
 with Path(path).open('rb') as f:
  for c in iter(lambda:f.read(65536),b''): h.update(c)
 return h.hexdigest()
def sha256_bytes(data): return hashlib.sha256(data).hexdigest()
def utc_now_iso(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sanitize_id(v): return re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'
def stable_payload_hash(payload): return sha256_bytes(json.dumps(payload,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve())).replace('\\','/')
def public_url_join(base_url,path): return base_url.rstrip('/')+'/'+path.lstrip('/')
def validate_base_public_url(v):
 if not v: return False
 u=urlparse(v)
 if u.scheme=='https': return u.username is None and u.password is None
 return u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'} and u.username is None and u.password is None
def scan_text_for_forbidden_terms(text): t=(text or '').lower(); return [x for x in FORBIDDEN_TERMS if x.lower() in t]
def scan_payload_for_forbidden_terms(payload): return scan_text_for_forbidden_terms(json.dumps(payload,sort_keys=True))
def has_private_path(v): return isinstance(v,str) and (v.startswith('/') or v.startswith('file://') or '..' in v or re.match(r'^[A-Za-z]:\\',v))
def is_public_rights(r): return str(r or '').lower() in PUBLIC_RIGHTS
load_current_certification=lambda r:load_json(Path(r)/'certification/soil/current_certification.json')
load_certification_manifest=lambda r,i:load_json(Path(r)/f'certification/soil/certifications/{i}/certification_manifest.json')
load_certification_receipt=lambda r,i:load_json(Path(r)/f'certification/soil/certifications/{i}/certification_receipt.json')
load_public_trust_report=lambda r,i:load_json(Path(r)/f'certification/soil/certifications/{i}/public_trust_report.json')
load_control_matrix=lambda r,i:load_json(Path(r)/f'certification/soil/certifications/{i}/control_matrix.json')
load_receipt_chain=lambda r,i:load_json(Path(r)/f'certification/soil/certifications/{i}/receipt_chain.json')
load_current_archive_package=lambda r:load_json(Path(r)/'archive/soil/current_archive_package.json')
load_current_preservation=lambda r:load_json(Path(r)/'preservation/soil/current_preservation.json')
load_current_reconciliation=lambda r:load_json(Path(r)/'federation/soil/reconciliation/current_reconciliation.json')
load_current_federation=lambda r:load_json(Path(r)/'federation/soil/current_federation.json')
load_current_discovery=lambda r:load_json(Path(r)/'discovery/soil/current_discovery.json')
load_current_release=lambda r:load_json(Path(r)/'published/soil/current.json')
load_operational_status=lambda r:load_json(Path(r)/'ops/soil/status/current_status.json')
release_is_retracted=lambda r,i:(Path(r)/f'published/soil/retractions/{i}.retraction_notice.json').exists()
load_archive_tombstone=lambda r,i:load_json(Path(r)/f'archive/soil/tombstones/{i}.archive_tombstone_receipt.json')
def build_hash_chain(entries):
 prev=None; out=[]
 for i,e in enumerate(entries,1):
  row=dict(e); row['ordinal']=i; row['previous_entry_hash']=prev; row['entry_hash']='sha256:'+stable_payload_hash({k:v for k,v in row.items() if k!='entry_hash'}); prev=row['entry_hash']; out.append(row)
 return out, prev

def validate_registry_inputs(*_args,**_kwargs): return []
def public_safe_certificate_payload(payload): return payload
