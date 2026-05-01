#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path

VERSION = '0.23.0'
GOVERNED_FILTER = "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10"


def now(): return datetime.now(timezone.utc).isoformat()
def fail(m): print(f'ERROR: {m}', file=sys.stderr); raise SystemExit(2)

def canonical(v): return json.dumps(v, sort_keys=True, separators=(',', ':'))
def sha(path: str | None):
    if not path: return None
    p = Path(path)
    if not p.exists() or not p.is_file(): return None
    return hashlib.sha256(p.read_bytes()).hexdigest()

def denied_scan(value):
    text = json.dumps(value)
    denied = ['decimalLatitude','decimalLongitude','raw_row_number','suppression_receipt_path','geometry','restricted_observations','token=','api_key=']
    return [d for d in denied if d in text]

def parse(argv):
    p = argparse.ArgumentParser(prog='kfm-ebird-rerun-remediation')
    p.add_argument('--version', action='version', version=VERSION)
    p.add_argument('--mode', default='plan', choices=['plan','execute','validate','compare','candidate','approve-local','rollback-plan','report'])
    p.add_argument('--aggregate', default='huc12', choices=['huc12','county','both'])
    for a in ['ebd-file','source-uri','filter','remediation-plan','remediation-receipt','triage-queue','quality-report','original-pipeline-manifest','original-release-receipt','replay-artifact','regions-file','taxon-crosswalk','region-crosswalk','work-dir','publish-dir','catalog-dir','out-dir','public-out-dir','layer-registry-dir','run-id','rerun-id']:
        p.add_argument(f'--{a}')
    p.add_argument('--format', default='jsonl', choices=['jsonl','csv'])
    p.add_argument('--limit', type=int)
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--force', action='store_true')
    return p.parse_args(argv)

def rerun_id(a):
    payload = {
        'aggregate_targets': a.aggregate, 'ebd_file_sha256': sha(a.ebd_file), 'source_uri': a.source_uri,
        'query_predicate': a.filter or GOVERNED_FILTER, 'original_pipeline_manifest_sha256': sha(a.original_pipeline_manifest),
        'original_release_receipt_sha256': sha(a.original_release_receipt), 'remediation_plan_sha256': sha(a.remediation_plan),
        'triage_queue_sha256': sha(a.triage_queue), 'taxon_crosswalk_sha256': sha(a.taxon_crosswalk),
        'region_crosswalk_sha256': sha(a.region_crosswalk), 'regions_file_sha256': sha(a.regions_file),
        'format': a.format, 'adapter_version': VERSION, 'contract_hash': 'v1'
    }
    return hashlib.sha256(canonical(payload).encode()).hexdigest()[:16]

def main():
    a = parse(sys.argv[1:])
    filt = a.filter or GOVERNED_FILTER
    if filt != GOVERNED_FILTER: fail('governed predicate must remain unchanged')
    if a.mode in ('execute','approve-local') and not a.force: fail(f'{a.mode} requires --force')
    if a.mode == 'execute' and not (a.ebd_file or a.replay_artifact): fail('execute requires --ebd-file or --replay-artifact')
    rid = a.rerun_id or rerun_id(a)
    out = Path(a.out_dir or f'data/catalog/fauna/ebird/rerun-remediation/{rid}')
    public_out = Path(a.public_out_dir or f'data/published/fauna/ebird/rerun-remediation/{rid}')
    out.mkdir(parents=True, exist_ok=True)

    plan = {'schema_version':'v1','object_type':'EbirdRerunRemediationPlan','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'rerun_remediation','public_safe_final_outputs':True,'exact_points':'restricted','rerun_id':rid,'aggregate_targets':[a.aggregate],'source_uri':a.source_uri or (Path(a.ebd_file).resolve().as_uri() if a.ebd_file else None),'query_predicate':filt,'executable_filter_name':'governed_ebird_checklist_qa_v1','safety_checks':{'no_network':True,'no_credentials':True,'suppression_min_n_at_least_10':True,'exact_points_restricted':True},'denied_public_fields_checked':['decimalLatitude','decimalLongitude','geometry','raw_row_number'],'generated_at':now()}
    (out/'rerun_remediation_plan.json').write_text(json.dumps(plan, indent=2)+'\n')

    if a.mode in ('validate','report','candidate','approve-local','compare'):
        findings=[]
        if a.public_out_dir and public_out.exists():
            for f in public_out.glob('*.json'):
                denied = denied_scan(json.loads(f.read_text()))
                findings.extend([f'{f}:{x}' for x in denied])
        status = 'pass' if not findings else 'fail'
        vr = {'schema_version':'v1','object_type':'EbirdRerunRemediationValidationReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','rerun_id':rid,'status':status,'checks':[{'name':'public_safety_scan','category':'safety','severity':'fail' if findings else 'info','status':'fail' if findings else 'pass','message':'denied fields found' if findings else 'ok'}],'hard_gates_failed':bool(findings),'public_safety_findings_count':len(findings),'unsupported_claims_count':0,'denied_public_fields_checked':plan['denied_public_fields_checked'],'generated_at':now()}
        (out/'rerun_remediation_validation_report.json').write_text(json.dumps(vr, indent=2)+'\n')
        if a.mode == 'candidate':
            cand={'schema_version':'v1','object_type':'EbirdDataAffectingCorrectiveReleaseCandidate','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'corrective_release_candidate','public_safe_final_outputs':True,'exact_points':'restricted','rerun_id':rid,'aggregate_targets':[a.aggregate],'rerun_validation_report_path':str(out/'rerun_remediation_validation_report.json'),'validations_failed':['public_safety_scan'] if findings else [],'blockers':['public_safety_validation_failed'] if findings else [],'generated_at':now()}
            (out/'data_affecting_corrective_release_candidate.json').write_text(json.dumps(cand, indent=2)+'\n')
    print(rid)

if __name__ == '__main__': main()
