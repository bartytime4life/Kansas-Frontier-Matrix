#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, os, re
from pathlib import Path
FORBIDDEN_PATH_TERMS=("RAW","WORK","QUARANTINE","PROCESSED")
SECRET_TERMS=("api_key","token","secret","password","bearer","private_key","access_key")
PUBLIC_RIGHTS={"open","public","public_aggregate","public_safe","public_reviewed"}

def load_json(path:Path)->dict:
 d=json.loads(path.read_text());
 if not isinstance(d,dict): raise ValueError(f"expected object at {path}")
 return d

def sha256_file(path:Path)->str: return hashlib.sha256(path.read_bytes()).hexdigest()
def sanitize_id(value:str)->str: return re.sub(r"[^A-Za-z0-9._-]","_",value or "") or "release"
def safe_join(root:Path,ref:str)->Path:
 if not isinstance(ref,str) or not ref: raise ValueError("invalid ref")
 if os.path.isabs(ref) or ".." in Path(ref).parts: raise ValueError(f"unsafe ref: {ref}")
 p=(root/ref).resolve();rr=root.resolve()
 if rr!=p and rr not in p.parents: raise ValueError(f"ref escapes root: {ref}")
 return p

def scan_public_payload_for_forbidden_terms(payload:object)->list[str]:
 txt=json.dumps(payload,sort_keys=True).lower();return sorted(set(t for t in SECRET_TERMS if t in txt))
def is_public_rights(rights_status:str)->bool: return rights_status in PUBLIC_RIGHTS
def is_retracted(published_root:Path,release_id:str)->bool: return (published_root/"published/soil/retractions"/f"{sanitize_id(release_id)}.retraction_notice.json").exists()

def _check_hashes(root:Path,mapping:dict,reasons:list[str],label:str)->bool:
 ok=True
 for ref,expected in sorted((mapping or {}).items()):
  if Path(ref).name in {'manifest.json','publication_receipt.json'}: continue
  try:
   p=safe_join(root,ref)
   if not p.exists() or sha256_file(p)!=expected: reasons.append(f"{label} hash mismatch: {ref}");ok=False
  except Exception as exc:
   reasons.append(f"{label} invalid ref {ref}: {exc}");ok=False
 return ok

def validate_published_release(published_root:Path,release_id:str)->dict:
 reasons=[];checks={};rel=published_root/"published/soil/releases"/release_id
 man=load_json(rel/"manifest.json");idx=load_json(rel/"index.json");rec=load_json(rel/"publication_receipt.json")
 checks["manifest_shape"]=man.get("object_type")=="PublishedReleaseManifest" and man.get("domain")=="soil" and man.get("state")=="PUBLISHED"
 checks["bundle_count"]=man.get("bundle_count")==len(man.get("bundles") or [])
 checks["receipt_shape"]=rec.get("receipt_type")=="PublicationReceipt" and rec.get("from_state")=="CATALOG/TRIPLET" and rec.get("to_state")=="PUBLISHED" and rec.get("decision")=="pass" and bool(rec.get("signatures"))
 checks["index_shape"]=idx.get("object_type")=="SoilPublicReadModel"
 if not checks["manifest_shape"]: reasons.append("manifest shape invalid")
 if not checks["bundle_count"]: reasons.append("bundle_count mismatch")
 if not checks["receipt_shape"]: reasons.append("publication receipt invalid")
 if not checks["index_shape"]: reasons.append("index shape invalid")
 for r in idx.get("records") or []:
  if r.get("publication_status")!="PUBLISHED": reasons.append("record not PUBLISHED")
  if not is_public_rights(r.get("rights_status")): reasons.append("record rights not public")
  if not r.get("policy_label"): reasons.append("missing policy_label")
  if r.get("sensitivity")!="public": reasons.append("non-public sensitivity")
  for fld in ("evidence_bundle_ref","stac_ref","dcat_ref","prov_ref","triplet_ref"):
   if not r.get(fld): reasons.append(f"missing {fld}")
 for fc in sorted((rel/"focus_cards").glob("*.json")):
  c=load_json(fc)
  if c.get("provisional") is not False: reasons.append("focus card provisional")
  if c.get("status")!="PUBLISHED": reasons.append("focus card status")
  if (c.get("truth_policy") or {}).get("model_output_is_truth_source") is not False: reasons.append("focus card truth policy")
 checks["manifest_hashes"]=_check_hashes(rel,man.get("artifact_hashes") or {},reasons,"manifest")
 checks["receipt_hashes"]=_check_hashes(rel,rec.get("published_artifacts") or {},reasons,"receipt")
 payloads=[man,idx,rec]+[load_json(p) for p in sorted((rel/"focus_cards").glob("*.json"))]
 for payload in payloads:
  txt=json.dumps(payload)
  if any(t in txt for t in FORBIDDEN_PATH_TERMS): reasons.append("forbidden lifecycle path reference")
  secrets=scan_public_payload_for_forbidden_terms(payload)
  if secrets: reasons.append(f"secret-like terms found: {','.join(secrets)}")
 return {"valid":not reasons,"reasons":sorted(set(reasons)),"checks":checks,"release_dir":rel,"manifest":man,"index":idx,"publication_receipt":rec}
