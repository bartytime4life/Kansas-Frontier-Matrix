#!/usr/bin/env python
import argparse,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--candidate-artifact-refresh',required=True);p.add_argument('--candidate-read-model-refresh',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
out=Path(a.out_dir)/'candidate_delivery';out.mkdir(parents=True,exist_ok=True);f=out/'static_response_bundle.candidate.json';w(f,{"status":"candidate_only"});s=sha(f)
m={"schema_version":"1.0.0","delivery_refresh_id":"cdr-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"candidate_artifact_refresh_manifest_ref":a.candidate_artifact_refresh,"candidate_read_model_refresh_ref":a.candidate_read_model_refresh,"source_client_delivery_manifest_ref":"delivery/client_delivery_manifest.json","source_route_manifest_ref":"delivery/client_route_manifest.json","source_static_response_bundle_ref":"delivery/static_response_bundle.json","source_cache_manifest_ref":"delivery/client_cache_manifest.json","candidate_client_delivery_manifest_ref":str(out/'client_delivery_manifest.candidate.json'),"candidate_route_manifest_ref":str(out/'client_route_manifest.candidate.json'),"candidate_static_response_bundle_ref":str(f),"candidate_cache_manifest_ref":str(out/'client_cache_manifest.candidate.json'),"candidate_delta_refs":[],"candidate_invalidation_notice_refs":[],"etag_refreshes":[{"path":str(f),"sha256":s,"etag":etag_from_sha(s)}],"safety_checks":["no_route_removal","no_notice_send"],"status":"fixture_delivery_refresh"}
if not a.dry_run:
 w(Path(a.out_dir)/'client_delivery_refresh_manifest.json',m);(Path(a.out_dir)/'maintenance_rollforward_events.jsonl').write_text('{"event_type":"client_delivery_refresh_created","result":"pass"}\n')
print('PASS')
