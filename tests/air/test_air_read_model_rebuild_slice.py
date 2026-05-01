import subprocess,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'tools/publishers/air/plan_air_read_model_rebuild.py';B=ROOT/'tools/publishers/air/rebuild_air_public_read_model_from_plan.py';A=ROOT/'tools/auditors/air/audit_air_read_model_rebuild.py'
def run(*args): return subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)
def test_pass(tmp_path):
 d=ROOT/'tests/fixtures/air/read_model_rebuild/pass_fixture_rebuild'; po=tmp_path/'plan'; ro=tmp_path/'reb'
 assert run(P,'--read-model-dir',d/'source_read_model','--stewardship-dir',d/'stewardship','--out-dir',po,'--as-of','2026-04-30T00:00:00Z','--allow-fixture-plan').returncode==0
 assert run(B,'--rebuild-plan',po/'read_model_rebuild_plan.json','--read-model-dir',d/'source_read_model','--out-dir',ro,'--as-of','2026-04-30T00:00:00Z','--fixture-only').returncode==0
 assert run(A,ro,'--source-read-model-dir',d/'source_read_model','--as-of','2026-04-30T00:00:00Z').returncode==0
 assert json.loads((ro/'public_status.json').read_text())['retracted_records']>=1

def test_denies(tmp_path):
 for name in ['deny_missing_tombstone','deny_missing_invalidation_notice','deny_missing_steward_decision','deny_unapproved_steward_decision']:
  d=ROOT/'tests/fixtures/air/read_model_rebuild'/name
  r=run(P,'--read-model-dir',d/'source_read_model','--stewardship-dir',d/'stewardship','--out-dir',tmp_path/name,'--as-of','2026-04-30T00:00:00Z','--allow-fixture-plan')
  assert r.returncode!=0
