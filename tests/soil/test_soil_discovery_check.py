from tests.soil.test_soil_discovery_builder import prep,run,DISC
from pathlib import Path
import json,sys
CHK=Path(__file__).resolve().parents[2]/'tools/validators/soil/discovery_check.py'

def test_check_ok(tmp_path):
 p,o,d=prep(tmp_path); assert run([DISC,'--published-root',p,'--ops-root',o,'--out-root',d,'--base-public-url','https://example.invalid/kfm/soil']).returncode==0
 assert run([CHK,'--discovery-root',d]).returncode==0
