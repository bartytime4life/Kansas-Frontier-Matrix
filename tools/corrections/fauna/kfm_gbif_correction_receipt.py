#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys,hashlib
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.fauna.gbif_publication_ops_validator import stable_hash

def h(v): return 'sha256:'+hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--original-package',required=True);ap.add_argument('--corrected-package',required=True);ap.add_argument('--correction-type',required=True);ap.add_argument('--correction-reason',required=True);ap.add_argument('--reviewer',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
 o=json.loads(Path(a.original_package).read_text()); c=json.loads(Path(a.corrected_package).read_text())
 changed=[]
 if o.get('limitations')!=c.get('limitations'): changed.append({"path":"$.limitations","old_value_hash":h(o.get('limitations')),"new_value_hash":h(c.get('limitations'))})
 if not changed: raise SystemExit('no changed_fields detected')
 out={"correction_receipt_id":"gbif_correction_TEST_001","publication_package_id":o.get('publication_package_id'),"corrected_publication_package_id":c.get('publication_package_id'),"correction_type":a.correction_type,"correction_reason":a.correction_reason,"changed_fields":changed,"requires_withdrawal":False,"reviewer_required":True,"reviewer":{"actor_type":"steward","actor_id":a.reviewer},"audit_ledger_entry_ref":"gbif_audit_TEST_CORRECTION_001","created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','correction_receipt_id','kfm:spec_hash'))
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n'); print('ok')
if __name__=='__main__':main()
