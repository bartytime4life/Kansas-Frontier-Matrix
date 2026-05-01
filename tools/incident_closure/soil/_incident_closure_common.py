#!/usr/bin/env python3
import hashlib, json, os, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location","ip_address","client_ip","user_agent","x_forwarded_for"]
load_json=lambda path: json.loads(Path(path).read_text(encoding='utf-8'))
def write_text_atomic(path,text):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent)); os.close(fd); Path(tmp).write_text(text,encoding='utf-8'); os.replace(tmp,p)
def write_json_atomic(path,payload): write_text_atomic(path,json.dumps(payload,sort_keys=True,indent=2)+'\n')
sha256_file=lambda p:'sha256:'+hashlib.sha256(Path(p).read_bytes()).hexdigest()
sha256_bytes=lambda b:'sha256:'+hashlib.sha256(b).hexdigest()
utc_now_iso=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
sanitize_id=lambda v:(re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id')
stable_payload_hash=lambda p: sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
safe_rel_ref=lambda p,r: str(Path(p).resolve().relative_to(Path(r).resolve()))
public_url_join=lambda b,p:b.rstrip('/')+'/'+p.lstrip('/')
def validate_base_public_url(v):
 u=urlparse(str(v or '')); return (u.scheme=='https' and u.netloc and '@' not in u.netloc) or (u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'} and '@' not in u.netloc)
def scan_text_for_forbidden_terms(t):
 s=str(t).lower(); return any(x.lower() in s for x in FORBIDDEN_TERMS)
scan_payload_for_forbidden_terms=lambda p: scan_text_for_forbidden_terms(json.dumps(p,sort_keys=True))
def scan_payload_for_contact_or_secret_terms(p):
 s=json.dumps(p,sort_keys=True).lower(); return any(x in s for x in [*map(str.lower,CONTACT_TERMS),'secret','token','authorization','cookie'])
scan_access_payload_for_private_fields=scan_payload_for_contact_or_secret_terms
has_private_path=lambda v: str(v or '').startswith('/') or '..' in str(v or '') or bool(re.search(r'^[A-Za-z]:\\',str(v or '')))
is_public_rights=lambda r:str(r or '').lower() in {'public','open','cc-by-4.0','cc0','open_data'}

def _load(root,rel): return load_json(Path(root)/rel)
load_current_delivery_incident_response=lambda r:_load(r,'incident_response/soil/current_delivery_incident_response.json')
load_delivery_incident_response_manifest=lambda r,i:_load(r,f'incident_response/soil/cycles/{i}/delivery_incident_response_manifest.json')
load_delivery_incident_response_receipt=lambda r,i:_load(r,f'incident_response/soil/cycles/{i}/delivery_incident_response_receipt.json')
load_delivery_incident_declaration_registry=lambda r,i:_load(r,f'incident_response/soil/cycles/{i}/incident_declaration_registry.json')
load_safe_mode_routing_recommendation_packet=lambda r,i:_load(r,f'incident_response/soil/cycles/{i}/safe_mode_routing_recommendation_packet.json')
load_mitigation_action_ledger=lambda r,i:_load(r,f'incident_response/soil/cycles/{i}/mitigation_action_ledger.json')
load_recovery_verification_registry=lambda r,i:_load(r,f'incident_response/soil/cycles/{i}/recovery_verification_registry.json')
