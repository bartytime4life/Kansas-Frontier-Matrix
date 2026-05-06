import subprocess,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
B=ROOT/'tools/publishers/air/build_air_client_delivery_package.py'
V=ROOT/'tools/validators/air/validate_air_client_delivery.py'
A=ROOT/'tools/auditors/air/audit_air_client_delivery.py'
E=ROOT/'tools/clients/air/emulate_air_static_api.py'
FX=ROOT/'tests/fixtures/air/client_delivery/pass_fixture_delivery/read_model'
def run(*args): return subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)

def test_pass(tmp_path):
 out=tmp_path/'out'
 assert run(B,'--read-model-dir',FX,'--out-dir',out,'--api-version','v1','--as-of','2026-04-30T00:00:00Z','--allow-fixture-delivery').returncode==0
 assert run(V,out,'--as-of','2026-04-30T00:00:00Z').returncode==0
 aud=tmp_path/'aud'; assert run(A,out,'--source-read-model-dir',FX,'--out-dir',aud,'--as-of','2026-04-30T00:00:00Z').returncode==0
 assert run(E,'--delivery-dir',out,'--route','/air/v1/index','--include-candidates','--show-headers').returncode==0
 assert json.loads((out/'client_delivery_manifest.json').read_text())['status']=='fixture_delivery_candidate'

def test_deny_bad_etag_fixture():
 d=ROOT/'tests/fixtures/air/client_delivery/deny_bad_etag'
 assert run(V,d,'--as-of','2026-04-30T00:00:00Z').returncode!=0
