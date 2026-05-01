#!/usr/bin/env python3
import argparse,json,hashlib,shutil
from pathlib import Path
from datetime import datetime,timezone
now=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def main():
 p=argparse.ArgumentParser();p.add_argument('--artifact-preview-manifest',required=True);p.add_argument('--publication-manifest-candidate',required=True);p.add_argument('--publication-eligibility-decision',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();asof=a.as_of or now();out=Path(a.out_dir);pr=out/'publication_preview';pr.mkdir(parents=True,exist_ok=True)
 dst=pr/'finalized_manifest_candidate.preview.json';shutil.copyfile(a.publication_manifest_candidate,dst)
 o={'schema_version':'v1','finalization_id':'f-'+hashlib.sha256(asof.encode()).hexdigest()[:10],'domain':'atmosphere.air','generated_at':now(),'as_of':asof,'reentry_publication_manifest_candidate_ref':a.publication_manifest_candidate,'reentry_publication_artifact_preview_manifest_ref':a.artifact_preview_manifest,'reentry_publication_eligibility_decision_ref':a.publication_eligibility_decision,'finalized_manifest_preview_ref':str(dst),'public_boundary_checks':{'published_status_absent':True},'publication_mode':'fixture_preview_only','status':'fixture_finalization_candidate'}
 if not a.dry_run:(out/'reentry_publication_manifest_finalization_candidate.json').write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
 print('PASS')
if __name__=='__main__': main()
