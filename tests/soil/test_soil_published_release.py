from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py'
PUB=ROOT/'tools/publish/soil/build_release.py'
FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'

def run(cmd): return subprocess.run(cmd,capture_output=True,text=True,check=False)

def make_catalog(tmp_path:Path)->Path:
    croot=tmp_path/'catalog';r=run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(croot)]);assert r.returncode==0,r.stderr;return croot

def test_publish_pass_and_idempotent(tmp_path:Path):
    c=make_catalog(tmp_path);out=tmp_path/'pub'
    r=run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(out),'--release-id','soil-test-release']);assert r.returncode==0
    rid=json.loads(r.stdout)['release_id'];rel=out/'published/soil/releases'/rid
    assert (rel/'manifest.json').exists();assert (rel/'index.json').exists();assert (rel/'publication_receipt.json').exists();assert (out/'published/soil/current.json').exists()
    card=next((rel/'focus_cards').glob('*.json'));assert json.loads(card.read_text())['provisional'] is False
    assert next((rel/'triplets').glob('*.nt')).exists()
    r2=run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(out),'--release-id','soil-test-release']);assert r2.returncode==0

def test_blocks(tmp_path:Path):
    c=make_catalog(tmp_path);rp=next((c/'receipts/soil').glob('*.promotion_receipt.json'));payload=json.loads(rp.read_text())
    # tampered hash
    payload['generated_artifacts']['stac']['sha256']='0'*64;rp.write_text(json.dumps(payload));
    out=tmp_path/'pub1';r=run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(out)]);assert r.returncode!=0;assert not (out/'published/soil/releases').exists()
