import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def test_valid_sentinel(tmp_path):
 p=subprocess.run([sys.executable,ROOT/'tools/stability/soil/record_regression_sentinel.py','--continuity-root',tmp_path/'c','--stability-root',tmp_path/'s','--sentinel',ROOT/'tests/fixtures/soil/stability/sentinels/regression_sentinel_valid.json'],capture_output=True,text=True)
 assert p.returncode==0
