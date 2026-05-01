from __future__ import annotations
import json, subprocess, sys, urllib.request, urllib.parse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py'; PUB=ROOT/'tools/publish/soil/build_release.py'; RET=ROOT/'tools/publish/soil/retract_release.py'; SVC=ROOT/'tools/serve/soil/public_api.py'; FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'; REASON=ROOT/'tests/fixtures/soil/retraction/reason_valid.json'
def run(c): return subprocess.run(c,capture_output=True,text=True,check=False)
def make(tmp):
 c=tmp/'c'; assert run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]).returncode==0
 p=tmp/'p'; assert run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-test-release']).returncode==0
 return p
def start(pub):
 p=subprocess.Popen([sys.executable,str(SVC),'--published-root',str(pub),'--host','127.0.0.1','--port','0'],stdout=subprocess.PIPE,text=True)
 return p, json.loads(p.stdout.readline())
def stop(p):
 p.terminate()
 try: p.wait(timeout=5)
 except subprocess.TimeoutExpired: p.kill()
def test_server_endpoints(tmp_path):
 pub=make(tmp_path); p,info=start(pub); base=f"http://127.0.0.1:{info['port']}"
 assert info['service_started'] is True
 assert json.loads(urllib.request.urlopen(base+'/health').read())['audit_passed'] is True
 assert json.loads(urllib.request.urlopen(base+'/openapi.json').read())['info']['version']=='v1'
 recs=json.loads(urllib.request.urlopen(base+'/soil/records').read()); bid=recs['records'][0]['bundle_id']; sid=''.join(ch if ch.isalnum() or ch in '._-' else '_' for ch in bid)
 assert json.loads(urllib.request.urlopen(base+'/soil/records/'+urllib.parse.quote(bid,safe='')).read())['bundle_id']==bid
 assert json.loads(urllib.request.urlopen(base+'/soil/records/'+sid).read())['bundle_id']==bid
 assert json.loads(urllib.request.urlopen(base+f'/soil/focus-cards/{sid}').read())['provisional'] is False
 assert urllib.request.urlopen(base+f'/soil/triplets/{sid}.nt').read().decode().strip()
 assert json.loads(urllib.request.urlopen(base+'/soil/governance/status').read())['public_access_allowed'] is True
 stop(p)
def test_blocked_startup_modes(tmp_path):
 pub=make(tmp_path); cur=pub/'published/soil/current.json'; d=json.loads(cur.read_text()); d['current_release_id']=None; cur.write_text(json.dumps(d)); assert run([sys.executable,str(SVC),'--published-root',str(pub)]).returncode!=0
 pub=make(tmp_path/'x'); assert run([sys.executable,str(RET),'--published-root',str(pub),'--release-id','soil-test-release','--reason',str(REASON)]).returncode==0; assert run([sys.executable,str(SVC),'--published-root',str(pub)]).returncode!=0
