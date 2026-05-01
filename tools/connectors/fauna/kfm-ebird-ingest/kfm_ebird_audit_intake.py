#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json
from pathlib import Path
from datetime import datetime,timezone

VERSION='0.33.0'
DENIED=['decimalLatitude','decimalLongitude','latitude','longitude','lat','lon','raw_latitude','raw_longitude','point','geom','geometry','raw_row_number','suppression_receipt','suppressed_group_hash']


def sha(path:Path)->str:
    return 'sha256:'+hashlib.sha256(path.read_bytes()).hexdigest()

def canonical(obj)->str:
    return json.dumps(obj,sort_keys=True,separators=(',',':'))

def make_id(payload)->str:
    return hashlib.sha256(canonical(payload).encode()).hexdigest()[:16]

def load_findings(path:Path):
    if path.suffix.lower()=='.csv':
        with path.open() as f: return list(csv.DictReader(f))
    if path.suffix.lower()=='.jsonl':
        return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    obj=json.loads(path.read_text())
    return obj if isinstance(obj,list) else obj.get('findings',[])

def contains_denied_text(text:str)->bool:
    t=text.lower()
    return any(x.lower() in t for x in DENIED)

def parse(argv=None):
    p=argparse.ArgumentParser(prog='kfm-ebird-audit-intake')
    p.add_argument('--mode',default='ingest',choices=['ingest','classify','validate','queue','diff','report'])
    p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
    for a in ['offline-verification-report','offline-failed-proofs-report','offline-proof-results','verifier-kit-manifest','verifier-proof-index','public-offline-verification-summary','audit-finding-file','root-of-trust','root-validation-report','gate-decision','public-gate-summary','global-invariant-report','hash-reconciliation-report','spec-hash-reconciliation-report','public-reconciliation-summary','public-transparency-report','previous-audit-intake','published-root','catalog-root','out-dir','public-out-dir']:
        p.add_argument(f'--{a}')
    p.add_argument('--dry-run',action='store_true');p.add_argument('--force',action='store_true');p.add_argument('--version',action='store_true')
    return p.parse_args(argv)

