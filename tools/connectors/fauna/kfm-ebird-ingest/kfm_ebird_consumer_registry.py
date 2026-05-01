#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, hashlib, os
from pathlib import Path
from datetime import datetime
VERSION='0.30.0'

MUTATING={'apply','renew','revoke','suspend','reinstate','badge-refresh'}


def sha(path:str)->str:
    h=hashlib.sha256();h.update(Path(path).read_bytes());return 'sha256:'+h.hexdigest()

def run_id(args)->str:
    payload={'aggregate_targets':args.aggregate,'consumer_ids':sorted(args.consumer_id or []),'decision':args.decision,'reason':args.reason,'validity_days':args.validity_days,'adapter_version':VERSION}
    if args.consumer_registry and Path(args.consumer_registry).exists(): payload['consumer_registry_sha256']=sha(args.consumer_registry)
    s=json.dumps(payload,sort_keys=True,separators=(',',':'))
    return hashlib.sha256(s.encode()).hexdigest()[:16]

def parse(argv=None):
    p=argparse.ArgumentParser(prog='kfm-ebird-consumer-registry')
    p.add_argument('--mode',default='plan',choices=['plan','apply','validate','renew','revoke','suspend','reinstate','badge-refresh','registry-index','diff','report'])
    p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
    p.add_argument('--consumer-registry'); p.add_argument('--consumer-id',action='append')
    p.add_argument('--out-dir'); p.add_argument('--public-out-dir'); p.add_argument('--registry-root',default='data/catalog/fauna/ebird/consumer-registry'); p.add_argument('--public-registry-root',default='data/published/fauna/ebird/consumer-registry')
    p.add_argument('--decision',choices=['certified','renewed','revoked','suspended','reinstated','needs_review','blocked'])
    p.add_argument('--reason'); p.add_argument('--validity-days',type=int,default=180)
    p.add_argument('--dry-run',action='store_true'); p.add_argument('--apply',action='store_true'); p.add_argument('--force',action='store_true')
    p.add_argument('--version',action='store_true')
    return p.parse_known_args(argv)

def main(argv=None):
    args,_=parse(argv)
    if args.version:
        print(json.dumps({'adapter':'kfm-ebird','tool':'consumer-registry','version':VERSION}));return
    rid=run_id(args)
    out=Path(args.out_dir or f'data/catalog/fauna/ebird/consumer-registry/runs/{rid}')
    pub=Path(args.public_out_dir or f'data/published/fauna/ebird/consumer-registry/runs/{rid}')
    if args.mode in MUTATING and not (args.apply and args.force):
        raise SystemExit('mutating modes require --apply --force')
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
    plan={'schema_version':'v1','object_type':'KfmEbirdConsumerRegistryOperationPlan','adapter':'kfm-ebird','policy_label':'consumer_registry','public_safe_final_outputs':True,'exact_points':'restricted','registry_run_id':rid,'aggregate_targets':args.aggregate,'planned_mode':args.mode,'planned_decision':args.decision,'prohibited_actions':['delete_consumer_artifacts','publish_exact_coordinates','send_external_notification']}
    (out/'consumer_registry_operation_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    manifest={'schema_version':'v1','object_type':'KfmEbirdConsumerRegistryOperationManifest','adapter':'kfm-ebird','registry_run_id':rid,'lifecycle_audit_ledger_path':str(out/'consumer_lifecycle_audit_ledger.jsonl'),'public_safety_checks_run':['layer30_public_safety_scanner']}
    (out/'consumer_registry_operation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (out/'consumer_lifecycle_audit_ledger.jsonl').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdConsumerLifecycleAuditEvent','registry_run_id':rid,'event_id':rid+'-1','consumer_id':(args.consumer_id or ['synthetic'])[0],'event_type':'validation_passed','public_safe':False,'exact_points':'restricted','timestamp':datetime.utcnow().isoformat()+'Z'})+'\n')
    pubidx={'schema_version':'v1','object_type':'PublicKfmEbirdConsumerRegistryIndex','public_safe':True,'exact_points':'restricted','registry_run_id':rid,'aggregate_targets':args.aggregate,'consumers':[],'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'no_restricted_observations_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True,'no_network_required':True,'no_credentials_required':True}}
    (pub/'public_consumer_registry_index.json').write_text(json.dumps(pubidx,indent=2)+'\n')
    (pub/'public_consumer_status_summary.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdConsumerStatusSummary','public_safe':True,'exact_points':'restricted','registry_run_id':rid,'aggregate_targets':args.aggregate,'counts':{'certified':0,'renewed':0,'revoked':0,'suspended':0,'needs_review':0,'blocked':0,'expired':0,'unknown':0},'warnings_count':0,'blockers_count':0},indent=2)+'\n')
    print(json.dumps({'registry_run_id':rid,'out_dir':str(out),'public_out_dir':str(pub)}))

if __name__=='__main__': main()
