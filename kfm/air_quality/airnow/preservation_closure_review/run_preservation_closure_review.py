import json, re, tarfile, hashlib
from datetime import datetime, timezone
from pathlib import Path
from .checksums import sha256_path
from .constants import REQUIRED_LAYER24_KEYS,L24_DENIED_TRUE_FIELDS,EVIDENCE_TYPES,INTERNAL_DISCLAIMER,FORBIDDEN_TEXT_TERMS,COORD_RE,REFS
from .ids import sid
from .loaders import loadj,wj,wjl
from .manifest import validate_manifest,validate_path_safe
EPOCH=datetime(1970,1,1,tzinfo=timezone.utc)

def _packet(out,created_at):
 files=sorted([p for p in out.iterdir() if p.is_file() and p.name!='preservation_closure_review_packet.tar.gz'])
 pkt=out/'preservation_closure_review_packet.tar.gz'
 with tarfile.open(pkt,'w:gz',format=tarfile.PAX_FORMAT) as tf:
  for p in files:
   if p.name.endswith('.tar.gz') or p.name.endswith('.zip'): continue
   ti=tf.gettarinfo(str(p),arcname=p.name); ti.uid=0; ti.gid=0; ti.uname=''; ti.gname=''; ti.mtime=0
   with p.open('rb') as fh: tf.addfile(ti,fh)
 return hashlib.sha256(pkt.read_bytes()).hexdigest()

