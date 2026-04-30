#!/usr/bin/env python3
import argparse, json, hashlib, shutil
from pathlib import Path
from datetime import datetime, timezone
from kfm_ebird_contract import ADAPTER_VERSION, load_contract_lock, canonical_json, version_payload

CORE=["public_decimalLatitude_field","public_geometry_object","restricted_observation_path_in_public_artifact","suppression_receipt_path_in_public_artifact","suppression_group_hash_in_public_artifact","source_uri_token_query_param_unredacted","suppression_min_n_below_10","exact_points_public","checklist_count_below_suppression_min_n"]
ALL=CORE

def now(): return datetime.now(timezone.utc).isoformat()

def sha(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()

def guard_out(out:Path):
    s=str(out)
    if 'data/published' in s and 'fixtures/redteam' not in s: raise SystemExit('out-dir cannot be under real published roots')

def mutation_id(sid,seed,input_sha,params,contract_hash):
    obj={"scenario_id":sid,"seed":seed,"input_artifact_sha256":input_sha,"mutation_parameters":params,"adapter_version":ADAPTER_VERSION}
    if contract_hash: obj['contract_hash']=contract_hash
    return hashlib.sha256(canonical_json(obj).encode()).hexdigest()[:16]

def make_case(sid):
    bad={"schema_version":"v1","object_type":"EbirdRedTeamCase","policy_label":"redteam_fixture","public_safe":False,"synthetic":True,"scenario_id":sid,"payload":{}}
    if sid=='public_decimalLatitude_field': bad['payload']['decimalLatitude']=39.123
    elif sid=='public_geometry_object': bad['payload']['geometry']={"type":"Point","coordinates":[-100,40]}
    elif sid=='restricted_observation_path_in_public_artifact': bad['payload']['path']='data/work/fauna/ebird/restricted_observations.jsonl'
    elif sid=='suppression_receipt_path_in_public_artifact': bad['payload']['suppression_receipt_path']='data/work/fauna/ebird/suppression_receipt.json'
    elif sid=='suppression_group_hash_in_public_artifact': bad['payload']['suppression_group_hash']='sha256:deadbeef'
    elif sid=='source_uri_token_query_param_unredacted': bad['payload']['source_uri']='https://example.invalid?token=SYNTHETIC_TOKEN'
    elif sid=='suppression_min_n_below_10': bad['payload']['suppression_min_n']=9
    elif sid=='exact_points_public': bad['payload']['exact_points']='public'
    elif sid=='checklist_count_below_suppression_min_n': bad['payload'].update({"checklist_count":3,"suppression_min_n":10})
    return bad

def main():
    ap=argparse.ArgumentParser(prog='kfm-ebird-mutate')
    ap.add_argument('--mode',default='generate',choices=['generate','validate-corpus','list','clean'])
    ap.add_argument('--fixture-dir',default='tools/connectors/fauna/kfm-ebird-ingest/fixtures/redteam/base')
    ap.add_argument('--out-dir',default='tools/connectors/fauna/kfm-ebird-ingest/fixtures/redteam/generated')
    ap.add_argument('--scenario-set',default='core')
    ap.add_argument('--max-cases',type=int,default=100)
    ap.add_argument('--seed',default='contract_hash_or_adapter_version')
    ap.add_argument('--format',default='all')
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
    a=ap.parse_args()
    lock=Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')
    if a.version: print(json.dumps(version_payload('kfm-ebird-mutate', lock),indent=2,sort_keys=True)); return 0
    out=Path(a.out_dir); guard_out(out)
    if a.mode=='list': print('\n'.join(ALL)); return 0
    if a.mode=='clean':
        if out.exists() and not a.dry_run: shutil.rmtree(out)
        return 0
    if a.mode=='validate-corpus':
        man=out/'mutation_corpus_manifest.json'
        if not man.exists(): raise SystemExit('missing manifest')
        m=json.loads(man.read_text())
        missing=[s for s in CORE if s not in {c['scenario_id'] for c in m.get('generated_cases',[])}]
        if missing: raise SystemExit(f'missing core scenarios: {missing}')
        print(json.dumps({"status":"pass","missing":missing},indent=2)); return 0
    if out.exists() and any(out.iterdir()) and not a.force: raise SystemExit('out-dir exists, use --force')
    if a.dry_run: print(json.dumps({'status':'dry-run','out_dir':str(out)})); return 0
    out.mkdir(parents=True,exist_ok=True); (out/'cases').mkdir(exist_ok=True)
    lockj=load_contract_lock(lock)
    ch=lockj.get('contract_hash'); scenarios=ALL[:a.max_cases]
    cases=[]; failures=[]
    for sid in scenarios:
        obj=make_case(sid); mid=mutation_id(sid,a.seed,'sha256:synthetic',{},ch)
        cdir=out/'cases'/sid; cdir.mkdir(parents=True,exist_ok=True); p=cdir/f'{mid}.json'; p.write_text(json.dumps(obj,indent=2),encoding='utf-8')
        cases.append({'scenario_id':sid,'mutation_id':mid,'path':str(p),'sha256':sha(p),'artifact_type':'json','expected_detection':True,'expected_validator':'validate_ebird_redteam','expected_policy_gate':'ebird.rego','expected_failure_category':'public_safety'})
        failures.append({'schema_version':'v1','object_type':'EbirdExpectedRedTeamFailure','scenario_id':sid,'mutation_id':mid,'artifact_path':str(p),'expected_failure_category':'public_safety','expected_detector':'scanner','must_fail':True,'synthetic':True})
    man={'schema_version':'v1','object_type':'EbirdMutationCorpusManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'redteam_fixture','public_safe':False,'exact_points':'restricted','synthetic':True,'scenario_set':a.scenario_set,'seed':a.seed,'input_artifacts':[],'generated_cases':cases,'generated_at':now()}
    (out/'mutation_corpus_manifest.json').write_text(json.dumps(man,indent=2),encoding='utf-8')
    (out/'expected_failures.jsonl').write_text('\n'.join(json.dumps(r) for r in failures)+'\n',encoding='utf-8')
    (out/'corpus_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdMutationCorpusValidationReport','status':'pass','synthetic':True,'scenarios_generated':len(cases)},indent=2),encoding='utf-8')
    return 0
if __name__=='__main__': raise SystemExit(main())
