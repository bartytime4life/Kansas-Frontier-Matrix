#!/usr/bin/env python
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from kfm.air_quality.airnow.reconcile.reconcile_batch import reconcile_from_manifest
from kfm.air_quality.airnow.reconcile.ids import make_id, sha256_text, canonical_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--created-at',required=True)
    a=ap.parse_args()
    try: m=json.loads(Path(a.manifest).read_text())
    except Exception: return 2
    out,errs=reconcile_from_manifest(m,a.created_at)
    if errs:
        rec={'object_type':'AirNowReconciliationReceipt','schema_version':'v1','receipt_id':make_id('kfm:air_quality:airnow:reconciliation_receipt:v1',[m.get('manifest_id'),'fail',errs,a.created_at]),'source_id':'airnow','manifest_id':m.get('manifest_id'),'reconciler':'airnow_layer4_reconciliation','reconciler_version':'v1','input_counts':{},'output_counts':{},'validation_outcome':'FAIL','finite_outcome':'DENY' if any(e in errs for e in ['NETWORK_FORBIDDEN','SECRET_FIELD_DENIED']) else 'ERROR','input_hashes':{},'output_hashes':{},'outputs':{},'warnings':[],'errors':errs,'created_at':a.created_at}
        print(json.dumps(rec,sort_keys=True)); return 1
    od=Path(a.out_dir); od.mkdir(parents=True,exist_ok=True)
    name_map={'site_index':'site_index.jsonl','site_parameter_index':'site_parameter_index.jsonl','reporting_area_index':'reporting_area_index.jsonl','zip_reporting_area_index':'zip_reporting_area_index.jsonl','relationship_edges':'relationship_edges.jsonl','conflicts':'conflicts.jsonl','quarantine':'quarantine.jsonl'}
    out_hashes={}
    for k,fn in name_map.items():
        body='\n'.join(canonical_json(r) for r in out[k])
        (od/fn).write_text((body+'\n') if body else '')
        out_hashes[f'{k}_hash']=sha256_text(body)
    rec={'object_type':'AirNowReconciliationReceipt','schema_version':'v1','source_id':'airnow','manifest_id':m['manifest_id'],'reconciler':'airnow_layer4_reconciliation','reconciler_version':'v1','input_counts':{k:len(json.loads((Path(m['inputs'][v]).read_text().replace('\n','\n') if Path(m['inputs'][v]).exists() else '[]'))) if False else 0 for k,v in []},'output_counts':{k:len(v) for k,v in out.items()},'validation_outcome':'PASS','finite_outcome':'ANSWER' if any(len(v)>0 for v in out.values()) else 'ABSTAIN','input_hashes':{'manifest_hash':sha256_text(canonical_json(m))},'output_hashes':out_hashes,'outputs':name_map,'warnings':[],'errors':[],'created_at':a.created_at}
    rec['receipt_id']=make_id('kfm:air_quality:airnow:reconciliation_receipt:v1',[m['manifest_id'],rec['output_counts'],out_hashes,a.created_at])
    (od/'reconciliation_receipt.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
    print(json.dumps(rec,sort_keys=True))
    return 0
if __name__=='__main__': raise SystemExit(main())
