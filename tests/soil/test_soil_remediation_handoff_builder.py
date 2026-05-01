import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def run(*a): return subprocess.run([sys.executable,*map(str,a)],capture_output=True,text=True,cwd=ROOT)

def test_builder_smoke(tmp_path):
 c=tmp_path/'c'; (c/'corrective/soil/cycles/soil-corrective-test').mkdir(parents=True)
 (c/'corrective/soil').mkdir(parents=True,exist_ok=True)
 (c/'corrective/soil/current_corrective_action.json').write_text('{"active_corrective_id":"soil-corrective-test"}')
 (c/'corrective/soil/cycles/soil-corrective-test/corrective_action_manifest.json').write_text('{"release_id":"soil-test-release","registry_id":"soil-registry-test","resolution_id":"soil-resolution-test","accountability_id":"soil-accountability-test","assurance_id":"soil-assurance-test","records":[]}')
 r=run('tools/remediation/soil/build_remediation_handoff.py','--corrective-root',c,'--out-root',tmp_path/'r','--base-public-url','https://example.invalid/kfm/soil')
 assert r.returncode==0, r.stderr
 out=json.loads(r.stdout)
 assert out['remediation_handoff_allowed'] is True
 rc=run('tools/validators/soil/remediation_handoff_check.py','--remediation-root',tmp_path/'r')
 assert rc.returncode==0
