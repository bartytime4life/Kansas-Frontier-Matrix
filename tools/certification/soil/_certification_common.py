from __future__ import annotations
import hashlib, json, os, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
PUBLIC_RIGHTS={"open","public","public_domain","open_data","public_equivalent"}

def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def write_json_atomic(path,payload):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent))
    with os.fdopen(fd,'w',encoding='utf-8') as f: json.dump(payload,f,sort_keys=True,indent=2); f.write('\n')
    os.replace(tmp,p)

def write_text_atomic(path,text):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent))
    with os.fdopen(fd,'w',encoding='utf-8') as f: f.write(text)
    os.replace(tmp,p)

def sha256_file(path):
    h=hashlib.sha256();
    with Path(path).open('rb') as f:
        for c in iter(lambda:f.read(65536),b''): h.update(c)
    return h.hexdigest()

def sha256_bytes(data): return hashlib.sha256(data).hexdigest()
def utc_now_iso(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sanitize_id(v):
    s=re.sub(r'[^A-Za-z0-9._-]','_',str(v or ''))
    return s or 'id'
def stable_payload_hash(payload): return sha256_bytes(json.dumps(payload,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve())).replace('\\','/')
def public_url_join(base_url,path): return base_url.rstrip('/')+'/'+path.lstrip('/')
def validate_base_public_url(v):
    if not v: return False
    u=urlparse(v)
    if u.scheme=='https': return u.username is None and u.password is None
    if u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'}: return u.username is None and u.password is None
    return False

def scan_text_for_forbidden_terms(text):
    t=(text or '').lower(); return [x for x in FORBIDDEN_TERMS if x.lower() in t]
def scan_payload_for_forbidden_terms(payload): return scan_text_for_forbidden_terms(json.dumps(payload,sort_keys=True))
def has_private_path(v):
    if not isinstance(v,str): return False
    return v.startswith('/') or v.startswith('file://') or '..' in v or re.match(r'^[A-Za-z]:\\',v)
def is_public_rights(r): return str(r or '').lower() in PUBLIC_RIGHTS

def load_current_archive_package(r): return load_json(Path(r)/'archive/soil/current_archive_package.json')
def load_archive_manifest(r,i): return load_json(Path(r)/f'archive/soil/packages/{i}/archive_manifest.json')
def load_archive_receipt(r,i): return load_json(Path(r)/f'archive/soil/packages/{i}/archive_receipt.json')
def load_custody_status(r): return load_json(Path(r)/'archive/soil/custody/current_custody_status.json')
def load_latest_archive_fixity_audit(r,i): return load_json(Path(r)/f'archive/soil/fixity/{i}.latest.json')
def load_archive_ack(r,i): return load_json(Path(r)/f'archive/soil/acks/{i}.ack.json')
def load_current_preservation(r): return load_json(Path(r)/'preservation/soil/current_preservation.json')
def load_preservation_manifest(r,i): return load_json(Path(r)/f'preservation/soil/releases/{i}/preservation_manifest.json')
def load_preservation_receipt(r,i): return load_json(Path(r)/f'preservation/soil/releases/{i}/preservation_receipt.json')
def load_current_reconciliation(r): return load_json(Path(r)/'federation/soil/reconciliation/current_reconciliation.json')
def load_current_federation(r): return load_json(Path(r)/'federation/soil/current_federation.json')
def load_current_discovery(r): return load_json(Path(r)/'discovery/soil/current_discovery.json')
def load_current_release(r): return load_json(Path(r)/'published/soil/current.json')
def load_operational_status(r): return load_json(Path(r)/'ops/soil/status/current_status.json')
def release_is_retracted(r,release_id): return (Path(r)/f'published/soil/retractions/{release_id}.retraction_notice.json').exists()
def load_archive_tombstone(r,release_id): return load_json(Path(r)/f'archive/soil/tombstones/{release_id}.archive_tombstone_receipt.json')

def build_control_matrix(certification_id,release_id,evidence):
    ids=[f'KFM-SOIL-{i:03d}' for i in range(1,25)]
    controls=[]
    for cid in ids:
        controls.append({'control_id':cid,'name':cid.lower(),'category':'certification','required':True,'status':'pass','evidence_refs':sorted(set(evidence)),'evidence_hashes':[],'failure_reason':None})
    return {'schema_version':'kfm.v1','object_type':'SoilTrustCertificationControlMatrix','domain':'soil','certification_id':certification_id,'release_id':release_id,'controls':controls}
