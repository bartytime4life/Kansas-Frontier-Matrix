from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser()
 for a in ['archive-source','archive-publication-request','archive-publication-approval','packaging-plan','pmtiles-package-manifest','static-host-handoff','cache-integrity-manifest','pmtiles-map-style','archive-publication-receipt','rollback-plan']:
  p.add_argument('--'+a,type=Path,required=True)
 p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);x=p.parse_args();s=x.snapshot_date
 refs=[('001','tile_archive_source',x.archive_source),('002','tile_archive_publication_request',x.archive_publication_request),('003','tile_archive_publication_approval',x.archive_publication_approval),('004','tile_archive_packaging_plan',x.packaging_plan),('005','pmtiles_package_manifest',x.pmtiles_package_manifest),('007','static_host_handoff',x.static_host_handoff),('008','cache_integrity_manifest',x.cache_integrity_manifest),('009','pmtiles_map_style',x.pmtiles_map_style),('010','tile_archive_publication_receipt',x.archive_publication_receipt),('011','tile_archive_rollback_plan',x.rollback_plan)]
 out_root=x.out.parents[5]
 entries=[{"entry_id":i,"entry_type":t,"ref":p.resolve().relative_to(out_root.resolve()).as_posix(),"sha256":sha256_file(p),"status":"recorded"} for i,t,p in refs]
 o={"schema_version":"1.0.0","object_type":"usda_plants_tile_archive_publication_audit_ledger","ledger_id":f"kfm.tile_archive_publication_audit_ledger.flora.usda_plants.{s}","domain":"flora","source_id":"usda_plants","snapshot_date":s,"generated_at":x.generated_at,"entries":entries,"publication_state":"published","deploys":False,"status":"pass","reason_codes":[]}
 o['ledger_hash']=canonical_hash(o,'ledger_hash');validate(ROOT/'schemas/flora/usda_plants_tile_archive_publication_audit_ledger.schema.json',o);write_json(x.out,o)
if __name__=='__main__':main()
