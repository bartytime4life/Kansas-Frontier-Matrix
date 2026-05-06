from pathlib import Path
import json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py'; PUB=ROOT/'tools/publish/soil/build_release.py'; DISC=ROOT/'tools/discovery/soil/build_discovery.py'; FED=ROOT/'tools/federation/soil/build_federation.py'; FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'
def run(c): return subprocess.run([sys.executable,*map(str,c)],capture_output=True,text=True)
def prep(tmp_path,retracted=False):
 c=tmp_path/'catalog';p=tmp_path/'pub';o=tmp_path/'ops';d=tmp_path/'disc';f=tmp_path/'fed'
 assert run([CAT,'--receipt',FIX,'--out-root',c]).returncode==0; assert run([PUB,'--catalog-root',c,'--out-root',p]).returncode==0
 rid=json.loads((p/'published/soil/current.json').read_text())['current_release_id']; s=o/'ops/soil/status'; s.mkdir(parents=True,exist_ok=True)
 (s/'current_status.json').write_text(json.dumps({'object_type':'SoilOperationalStatus','service_state':'operational','public_access_allowed':True,'latest_probe_decision':'pass','release_id':rid,'active_incidents':[]})); (s/'status_receipt.json').write_text(json.dumps({'receipt_type':'OperationalStatusReceipt','signatures':{'dsse':'x'}}))
 assert run([DISC,'--published-root',p,'--ops-root',o,'--out-root',d,'--base-public-url','https://example.invalid/kfm/soil']).returncode==0
 if retracted:
  rr=p/'published/soil/retractions'; rr.mkdir(parents=True,exist_ok=True); (rr/f'{rid}.retraction_notice.json').write_text(json.dumps({'release_id':rid,'status':'RETRACTED','reason_type':'test','severity':'high'}))
 return p,o,d,f

def test_federation_ok(tmp_path):
 p,o,d,f=prep(tmp_path); r=run([FED,'--discovery-root',d,'--published-root',p,'--ops-root',o,'--out-root',f,'--base-public-url','https://example.invalid/kfm/soil']); assert r.returncode==0
 obj=json.loads(r.stdout); rel=f/'federation/soil/releases'/obj['federation_id']; assert (rel/'federation_manifest.json').exists(); assert json.loads((rel/'mirror/mirror_manifest.json').read_text())['object_type']=='SoilMirrorManifest'

def test_federation_block_retracted(tmp_path):
 p,o,d,f=prep(tmp_path,retracted=True); r=run([FED,'--discovery-root',d,'--published-root',p,'--ops-root',o,'--out-root',f,'--base-public-url','https://example.invalid/kfm/soil']); assert r.returncode!=0
