#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path
from kfm_ebird_contract import ADAPTER_VERSION, now_iso, verify_contract_lock, load_contract_lock, version_payload

CLI_NAMES=['kfm-ebird-ingest','kfm-ebird-aggregate','kfm-ebird-promote','kfm-ebird-build-public-view','kfm-ebird-run-pipeline','kfm-ebird-release-ops','kfm-ebird-observe','kfm-ebird-doctor','kfm-ebird-conformance']

def parse_args(argv):
    p=argparse.ArgumentParser(prog='kfm-ebird-doctor', description='Local eBird adapter readiness checks (no network).')
    p.add_argument('--repo-root', default='.')
    p.add_argument('--contract-lock', default='tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')
    p.add_argument('--json', action='store_true')
    p.add_argument('--strict', action='store_true')
    p.add_argument('--version', action='store_true')
    return p.parse_args(argv)

def run():
    a=parse_args(sys.argv[1:])
    if a.version:
        print(json.dumps(version_payload('kfm-ebird-doctor', Path(a.contract_lock)), indent=2, sort_keys=True)); return 0
    root=Path(a.repo_root); checks=[]
    tooldir=root/'tools/connectors/fauna/kfm-ebird-ingest'
    for cli in CLI_NAMES:
        p=tooldir/cli
        ok=p.exists()
        checks.append({'name':f'cli_exists:{cli}','category':'cli','status':'pass' if ok else 'fail','message':'found' if ok else 'missing','artifact_path':str(p)})
    lock=root/a.contract_lock
    if lock.exists():
        data=load_contract_lock(lock); ok,exp,act=verify_contract_lock(data)
        checks.append({'name':'contract_lock_hash','category':'contract','status':'pass' if ok else 'fail','message':f'expected {exp} got {act}','artifact_path':str(lock)})
        contract_hash=data.get('contract_hash')
    else:
        checks.append({'name':'contract_lock_exists','category':'contract','status':'fail','message':'missing','artifact_path':str(lock)})
        contract_hash=None
    status='pass' if all(c['status']=='pass' for c in checks) else 'fail'
    report={'schema_version':'v1','object_type':'EbirdDoctorReport','domain':'fauna','source':'ebird','adapter_version':ADAPTER_VERSION,'status':status,'checks':checks,'contract_hash':contract_hash,'generated_at':now_iso()}
    if a.json: print(json.dumps(report,indent=2,sort_keys=True))
    else: print(f"kfm-ebird doctor: {status} ({sum(c['status']=='pass' for c in checks)}/{len(checks)} passed)")
    return 0 if status=='pass' else 1
if __name__=='__main__': raise SystemExit(run())
