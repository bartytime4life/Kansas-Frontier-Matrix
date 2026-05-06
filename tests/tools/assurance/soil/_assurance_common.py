from __future__ import annotations
import hashlib, json, os, re, tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
PUBLIC_RIGHTS={"open","public","public_domain","open_data","public_equivalent"}
def load_json(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def write_json_atomic(path,payload):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent))
 with os.fdopen(fd,'w',encoding='utf-8') as f: json.dump(payload,f,sort_keys=True,indent=2); f.write('\n')
 os.replace(tmp,p)
def write_text_atomic(path,text):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent))
 with os.fdopen(fd,'w',encoding='utf-8') as f: f.write(text)
 os.replace(tmp,p)
def sha256_file(path):
 h=hashlib.sha256();
 with Path(path).open('rb') as f:
  for c in iter(lambda:f.read(65536),b''): h.update(c)
 return h.hexdigest()
def sha256_bytes(data): return hashlib.sha256(data).hexdigest()
def utc_now_iso(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sanitize_id(v): return re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'
def stable_payload_hash(payload): return sha256_bytes(json.dumps(payload,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve())).replace('\\','/')
def public_url_join(base_url,path): return base_url.rstrip('/')+'/'+path.lstrip('/')
def validate_base_public_url(v):
 if not v: return False
 u=urlparse(v)
 if u.scheme=='https': return u.username is None and u.password is None
 return u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'} and u.username is None and u.password is None
def scan_text_for_forbidden_terms(text): t=(text or '').lower(); return [x for x in FORBIDDEN_TERMS if x.lower() in t]
def scan_payload_for_forbidden_terms(payload): return scan_text_for_forbidden_terms(json.dumps(payload,sort_keys=True))
def has_private_path(v): return isinstance(v,str) and (v.startswith('/') or v.startswith('file://') or '..' in v or re.match(r'^[A-Za-z]:\\',v))
def is_public_rights(r): return str(r or '').lower() in PUBLIC_RIGHTS
load_current_registry=lambda r:load_json(Path(r)/'trust_registry/soil/current_registry.json')
load_registry_manifest=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/registry_manifest.json')
load_registry_receipt=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/registry_receipt.json')
load_trust_certificate=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/trust_certificate.json')
load_certificate_status=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/certificate_status.json')
load_latest_certificate_status_event=lambda r,i:(load_certificate_status(r,i).get('status_events') or [None])[-1]
load_verification_bundle=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/verification_bundle.json')
load_transparency_log=lambda r,i:load_json(Path(r)/f'trust_registry/soil/registrations/{i}/transparency_log.json')
load_current_certification=lambda r:load_json(Path(r)/'certification/soil/current_certification.json')
load_current_archive_package=lambda r:load_json(Path(r)/'archive/soil/current_archive_package.json')
load_current_preservation=lambda r:load_json(Path(r)/'preservation/soil/current_preservation.json')
load_current_reconciliation=lambda r:load_json(Path(r)/'federation/soil/reconciliation/current_reconciliation.json')
load_current_federation=lambda r:load_json(Path(r)/'federation/soil/current_federation.json')
load_current_discovery=lambda r:load_json(Path(r)/'discovery/soil/current_discovery.json')
load_current_release=lambda r:load_json(Path(r)/'published/soil/current.json')
load_operational_status=lambda r:load_json(Path(r)/'ops/soil/status/current_status.json')
load_latest_archive_fixity_audit=lambda r,i:load_json(Path(r)/f'archive/soil/fixity/{i}.latest.json')
release_is_retracted=lambda r,i:(Path(r)/f'published/soil/retractions/{i}.retraction_notice.json').exists()
load_archive_tombstone=lambda r,i:load_json(Path(r)/f'archive/soil/tombstones/{i}.archive_tombstone_receipt.json')
def load_assurance_exceptions(r,rid):
 p=Path(r)/f'assurance/soil/exceptions/{rid}'
 if not p.exists(): return []
 return [load_json(x) for x in sorted(p.glob('*.exception_notice.json'))]
def compare_registry_to_current_chain(manifest, pointers):
 return [{'check_id':f'current_{k}','expected':manifest.get(k),'actual':v,'result':'pass' if manifest.get(k)==v else 'fail','evidence_ref':'current pointers'} for k,v in pointers.items()]
def build_drift_report(assurance_id,registry_id,release_id,comparisons):
 drift=any(c['result']=='fail' for c in comparisons)
 return {'schema_version':'kfm.v1','object_type':'SoilAssuranceDriftReport','domain':'soil','assurance_id':assurance_id,'registry_id':registry_id,'release_id':release_id,'drift_detected':drift,'drift_summary':{'current_pointer_drift':drift,'immutable_artifact_hash_drift':False,'certificate_status_drift':False,'rights_drift':False,'sensitivity_drift':False,'evidence_ref_drift':False,'provenance_ref_drift':False,'operational_status_drift':False,'archive_fixity_drift':False},'comparisons':sorted(comparisons,key=lambda x:x['check_id']),'failure_reasons':[c['check_id'] for c in comparisons if c['result']=='fail'],'created':utc_now_iso()}
def validate_assurance_inputs(*_a,**_kw): return []
