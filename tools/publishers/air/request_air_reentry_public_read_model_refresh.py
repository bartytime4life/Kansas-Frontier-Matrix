#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
now=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def main():
 p=argparse.ArgumentParser();p.add_argument('--publication-receipt-candidate',required=True);p.add_argument('--artifact-preview-manifest',required=True);p.add_argument('--manifest-finalization-candidate',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();asof=a.as_of or now();out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
 src=json.loads(Path(a.artifact_preview_manifest).read_text())
 rr={'schema_version':'v1','refresh_request_id':'rr-'+hashlib.sha256(asof.encode()).hexdigest()[:8],'domain':'atmosphere.air','created_at':now(),'as_of':asof,'publication_receipt_candidate_ref':a.publication_receipt_candidate,'artifact_preview_manifest_ref':a.artifact_preview_manifest,'publication_manifest_finalization_candidate_ref':a.manifest_finalization_candidate,'source_publication_candidate_manifest_ref':src['source_publication_candidate_manifest_ref'],'requested_refresh_scope':'candidate_preview_only','candidate_publication_refs':[],'candidate_delta_seed_refs':['reentry_publication_delta_seed.json'],'candidate_invalidation_refs':[],'preconditions':['no_publish'],'forbidden_actions':['rebuild_read_model','publish'],'safety_checks':{'request_only':True},'status':'fixture_refresh_request'}
 ds={'schema_version':'v1','delta_seed_id':'ds-'+hashlib.sha256(asof.encode()).hexdigest()[:8],'domain':'atmosphere.air','created_at':now(),'as_of':asof,'publication_receipt_candidate_ref':a.publication_receipt_candidate,'artifact_preview_manifest_ref':a.artifact_preview_manifest,'source_publication_candidate_manifest_ref':src['source_publication_candidate_manifest_ref'],'change_seeds':[{'change_seed_id':'cs-1','change_type':'metadata_only','publication_candidate_ref':'candidate-1','record_ref':'record-1','reason':'fixture-preview','candidate_only':True}],'public_safe_refs':[],'redactions':[],'safety_checks':{'no_notification_claim':True},'status':'fixture_delta_seed'}
 if not a.dry_run: (out/'reentry_public_read_model_refresh_request.json').write_text(json.dumps(rr,indent=2,sort_keys=True)+'\n');(out/'reentry_publication_delta_seed.json').write_text(json.dumps(ds,indent=2,sort_keys=True)+'\n')
 print('PASS')
if __name__=='__main__': main()
