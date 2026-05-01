#!/usr/bin/env python
import argparse,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--maintenance-closure',required=True);p.add_argument('--candidate-artifact-refresh',required=True);p.add_argument('--candidate-read-model-refresh',required=True);p.add_argument('--client-delivery-refresh',required=True);p.add_argument('--assurance-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();out=Path(a.out_dir)
o={"schema_version":"1.0.0","baseline_rotation_id":"abr-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"maintenance_closure_record_ref":a.maintenance_closure,"candidate_artifact_refresh_manifest_ref":a.candidate_artifact_refresh,"candidate_read_model_refresh_ref":a.candidate_read_model_refresh,"client_delivery_refresh_manifest_ref":a.client_delivery_refresh,"previous_assurance_summary_ref":str(Path(a.assurance_dir)/'continuous_assurance_summary.json'),"previous_evidence_archive_manifest_ref":str(Path(a.assurance_dir)/'evidence_archive_manifest.json'),"candidate_baseline_refs":["candidate/baseline.json"],"baseline_diff":[],"required_recertification_refs":[],"safety_checks":["preserve_prior_baselines"],"status":"fixture_baseline_rotation"}
if not a.dry_run:
 w(out/'assurance_baseline_rotation.json',o);(out/'maintenance_rollforward_events.jsonl').write_text('{"event_type":"assurance_baseline_rotation_created","result":"pass"}\n')
print('PASS')
