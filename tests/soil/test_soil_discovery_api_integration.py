from tests.soil.test_soil_discovery_builder import prep,run,DISC
from pathlib import Path
import json, subprocess, sys, time, urllib.request
SVC=Path(__file__).resolve().parents[2]/'tools/serve/soil/public_api.py'

def test_api_discovery(tmp_path):
 p,o,d=prep(tmp_path); assert run([DISC,'--published-root',p,'--ops-root',o,'--out-root',d,'--base-public-url','https://example.invalid/kfm/soil']).returncode==0
 proc=subprocess.Popen([sys.executable,str(SVC),'--published-root',str(p),'--ops-root',str(o),'--discovery-root',str(d),'--port','8877'],stdout=subprocess.PIPE,text=True)
 try:
  time.sleep(1)
  with urllib.request.urlopen('http://127.0.0.1:8877/soil/discovery') as r: assert r.status==200
 finally:
  proc.terminate(); proc.wait(timeout=5)
