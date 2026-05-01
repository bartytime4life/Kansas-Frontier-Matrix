import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
AUD=ROOT/'tools/auditors/air/replay_air_lineage.py'
MON=ROOT/'tools/monitors/air/build_air_public_ops_health.py'
RET=ROOT/'tools/retractions/air/prepare_air_retraction.py'

def run(script,*args): return subprocess.run([sys.executable,str(script),*args],cwd=ROOT,capture_output=True,text=True)

def test_pass_fixture_candidate(tmp_path):
 d='tests/fixtures/air/public_ops/pass_fixture_candidate'; out=tmp_path/'o'
 r=run(MON,'--read-model-dir',d,'--out-dir',str(out),'--as-of','2026-04-30T00:00:00Z','--allow-fixture-ops'); assert r.returncode==0
 assert json.loads((out/'public_ops_health.json').read_text())['status']=='fixture_only'
 assert json.loads((out/'public_slo_report.json').read_text())['status']=='fixture_only'
 assert (out/'ops_events.jsonl').exists()

def test_deny_raw_path_leak(tmp_path):
 d='tests/fixtures/air/public_ops/deny_raw_path_leak'; out=tmp_path/'d'
 r=run(MON,'--read-model-dir',d,'--out-dir',str(out),'--as-of','2026-04-30T00:00:00Z'); assert r.returncode!=0

def test_retraction_candidate(tmp_path):
 d='tests/fixtures/air/public_ops/retraction_request_candidate'; out=tmp_path/'r'
 r=run(RET,'--incident-record',f'{d}/incident_record.json','--publication-dir',d,'--out-dir',str(out),'--as-of','2026-04-30T00:00:00Z'); assert r.returncode==0
 req=json.loads((out/'retraction_request.json').read_text()); assert req['status']=='candidate'; assert req['steward_review_required'] is True
