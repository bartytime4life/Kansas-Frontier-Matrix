#!/usr/bin/env python3
import argparse,json
from datetime import datetime,timezone
from pathlib import Path
from tools.distribution.fauna._gbif_distribution_common import stable_hash
L=lambda p: json.loads(Path(p).read_text())
a=argparse.ArgumentParser();a.add_argument('--distribution-bundle',required=True);a.add_argument('--withdrawal-receipt',required=True);a.add_argument('--reason',required=True);a.add_argument('--output',required=True);a.add_argument('--cache-receipt-output',required=True);x=a.parse_args();b,w=L(x.distribution_bundle),L(x.withdrawal_receipt)
if x.reason=='withdrawal_applied' and not w.get('withdrawal_receipt_id'): raise SystemExit('withdrawal receipt required')
cr={"cache_invalidation_receipt_id":"gbif_cache_TEST_001","domain":"fauna","source_system":"GBIF","distribution_bundle_id":b['distribution_bundle_id'],"release_registry_entry_id":b['release_registry_entry_id'],"reason":"withdrawal_applied","cache_keys":[r['cache_key'] for r in b['public_routes']],"public_url_paths":[r['public_url_path'] for r in b['public_routes']],"invalidation_state":"requested","affected_artifact_ids":[r['artifact_id'] for r in b['public_routes']],"replacement_distribution_bundle_id":None,"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}; cr['kfm:spec_hash']=stable_hash(cr,exclude=('created_at','cache_invalidation_receipt_id'))
out={"takedown_enforcement_receipt_id":"gbif_takedown_TEST_001","domain":"fauna","source_system":"GBIF","takedown_reason":x.reason,"withdrawal_receipt_ref":w.get('withdrawal_receipt_id'),"correction_receipt_ref":None,"distribution_bundle_id":b['distribution_bundle_id'],"release_registry_entry_id":b['release_registry_entry_id'],"removed_public_url_paths":[r['public_url_path'] for r in b['public_routes']],"removed_cache_keys":[r['cache_key'] for r in b['public_routes']],"removed_search_index_record_ids":b['search_index_record_ids'],"replacement_distribution_bundle_id":None,"public_use_allowed":False,"cache_invalidation_receipt_ref":cr['cache_invalidation_receipt_id'],"audit_ledger_entry_ref":"gbif_audit_TAKEDOWN_TEST_001","created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}; out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','takedown_enforcement_receipt_id'))
Path(x.cache_receipt_output).write_text(json.dumps(cr,indent=2)+'
');Path(x.output).write_text(json.dumps(out,indent=2)+'
');print('ok')
