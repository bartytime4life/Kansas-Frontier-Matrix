#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
from datetime import datetime, timezone
from kfm_ebird_contract import ADAPTER_VERSION, load_contract_lock, canonical_json, version_payload
CRIT={'public_decimalLatitude_field','public_geometry_object','restricted_observation_path_in_public_artifact','suppression_receipt_path_in_public_artifact','suppression_group_hash_in_public_artifact','source_uri_token_query_param_unredacted','exact_points_public'}
def now(): return datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def detect(case):
 p=case.get('payload',{}); hits=[]
 for k in ['decimalLatitude','geometry','suppression_receipt_path','suppression_group_hash','exact_points']: 
  if k in p: hits.append('scanner')
 if 'path' in p and 'restricted_observations' in str(p['path']): hits.append('scanner')
 if 'source_uri' in p and 'token=' in p['source_uri']: hits.append('scanner')
 if p.get('suppression_min_n',10)<10: hits.append('validator')
 if p.get('checklist_count',10)<p.get('suppression_min_n',10): hits.append('validator')
 return sorted(set(hits))
def run(a):
 cdir=Path(a.corpus_dir); manp=cdir/'mutation_corpus_manifest.json'
 if not manp.exists(): raise SystemExit('missing corpus manifest')
 m=json.loads(manp.read_text()); out=Path(a.out_dir)
 if 'data/published' in str(out): raise SystemExit('out-dir cannot be published')
 out.mkdir(parents=True,exist_ok=True)
 lock=load_contract_lock(Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')); ch=lock.get('contract_hash')
 rid=hashlib.sha256(canonical_json({'corpus_manifest_sha256':sha(manp),'scenario_set':a.scenario_set,'adapter_version':ADAPTER_VERSION,'contract_hash':ch,'validator_hashes':['synthetic'],'policy_hashes':['synthetic'],'scanner_hashes':['synthetic'],'fail_open':a.fail_open}).encode()).hexdigest()[:16]
 results=[]; missed=[]; cov=[]
 for c in m['generated_cases']:
  case=json.loads(Path(c['path']).read_text()); det=detect(case); detected=bool(det); status='pass' if detected else 'fail';
  if not detected: missed.append({'scenario_id':c['scenario_id'],'mutation_id':c['mutation_id'],'artifact_path':c['path'],'expected_detector':'scanner','expected_failure_category':'public_safety','recommended_fix':'add detector','severity':'critical' if c['scenario_id'] in CRIT else 'medium'})
  results.append({'schema_version':'v1','object_type':'EbirdRedTeamResult','domain':'fauna','source':'ebird','adapter':'kfm-ebird','redteam_run_id':rid,'scenario_id':c['scenario_id'],'mutation_id':c['mutation_id'],'artifact_path':c['path'],'expected_failure_category':'public_safety','expected_detector':'scanner','actual_detectors_run':['scanner','validator'],'expected_result':'fail','actual_result':'fail' if detected else 'pass','detected':detected,'detector_messages':det,'policy_denies':det,'validator_failures':det,'scanner_findings':det,'status':status,'synthetic':True})
  cov.append({'scenario_id':c['scenario_id'],'expected_failure_category':'public_safety','validators_expected':['validator'],'validators_triggered':['validator'] if 'validator' in det else [],'policies_expected':['ebird.rego'],'policies_triggered':['ebird.rego'] if det else [],'scanners_expected':['scanner'],'scanners_triggered':['scanner'] if 'scanner' in det else [],'coverage_status':'covered' if det else 'missed'})
 crit_missed=sum(1 for x in missed if x['scenario_id'] in CRIT)
 cstatus='fail' if crit_missed else ('warn' if missed else 'pass')
 (out/'redteam_results.jsonl').write_text('\n'.join(json.dumps(x) for x in results)+'\n')
 (out/'missed_detection_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdMissedDetectionReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','redteam_run_id':rid,'missed_detections':missed,'generated_at':now()},indent=2))
 (out/'validator_policy_coverage_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdValidatorPolicyCoverageReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','redteam_run_id':rid,'status':cstatus,'coverage':cov,'coverage_summary':{'scenarios_total':len(cov),'scenarios_covered':sum(1 for x in cov if x['coverage_status']=='covered'),'scenarios_partially_covered':0,'scenarios_missed':sum(1 for x in cov if x['coverage_status']=='missed'),'critical_scenarios_missed':crit_missed},'generated_at':now()},indent=2))
 (out/'safety_regression_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdSafetyRegressionReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','redteam_run_id':rid,'status':'fail' if crit_missed else 'pass','critical_regressions':[{'scenario_id':m['scenario_id'],'mutation_id':m['mutation_id'],'message':'missed detection','expected_detector':'scanner'} for m in missed if m['scenario_id'] in CRIT],'warnings':['fail_open allowed used'] if a.fail_open=='allowed' else [],'public_safety_categories':{},'generated_at':now()},indent=2))
 (out/'redteam_run_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdRedTeamRunManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'redteam','public_safe':False,'exact_points':'restricted','synthetic':True,'redteam_run_id':rid,'scenario_set':a.scenario_set,'corpus_dir':str(cdir),'corpus_manifest_path':str(manp),'corpus_manifest_sha256':sha(manp),'adapter_version':ADAPTER_VERSION,'contract_hash':ch,'validators':[{'name':'validator','path':'synthetic','sha256':'synthetic'}],'policies':[{'name':'ebird.rego','path':'policy/fauna/ebird.rego','sha256':'synthetic'}],'scanners':[{'name':'scanner','path':'synthetic','sha256':'synthetic'}],'outputs':[],'generated_at':now()},indent=2))
 return 2 if crit_missed and a.fail_open=='blocked' else 0

def main():
 ap=argparse.ArgumentParser(prog='kfm-ebird-redteam'); ap.add_argument('--mode',default='run',choices=['run','validate','coverage','report','triage'])
 ap.add_argument('--corpus-dir',default='tools/connectors/fauna/kfm-ebird-ingest/fixtures/redteam/generated'); ap.add_argument('--base-fixture-dir',default='tools/connectors/fauna/kfm-ebird-ingest/fixtures/redteam/base')
 ap.add_argument('--out-dir',default='data/catalog/fauna/ebird/redteam/run'); ap.add_argument('--scenario-set',default='all'); ap.add_argument('--fail-open',default='blocked',choices=['allowed','blocked']); ap.add_argument('--update-baseline',action='store_true'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
 a=ap.parse_args();
 if a.version: print(json.dumps(version_payload('kfm-ebird-redteam', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2,sort_keys=True)); return 0
 if a.dry_run: print(json.dumps({'status':'dry-run'})); return 0
 return run(a)
if __name__=='__main__': raise SystemExit(main())
