import hashlib, json, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
CONTACT_TERMS=["email","phone","address","ssn","social_security","driver_license","credit_card","bank_account","precise_home_location","ip_address","client_ip","user_agent","x_forwarded_for"]

def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def write_json_atomic(path,payload):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile('w',delete=False,dir=p.parent,encoding='utf-8') as f:
        json.dump(payload,f,indent=2,sort_keys=True);f.write('\n');tmp=f.name
    Path(tmp).replace(p)

def write_text_atomic(path,text):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile('w',delete=False,dir=p.parent,encoding='utf-8') as f:
        f.write(text);tmp=f.name
    Path(tmp).replace(p)

def sha256_file(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def sha256_bytes(data): return hashlib.sha256(data).hexdigest()
def utc_now_iso(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sanitize_id(v):
    s=''.join(c if (c.isalnum() or c in '._-') else '_' for c in str(v or ''))
    return s or 'id'
def stable_payload_hash(payload): return sha256_bytes(json.dumps(payload,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve()))
def public_url_join(base_url,path): return base_url.rstrip('/')+'/'+str(path).lstrip('/')
def validate_base_public_url(v):
    u=urlparse(v)
    if u.scheme=='https': return True
    if u.scheme=='http' and u.hostname in ('localhost','127.0.0.1'): return True
    return False

def _scan_text(t,terms):
    s=str(t).lower();
    return [x for x in terms if x.lower() in s]
def scan_payload_for_forbidden_terms(payload): return _scan_text(json.dumps(payload,sort_keys=True),FORBIDDEN_TERMS)
def scan_text_for_forbidden_terms(text): return _scan_text(text,FORBIDDEN_TERMS)
def scan_payload_for_contact_or_secret_terms(payload): return _scan_text(json.dumps(payload,sort_keys=True),CONTACT_TERMS+["secret","token","password"])
def scan_access_payload_for_private_fields(payload): return [k for k in ["authorization","cookie","user_agent","client_ip","ip_address"] if k in json.dumps(payload).lower()]
def has_private_path(v): return bool(re.search(r'(^/|[A-Za-z]:\\)',str(v)))
def is_public_rights(rs): return str(rs).lower() in {"public","open","open-data","open_data"}

def _load_current(root,sub,name):
    p=Path(root)/sub/'soil'/name
    return load_json(p) if p.exists() else {}

def load_current_public_continuity(root): return _load_current(root,'continuity','current_public_delivery_continuity.json')
def load_public_continuity_manifest(root,cid): return load_json(Path(root)/'continuity/soil/cycles'/cid/'public_delivery_continuity_manifest.json')
def load_public_continuity_receipt(root,cid): return load_json(Path(root)/'continuity/soil/cycles'/cid/'public_delivery_continuity_receipt.json')
def load_current_public_resilience(root): return _load_current(root,'resilience','current_public_delivery_resilience.json')
def load_public_resilience_manifest(root,rid): return load_json(Path(root)/'resilience/soil/cycles'/rid/'public_delivery_resilience_manifest.json')
def load_current_delivery_incident_closure(root): return _load_current(root,'incident_closure','current_delivery_incident_closure.json')
def load_current_delivery_incident_response(root): return _load_current(root,'incident_response','current_delivery_incident_response.json')
def load_current_public_observability(root): return _load_current(root,'observability','current_public_delivery_observability.json')
def load_current_public_delivery(root): return _load_current(root,'delivery','current_public_delivery.json')
def load_current_public_routing(root): return _load_current(root,'routing','current_public_routing.json')
def load_current_active_release(root): return _load_current(root,'active_release','current_active_release_pointer.json')
def load_current_lineage(root): return _load_current(root,'lineage','current_lineage.json')
def load_operational_status(root): return load_json(Path(root)/'ops/soil/status/current_status.json')

def build_stability_transparency_log(entries):
    prev=None;out=[]
    for i,e in enumerate(entries,1):
        x=dict(e);x['ordinal']=i;x['previous_entry_hash']=prev
        h=stable_payload_hash(x);x['entry_hash']=h;prev=h;out.append(x)
    return out,prev
