from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[2]

def run(*c): return subprocess.run([sys.executable,*map(str,c)],capture_output=True,text=True)

def test_rejected_fails(tmp_path):
 r=run(ROOT/'tools/certification/soil/mock_steward_attest.py','--archive-root',tmp_path,'--attestation',ROOT/'tests/fixtures/soil/certification/steward/steward_attestation_rejected.json','--out-root',tmp_path)
 assert r.returncode!=0
