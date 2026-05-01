import json, subprocess, sys
from pathlib import Path

def test_missing_review_fails(tmp_path):
 inc=tmp_path/'inc'; (inc/'incident_response/soil/cycles/i1').mkdir(parents=True)
 (inc/'incident_response/soil').mkdir(parents=True,exist_ok=True)
 (inc/'incident_response/soil/current_delivery_incident_response.json').write_text(json.dumps({'active_incident_response_id':'i1'}))
 (inc/'incident_response/soil/cycles/i1/incident_declaration_registry.json').write_text(json.dumps({'incidents':[]}))
 c=tmp_path/'c.json'; c.write_text(json.dumps({'closure_type':'no_active_incident','root_cause_category':'none','severity':'low','public_message':'ok','steward_review':{'required':True,'decision':'rejected'}}))
 p=subprocess.run([sys.executable,'tools/incident_closure/soil/record_incident_closure.py','--incident-root',str(inc),'--closure-root',str(tmp_path/'out'),'--closure',str(c)],capture_output=True,text=True)
 assert p.returncode!=0
