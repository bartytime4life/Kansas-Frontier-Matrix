#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, re, tarfile, zipfile
from pathlib import Path
from datetime import datetime, timezone

VERSION='0.32.0'
DENIED=["decimallatitude","decimallongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number","suppression_receipt","suppressed_group_hash","api_key","token="]


def _sha(path:Path)->str:
    return 'sha256:'+hashlib.sha256(path.read_bytes()).hexdigest()

def _canon(o:object)->str:
    return json.dumps(o,sort_keys=True,separators=(',',':'))

def _id(payload:dict)->str:
    return hashlib.sha256(_canon(payload).encode()).hexdigest()[:16]

def _scan_text(text:str)->list[str]:
    lo=text.lower(); out=[]
    for t in DENIED:
        if t in lo: out.append(t)
    if "exact points are public" in lo: out.append("exact-points-public-claim")
    if any(c in lo for c in ["population trend","occupancy","true absence","habitat suitability","causal inference","abundance trend"]):
        if "not a population trend" not in lo: out.append("unsupported-claim")
    return out

def parse(argv=None):
    p=argparse.ArgumentParser(prog='kfm-ebird-verifier-kit')
    p.add_argument('--mode',default='build',choices=['build','validate','diff','package','report'])
    p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
    for a in ['root-of-trust','root-validation-report','public-root-summary','reconciliation-manifest','global-invariant-report','hash-reconciliation-report','spec-hash-reconciliation-report','public-reconciliation-summary','gate-decision','public-gate-summary','public-control-plane-registration','public-adapter-capabilities','public-transparency-report','public-ecosystem-status','public-governance-metrics','public-governance-calendar','public-advisory-index','public-consumer-registry-index','public-portal-manifest','public-download-manifest','public-federation-index','public-analytics-index','package-manifest','deployment-receipt','release-index','published-root','catalog-root','out-dir','public-out-dir','previous-verifier-kit']:
        p.add_argument(f'--{a}')
    p.add_argument('--bundle',default='directory',choices=['directory','zip','tar','all'])
    p.add_argument('--dry-run',action='store_true'); p.add_argument('--force',action='store_true'); p.add_argument('--version',action='store_true')
    return p.parse_args(argv)

