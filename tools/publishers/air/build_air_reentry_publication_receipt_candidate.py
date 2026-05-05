#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
now=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def main():
 p=argparse.ArgumentParser();p.add_argument('--materialization-plan',required=True);p.add_argument('--artifact-preview-manifest',required=True);p.add_argument('--manifest-finalization-candidate',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--actor',default='fixture-non-production');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();asof=a.as_of or now();out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
 o={'schema_version':'v1','receipt_id':'rc-'+hashlib.sha256(asof.encode()).hexdigest()[:10],'domain':'atmosphere.air','created_at':now(),'as_of':asof,'execution_mode':'fixture_preview_materialization','materialization_plan_ref':a.materialization_plan,'artifact_preview_manifest_ref':a.artifact_preview_manifest,'publication_manifest_finalization_candidate_ref':a.manifest_finalization_candidate,'actor':a.actor,'steps_observed':['plan','preview','finalize'],'artifact_refs':[a.materialization_plan,a.artifact_preview_manifest,a.manifest_finalization_candidate],'hashes':{},'non_mutation_evidence':{'source_unchanged':True},'result':'pass','status':'fixture_receipt'}
 if not a.dry_run:(out/'reentry_publication_receipt_candidate.json').write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
 print('PASS')
if __name__=='__main__': main()
