from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py';PUB=ROOT/'tools/publish/soil/build_release.py';DIFF=ROOT/'tools/audit/soil/diff_releases.py';FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'
def run(c): return subprocess.run(c,capture_output=True,text=True,check=False)

def setup(tmp:Path):
 c=tmp/'c';assert run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]).returncode==0
 p=tmp/'p';assert run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-old']).returncode==0
 rr=next((c/'receipts/soil').glob('*.promotion_receipt.json'));d=json.loads(rr.read_text());d['bundle_id']='bundle-2';rr2=c/'receipts/soil/b2.promotion_receipt.json';rr2.write_text(json.dumps(d))
 assert run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-new']).returncode==0
 return p

def test_diff(tmp_path:Path):
 p=setup(tmp_path);o=tmp_path/'d.json';r=run([sys.executable,str(DIFF),'--published-root',str(p),'--from-release','soil-old','--to-release','soil-new','--out',str(o)]);assert r.returncode==0
 a=json.loads(o.read_text());assert a['object_type']=='SoilPublishedReleaseDiff';assert 'bundle-2' in a['added_bundles']
 o2=tmp_path/'d2.json';assert run([sys.executable,str(DIFF),'--published-root',str(p),'--from-release','soil-old','--to-release','soil-new','--out',str(o2)]).returncode==0
 b=json.loads(o2.read_text());x={k:v for k,v in a.items() if k!='created'};y={k:v for k,v in b.items() if k!='created'};assert x==y
 assert run([sys.executable,str(DIFF),'--published-root',str(p),'--from-release','missing','--to-release','soil-new','--out',str(tmp_path/'x.json')]).returncode!=0
