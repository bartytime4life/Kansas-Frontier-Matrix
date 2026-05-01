import json, subprocess, sys

def test_unknown_exit_type_fails(tmp_path):
 inc=tmp_path/'inc'; (inc/'incident_response/soil/cycles/i1').mkdir(parents=True)
 (inc/'incident_response/soil/current_delivery_incident_response.json').write_text(json.dumps({'active_incident_response_id':'i1'}))
 (inc/'incident_response/soil/cycles/i1/incident_declaration_registry.json').write_text(json.dumps({'incidents':[]}))
 a=tmp_path/'a.json'; a.write_text(json.dumps({'incident_response_id':'i1','exit_type':'bad','steward_review':{'required':True,'decision':'approved'}}))
 p=subprocess.run([sys.executable,'tools/incident_closure/soil/record_safe_mode_exit_approval.py','--incident-root',str(inc),'--closure-root',str(tmp_path/'out'),'--approval',str(a)],capture_output=True,text=True)
 assert p.returncode!=0
