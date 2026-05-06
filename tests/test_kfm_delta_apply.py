import json, subprocess, sys
from pathlib import Path

TOOL=[sys.executable,'tools/tiles/kfm_delta_apply.py']
V='tests/fixtures/tiles/delta_apply/valid'

def run(args): return subprocess.run(args,capture_output=True,text=True)

def test_verify_pass():
    r=run(TOOL+['verify','--manifest',f'{V}/delta_manifest.json','--base-store',f'{V}/base_tile_store.json','--delta-store',f'{V}/delta_tile_store.json','--ledger',f'{V}/applied_ledger.json'])
    assert r.returncode==0

def test_apply_outputs(tmp_path):
    out=tmp_path/'out.json'; rec=tmp_path/'rec.json'
    r=run(TOOL+['apply','--manifest',f'{V}/delta_manifest.json','--base-store',f'{V}/base_tile_store.json','--delta-store',f'{V}/delta_tile_store.json','--ledger',f'{V}/applied_ledger.json','--out-store',str(out),'--receipt',str(rec)])
    assert r.returncode==0
    store=json.loads(out.read_text())
    assert '12/1203/1532' in store['tiles']
    assert store['tiles']['12/1204/1533']['digest']=='sha256:0ecfcd6c5a09deeb99c94098c962f87d207bc2f8b7d4458091cc7ea8aeb13041'
    assert '12/1205/1534' not in store['tiles']

def test_invalid_cases_fail():
    cases=['digest_mismatch','prior_digest_mismatch','base_spec_hash_mismatch','raw_path_reference','ledger_replay_mismatch']
    for c in cases:
      r=run(TOOL+['verify','--manifest',f'tests/fixtures/tiles/delta_apply/invalid/{c}/delta_manifest.json','--base-store',f'tests/fixtures/tiles/delta_apply/invalid/{c}/base.json','--delta-store',f'tests/fixtures/tiles/delta_apply/invalid/{c}/delta.json','--ledger',f'tests/fixtures/tiles/delta_apply/invalid/{c}/ledger.json'])
      assert r.returncode!=0

def test_produced_tile_count_and_masked_pct_fail(tmp_path):
    m=json.loads(Path(f'{V}/delta_manifest.json').read_text()); m['produced_tile_count']=0
    p=tmp_path/'m.json'; p.write_text(json.dumps(m))
    r=run(TOOL+['verify','--manifest',str(p),'--base-store',f'{V}/base_tile_store.json','--delta-store',f'{V}/delta_tile_store.json','--ledger',f'{V}/applied_ledger.json'])
    assert r.returncode!=0
    m['produced_tile_count']=3; m['tiles'][0]['masked_pct']=30; p.write_text(json.dumps(m))
    r=run(TOOL+['verify','--manifest',str(p),'--base-store',f'{V}/base_tile_store.json','--delta-store',f'{V}/delta_tile_store.json','--ledger',f'{V}/applied_ledger.json'])
    assert r.returncode!=0

def test_hash_deterministic():
    a=run(TOOL+['hash','--manifest',f'{V}/delta_manifest.json']).stdout.strip()
    b=run(TOOL+['hash','--manifest',f'{V}/delta_manifest.json']).stdout.strip()
    assert a==b
