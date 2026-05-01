#!/usr/bin/env python3
import json, hashlib, re, tempfile, os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location","ip_address","client_ip","user_agent","x_forwarded_for"]

def load_json(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def write_json_atomic(path,payload): write_text_atomic(path,json.dumps(payload,sort_keys=True,indent=2)+"\n")
def write_text_atomic(path,text):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); t=Path(tempfile.mkstemp(prefix=p.name,dir=str(p.parent))[1]); t.write_text(text,encoding='utf-8'); os.replace(t,p)
def sha256_file(path): return 'sha256:'+hashlib.sha256(Path(path).read_bytes()).hexdigest()
def sha256_bytes(data): return 'sha256:'+hashlib.sha256(data).hexdigest()
def utc_now_iso(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sanitize_id(v):
 s=re.sub(r'[^A-Za-z0-9._-]','_',str(v or ''))
 return s or 'id'
def stable_payload_hash(payload): return sha256_bytes(json.dumps(payload,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve()))
def public_url_join(base_url,path): return base_url.rstrip('/')+'/'+path.lstrip('/')
def validate_base_public_url(value):
 try:u=urlparse(value)
 except Exception:return False
 if u.scheme=='https' and u.netloc and '@' not in u.netloc: return True
 return u.scheme=='http' and u.hostname in {'127.0.0.1','localhost'} and '@' not in u.netloc
def scan_text_for_forbidden_terms(text):
 t=str(text).lower(); return any(x.lower() in t for x in FORBIDDEN_TERMS)
def scan_payload_for_forbidden_terms(payload): return scan_text_for_forbidden_terms(json.dumps(payload,sort_keys=True))
def scan_payload_for_contact_or_secret_terms(payload):
 t=json.dumps(payload,sort_keys=True).lower(); return any(x.lower() in t for x in CONTACT_TERMS)
def has_private_path(value):
 s=str(value); return s.startswith('/') or '..' in s or re.search(r'[A-Za-z]:\\',s)
def scan_access_log_for_private_fields(entry):
 t=json.dumps(entry,sort_keys=True).lower()
 bad=['authorization','cookie','user-agent','user_agent','request_body','query','ip','client_ip','token','secret']
 return any(b in t for b in bad)
def is_public_rights(r): return str(r or '').lower() in {'public','open','cc-by-4.0','cc0','open_data'}
def _load(root,rel): return load_json(Path(root)/rel)
def load_current_public_delivery(r): return _load(r,'delivery/soil/current_public_delivery.json')
def load_public_delivery_manifest(r,i): return _load(r,f'delivery/soil/cycles/{i}/public_delivery_manifest.json')
def load_public_delivery_receipt(r,i): return _load(r,f'delivery/soil/cycles/{i}/public_delivery_receipt.json')
def load_route_probe_registry(r,i): return _load(r,f'delivery/soil/cycles/{i}/route_probe_registry.json')
def load_endpoint_response_snapshot_registry(r,i): return _load(r,f'delivery/soil/cycles/{i}/endpoint_response_snapshot_registry.json')
def load_active_read_model_parity_report(r,i): return _load(r,f'delivery/soil/cycles/{i}/active_read_model_parity_report.json')
def load_consumer_contract_status(r,i): return _load(r,f'delivery/soil/cycles/{i}/consumer_contract_status.json')
def load_current_public_routing(r): return _load(r,'routing/soil/current_public_routing.json')
def load_current_active_release(r): return _load(r,'active_release/soil/current_active_release_pointer.json')
def load_current_lineage(r): return _load(r,'lineage/soil/current_lineage.json')
def load_current_remediation_outcome(r): return _load(r,'remediation/soil/current_remediation_outcome.json')
def load_current_remediation_handoff(r): return _load(r,'remediation/soil/current_remediation_handoff.json')
def load_current_corrective_action(r): return _load(r,'corrective_actions/soil/current_corrective_action.json')
def load_current_resolution(r): return _load(r,'resolution/soil/current_resolution.json')
def load_current_accountability(r): return _load(r,'accountability/soil/current_accountability.json')
def load_current_assurance(r): return _load(r,'assurance/soil/current_assurance.json')
def load_current_registry(r): return _load(r,'trust_registry/soil/current_trust_registry.json')
def load_latest_certificate_status(r,registry_id): return 'active'
def load_current_certification(r): return _load(r,'certification/soil/current_certification.json')
def load_current_archive_package(r): return _load(r,'archive/soil/current_archive_package.json')
def load_current_preservation(r): return _load(r,'preservation/soil/current_preservation.json')
def load_current_reconciliation(r): return _load(r,'reconciliation/soil/current_reconciliation.json')
def load_current_federation(r): return _load(r,'federation/soil/current_federation.json')
def load_current_discovery(r): return _load(r,'discovery/soil/current_discovery.json')
def load_current_release(r): return _load(r,'published/soil/current.json')
def load_operational_status(r): return _load(r,'ops/soil/status/current_status.json')
def release_is_retracted(published_root,release_id): return (Path(published_root)/f'published/soil/retractions/{release_id}.retraction_notice.json').exists()
def build_observability_transparency_log(entries):
 prev=None; out=[]
 for i,e in enumerate(entries,1):
  row=dict(e); row['ordinal']=i; row['previous_entry_hash']=prev
  h=stable_payload_hash(row); row['entry_hash']=h; prev=h; out.append(row)
 return {'entries':out,'log_root':prev}
def summarize_monitor_receipts(receipts): return {'count':len(receipts),'latest_decision':receipts[-1]['decision'] if receipts else None}
def summarize_access_log_snapshot(entries): return {'entry_count':sum(e.get('entry_count',0) for e in entries)}
def validate_observability_inputs(base_public_url):
 rs=[]
 if not validate_base_public_url(base_public_url): rs.append('invalid base_public_url')
 return (not rs,rs)
