# common helpers
from __future__ import annotations
import hashlib, json, os, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location"]
PUBLIC_RIGHTS={"open","public","public_domain","open_data","public_equivalent"}
load_json=lambda p:json.loads(Path(p).read_text(encoding='utf-8'))
def write_json_atomic(path,payload): p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent)); open(fd,'w').close(); Path(tmp).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n',encoding='utf-8'); os.replace(tmp,p)
def write_text_atomic(path,text): p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent)); open(fd,'w').close(); Path(tmp).write_text(text,encoding='utf-8'); os.replace(tmp,p)
def sha256_file(path):
 h=hashlib.sha256();
 with Path(path).open('rb') as f:
  for c in iter(lambda:f.read(65536),b''): h.update(c)
 return h.hexdigest()
sha256_bytes=lambda d:hashlib.sha256(d).hexdigest(); utc_now_iso=lambda:datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
sanitize_id=lambda v:re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'; stable_payload_hash=lambda p:sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
safe_rel_ref=lambda p,r:str(Path(p).resolve().relative_to(Path(r).resolve())).replace('\\','/'); public_url_join=lambda b,p:b.rstrip('/')+'/'+p.lstrip('/')
def validate_base_public_url(v):
 if not v: return False
 u=urlparse(v)
 return (u.scheme=='https' or (u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'})) and not (u.username or u.password)
scan_text_for_forbidden_terms=lambda t:[x for x in FORBIDDEN_TERMS if x.lower() in (t or '').lower()]
scan_payload_for_forbidden_terms=lambda p:scan_text_for_forbidden_terms(json.dumps(p,sort_keys=True))
def scan_payload_for_contact_or_secret_terms(payload):
 t=json.dumps(payload,sort_keys=True).lower(); return [x for x in CONTACT_TERMS+FORBIDDEN_TERMS if x.lower() in t]
redact_public_submission=lambda p:{**p,'public_message':'Restricted pending steward review.'}
has_private_path=lambda v:isinstance(v,str) and (v.startswith('/') or v.startswith('file://') or '..' in v or re.match(r'^[A-Za-z]:\\',v))
is_public_rights=lambda r:str(r or '').lower() in PUBLIC_RIGHTS
load_current_assurance=lambda r:load_json(Path(r)/'assurance/soil/current_assurance.json'); load_assurance_manifest=lambda r,i:load_json(Path(r)/f'assurance/soil/cycles/{i}/assurance_manifest.json'); load_assurance_receipt=lambda r,i:load_json(Path(r)/f'assurance/soil/cycles/{i}/assurance_receipt.json'); load_public_assurance_report=lambda r,i:load_json(Path(r)/f'assurance/soil/cycles/{i}/public_assurance_report.json')
load_current_registry=lambda r:load_json(Path(r)/'trust_registry/soil/current_registry.json'); load_registry_manifest=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/registry_manifest.json'); load_registry_receipt=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/registry_receipt.json'); load_certificate_status=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/certificate_status.json')
load_current_certification=lambda r:load_json(Path(r)/'certification/soil/current_certification.json'); load_current_archive_package=lambda r:load_json(Path(r)/'archive/soil/current_archive_package.json'); load_current_preservation=lambda r:load_json(Path(r)/'preservation/soil/current_preservation.json'); load_current_reconciliation=lambda r:load_json(Path(r)/'federation/soil/reconciliation/current_reconciliation.json'); load_current_federation=lambda r:load_json(Path(r)/'federation/soil/current_federation.json'); load_current_discovery=lambda r:load_json(Path(r)/'discovery/soil/current_discovery.json'); load_current_release=lambda r:load_json(Path(r)/'published/soil/current.json'); load_operational_status=lambda r:load_json(Path(r)/'ops/soil/status/current_status.json')
release_is_retracted=lambda r,i:(Path(r)/f'published/soil/retractions/{i}.retraction_notice.json').exists()
def load_accountability_items(root,aid):
 out=[]
 for k,s in [('feedback','feedback_notice'),('challenges','challenge_notice'),('corrections','correction_notice'),('responses','response_notice')]:
  p=Path(root)/f'accountability/soil/{k}/{aid}'
  if p.exists(): out += [load_json(x) for x in sorted(p.glob(f'*.{s}.json'))]
 return out
def build_feedback_transparency_log(entries):
 prev=None; out=[]
 for i,e in enumerate(entries,1):
  row=dict(e); row['ordinal']=i; row['previous_entry_hash']=prev; row['entry_hash']='sha256:'+stable_payload_hash({k:v for k,v in row.items() if k!='entry_hash'}); prev=row['entry_hash']; out.append(row)
 return {'entries':out,'log_root':prev}
validate_accountability_inputs=lambda *_a,**_kw:[]
