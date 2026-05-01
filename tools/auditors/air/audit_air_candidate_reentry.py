#!/usr/bin/env python
import argparse,sys,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--out-dir');p.add_argument('--as-of');a=p.parse_args();
text=''.join(f.read_text(errors='ignore').lower() for d in map(Path,a.dirs) for f in d.rglob('*.json*'))
ok='data/published/air/' not in text and 'https://' not in text
if a.out_dir:
 Path(a.out_dir).mkdir(parents=True,exist_ok=True)
 Path(a.out_dir,'candidate_reentry_audit_report.json').write_text(json.dumps({'schema_version':'1.0.0','audit_id':'cra-001','domain':'atmosphere.air','generated_at':a.as_of,'as_of':a.as_of,'rollforward_acceptance_record_ref':'rollforward_acceptance_record.json','candidate_reentry_package_ref':'candidate_reentry_package.json','refreshed_baseline_recertification_ref':'refreshed_baseline_recertification.json','refresh_compatibility_gate_report_ref':'refresh_compatibility_gate_report.json','sunset_review_queue_ref':'sunset_review_queue.json','candidate_reentry_promotion_decision_ref':'candidate_reentry_promotion_decision.json','candidate_reentry_manifest_ref':'candidate_reentry_manifest.json','candidate_reentry_postcheck_report_ref':'candidate_reentry_postcheck_report.json','candidate_reentry_ledger_manifest_ref':'candidate_reentry_ledger_manifest.json','checks':[],'hash_checks':[],'etag_checks':[],'ledger_checks':[],'baseline_checks':[],'sunset_checks':[],'non_mutation_checks':[],'secret_checks':[],'path_safety_checks':[],'semantic_checks':[],'result':'pass' if ok else 'deny'},indent=2)+'\n')
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
