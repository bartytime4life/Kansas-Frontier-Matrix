#!/usr/bin/env python3
import argparse, hashlib, json, shutil, sys
from datetime import datetime, timezone
from pathlib import Path
import jsonschema

DENY_PATH_TOKENS = ("/raw/", "/work/", "/quarantine/")

def load_json(p: Path): return json.loads(p.read_text(encoding='utf-8'))
def dump_json(p: Path, d: dict): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(d, indent=2, sort_keys=True)+"\n", encoding='utf-8')
def sha256_file(p: Path):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()
def stable_id(prefix,*parts): return f"{prefix}-"+hashlib.sha256("|".join(parts).encode()).hexdigest()[:12]
def now_iso(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def validate(doc, schema): jsonschema.validate(instance=doc, schema=load_json(schema))

def is_fixture(evidence):
    return any(s.get('source_class')=='fixture' for s in evidence.get('sources',[]))

def contains_forbidden_ref(value: str):
    low=value.lower().replace('\\\\','/')
    return any(t in low for t in DENY_PATH_TOKENS) or '/data/processed/air/' in low

def evaluate(qa,evidence,promo,release,receipt,att,aqs,requested_status):
    denies=[]
    gates=promo.get('gates',{})
    if promo.get('decision')!='approved_for_catalog': denies.append('promotion_decision_not_approved_for_catalog')
    if release.get('public_readiness',{}).get('status') not in {'catalog_candidate','published'}: denies.append('release_manifest_not_catalog_candidate_or_better')
    for k in ('gate_a_nowcast_gt_35','gate_b_nowcast_vs_baseline_sigma_gt_2','gate_c_station_coverage_lt_75'):
        if gates.get(k,{}).get('triggered') and not att: denies.append('qa_gate_denied_without_override_attestation')
    if evidence.get('measurements',{}).get('nowcast_truth_status')!='operational_evidence_not_validated_aqs_truth': denies.append('nowcast_mislabelled_as_validated_truth')
    refs=[release.get('promotion_decision_ref',''),release.get('evidence_bundle_ref',''),release.get('run_receipt_ref','')] + release.get('catalog_refs',[]) + release.get('artifact_refs',[])
    if any(contains_forbidden_ref(r) for r in refs if isinstance(r,str)): denies.append('forbidden_raw_work_quarantine_or_processed_reference')
    fixture=is_fixture(evidence)
    if requested_status=='published':
        if not att: denies.append('missing_gate_d_attestation_for_published')
        else:
            if att.get('signature_type')=='fixture_signature': denies.append('fixture_attestation_cannot_authorize_real_publication')
        if fixture: denies.append('fixture_backed_artifacts_cannot_be_published_truth')
        if not aqs: denies.append('missing_aqs_reconciliation_for_published')
        else:
            st=aqs.get('status')
            if st in {'pending','conflict_detected'}: denies.append('aqs_reconciliation_not_ready')
            if st=='reconciled':
                ts=datetime.fromisoformat(aqs['reconciled_at'].replace('Z','+00:00'))
                if (datetime.now(timezone.utc)-ts).total_seconds()>72*3600: denies.append('aqs_reconciliation_older_than_72_hours')
    return denies

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--release-candidate-dir',required=True)
    ap.add_argument('--out-dir',required=True)
    ap.add_argument('--attestation')
    ap.add_argument('--aqs-reconciliation')
    ap.add_argument('--allow-fixture-publication-candidate',action='store_true')
    ap.add_argument('--write-tombstone')
    ap.add_argument('--dry-run',action='store_true')
    ap.add_argument('--requested-status',choices=['publication_candidate','published'],default='published')
    a=ap.parse_args()
    rc=Path(a.release_candidate_dir); out=Path(a.out_dir)
    qa=load_json(rc/'qa_summary.json'); evidence=load_json(rc/'evidence_bundle.json'); promo=load_json(rc/'promotion_decision.json'); release=load_json(rc/'release_manifest.json'); receipt=load_json(rc/'run_receipt.json')
    validate(qa,Path('schemas/contracts/v1/air/qa_summary.schema.json')); validate(evidence,Path('schemas/contracts/v1/air/evidence_bundle.schema.json')); validate(promo,Path('schemas/contracts/v1/air/promotion_decision.schema.json')); validate(release,Path('schemas/contracts/v1/air/release_manifest.schema.json'))
    att=load_json(Path(a.attestation)) if a.attestation else (load_json(rc/'attestation.json') if (rc/'attestation.json').exists() else None)
    aqs=load_json(Path(a.aqs_reconciliation)) if a.aqs_reconciliation else (load_json(rc/'aqs_reconciliation.json') if (rc/'aqs_reconciliation.json').exists() else None)
    if att: validate(att,Path('schemas/contracts/v1/air/attestation.schema.json'))
    if aqs: validate(aqs,Path('schemas/contracts/v1/air/aqs_reconciliation.schema.json'))
    status='published' if a.requested_status=='published' else 'publication_candidate'
    denies=evaluate(qa,evidence,promo,release,receipt,att,aqs,status)
    pub_id=stable_id('pub', release.get('release_id',''), promo.get('decision_id',''), evidence.get('bundle_id',''))
    manifest={"schema_version":"v1","publication_id":pub_id,"domain":"atmosphere.air","release_manifest_ref":str((rc/'release_manifest.json').as_posix()),"promotion_decision_ref":str((rc/'promotion_decision.json').as_posix()),"evidence_bundle_ref":str((rc/'evidence_bundle.json').as_posix()),"run_receipt_ref":str((rc/'run_receipt.json').as_posix()),"attestation_ref":str((rc/'attestation.json').as_posix()) if att else "","aqs_reconciliation_ref":str((rc/'aqs_reconciliation.json').as_posix()) if aqs else "","published_artifacts":[],"public_boundary_checks":{"no_raw_work_quarantine_refs":'forbidden_raw_work_quarantine_or_processed_reference' not in denies,"deny_reasons":denies},"published_at":now_iso(),"status":status}
    if denies:
        manifest['status']='published_fixture_blocked' if (is_fixture(evidence) and a.allow_fixture_publication_candidate) else 'published_fixture_blocked'
        out.mkdir(parents=True, exist_ok=True); dump_json(out/'publication_manifest.json',manifest)
        if a.write_tombstone:
            t={"schema_version":"v1","tombstone_id":stable_id('tomb',pub_id,now_iso()),"domain":"atmosphere.air","publication_manifest_ref":str((out/'publication_manifest.json').as_posix()),"reason":";".join(denies),"created_at":now_iso(),"created_by":"publish_air_release.py","replacement_ref":"","affected_artifacts":[]}
            dump_json(Path(a.write_tombstone),t)
        if a.dry_run or a.allow_fixture_publication_candidate: return 0
        return 1
    if a.dry_run: return 0
    if is_fixture(evidence):
        if not a.allow_fixture_publication_candidate: return 1
        manifest['status']='publication_candidate'
        target=out/'data/catalog/air/publication_candidate/example'; target.mkdir(parents=True,exist_ok=True)
    else:
        target=Path('data/published/air')/pub_id; target.mkdir(parents=True,exist_ok=True)
    for name in ['qa_summary.json','evidence_bundle.json','promotion_decision.json','release_manifest.json','run_receipt.json']:
        src=rc/name; dst=target/name; shutil.copy2(src,dst); manifest['published_artifacts'].append({"artifact_type":name.removesuffix('.json'),"path":dst.as_posix(),"sha256":sha256_file(dst),"source_ref":src.as_posix()})
    dump_json(target/'publication_manifest.json',manifest)
    return 0

if __name__=='__main__': raise SystemExit(main())
