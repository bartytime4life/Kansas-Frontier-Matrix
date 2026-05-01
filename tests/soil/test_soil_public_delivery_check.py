import json, subprocess, sys
from pathlib import Path

def test_public_delivery_check_smoke(tmp_path):
    root=tmp_path
    d=root/'delivery/soil/cycles/d1'; d.mkdir(parents=True)
    (root/'delivery/soil').mkdir(parents=True,exist_ok=True)
    (root/'delivery/soil/current_public_delivery.json').write_text(json.dumps({'active_delivery_id':'d1'}))
    m={'schema_version':'kfm.v1','object_type':'SoilPublicDeliveryManifest','public_delivery_status':'PUBLIC_DELIVERY_VERIFIED','routing_id':'r1'}
    r={'schema_version':'kfm.v1','receipt_type':'PublicDeliveryReceipt','from_state':'PUBLIC_ROUTING_RECONCILED','to_state':'PUBLIC_DELIVERY_VERIFIED','decision':'pass','signatures':{'x':1},'generated_artifacts':{}}
    (d/'public_delivery_manifest.json').write_text(json.dumps(m)); (d/'public_delivery_receipt.json').write_text(json.dumps(r))
    cmd=[sys.executable,'tools/validators/soil/public_delivery_check.py','--delivery-root',str(root)]
    p=subprocess.run(cmd,capture_output=True,text=True)
    assert p.returncode==0, p.stdout+p.stderr
