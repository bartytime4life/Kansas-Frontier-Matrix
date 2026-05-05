#!/usr/bin/env python3
from __future__ import annotations
import json,sys,hashlib
from pathlib import Path
BLOCKED=("raw","work","quarantine","candidate","private")
def cjson(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False)

def main(p:Path)->int:
 req=json.loads(p.read_text()); idx=json.loads(Path(req['receipt_index_path']).read_text())
 target=next((r for r in idx.get('records',[]) if r.get('release_id')==req.get('target_release_id')),None)
 if not target: print('{"error":"unknown target release"}'); return 1
 if any(b in target.get('public_path','').lower() for b in BLOCKED): print('{"error":"target unpublished/private"}'); return 1
 for f in ('decision_log_ref','run_receipt_ref','spec_hash'):
  if not target.get(f): print('{"error":"missing required prior release evidence"}'); return 1
 out={"object_type":"RollbackPlan","schema_version":"v1","requested_at":req['requested_at'],"requested_by":req['requested_by'],"target_release_id":target['release_id'],"target_public_path":target['public_path'],"target_spec_hash":target['spec_hash'],"source_promotion_registry_ref":req['source_promotion_registry_ref'],"prior_decision_log_ref":target['decision_log_ref'],"prior_run_receipt_ref":target['run_receipt_ref']}
 out['rollback_plan_id']=hashlib.sha256(cjson(out).encode()).hexdigest()[:16]
 print(cjson(out)); return 0
if __name__=='__main__': sys.exit(main(Path(sys.argv[1])))
