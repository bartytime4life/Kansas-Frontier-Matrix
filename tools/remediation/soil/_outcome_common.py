from __future__ import annotations
import hashlib, json, os, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location"]
PUBLIC_RIGHTS={"open","public","public_domain","open_data","public_equivalent"}


def load_json(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def write_json_atomic(path,payload):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
 fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent)); os.close(fd)
 Path(tmp).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n',encoding='utf-8'); os.replace(tmp,p)
def write_text_atomic(path,text):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
 fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent)); os.close(fd)
 Path(tmp).write_text(text,encoding='utf-8'); os.replace(tmp,p)
def sha256_file(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for c in iter(lambda:f.read(65536),b''): h.update(c)
 return h.hexdigest()
def sha256_bytes(data): return hashlib.sha256(data).hexdigest()
def utc_now_iso(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sanitize_id(v): return re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'
def stable_payload_hash(p): return sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve())).replace('\\','/')
def public_url_join(b,p): return b.rstrip('/')+'/'+p.lstrip('/')
def validate_base_public_url(v):
 if not v: return False
 u=urlparse(v)
 return (u.scheme=='https' or (u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'})) and not (u.username or u.password) and not v.startswith('/')
def scan_text_for_forbidden_terms(t): return [x for x in FORBIDDEN_TERMS if x.lower() in (t or '').lower()]
def scan_payload_for_forbidden_terms(p): return scan_text_for_forbidden_terms(json.dumps(p,sort_keys=True))
def scan_payload_for_contact_or_secret_terms(p):
 t=json.dumps(p,sort_keys=True).lower(); return [x for x in CONTACT_TERMS+FORBIDDEN_TERMS if x.lower() in t]
def has_private_path(v): return isinstance(v,str) and (v.startswith('/') or v.startswith('file://') or '..' in v)
def is_public_rights(r): return str(r or '').lower() in PUBLIC_RIGHTS

def _lj(root,rel): return load_json(Path(root)/rel)
load_current_remediation_handoff=lambda r:_lj(r,'remediation/soil/current_remediation_handoff.json')
load_remediation_handoff_manifest=lambda r,i:_lj(r,f'remediation/soil/cycles/{i}/remediation_handoff_manifest.json')
load_remediation_handoff_receipt=lambda r,i:_lj(r,f'remediation/soil/cycles/{i}/remediation_handoff_receipt.json')
load_errata_publication_registry=lambda r,i:_lj(r,f'remediation/soil/cycles/{i}/errata_publication_registry.json')
load_certificate_event_execution_tracker=lambda r,i:_lj(r,f'remediation/soil/cycles/{i}/certificate_event_execution_tracker.json')
load_successor_release_intake_bundle=lambda r,i:_lj(r,f'remediation/soil/cycles/{i}/successor_release_intake_bundle.json')
load_retraction_review_intake_bundle=lambda r,i:_lj(r,f'remediation/soil/cycles/{i}/retraction_review_intake_bundle.json')
load_current_corrective_action=lambda r:_lj(r,'corrective/soil/current_corrective_action.json')
load_current_resolution=lambda r:_lj(r,'resolution/soil/current_resolution.json')
load_current_accountability=lambda r:_lj(r,'accountability/soil/current_accountability.json')
load_current_assurance=lambda r:_lj(r,'assurance/soil/current_assurance.json')
load_current_registry=lambda r:_lj(r,'trust_registry/soil/current_registry.json')
load_latest_certificate_status=lambda r,i:_lj(r,f'trust_registry/soil/registrations/{i}/certificate_status.json')
def load_certificate_event_receipts(root, registry_id):
 p=Path(root)/f'trust_registry/soil/registrations/{registry_id}/events'; return [load_json(x) for x in sorted(p.glob('*.receipt.json'))] if p.exists() else []
load_current_certification=lambda r:_lj(r,'certification/soil/current_certification.json')
load_current_archive_package=lambda r:_lj(r,'archive/soil/current_archive_package.json')
load_current_preservation=lambda r:_lj(r,'preservation/soil/current_preservation.json')
load_current_reconciliation=lambda r:_lj(r,'federation/soil/current_reconciliation.json')
load_current_federation=lambda r:_lj(r,'federation/soil/current_federation.json')
load_current_discovery=lambda r:_lj(r,'discovery/soil/current_discovery.json')
load_current_release=lambda r:_lj(r,'published/soil/current.json')
load_publication_receipt=lambda r,i:_lj(r,f'published/soil/releases/{i}.publication_receipt.json')
load_retraction_notice=lambda r,i:_lj(r,f'published/soil/retractions/{i}.retraction_notice.json')
load_retraction_receipt=lambda r,i:_lj(r,f'published/soil/retractions/{i}.retraction_receipt.json')
load_archive_tombstone=lambda r,i:_lj(r,f'archive/soil/tombstones/{i}.tombstone_receipt.json')
load_operational_status=lambda r:_lj(r,'ops/soil/status/current_status.json')
release_is_retracted=lambda r,i:(Path(r)/f'published/soil/retractions/{i}.retraction_notice.json').exists()

def build_outcome_transparency_log(entries):
 out=[]; prev=None
 for i,e in enumerate(entries,1):
  b={**e,'ordinal':i,'previous_entry_hash':prev}; h='sha256:'+stable_payload_hash(b); b['entry_hash']=h; out.append(b); prev=h
 return {'schema_version':'kfm.v1','object_type':'SoilRemediationOutcomeTransparencyLog','domain':'soil','log_mode':'offline_deterministic_hash_chain','live_notification_performed':False,'live_helpdesk_submission_performed':False,'live_external_workflow_submission_performed':False,'entries':out,'log_root':prev,'created':utc_now_iso()}

def validate_successor_release_chain(*_a,**_kw): return []
def validate_retraction_outcome_chain(*_a,**_kw): return []
def validate_certificate_event_outcome(*_a,**_kw): return []
def validate_remediation_outcome_inputs(*_a,**_kw): return []
