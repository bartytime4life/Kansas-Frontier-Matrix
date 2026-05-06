from test_soil_federation_builder import prep,run,FED,ROOT
import json
W=ROOT/'tools/federation/soil/build_withdrawal.py'
def test_withdrawal(tmp_path):
 p,o,d,f=prep(tmp_path,retracted=True)
 # build federation should fail, then withdrawal on release id still allowed via retraction
 rid=json.loads((p/'published/soil/current.json').read_text())['current_release_id']
 assert run([W,'--federation-root',f,'--published-root',p,'--release-id',rid,'--out-root',f]).returncode==0
