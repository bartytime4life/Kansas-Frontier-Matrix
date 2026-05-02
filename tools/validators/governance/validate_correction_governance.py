#!/usr/bin/env python3
from __future__ import annotations
import json,sys,hashlib
from pathlib import Path
from datetime import datetime
from jsonschema import Draft202012Validator
BLOCKED=("raw","work","quarantine","private","candidate","secret","token")
REASONS={"DATA_FIX","POLICY_ALIGNMENT","METADATA_FIX"}
MAP={"CorrectionNotice":"correction_notice","WithdrawalNotice":"withdrawal_notice","RollbackPlan":"rollback_plan","RollbackExecutionReceipt":"rollback_execution_receipt","PromotionCorrectionLedger":"promotion_correction_ledger","PublicCorrectionIndex":"public_correction_index"}

def cjson(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def has_blocked(v:str)->bool: return any(b in v.lower() for b in BLOCKED)
def t(s): return datetime.fromisoformat(s.replace('Z','+00:00'))

def validate(path:Path):
 obj=json.loads(path.read_text(encoding='utf-8')); errs=[]
 k=obj.get('object_type'); sv=obj.get('schema_version')
 if k not in MAP or sv!='v1': errs.append('unknown object_type/schema_version')
 else:
  sch=json.loads(Path(f"schemas/governance/{MAP[k]}.schema.json").read_text())
  errs += [f"schema:{e.message}" for e in Draft202012Validator(sch).iter_errors(obj)]
 for f in ('source_promotion_registry_ref','prior_decision_log_ref','prior_run_receipt_ref'):
  if f in obj and not obj.get(f): errs.append(f'missing {f}')
 if k=='CorrectionNotice':
  if obj.get('reason_code') not in REASONS: errs.append('invalid reason_code')
  if obj.get('mutates_original_receipt') is True: errs.append('mutation of original receipt denied')
  if not obj.get('authority',{}).get('actor'): errs.append('missing authority')
 if k=='WithdrawalNotice':
  if not obj.get('authority',{}).get('actor'): errs.append('missing authority')
  if not obj.get('preserve_audit_chain',False): errs.append('withdrawal must preserve audit chain')
 if k=='RollbackPlan':
  if has_blocked(obj.get('target_public_path','')): errs.append('rollback target path not public-safe')
  if obj.get('target_release_id')=='rel-unknown': errs.append('unknown target release')
 if k=='PublicCorrectionIndex':
  for i in obj.get('items',[]):
   if has_blocked(i.get('public_notice_path','')): errs.append('public index exposes private path')
 if k=='PromotionCorrectionLedger':
  es=obj.get('entries',[])
  ids=set();last=None
  for e in es:
   if e['event_id'] in ids: errs.append('duplicate event_id')
   ids.add(e['event_id'])
   ts=t(e['timestamp'])
   if last and ts<last: errs.append('out-of-order timestamps')
   last=ts
   eh=e.get('entry_hash')
   calc=hashlib.sha256(cjson({"event_id":e['event_id'],"event_type":e['event_type'],"timestamp":e['timestamp']}).encode()).hexdigest()
   if eh!=calc: errs.append(f"entry hash mismatch:{e['event_id']}")
  ch=hashlib.sha256(''.join(e.get('entry_hash','') for e in es).encode()).hexdigest()
  if obj.get('chain_hash')!=ch: errs.append('chain_hash mismatch')
 return {"ok":not errs,"object_type":k,"schema_version":sv,"errors":errs}

if __name__=='__main__':
 out=validate(Path(sys.argv[1])); print(cjson(out)); sys.exit(0 if out['ok'] else 1)
