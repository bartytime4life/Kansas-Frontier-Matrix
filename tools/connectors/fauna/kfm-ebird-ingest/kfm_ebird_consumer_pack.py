#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, now_iso, sha256_text, version_payload
REQ_ROUTES=['/api/fauna/ebird/health','/api/fauna/ebird/capabilities','/api/fauna/ebird/registration','/api/fauna/ebird/gate','/api/fauna/ebird/root','/api/fauna/ebird/layers']

def load(p:str|None)->dict[str,Any]:
    if not p: return {}
    q=Path(p)
    return json.loads(q.read_text(encoding='utf-8')) if q.exists() else {}

def parse(argv:list[str]):
    ap=argparse.ArgumentParser(prog='kfm-ebird-consumer-pack')
    ap.add_argument('--mode',choices=['build','validate','test','diff','report'],default='build'); ap.add_argument('--aggregate',choices=['huc12','county','both'],default='both')
    for n in ['public-control-plane-registration','public-adapter-capabilities','mock-control-plane-manifest','mock-route-catalog','public-gate-summary','public-root-summary','public-reconciliation-summary','release-index','public-federation-index','public-analytics-index','public-portal-manifest','public-download-manifest','package-manifest','public-out-dir','previous-consumer-pack']:
        ap.add_argument(f'--{n}')
    ap.add_argument('--out-dir',default='data/catalog/fauna/ebird/consumer-packs'); ap.add_argument('--language',choices=['typescript','python','json-schema','all'],default='json-schema')
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
    return ap.parse_args(argv)

def main(argv:list[str]|None=None)->int:
    import sys
    a=parse(sys.argv[1:] if argv is None else argv)
    if a.version: print(json.dumps(version_payload('kfm-ebird-consumer-pack', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    payload={k:load(getattr(a,k)) for k in ['public_control_plane_registration','public_adapter_capabilities','mock_control_plane_manifest','mock_route_catalog','public_gate_summary','public_root_summary','public_reconciliation_summary','release_index','public_federation_index','public_analytics_index','public_portal_manifest','public_download_manifest','package_manifest'] if getattr(a,k)}
    ih={k:sha256_text(canonical_json(v)).split(':',1)[1] for k,v in payload.items()}
    cid=sha256_text(canonical_json({'aggregate_targets':[a.aggregate],'input_artifact_hashes':ih,'language':a.language,'adapter_version':ADAPTER_VERSION})).split(':',1)[1][:16]
    out=Path(a.out_dir)/cid
    if a.dry_run: print(json.dumps({'object_type':'KfmEbirdConsumerPackPlan','consumer_pack_id':cid,'out_dir':str(out)},indent=2)); return 0
    if out.exists() and not a.force: raise SystemExit('output exists; pass --force')
    out.mkdir(parents=True,exist_ok=True)
    manifest={'schema_version':'v1','object_type':'KfmEbirdConsumerContractManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'consumer_contract','public_safe_final_outputs':True,'exact_points':'restricted','consumer_pack_id':cid,'aggregate_targets':[a.aggregate],'language':a.language,'input_artifacts':[{'path_or_uri':k,'sha256':'sha256:'+v,'artifact_type':'input','public_safe':True,'policy_label':'public_aggregate'} for k,v in ih.items()],'supported_routes':REQ_ROUTES,'supported_dtos':['PublicAggregateFeature','FeatureEvidenceDrawer'],'generated_at':now_iso()}
    (out/'consumer_contract_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (out/'consumer_route_descriptor.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdConsumerRouteDescriptor','domain':'fauna','source':'ebird','adapter':'kfm-ebird','consumer_pack_id':cid,'public_safe':True,'exact_points':'restricted','routes':[{'route_id':r.split('/')[-1] or 'root','method':'GET','route_template':r,'public_safe':True,'denied_fields':['decimalLatitude','geometry']} for r in REQ_ROUTES]},indent=2)+'\n')
    (out/'consumer_openapi_lite.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdOpenApiLite','domain':'fauna','source':'ebird','adapter':'kfm-ebird','consumer_pack_id':cid,'title':'KFM eBird Public Aggregate','version':'v1','public_safe':True,'exact_points':'restricted','paths':{r:{'get':{'operationId':r.split('/')[-1] or 'root'}} for r in REQ_ROUTES},'components':{},'security':{'network_required':False,'credentials_required':False,'public_exact_points_available':False,'restricted_observations_available':False,'suppression_receipts_available':False}},indent=2)+'\n')
    print(str(out)); return 0
if __name__=='__main__': raise SystemExit(main())
