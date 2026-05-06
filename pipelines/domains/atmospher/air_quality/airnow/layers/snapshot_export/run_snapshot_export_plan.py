import json, tarfile, zipfile
from pathlib import Path
from .checksums import sha256_bytes
from .constants import DENY_SCHEMES,FORBIDDEN_MEMBER_TERMS
from .ids import sid
from .loaders import loadj,wj,wjl
from .manifest import validate_manifest
from .layer15_intake import validate_layer15_inputs

def _unsafe_path(v:str)->bool:
 vv=v.lower()
 return (".." in Path(v).parts) or any(vv.startswith(s) for s in DENY_SCHEMES) or ("://" in vv)



def _build_packet_if_enabled(manifest,out,created_at):
 pol=manifest.get("snapshot_policy",{}) if isinstance(manifest.get("snapshot_policy"),dict) else {}
 if not pol.get("include_packet",False):
  return None
 fmt=pol.get("packet_format","tar.gz")
 members=sorted([p for p in out.iterdir() if p.is_file() and p.name!="snapshot_export_planning_packet.tar.gz" and p.name!="snapshot_export_planning_packet.zip"], key=lambda p:p.name)
 if fmt=="zip":
  ap=out/'snapshot_export_planning_packet.zip'
  with zipfile.ZipFile(ap,'w',compression=zipfile.ZIP_DEFLATED) as zf:
   for m in members:
    zi=zipfile.ZipInfo(m.name)
    zi.date_time=(1980,1,1,0,0,0)
    zi.compress_type=zipfile.ZIP_DEFLATED
    zf.writestr(zi,m.read_bytes())
 else:
  ap=out/'snapshot_export_planning_packet.tar.gz'
  with tarfile.open(ap,'w:gz',format=tarfile.PAX_FORMAT) as tf:
   for m in members:
    ti=tarfile.TarInfo(name=m.name); b=m.read_bytes(); ti.size=len(b); ti.mtime=0; ti.uid=0; ti.gid=0; ti.uname=''; ti.gname=''
    import io; tf.addfile(ti,io.BytesIO(b))
 return sha256_bytes(ap.read_bytes())

