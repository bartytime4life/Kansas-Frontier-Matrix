from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py'; PUB=ROOT/'tools/publish/soil/build_release.py'; SVC=ROOT/'tools/serve/soil/public_api.py'; CHK=ROOT/'tools/validators/soil/api_contract_check.py'; FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'; OAPI=ROOT/'schemas/openapi/soil_public_api.openapi.json'
def run(c): return subprocess.run(c,capture_output=True,text=True,check=False)
def test_contract(tmp_path):
 c=tmp_path/'c';run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]);p=tmp_path/'p';run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-test-release'])
 sp=subprocess.Popen([sys.executable,str(SVC),'--published-root',str(p),'--port','0'],stdout=subprocess.PIPE,text=True); info=json.loads(sp.stdout.readline()); base=f"http://127.0.0.1:{info['port']}"
 assert run([sys.executable,str(CHK),'--base-url',base,'--openapi',str(OAPI)]).returncode==0
 bad=tmp_path/'bad.json'; d=json.loads(OAPI.read_text()); d['paths'].pop('/health'); bad.write_text(json.dumps(d)); assert run([sys.executable,str(CHK),'--base-url',base,'--openapi',str(bad)]).returncode!=0
 sp.terminate()
 try: sp.wait(timeout=5)
 except subprocess.TimeoutExpired: sp.kill()
