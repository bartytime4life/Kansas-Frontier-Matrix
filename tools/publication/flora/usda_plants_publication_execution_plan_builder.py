from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--publication-request',type=Path,required=True);p.add_argument('--publication-approval',type=Path,required=True);p.add_argument('--promoted-package',type=Path,required=True);p.add_argument('--out-root',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 appr=json.loads(a.publication_approval.read_text());pkg=json.loads(a.promoted_package.read_text())
 if appr.get('decision')!='approved': raise SystemExit('USDA_PLANTS_PUBLICATION_PLAN_APPROVAL_NOT_APPROVED')
 if not pkg.get('sealed',False): raise SystemExit('USDA_PLANTS_PUBLICATION_PLAN_PROMOTED_PACKAGE_NOT_SEALED')
 root=f'published/flora/usda_plants/{a.snapshot_date}'
 roles=['published_release_manifest','published_dataset_index','published_evidence_drawer_index','published_county_presence','published_map_descriptor']
 targets=['release_manifest.json','dataset_index.json','evidence_drawer_index.json','county_presence.json','map_descriptor.json']
 plan=[{"role":r,"source_ref":f'promoted/flora/usda_plants/{a.snapshot_date}/promoted_package.json',"target_ref":f'{root}/{t}',"required":True} for r,t in zip(roles,targets)]
 o={"schema_version":"1.0.0","object_type":"usda_plants_publication_execution_plan","execution_plan_id":f"kfm.publication_execution_plan.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"publication_request_ref":str(a.publication_request),"publication_approval_ref":str(a.publication_approval),"promoted_package_ref":str(a.promoted_package),"target_root":root,"publish_plan":plan,"guards":{"requires_publication_approval":True,"requires_promoted_package":True,"writes_published_only":True,"allows_precise_coordinates":False,"allows_county_geometry":False,"allows_vector_tiles":False,"allows_raw_refs":False,"allows_work_refs":False,"allows_quarantine_refs":False},"status":"pass","reason_codes":["USDA_PLANTS_PUBLICATION_PLAN_PASS"]}
 o['plan_hash']=canonical_hash(o,'plan_hash');validate(ROOT/'schemas/flora/usda_plants_publication_execution_plan.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
