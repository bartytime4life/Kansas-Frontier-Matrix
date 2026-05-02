import json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CLI=ROOT/'tools'/'air_quality'/'airnow_normalize_batch.py'
FIX=ROOT/'tests'/'fixtures'/'air_quality'/'airnow'


def run(tmp, manifest):
    return subprocess.run([sys.executable,str(CLI),'--manifest',str(manifest),'--input',str(FIX/'layer2'/'input'/'mixed_valid_invalid_batch.jsonl'),'--out-dir',str(tmp),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)

def test_mixed_batch_and_ordering_and_counts(tmp_path):
    out=run(tmp_path,FIX/'valid'/'intake_manifest_fixture_only.json'); assert out.returncode==0
    r=json.loads((tmp_path/'normalization_receipt.json').read_text())
    assert r['normalized_observation_count']==1 and r['normalized_forecast_count']==1 and r['quarantined_record_count']==2
    obs=[json.loads(x) for x in (tmp_path/'normalized_observations.jsonl').read_text().splitlines() if x]
    assert obs==sorted(obs,key=lambda x:x['canonical_id'])

def test_manifest_denials(tmp_path):
    m=json.loads((FIX/'valid'/'intake_manifest_fixture_only.json').read_text()); m['no_network']=False
    m1=tmp_path/'m1.json'; m1.write_text(json.dumps(m)); assert run(tmp_path,m1).returncode!=0
    m['no_network']=True; m['intake_mode']='bulk_zip_loop'
    m2=tmp_path/'m2.json'; m2.write_text(json.dumps(m)); assert run(tmp_path,m2).returncode!=0

def test_no_network_imports():
    txt=(ROOT/'tools'/'air_quality'/'airnow_normalize_batch.py').read_text()+ (ROOT/'kfm'/'air_quality'/'airnow'/'normalize.py').read_text()
    for bad in ('requests','httpx','aiohttp','urllib.request'):
        assert bad not in txt
