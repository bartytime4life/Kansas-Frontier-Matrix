import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FIX=ROOT/'tests/fixtures/air/reentry_read_model_refresh/pass_fixture_read_model_refresh/materialization'

def run(cmd,ok=True):
 r=subprocess.run(cmd,capture_output=True,text=True)
 if ok:
  assert r.returncode==0,(cmd,r.stdout,r.stderr)
 else:
  assert r.returncode!=0

def test_smoke(tmp_path):
 plan=tmp_path/'plan';prev=tmp_path/'prev';dec=tmp_path/'dec';aud=tmp_path/'aud'
 run([sys.executable,str(ROOT/'tools/publishers/air/plan_air_reentry_public_read_model_refresh.py'),'--materialization-dir',str(FIX),'--materialization-ledger',str(FIX/'reentry_publication_materialization_ledger_manifest.json'),'--materialization-postcheck',str(FIX/'reentry_publication_materialization_postcheck_report.json'),'--materialization-audit',str(FIX/'reentry_publication_materialization_audit_report.json'),'--out-dir',str(plan),'--as-of','2026-04-30T00:00:00Z','--allow-fixture-plan'])
 run([sys.executable,str(ROOT/'tools/publishers/air/build_air_reentry_public_read_model_refresh_preview.py'),'--refresh-plan',str(plan/'reentry_public_read_model_refresh_plan.json'),'--materialization-dir',str(FIX),'--out-dir',str(prev),'--fixture-only'])
 run([sys.executable,str(ROOT/'tools/publishers/air/decide_air_reentry_read_model_refresh.py'),'--read-model-refresh-manifest',str(prev/'reentry_read_model_refresh_manifest.json'),'--refresh-plan',str(plan/'reentry_public_read_model_refresh_plan.json'),'--materialization-postcheck',str(FIX/'reentry_publication_materialization_postcheck_report.json'),'--materialization-audit',str(FIX/'reentry_publication_materialization_audit_report.json'),'--out-dir',str(dec),'--fixture-only'])
 run([sys.executable,str(ROOT/'tools/validators/air/validate_air_reentry_read_model_refresh.py'),str(plan),str(prev),str(dec)])
 run([sys.executable,str(ROOT/'tools/auditors/air/audit_air_reentry_read_model_refresh.py'),str(plan),str(prev),str(dec),'--out-dir',str(aud)])
