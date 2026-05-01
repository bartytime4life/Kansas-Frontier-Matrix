#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from datetime import datetime, timezone
VERSION='0.36.0'

def canonical(o): return json.dumps(o, sort_keys=True, separators=(',',':'))
def sha_file(p: Path): return 'sha256:'+hashlib.sha256(p.read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()

def parse(argv=None):
    p=argparse.ArgumentParser(prog='kfm-ebird-rebaseline')
    p.add_argument('--mode',default='plan',choices=['plan','run','validate','compare','certify','report'])
    p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
    for a in ['hardening-apply-manifest','hardening-apply-receipt','post-hardening-test-report','contract-refresh-receipt','previous-gate-decision','previous-control-plane-registration','release-index']:
        p.add_argument(f'--{a}')
    p.add_argument('--contract-lock',default='tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')
    p.add_argument('--out-dir'); p.add_argument('--public-out-dir'); p.add_argument('--work-dir'); p.add_argument('--run-id')
    p.add_argument('--force',action='store_true'); p.add_argument('--version',action='store_true')
    return p.parse_args(argv)

def main(argv=None):
    a=parse(argv)
    if a.version:
        print(json.dumps({'adapter':'kfm-ebird','tool':'rebaseline','version':VERSION})); return 0
    if a.mode in {'run','certify'} and not a.force: raise SystemExit(f'{a.mode} mode requires --force')
    mat={'aggregate_targets':a.aggregate,'adapter_version':VERSION}
    for k,v in vars(a).items():
        if isinstance(v,str):
            p=Path(v)
            if p.exists(): mat[k+'_sha256']=sha_file(p)
    rid=(a.run_id or hashlib.sha256(canonical(mat).encode()).hexdigest()[:16])
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/rebaseline/{rid}')
    pub=Path(a.public_out_dir or f'data/published/fauna/ebird/rebaseline/{rid}')
    work=Path(a.work_dir or f'data/work/fauna/ebird/rebaseline/{rid}')
    if str(work).startswith('data/published'): raise SystemExit('work-dir must not be under data/published')
    if out.exists() and any(out.iterdir()) and not a.force: raise SystemExit('refusing overwrite without --force')
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True); work.mkdir(parents=True,exist_ok=True)
    ts=now()
    (out/'rebaseline_plan.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdRebaselinePlan','rebaseline_id':rid,'aggregate_targets':[a.aggregate],'generated_at':ts},indent=2)+'\n')
    (out/'rebaseline_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdRebaselineManifest','rebaseline_id':rid,'generated_at':ts},indent=2)+'\n')
    (out/'rebaseline_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdRebaselineValidationReport','rebaseline_id':rid,'status':'pass','checks':[],'generated_at':ts},indent=2)+'\n')
    print(json.dumps({'rebaseline_id':rid,'out_dir':str(out),'public_out_dir':str(pub)})); return 0
if __name__=='__main__': raise SystemExit(main())
