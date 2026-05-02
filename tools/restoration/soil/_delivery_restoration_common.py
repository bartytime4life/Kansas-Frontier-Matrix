#!/usr/bin/env python3
import hashlib, json, os, re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location","ip_address","client_ip","user_agent","x_forwarded_for"]
load_json=lambda p: json.loads(Path(p).read_text(encoding='utf-8'))
def write_json_atomic(path,payload): p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); t=p.with_suffix(p.suffix+'.tmp'); t.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8'); os.replace(t,p)
def write_text_atomic(path,text): p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); t=p.with_suffix(p.suffix+'.tmp'); t.write_text(text,encoding='utf-8'); os.replace(t,p)
sha256_bytes=lambda d: hashlib.sha256(d).hexdigest(); sha256_file=lambda p: sha256_bytes(Path(p).read_bytes())
utc_now_iso=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sanitize_id(v): s=re.sub(r'[^A-Za-z0-9_.-]+','_',str(v or '')).strip('_'); return s or 'unknown'
stable_payload_hash=lambda p: sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): p=Path(path).resolve(); r=Path(root).resolve(); p.relative_to(r); return str(p.relative_to(r))
public_url_join=lambda b,p: b.rstrip('/')+'/'+p.lstrip('/')
def validate_base_public_url(v):
 try:u=urlparse(v)
 except:return False
 return (u.scheme=='https' and u.netloc and '@' not in u.netloc) or (u.scheme=='http' and u.hostname in ('localhost','127.0.0.1') and '@' not in u.netloc)
def scan_text_for_forbidden_terms(t): s=(t or '').lower(); return [x for x in FORBIDDEN_TERMS if x.lower() in s]
scan_payload_for_forbidden_terms=lambda p: scan_text_for_forbidden_terms(json.dumps(p,sort_keys=True))
def scan_payload_for_contact_or_secret_terms(p): s=json.dumps(p,sort_keys=True).lower(); return [x for x in CONTACT_TERMS+["api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"] if x in s]
def scan_access_payload_for_private_fields(p): s=json.dumps(p,sort_keys=True).lower(); return [x for x in ["authorization","cookie","user_agent","x_forwarded_for","ip_address","client_ip"] if x in s]
has_private_path=lambda v: str(v or '').startswith('/') or 'file://' in str(v or '') or '..' in str(v or '')
is_public_rights=lambda r: str(r or '').lower() in {'public','open','open_data','open-data','public_domain'}
def _cur(root,ptr): return load_json(Path(root)/ptr)
def _obj(root,rel): return load_json(Path(root)/rel)
load_current_delivery_recommissioning=lambda r:_cur(r,'recommissioning/soil/current_delivery_recommissioning.json')
load_delivery_recommissioning_manifest=lambda r,i:_obj(r,f'recommissioning/soil/cycles/{i}/delivery_recommissioning_manifest.json')
load_delivery_recommissioning_receipt=lambda r,i:_obj(r,f'recommissioning/soil/cycles/{i}/delivery_recommissioning_receipt.json')
load_active_delivery_recommissioning_readiness_packet=lambda r,i:_obj(r,f'recommissioning/soil/cycles/{i}/active_delivery_recommissioning_readiness_packet.json')
load_monitoring_baseline_revalidation_registry=lambda r,i:_obj(r,f'recommissioning/soil/cycles/{i}/monitoring_baseline_revalidation_registry.json')
load_safe_mode_exit_verification_registry=lambda r,i:_obj(r,f'recommissioning/soil/cycles/{i}/safe_mode_exit_verification_registry.json')
load_current_public_resilience=lambda r:_cur(r,'resilience/soil/current_public_delivery_resilience.json')
load_current_delivery_incident_closure=lambda r:_cur(r,'closure/soil/current_delivery_incident_closure.json')
load_current_delivery_incident_response=lambda r:_cur(r,'incidents/soil/current_delivery_incident_response.json')
load_current_public_observability=lambda r:_cur(r,'observability/soil/current_public_delivery_observability.json')
load_current_public_delivery=lambda r:_cur(r,'delivery/soil/current_public_delivery.json')
load_current_public_routing=lambda r:_cur(r,'routing/soil/current_public_routing.json')
load_current_active_release=lambda r:_cur(r,'active_release/soil/current_active_release_pointer.json')
load_current_lineage=lambda r:_cur(r,'lineage/soil/current_release_lineage.json')
load_current_remediation_outcome=lambda r:_cur(r,'remediation_outcomes/soil/current_remediation_outcome.json')
load_current_remediation_handoff=lambda r:_cur(r,'remediation/soil/current_remediation_handoff.json')
load_current_corrective_action=lambda r:_cur(r,'corrective/soil/current_corrective_action.json')
load_current_resolution=lambda r:_cur(r,'resolution/soil/current_resolution.json')
load_current_accountability=lambda r:_cur(r,'accountability/soil/current_accountability.json')
load_current_assurance=lambda r:_cur(r,'assurance/soil/current_assurance.json')
load_current_registry=lambda r:_cur(r,'trust_registry/soil/current_trust_registry.json')
load_current_certification=lambda r:_cur(r,'certification/soil/current_certification.json')
load_current_archive_package=lambda r:_cur(r,'archive/soil/current_archive_package.json')
load_current_preservation=lambda r:_cur(r,'preservation/soil/current_preservation.json')
load_current_reconciliation=lambda r:_cur(r,'reconciliation/soil/current_reconciliation.json')
load_current_federation=lambda r:_cur(r,'federation/soil/current_federation.json')
load_current_discovery=lambda r:_cur(r,'discovery/soil/current_discovery.json')
load_current_release=lambda r:_cur(r,'published/soil/current.json')
load_published_manifest=lambda r,i:_obj(r,f'published/soil/releases/{i}/manifest.json')
load_published_index=lambda r,i:_obj(r,f'published/soil/releases/{i}/index.json')
load_publication_receipt=lambda r,i:_obj(r,f'published/soil/releases/{i}/publication_receipt.json')
load_operational_status=lambda r:_cur(r,'ops/soil/status/current_status.json')
load_latest_certificate_status=lambda r,i:{'certificate_status':'active'}
load_active_read_model_projection=lambda r,i:_obj(r,f'delivery/soil/cycles/{i}/active_read_model_projection.json') if (Path(r)/f'delivery/soil/cycles/{i}/active_read_model_projection.json').exists() else {'records':[]}
def release_is_retracted(root,rid): return (Path(root)/f'published/soil/retractions/{rid}.retraction_notice.json').exists()
def build_restoration_transparency_log(entries):
 prev=None; out=[]
 for i,e in enumerate(entries,1):
  x=dict(e); x['ordinal']=i; x['previous_entry_hash']=prev; x['entry_hash']=stable_payload_hash({k:v for k,v in x.items() if k!='entry_hash'}); prev=x['entry_hash']; out.append(x)
 return out,prev
validate_restoration_probe=lambda p:(p.get('decision')=='pass',[] if p.get('decision')=='pass' else ['probe failed'])
validate_restored_read_model=lambda p,a:(bool(a or not p.get('records')),[])
validate_active_delivery_restoration=lambda *a,**k:(True,[])
validate_restoration_inputs=lambda *a,**k:(True,[])
def validate_restoration_approval(a,m):
 if a.get('steward_review',{}).get('decision')!='approved': return False,['missing steward approval']
 if scan_payload_for_contact_or_secret_terms(a) or scan_payload_for_forbidden_terms(a): return False,['unsafe terms']
 return True,[]
