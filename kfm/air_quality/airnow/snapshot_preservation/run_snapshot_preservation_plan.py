import hashlib
import io
import json
import tarfile
from pathlib import Path
from .checksums import sha256_path
from .constants import LAYER19_REQUIRED_KEYS,REFS
from .ids import sid
from .loaders import loadj,wj,wjl
from .manifest import validate_manifest,validate_path_safe


def _deny(m,out,created_at,errs):
 r={"object_type":"AirNowSnapshotPreservationReceipt","schema_version":"v1","workflow_runner":"airnow_layer20_snapshot_preservation","manifest_id":m.get("manifest_id"),"workflow_outcome":"SNAPSHOT_PRESERVATION_PLAN_DENIED_REQUESTED_CAPABILITY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(set(errs)),"output_hashes":{"snapshot_preservation_packet_hash":None},"created_at":created_at}
 wj(out/"snapshot_preservation_receipt.json",r)
 return r



def _build_packet(out: Path, created_at: str):
 packet = out / "snapshot_preservation_packet.tar.gz"
 members=[]
 for fp in sorted(out.iterdir(), key=lambda x: x.name):
  if not fp.is_file():
   continue
  if fp.name==packet.name:
   continue
  rel=fp.name
  if rel.startswith('/') or '..' in Path(rel).parts:
   raise ValueError('UNSAFE_PACKET_MEMBER_PATH')
  members.append(fp)
 with tarfile.open(packet,'w:gz',format=tarfile.PAX_FORMAT) as tf:
  for fp in members:
   data=fp.read_bytes()
   ti=tarfile.TarInfo(name=fp.name)
   ti.size=len(data); ti.mtime=0; ti.uid=0; ti.gid=0; ti.uname=''; ti.gname=''; ti.mode=0o644
   tf.addfile(ti,io.BytesIO(data))
 return packet

def run_snapshot_preservation_plan(manifest_path,out_dir,created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); errs=validate_manifest(m)
 li=m.get("layer19_inputs",{})
 for k in LAYER19_REQUIRED_KEYS:
  p=li.get(k)
  if not p: errs.append(f"MISSING_REQUIRED_INPUT:layer19_inputs.{k}"); continue
  if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:layer19_inputs.{k}")
  elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:layer19_inputs.{k}")
 if errs: return _deny(m,out,created_at,errs)
 r19=loadj(li["snapshot_audit_receipt"])
 if r19.get("object_type")!="AirNowSnapshotAuditReceipt": errs.append("INVALID_LAYER19_RECEIPT_OBJECT_TYPE")
 for f in ["publication_allowed","public_release_allowed","snapshot_export_execution_allowed","snapshot_copy_allowed","snapshot_transfer_allowed","snapshot_publication_allowed","snapshot_release_allowed","archive_transfer_allowed","file_deletion_allowed","legal_hold_creation_allowed","official_archive_certification_allowed","command_execution_allowed","final_accession_execution_allowed","preservation_action_execution_allowed","task_closure_allowed"]:
  if r19.get(f) is True: errs.append(f"LAYER19_RECEIPT_DENIED_CAPABILITY_REQUIRED:{f}")
 if errs: return _deny(m,out,created_at,errs)
 wj(out/'snapshot_preservation_manifest.resolved.json',{"object_type":"AirNowResolvedSnapshotPreservationManifest","schema_version":"v1","manifest_id":m.get('manifest_id'),"created_at":created_at})
 rows=[]
 for k,v in sorted(li.items()):
  p=Path(v); rows.append({"input_record_id":sid('kfm:airnow:l20:input:v1',[m.get('manifest_id'),k]),"input_id":k,"path_original":v,"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at})
 wj(out/'snapshot_preservation_input_inventory.json',{"object_type":"AirNowSnapshotPreservationInputInventory","schema_version":"v1","records":rows,"created_at":created_at}); wjl(out/'snapshot_preservation_input_inventory.jsonl',sorted(rows,key=lambda x:x['input_record_id']))
 scope=[{"scope_record_id":sid('kfm:airnow:l20:scope:v1',r['input_id']),"input_id":r['input_id'],"scope":"INTERNAL_ONLY"} for r in rows]
 wj(out/'snapshot_preservation_scope_plan.json',{"object_type":"AirNowSnapshotPreservationScopePlan","schema_version":"v1","records":scope,"created_at":created_at}); wjl(out/'snapshot_preservation_scope_plan.jsonl',sorted(scope,key=lambda x:x['scope_record_id']))
 def cls(name):
  if any(t in name for t in ['receipt','decision','policy','caveat','hash_chain']): return 'internal_audit_core'
  if any(t in name for t in ['status','report']): return 'internal_generated_report'
  if any(t in name for t in ['blocker','exception']): return 'internal_governance_record'
  return 'internal_governance_record'
 c=[{"classification_id":sid('kfm:airnow:l20:class:v1',r['input_id']),"input_id":r['input_id'],"classification":cls(r['input_id'])} for r in rows]
 wj(out/'snapshot_preservation_classification_matrix.json',{"object_type":"AirNowSnapshotPreservationClassificationMatrix","schema_version":"v1","records":c,"created_at":created_at}); wjl(out/'snapshot_preservation_classification_matrix.jsonl',sorted(c,key=lambda x:x['classification_id']))
 f=[{"fixity_id":sid('kfm:airnow:l20:fixity:v1',r['input_id']),"input_id":r['input_id'],"algorithm":"sha256","baseline_sha256":r['sha256']} for r in rows]
 wj(out/'snapshot_preservation_fixity_plan.json',{"object_type":"AirNowSnapshotPreservationFixityPlan","schema_version":"v1","records":f,"created_at":created_at}); wjl(out/'snapshot_preservation_fixity_plan.jsonl',sorted(f,key=lambda x:x['fixity_id']))
 wj(out/'snapshot_preservation_layout_plan.json',{"object_type":"AirNowSnapshotPreservationLayoutPlan","schema_version":"v1","planning_only":True,"record_count":len(rows),"created_at":created_at}); wjl(out/'snapshot_preservation_layout_plan.jsonl',[{"layout_id":sid('kfm:airnow:l20:layout:v1',m.get('manifest_id','')),"planning_only":True}])
 for nm,objt in [('access_review','AirNowSnapshotPreservationAccessReviewPlan'),('minimization_review','AirNowSnapshotPreservationMinimizationReviewPlan')]:
  rec=[{"record_id":sid(f'kfm:airnow:l20:{nm}:v1',r['input_id']),"input_id":r['input_id'],"public_access_allowed":False,"execution_performed":False} for r in rows]
  wj(out/f'snapshot_preservation_{nm}_plan.json',{"object_type":objt,"schema_version":"v1","records":rec,"created_at":created_at}); wjl(out/f'snapshot_preservation_{nm}_plan.jsonl',sorted(rec,key=lambda x:x['record_id']))
 hold=[{"record_id":sid('kfm:airnow:l20:hold_candidate:v1',r['input_id']),"input_id":r['input_id'],"candidate_only":True,"legal_hold_created":False} for r in rows]
 wj(out/'snapshot_preservation_hold_candidate_plan.json',{"object_type":"AirNowSnapshotPreservationHoldCandidatePlan","schema_version":"v1","records":hold,"created_at":created_at}); wjl(out/'snapshot_preservation_hold_candidate_plan.jsonl',sorted(hold,key=lambda x:x['record_id']))
 risks=[{"risk_id":sid('kfm:airnow:l20:risk:v1','preliminary'),"risk":"PRELIMINARY_DATA_NON_REGULATORY"},{"risk_id":sid('kfm:airnow:l20:risk:v1','regulatory'),"risk":"NON_REGULATORY_DATA_USE_ONLY"},{"risk_id":sid('kfm:airnow:l20:risk:v1','freshness'),"risk":"NO_LIVE_FRESHNESS_ASSERTION"}]
 wj(out/'snapshot_preservation_risk_register.json',{"object_type":"AirNowSnapshotPreservationRiskRegister","schema_version":"v1","records":risks,"created_at":created_at}); wjl(out/'snapshot_preservation_risk_register.jsonl',sorted(risks,key=lambda x:x['risk_id']))
 wjl(out/'snapshot_preservation_blockers.jsonl',[])
 wj(out/'snapshot_preservation_non_execution_attestation.json',{"object_type":"AirNowSnapshotPreservationNonExecutionAttestation","schema_version":"v1","commands_executed":False,"preservation_actions_executed":False,"created_at":created_at})
 pol=[{"policy_id":sid('kfm:airnow:l20:policy:v1',m.get('manifest_id','')),"continuity_status":"CONTINUED"}]
 wj(out/'snapshot_preservation_policy_continuity_matrix.json',{"object_type":"AirNowSnapshotPreservationPolicyContinuityMatrix","schema_version":"v1","records":pol,"created_at":created_at}); wjl(out/'snapshot_preservation_policy_continuity_matrix.jsonl',pol)
 wj(out/'snapshot_preservation_caveat_register.json',{"object_type":"AirNowSnapshotPreservationCaveatRegister","schema_version":"v1","caveats":["AIRNOW_PRELIMINARY_DATA","AIRNOW_NOT_AQS_REGULATORY_DATA","AIRNOW_NO_BULK_ZIP_WEB_SERVICE_LOOP","SNAPSHOT_PRESERVATION_NOT_ACTION_EXECUTION","SNAPSHOT_PRESERVATION_NOT_PUBLICATION"],"references":REFS,"created_at":created_at})
 wj(out/'snapshot_preservation_readiness_summary.json',{"object_type":"AirNowSnapshotPreservationReadinessSummary","schema_version":"v1","readiness_status":"NEEDS_MANUAL_REVIEW","created_at":created_at})
 wj(out/'snapshot_preservation_rerun_plan.json',{"object_type":"AirNowSnapshotPreservationRerunPlan","schema_version":"v1","rerun_required":False,"created_at":created_at})
 wj(out/'snapshot_preservation_status_board.json',{"object_type":"AirNowSnapshotPreservationStatusBoard","schema_version":"v1","board_status":"SNAPSHOT_PRESERVATION_PLAN_COMPLETE_INTERNAL_ONLY","created_at":created_at})
 (out/'snapshot_preservation_status_board.md').write_text('# AirNow Layer 20 Snapshot Preservation Status Board\n\nInternal planning only. No execution, transfer, publication, or release.\n')
 (out/'snapshot_preservation_report.md').write_text('# AirNow Layer 20 Snapshot Preservation Report\n\nPlanning-only internal preservation review preparation; no preservation execution.\n')
 r={"object_type":"AirNowSnapshotPreservationReceipt","schema_version":"v1","workflow_runner":"airnow_layer20_snapshot_preservation","manifest_id":m.get("manifest_id"),"workflow_outcome":"SNAPSHOT_PRESERVATION_PLAN_COMPLETE_INTERNAL_ONLY","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"snapshot_preservation_packet_hash":None},"created_at":created_at}
 if m.get('preservation_policy',{}).get('include_packet') is True:
  packet=_build_packet(out,created_at)
  r['output_hashes']['snapshot_preservation_packet_hash']=sha256_path(packet)
 wj(out/'snapshot_preservation_receipt.json',r)
 return r
