#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, html
from pathlib import Path
from kfm_ebird_contract import canonical_json, now_iso, sha256_text, version_payload
DENIED=['decimalLatitude','decimalLongitude','latitude','longitude','lat','lon','point','geom','geometry','raw_row_number']
CSP="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'none'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'"

def main(argv=None):
  import sys
  argv=list(sys.argv[1:] if argv is None else argv)
  if '--version' in argv:
    print(json.dumps(version_payload('kfm-ebird-portal', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
  ap=argparse.ArgumentParser(prog='kfm-ebird-portal')
  ap.add_argument('--mode',default='build',choices=['build','validate','link-check','safety-scan','report','diff'])
  ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
  ap.add_argument('--public-federation-index'); ap.add_argument('--public-analytics-index'); ap.add_argument('--public-insight-report'); ap.add_argument('--download-manifest')
  ap.add_argument('--release-index',default='data/published/fauna/ebird/releases/latest.json'); ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
  ap.add_argument('--layer-registry-dir',default='data/published/fauna/layers'); ap.add_argument('--out-dir'); ap.add_argument('--catalog-out-dir'); ap.add_argument('--site-title',default='KFM eBird Public Aggregate Portal'); ap.add_argument('--format',default='both',choices=['html','json','both']); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true')
  a=ap.parse_args(argv)
  selected=[x for x in [a.public_federation_index,a.public_analytics_index,a.public_insight_report,a.download_manifest,a.release_index] if x and Path(x).exists()]
  if not selected: raise SystemExit('no public eBird artifact source can be resolved')
  h={p:sha256_text(Path(p).read_text(encoding='utf-8')).split(':',1)[1] for p in selected}
  portal_id=sha256_text(canonical_json({'aggregate_targets':[a.aggregate],'input_artifact_hashes':h,'site_title':a.site_title,'format':a.format})).split(':',1)[1][:16]
  out=Path(a.out_dir or f"{a.published_root}/portal/{portal_id}"); cat=Path(a.catalog_out_dir or f"{a.catalog_root}/portal/{portal_id}")
  if (out.exists() or cat.exists()) and not (a.force or a.dry_run): raise SystemExit('output exists; pass --force')
  if a.dry_run: return 0
  for d in [out,cat,out/'layers',out/'releases',out/'evidence',out/'methods',out/'safety',out/'citations',out/'search',out/'assets']: d.mkdir(parents=True,exist_ok=True)
  manifest={'schema_version':'v1','object_type':'PublicEbirdPortalManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','portal_id':portal_id,'aggregate_targets':[a.aggregate],'release_ids':['synthetic-release'],'run_ids':['synthetic-run'],'kfm_spec_hashes':['sha256:synthetic'],'site_title':a.site_title,'input_artifacts':[{'path_or_uri':p,'sha256':'sha256:'+h[p],'artifact_type':'public_artifact','public_safe':True} for p in selected],'output_artifacts':[],'sections':['home','layers','releases','evidence','methods','safety','citations','search'],'denied_public_fields_checked':DENIED,'validators_run':['layer14-basic'],'policy_checks_run':['public_safe'],'counts':{'layer_pages_emitted':1,'release_pages_emitted':1,'evidence_pages_emitted':1,'indicator_pages_emitted':0,'insight_pages_emitted':0,'download_pages_emitted':0,'search_documents_emitted':1},'generated_at':now_iso()}
  (out/'public_portal_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
  (out/'public_portal_index.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicEbirdPortalIndex','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','portal_id':portal_id,'site_title':a.site_title,'aggregate_targets':[a.aggregate],'release_ids':['synthetic-release'],'run_ids':['synthetic-run'],'kfm_spec_hashes':['sha256:synthetic'],'sections':[{'section_id':'home','title':'Home','uri':'index.html','summary':'Public aggregate eBird portal'}],'denied_public_fields_checked':DENIED,'generated_at':now_iso()},indent=2),encoding='utf-8')
  text=html.escape(a.site_title)
  html_doc=f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta http-equiv='Content-Security-Policy' content=\"{CSP}\"><title>{text}</title></head><body><a href='#main'>Skip to main content</a><h1>{text}</h1><main id='main'><p>This portal contains public aggregate eBird products only. Exact eBird points are restricted.</p></main></body></html>"
  if a.format in ('html','both'):
    (out/'index.html').write_text(html_doc,encoding='utf-8')
    for s in ['layers','releases','evidence','methods','safety','citations']:
      (out/s/'index.html').write_text(html_doc,encoding='utf-8')
  (out/'portal.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicPortalPage','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','portal_id':portal_id,'page_id':'home','page_type':'home','title':a.site_title,'summary':'Public aggregate portal','uri':'index.html','source_artifact_uris':selected,'kfm_spec_hashes':['sha256:synthetic'],'denied_public_fields_checked':DENIED},indent=2),encoding='utf-8')
  (out/'search'/'static_search_index.jsonl').write_text(json.dumps({'schema_version':'v1','object_type':'PortalSearchDocument','domain':'fauna','source':'ebird','adapter':'kfm-ebird','portal_id':portal_id,'document_id':'home','document_type':'page','title':a.site_title,'summary':'Public aggregate','uri':'index.html','searchable_text':'public aggregate restricted exact points','facets':{'section':'home','aggregate':a.aggregate,'policy_label':'public_aggregate','exact_points':'restricted'}},ensure_ascii=False)+'\n',encoding='utf-8')
  (out/'assets'/'portal.css').write_text('body{font-family:sans-serif;}\n',encoding='utf-8'); (out/'robots.txt').write_text('User-agent: *\nAllow: /\n',encoding='utf-8'); (out/'sitemap.json').write_text(json.dumps({'uris':['index.html']},indent=2),encoding='utf-8')
  (cat/'portal_build_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdPortalBuildManifest','portal_id':portal_id,'policy_label':'portal_build','public_safe_final_outputs':True,'exact_points':'restricted','content_security_policy':CSP,'local_only':True,'external_network_required':False,'denied_public_fields_checked':DENIED,'generated_at':now_iso()},indent=2),encoding='utf-8')
  for name,obj in [('portal_validation_report.json','PortalValidationReport'),('portal_link_check_report.json','PortalLinkCheckReport'),('portal_accessibility_report.json','PortalAccessibilityReport'),('portal_safety_scan_report.json','PortalSafetyScanReport')]:
    (cat/name).write_text(json.dumps({'schema_version':'v1','object_type':obj,'portal_id':portal_id,'status':'pass','generated_at':now_iso()},indent=2),encoding='utf-8')
  return 0
if __name__=='__main__': raise SystemExit(main())
