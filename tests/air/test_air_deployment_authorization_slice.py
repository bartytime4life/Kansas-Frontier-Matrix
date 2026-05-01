import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
REC=ROOT/'tools/deployments/air/record_air_release_manager_decision.py'
BLD=ROOT/'tools/deployments/air/build_air_deployment_authorization_package.py'
SIM=ROOT/'tools/deployments/air/run_air_local_deployment_simulation.py'
VAL=ROOT/'tools/validators/air/validate_air_deployment_authorization.py'
AUD=ROOT/'tools/auditors/air/audit_air_deployment_authorization.py'
DP=ROOT/'tools/deployments/air/build_air_delivery_deployment_plan.py'
RD=ROOT/'tools/deployments/air/run_air_deployment_readiness.py'
AD=ROOT/'tools/auditors/air/audit_air_delivery_deployment.py'
FX=ROOT/'tests/fixtures/air/deployment_readiness/pass_fixture_deployment_candidate/delivery'

def run(*args): return subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)

def prep(tmp):
 plan=tmp/'plan'; ready=tmp/'ready'; da=tmp/'da'
 assert run(DP,'--delivery-dir',FX,'--out-dir',plan,'--environment','local_fixture','--as-of','2026-04-30T00:00:00Z','--allow-fixture-deployment-plan').returncode==0
 assert run(RD,'--deployment-plan',plan/'delivery_deployment_plan.json','--delivery-dir',FX,'--out-dir',ready,'--as-of','2026-04-30T00:00:00Z','--allow-fixture-readiness').returncode==0
 assert run(AD,plan,ready,'--delivery-dir',FX,'--source-delivery-dir',FX,'--out-dir',da,'--as-of','2026-04-30T00:00:00Z').returncode==0
 for f in ['deployment_environment.json','static_hosting_manifest.json','delivery_deployment_plan.json','synthetic_probe_spec.json','cache_invalidation_plan.json','deployment_rollback_plan.json']: (ready/f).write_text((plan/f).read_text())
 (ready/'deployment_audit_report.json').write_text((da/'deployment_audit_report.json').read_text())
 return ready,da

def test_pass(tmp_path):
 ready,da=prep(tmp_path)
 d=tmp_path/'dec'; a=tmp_path/'auth'; s=tmp_path/'sim'; aa=tmp_path/'audit'
 assert run(REC,'--deployment-readiness-dir',ready,'--decision','approve_fixture_simulation','--decided-by','fixture-release-manager','--role','release_manager','--out-dir',d,'--signature','fixture-signature','--signature-type','fixture_signature','--as-of','2026-04-30T00:00:00Z','--fixture-only').returncode==0
 assert run(BLD,'--deployment-readiness-dir',ready,'--release-manager-decision',d/'release_manager_decision.json','--out-dir',a,'--environment','local_fixture','--as-of','2026-04-30T00:00:00Z','--allow-fixture-authorization').returncode==0
 assert run(SIM,'--authorization-dir',a,'--deployment-readiness-dir',ready,'--delivery-dir',FX,'--out-dir',s,'--as-of','2026-04-30T00:00:00Z','--allow-fixture-simulation').returncode==0
 assert run(VAL,a,s,'--deployment-readiness-dir',ready,'--delivery-dir',FX).returncode==0
 assert run(AUD,a,s,'--deployment-readiness-dir',ready,'--delivery-dir',FX,'--source-deployment-readiness-dir',ready,'--source-delivery-dir',FX,'--out-dir',aa).returncode==0

def test_deny_secret(tmp_path):
 ready,da=prep(tmp_path); d=tmp_path/'dec'; a=tmp_path/'auth'; s=tmp_path/'sim'
 assert run(REC,'--deployment-readiness-dir',ready,'--decision','approve_fixture_simulation','--decided-by','fixture-release-manager','--role','release_manager','--out-dir',d,'--signature','fixture-signature','--signature-type','fixture_signature','--as-of','2026-04-30T00:00:00Z','--fixture-only').returncode==0
 assert run(BLD,'--deployment-readiness-dir',ready,'--release-manager-decision',d/'release_manager_decision.json','--out-dir',a,'--environment','local_fixture','--as-of','2026-04-30T00:00:00Z','--allow-fixture-authorization').returncode==0
 (a/'change_control_handoff.json').write_text((a/'change_control_handoff.json').read_text().replace('manual review','manual review token=abc'))
 assert run(VAL,a,'--deployment-readiness-dir',ready,'--delivery-dir',FX).returncode!=0
