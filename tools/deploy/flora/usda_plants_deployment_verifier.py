from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,sha256_file,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--site-bundle-manifest',type=Path,required=True);p.add_argument('--mode',default='local_artifact');p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();m=json.loads(a.site_bundle_manifest.read_text())
 checks=[];ok=True
 site=Path(m['site_root'])
 for f in m['files']:
  exists=(site/f['path']).exists();checks.append({'check':f"exists:{f['path']}",'pass':exists});ok=ok and exists
 o={'schema_version':'1.0.0','object_type':'usda_plants_deployment_verification_report','domain':'flora','source_id':'usda_plants','snapshot_date':m['snapshot_date'],'generated_at':a.generated_at,'report_id':f"kfm.deploy.verify.flora.usda_plants.{m['snapshot_date']}",'mode':a.mode,'site_bundle_manifest_ref':str(a.site_bundle_manifest),'checks':checks,'status':'pass' if ok and a.mode=='local_artifact' else 'fail','reason_codes':['USDA_PLANTS_DEPLOYMENT_VERIFICATION_PASS' if ok else 'USDA_PLANTS_DEPLOYMENT_VERIFICATION_FAIL']}
 o['report_hash']=canonical_hash(o,'report_hash');validate(ROOT/'schemas/flora/usda_plants_deployment_verification_report.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