def _deny(m,out,created_at,errs):
 r={"object_type":"AirNowPreservationClosureReviewReceipt","schema_version":"v1","workflow_runner":"airnow_layer25_preservation_closure_review","manifest_id":m.get("manifest_id"),"workflow_outcome":"PRESERVATION_CLOSURE_REVIEW_DENIED_REQUESTED_CAPABILITY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"review_actions_executed":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(set(errs)),"output_hashes":{"preservation_closure_review_packet_hash":None},"created_at":created_at}
 wj(out/'preservation_closure_review_receipt.json',r); return r

def run_preservation_closure_review(manifest_path,out_dir,created_at):
 out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); m=loadj(manifest_path); errs=validate_manifest(m)
 l24=m.get('layer24_inputs',{})
 for k in REQUIRED_LAYER24_KEYS:
  p=l24.get(k)
  if not p: errs.append(f"MISSING_REQUIRED_INPUT:layer24_inputs.{k}"); continue
  if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:layer24_inputs.{k}")
  elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:layer24_inputs.{k}")
 ev=m.get('manual_evidence',[])
 if not isinstance(ev,list) or not ev: errs.append('MISSING_MANUAL_EVIDENCE')
 for i,e in enumerate(ev):
  if e.get('evidence_type') not in EVIDENCE_TYPES: errs.append(f"INVALID_EVIDENCE_TYPE:{i}")
  p=e.get('path','')
  if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:manual_evidence[{i}]")
  elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:manual_evidence[{i}]")
 if errs: return _deny(m,out,created_at,errs)
 r24=loadj(l24['preservation_closure_receipt'])
 if r24.get('object_type')!='AirNowPreservationClosureReceipt': errs.append('INVALID_LAYER24_RECEIPT_OBJECT_TYPE')
 for f in L24_DENIED_TRUE_FIELDS:
  if r24.get(f) is True: errs.append(f"LAYER24_RECEIPT_DENIED_CAPABILITY_REQUIRED:{f}")
 if errs: return _deny(m,out,created_at,errs)
 wj(out/'preservation_closure_review_manifest.resolved.json',{"object_type":"AirNowResolvedPreservationClosureReviewManifest","schema_version":"v1","manifest_id":m.get('manifest_id'),"created_at":created_at})
 inv=[]; assess=[]
 for e in sorted(ev,key=lambda x:(x.get('evidence_type',''),x.get('path',''))):
  p=Path(e['path']); txt=p.read_text(errors='ignore') if p.suffix.lower() in ('.md','.txt','.json') else ''
  if p.suffix.lower() in ('.md','.txt'):
   if INTERNAL_DISCLAIMER.lower() not in txt.lower(): errs.append(f"MISSING_INTERNAL_DISCLAIMER:{p}")
   if re.search(COORD_RE,txt): errs.append(f"COORDINATE_LEAK:{p}")
  if any(t in txt.lower() for t in FORBIDDEN_TEXT_TERMS): errs.append(f"FORBIDDEN_LANGUAGE:{p}")
  eid=sid('kfm:airnow:l25:evidence:v1',[m.get('manifest_id'),e['evidence_type'],e['path']])
  inv.append({"evidence_id":eid,"evidence_type":e['evidence_type'],"path":e['path'],"sha256":sha256_path(p),"byte_size":p.stat().st_size})
  assess.append({"assessment_id":sid('kfm:airnow:l25:assessment:v1',eid),"evidence_id":eid,"candidate_supported":True})
 if errs: return _deny(m,out,created_at,errs)
 wj(out/'preservation_closure_review_evidence_inventory.json',{"object_type":"AirNowPreservationClosureReviewEvidenceInventory","schema_version":"v1","records":inv,"created_at":created_at}); wjl(out/'preservation_closure_review_evidence_inventory.jsonl',sorted(inv,key=lambda x:x['evidence_id']))
 wj(out/'preservation_closure_review_assessment_matrix.json',{"object_type":"AirNowPreservationClosureReviewAssessmentMatrix","schema_version":"v1","records":assess,"created_at":created_at}); wjl(out/'preservation_closure_review_assessment_matrix.jsonl',sorted(assess,key=lambda x:x['assessment_id']))
 sat=[{"item_id":k,"satisfied":True} for k in sorted(REQUIRED_LAYER24_KEYS)]
 wj(out/'preservation_closure_item_satisfaction_matrix.json',{"object_type":"AirNowPreservationClosureItemSatisfactionMatrix","schema_version":"v1","records":sat,"created_at":created_at}); wjl(out/'preservation_closure_item_satisfaction_matrix.jsonl',sat)
 wjl(out/'preservation_closure_acceptance_candidates.jsonl',[{"acceptance_id":sid('kfm:airnow:l25:accept:v1',m.get('manifest_id','')),"candidate":"ACCEPT_LAYER24_CLOSURE_READINESS_FOR_MANUAL_INTERNAL_CLOSURE_REVIEW_ONLY"}])
 wjl(out/'residual_preservation_closure_blockers.jsonl',[])
 v=[{"validation_id":sid('kfm:airnow:l25:validation:v1',m.get('manifest_id','')),"status":"PASS"}]
 wj(out/'preservation_closure_review_validation_results.json',{"object_type":"AirNowPreservationClosureReviewValidationResults","schema_version":"v1","records":v,"created_at":created_at}); wjl(out/'preservation_closure_review_validation_results.jsonl',v)
 wj(out/'preservation_closure_review_readiness_summary.json',{"object_type":"AirNowPreservationClosureReviewReadinessSummary","schema_version":"v1","readiness_status":"READY_FOR_MANUAL_INTERNAL_CLOSURE_REVIEW","created_at":created_at})
 wj(out/'preservation_closure_review_rerun_plan.json',{"object_type":"AirNowPreservationClosureReviewRerunPlan","schema_version":"v1","rerun_required":False,"created_at":created_at})
 wj(out/'preservation_closure_review_policy_attestation.json',{"object_type":"AirNowPreservationClosureReviewPolicyAttestation","schema_version":"v1","policy_status":"CONTINUED","references":REFS,"created_at":created_at})
 wj(out/'preservation_closure_review_caveat_register.json',{"object_type":"AirNowPreservationClosureReviewCaveatRegister","schema_version":"v1","caveats":["AIRNOW_PRELIMINARY_DATA","AIRNOW_NOT_AQS_REGULATORY_DATA","AIRNOW_NO_BULK_ZIP_WEB_SERVICE_LOOP","PRESERVATION_CLOSURE_REVIEW_NOT_ACTUAL_CLOSURE","PRESERVATION_CLOSURE_REVIEW_NOT_PUBLICATION"],"created_at":created_at})
 wj(out/'preservation_closure_review_status_board.json',{"object_type":"AirNowPreservationClosureReviewStatusBoard","schema_version":"v1","board_status":"PRESERVATION_CLOSURE_REVIEW_ACCEPTED_FOR_INTERNAL_REVIEW","created_at":created_at})
 (out/'preservation_closure_review_status_board.md').write_text('# AirNow Layer 25 Preservation Closure Review Status Board\n\nInternal-only manual review intake complete. Not publication, not dashboard, not API, and no closure execution.\n')
 (out/'preservation_closure_review_report.md').write_text('# AirNow Layer 25 Preservation Closure Review Report\n\nCandidate-only acceptance for manual internal closure review; no closure execution, no task/audit/governance closure, no preservation actions.\n')
 packet_hash=None
 if bool(m.get('review_policy',{}).get('include_packet',False)):
  packet_hash=_packet(out,created_at)
 r={"object_type":"AirNowPreservationClosureReviewReceipt","schema_version":"v1","workflow_runner":"airnow_layer25_preservation_closure_review","manifest_id":m.get("manifest_id"),"workflow_outcome":"PRESERVATION_CLOSURE_REVIEW_ACCEPTED_FOR_INTERNAL_REVIEW","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"review_actions_executed":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"preservation_closure_review_packet_hash":packet_hash},"created_at":created_at}
 wj(out/'preservation_closure_review_receipt.json',r); return r
