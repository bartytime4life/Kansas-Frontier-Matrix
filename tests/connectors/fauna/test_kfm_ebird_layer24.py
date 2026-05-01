import json, subprocess
from pathlib import Path

BIN='tools/connectors/fauna/kfm-ebird-ingest'

def test_reconcile_help():
    r=subprocess.run([f'{BIN}/kfm-ebird-reconcile','--help'],capture_output=True,text=True)
    assert r.returncode==0

def test_root_help():
    r=subprocess.run([f'{BIN}/kfm-ebird-root','--help'],capture_output=True,text=True)
    assert r.returncode==0

def test_deterministic_ids(tmp_path: Path):
    out=tmp_path/'rec'
    r1=subprocess.run([f'{BIN}/kfm-ebird-reconcile','--mode','discover','--catalog-root','tests/fixtures/fauna/ebird','--published-root','tests/fixtures/fauna/ebird','--layer-registry-dir','data/published/fauna/layers','--out-dir',str(out),'--force'],capture_output=True,text=True)
    assert r1.returncode==0
    rid=r1.stdout.strip().splitlines()[-1]
    r2=subprocess.run([f'{BIN}/kfm-ebird-reconcile','--mode','discover','--catalog-root','tests/fixtures/fauna/ebird','--published-root','tests/fixtures/fauna/ebird','--layer-registry-dir','data/published/fauna/layers','--out-dir',str(out),'--force'],capture_output=True,text=True)
    assert rid==r2.stdout.strip().splitlines()[-1]
    rm=out/'reconciliation_manifest.json'
    rm.write_text(json.dumps({'reconciliation_id':rid,'aggregate_targets':['both']}))
    a=[f'{BIN}/kfm-ebird-root','--reconciliation-manifest',str(rm),'--out-dir',str(tmp_path/'root'),'--force']
    q1=subprocess.run(a,capture_output=True,text=True); q2=subprocess.run(a,capture_output=True,text=True)
    assert q1.stdout.strip().splitlines()[-1]==q2.stdout.strip().splitlines()[-1]
