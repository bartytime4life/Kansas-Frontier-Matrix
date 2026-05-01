from __future__ import annotations
import datetime as dt, hashlib, json, os, re, tempfile
from pathlib import Path
FORBIDDEN_TERMS=("RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key")
load_json=lambda p: json.loads(Path(p).read_text(encoding='utf-8'))

def sha256_bytes(data:bytes)->str: return 'sha256:'+hashlib.sha256(data).hexdigest()
def sha256_file(path)->str: return sha256_bytes(Path(path).read_bytes())
def utc_now_iso()->str: return dt.datetime.now(dt.timezone.utc).isoformat()
def sanitize_id(value:str)->str: return re.sub(r'[^A-Za-z0-9._-]','_',value or '') or 'id'
def write_json_atomic(path,payload):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix='.tmp_',dir=str(p.parent))
 with os.fdopen(fd,'w',encoding='utf-8') as f: f.write(json.dumps(payload,sort_keys=True,indent=2)+'\n')
 os.replace(tmp,p)
def scan_text_for_forbidden_terms(text:str)->list[str]:
 t=(text or '').lower(); return sorted({x for x in FORBIDDEN_TERMS if x.lower() in t})
def scan_payload_for_forbidden_terms(payload)->list[str]: return scan_text_for_forbidden_terms(json.dumps(payload,sort_keys=True,ensure_ascii=False))
def is_public_rights(rights_status)->bool: return str(rights_status or '').lower() in {'open','public','public_aggregate','public_safe','public_reviewed'}
def safe_public_ref(value):
 s=str(value or '')
 return '' if os.path.isabs(s) or '..' in Path(s).parts else s
def deterministic_probe_id(payload)->str: return 'probe-'+hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:16]
def load_current_release(published_root):
 cur=load_json(Path(published_root)/'published/soil/current.json'); rid=cur.get('current_release_id')
 if not rid: raise ValueError('no active current release')
 return rid
def load_retraction_notices(published_root):
 r=Path(published_root)/'published/soil/retractions'
 return [load_json(p) for p in sorted(r.glob('*.retraction_notice.json'))] if r.exists() else []
def release_is_retracted(published_root, release_id): return any(x.get('release_id')==release_id for x in load_retraction_notices(published_root))
def latest_probe_receipts(out_root):
 d=Path(out_root)/'ops/soil/probes'; items=[load_json(p) for p in sorted(d.glob('*.probe_receipt.json'))] if d.exists() else []
 return sorted(items,key=lambda x:x.get('created',''))
def summarize_probe_receipts(receipts): return {'count':len(receipts),'latest_probe_id':(receipts[-1].get('probe_id') if receipts else None),'latest_decision':(receipts[-1].get('decision') if receipts else None)}
