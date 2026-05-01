from pathlib import Path
import subprocess, sys, json
ROOT=Path(__file__).resolve().parents[2]

def test_tools_help():
 for p in ['tools/trust_registry/soil/build_trust_registry.py','tools/validators/soil/trust_registry_check.py','tools/trust_registry/soil/verify_trust_certificate.py','tools/trust_registry/soil/record_certificate_event.py','tools/validators/soil/trust_registry_gate.py']:
  r=subprocess.run([sys.executable,str(ROOT/p),'--help'],capture_output=True,text=True)
  assert r.returncode==0
