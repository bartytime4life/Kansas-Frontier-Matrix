#!/usr/bin/env python3
from __future__ import annotations
import argparse,datetime as dt,hashlib,json,os,re,shutil,tempfile
from pathlib import Path
A={"open","public","public_aggregate","public_safe","public_reviewed"}
S=lambda v:(re.sub(r"[^A-Za-z0-9._-]","_",v or "") or "bundle")
H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
L=lambda p:json.loads(Path(p).read_text())

def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('--catalog-root',required=True);p.add_argument('--out-root',required=True);p.add_argument('--release-id');a=p.parse_args(argv)
 try:
  root,out=Path(a.catalog_root),Path(a.out_root);receipts=sorted((root/'receipts/soil').glob('*.promotion_receipt.json'))
  if not receipts:raise ValueError('no promotion receipts')
  bundles=[];hs=[]
  for rp in receipts:
   r=L(rp);ga=r.get('generated_artifacts') or {}
   if r.get('receipt_type')!='PromotionReceipt' or r.get('from_state')!='PROCESSED' or r.get('decision')!='pass':raise ValueError('invalid promotion receipt')
   for k in ['stac','dcat','prov','triplets']:
    if k not in ga or not Path(ga[k]['path']).exists() or H(ga[k]['path'])!=ga[k].get('sha256'):raise ValueError('artifact hash/path check failed')
    hs.append(ga[k]['sha256'])
   st=L(ga['stac']['path']);dc=L(ga['dcat']['path']);pv=L(ga['prov']['path']);pr=st.get('properties',{})
   if pr.get('kfm:domain')!='soil' or pr.get('kfm:decision')!='pass' or pr.get('kfm:rights_status') not in A or pr.get('kfm:sensitivity')!='public' or not pr.get('kfm:evidence_bundle_ref') or not pr.get('kfm:policy_label'):raise ValueError('stac policy checks failed')
   if not dc.get('prov:wasGeneratedBy') or not any('Activity' in str((x or {}).get('@type','')) for x in pv.get('@graph',[])):raise ValueError('provenance invalid')
   bundles.append((r,st,pr,rp))
  rid=S(a.release_id) if a.release_id else 'soil-'+hashlib.sha256(''.join(sorted(hs)).encode()).hexdigest()[:16]
  rel=out/'published/soil/releases'/rid;tmp=Path(tempfile.mkdtemp(prefix='soilpub_'));work=tmp/rid;(work/'focus_cards').mkdir(parents=True);(work/'triplets').mkdir(parents=True)
  mb=[];recs=[]
  for r,st,pr,rp in sorted(bundles,key=lambda x:x[0]['bundle_id']):
   sid=S(r['bundle_id']);shutil.copy2(r['generated_artifacts']['triplets']['path'],work/'triplets'/f'{sid}.nt');m={k:pr.get(f'soil:{k}') for k in ['masked_pct','zscore_30d_max','station_grid_residual_max']}
   mb.append({'bundle_id':r['bundle_id'],'safe_bundle_id':sid,'evidence_bundle_ref':pr['kfm:evidence_bundle_ref'],'promotion_receipt_ref':str(rp),'stac_ref':f'catalog/stac/soil/{sid}.json','dcat_ref':f'catalog/dcat/soil/{sid}.jsonld','prov_ref':f'catalog/prov/soil/{sid}.jsonld','triplet_ref':f'triplets/{sid}.nt','rights_status':pr['kfm:rights_status'],'policy_label':pr['kfm:policy_label'],'sensitivity':pr['kfm:sensitivity'],'decision':'pass','metrics':m})
   recs.append({'bundle_id':r['bundle_id'],'source':pr.get('soil:source'),'aggregation':pr.get('soil:aggregation'),'time_window':{'start':pr.get('start_datetime'),'end':pr.get('end_datetime')},'bbox':st.get('bbox') or [-102.1,36.9,-94.6,40.1],'metrics':m,'evidence_bundle_ref':pr['kfm:evidence_bundle_ref'],'stac_ref':f'catalog/stac/soil/{sid}.json','dcat_ref':f'catalog/dcat/soil/{sid}.jsonld','prov_ref':f'catalog/prov/soil/{sid}.jsonld','triplet_ref':f'triplets/{sid}.nt','publication_status':'PUBLISHED','rights_status':pr['kfm:rights_status'],'policy_label':pr['kfm:policy_label'],'sensitivity':pr['kfm:sensitivity']})
  idx={'schema_version':'kfm.v1','object_type':'SoilPublicReadModel','release_id':rid,'domain':'soil','units':{'canonical_soil_moisture':'m3/m3','ui_percent_conversion':'multiply_by_100_for_display_only'},'records':sorted(recs,key=lambda x:x['bundle_id'])}
  man={'schema_version':'kfm.v1','object_type':'PublishedReleaseManifest','domain':'soil','release_id':rid,'state':'PUBLISHED','created':dt.datetime.now(dt.timezone.utc).isoformat(),'source_state':'CATALOG/TRIPLET','bundle_count':len(mb),'bundles':mb,'artifact_hashes':{},'policy_summary':{'rights_checked':True,'provenance_checked':True,'hash_integrity_checked':True,'public_access_allowed':True}}
  (work/'index.json').write_text(json.dumps(idx,sort_keys=True,indent=2)+'\n');(work/'manifest.json').write_text(json.dumps(man,sort_keys=True,indent=2)+'\n')
  for b in mb:(work/'focus_cards'/f"{b['safe_bundle_id']}.json").write_text(json.dumps({'schema_version':'kfm.v1','object_type':'FocusModeCard','mode':'public','status':'PUBLISHED','provisional':False,'domain':'soil','title':f"Soil Moisture {b['bundle_id']}",'summary':'Published soil moisture bundle','bundle_id':b['bundle_id'],'release_id':rid,'time_window':{},'metrics':b['metrics'],'evidence':{'evidence_bundle_ref':b['evidence_bundle_ref'],'promotion_receipt_ref':b['promotion_receipt_ref'],'publication_receipt_ref':'publication_receipt.json','stac_ref':b['stac_ref'],'dcat_ref':b['dcat_ref'],'prov_ref':b['prov_ref'],'triplet_ref':b['triplet_ref']},'caveats':['canonical units are m³/m³','UI percent displays multiply by 100','satellite/grid and station probes may differ'],'truth_policy':{'observational_data_bound':True,'ai_interpretive_only':True,'model_output_is_truth_source':False}},sort_keys=True,indent=2)+'\n')
  for f in sorted(work.rglob('*')):
   if f.is_file() and f.name!='publication_receipt.json':man['artifact_hashes'][str(f.relative_to(work))]=H(f)
  (work/'manifest.json').write_text(json.dumps(man,sort_keys=True,indent=2)+'\n')
  rec={'schema_version':'kfm.v1','receipt_type':'PublicationReceipt','from_state':'CATALOG/TRIPLET','to_state':'PUBLISHED','decision':'pass','release_id':rid,'created':dt.datetime.now(dt.timezone.utc).isoformat(),'source_promotion_receipts':[{'path':str(r),'sha256':H(r)} for r in receipts],'published_artifacts':{},'policy_checks':{'rights_checked':True,'provenance_checked':True,'hash_integrity_checked':True,'sensitivity_checked':True,'public_access_allowed':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
  for f in sorted(work.rglob('*')):
   if f.is_file():rec['published_artifacts'][str(f.relative_to(work))]=H(f)
  (work/'publication_receipt.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
  if not rel.exists():
   rel.parent.mkdir(parents=True,exist_ok=True);os.replace(work,rel)
  cur=out/'published/soil/current.json';cur.parent.mkdir(parents=True,exist_ok=True);cur.write_text(json.dumps({'schema_version':'kfm.v1','domain':'soil','current_release_id':rid,'release_ref':f'releases/{rid}'},sort_keys=True,indent=2)+'\n')
  print(json.dumps({'publication_allowed':True,'release_id':rid,'state_transition':'CATALOG/TRIPLET->PUBLISHED','published_root':str(out/'published/soil'),'bundles':[b['bundle_id'] for b in mb],'outputs':{'release':str(rel),'current':str(cur)}},sort_keys=True));return 0
 except Exception as e:
  print(json.dumps({'publication_allowed':False,'reasons':[str(e)],'state_transition':'CATALOG/TRIPLET->PUBLISHED'},sort_keys=True));return 1
if __name__=='__main__':raise SystemExit(main())
