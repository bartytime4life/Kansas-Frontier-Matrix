import json,re
from pathlib import Path
from .checksums import sha256_path
from .constants import REQUIRED_LAYER20_KEYS,L20_DENIED_TRUE_FIELDS,EVIDENCE_TYPES,INTERNAL_DISCLAIMER,FORBIDDEN_TEXT_TERMS,COORD_RE,REFS
from .ids import sid
from .loaders import loadj,wj,wjl
from .manifest import validate_manifest,validate_path_safe

def _deny(m,out,created_at,errs):
 r={"object_type":"AirNowSnapshotPreservationReviewReceipt","schema_version":"v1","workflow_runner":"airnow_layer21_snapshot_preservation_review","manifest_id":m.get("manifest_id"),"workflow_outcome":"SNAPSHOT_PRESERVATION_REVIEW_DENIED_REQUESTED_CAPABILITY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"review_actions_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(set(errs)),"output_hashes":{"snapshot_preservation_review_packet_hash":None},"created_at":created_at}
 wj(out/'snapshot_preservation_review_receipt.json',r); return r

def run_snapshot_preservation_review(manifest_path,out_dir,created_at):
 out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); m=loadj(manifest_path); errs=validate_manifest(m)
 l20=m.get('layer20_inputs',{})
 for k in REQUIRED_LAYER20_KEYS:
  p=l20.get(k)
  if not p: errs.append(f"MISSING_REQUIRED_INPUT:layer20_inputs.{k}"); continue
  if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:layer20_inputs.{k}")
  elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:layer20_inputs.{k}")
 ev=m.get('manual_evidence',[])
 if not isinstance(ev,list) or not ev: errs.append('MISSING_MANUAL_EVIDENCE')
 for i,e in enumerate(ev):
  t=e.get('evidence_type'); p=e.get('path','')
  if t not in EVIDENCE_TYPES: errs.append(f"INVALID_EVIDENCE_TYPE:{i}")
  if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:manual_evidence[{i}]")
  elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:manual_evidence[{i}]")
 if errs: return _deny(m,out,created_at,errs)
 r20=loadj(l20['snapshot_preservation_receipt'])
 if r20.get('object_type')!='AirNowSnapshotPreservationReceipt': errs.append('INVALID_LAYER20_RECEIPT_OBJECT_TYPE')
 for f in L20_DENIED_TRUE_FIELDS:
  if r20.get(f) is True: errs.append(f"LAYER20_RECEIPT_DENIED_CAPABILITY_REQUIRED:{f}")
 if errs: return _deny(m,out,created_at,errs)
 wj(out/'snapshot_preservation_review_manifest.resolved.json',{"object_type":"AirNowResolvedSnapshotPreservationReviewManifest","schema_version":"v1","manifest_id":m.get('manifest_id'),"created_at":created_at})
 inv=[]; assess=[]
 for i,e in enumerate(sorted(ev,key=lambda x:(x.get('evidence_type',''),x.get('path','')))):
  p=Path(e['path']); txt=p.read_text(errors='ignore') if p.suffix.lower() in ('.md','.txt','.json') else ''
  if p.suffix.lower() in ('.md','.txt'):
   if INTERNAL_DISCLAIMER.lower() not in txt.lower(): errs.append(f"MISSING_INTERNAL_DISCLAIMER:{p}")
   if re.search(COORD_RE,txt): errs.append(f"COORDINATE_LEAK:{p}")
  if any(t in txt.lower() for t in FORBIDDEN_TEXT_TERMS): errs.append(f"FORBIDDEN_LANGUAGE:{p}")
  eid=sid('kfm:airnow:l21:evidence:v1',[m.get('manifest_id'),e['evidence_type'],e['path']])
  inv.append({"evidence_id":eid,"evidence_type":e['evidence_type'],"path":e['path'],"sha256":sha256_path(p),"byte_size":p.stat().st_size})
  assess.append({"assessment_id":sid('kfm:airnow:l21:assessment:v1',eid),"evidence_id":eid,"candidate_supported":True})
 if errs: return _deny(m,out,created_at,errs)
 wj(out/'snapshot_preservation_review_evidence_inventory.json',{"object_type":"AirNowSnapshotPreservationReviewEvidenceInventory","schema_version":"v1","records":inv,"created_at":created_at}); wjl(out/'snapshot_preservation_review_evidence_inventory.jsonl',sorted(inv,key=lambda x:x['evidence_id']))
 wj(out/'snapshot_preservation_review_assessment_matrix.json',{"object_type":"AirNowSnapshotPreservationReviewAssessmentMatrix","schema_version":"v1","records":assess,"created_at":created_at}); wjl(out/'snapshot_preservation_review_assessment_matrix.jsonl',sorted(assess,key=lambda x:x['assessment_id']))
 sat=[{"item_id":k,"satisfied":True} for k in sorted(REQUIRED_LAYER20_KEYS)]
 wj(out/'snapshot_preservation_item_satisfaction_matrix.json',{"object_type":"AirNowSnapshotPreservationItemSatisfactionMatrix","schema_version":"v1","records":sat,"created_at":created_at}); wjl(out/'snapshot_preservation_item_satisfaction_matrix.jsonl',sat)
 acc=[{"acceptance_id":sid('kfm:airnow:l21:accept:v1',m.get('manifest_id','')),"candidate":"ACCEPT_LAYER20_PLAN_FOR_MANUAL_INTERNAL_PRESERVATION_REVIEW_ONLY"}]
 wjl(out/'snapshot_preservation_acceptance_candidates.jsonl',acc); wjl(out/'residual_snapshot_preservation_blockers.jsonl',[])
 v=[{"validation_id":sid('kfm:airnow:l21:validation:v1',m.get('manifest_id','')),"status":"PASS"}]
 wj(out/'snapshot_preservation_review_validation_results.json',{"object_type":"AirNowSnapshotPreservationReviewValidationResults","schema_version":"v1","records":v,"created_at":created_at}); wjl(out/'snapshot_preservation_review_validation_results.jsonl',v)
 wj(out/'snapshot_preservation_review_readiness_summary.json',{"object_type":"AirNowSnapshotPreservationReviewReadinessSummary","schema_version":"v1","readiness_status":"READY_FOR_MANUAL_INTERNAL_REVIEW","created_at":created_at})
 wj(out/'snapshot_preservation_review_rerun_plan.json',{"object_type":"AirNowSnapshotPreservationReviewRerunPlan","schema_version":"v1","rerun_required":False,"created_at":created_at})
 wj(out/'snapshot_preservation_review_policy_attestation.json',{"object_type":"AirNowSnapshotPreservationReviewPolicyAttestation","schema_version":"v1","policy_status":"CONTINUED","references":REFS,"created_at":created_at})
 wj(out/'snapshot_preservation_review_caveat_register.json',{"object_type":"AirNowSnapshotPreservationReviewCaveatRegister","schema_version":"v1","caveats":["INTERNAL_ONLY","NO_EXECUTION"],"created_at":created_at})
 wj(out/'snapshot_preservation_review_status_board.json',{"object_type":"AirNowSnapshotPreservationReviewStatusBoard","schema_version":"v1","board_status":"SNAPSHOT_PRESERVATION_REVIEW_ACCEPTED_FOR_INTERNAL_REVIEW","created_at":created_at})
 (out/'snapshot_preservation_review_status_board.md').write_text('# AirNow Layer 21 Snapshot Preservation Review Status Board\n\nInternal-only manual review intake complete.\n')
 (out/'snapshot_preservation_review_report.md').write_text('# AirNow Layer 21 Snapshot Preservation Review Report\n\nCandidate-only acceptance for manual internal preservation review; no execution.\n')
 r={"object_type":"AirNowSnapshotPreservationReviewReceipt","schema_version":"v1","workflow_runner":"airnow_layer21_snapshot_preservation_review","manifest_id":m.get("manifest_id"),"workflow_outcome":"SNAPSHOT_PRESERVATION_REVIEW_ACCEPTED_FOR_INTERNAL_REVIEW","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"review_actions_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"snapshot_preservation_review_packet_hash":None},"created_at":created_at}
 wj(out/'snapshot_preservation_review_receipt.json',r); return r
