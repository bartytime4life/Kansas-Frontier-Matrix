import json, unittest
from pathlib import Path

class T(unittest.TestCase):
    def test_release_candidate_fields(self):
        r=json.loads(Path('release/dry_runs/synthetic_hydrology_release_manifest.json').read_text())
        for k in ['release_candidate_id','content_spec_hash','run_receipt_id','validation_report_id','policy_decision_id','rollback_target','correction_path','included_evidence_bundle_ids','result']:
            self.assertIn(k,r)
        self.assertIn(r['result'],['READY_FOR_REVIEW','DENY','ABSTAIN','ERROR'])
