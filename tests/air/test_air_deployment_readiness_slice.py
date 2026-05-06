import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
B=ROOT/'tools/deployments/air/build_air_delivery_deployment_plan.py'
R=ROOT/'tools/deployments/air/run_air_deployment_readiness.py'
V=ROOT/'tools/validators/air/validate_air_deployment_readiness.py'
A=ROOT/'tools/auditors/air/audit_air_delivery_deployment.py'
E=ROOT/'tools/deployments/air/emulate_air_static_hosting.py'
FX=ROOT/'tests/fixtures/air/deployment_readiness/pass_fixture_deployment_candidate/delivery'
def run(*args): return subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)
def test_pass(tmp_path):
 plan=tmp_path/'plan'; rd=tmp_path/'ready'; ad=tmp_path/'aud'
 assert run(B,'--delivery-dir',FX,'--out-dir',plan,'--environment','local_fixture','--as-of','2026-04-30T00:00:00Z','--allow-fixture-deployment-plan').returncode==0
 assert run(R,'--deployment-plan',plan/'delivery_deployment_plan.json','--delivery-dir',FX,'--out-dir',rd,'--as-of','2026-04-30T00:00:00Z','--allow-fixture-readiness').returncode==0
 assert run(V,plan,rd,'--delivery-dir',FX).returncode==0
 assert run(A,plan,rd,'--delivery-dir',FX,'--source-delivery-dir',FX,'--out-dir',ad,'--as-of','2026-04-30T00:00:00Z').returncode==0
 assert run(E,'--deployment-dir',plan,'--delivery-dir',FX,'--route','/air/v1/index','--include-candidates','--show-headers').returncode==0

def test_deny_missing_manifest(tmp_path):
 d=ROOT/'tests/fixtures/air/deployment_readiness/deny_missing_delivery_manifest/delivery'
 assert run(B,'--delivery-dir',d,'--out-dir',tmp_path/'x','--environment','local_fixture','--as-of','2026-04-30T00:00:00Z','--allow-fixture-deployment-plan').returncode!=0
