from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py';PUB=ROOT/'tools/publish/soil/build_release.py';RET=ROOT/'tools/publish/soil/retract_release.py';Q=ROOT/'tools/query/soil/public_read.py';FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'
RV=ROOT/'tests/fixtures/soil/retraction/reason_valid.json';RM=ROOT/'tests/fixtures/soil/retraction/reason_invalid_missing_review.json';RU=ROOT/'tests/fixtures/soil/retraction/reason_invalid_unknown_type.json'
def run(c): return subprocess.run(c,capture_output=True,text=True,check=False)
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def setup(tmp:Path): c=tmp/'c';assert run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]).returncode==0; p=tmp/'p';assert run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-test-release']).returncode==0; return p

def test_retract_and_public_read_block(tmp_path:Path):
 p=setup(tmp_path);rel=p/'published/soil/releases/soil-test-release';m0,i0,r0=h(rel/'manifest.json'),h(rel/'index.json'),h(rel/'publication_receipt.json')
 rr=run([sys.executable,str(RET),'--published-root',str(p),'--release-id','soil-test-release','--reason',str(RV)]);assert rr.returncode==0
 assert h(rel/'manifest.json')==m0 and h(rel/'index.json')==i0 and h(rel/'publication_receipt.json')==r0
 cur=json.loads((p/'published/soil/current.json').read_text());assert cur['current_release_id'] is None
 assert run([sys.executable,str(Q),'--published-root',str(p),'--list']).returncode!=0
 assert (p/'published/soil/releases/soil-test-release').exists()

def test_retract_with_replacement_and_invalids(tmp_path:Path):
 p=setup(tmp_path);assert run([sys.executable,str(PUB),'--catalog-root',str(tmp_path/'c'),'--out-root',str(p),'--release-id','soil-corrected-release']).returncode==0
 assert run([sys.executable,str(RET),'--published-root',str(p),'--release-id','soil-test-release','--replacement-release-id','soil-corrected-release','--reason',str(RV)]).returncode==0
 cur=json.loads((p/'published/soil/current.json').read_text());assert cur['current_release_id']=='soil-corrected-release'
 assert run([sys.executable,str(RET),'--published-root',str(p),'--release-id','soil-corrected-release','--reason',str(RM)]).returncode!=0
 assert run([sys.executable,str(RET),'--published-root',str(p),'--release-id','soil-corrected-release','--reason',str(RU)]).returncode!=0
 assert run([sys.executable,str(RET),'--published-root',str(p),'--release-id','soil-corrected-release','--replacement-release-id','missing','--reason',str(RV)]).returncode!=0