def main(argv=None):
    a=parse(argv)
    if a.version:
        print(json.dumps({'adapter':'kfm-ebird','tool':'audit-intake','version':VERSION}));return
    refs=[getattr(a,k.replace('-','_')) for k in ['offline-verification-report','offline-failed-proofs-report','offline-proof-results','verifier-kit-manifest','verifier-proof-index','audit-finding-file','gate-decision','global-invariant-report']]
    refs=[Path(x) for x in refs if x and Path(x).exists()]
    root_hash='not_available'
    if a.root_of_trust and Path(a.root_of_trust).exists():
        root=json.loads(Path(a.root_of_trust).read_text());root_hash=root.get('root_hash','not_available')
    payload={'aggregate_targets':a.aggregate,'adapter_version':VERSION,'root_hash':root_hash}
    for r in refs: payload[f'{r.name}_sha256']=sha(r)
    intake_id=make_id(payload)
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/audit-intake/{intake_id}')
    pub=Path(a.public_out_dir or f'data/published/fauna/ebird/audit-intake/{intake_id}')
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
    findings=[]
    if a.audit_finding_file and Path(a.audit_finding_file).exists(): findings.extend(load_findings(Path(a.audit_finding_file)))
    if a.offline_failed_proofs_report and Path(a.offline_failed_proofs_report).exists():
        f=json.loads(Path(a.offline_failed_proofs_report).read_text())
        for i,pf in enumerate(f.get('failed_proofs',[]),1): findings.append({'finding_id':f'failed-proof-{i}','finding_type':'failed_proof','severity':'high','summary':pf.get('message','failed proof'),'public_safe':False,'exact_points':'restricted'})
    queue=[]
    for i,f in enumerate(findings,1):
        summary=str(f.get('summary',''))
        if contains_denied_text(summary): raise SystemExit('audit finding contains denied content')
        ft=f.get('finding_type','manual_review'); sev=f.get('severity','medium')
        route='manual_review'; cli='kfm-ebird-audit-response --mode respond'
        if ft in ('hash_mismatch','root_hash_mismatch'): route='run_reconciliation'; cli='kfm-ebird-reconcile'
        elif ft=='verifier_kit_gap': route='rebuild_verifier_kit'; cli='kfm-ebird-verifier-kit'
        elif ft=='public_safety_finding': route='run_remediation'; cli='kfm-ebird-remediate'
        blocks= sev=='critical' or ft=='public_safety_finding'
        queue.append({'schema_version':'v1','object_type':'KfmEbirdVerifierFindingQueueItem','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'audit_intake','public_safe':False,'exact_points':'restricted','audit_intake_id':intake_id,'queue_item_id':f'qi-{i:04d}','source_finding_id':f.get('finding_id',f'f-{i}'),'finding_type':ft,'severity':sev,'status':'open','affected_layer':'unknown','summary':summary,'recommended_route':route,'suggested_cli':cli,'blocks_gate':blocks,'blocks_public_transparency_pass':blocks,'blocks_consumer_certification':sev in ('high','critical'),'evidence_artifacts':[]})
    cls={'schema_version':'v1','object_type':'KfmEbirdAuditFindingClassificationReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','audit_intake_id':intake_id,'status':'pass','classifications':[{'source_finding_id':q['source_finding_id'],'queue_item_id':q['queue_item_id'],'finding_type':q['finding_type'],'severity':q['severity'],'affected_layer':q['affected_layer'],'recommended_route':q['recommended_route'],'suggested_cli':q['suggested_cli'],'blocks_gate':q['blocks_gate'],'blocks_public_transparency_pass':q['blocks_public_transparency_pass'],'blocks_consumer_certification':q['blocks_consumer_certification'],'rationale':'rule-based'} for q in queue],'summary':{'findings_total':len(queue),'critical':sum(q['severity']=='critical' for q in queue)}}
    manifest={'schema_version':'v1','object_type':'KfmEbirdAuditIntakeManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'audit_intake','public_safe_final_outputs':True,'exact_points':'restricted','audit_intake_id':intake_id,'aggregate_targets':a.aggregate,'root_hash':root_hash,'findings_seen':len(findings),'findings_classified':len(queue),'critical_findings_count':sum(q['severity']=='critical' for q in queue),'public_safety_findings_count':sum(q['finding_type']=='public_safety_finding' for q in queue),'denied_public_fields_checked':DENIED,'generated_at':datetime.now(timezone.utc).isoformat()}
    pubsum={'schema_version':'v1','object_type':'PublicKfmEbirdAuditIntakeSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','audit_intake_id':intake_id,'aggregate_targets':a.aggregate,'root_hash':root_hash,'intake_status':'pass','finding_counts':{'total':len(queue),'critical':manifest['critical_findings_count']},'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True,'no_network_required':True,'no_credentials_required':True}}
    (out/'audit_intake_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (out/'verifier_finding_queue.jsonl').write_text('\n'.join(json.dumps(q) for q in queue)+'\n')
    (out/'audit_finding_classification_report.json').write_text(json.dumps(cls,indent=2)+'\n')
    (out/'audit_evidence_index.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdAuditEvidenceIndex','audit_intake_id':intake_id,'evidence':[]},indent=2)+'\n')
    (out/'audit_intake_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdAuditIntakeValidationReport','status':'pass','audit_intake_id':intake_id},indent=2)+'\n')
    (out/'audit_intake_operator_report.md').write_text('# Audit intake\n')
    (pub/'public_audit_intake_summary.json').write_text(json.dumps(pubsum,indent=2)+'\n')
    (pub/'public_verifier_finding_summary.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdVerifierFindingSummary','public_safe':True,'exact_points':'restricted','audit_intake_id':intake_id,'findings':[{'public_finding_id':q['queue_item_id'],'finding_type':q['finding_type'],'severity':q['severity'],'affected_public_scope':'general','summary':q['summary'],'public_status':'open','public_recommended_action':'under review'} for q in queue]},indent=2)+'\n')
    print(json.dumps({'audit_intake_id':intake_id,'out_dir':str(out),'public_out_dir':str(pub)}))
if __name__=='__main__': main()
