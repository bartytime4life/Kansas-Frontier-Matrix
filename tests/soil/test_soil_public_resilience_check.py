import json, subprocess, sys

def test_cli_help():
 p=subprocess.run([sys.executable,'tools/validators/soil/public_resilience_check.py','--help'],capture_output=True,text=True)
 assert p.returncode==0
 assert '--resilience-root' in p.stdout
