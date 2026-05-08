from tests.soil.test_soil_discovery_builder import prep,run,DISC
from pathlib import Path
G=Path(__file__).resolve().parents[2]/'tools/validators/soil/discovery_gate.py'

def test_gate_ok(tmp_path):
 p,o,d=prep(tmp_path); assert run([DISC,'--published-root',p,'--ops-root',o,'--out-root',d,'--base-public-url','https://example.invalid/kfm/soil']).returncode==0
 assert run([G,'--discovery-root',d,'--published-root',p,'--ops-root',o]).returncode==0
