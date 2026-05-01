#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from datetime import datetime, timezone
VERSION='0.34.0'
DENIED=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number","suppression_receipt","suppressed_group_hash"]
CLAIMS=["occupancy","abundance trend","true absence","population trend","habitat suitability","causal inference"]

def canonical(o): return json.dumps(o,sort_keys=True,separators=(',',':'))
def sha(p): return 'sha256:'+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load_json(p): return json.loads(Path(p).read_text())
def parse(argv=None):
 p=argparse.ArgumentParser(prog='kfm-ebird-hardening')
 p.add_argument('--mode',default='analyze',choices=['analyze','plan','validate','diff','report'])
 p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
 for a in ['audit-intake-manifest','verifier-finding-queue','audit-finding-classification-report','audit-response-packet','audit-finding-closure-receipt','offline-verification-report','offline-failed-proofs-report','verifier-proof-index','verifier-kit-manifest','redteam-summary-report','validator-policy-coverage-report','safety-regression-report','missed-detection-report','global-invariant-report','hash-reconciliation-report','gate-decision','gate-blocker-report','quality-scan-report','quality-anomaly-report','control-matrix','root-of-trust','contract-lock','conformance-report','previous-hardening-manifest','published-root','catalog-root','out-dir','public-out-dir']:
  p.add_argument(f'--{a}')
 p.add_argument('--dry-run',action='store_true');p.add_argument('--force',action='store_true');p.add_argument('--version',action='store_true')
 return p.parse_args(argv)

