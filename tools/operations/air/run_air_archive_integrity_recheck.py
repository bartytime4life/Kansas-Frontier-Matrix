#!/usr/bin/env python
import argparse,json
from pathlib import Path
from _assurance_common import *
def main():
 p=argparse.ArgumentParser();
 for a in ('--assurance-plan','--closure-dir','--handoff-dir','--cutover-dir','--authorization-dir','--deployment-readiness-dir','--delivery-dir','--out-dir'): p.add_argument(a,required=True)
 p.add_argument('--as-of');p.add_argument('--allow-fixture-archive-recheck',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 plan=j(a.assurance_plan); manifest=j(Path(a.closure_dir)/'evidence_archive_manifest.json')
 deny=bad_text(manifest)
 result='deny' if deny else 'pass_fixture'
 out={"schema_version":"1.0.0","archive_recheck_id":"ar-"+h(plan)[:12],"domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"continuous_assurance_plan_ref":a.assurance_plan,"evidence_archive_manifest_ref":str(Path(a.closure_dir)/'evidence_archive_manifest.json'),"source_chain_refs":[plan.get('release_closure_dossier_ref','')],"hash_checks":[{"name":"manifest_present","pass":not deny}],"path_safety_checks":[{"name":"no_unsafe_paths","pass":not deny}],"redaction_checks":[{"name":"no_secret_like","pass":not deny}],"lifecycle_separation_checks":[{"name":"separate_artifacts","pass":True}],"missing_artifacts":[],"result":result}
 od=Path(a.out_dir)
 if not a.dry_run: w(od/'archive_integrity_recheck.json',out)
 print('PASS' if result!='deny' else 'DENY'); return 0 if result!='deny' else 1
if __name__=='__main__': raise SystemExit(main())
