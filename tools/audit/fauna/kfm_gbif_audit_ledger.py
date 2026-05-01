#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.fauna.gbif_publication_ops_validator import stable_hash

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--package',required=True);ap.add_argument('--entry-type',required=True);ap.add_argument('--actor-type',required=True);ap.add_argument('--actor-id',required=True);ap.add_argument('--previous-ledger-entry-hash');ap.add_argument('--output',required=True);a=ap.parse_args()
 pkg=json.loads(Path(a.package).read_text())
 out={"audit_ledger_entry_id":"gbif_audit_TEST_001","entry_type":a.entry_type,"domain":"fauna","source_system":"GBIF","publication_package_id":pkg.get('publication_package_id'),"actor":{"actor_type":a.actor_type,"actor_id":a.actor_id},"action":"create_publication_package","policy_version":"gbif_publication_ops.v1","input_artifact_hashes":sum(pkg.get('artifact_hashes',{}).values(),[]),"output_artifact_hashes":[pkg.get('kfm:spec_hash')],"previous_ledger_entry_hash":a.previous_ledger_entry_hash,"chain_index":1,"decision":"allowed" if pkg.get('policy_results',{}).get('passed') else 'denied',"decision_reasons":pkg.get('policy_results',{}).get('denies',[]),"redactions":["exact occurrence coordinates not emitted"],"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','audit_ledger_entry_id','kfm:spec_hash'))
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n'); print('ok')
if __name__=='__main__':main()
