import json, subprocess, sys
from pathlib import Path

def test_public_delivery_gate_blocks_on_mismatch(tmp_path):
    root=tmp_path
    (root/'routing/soil').mkdir(parents=True); (root/'routing/soil/current_public_routing.json').write_text(json.dumps({'active_routing_id':'r2'}))
    d=root/'delivery/soil/cycles/d1'; d.mkdir(parents=True)
    (root/'delivery/soil/current_public_delivery.json').write_text(json.dumps({'active_delivery_id':'d1','routing_id':'r1'}))
    (d/'public_delivery_manifest.json').write_text(json.dumps({'object_type':'SoilPublicDeliveryManifest','public_delivery_status':'PUBLIC_DELIVERY_VERIFIED'}))
    (d/'public_delivery_receipt.json').write_text(json.dumps({'receipt_type':'PublicDeliveryReceipt','from_state':'PUBLIC_ROUTING_RECONCILED','to_state':'PUBLIC_DELIVERY_VERIFIED','decision':'pass','signatures':{'x':1},'generated_artifacts':{}}))
    args=['--delivery-root',str(root),'--routing-root',str(root),'--active-root',str(root),'--lineage-root',str(root),'--outcome-root',str(root),'--remediation-root',str(root),'--corrective-root',str(root),'--resolution-root',str(root),'--accountability-root',str(root),'--assurance-root',str(root),'--registry-root',str(root),'--certification-root',str(root),'--archive-root',str(root),'--preservation-root',str(root),'--reconciliation-root',str(root),'--federation-root',str(root),'--discovery-root',str(root),'--published-root',str(root),'--ops-root',str(root)]
    p=subprocess.run([sys.executable,'tools/validators/soil/public_delivery_gate.py',*args],capture_output=True,text=True)
    assert p.returncode!=0
