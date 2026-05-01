import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CHK=ROOT/'tools/validators/soil/preservation_check.py'
def test_cli_requires_valid(tmp_path):
 r=subprocess.run([sys.executable,str(CHK),'--preservation-root',str(tmp_path)],capture_output=True,text=True)
 assert r.returncode!=0
