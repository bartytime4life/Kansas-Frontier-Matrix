#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.federation.soil._reconciliation_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--reconciliation-root',required=True);a.add_argument('--reconciliation-id');x=a.parse_args(argv)
 rr=Path(x.reconciliation_root)/'federation/soil'; rid=x.reconciliation_id or load_json(rr/'current_reconciliation.json')['active_reconciliation_id']
 rel=rr/'reconciliations'/rid; rs=[]
 m=load_json(rel/'reconciliation_manifest.json'); rc=load_json(rel/'reconciliation_receipt.json')
 if m.get('object_type')!='SoilFederationReconciliationManifest': rs.append('invalid manifest type')
 if m.get('reconciliation_status')!='FEDERATION_RECONCILED': rs.append('invalid reconciliation status')
 if rc.get('receipt_type')!='FederationReconciliationReceipt' or rc.get('from_state')!='FEDERATION_READY' or rc.get('to_state')!='FEDERATION_RECONCILED': rs.append('invalid receipt transition')
 if rc.get('decision') not in {'pass','degraded'} or not rc.get('signatures'): rs.append('invalid receipt decision/signatures')
 if rc.get('live_registry_poll_performed') is not False or rc.get('live_external_submission_performed') is not False: rs.append('live flags must be false')
 for f,h in rc.get('generated_artifacts',{}).items():
  p=rel/f
  if not p.exists() or 'sha256:'+sha256_file(p)!=h: rs.append(f'hash mismatch {f}')
 out={'reconciliation_valid':not rs,'reconciliation_id':rid,'federation_id':m.get('federation_id'),'release_id':m.get('release_id'),'external_federation_state':m.get('external_federation_state'),'failure_reasons':sorted(set(rs))}
 print(json.dumps(out,sort_keys=True)); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
