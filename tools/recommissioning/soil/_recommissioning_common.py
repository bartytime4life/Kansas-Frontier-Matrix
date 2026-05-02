#!/usr/bin/env python3
import hashlib, json, os, re
from datetime import datetime, timezone
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location","ip_address","client_ip","user_agent","x_forwarded_for"]
load_json=lambda p: json.loads(Path(p).read_text(encoding='utf-8'))
def write_json_atomic(path,payload):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); t=p.with_suffix(p.suffix+'.tmp'); t.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8'); os.replace(t,p)
def write_text_atomic(path,text):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); t=p.with_suffix(p.suffix+'.tmp'); t.write_text(text,encoding='utf-8'); os.replace(t,p)
sha256_bytes=lambda d: hashlib.sha256(d).hexdigest(); sha256_file=lambda p: sha256_bytes(Path(p).read_bytes())
utc_now_iso=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sanitize_id(v):
 s=re.sub(r'[^A-Za-z0-9_.-]+','_',str(v or '')).strip('_'); return s or 'unknown'
stable_payload_hash=lambda p: sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): rp=Path(root).resolve(); p=Path(path).resolve(); p.relative_to(rp); return str(p.relative_to(rp))
public_url_join=lambda b,p: b.rstrip('/')+'/'+p.lstrip('/')
def validate_base_public_url(v):
 try:u=urlparse(v)
 except:return False
 return (u.scheme=='https' and u.netloc and '@' not in u.netloc) or (u.scheme=='http' and u.hostname in ('localhost','127.0.0.1') and '@' not in u.netloc)
def scan_text_for_forbidden_terms(t): s=(t or '').lower(); return [x for x in FORBIDDEN_TERMS if x.lower() in s]
scan_payload_for_forbidden_terms=lambda p: scan_text_for_forbidden_terms(json.dumps(p,sort_keys=True))
def scan_payload_for_contact_or_secret_terms(p): s=json.dumps(p,sort_keys=True).lower(); secret_terms=["api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]; return [x for x in CONTACT_TERMS+secret_terms if x.lower() in s]
def scan_access_payload_for_private_fields(p): s=json.dumps(p,sort_keys=True).lower(); return [k for k in ['authorization','cookie','user_agent','x_forwarded_for','ip_address','client_ip'] if k in s]
has_private_path=lambda v: str(v or '').startswith('/') or 'file://' in str(v or '') or '..' in str(v or '')
is_public_rights=lambda r: str(r or '').lower() in {'public','open','open_data','open-data','public_domain'}
def _lc(root,n): return load_json(Path(root)/n)
load_current_public_resilience=lambda r:_lc(r,'resilience/soil/current_public_delivery_resilience.json')
load_public_resilience_manifest=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/public_delivery_resilience_manifest.json')
load_public_resilience_receipt=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/public_delivery_resilience_receipt.json')
load_resilience_control_adoption_registry=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/resilience_control_adoption_registry.json')
load_monitoring_baseline_update_packet=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/monitoring_baseline_update_packet.json')
load_slo_error_budget_update_packet=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/slo_error_budget_update_packet.json')
load_access_log_safety_rule_update_packet=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/access_log_safety_rule_update_packet.json')
load_consumer_contract_hardening_packet=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/consumer_contract_hardening_packet.json')
load_safe_mode_exit_handoff_packet=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/safe_mode_exit_handoff_packet.json')
load_followup_work_order_registry=lambda r,i: load_json(Path(r)/f'resilience/soil/cycles/{i}/followup_work_order_registry.json')
def build_recommissioning_transparency_log(entries):
 prev=None; out=[]
 for i,e in enumerate(entries,1):
  x=dict(e); x['ordinal']=i; x['previous_entry_hash']=prev; x['entry_hash']=stable_payload_hash({k:v for k,v in x.items() if k!='entry_hash'}); prev=x['entry_hash']; out.append(x)
 return out,prev
validate_followup_completion=lambda r,*a,**k: r.get('completion_status') in {'completed','not_required'}
validate_monitoring_baseline_revalidation=lambda r,*a,**k: r.get('monitor_status') in {'pass','not_required'}
validate_safe_mode_exit_verification=lambda r,*a,**k: r.get('verification_status') in {'verified','remain_governance_only','not_required'}
validate_active_delivery_recommissioning=lambda p,*a,**k: isinstance(p.get('active_public_delivery_recommended'),bool)
validate_recommissioning_inputs=lambda *a,**k:(True,[])
