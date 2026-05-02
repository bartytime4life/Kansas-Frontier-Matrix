#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from pathlib import Path
import jsonschema,hashlib
from jsonschema import Draft202012Validator

def canon_hash(p:Path)->str:
 o=json.loads(p.read_text(encoding="utf-8"))
 return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")).hexdigest()

def validate(path:Path):
 reg=json.loads(path.read_text(encoding="utf-8"))
 sch=json.loads(Path("schemas/governance/promotion_evidence_registry.schema.json").read_text())
 errors=[f"schema:{e.message}" for e in Draft202012Validator(sch).iter_errors(reg)]
 if not reg.get("decision_log",{}).get("allow",False): errors.append("decision_log allow must be true")
 if not reg.get("steward_attestation"): errors.append("missing steward_attestation")
 if reg.get("artifact",{}).get("spec_hash") and Path(reg["artifact"]["path"]).exists() and canon_hash(Path(reg["artifact"]["path"]))!=reg["artifact"]["spec_hash"]: errors.append("spec_hash mismatch")
 return {"ok":not errors,"errors":errors}

def main(req_path:Path)->int:
 try:req=json.loads(req_path.read_text(encoding='utf-8'))
 except Exception as e:
  print(json.dumps({"schema_version":"PromotionReplayResult.v1","outcome":"ERROR","checks":[],"errors":[str(e)]}));return 1
 try:
  regp=Path(req['registry_path']); idxp=Path(req['receipt_index_path'])
  reg=json.loads(regp.read_text()); idx=json.loads(idxp.read_text())
 except Exception as e:
  print(json.dumps({"schema_version":"PromotionReplayResult.v1","outcome":"ERROR","checks":[],"errors":[str(e)]}));return 1
 checks=[];errs=[]
 v=validate(regp)
 checks.append({"name":"validator","ok":v['ok']})
 if not v['ok']:
  if any('missing steward_attestation' in x for x in v['errors']):
   out='ABSTAIN'
  else: out='DENY'
  errs=v['errors']
 else:
  expected=canon_hash(Path(reg['artifact']['path']))
  found=next((r for r in idx.get('records',[]) if r.get('registry_id')==reg.get('registry_id')),None)
  if not found: out='ABSTAIN'; errs=['receipt index missing registry_id']
  elif found.get('spec_hash')!=expected: out='DENY'; errs=['receipt index hash mismatch']
  else: out='VERIFIED'
 print(json.dumps({"schema_version":"PromotionReplayResult.v1","outcome":out,"checks":checks,"errors":errs},sort_keys=True,separators=(',',':')))
 return 0 if out=='VERIFIED' else 1

if __name__=='__main__': sys.exit(main(Path(sys.argv[1])))
