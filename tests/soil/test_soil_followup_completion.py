import json,subprocess,sys
from pathlib import Path

def test_followup_cli(tmp_path):
 r=tmp_path/'resilience/resilience/soil/cycles/r1'; r.mkdir(parents=True)
 (tmp_path/'resilience/resilience/soil/current_public_delivery_resilience.json').write_text(json.dumps({'active_resilience_id':'r1'}))
 (r/'public_delivery_resilience_manifest.json').write_text('{}'); (r/'public_delivery_resilience_receipt.json').write_text('{}')
 cp=subprocess.run([sys.executable,'tools/recommissioning/soil/record_followup_completion.py','--resilience-root',str(tmp_path/'resilience'),'--recommissioning-root',str(tmp_path/'recom'),'--completion','tests/fixtures/soil/recommissioning/followups/followup_completion_valid_reprobe.json'],capture_output=True,text=True)
 assert cp.returncode==0
