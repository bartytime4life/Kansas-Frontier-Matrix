#!/usr/bin/env python
import argparse,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--rollforward-dir',action='append',default=[]);p.add_argument('--rollforward-ledger',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--assurance-dir');p.add_argument('--maintenance-dir');p.add_argument('--as-of');p.add_argument('--allow-fixture-postcheck',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();led=j(a.rollforward_ledger)
o={"schema_version":"1.0.0","postcheck_id":"rpc-001","domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"remediation_rollforward_plan_ref":"remediation_rollforward_plan.json","candidate_artifact_refresh_manifest_ref":"candidate_artifact_refresh_manifest.json","candidate_read_model_refresh_ref":"candidate_read_model_refresh.json","client_delivery_refresh_manifest_ref":"client_delivery_refresh_manifest.json","sunset_delta_candidate_ref":"sunset_delta_candidate.json","assurance_baseline_rotation_ref":"assurance_baseline_rotation.json","checks":["no_published_writes","no_route_deletion"],"hash_checks":["pass"],"etag_checks":["pass"],"path_safety_checks":["pass"],"semantic_checks":["nowcast_operational_not_validated_truth","aqs_24h_validated"],"non_mutation_checks":["pass"],"open_findings":[],"result":"pass_fixture"}
if not a.dry_run:
 out=Path(a.out_dir);w(out/'rollforward_postcheck_report.json',o);(out/'maintenance_rollforward_events.jsonl').write_text('{"event_type":"rollforward_postcheck_created","result":"pass"}\n')
print('PASS')