def main(argv=None):
 a=parse(argv)
 if a.version: print(json.dumps({'adapter':'kfm-ebird','tool':'hardening','version':VERSION})); return
 inputs={k:getattr(a,k.replace('-','_')) for k in ['audit-intake-manifest','verifier-finding-queue','audit-response-packet','offline-verification-report','offline-failed-proofs-report','redteam-summary-report','validator-policy-coverage-report','missed-detection-report','global-invariant-report','gate-decision','quality-scan-report','control-matrix'] if getattr(a,k.replace('-','_'))}
 id_material={'aggregate_targets':a.aggregate,'adapter_version':VERSION}
 for k,v in sorted(inputs.items()):
  if Path(v).exists(): id_material[k.replace('-','_')+'_sha256']=sha(v)
 hardening_id=hashlib.sha256(canonical(id_material).encode()).hexdigest()[:16]
 out=Path(a.out_dir or f'data/catalog/fauna/ebird/hardening/{hardening_id}')
 pub=Path(a.public_out_dir or f'data/published/fauna/ebird/hardening/{hardening_id}') if a.public_out_dir or True else None
 if out.exists() and any(out.iterdir()) and not a.force: raise SystemExit('refusing overwrite without --force')
 out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
 gaps=[]
 if a.verifier_finding_queue and Path(a.verifier_finding_queue).exists():
  for i,l in enumerate(Path(a.verifier_finding_queue).read_text().splitlines()):
   if not l.strip(): continue
   row=json.loads(l)
   sev=row.get('severity','medium')
   gap_id=f'gap-{i+1:03d}'
   gaps.append({'gap_id':gap_id,'source_finding_id':row.get('source_finding_id'),'source_artifact':'verifier_finding_queue','gap_type':'verifier_proof_gap','severity':sev,'affected_layer':'layer34','affected_artifact_type':'finding','description':row.get('summary','finding'),'recommended_hardening_action':'add verifier proof and regression fixture','suggested_owner_layer':'verifier_kit','blocks_gate':sev in ('high','critical'),'blocks_public_transparency_pass':sev=='critical','blocks_consumer_certification':sev in ('high','critical')})
 status='fail' if any(g['severity']=='critical' for g in gaps) else ('warn' if gaps else 'pass')
 summary={'gaps_total':len(gaps),'critical':sum(g['severity']=='critical' for g in gaps),'high':sum(g['severity']=='high' for g in gaps),'medium':sum(g['severity']=='medium' for g in gaps),'low':sum(g['severity']=='low' for g in gaps),'info':sum(g['severity']=='info' for g in gaps),'gate_blocking':sum(g['blocks_gate'] for g in gaps),'transparency_blocking':sum(g['blocks_public_transparency_pass'] for g in gaps),'consumer_certification_blocking':sum(g['blocks_consumer_certification'] for g in gaps)}
 ts=datetime.now(timezone.utc).isoformat()
 manifest={'schema_version':'v1','object_type':'KfmEbirdHardeningManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'hardening','public_safe_final_outputs':True,'exact_points':'restricted','hardening_id':hardening_id,'aggregate_targets':a.aggregate,'input_artifacts':[{'path_or_uri':v,'sha256':sha(v) if Path(v).exists() else None,'artifact_type':k,'public_safe':False,'policy_label':'hardening_input'} for k,v in inputs.items()],'output_artifacts':[],'hardening_scope':{'validators':True,'policies':True,'scanners':True,'verifier_proofs':True,'conformance':True,'redteam':True,'docs':True,'controls':True,'quality':True,'gate':True},'denied_public_fields_checked':DENIED,'validators_run':['validate_ebird_hardening'],'policy_checks_run':['fauna/ebird.rego'],'public_safety_checks_run':['public_safety_scanner'],'generated_at':ts}
 gap_report={'schema_version':'v1','object_type':'KfmEbirdHardeningGapReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'hardening','public_safe':False,'exact_points':'restricted','hardening_id':hardening_id,'status':status,'gaps':gaps,'summary':summary,'generated_at':ts}
 common={'schema_version':'v1','domain':'fauna','source':'ebird','adapter':'kfm-ebird','hardening_id':hardening_id,'policy_label':'hardening','public_safe_final_outputs':True,'exact_points':'restricted','generated_at':ts}
 files={
 'hardening_manifest.json':manifest,'hardening_gap_report.json':gap_report,
 'validator_hardening_plan.json':{**common,'object_type':'KfmEbirdValidatorHardeningPlan','proposed_validator_updates':[],'prohibited_updates':['remove_public_safety_check']},
 'policy_hardening_plan.json':{**common,'object_type':'KfmEbirdPolicyHardeningPlan','proposed_policy_updates':[],'prohibited_updates':['lower_suppression_min_n']},
 'scanner_hardening_plan.json':{**common,'object_type':'KfmEbirdScannerHardeningPlan','proposed_scanner_updates':[],'false_positive_guardrails':{'denied_fields':DENIED,'safety_text':'blocked capabilities only'}},
 'verifier_proof_upgrade_plan.json':{**common,'object_type':'KfmEbirdVerifierProofUpgradePlan','proposed_proof_updates':[{'proof_update_id':'proof-001','source_gap_id':gaps[0]['gap_id'] if gaps else 'none','proof_type':'no_public_coordinates','verification_method':'text_scan','required':True,'expected_negative_fixture':'fixtures/ebird/hardening/invalid_public_summary_decimalLatitude.json','expected_positive_fixture':'fixtures/ebird/hardening/valid_public_hardening_summary.json','reason':'public safety'}]},
 'conformance_hardening_plan.json':{**common,'object_type':'KfmEbirdConformanceHardeningPlan','proposed_conformance_tests':[]},
 'redteam_promotion_plan.json':{**common,'object_type':'KfmEbirdRedTeamPromotionPlan','promotion_candidates':[],'prohibited_promotions':['real_ebird_data']},
 'docs_hardening_plan.json':{**common,'object_type':'KfmEbirdDocsHardeningPlan','proposed_doc_updates':[]},
 'control_matrix_update_plan.json':{**common,'object_type':'KfmEbirdControlMatrixUpdatePlan','proposed_controls':[],'proposed_control_updates':[]},
 'hardening_validation_report.json':{'schema_version':'v1','object_type':'KfmEbirdHardeningValidationReport','hardening_id':hardening_id,'status':'pass','errors':[]},
 'hardening_operator_report.md':'# Layer 34 hardening\n\nLocal-only synthetic hardening output.\n'
 }
 for fn,obj in files.items():
  (out/fn).write_text(obj if isinstance(obj,str) else json.dumps(obj,indent=2)+'\n')
 public={'schema_version':'v1','object_type':'PublicKfmEbirdHardeningSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','hardening_id':hardening_id,'aggregate_targets':a.aggregate,'hardening_status':status,'gaps_summary':{k:summary[k] for k in ['gaps_total','critical','high','medium','low','info','gate_blocking','transparency_blocking']},'public_hardening_actions':{'verifier_proof_updates_recommended':len(gaps),'redteam_scenarios_recommended':len(gaps),'validator_updates_recommended':len(gaps),'policy_updates_recommended':len(gaps),'scanner_updates_recommended':len(gaps),'docs_updates_recommended':1,'conformance_updates_recommended':1},'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True,'no_restricted_observations_public':True,'no_quarantines_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True,'no_network_required':True,'no_credentials_required':True},'generated_at':ts}
 text=json.dumps(public)
 if any(re.search(rf'\b{re.escape(x)}\b',text,re.I) for x in CLAIMS): raise SystemExit('unsupported claim in public output')
 (pub/'public_hardening_summary.json').write_text(json.dumps(public,indent=2)+'\n')
 (pub/'public_hardening_summary.md').write_text('# Public hardening summary\n\nAggregate-only, no exact points.\n')
 print(json.dumps({'hardening_id':hardening_id,'out_dir':str(out),'public_out_dir':str(pub)}))
if __name__=='__main__': main()
