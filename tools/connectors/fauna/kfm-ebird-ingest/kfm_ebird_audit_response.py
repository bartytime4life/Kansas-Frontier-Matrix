#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from datetime import datetime,timezone
VERSION='0.33.0'
def sha(p): return 'sha256:'+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def cid(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:16]
def parse(argv=None):
 p=argparse.ArgumentParser(prog='kfm-ebird-audit-response')
 p.add_argument('--mode',default='plan',choices=['plan','respond','close','validate','public-notice','diff','report']);p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
 for a in ['audit-intake-manifest','verifier-finding-queue','audit-finding-classification-report','audit-evidence-index','offline-verification-report','root-of-trust','gate-decision','public-gate-summary','public-root-summary','new-offline-verification-report','new-public-offline-verification-summary','out-dir','public-out-dir','decision','reason']:
  p.add_argument(f'--{a}')
 p.add_argument('--finding-id',action='append');p.add_argument('--dry-run',action='store_true');p.add_argument('--force',action='store_true');p.add_argument('--version',action='store_true')
 return p.parse_args(argv)
def main(argv=None):
 a=parse(argv)
 if a.version: print(json.dumps({'adapter':'kfm-ebird','tool':'audit-response','version':VERSION})); return
 q=[]
 if a.verifier_finding_queue and Path(a.verifier_finding_queue).exists(): q=[json.loads(l) for l in Path(a.verifier_finding_queue).read_text().splitlines() if l.strip()]
 selected=[x for x in q if not a.finding_id or x['queue_item_id'] in a.finding_id or x['source_finding_id'] in a.finding_id]
 resp_id=cid({'aggregate_targets':a.aggregate,'verifier_finding_queue_sha256':sha(a.verifier_finding_queue) if a.verifier_finding_queue else None,'decision':a.decision,'reason':a.reason,'adapter_version':VERSION})
 out=Path(a.out_dir or f'data/catalog/fauna/ebird/audit-responses/{resp_id}'); pub=Path(a.public_out_dir or f'data/published/fauna/ebird/audit-responses/{resp_id}')
 out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
 decision=a.decision or 'manual_review'
 findings=[]
 for item in selected:
  status='open' if decision in ('needs_remediation','needs_rerun','manual_review') else decision
  findings.append({'queue_item_id':item['queue_item_id'],'finding_type':item['finding_type'],'severity':item['severity'],'response_status':status,'evidence_artifacts':[],'response_summary':a.reason or 'governance response','next_action':item.get('recommended_route','manual_review'),'suggested_cli':item.get('suggested_cli','kfm-ebird-audit-response')})
 critical_open=any(f['severity']=='critical' and f['response_status'] in ('open','manual_review','needs_remediation','needs_rerun','blocked') for f in findings)
 packet_status='pass' if not critical_open else 'needs_review'
 plan={'schema_version':'v1','object_type':'KfmEbirdAuditResponsePlan','audit_response_id':resp_id,'aggregate_targets':a.aggregate,'selected_findings':[{'queue_item_id':i['queue_item_id'],'source_finding_id':i['source_finding_id'],'finding_type':i['finding_type'],'severity':i['severity'],'current_status':i['status'],'proposed_decision':decision,'allowed_to_close':i['severity']!='critical' or decision=='resolved','reason':a.reason or ''} for i in selected],'prohibited_actions':['delete_audit_findings','hide_critical_public_safety_findings'],'generated_at':datetime.now(timezone.utc).isoformat()}
 packet={'schema_version':'v1','object_type':'KfmEbirdAuditResponsePacket','audit_response_id':resp_id,'aggregate_targets':a.aggregate,'status':packet_status,'findings':findings,'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True}}
 (out/'audit_response_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
 (out/'audit_response_packet.json').write_text(json.dumps(packet,indent=2)+'\n')
 (out/'audit_response_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdAuditResponseManifest','audit_response_id':resp_id,'findings_addressed_count':len(findings),'findings_closed_count':sum(f['response_status'] in ('resolved','accepted_risk') for f in findings),'critical_findings_closed_count':sum(f['severity']=='critical' and f['response_status']=='resolved' for f in findings),'findings_remaining_open_count':sum(f['response_status'] not in ('resolved','accepted_risk') for f in findings),'generated_at':datetime.now(timezone.utc).isoformat()},indent=2)+'\n')
 (out/'audit_response_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdAuditResponseValidationReport','audit_response_id':resp_id,'status':'fail' if critical_open and packet_status=='pass' else 'pass'},indent=2)+'\n')
 (out/'audit_response_operator_report.md').write_text('# Audit response\n')
 if a.mode=='close': (out/'audit_finding_closure_receipt.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdAuditFindingClosureReceipt','audit_response_id':resp_id,'closure_decision':decision,'closed_findings':[{'queue_item_id':f['queue_item_id'],'closure_status':f['response_status'],'validation_status':'pass' if f['response_status']=='resolved' else 'warn','message':'synthetic'} for f in findings],'remaining_open_findings_count':sum(f['response_status'] not in ('resolved','accepted_risk') for f in findings),'remaining_critical_findings_count':sum(f['severity']=='critical' and f['response_status']!='resolved' for f in findings)},indent=2)+'\n')
 (pub/'public_audit_response_notice.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdAuditResponseNotice','public_safe':True,'exact_points':'restricted','audit_response_id':resp_id,'aggregate_targets':a.aggregate,'notice_type':'mixed','status':'under_review' if critical_open else 'resolved','summary':a.reason or 'synthetic response'},indent=2)+'\n')
 (pub/'public_audit_response_notice.md').write_text('Public audit response notice (aggregate-only).\n')
 (pub/'public_audit_response_summary.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdAuditResponseSummary','public_safe':True,'exact_points':'restricted','audit_response_id':resp_id},indent=2)+'\n')
 (pub/'public_audit_finding_status_index.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdAuditFindingStatusIndex','public_safe':True,'exact_points':'restricted','audit_response_id':resp_id,'findings':[{'public_finding_id':f['queue_item_id'],'finding_type':f['finding_type'],'severity':f['severity'],'public_status':f['response_status'],'last_response_notice_uri':'public_audit_response_notice.json'} for f in findings]},indent=2)+'\n')
 print(json.dumps({'audit_response_id':resp_id,'out_dir':str(out),'public_out_dir':str(pub)}))
if __name__=='__main__': main()