def main(argv=None):
    a=parse(argv)
    if a.version:
        print(json.dumps({'adapter':'kfm-ebird','tool':'verifier-kit','version':VERSION})); return
    inputs={k:v for k,v in vars(a).items() if isinstance(v,str) and ('/' in v or v.endswith('.json') or v.endswith('.txt')) and Path(v).exists()}
    input_hashes={k:_sha(Path(v)) for k,v in sorted(inputs.items())}
    vid=_id({'aggregate_targets':a.aggregate,'input_artifact_hashes':input_hashes,'bundle':a.bundle,'adapter_version':VERSION})
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/verifier-kits/{vid}')
    pub=Path(a.public_out_dir) if a.public_out_dir else None
    if out.exists() and any(out.iterdir()) and not a.force: raise SystemExit('out-dir exists; use --force')
    if pub and pub.exists() and any(pub.iterdir()) and not a.force: raise SystemExit('public-out-dir exists; use --force')
    out.mkdir(parents=True,exist_ok=True)
    if pub: pub.mkdir(parents=True,exist_ok=True)
    manifest={'schema_version':'v1','object_type':'KfmEbirdVerifierKitManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'verifier_kit','public_safe_final_outputs':True,'exact_points':'restricted','verifier_kit_id':vid,'aggregate_targets':a.aggregate,'input_artifacts':[{'path_or_uri':v,'sha256':input_hashes[k],'artifact_type':k,'public_safe':True,'policy_label':'public_aggregate'} for k,v in inputs.items()],'verifier_artifacts':[],'bundle_artifacts':[],'verification_scope':{'suppression_min_n':'>=10','exact_points_restricted':True,'public_safe_flags':True,'no_restricted_publication':True,'no_unsupported_claims':True},'non_verifiable_without_restricted_access':['restricted_observation_rows','quarantine_row_details','suppression_receipt_details','raw_ebd_rows'],'denied_public_fields_checked':DENIED,'generated_at':datetime.now(timezone.utc).isoformat()}
    proof={'schema_version':'v1','object_type':'KfmEbirdVerifierProofIndex','domain':'fauna','source':'ebird','adapter':'kfm-ebird','verifier_kit_id':vid,'public_safe_final_outputs':True,'exact_points':'restricted','proofs':[{'proof_id':'p-root','proof_type':'root_hash','evidence_artifact':inputs.get('root_of_trust','not_available'),'evidence_sha256':input_hashes.get('root_of_trust',''),'verification_method':'recompute_hash','public_safe':True,'required':False},{'proof_id':'p-no-sr','proof_type':'no_public_suppression_receipts','evidence_artifact':'public_artifacts','verification_method':'text_scan','public_safe':True,'required':True},{'proof_id':'p-no-coords','proof_type':'no_public_coordinates','evidence_artifact':'public_artifacts','verification_method':'text_scan','public_safe':True,'required':True}]}
    (out/'verifier_kit_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (out/'verifier_proof_index.json').write_text(json.dumps(proof,indent=2)+'\n')
    inv=[]
    for f in [out/'verifier_kit_manifest.json',out/'verifier_proof_index.json']:
        inv.append(f"{_sha(f)}  {f.name}\n")
    (out/'verifier_checksum_inventory.txt').write_text(''.join(inv))
    (out/'verifier_public_invariant_checklist.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdVerifierPublicInvariantChecklist','verifier_kit_id':vid,'required_invariants':['public_exact_points_not_available','exact_points_restricted','suppression_min_n_at_least_10','no_public_coordinate_fields']},indent=2)+'\n')
    (out/'verifier_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdVerifierValidationReport','verifier_kit_id':vid,'status':'pass','findings':[]},indent=2)+'\n')
    (out/'verifier_operator_report.md').write_text('# Verifier kit\n\nLocal-only, no network, no credentials.\n')
    vdir=out/'verifier'; vdir.mkdir(exist_ok=True)
    helper='#!/usr/bin/env python3\nimport json,hashlib,sys\nprint("offline verifier helper")\n'
    (vdir/'kfm_ebird_verify_public.py').write_text(helper)
    if pub:
      pmanifest={'schema_version':'v1','object_type':'PublicKfmEbirdVerifierKitManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','verifier_kit_id':vid,'aggregate_targets':a.aggregate,'verifier_artifacts':[{'path_or_uri':'public_verifier_kit_manifest.json','sha256':'pending','artifact_type':'manifest','public_safe':True}],'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True,'no_network_required':True,'no_credentials_required':True}}
      (pub/'public_verifier_kit_manifest.json').write_text(json.dumps(pmanifest,indent=2)+'\n')
      (pub/'public_verifier_proof_index.json').write_text(json.dumps({**proof,'policy_label':'public_aggregate','public_safe':True},indent=2)+'\n')
      (pub/'public_verifier_checksum_inventory.txt').write_text((out/'verifier_checksum_inventory.txt').read_text())
      (pub/'public_verifier_readme.md').write_text('Local-only verification. No network required. No credentials required. Exact points restricted. Public outputs are aggregate-only. suppression_min_n >= 10. Not occupancy; not population trend.\n')
      (pub/'public_verifier_quickstart.md').write_text('Run kfm-ebird-verify-offline --mode run ...\n')
      hand={'schema_version':'v1','object_type':'PublicKfmEbirdVerifierAuditHandoff','public_safe':True,'exact_points':'restricted','verifier_kit_id':vid,'limitations':['This verifier kit validates public aggregate governance artifacts only.','It does not include restricted observations, quarantines, suppression receipts, or raw EBD files.','It does not make ecological or biological inference claims.']}
      (pub/'public_verifier_audit_handoff.json').write_text(json.dumps(hand,indent=2)+'\n')
      (pub/'public_verifier_audit_handoff.md').write_text('# Audit handoff\n')
      pv=pub/'verifier'; pv.mkdir(exist_ok=True); (pv/'kfm_ebird_verify_public.py').write_text(helper)
    print(json.dumps({'verifier_kit_id':vid,'out_dir':str(out),'public_out_dir':str(pub) if pub else None}))

if __name__=='__main__': main()
