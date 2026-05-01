#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.fauna.gbif_publication_ops_validator import stable_hash

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--package',required=True);ap.add_argument('--replay-verification',required=True);ap.add_argument('--withdrawal-receipt');ap.add_argument('--correction-receipt');ap.add_argument('--output',required=True);a=ap.parse_args()
 pkg=json.loads(Path(a.package).read_text()); rv=json.loads(Path(a.replay_verification).read_text())
 st="published" if rv.get('verification_posture')=='verified' and pkg.get('policy_results',{}).get('passed') else 'blocked'; reason='policy_passed' if st=='published' else 'policy_denied'; superseded_by=None
 w=[]; c=[]
 if a.withdrawal_receipt:
  wr=json.loads(Path(a.withdrawal_receipt).read_text()); w=[wr.get('withdrawal_receipt_id')]; st='withdrawn'; reason='withdrawal_requested'
 if a.correction_receipt:
  cr=json.loads(Path(a.correction_receipt).read_text()); c=[cr.get('correction_receipt_id')]; st='corrected'; reason='correction_applied'; superseded_by=cr.get('corrected_publication_package_id')
 out={"publication_status_id":"gbif_pubstatus_TEST_001","publication_package_id":pkg.get('publication_package_id'),"current_state":st,"previous_state":None,"state_reason":reason,"effective_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),"supersedes":[],"superseded_by":superseded_by,"correction_receipt_refs":c,"withdrawal_receipt_refs":w,"audit_ledger_entry_refs":["gbif_audit_TEST_001"],"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
 out['kfm:spec_hash']=stable_hash(out,exclude=('effective_at','created_at','publication_status_id','kfm:spec_hash'))
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n'); print('ok')
if __name__=='__main__':main()
