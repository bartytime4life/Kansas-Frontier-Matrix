#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from tools.certification.soil._certification_common import *

def main(argv=None):
 a=argparse.ArgumentParser()
 for n in ['archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root','out-root']: a.add_argument(f'--{n}',required=True)
 a.add_argument('--archive-package-id');x=a.parse_args(argv)
 aid=x.archive_package_id or load_current_archive_package(x.archive_root)['active_archive_package_id']
 am=load_archive_manifest(x.archive_root,aid);rid=am.get('release_id');fail=[]
 refs=[('PublicationReceipt',Path(x.published_root)/f'published/soil/releases/{rid}/publication_receipt.json'),('DiscoveryReceipt',Path(x.discovery_root)/'discovery/soil/releases'/load_current_discovery(x.discovery_root)['active_discovery_id']/'discovery_receipt.json'),('FederationReceipt',Path(x.federation_root)/'federation/soil/releases'/load_current_federation(x.federation_root)['active_federation_id']/'federation_receipt.json'),('FederationReconciliationReceipt',Path(x.reconciliation_root)/'federation/soil/reconciliation/releases'/load_current_reconciliation(x.reconciliation_root)['active_reconciliation_id']/'reconciliation_receipt.json'),('PreservationReceipt',Path(x.preservation_root)/'preservation/soil/releases'/load_current_preservation(x.preservation_root)['active_preservation_id']/'preservation_receipt.json'),('ArchiveCustodyReceipt',Path(x.archive_root)/f'archive/soil/packages/{aid}/archive_receipt.json'),('ArchiveFixityAuditReceipt',Path(x.archive_root)/f'archive/soil/fixity/{aid}.latest.json'),('ArchiveAcknowledgementReceipt',Path(x.archive_root)/f'archive/soil/acks/{aid}.ack.json'),('OperationalStatusReceipt',Path(x.ops_root)/'ops/soil/status/status_receipt.json')]
 chain=[]
 for i,(rt,p) in enumerate(refs,1):
  if not p.exists(): fail.append(f'missing required receipt: {rt}'); continue
  o=load_json(p)
  if not o.get('schema_version') and 'receipt_type' in o: pass
  if not o.get('receipt_type'): fail.append(f'missing receipt_type {rt}')
  if not o.get('signatures'): fail.append(f'missing signatures {rt}')
  if str(o.get('decision','pass')).lower() in {'fail','failed','rejected','deny'}: fail.append(f'failed decision {rt}')
  if scan_payload_for_forbidden_terms(o): fail.append(f'forbidden terms {rt}')
  chain.append({'ordinal':i,'receipt_type':rt,'ref':safe_rel_ref(p,x.archive_root if str(p).startswith(x.archive_root) else p.parents[3]),'sha256':'sha256:'+sha256_file(p),'decision':o.get('decision','pass'),'signatures_present':bool(o.get('signatures'))})
 passed=not fail
 out=Path(x.out_root)/'certification/soil/receipt_chain';out.mkdir(parents=True,exist_ok=True)
 audit={'schema_version':'kfm.v1','object_type':'SoilReceiptChainAudit','domain':'soil','archive_package_id':aid,'release_id':rid,'receipt_chain_audit_passed':passed,'chain':chain,'missing_optional_receipts':[],'failure_reasons':fail,'created':utc_now_iso()}
 ap=out/f'{sanitize_id(aid)}.receipt_chain_audit.json';write_json_atomic(ap,audit)
 rec={'schema_version':'kfm.v1','receipt_type':'SoilReceiptChainAuditReceipt','domain':'soil','archive_package_id':aid,'release_id':rid,'decision':'pass' if passed else 'fail','audit_ref':safe_rel_ref(ap,x.out_root),'audit_hash':'sha256:'+sha256_file(ap),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 rp=out/f'{sanitize_id(aid)}.receipt_chain_audit_receipt.json';write_json_atomic(rp,rec)
 print(json.dumps({'receipt_chain_audit_passed':passed,'archive_package_id':aid,'release_id':rid,'failure_reasons':fail},sort_keys=True)); return 0 if passed else 1
if __name__=='__main__': raise SystemExit(main())
