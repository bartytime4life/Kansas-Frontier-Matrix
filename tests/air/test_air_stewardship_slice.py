import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
Q=ROOT/'tools/stewards/air/build_air_steward_review_queue.py'
D=ROOT/'tools/stewards/air/record_air_steward_decision.py'
R=ROOT/'tools/retractions/air/build_air_remediation_package.py'
A=ROOT/'tools/retractions/air/apply_air_retraction_fixture.py'
U=ROOT/'tools/auditors/air/audit_air_stewardship.py'

def run(*c): return subprocess.run([sys.executable,*map(str,c)],cwd=ROOT,capture_output=True,text=True)

def test_pass(tmp_path):
 out=tmp_path/'q'; d='tests/fixtures/air/stewardship/pass_fixture_retraction'
 assert run(Q,'--ops-dir',d,'--out-dir',out,'--as-of','2026-04-30T00:00:00Z','--allow-fixture-queue').returncode==0
 assert json.loads((out/'steward_review_queue.json').read_text())['status']=='fixture_only'
 dec=tmp_path/'d'; assert run(D,'--queue',out/'steward_review_queue.json','--item-id','item_fixture_retraction_001','--decision','approve_retraction','--decided-by','fixture-steward','--role','steward','--out-dir',dec,'--signature','fixture-signature','--signature-type','fixture_signature','--as-of','2026-04-30T00:00:00Z','--fixture-only').returncode==0
 rem=tmp_path/'r'; assert run(R,'--steward-decision',dec/'steward_decision.json','--incident-record',f'{d}/incident_record.json','--retraction-request',f'{d}/retraction_request.json','--publication-dir',d,'--out-dir',rem,'--as-of','2026-04-30T00:00:00Z','--fixture-only').returncode==0
 app=tmp_path/'a'; assert run(A,'--remediation-package',rem/'remediation_package.json','--publication-dir',d,'--out-dir',app,'--as-of','2026-04-30T00:00:00Z').returncode==0
 assert json.loads((app/'retraction_execution_manifest.json').read_text())['status']=='executed_fixture_only'
 assert run(U,app).returncode==0

def test_deny_unsigned(tmp_path):
 d='tests/fixtures/air/stewardship/deny_unsigned_decision'
 assert run(A,'--remediation-package',f'{d}/remediation_package.json','--publication-dir',d,'--out-dir',tmp_path/'x','--as-of','2026-04-30T00:00:00Z').returncode!=0
