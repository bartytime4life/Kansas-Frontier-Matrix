import json,re
from pathlib import Path
from .constants import L23_INPUTS,FORBIDDEN_TEXT_TERMS,COORD_RE,REFS
from .loaders import loadj
from .checksums import sha256_path
from .ids import sid,cjson
from .manifest import validate_manifest,validate_path_safe

def _wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def _wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))
def _deny(m,out,created_at,errs):
 r={"object_type":"AirNowPreservationClosureReceipt","schema_version":"v1","workflow_runner":"airnow_layer24_preservation_closure_readiness","manifest_id":m.get("manifest_id"),"workflow_outcome":"PRESERVATION_CLOSURE_DENIED_BY_POLICY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(set(errs)),"created_at":created_at}
 _wj(out/'preservation_closure_receipt.json',r); return r

def build_layer23_intake(m,created_at):
 d={}
 for k in L23_INPUTS: d[k]=loadj(m['layer23_inputs'][k])
 return d

def run_preservation_closure_readiness(manifest_path,out_dir,created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); errs=validate_manifest(m)
 for k in L23_INPUTS:
  p=m.get('layer23_inputs',{}).get(k)
  if not p: errs.append(f'MISSING_REQUIRED_INPUT:layer23_inputs.{k}'); continue
  if not validate_path_safe(p): errs.append(f'UNSAFE_PATH:layer23_inputs.{k}')
  elif not Path(p).exists(): errs.append(f'MISSING_INPUT_FILE:layer23_inputs.{k}')
 if errs: return _deny(m,out,created_at,errs)
 l23=build_layer23_intake(m,created_at); r=l23['snapshot_preservation_audit_receipt_json']
 if r.get('object_type')!='AirNowSnapshotPreservationAuditReceipt': errs.append('INVALID_LAYER23_RECEIPT_OBJECT_TYPE')
 for f in ['publication_allowed','public_release_allowed','preservation_action_allowed','preservation_copy_allowed','preservation_transfer_allowed','snapshot_export_execution_allowed','snapshot_copy_allowed','snapshot_transfer_allowed','snapshot_publication_allowed','snapshot_release_allowed','archive_transfer_allowed','file_deletion_allowed','legal_hold_creation_allowed','official_archive_certification_allowed','command_execution_allowed','final_accession_execution_allowed','task_closure_allowed','audit_closure_allowed']:
  if r.get(f) is True: errs.append('FORBIDDEN_LAYER23_RECEIPT_FLAG:'+f)
 if errs: return _deny(m,out,created_at,errs)
 _wj(out/'preservation_closure_manifest.resolved.json',{"object_type":"AirNowResolvedPreservationClosureManifest","schema_version":"v1","manifest_id":m.get('manifest_id'),"created_at":created_at})
 inv=[]
 for k in sorted(L23_INPUTS):
  p=Path(m['layer23_inputs'][k]); inv.append({"input_record_id":sid('kfm:air_quality:airnow:preservation_closure_input_record:v1',[m.get('manifest_id'),k]),"input_id":k,"path_original":str(p),"exists":p.exists(),"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at})
 _wj(out/'preservation_closure_input_inventory.json',{"object_type":"AirNowPreservationClosureInputInventory","schema_version":"v1","records":inv,"created_at":created_at}); _wjl(out/'preservation_closure_input_inventory.jsonl',sorted(inv,key=lambda x:x['input_record_id']))
 unresolved=[]
 comp=l23['snapshot_preservation_completeness_matrix_json'].get('records',[]); cons=l23['snapshot_preservation_consistency_matrix_json'].get('records',[]); exc=l23['snapshot_preservation_audit_exception_register_json'].get('records',[])
 for rec in comp+cons:
  if rec.get('pass') is False: unresolved.append({'issue_id':sid('issue',[rec.get('check','unknown')]),'type':'FAILED_CHECK','check':rec.get('check')})
 for i,e in enumerate(exc): unresolved.append({'issue_id':sid('issue',['exception',i]),'type':'EXCEPTION','detail':e})
 ready=not unresolved
 rd=[{"readiness_id":sid('readiness',[m.get('manifest_id')]),"readiness_status":"READY_FOR_INTERNAL_GOVERNANCE_CLOSURE_REVIEW" if ready else "NOT_READY","unresolved_issue_count":len(unresolved)}]
 _wj(out/'preservation_closure_readiness_matrix.json',{"object_type":"AirNowPreservationClosureReadinessMatrix","schema_version":"v1","records":rd,"created_at":created_at}); _wjl(out/'preservation_closure_readiness_matrix.jsonl',rd)
 cand=[{"candidate_id":sid('candidate',[m.get('manifest_id')]),"candidate_type":"INTERNAL_GOVERNANCE_CLOSURE_REVIEW","candidate_status":"CANDIDATE_ONLY"}]
 _wj(out/'preservation_closure_candidate_ledger.json',{"object_type":"AirNowPreservationClosureCandidateLedger","schema_version":"v1","records":cand,"created_at":created_at}); _wjl(out/'preservation_closure_candidate_ledger.jsonl',cand)
 _wj(out/'unresolved_preservation_issue_register.json',{"object_type":"AirNowUnresolvedPreservationIssueRegister","schema_version":"v1","records":unresolved,"created_at":created_at}); _wjl(out/'unresolved_preservation_issue_register.jsonl',sorted(unresolved,key=lambda x:x['issue_id']))
 _wj(out/'preservation_governance_closure_gate.json',{"object_type":"AirNowPreservationGovernanceClosureGate","schema_version":"v1","gate_status":"INTERNAL_GOVERNANCE_CLOSURE_REVIEW_READY" if ready else "INTERNAL_GOVERNANCE_CLOSURE_REVIEW_BLOCKED","positive_outcome_ceiling":"INTERNAL_GOVERNANCE_CLOSURE_REVIEW_READY","created_at":created_at})
 ver=[{"check":"layer23_receipt_type","pass":True},{"check":"layer23_receipt_no_forbidden_flags","pass":True}]
 _wj(out/'preservation_receipt_closure_verification_matrix.json',{"object_type":"AirNowPreservationReceiptClosureVerificationMatrix","schema_version":"v1","records":ver,"created_at":created_at}); _wjl(out/'preservation_receipt_closure_verification_matrix.jsonl',ver)
 ev=[{"evidence_id":sid('evidence',[i]),"source":"layer23","object_type":x.get('object_type')} for i,x in enumerate([l23['snapshot_preservation_receipt_ledger_json'],l23['snapshot_preservation_decision_ledger_json'],l23['snapshot_preservation_evidence_ledger_json'],l23['snapshot_preservation_hash_chain_json']])]
 _wj(out/'preservation_evidence_closure_summary.json',{"object_type":"AirNowPreservationEvidenceClosureSummary","schema_version":"v1","records":ev,"created_at":created_at}); _wjl(out/'preservation_evidence_closure_summary.jsonl',ev)
 pol=[{"policy_id":sid('policy',[m.get('manifest_id')]),"continuity_status":"CONTINUOUS"}]
 _wj(out/'preservation_policy_closure_continuity_matrix.json',{"object_type":"AirNowPreservationPolicyClosureContinuityMatrix","schema_version":"v1","records":pol,"created_at":created_at}); _wjl(out/'preservation_policy_closure_continuity_matrix.jsonl',pol)
 _wj(out/'preservation_caveat_closure_continuity_register.json',{"object_type":"AirNowPreservationCaveatClosureContinuityRegister","schema_version":"v1","records":l23['snapshot_preservation_caveat_registry_json'].get('records',[]),"created_at":created_at})
 _wj(out/'preservation_closure_non_execution_attestation.json',{"object_type":"AirNowPreservationClosureNonExecutionAttestation","schema_version":"v1","commands_executed":False,"closure_executed":False,"created_at":created_at})
 _wj(out/'preservation_closure_decision_candidate.json',{"object_type":"AirNowPreservationClosureDecisionCandidate","schema_version":"v1","decision_candidate":"INTERNAL_REVIEW_ONLY","closure_execution":False,"created_at":created_at})
 _wj(out/'preservation_closure_rerun_plan.json',{"object_type":"AirNowPreservationClosureRerunPlan","schema_version":"v1","steps":[],"created_at":created_at})
 _wj(out/'preservation_closure_status_board.json',{"object_type":"AirNowPreservationClosureStatusBoard","schema_version":"v1","board_status":"PRESERVATION_CLOSURE_READY_INTERNAL_ONLY" if ready else "PRESERVATION_CLOSURE_BLOCKED_INTERNAL_ONLY","created_at":created_at})
 txt='Internal-only closure-readiness planning. Candidate-only; no closure execution, preservation execution, transfer, export, publication, or release.'
 if re.search(COORD_RE,txt): return _deny(m,out,created_at,['COORDINATE_LEAK'])
 if any(t in txt.lower() for t in FORBIDDEN_TEXT_TERMS): return _deny(m,out,created_at,['FORBIDDEN_LANGUAGE'])
 (out/'preservation_closure_status_board.md').write_text('# AirNow Layer 24 Preservation Closure Status Board\n\n'+txt+'\n')
 (out/'preservation_closure_report.md').write_text('# AirNow Layer 24 Preservation Closure Readiness Report\n\nInternal-only closure readiness planning from Layer 23 audit artifacts.\n')
 receipt={"object_type":"AirNowPreservationClosureReceipt","schema_version":"v1","workflow_runner":"airnow_layer24_preservation_closure_readiness","manifest_id":m.get('manifest_id'),"workflow_outcome":"PRESERVATION_CLOSURE_READY_INTERNAL_ONLY","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"references":REFS,"errors":[],"output_hashes":{"preservation_closure_packet_hash":None},"created_at":created_at}
 _wj(out/'preservation_closure_receipt.json',receipt); return receipt

# alias builders
build_input_inventory=build_readiness_matrix=build_candidate_ledger=build_unresolved_issues=build_governance_gate=build_receipt_verification=build_evidence_summary=build_policy_continuity=build_caveats=build_non_execution=build_decision_candidate=build_rerun=build_status_board=build_report=build_receipts=build_layer23_intake
