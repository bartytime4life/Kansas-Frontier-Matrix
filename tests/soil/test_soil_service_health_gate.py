from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
G=ROOT/'tools/validators/soil/service_health_gate.py'
def test_gate_fail(tmp_path):
 s=tmp_path/'s.json'; r=tmp_path/'r.json'
 s.write_text(json.dumps({'object_type':'SoilOperationalStatus','service_state':'unavailable','public_access_allowed':False,'latest_probe_decision':'fail','retracted':True,'active_incidents':[]}))
 r.write_text(json.dumps({'receipt_type':'OperationalStatusReceipt','policy_checks':{'public_access_allowed':False},'signatures':{}}))
 assert subprocess.run([sys.executable,str(G),'--status',str(s),'--status-receipt',str(r)]).returncode!=0
