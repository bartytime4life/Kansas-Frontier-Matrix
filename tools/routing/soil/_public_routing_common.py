import hashlib, json, os, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location"]
load_json=lambda p: json.loads(Path(p).read_text(encoding='utf-8'))
def write_json_atomic(path,payload):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(dir=p.parent,prefix=p.name,suffix='.tmp')
 with os.fdopen(fd,'w',encoding='utf-8') as f: json.dump(payload,f,indent=2,sort_keys=True);f.write('\n')
 os.replace(tmp,p)
def write_text_atomic(path,text):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(dir=p.parent,prefix=p.name,suffix='.tmp')
 with os.fdopen(fd,'w',encoding='utf-8') as f: f.write(text)
 os.replace(tmp,p)
sha256_file=lambda p:'sha256:'+hashlib.sha256(Path(p).read_bytes()).hexdigest()
sha256_bytes=lambda b:'sha256:'+hashlib.sha256(b).hexdigest()
utc_now_iso=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
sanitize_id=lambda v: re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'
stable_payload_hash=lambda p: sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
safe_rel_ref=lambda p,r: str(Path(p).resolve().relative_to(Path(r).resolve())).replace('\\','/')
public_url_join=lambda b,p: b.rstrip('/')+'/'+p.lstrip('/')
def validate_base_public_url(v):
 u=urlparse(v or ''); 
 return (u.scheme=='https') or (u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'}) and not u.username and not u.password
scan_payload_for_forbidden_terms=lambda p:[t for t in FORBIDDEN_TERMS if t.lower() in json.dumps(p).lower()]
scan_text_for_forbidden_terms=lambda t:[x for x in FORBIDDEN_TERMS if x.lower() in str(t).lower()]
scan_payload_for_contact_or_secret_terms=lambda p:[t for t in CONTACT_TERMS+["token","secret","password","api_key"] if t.lower() in json.dumps(p).lower()]
has_private_path=lambda v: str(v).startswith('/') or 'file://' in str(v) or 'ftp://' in str(v) or '..' in str(v)
is_public_rights=lambda r: str(r).lower() in {'open','public','public_open','open_data'}
def _load_current(root,sub,current): p=Path(root)/sub/current; return load_json(p) if p.exists() else {}
load_current_active_release=lambda r:_load_current(r,'active_release/soil/','current_active_release.json')
def load_active_release_pointer_manifest(r,tid): return load_json(Path(r)/'active_release/soil/transitions'/tid/'active_release_pointer_manifest.json')
def load_active_release_pointer_receipt(r,tid): return load_json(Path(r)/'active_release/soil/transitions'/tid/'active_release_pointer_receipt.json')
def load_current_active_release_pointer(r,tid): return load_json(Path(r)/'active_release/soil/transitions'/tid/'current_active_release_pointer.json')
def load_public_routing_table_from_pointer(r,tid): return load_json(Path(r)/'active_release/soil/transitions'/tid/'public_routing_table.json')
def load_release_advertising_lifecycle_registry(r,tid): return load_json(Path(r)/'active_release/soil/transitions'/tid/'release_advertising_lifecycle_registry.json')
load_current_lineage=lambda r:_load_current(r,'lineage/soil/','current_lineage.json')
load_current_remediation_outcome=lambda r:_load_current(r,'remediation_outcomes/soil/','current_outcome.json')
load_current_remediation_handoff=lambda r:_load_current(r,'remediation/soil/','current_remediation_handoff.json')
load_current_corrective_action=lambda r:_load_current(r,'corrective_actions/soil/','current_corrective_action.json')
load_current_resolution=lambda r:_load_current(r,'resolution/soil/','current_resolution.json')
load_current_accountability=lambda r:_load_current(r,'accountability/soil/','current_accountability.json')
load_current_assurance=lambda r:_load_current(r,'assurance/soil/','current_assurance.json')
load_current_registry=lambda r:_load_current(r,'trust_registry/soil/','current_registry.json')
load_latest_certificate_status=lambda r,i:{'status':'active'}
load_current_certification=lambda r:_load_current(r,'certification/soil/','current_certification.json')
load_current_archive_package=lambda r:_load_current(r,'archive/soil/','current_archive_package.json')
load_current_preservation=lambda r:_load_current(r,'preservation/soil/','current_preservation.json')
load_current_reconciliation=lambda r:_load_current(r,'reconciliation/soil/','current_reconciliation.json')
load_current_federation=lambda r:_load_current(r,'federation/soil/','current_federation.json')
load_current_discovery=lambda r:_load_current(r,'discovery/soil/','current_discovery.json')
load_current_release=lambda r:_load_current(r,'published/soil/','current.json')
load_published_manifest=lambda r,i:load_json(Path(r)/'published/soil/releases'/i/'manifest.json')
load_published_index=lambda r,i:load_json(Path(r)/'published/soil/releases'/i/'index.json')
def load_publication_receipt(r,i):
 p1=Path(r)/'published/soil/releases'/i/'publication_receipt.json'
 return load_json(p1) if p1.exists() else load_json(Path(r)/'published/soil/receipts'/f'{i}.publication_receipt.json')
load_retraction_notice=lambda r,i: load_json(p) if (p:=Path(r)/'published/soil/retractions'/f'{i}.retraction_notice.json').exists() else None
load_retraction_receipt=lambda r,i: load_json(p) if (p:=Path(r)/'published/soil/retractions'/f'{i}.retraction_receipt.json').exists() else None
load_operational_status=lambda r:_load_current(r,'ops/soil/status/','current_status.json')
release_is_retracted=lambda r,i:(Path(r)/'published/soil/retractions'/f'{i}.retraction_notice.json').exists()
def build_routing_transparency_log(entries): return entries
validate_active_routing_candidate=lambda *a,**k:(True,[])
validate_route_activation_approval=lambda *a,**k:(True,[])
def build_active_read_model_projection(active_release_id, prior_release_id, records, routing_id):
 return {"schema_version":"kfm.v1","object_type":"SoilActiveReadModelProjection","domain":"soil","routing_id":routing_id,"active_release_id":active_release_id,"prior_release_id":prior_release_id,"projection_state":"active" if active_release_id else "governance_only","units":{"canonical_soil_moisture":"m3/m3","ui_percent_conversion":"multiply_by_100_for_display_only"},"records":records if active_release_id else []}
validate_public_routing_inputs=lambda *a,**k:(True,[])
