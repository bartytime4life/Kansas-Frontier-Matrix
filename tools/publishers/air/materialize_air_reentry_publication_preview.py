#!/usr/bin/env python3
import argparse,json,hashlib,shutil
from pathlib import Path
from datetime import datetime,timezone
now=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--materialization-plan',required=True);p.add_argument('--publication-boundary-dir',action='append',default=[]);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();
 plan=json.loads(Path(a.materialization_plan).read_text());asof=a.as_of or now();out=Path(a.out_dir);prev=out/'publication_preview';prev.mkdir(parents=True,exist_ok=True)
 src=Path(plan['reentry_publication_manifest_candidate_ref']);dst=prev/'reentry_publication_manifest_candidate.preview.json';shutil.copyfile(src,dst)
 m={'schema_version':'v1','preview_manifest_id':'rpm-'+hashlib.sha256(asof.encode()).hexdigest()[:10],'domain':'atmosphere.air','generated_at':now(),'as_of':asof,'materialization_plan_ref':a.materialization_plan,'source_publication_candidate_manifest_ref':plan['reentry_publication_candidate_manifest_ref'],'source_publication_manifest_candidate_ref':str(src),'preview_root':str(prev),'preview_artifacts':[{'artifact_type':'publication_manifest_candidate_preview','path':str(dst),'sha256':sha(dst),'source_ref':str(src),'candidate_only':True,'immutable_preview':True}],'copied_from_refs':[str(src)],'hash_algorithm':'sha256','safety_checks':{'out_dir_only':True},'status':'fixture_preview_materialized'}
 if not a.dry_run: (out/'reentry_publication_artifact_preview_manifest.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
 print('PASS')
if __name__=='__main__': main()
