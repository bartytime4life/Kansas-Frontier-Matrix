import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def test_valid_observation(tmp_path):
 c=tmp_path/'c/continuity/soil'; c.mkdir(parents=True); (c/'current_public_delivery_continuity.json').write_text('{"active_continuity_id":"soil-continuity-test"}')
 p=subprocess.run([sys.executable,ROOT/'tools/stability/soil/record_steady_state_observation.py','--continuity-root',tmp_path/'c','--stability-root',tmp_path/'s','--observation',ROOT/'tests/fixtures/soil/stability/observations/steady_state_observation_valid.json'],capture_output=True,text=True)
 assert p.returncode==0
