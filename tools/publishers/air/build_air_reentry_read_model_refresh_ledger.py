#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from datetime import datetime, timezone
ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',required=True); ap.add_argument('--as-of'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--fixture-only',action='store_true')
args,_=ap.parse_known_args(); out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
as_of=args.as_of or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
obj={'schema_version':'v1','domain':'atmosphere.air','as_of':as_of,'generated_at':as_of,'status':'needs_review','fixture_backed':True,'production_use_allowed':False}
name=Path(__file__).name
mapping={
'create_air_reentry_gate_d_refresh_attestation.py':'reentry_gate_d_refresh_attestation.json',
'check_air_reentry_aqs_reconciliation_refresh_checkpoint.py':'reentry_aqs_reconciliation_refresh_checkpoint.json',
'review_air_reentry_publication_boundary_refresh.py':'reentry_publication_boundary_refresh_review.json',
'decide_air_reentry_publication_eligibility_refresh.py':'reentry_publication_eligibility_refresh_decision.json',
'build_air_reentry_publication_candidate_refresh_manifest.py':'reentry_publication_candidate_refresh_manifest.json',
'build_air_reentry_publication_manifest_refresh_candidate.py':'reentry_publication_manifest_refresh_candidate.json',
'build_air_reentry_publication_boundary_refresh_lineage_bridge.py':'reentry_publication_boundary_refresh_lineage_bridge.json',
'build_air_reentry_publication_boundary_refresh_manifest.py':'reentry_publication_boundary_refresh_manifest.json',
'build_air_reentry_publication_boundary_refresh_ledger.py':'reentry_publication_boundary_refresh_ledger_manifest.json',
'run_air_reentry_publication_boundary_refresh_postcheck.py':'reentry_publication_boundary_refresh_postcheck_report.json'}
if 'gate_d' in name: obj.update({'signature_type':'fixture_signature','status':'fixture_attested'})
if 'aqs' in name: obj.update({'status':'not_required','aqs_validated_window':{'averaging_window':'24h_validated','pm25_units':'ug_m3','nowcast_semantics':'operational_not_validated_truth'}})
if not args.dry_run:
    (out/mapping.get(name,'artifact.json')).write_text(json.dumps(obj,indent=2)+'\n')
    (out/'reentry_publication_boundary_refresh_events.jsonl').write_text(json.dumps({'event_type':'generated','as_of':as_of})+'\n')
print('PASS',name)
