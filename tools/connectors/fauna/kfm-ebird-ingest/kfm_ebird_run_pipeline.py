#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from packages.evidence.evidencebundle_hash import canonical_json, compute_spec_hash

GOVERNED_FILTER = "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10"
DENIED_FIELDS=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry"]
SECRET_KEYS={"token","api_key","apikey","key","secret","password","credential","access_token","refresh_token"}


def fail(m:str)->None:
    print(f"ERROR: {m}", file=sys.stderr); raise SystemExit(2)

def sha256_file(path:Path)->str:
    d=hashlib.sha256()
    with path.open('rb') as f:
        for c in iter(lambda:f.read(65536), b''): d.update(c)
    return f"sha256:{d.hexdigest()}"

def normalize_filter(p:str)->str:
    p=p.lower().replace(' ','').replace('"',"'")
    return p.replace('all_species_reported','complete').replace('duration_minutes','duration_min').replace('effort_distance_km','distance_km')

def redact_uri(uri:str)->str:
    if '?' not in uri: return uri
    b,q=uri.split('?',1); out=[]
    for part in q.split('&'):
        if '=' not in part: out.append(part); continue
        k,v=part.split('=',1)
        out.append(f"{k}=REDACTED" if k.lower() in SECRET_KEYS else f"{k}={v}")
    return b+'?'+('&'.join(out))

def parse_args(argv:list[str])->argparse.Namespace:
    p=argparse.ArgumentParser(prog='kfm-ebird-run-pipeline')
    p.add_argument('--ebd-file', required=True); p.add_argument('--source-uri'); p.add_argument('--filter', dest='predicate', default=GOVERNED_FILTER)
    p.add_argument('--aggregate', choices=('huc12','county','both'), default='huc12'); p.add_argument('--suppression', type=int, default=10)
    p.add_argument('--work-dir'); p.add_argument('--publish-dir', default='data/published/fauna/ebird'); p.add_argument('--catalog-dir', default='data/catalog/fauna/ebird'); p.add_argument('--layer-registry-dir', default='data/published/fauna/layers')
    p.add_argument('--regions-file'); p.add_argument('--format', choices=('jsonl','csv'), default='jsonl'); p.add_argument('--limit', type=int); p.add_argument('--run-id')
    p.add_argument('--plan', action='store_true'); p.add_argument('--execute', action='store_true'); p.add_argument('--resume', action='store_true'); p.add_argument('--force', action='store_true')
    p.add_argument('--skip-promote', action='store_true'); p.add_argument('--skip-public-view', action='store_true'); p.add_argument('--maplibre', action=argparse.BooleanOptionalAction, default=True); p.add_argument('--dry-run', action='store_true')
    return p.parse_args(argv)

def run(cmd:list[str])->None:
    subprocess.run(cmd, check=True)

