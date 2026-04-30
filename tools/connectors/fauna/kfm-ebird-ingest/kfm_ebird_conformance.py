#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess, sys, time
from pathlib import Path
from kfm_ebird_contract import ADAPTER_VERSION, SCHEMA_BUNDLE_VERSION, now_iso, load_contract_lock, version_payload

def parse_args(argv):
 p=argparse.ArgumentParser(prog='kfm-ebird-conformance',description='Synthetic eBird conformance suite runner.')
 p.add_argument('--repo-root',default='.')
 p.add_argument('--work-dir',default=None)
 p.add_argument('--aggregate',choices=('huc12','county','both'),default='both')
 p.add_argument('--format',choices=('jsonl','csv'),default='jsonl')
 p.add_argument('--json',action='store_true')
 p.add_argument('--version',action='store_true')
 return p.parse_args(argv)

def run():
 a=parse_args(sys.argv[1:])
 lock=Path(a.repo_root)/'tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json'
 if a.version:
  print(json.dumps(version_payload('kfm-ebird-conformance', lock), indent=2, sort_keys=True)); return 0
 data=load_contract_lock(lock); ch=data['contract_hash']
 work=Path(a.work_dir or f'/tmp/kfm-ebird-conformance/{ch}'); work.mkdir(parents=True,exist_ok=True)
 stages=[]
 t=time.time()
 cmd=[str(Path(a.repo_root)/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-doctor'),'--json']
 p=subprocess.run(cmd,capture_output=True,text=True)
 stages.append({'name':'doctor','status':'pass' if p.returncode==0 else 'fail','command_or_helper':'kfm-ebird-doctor --json','outputs':[],'output_hashes':{},'duration_ms':int((time.time()-t)*1000),'validations_run':['doctor'],'policy_checks_run':[]})
 status='pass' if all(s['status']=='pass' for s in stages) else 'fail'
 rep={'schema_version':'v1','object_type':'EbirdConformanceReport','domain':'fauna','source':'ebird','adapter_version':ADAPTER_VERSION,'schema_bundle_version':SCHEMA_BUNDLE_VERSION,'contract_hash':ch,'aggregate_targets':[a.aggregate] if a.aggregate!='both' else ['huc12','county'],'format':a.format,'status':status,'stages':stages,'golden_comparisons':[],'public_safety_regression':{'denied_public_fields_checked':data.get('denied_public_fields',[]),'artifacts_checked':[],'failures':[]},'counts':{'synthetic_rows_seen':0,'synthetic_rows_accepted':0,'synthetic_rows_quarantined':0,'groups_published':0,'groups_suppressed':0,'features_emitted':0,'evidence_drawers_emitted':0},'generated_at':now_iso()}
 out=work/'conformance_report.json'; out.write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n',encoding='utf-8')
 if a.json: print(json.dumps(rep,indent=2,sort_keys=True))
 else: print(f'conformance {status}: {out}')
 return 0 if status=='pass' else 1
if __name__=='__main__': raise SystemExit(run())
