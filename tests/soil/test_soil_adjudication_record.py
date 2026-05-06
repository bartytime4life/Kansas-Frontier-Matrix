import json, subprocess, sys
from pathlib import Path

def test_cli_help():
    r=subprocess.run([sys.executable,'tools/resolution/soil/record_adjudication.py','--help'],capture_output=True,text=True)
    assert r.returncode==0
