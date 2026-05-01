from test_soil_federation_builder import prep,run,FED,ROOT
import json
CHK=ROOT/'tools/validators/soil/federation_check.py'
def test_check_ok(tmp_path):
 p,o,d,f=prep(tmp_path); assert run([FED,'--discovery-root',d,'--published-root',p,'--ops-root',o,'--out-root',f,'--base-public-url','https://example.invalid/kfm/soil']).returncode==0
 assert run([CHK,'--federation-root',f]).returncode==0