def run_snapshot_export_plan(manifest_path,out_dir,created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
 errs=validate_manifest(m)
 miss=validate_layer15_inputs(m)
 if miss: errs += [f"MISSING_LAYER15_INPUT:{k}" for k in miss]
 li=m.get("layer15_inputs",{})
 rows=[]
 for k,v in sorted(li.items()):
  if _unsafe_path(v): errs.append(f"UNSAFE_PATH:{k}"); continue
  p=Path(v)
  if not p.exists(): errs.append(f"MISSING_INPUT_FILE:{k}"); continue
  b=p.read_bytes()
  obj=loadj(p) if p.suffix=='.json' else None
  rows.append({"input_id":k,"path":v,"sha256":sha256_bytes(b),"byte_size":len(b),"object_type_detected":obj.get("object_type") if obj else None})
 fr=[r for r in rows if r["input_id"]=="archival_finalization_receipt"]
 if not fr or fr[0].get("object_type_detected")!="AirNowArchivalFinalizationReceipt": errs.append("INVALID_LAYER15_RECEIPT_OBJECT_TYPE")
 if fr:
  receipt=loadj(li["archival_finalization_receipt"])
  banned=["publication_allowed","public_release_allowed","snapshot_export_execution_allowed","archive_transfer_allowed","file_deletion_allowed","legal_hold_creation_allowed","official_archive_certification_allowed","command_execution_allowed","final_accession_execution_allowed"]
  for bk in banned:
   if receipt.get(bk) not in (False,None): errs.append(f"LAYER15_RECEIPT_DENIED_CAPABILITY_REQUIRED:{bk}")
 plan_members=[]
 for r in sorted(rows,key=lambda x:x['input_id']):
  name=f"internal/{r['input_id']}.json"
  if any(t in name.lower() for t in FORBIDDEN_MEMBER_TERMS): errs.append(f"FORBIDDEN_MEMBER_PATH:{name}")
  plan_members.append({"member_id":sid("kfm:airnow:snapshot_member:v1",[m.get('manifest_id'),r['input_id']]),"member_path":name,"source_input_id":r['input_id']})
 denied=bool(errs)
 outcome="SNAPSHOT_EXPORT_PLAN_DENIED" if denied else "SNAPSHOT_EXPORT_PLAN_COMPLETE_INTERNAL_ONLY"
 val="FAIL" if denied else "PASS"
 finite="DENY" if denied else "ANSWER"
 resolved={"object_type":"AirNowResolvedSnapshotExportManifest","schema_version":"v1","manifest_id":m.get("manifest_id"),"created_at":created_at}
 wj(out/'snapshot_export_manifest.resolved.json',resolved)
 inv={"object_type":"AirNowSnapshotExportInputInventory","schema_version":"v1","records":rows,"created_at":created_at}; wj(out/'snapshot_export_input_inventory.json',inv); wjl(out/'snapshot_export_input_inventory.jsonl',sorted(rows,key=lambda x:x['input_id']))
 obj_list=[('snapshot_scope_plan',{"object_type":"AirNowSnapshotScopePlan","schema_version":"v1","scope":"INTERNAL_ONLY","created_at":created_at},[{"scope_item_id":sid("kfm:airnow:scope:v1",m.get('manifest_id','')),"scope":"INTERNAL_ONLY"}]),('snapshot_member_plan',{"object_type":"AirNowSnapshotMemberPlan","schema_version":"v1","members":plan_members,"created_at":created_at},plan_members),('snapshot_layout_plan',{"object_type":"AirNowSnapshotLayoutPlan","schema_version":"v1","layout_status":"PLANNED_ONLY","created_at":created_at},[{"layout_id":sid("kfm:airnow:layout:v1",m.get('manifest_id','')),"member_count":len(plan_members)}]),('snapshot_access_classification',{"object_type":"AirNowSnapshotAccessClassification","schema_version":"v1","classification":"INTERNAL","created_at":created_at},[{"access_id":sid("kfm:airnow:access:v1",m.get('manifest_id','')),"classification":"INTERNAL"}]),('snapshot_redaction_review_plan',{"object_type":"AirNowSnapshotRedactionReviewPlan","schema_version":"v1","redaction_required":True,"created_at":created_at},[{"review_id":sid("kfm:airnow:redaction:v1",m.get('manifest_id','')),"review_status":"REQUIRED"}]),('snapshot_fixity_plan',{"object_type":"AirNowSnapshotFixityPlan","schema_version":"v1","algorithm":"sha256","created_at":created_at},[{"fixity_id":sid("kfm:airnow:fixity:v1",m.get('manifest_id','')),"algorithm":"sha256"}]),('snapshot_manifest_preview',{"object_type":"AirNowSnapshotManifestPreview","schema_version":"v1","preview_members":len(plan_members),"created_at":created_at},sorted(plan_members,key=lambda x:x['member_id']))]
 for n,o,jl in obj_list: wj(out/f'{n}.json',o); wjl(out/f'{n}.jsonl',jl)
 wjl(out/'snapshot_export_blockers.jsonl',[{"blocker_id":sid("kfm:airnow:blocker:v1",e),"message":e} for e in sorted(errs)])
 wj(out/'snapshot_non_execution_attestation.json',{"object_type":"AirNowSnapshotNonExecutionAttestation","schema_version":"v1","commands_executed":False,"snapshot_export_executed":False,"created_at":created_at})
 wj(out/'snapshot_policy_continuity_matrix.json',{"object_type":"AirNowSnapshotPolicyContinuityMatrix","schema_version":"v1","policy_status":"CONTINUED","created_at":created_at}); wjl(out/'snapshot_policy_continuity_matrix.jsonl',[{"policy_id":sid("kfm:airnow:policy:v1",m.get('manifest_id','')),"policy_status":"CONTINUED"}])
 wj(out/'snapshot_caveat_continuity_register.json',{"object_type":"AirNowSnapshotCaveatContinuityRegister","schema_version":"v1","registry_status":"PASS","created_at":created_at})
 wj(out/'snapshot_readiness_summary.json',{"object_type":"AirNowSnapshotReadinessSummary","schema_version":"v1","readiness_status":"READY" if not denied else "DENIED","created_at":created_at})
 wj(out/'snapshot_rerun_plan.json',{"object_type":"AirNowSnapshotRerunPlan","schema_version":"v1","rerun_required":denied,"created_at":created_at})
 wj(out/'snapshot_status_board.json',{"object_type":"AirNowSnapshotStatusBoard","schema_version":"v1","board_status":outcome,"created_at":created_at})
 (out/'snapshot_status_board.md').write_text("# AirNow Layer 16 Snapshot Export Status Board\n\nInternal planning only.\n")
 (out/'snapshot_export_report.md').write_text("# AirNow Layer 16 Snapshot Export Report\n\nPlanning-only workflow; no execution.\n")
 packet_hash=_build_packet_if_enabled(m,out,created_at)
 receipt={"object_type":"AirNowSnapshotExportReceipt","schema_version":"v1","workflow_runner":"airnow_layer16_snapshot_export_plan","manifest_id":m.get("manifest_id"),"workflow_outcome":outcome,"validation_outcome":val,"finite_outcome":finite,"commands_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(errs),"output_hashes":{"snapshot_export_planning_packet_hash":packet_hash},"created_at":created_at}
 wj(out/'snapshot_export_receipt.json',receipt)
 return receipt
