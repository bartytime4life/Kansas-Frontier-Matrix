#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.fauna.gbif_publication_ops_validator import stable_hash

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--package',required=True);ap.add_argument('--withdrawal-reason',required=True);ap.add_argument('--reviewer',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
 p=json.loads(Path(a.package).read_text())
 out={"withdrawal_receipt_id":"gbif_withdrawal_TEST_001","publication_package_id":p.get('publication_package_id'),"withdrawal_reason":a.withdrawal_reason,"public_use_allowed":False,"replacement_publication_package_id":None,"affected_answer_ids":p.get('answer_ids',[]),"affected_ui_card_ids":p.get('ui_card_ids',[]),"affected_claim_ids":p.get('claim_ids',[]),"reviewer_required":True,"reviewer":{"actor_type":"steward","actor_id":a.reviewer},"audit_ledger_entry_ref":"gbif_audit_TEST_WITHDRAWAL_001","created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','withdrawal_receipt_id','kfm:spec_hash'))
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n'); print('ok')
if __name__=='__main__':main()
