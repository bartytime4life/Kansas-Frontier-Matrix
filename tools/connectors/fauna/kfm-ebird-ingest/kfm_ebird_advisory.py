#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, hashlib
from pathlib import Path
VERSION='0.30.0'

def aid(args):
    payload={'aggregate_targets':args.aggregate,'advisory_type':args.advisory_type,'severity':args.severity,'title':args.title,'summary':args.summary,'consumer_ids':sorted(args.consumer_id or []),'adapter_version':VERSION}
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:16]

def main(argv=None):
    p=argparse.ArgumentParser(prog='kfm-ebird-advisory')
    p.add_argument('--mode',default='plan',choices=['plan','build','validate','publish-local','diff','report']); p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
    p.add_argument('--advisory-type',default='general',choices=['public_safety','contract_change','sdk_change','root_change','gate_change','release_change','quality_issue','remediation','rerun_correction','consumer_reaudit','consumer_revocation','consumer_renewal','general'])
    p.add_argument('--severity',default='info',choices=['info','low','medium','high','critical'])
    p.add_argument('--out-dir'); p.add_argument('--public-out-dir'); p.add_argument('--title'); p.add_argument('--summary'); p.add_argument('--consumer-id',action='append'); p.add_argument('--force',action='store_true'); p.add_argument('--dry-run',action='store_true'); p.add_argument('--version',action='store_true')
    args,_=p.parse_known_args(argv)
    if args.version: print(json.dumps({'adapter':'kfm-ebird','tool':'advisory','version':VERSION})); return
    if args.mode in {'build','publish-local'} and not args.force: raise SystemExit('build/publish-local require --force')
    i=aid(args); out=Path(args.out_dir or f'data/catalog/fauna/ebird/advisories/{i}'); pub=Path(args.public_out_dir or f'data/published/fauna/ebird/advisories/{i}'); out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
    plan={'schema_version':'v1','object_type':'KfmEbirdAdvisoryPlan','advisory_id':i,'advisory_type':args.advisory_type,'severity':args.severity,'public_safe_final_outputs':True,'exact_points':'restricted','delivery':{'local_artifacts_only':True,'external_delivery_performed':False,'email_sent':False,'webhook_sent':False,'ticket_created':False}}
    (out/'advisory_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    (out/'consumer_outbox_drafts.jsonl').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdConsumerOutboxDraft','advisory_id':i,'consumer_id':(args.consumer_id or ['synthetic'])[0],'notification_type':'advisory','subject':'Local advisory','body':'Local-only draft','delivery_performed':False,'external_delivery_required':False,'public_safe':False,'exact_points':'restricted'})+'\n')
    notice={'schema_version':'v1','object_type':'PublicKfmEbirdAdvisoryNotice','public_safe':True,'exact_points':'restricted','advisory_id':i,'advisory_type':args.advisory_type,'severity':args.severity,'title':args.title or 'Synthetic advisory','summary':args.summary or 'Synthetic local-only advisory','aggregate_targets':args.aggregate,'recommended_public_actions':['review_public_notice'],'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'no_restricted_observations_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True}}
    (pub/'public_advisory_notice.json').write_text(json.dumps(notice,indent=2)+'\n')
    print(json.dumps({'advisory_id':i,'out_dir':str(out),'public_out_dir':str(pub)}))
if __name__=='__main__': main()
