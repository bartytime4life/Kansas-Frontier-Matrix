import json,subprocess,sys
from pathlib import Path

def test_outcome_check_smoke(tmp_path):
 root=tmp_path
 (root/'remediation/soil/cycles/r1').mkdir(parents=True)
 (root/'remediation/soil').mkdir(parents=True,exist_ok=True)
 (root/'remediation/soil/current_remediation_handoff.json').write_text(json.dumps({'active_remediation_id':'r1'}))
 m={'schema_version':'kfm.v1','object_type':'SoilRemediationHandoffManifest','domain':'soil','remediation_id':'r1','corrective_id':'c1','resolution_id':'z1','accountability_id':'a1','assurance_id':'as1','registry_id':'reg1','certification_id':'cert1','archive_package_id':'ar1','preservation_id':'p1','reconciliation_id':'rec1','federation_id':'f1','discovery_id':'d1','release_id':'rel1','remediation_handoff_status':'REMEDIATION_HANDOFF_READY','certificate_status':'active'}
 (root/'remediation/soil/cycles/r1/remediation_handoff_manifest.json').write_text(json.dumps(m))
 (root/'remediation/soil/cycles/r1/remediation_handoff_receipt.json').write_text(json.dumps({'decision':'pass'}))
 p=subprocess.run([sys.executable,'tools/remediation/soil/build_remediation_outcomes.py','--remediation-root',str(root),'--corrective-root',str(root),'--resolution-root',str(root),'--accountability-root',str(root),'--assurance-root',str(root),'--registry-root',str(root),'--certification-root',str(root),'--archive-root',str(root),'--preservation-root',str(root),'--reconciliation-root',str(root),'--federation-root',str(root),'--discovery-root',str(root),'--published-root',str(root),'--ops-root',str(root),'--outcome-root',str(root),'--base-public-url','https://example.invalid'],capture_output=True,text=True)
 assert p.returncode==0
 c=subprocess.run([sys.executable,'tools/validators/soil/remediation_outcome_check.py','--outcome-root',str(root)],capture_output=True,text=True)
 assert c.returncode==0
