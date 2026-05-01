from __future__ import annotations
import hashlib, json, os
from pathlib import Path
from tools.audit.soil._published_common import validate_published_release, load_json, is_retracted
FORBIDDEN_LIFECYCLE=("RAW","WORK","QUARANTINE","PROCESSED")
SECRET_TERMS=("api_key","token","secret","password","bearer","private_key","access_key")
def sha256_bytes(data:bytes)->str: return hashlib.sha256(data).hexdigest()
def safe_join(root:Path, ref:str)->Path:
    if not isinstance(ref,str) or not ref or os.path.isabs(ref) or ".." in Path(ref).parts: raise ValueError("unsafe ref")
    p=(root/ref).resolve(); rr=root.resolve()
    if rr!=p and rr not in p.parents: raise ValueError("ref escapes root")
    return p
def public_safe_payload(payload:object)->object:
    if isinstance(payload,dict): return {k:public_safe_payload(v) for k,v in payload.items() if not (isinstance(v,str) and os.path.isabs(v))}
    if isinstance(payload,list): return [public_safe_payload(x) for x in payload]
    return payload
def scan_payload_for_forbidden_terms(payload:object)->list[str]:
    txt=json.dumps(payload, sort_keys=True).lower(); hits=[t.lower() for t in FORBIDDEN_LIFECYCLE if t.lower() in txt]+[t for t in SECRET_TERMS if t in txt]; return sorted(set(hits))
def resolve_active_release(published_root:Path)->str:
    cur=published_root/'published/soil/current.json'
    if not cur.exists(): raise ValueError('current.json missing')
    rid=(load_json(cur).get('current_release_id'))
    if not rid: raise ValueError('no active current release')
    return rid
def validate_service_release(published_root:Path, release_id:str|None):
    reasons=[]; rid=release_id
    if not rid:
        try: rid=resolve_active_release(published_root)
        except Exception as e: return {"valid":False,"reasons":[str(e)]}
    if is_retracted(published_root, rid): reasons.append('release is retracted')
    v=validate_published_release(published_root, rid)
    if not v['valid']: reasons.extend(v['reasons'])
    rec=(published_root/'published/soil/releases'/rid/'publication_receipt.json')
    if not rec.exists(): reasons.append('publication receipt missing')
    else:
        r=load_json(rec)
        if r.get('decision')!='pass': reasons.append('publication receipt decision is not pass')
    return {"valid": not reasons, "reasons": sorted(set(reasons)), "release_id": rid}
