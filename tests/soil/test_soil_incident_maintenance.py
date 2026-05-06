from __future__ import annotations
import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAT=ROOT/'tools/catalog/soil/build_catalog.py'; PUB=ROOT/'tools/publish/soil/build_release.py'; RI=ROOT/'tools/ops/soil/record_incident.py'; RM=ROOT/'tools/ops/soil/record_maintenance.py'; FIX=ROOT/'tests/fixtures/soil/catalog/run_receipt_pass_embedded_bundle.json'
def run(c): return subprocess.run(c,capture_output=True,text=True)
def make(tmp):
 c=tmp/'c'; p=tmp/'p'; assert run([sys.executable,str(CAT),'--receipt',str(FIX),'--out-root',str(c)]).returncode==0; assert run([sys.executable,str(PUB),'--catalog-root',str(c),'--out-root',str(p),'--release-id','soil-test-release']).returncode==0; return p

def test_incident_maintenance(tmp_path):
 pub=make(tmp_path); ops=tmp_path/'ops'
 assert run([sys.executable,str(RI),'--ops-root',str(ops),'--published-root',str(pub),'--incident',str(ROOT/'tests/fixtures/soil/ops/incidents/incident_valid_low.json')]).returncode==0
 assert run([sys.executable,str(RI),'--ops-root',str(ops),'--published-root',str(pub),'--incident',str(ROOT/'tests/fixtures/soil/ops/incidents/incident_invalid_secret_leak.json')]).returncode!=0
 assert run([sys.executable,str(RM),'--ops-root',str(ops),'--published-root',str(pub),'--maintenance',str(ROOT/'tests/fixtures/soil/ops/maintenance/maintenance_valid.json')]).returncode==0