def main()->None:
    a=parse_args(sys.argv[1:])
    if a.dry_run: a.plan=True
    if not a.plan and not a.execute: a.plan=True
    if a.plan and a.execute: fail('choose only one of --plan/--dry-run or --execute')
    if a.suppression<10: fail('--suppression must be >= 10')
    if a.limit is not None and a.limit<=0: fail('--limit must be positive')
    if normalize_filter(a.predicate)!=normalize_filter(GOVERNED_FILTER): fail('Only governed_ebird_checklist_qa_v1 predicate is executable')
    ebd=Path(a.ebd_file)
    if not ebd.exists(): fail(f'Input file not found: {ebd}')
    src=a.source_uri or ebd.resolve().as_uri(); redacted=redact_uri(src)
    ebd_sha=sha256_file(ebd)
    reg_sha=sha256_file(Path(a.regions_file)) if a.regions_file else None
    agg_targets=['huc12','county'] if a.aggregate=='both' else [a.aggregate]
    run_id=a.run_id or hashlib.sha256(canonical_json({"source_uri":src,"ebd_file_sha256":ebd_sha,"query_predicate":a.predicate,"aggregate":a.aggregate,"suppression_min_n":a.suppression,"regions_file_sha256":reg_sha,"format":a.format,"executable_filter_name":"governed_ebird_checklist_qa_v1"}).encode()).hexdigest()[:16]
    work=Path(a.work_dir or f"data/work/fauna/ebird/runs/{run_id}")
    if 'data/published' in work.as_posix(): fail('--work-dir must not be under data/published')
    pub=Path(a.publish_dir); cat=Path(a.catalog_dir); layers=Path(a.layer_registry_dir)
    if 'published' not in pub.as_posix(): fail('--publish-dir must be a published artifact root')
    if work.exists() and not a.resume and not a.force and a.execute: fail('run dir exists; use --resume or --force')
    if work.exists() and a.force and a.execute: shutil.rmtree(work)

    stages=['ingest']+[f'aggregate_{x}' for x in agg_targets]+([] if a.skip_promote else [f'promote_{x}' for x in agg_targets])+([] if a.skip_public_view else [f'public_view_{x}' for x in agg_targets])
    plan={"schema_version":"v1","object_type":"PipelinePlan","domain":"fauna","source":"ebird","policy_label":"mixed_restricted_public","public_safe_final_outputs":True,"exact_points":"restricted","run_id":run_id,"source_uri":src,"redacted_source_uri":redacted,"ebd_file":str(ebd),"ebd_file_sha256":ebd_sha,"query_predicate":a.predicate,"aggregate_targets":agg_targets,"suppression_min_n":a.suppression,"format":a.format,"work_dir":str(work),"publish_dir":str(pub),"catalog_dir":str(cat),"layer_registry_dir":str(layers),"stages":stages,"denied_public_fields_checked":DENIED_FIELDS,"safety_checks":["restricted_outputs_not_under_data_published","public_outputs_aggregate_only","suppression_min_n_at_least_10","exact_points_restricted","no_credentials_or_downloads"]}
    if a.regions_file: plan['regions_file']=a.regions_file; plan['regions_file_sha256']=reg_sha
    if a.plan:
        print(json.dumps(plan, indent=2, sort_keys=True)); return

    work.mkdir(parents=True, exist_ok=True)
    lock=work/'.pipeline.lock'
    if lock.exists() and not a.resume: fail('lock file exists')
    lock.write_text(json.dumps({'run_id':run_id},indent=2), encoding='utf-8')
    ledger=work/'audit_ledger.jsonl'; events=[]; validations=[]
    def event(t:str, **kw:Any)->None:
        obj={"schema_version":"v1","object_type":"AuditLedgerEvent","domain":"fauna","source":"ebird","run_id":run_id,"event_id":len(events)+1,"event_type":t,"timestamp":datetime.now(timezone.utc).isoformat(),"message":kw.pop('message',t),"redacted_source_uri":redacted,**kw}
        events.append(obj)
        with ledger.open('a',encoding='utf-8') as f: f.write(json.dumps(obj,sort_keys=True)+'\n')
    event('pipeline_started')
    (work/'pipeline_plan.json').write_text(json.dumps(plan,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    tooldir=Path(__file__).parent
    restricted=work/'restricted'; public=work/'public'; restricted.mkdir(exist_ok=True); public.mkdir(exist_ok=True)

    ev=work/'evidencebundle.json'; obs=restricted/f'observations.restricted.{a.format}'; qua=restricted/f'quarantine.restricted.{a.format}'; ingm=restricted/'ingest_manifest.json'
    event('stage_started',stage='ingest')
    run([str(tooldir/'kfm-ebird-ingest'),'--ebd-file',str(ebd),'--source-uri',src,'--filter',a.predicate,'--aggregate','huc12','--suppression',str(a.suppression),'--emit',str(ev),'--out',str(obs),'--quarantine',str(qua),'--manifest',str(ingm),'--format',a.format] + (['--limit',str(a.limit)] if a.limit else []))
    event('stage_completed',stage='ingest')
    manifests=[]
    for agg in agg_targets:
        aout=public/f'aggregates_{agg}.public.{a.format}'; am=public/f'aggregate_manifest_{agg}.json'; sr=restricted/f'suppression_receipt_{agg}.restricted.json'
        event('stage_started',stage=f'aggregate_{agg}')
        cmd=[str(tooldir/'kfm-ebird-aggregate'),'--observations',str(obs),'--evidencebundle',str(ev),'--aggregate',agg,'--suppression',str(a.suppression),'--out',str(aout),'--manifest',str(am),'--suppression-receipt',str(sr),'--format',a.format]
        if a.regions_file: cmd += ['--regions-file',a.regions_file]
        if a.limit: cmd += ['--limit',str(a.limit)]
        run(cmd); event('stage_completed',stage=f'aggregate_{agg}')
        manifests.append((agg,aout,am,sr))

    promoted=[]
    if a.skip_promote:
        for agg, *_ in manifests: event('stage_skipped',stage=f'promote_{agg}')
    else:
        for agg,aout,am,_ in manifests:
            event('stage_started',stage=f'promote_{agg}')
            run([str(tooldir/'kfm-ebird-promote'),'--aggregate-file',str(aout),'--aggregate-manifest',str(am),'--evidencebundle',str(ev),'--aggregate',agg,'--publish-dir',str(pub/agg),'--catalog-dir',str(cat/agg),'--layer-registry',str(layers/f'ebird_agg_{agg}.json'),'--format',a.format,'--run-id',run_id,'--overwrite'])
            event('stage_completed',stage=f'promote_{agg}'); promoted.append((agg,pub/agg/run_id))

    if a.skip_public_view:
        for agg,_ in promoted: event('stage_skipped',stage=f'public_view_{agg}')
    else:
        for agg,pdir in promoted:
            event('stage_started',stage=f'public_view_{agg}')
            cmd=['python',str(tooldir/'kfm_ebird_build_public_view.py'),'--promotion-dir',str(pdir),'--aggregate',agg,'--out-dir',str(pdir/'api'),'--format',a.format,'--overwrite']
            if a.maplibre: cmd += ['--maplibre-out',str(pub.parent/'maplibre'/f'ebird_agg_{agg}.json')]
            run(cmd); event('stage_completed',stage=f'public_view_{agg}')

    vrep={"schema_version":"v1","object_type":"ValidationReport","domain":"fauna","source":"ebird","run_id":run_id,"status":"pass","checks":[],"summary":{"total":0,"passed":0,"failed":0,"skipped":0},"denied_public_fields_checked":DENIED_FIELDS,"public_artifacts_checked":[],"restricted_artifacts_checked":[str(obs),str(qua)] ,"generated_at":datetime.now(timezone.utc).isoformat()}
    for p in [ev,obs,qua,ingm,work/'pipeline_plan.json']:
        ok=p.exists(); vrep['checks'].append({"name":f"exists:{p.name}","category":"filesystem","status":"pass" if ok else "fail","artifact_path":str(p),"message":"exists" if ok else "missing"})
    vrep['summary']['total']=len(vrep['checks']); vrep['summary']['passed']=sum(1 for c in vrep['checks'] if c['status']=='pass'); vrep['summary']['failed']=sum(1 for c in vrep['checks'] if c['status']=='fail')
    if vrep['summary']['failed']>0: vrep['status']='fail'
    vrp=work/'validation_report.json'; vrp.write_text(json.dumps(vrep,indent=2,sort_keys=True)+'\n',encoding='utf-8')

    pm={"schema_version":"v1","object_type":"PipelineManifest","domain":"fauna","source":"ebird","policy_label":"mixed_restricted_public","public_safe_final_outputs":True,"exact_points":"restricted","run_id":run_id,"source_uri":src,"ebd_file":str(ebd),"ebd_file_sha256":ebd_sha,"query_predicate":a.predicate,"aggregate_targets":agg_targets,"suppression_min_n":a.suppression,"format":a.format,"kfm:spec_hash":json.loads(ev.read_text())['kfm:spec_hash'],"evidencebundle_path":str(ev),"evidencebundle_sha256":sha256_file(ev),"pipeline_plan_path":str(work/'pipeline_plan.json'),"pipeline_plan_sha256":sha256_file(work/'pipeline_plan.json'),"audit_ledger_path":str(ledger),"audit_ledger_sha256":sha256_file(ledger),"validation_report_path":str(vrp),"validation_report_sha256":sha256_file(vrp),"stages":[],"output_roots":{"work_dir":str(work),"publish_dir":str(pub),"catalog_dir":str(cat)},"public_outputs":[str(x[1]) for x in promoted],"restricted_outputs":[str(obs),str(qua)]+[str(x[3]) for x in manifests],"counts":{},"denied_public_fields_checked":DENIED_FIELDS,"validations_passed":vrep['summary']['passed'],"validations_failed":vrep['summary']['failed'],"completed_at":datetime.now(timezone.utc).isoformat()}
    pmp=work/'pipeline_manifest.json'; pmp.write_text(json.dumps(pm,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    replay=work/'replay.json'; replay.write_text(json.dumps({"run_id":run_id,"source_uri":src,"query_predicate":a.predicate,"aggregate_targets":agg_targets,"suppression_min_n":a.suppression,"format":a.format,"command":"kfm-ebird-run-pipeline --execute ...","input_hashes":{"ebd_file_sha256":ebd_sha,"regions_file_sha256":reg_sha}},indent=2,sort_keys=True)+'\n',encoding='utf-8')
    event('pipeline_completed')
    lock.unlink(missing_ok=True)

if __name__=='__main__': main()
