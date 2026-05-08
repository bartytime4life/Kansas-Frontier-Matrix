from tests.soil.test_soil_federation_builder import prep,run,FED,ROOT
M=ROOT/'tools/federation/soil/mock_submit.py'; ACC=ROOT/'tests/fixtures/soil/federation/registries/ckan_accept.json'; REJ=ROOT/'tests/fixtures/soil/federation/registries/ckan_reject.json'
def test_submit_accept(tmp_path):
 p,o,d,f=prep(tmp_path); assert run([FED,'--discovery-root',d,'--published-root',p,'--ops-root',o,'--out-root',f,'--base-public-url','https://example.invalid/kfm/soil']).returncode==0
 assert run([M,'--federation-root',f,'--target','ckan','--registry-fixture',ACC,'--out-root',tmp_path/'sub']).returncode==0

def test_submit_reject(tmp_path):
 p,o,d,f=prep(tmp_path); assert run([FED,'--discovery-root',d,'--published-root',p,'--ops-root',o,'--out-root',f,'--base-public-url','https://example.invalid/kfm/soil']).returncode==0
 assert run([M,'--federation-root',f,'--target','ckan','--registry-fixture',REJ,'--out-root',tmp_path/'sub']).returncode!=0
