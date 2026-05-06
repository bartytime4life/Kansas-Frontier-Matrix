from __future__ import annotations
import subprocess, sys, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py'; PUB=ROOT/'tools/publish/soil/build_release.py'; SVC=ROOT/'tools/serve/soil/public_api.py'; PR=ROOT/'tools/ops/soil/synthetic_probe.py'; FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'
def run(c): return subprocess.run(c,capture_output=True,text=True)
def make(tmp):
 c=tmp/'c'; p=tmp/'p'; assert run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]).returncode==0; assert run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-test-release']).returncode==0; return p

def test_probe(tmp_path):
 pub=make(tmp_path); sp=subprocess.Popen([sys.executable,str(SVC),'--published-root',str(pub),'--host','127.0.0.1','--port','0'],stdout=subprocess.PIPE,text=True)
 info=json.loads(sp.stdout.readline()); base=f"http://127.0.0.1:{info['port']}"
 assert run([sys.executable,str(PR),'--base-url',base,'--expected-release-id','soil-test-release','--out-root',str(tmp_path/'ops')]).returncode==0
 assert run([sys.executable,str(PR),'--base-url','http://127.0.0.1:9']).returncode!=0
 sp.terminate(); sp.wait()
