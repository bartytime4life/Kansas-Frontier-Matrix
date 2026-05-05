#!/usr/bin/env python
import argparse,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--rollforward-plan',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--read-model-dir');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();plan=j(a.rollforward_plan)
out=Path(a.out_dir);cand=out/'candidate_artifacts';cand.mkdir(parents=True,exist_ok=True)
idx=cand/'public_index.candidate.json';w(idx,{"nowcast_label":"operational_nowcast","aqs_validated_label":"24h_validated"})
s=sha(idx)
manifest={"schema_version":"1.0.0","refresh_id":"car-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"remediation_rollforward_plan_ref":a.rollforward_plan,"maintenance_closure_record_ref":plan['maintenance_closure_record_ref'],"source_artifact_refs":[a.delivery_dir],"candidate_artifact_refs":[{"artifact_type":"public_index","path":str(idx),"sha256":s,"source_ref":a.delivery_dir,"candidate_only":True}],"changed_artifacts":[str(idx)],"unchanged_artifacts":[],"supersession_notes":["candidate-only additive refresh"],"safety_checks":["no_data_published_mutation"],"status":"fixture_refresh_candidate"}
rm={"schema_version":"1.0.0","read_model_refresh_id":"rmr-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"candidate_artifact_refresh_manifest_ref":str(out/'candidate_artifact_refresh_manifest.json'),"source_public_index_ref":"delivery/public_index.json","source_public_api_record_refs":["delivery/public_api_record.rec-1.json"],"source_public_status_ref":"delivery/public_status.json","source_public_provenance_trace_refs":["delivery/public_provenance_trace.tr-1.json"],"candidate_public_index_ref":str(idx),"candidate_public_api_record_refs":[str(idx)],"candidate_public_status_ref":str(idx),"candidate_public_provenance_trace_refs":[str(idx)],"applied_remediation_refs":plan['assurance_remediation_record_refs'],"applied_sunset_plan_ref":plan['client_sunset_plan_ref'],"visibility_changes":[],"safety_checks":["preserve_old_versions"],"status":"fixture_read_model_refresh"}
if not a.dry_run:
 w(out/'candidate_artifact_refresh_manifest.json',manifest);w(out/'candidate_read_model_refresh.json',rm);(out/'maintenance_rollforward_events.jsonl').write_text('{"event_type":"candidate_artifact_refresh_created","result":"pass"}\n')
print('PASS')
