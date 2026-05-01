import hashlib, json, os, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location"]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def write_json_atomic(path,payload):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(dir=p.parent,prefix=p.name,suffix='.tmp')
    with os.fdopen(fd,'w',encoding='utf-8') as f:
        json.dump(payload,f,indent=2,sort_keys=True); f.write('\n')
    os.replace(tmp,p)

def write_text_atomic(path,text):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(dir=p.parent,prefix=p.name,suffix='.tmp')
    with os.fdopen(fd,'w',encoding='utf-8') as f: f.write(text)
    os.replace(tmp,p)

sha256_file=lambda p:'sha256:'+hashlib.sha256(Path(p).read_bytes()).hexdigest()
sha256_bytes=lambda b:'sha256:'+hashlib.sha256(b).hexdigest()
utc_now_iso=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
sanitize_id=lambda v: re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'
canonical_json=lambda p: json.dumps(p,sort_keys=True,separators=(',',':'))
stable_payload_hash=lambda p: sha256_bytes(canonical_json(p).encode())

def safe_rel_ref(path,root):
    return str(Path(path).resolve().relative_to(Path(root).resolve())).replace('\\','/')

public_url_join=lambda b,p: urljoin(b.rstrip('/')+'/', p.lstrip('/'))

def validate_base_public_url(value):
    u=urlparse(value or '')
    if u.scheme not in {'https','http'} or not u.netloc or u.username or u.password: return False
    if u.scheme=='http' and u.hostname not in {'127.0.0.1','localhost'}: return False
    return True

scan_text_for_forbidden_terms=lambda t:[x for x in FORBIDDEN_TERMS if x.lower() in str(t).lower()]
scan_payload_for_forbidden_terms=lambda p: scan_text_for_forbidden_terms(json.dumps(p,sort_keys=True))
scan_payload_for_contact_or_secret_terms=lambda p:[x for x in CONTACT_TERMS+["token","secret","password","api_key"] if x.lower() in json.dumps(p).lower()]
has_private_path=lambda v: isinstance(v,str) and (v.startswith('/') or 'file://' in v or 'ftp://' in v or '..' in v)
is_public_rights=lambda r: str(r).lower() in {'open','public','public_open','open_data'}

def _load_current(root,sub,current):
    p=Path(root)/sub/current
    return load_json(p) if p.exists() else {}

def load_current_public_routing(routing_root): return _load_current(routing_root,'routing/soil/','current_public_routing.json')
def load_public_routing_manifest(routing_root, routing_id): return load_json(Path(routing_root)/'routing/soil/routes'/routing_id/'public_routing_manifest.json')
def load_public_routing_receipt(routing_root, routing_id): return load_json(Path(routing_root)/'routing/soil/routes'/routing_id/'public_routing_receipt.json')
def load_active_endpoint_routing_table(routing_root, routing_id): return load_json(Path(routing_root)/'routing/soil/routes'/routing_id/'active_endpoint_routing_table.json')
def load_compatibility_redirect_map(routing_root, routing_id): return load_json(Path(routing_root)/'routing/soil/routes'/routing_id/'compatibility_redirect_map.json')
def load_active_read_model_projection(routing_root, routing_id): return load_json(Path(routing_root)/'routing/soil/routes'/routing_id/'active_read_model_projection.json')
def load_route_policy_matrix(routing_root, routing_id): return load_json(Path(routing_root)/'routing/soil/routes'/routing_id/'route_policy_matrix.json')
def load_route_verification_report(routing_root, routing_id): return load_json(Path(routing_root)/'routing/soil/routes'/routing_id/'route_verification_report.json')

def load_current_active_release(active_root): return _load_current(active_root,'active_release/soil/','current_active_release.json')
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
    p=Path(r)/'published/soil/releases'/i/'publication_receipt.json'
    return load_json(p) if p.exists() else load_json(Path(r)/'published/soil/receipts'/f'{i}.publication_receipt.json')
load_operational_status=lambda r:_load_current(r,'ops/soil/status/','current_status.json')
release_is_retracted=lambda r,i:(Path(r)/'published/soil/retractions'/f'{i}.retraction_notice.json').exists()

def build_delivery_transparency_log(entries):
    prev=None; out=[]
    for i,e in enumerate(entries,1):
        item=dict(e); item['ordinal']=i; item['previous_entry_hash']=prev
        hsrc={k:v for k,v in item.items() if k!='entry_hash'}
        item['entry_hash']=sha256_bytes(canonical_json(hsrc).encode())
        prev=item['entry_hash']; out.append(item)
    return {'entries':out,'log_root':prev}
compute_response_etag=lambda b: sha256_bytes(b)

def validate_kfm_headers(headers, expected_state='PUBLIC_ROUTING_RECONCILED'):
    return headers.get('X-KFM-Domain')=='soil' and headers.get('X-KFM-State')==expected_state and bool(headers.get('X-KFM-Routing-ID')) and bool(headers.get('X-KFM-Routing-State')) and 'X-KFM-Active-Public-Routes-Enabled' in headers

def validate_probe_result(result): return result.get('result')=='pass'
def validate_active_read_model_parity(x): return x.get('parity_passed') is True

def validate_public_delivery_inputs(base_public_url):
    reasons=[]
    if not validate_base_public_url(base_public_url): reasons.append('invalid base_public_url')
    return (not reasons,reasons)
