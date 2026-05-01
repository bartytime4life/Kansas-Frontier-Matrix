#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, now_iso, sha256_text, version_payload
DENIED=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number","suppression_receipt","suppressed_group_hash"]

def load(p:str|None)->dict[str,Any]:
    if not p: return {}
    q=Path(p)
    return json.loads(q.read_text(encoding='utf-8')) if q.exists() else {}

def parse(argv:list[str]):
    ap=argparse.ArgumentParser(prog='kfm-ebird-mock-control-plane')
    ap.add_argument('--mode',choices=['build','validate','diff','report'],default='build')
    ap.add_argument('--aggregate',choices=['huc12','county','both'],default='both')
    for n in ['control-plane-registration','public-control-plane-registration','adapter-capabilities','public-adapter-capabilities','adapter-health-status','public-gate-summary','public-root-summary','public-reconciliation-summary','release-index','public-federation-index','public-analytics-index','public-portal-manifest','public-download-manifest','package-manifest','environment-latest','previous-mock-manifest','public-out-dir']:
        ap.add_argument(f'--{n}')
    ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird'); ap.add_argument('--layer-registry-dir',default='data/published/fauna/layers')
    ap.add_argument('--out-dir',default='data/catalog/fauna/ebird/mock-control-plane')
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
    return ap.parse_args(argv)

def main(argv:list[str]|None=None)->int:
    import sys
    a=parse(sys.argv[1:] if argv is None else argv)
    if a.version:
        print(json.dumps(version_payload('kfm-ebird-mock-control-plane', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    inputs={k:getattr(a,k.replace('-','_')) for k in ['public_control_plane_registration','public_adapter_capabilities','public_gate_summary','public_root_summary','public_reconciliation_summary','release_index','public_federation_index','public_analytics_index','public_portal_manifest','public_download_manifest','package_manifest','environment_latest']}
    payload={k:load(v) for k,v in inputs.items() if v}
    input_hashes={k:sha256_text(canonical_json(v)).split(':',1)[1] for k,v in payload.items()}
    mock_id=sha256_text(canonical_json({'aggregate_targets':[a.aggregate],'input_artifact_hashes':input_hashes,'adapter_version':ADAPTER_VERSION})).split(':',1)[1][:16]
    out=Path(a.out_dir)/mock_id
    if a.dry_run:
        print(json.dumps({'schema_version':'v1','object_type':'KfmEbirdMockControlPlanePlan','mock_id':mock_id,'out_dir':str(out),'mode':a.mode},indent=2)); return 0
    if out.exists() and not a.force: raise SystemExit('output exists; pass --force')
    (out/'responses/layers').mkdir(parents=True,exist_ok=True)
    base={'schema_version':'v1','domain':'fauna','source':'ebird','adapter':'kfm-ebird','mock_id':mock_id,'public_safe':True,'exact_points':'restricted'}
    resp={'health':{'object_type':'KfmEbirdAdapterHealthStatus','status':'ok','public_safe':True,'exact_points':'restricted'},'capabilities':payload.get('public_adapter_capabilities',{'object_type':'PublicKfmEbirdAdapterCapabilities','unsupported_capabilities':['public_exact_points']}),'registration':payload.get('public_control_plane_registration',{'object_type':'PublicKfmEbirdControlPlaneRegistration'}),'gate-summary':payload.get('public_gate_summary',{'object_type':'PublicEbirdGateSummary'}),'root-summary':payload.get('public_root_summary',{'object_type':'PublicEbirdRootOfTrustSummary'}),'reconciliation-summary':payload.get('public_reconciliation_summary',{'object_type':'PublicEbirdReconciliationSummary'}),'layers/index':{'object_type':'LayerIndex','layers':['ebird_agg_huc12','ebird_agg_county'],'public_safe':True,'exact_points':'restricted'}}
    for rid,obj in resp.items():
        p=out/f"responses/{rid}.json"; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps({**base,**obj},indent=2)+'\n',encoding='utf-8')
    (out/'responses/layers/ebird_agg_huc12.json').write_text(json.dumps({**base,'object_type':'LayerApiDescriptor','layer_id':'ebird_agg_huc12','public_safe':True,'exact_points':'restricted'},indent=2)+'\n')
    (out/'responses/layers/ebird_agg_county.json').write_text(json.dumps({**base,'object_type':'LayerApiDescriptor','layer_id':'ebird_agg_county','public_safe':True,'exact_points':'restricted'},indent=2)+'\n')
    manifest={**base,'schema_version':'v1','object_type':'KfmEbirdMockControlPlaneManifest','policy_label':'mock_control_plane','public_safe_final_outputs':True,'aggregate_targets':[a.aggregate],'input_artifacts':[{'path_or_uri':k,'sha256':'sha256:'+v,'artifact_type':'input','public_safe':True,'policy_label':'public_aggregate'} for k,v in input_hashes.items()],'denied_public_fields_checked':DENIED,'validators_run':['validate_ebird_mock_control_plane'],'public_safety_checks_run':['scanner_v1']}
    (out/'mock_control_plane_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(str(out)); return 0
if __name__=='__main__': raise SystemExit(main())
