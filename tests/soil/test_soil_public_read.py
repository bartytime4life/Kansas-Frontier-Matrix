from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py';PUB=ROOT/'tools/publish/soil/build_release.py';Q=ROOT/'tools/query/soil/public_read.py';FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'

def run(cmd): return subprocess.run(cmd,capture_output=True,text=True,check=False)

def setup_pub(tmp_path:Path)->Path:
    c=tmp_path/'c';assert run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]).returncode==0
    p=tmp_path/'p';assert run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p)]).returncode==0
    return p

def test_public_read(tmp_path:Path):
    p=setup_pub(tmp_path);r=run([sys.executable,str(Q),'--published-root',str(p),'--list']);assert r.returncode==0
    rows=json.loads(r.stdout)['records'];bid=rows[0]['bundle_id']
    r2=run([sys.executable,str(Q),'--published-root',str(p),'--bundle-id',bid]);assert r2.returncode==0
    assert all(x not in r2.stdout for x in ['RAW','WORK','QUARANTINE','PROCESSED'])
    r3=run([sys.executable,str(Q),'--published-root',str(p),'--bundle-id','missing']);assert r3.returncode!=0

def test_missing_current_or_bad_receipt(tmp_path:Path):
    p=setup_pub(tmp_path);(p/'published/soil/current.json').unlink();assert run([sys.executable,str(Q),'--published-root',str(p),'--list']).returncode!=0
