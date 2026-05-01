from __future__ import annotations
import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CHK=ROOT/'tools/validators/soil/access_log_check.py'; V=ROOT/'tests/fixtures/soil/ops/access/access_log_valid.jsonl'; I=ROOT/'tests/fixtures/soil/ops/access/access_log_invalid_secret.jsonl'
def test_access_log_check():
 assert subprocess.run([sys.executable,str(CHK),'--access-log',str(V)]).returncode==0
 assert subprocess.run([sys.executable,str(CHK),'--access-log',str(I)]).returncode!=0
