from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file
p=argparse.ArgumentParser()
for a in ['publication-request','publication-approval','execution-plan','published-release-manifest','published-dataset-index','published-evidence-drawer-index','published-county-presence','published-map-descriptor','publication-receipt','publication-rollback-plan','promoted-package','promotion-audit-ledger']: p.add_argument(f'--{a}',type=Path,required=True)
p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);ns=p.parse_args()
items=[('001','publication_request',ns.publication_request),('002','publication_approval',ns.publication_approval),('003','publication_execution_plan',ns.execution_plan),('004','published_release_manifest',ns.published_release_manifest),('005','published_dataset_index',ns.published_dataset_index),('006','published_evidence_drawer_index',ns.published_evidence_drawer_index),('007','published_county_presence',ns.published_county_presence),('008','published_map_descriptor',ns.published_map_descriptor),('009','publication_receipt',ns.publication_receipt),('010','publication_rollback_plan',ns.publication_rollback_plan),('011','promoted_package',ns.promoted_package),('012','promotion_audit_ledger',ns.promotion_audit_ledger)]
entries=[{"entry_id":i,"entry_type":t,"ref":str(p),"sha256":sha256_file(p),"status":"recorded"} for i,t,p in items]
o={"schema_version":"1.0.0","object_type":"usda_plants_publication_audit_ledger","ledger_id":f"kfm.publication_audit_ledger.flora.usda_plants.{ns.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":ns.snapshot_date,"generated_at":ns.generated_at,"entries":entries,"publication_state":"published","status":"pass","reason_codes":["USDA_PLANTS_PUBLICATION_LEDGER_PASS"]}
o['ledger_hash']=canonical_hash(o,'ledger_hash');validate(ROOT/'schemas/flora/usda_plants_publication_audit_ledger.schema.json',o);write_json(ns.out,o)
