from tests.soil.test_soil_federation_builder import prep,run,FED,ROOT
G=ROOT/'tools/validators/soil/federation_gate.py'
def test_gate_ok(tmp_path):
 p,o,d,f=prep(tmp_path); assert run([FED,'--discovery-root',d,'--published-root',p,'--ops-root',o,'--out-root',f,'--base-public-url','https://example.invalid/kfm/soil']).returncode==0
 assert run([G,'--federation-root',f,'--discovery-root',d,'--published-root',p,'--ops-root',o]).returncode==0
