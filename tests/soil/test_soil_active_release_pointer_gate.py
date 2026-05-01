from test_soil_active_release_pointer_builder import test_builder, run, ROOT

def test_gate(tmp_path):
 test_builder(tmp_path)
 s=ROOT/'tools/validators/soil/active_release_pointer_gate.py'
 args=[s,'--active-root',tmp_path/'a','--lineage-root',tmp_path,'--outcome-root',tmp_path,'--remediation-root',tmp_path,'--corrective-root',tmp_path,'--resolution-root',tmp_path,'--accountability-root',tmp_path,'--assurance-root',tmp_path,'--registry-root',tmp_path,'--certification-root',tmp_path,'--archive-root',tmp_path,'--preservation-root',tmp_path,'--reconciliation-root',tmp_path,'--federation-root',tmp_path,'--discovery-root',tmp_path,'--published-root',tmp_path,'--ops-root',tmp_path]
 assert run(args).returncode==0
