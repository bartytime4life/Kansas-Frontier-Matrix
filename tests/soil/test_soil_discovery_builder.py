from pathlib import Path
import json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py'; PUB=ROOT/'tools/publish/soil/build_release.py'; DISC=ROOT/'tools/discovery/soil/build_discovery.py'; FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'

def run(c): return subprocess.run([sys.executable,*map(str,c)],capture_output=True,text=True)

def prep(tmp_path):
 c=tmp_path/'catalog';p=tmp_path/'pub';o=tmp_path/'ops';d=tmp_path/'disc'
 assert run([CAT,'--receipt',FIX,'--out-root',c]).returncode==0
 assert run([PUB,'--catalog-root',c,'--out-root',p]).returncode==0
 rid=json.loads((p/'published/soil/current.json').read_text())['current_release_id']
 s=o/'ops/soil/status'; s.mkdir(parents=True,exist_ok=True)
 (s/'current_status.json').write_text(json.dumps({'object_type':'SoilOperationalStatus','service_state':'operational','public_access_allowed':True,'latest_probe_decision':'pass','release_id':rid,'active_incidents':[]}))
 (s/'status_receipt.json').write_text(json.dumps({'receipt_type':'OperationalStatusReceipt','signatures':{'dsse':'PROPOSED-COSIGN'}}))
 return p,o,d

def test_builder_ok(tmp_path):
 p,o,d=prep(tmp_path); r=run([DISC,'--published-root',p,'--ops-root',o,'--out-root',d,'--base-public-url','https://example.invalid/kfm/soil']); assert r.returncode==0
 obj=json.loads(r.stdout); did=obj['discovery_id']; rel=d/'discovery/soil/releases'/did
 assert (rel/'discovery_manifest.json').exists(); assert json.loads((rel/'landing.schemaorg.jsonld').read_text())['@type']=='Dataset'
