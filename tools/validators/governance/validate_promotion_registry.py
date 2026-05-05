#!/usr/bin/env python3
from __future__ import annotations
import json,hashlib,sys
from pathlib import Path
from datetime import datetime
from jsonschema import Draft202012Validator
BLOCKED=("raw","work","quarantine","candidate","private","secret","token")

def canon_hash(p:Path)->str:
 o=json.loads(p.read_text(encoding='utf-8'))
 c=json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
 return hashlib.sha256(c).hexdigest()

def ts(v:str): return datetime.fromisoformat(v.replace('Z','+00:00'))

def validate(path:Path):
 r=[]
 reg=json.loads(path.read_text(encoding='utf-8'))
 sch=json.loads(Path('schemas/governance/promotion_evidence_registry.schema.json').read_text())
 for e in Draft202012Validator(sch).iter_errors(reg): r.append(f"schema:{e.message}")
 art=reg.get('artifact',{})
 sp=art.get('spec_hash')
 if not sp: r.append('missing artifact.spec_hash')
 ap=Path(art.get('path',''))
 if ap.exists() and sp and canon_hash(ap)!=sp: r.append('spec_hash mismatch')
 if not reg.get('decision_log',{}).get('allow',False): r.append('decision_log allow must be true')
 rr=reg.get('run_receipt',{})
 if rr.get('decision_id')!=reg.get('decision_log',{}).get('decision_id'): r.append('run_receipt decision_id mismatch')
 if rr.get('spec_hash')!=sp: r.append('run_receipt spec_hash mismatch')
 if not reg.get('steward_attestation'): r.append('missing steward_attestation')
 s=reg.get('signing',{})
 if not(s.get('local_stub_signature') or (s.get('signature') and s.get('certificate'))): r.append('unsigned artifact')
 if not reg.get('gatehouse_registration',{}).get('receipt_id'): r.append('missing gatehouse receipt')
 try:
  if ts(reg['publish_manifest']['published_at'])<ts(reg['gatehouse_registration']['registered_at']): r.append('publish before registration')
 except Exception: r.append('invalid registration/publish timestamps')
 for key in (art.get('public_path',''), reg.get('publish_manifest',{}).get('path','')):
  lk=key.lower()
  if any(b in lk for b in BLOCKED): r.append(f'forbidden public path:{key}')
 ok=not r
 return {"ok":ok,"registry_id":reg.get('registry_id'),"errors":r}

if __name__=='__main__':
 if len(sys.argv)!=2:
  print('usage: validate_promotion_registry.py <registry.json>');sys.exit(2)
 out=validate(Path(sys.argv[1]))
 print(json.dumps(out,sort_keys=True,separators=(',',':')))
 sys.exit(0 if out['ok'] else 1)
