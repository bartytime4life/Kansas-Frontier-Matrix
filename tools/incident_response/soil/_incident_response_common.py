#!/usr/bin/env python3
import hashlib, json, os, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location","ip_address","client_ip","user_agent","x_forwarded_for"]
load_json=lambda path: json.loads(Path(path).read_text(encoding="utf-8"))
def write_text_atomic(path,text):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent)); os.close(fd); Path(tmp).write_text(text,encoding='utf-8'); os.replace(tmp,p)
def write_json_atomic(path,payload): write_text_atomic(path,json.dumps(payload,sort_keys=True,indent=2)+"\n")
sha256_file=lambda path:'sha256:'+hashlib.sha256(Path(path).read_bytes()).hexdigest()
sha256_bytes=lambda data:'sha256:'+hashlib.sha256(data).hexdigest()
utc_now_iso=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
sanitize_id=lambda v:(re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id')
stable_payload_hash=lambda payload: sha256_bytes(json.dumps(payload,sort_keys=True,separators=(",",":" )).encode())
safe_rel_ref=lambda path,root: str(Path(path).resolve().relative_to(Path(root).resolve()))
public_url_join=lambda b,p: b.rstrip('/')+'/'+p.lstrip('/')
def validate_base_public_url(value):
 u=urlparse(str(value or '')); return (u.scheme=='https' and u.netloc and '@' not in u.netloc) or (u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'} and '@' not in u.netloc)
def scan_text_for_forbidden_terms(text):
 t=str(text).lower(); return any(x.lower() in t for x in FORBIDDEN_TERMS)
scan_payload_for_forbidden_terms=lambda p: scan_text_for_forbidden_terms(json.dumps(p,sort_keys=True))
def scan_payload_for_contact_or_secret_terms(payload):
 t=json.dumps(payload,sort_keys=True).lower(); return any(x in t for x in [*map(str.lower,CONTACT_TERMS), 'secret','token','authorization','cookie'])
scan_access_payload_for_private_fields=scan_payload_for_contact_or_secret_terms
has_private_path=lambda v: str(v or '').startswith('/') or '..' in str(v or '') or bool(re.search(r'^[A-Za-z]:\\',str(v or '')))
is_public_rights=lambda r: str(r or '').lower() in {'public','open','cc-by-4.0','cc0','open_data'}
def _load(root,rel): return load_json(Path(root)/rel)
load_current_public_observability=lambda r:_load(r,'observability/soil/current_public_observability.json')
load_public_observability_manifest=lambda r,i:_load(r,f'observability/soil/cycles/{i}/public_delivery_observability_manifest.json')
load_public_observability_receipt=lambda r,i:_load(r,f'observability/soil/cycles/{i}/public_observability_receipt.json')
load_delivery_monitor_registry=lambda r,i:_load(r,f'observability/soil/cycles/{i}/delivery_monitor_registry.json')
load_endpoint_slo_matrix=lambda r,i:_load(r,f'observability/soil/cycles/{i}/endpoint_slo_matrix.json')
load_route_error_budget_report=lambda r,i:_load(r,f'observability/soil/cycles/{i}/route_error_budget_report.json')
load_endpoint_response_drift_report=lambda r,i:_load(r,f'observability/soil/cycles/{i}/endpoint_response_drift_report.json')
load_consumer_contract_drift_report=lambda r,i:_load(r,f'observability/soil/cycles/{i}/consumer_contract_drift_report.json')
load_incident_trigger_recommendations=lambda r,i:_load(r,f'observability/soil/cycles/{i}/incident_trigger_recommendations.json')
