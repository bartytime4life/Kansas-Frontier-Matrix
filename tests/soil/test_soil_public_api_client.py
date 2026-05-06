from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py'; PUB=ROOT/'tools/publish/soil/build_release.py'; SVC=ROOT/'tools/serve/soil/public_api.py'; CLI=ROOT/'tools/query/soil/public_api_client.py'; FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'
def run(c): return subprocess.run(c,capture_output=True,text=True,check=False)
def setup(tmp):
 c=tmp/'c';run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]);p=tmp/'p';run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-test-release'])
 sp=subprocess.Popen([sys.executable,str(SVC),'--published-root',str(p),'--port','0'],stdout=subprocess.PIPE,text=True); info=json.loads(sp.stdout.readline()); return sp, f"http://127.0.0.1:{info['port']}"
def stop(p):
 p.terminate()
 try: p.wait(timeout=5)
 except subprocess.TimeoutExpired: p.kill()
def test_client(tmp_path):
 sp,base=setup(tmp_path)
 assert run([sys.executable,str(CLI),'--base-url',base,'--health']).returncode==0
 rr=run([sys.executable,str(CLI),'--base-url',base,'--list']); assert rr.returncode==0; bid=json.loads(rr.stdout)['records'][0]['bundle_id']
 assert run([sys.executable,str(CLI),'--base-url',base,'--bundle-id',bid]).returncode==0
 assert run([sys.executable,str(CLI),'--base-url',base,'--bundle-id','missing']).returncode!=0
 assert run([sys.executable,str(CLI),'--base-url','http://127.0.0.1:9','--health']).returncode!=0
 stop(sp)
