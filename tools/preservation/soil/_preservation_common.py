#!/usr/bin/env python3
from __future__ import annotations
import datetime as dt, hashlib, json, os, re, tempfile
from pathlib import Path
from urllib.parse import urljoin, urlparse
FORBIDDEN_TERMS=["RAW","WORK","QUARANTINE","PROCESSED","api_key","token","secret","password","bearer","private_key","access_key","authorization","cookie"]
PUBLIC_RIGHTS={"open","public","public_aggregate","public_safe","public_reviewed"}
load_json=lambda p: json.loads(Path(p).read_text(encoding='utf-8'))
def write_json_atomic(path,payload):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent));os.close(fd);Path(tmp).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n',encoding='utf-8');os.replace(tmp,p)
def write_text_atomic(path,text):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(prefix=p.name,dir=str(p.parent));os.close(fd);Path(tmp).write_text(text,encoding='utf-8');os.replace(tmp,p)
sha256_file=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest(); sha256_bytes=lambda d: hashlib.sha256(d).hexdigest(); utc_now_iso=lambda: dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')
sanitize_id=lambda v: re.sub(r'[^A-Za-z0-9._-]','_',str(v or '')) or 'id'
stable_payload_hash=lambda p: sha256_bytes(json.dumps(p,sort_keys=True,separators=(',',':')).encode())
def safe_rel_ref(path,root): return str(Path(path).resolve().relative_to(Path(root).resolve()))
def public_url_join(base_url,path): return urljoin(base_url.rstrip('/')+'/',str(path).lstrip('/'))
def validate_base_public_url(v):
 u=urlparse(str(v or '')); return (u.scheme=='https' and u.netloc and not u.username and not u.password) or (u.scheme=='http' and u.hostname in {'localhost','127.0.0.1'} and not u.username and not u.password)
scan_text_for_forbidden_terms=lambda t: sorted({x for x in FORBIDDEN_TERMS if x.lower() in (t or '').lower()})
def has_private_path(v):
 s=str(v or ''); return s.startswith('/') or re.match(r'^[A-Za-z]:\\',s) is not None or 'file://' in s or '/../' in s or '..\\' in s
def scan_payload_for_forbidden_terms(p):
 s=json.dumps(p,sort_keys=True); f=scan_text_for_forbidden_terms(s)
 if has_private_path(s): f.append('private_path')
 return sorted(set(f))
is_public_rights=lambda r:(r or '').lower() in PUBLIC_RIGHTS
load_current_reconciliation=lambda r: load_json(Path(r)/'federation/soil/current_reconciliation.json')
load_reconciliation_manifest=lambda r,i: load_json(Path(r)/f'federation/soil/reconciliations/{i}/reconciliation_manifest.json')
load_reconciliation_receipt=lambda r,i: load_json(Path(r)/f'federation/soil/reconciliations/{i}/reconciliation_receipt.json')
load_external_status=lambda r,i: load_json(Path(r)/f'federation/soil/reconciliations/{i}/external_status.json')
load_current_federation=lambda r: load_json(Path(r)/'federation/soil/current_federation.json')
load_current_discovery=lambda r: load_json(Path(r)/'discovery/soil/current_discovery.json')
load_current_release=lambda r: load_json(Path(r)/'published/soil/current.json')
load_operational_status=lambda r: load_json(Path(r)/'ops/soil/status/current_status.json')
def release_is_retracted(pub_root,release_id):
 p=Path(pub_root)/'published/soil/retractions'
 return p.exists() and any(load_json(x).get('release_id')==release_id and load_json(x).get('status')=='RETRACTED' for x in p.glob('*.retraction_notice.json'))
def load_withdrawal_reconciliation(r,release_id):
 p=Path(r)/f'federation/soil/withdrawals/{sanitize_id(release_id)}.withdrawal_receipt.json'; return load_json(p) if p.exists() else None
def collect_public_source_artifacts(rr,fr,dr,pr,oroot,rid,fid,did,rel):
 return [('reconciliation_manifest.json',Path(rr)/f'federation/soil/reconciliations/{rid}/reconciliation_manifest.json','reconciliation_package'),('reconciliation_receipt.json',Path(rr)/f'federation/soil/reconciliations/{rid}/reconciliation_receipt.json','receipts'),('federation_manifest.json',Path(fr)/f'federation/soil/releases/{fid}/federation_manifest.json','federation_package'),('federation_receipt.json',Path(fr)/f'federation/soil/releases/{fid}/federation_receipt.json','receipts'),('discovery_manifest.json',Path(dr)/f'discovery/soil/releases/{did}/discovery_manifest.json','discovery_package'),('discovery_receipt.json',Path(dr)/f'discovery/soil/releases/{did}/discovery_receipt.json','receipts'),('published_manifest.json',Path(pr)/f'published/soil/releases/{rel}/manifest.json','published_release'),('publication_receipt.json',Path(pr)/f'published/soil/releases/{rel}/publication_receipt.json','receipts'),('operational_status.json',Path(oroot)/'ops/soil/status/current_status.json','operational_status'),('status_receipt.json',Path(oroot)/'ops/soil/status/status_receipt.json','receipts')]
def build_merkle_tree(preservation_id,leaves,created):
 cur=[l['sha256'] for l in leaves]; levels=[cur]
 while len(cur)>1:
  if len(cur)%2==1: cur=cur+[cur[-1]]
  cur=[sha256_bytes((cur[i]+cur[i+1]).encode()) for i in range(0,len(cur),2)]; levels.append(cur)
 return {'schema_version':'kfm.v1','object_type':'SoilPreservationMerkleTree','domain':'soil','preservation_id':preservation_id,'algorithm':'sha256','leaf_count':len(leaves),'leaves':leaves,'levels':levels,'merkle_root':levels[-1][0] if levels and levels[-1] else '','created':created}
def validate_preservation_inputs(recm,recr,ext,cf,cd,cp,ops):
 rs=[]
 if recm.get('reconciliation_status')!='FEDERATION_RECONCILED': rs.append('reconciliation_status not FEDERATION_RECONCILED')
 if ext.get('status') not in {'accepted','degraded'}: rs.append('external_federation_state invalid')
 if recr.get('decision') not in {'pass','degraded'} or not recr.get('signatures'): rs.append('invalid reconciliation receipt')
 if cf.get('active_federation_id')!=recm.get('federation_id'): rs.append('current federation mismatch')
 if cd.get('active_discovery_id')!=recm.get('discovery_id'): rs.append('current discovery mismatch')
 if cp.get('current_release_id')!=recm.get('release_id'): rs.append('current release mismatch')
 if not ops.get('public_access_allowed'): rs.append('public access blocked')
 if ops.get('latest_probe',{}).get('decision')!='pass': rs.append('latest probe not pass')
 if ops.get('mirror_audit',{}).get('decision')!='pass': rs.append('mirror audit failed')
 for r in recm.get('records',[]):
  if r.get('sensitivity')!='public': rs.append('private/restricted sensitivity')
  if r.get('publication_status')!='PUBLISHED': rs.append('record not PUBLISHED')
  if not is_public_rights(r.get('rights_status')): rs.append('unknown/non-public rights')
  if not r.get('evidence_bundle_ref'): rs.append('missing evidence_bundle_ref')
 return sorted(set(rs))
