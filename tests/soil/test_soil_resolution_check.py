import subprocess, sys

def test_cli_help():
    r=subprocess.run([sys.executable,'tools/validators/soil/resolution_check.py','--help'],capture_output=True,text=True)
    assert r.returncode==0
