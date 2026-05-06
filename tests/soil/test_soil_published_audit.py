from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py';PUB=ROOT/'tools/publish/soil/build_release.py';AUD=ROOT/'tools/audit/soil/audit_published.py';FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'

def run(cmd): return subprocess.run(cmd,capture_output=True,text=True,check=False)
def mk(tmp:Path): c=tmp/'c';assert run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]).returncode==0; p=tmp/'p';r=run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-test-release']);assert r.returncode==0; return p

def test_audit_ok_and_out(tmp_path:Path):
 p=mk(tmp_path);o=tmp_path/'o';r=run([sys.executable,str(AUD),'--published-root',str(p),'--out-root',str(o)]);assert r.returncode==0
 assert (o/'audits/soil/soil-test-release.audit_report.json').exists()

def test_audit_failure_modes(tmp_path:Path):
 p=mk(tmp_path);rel=p/'published/soil/releases/soil-test-release';
 for mode in ['tamper','secret','provisional','forbidden_path','traversal','missing_receipt']:
  q=tmp_path/mode; subprocess.run(['cp','-a',str(p),str(q)],check=True)
  rrel=q/'published/soil/releases/soil-test-release'
  if mode=='tamper': d=json.loads((rrel/'index.json').read_text());d['records'][0]['metrics']['masked_pct']=999;(rrel/'index.json').write_text(json.dumps(d))
  elif mode=='secret': d=json.loads((rrel/'index.json').read_text());d['records'][0]['token']='abc';(rrel/'index.json').write_text(json.dumps(d))
  elif mode=='provisional': fc=next((rrel/'focus_cards').glob('*.json'));d=json.loads(fc.read_text());d['provisional']=True;fc.write_text(json.dumps(d))
  elif mode=='forbidden_path': d=json.loads((rrel/'manifest.json').read_text());d['bundles'][0]['triplet_ref']='RAW/file';(rrel/'manifest.json').write_text(json.dumps(d))
  elif mode=='traversal': d=json.loads((rrel/'manifest.json').read_text());k=next(iter(d['artifact_hashes'].keys()));d['artifact_hashes']['../escape']=d['artifact_hashes'][k];(rrel/'manifest.json').write_text(json.dumps(d))
  elif mode=='missing_receipt': (rrel/'publication_receipt.json').unlink()
  rr=run([sys.executable,str(AUD),'--published-root',str(q),'--release-id','soil-test-release']);assert rr.returncode!=0,mode
