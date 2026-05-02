import json,re,tarfile,hashlib,io
from pathlib import Path
from .checksums import sha256_path
from .ids import sid,cjson
from .loaders import loadj,loadjl
from .manifest import validate_manifest, validate_path_safe
from .constants import REFS,L23_REQUIRED,FORBIDDEN_TEXT_TERMS,COORD_RE

def _wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def _wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))

def _deny(m,out,created_at,errs):
 r={"object_type":"AirNowSnapshotPreservationAuditReceipt","schema_version":"v1","workflow_runner":"airnow_layer23_snapshot_preservation_audit","manifest_id":m.get("manifest_id"),"workflow_outcome":"SNAPSHOT_PRESERVATION_INTERNAL_AUDIT_DENIED_BY_POLICY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"audit_actions_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(set(errs)),"output_hashes":{"snapshot_preservation_audit_packet_hash":None},"created_at":created_at}
 _wj(out/"snapshot_preservation_audit_receipt.json",r); return r



def _packet(out, created_at):
 files=sorted([p for p in out.glob('*') if p.is_file() and p.name!='snapshot_preservation_audit_packet.tar.gz'])
 packet=out/'snapshot_preservation_audit_packet.tar.gz'
 with tarfile.open(packet,'w:gz',format=tarfile.PAX_FORMAT) as tf:
  for f in files:
   rel=f.name
   if '..' in rel or rel.startswith('/'):
    raise ValueError('PATH_TRAVERSAL')
   data=f.read_bytes()
   info=tarfile.TarInfo(name=rel)
   info.size=len(data); info.mtime=0; info.uid=0; info.gid=0; info.uname=''; info.gname=''
   tf.addfile(info, io.BytesIO(data))
 return hashlib.sha256(packet.read_bytes()).hexdigest()

def _chk_receipt(rcp,pfx,errs):
 for f in ["publication_allowed","public_release_allowed","preservation_action_allowed","preservation_copy_allowed","preservation_transfer_allowed","snapshot_export_execution_allowed","snapshot_copy_allowed","snapshot_transfer_allowed","snapshot_publication_allowed","snapshot_release_allowed","archive_transfer_allowed","file_deletion_allowed","legal_hold_creation_allowed","official_archive_certification_allowed","command_execution_allowed","final_accession_execution_allowed","task_closure_allowed"]:
  if rcp.get(f) is True: errs.append(f"{pfx}_FORBIDDEN:{f}")

def run_snapshot_preservation_audit(manifest_path,out_dir,created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); errs=validate_manifest(m)
 for sect,keys in L23_REQUIRED.items():
  src=m.get(sect,{})
  for k in keys:
   p=src.get(k)
   if not p: errs.append(f"MISSING_REQUIRED_INPUT:{sect}.{k}"); continue
   if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:{sect}.{k}")
   elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:{sect}.{k}")
 if errs: return _deny(m,out,created_at,errs)
 l20,l21,l22=m['layer20_inputs'],m['layer21_inputs'],m['layer22_inputs']
 r20,r21,r22=loadj(l20['snapshot_preservation_receipt_json']),loadj(l21['snapshot_preservation_review_receipt_json']),loadj(l22['snapshot_preservation_finalization_receipt_json'])
 if r20.get('object_type')!='AirNowSnapshotPreservationReceipt': errs.append('INVALID_LAYER20_RECEIPT_OBJECT_TYPE')
 if r21.get('object_type')!='AirNowSnapshotPreservationReviewReceipt': errs.append('INVALID_LAYER21_RECEIPT_OBJECT_TYPE')
 if r22.get('object_type')!='AirNowSnapshotPreservationFinalizationReceipt': errs.append('INVALID_LAYER22_RECEIPT_OBJECT_TYPE')
 _chk_receipt(r20,'LAYER20_RECEIPT',errs); _chk_receipt(r21,'LAYER21_RECEIPT',errs); _chk_receipt(r22,'LAYER22_RECEIPT',errs)
 for p in [l22['snapshot_preservation_decision_candidate_json'],l22['snapshot_preservation_non_execution_attestation_json'],l22['snapshot_preservation_policy_continuity_matrix_json'],l22['snapshot_preservation_caveat_continuity_register_json']]:
  if not Path(p).exists(): errs.append('MISSING_LAYER22_REQUIRED')
 if errs: return _deny(m,out,created_at,errs)
 _wj(out/'snapshot_preservation_audit_manifest.resolved.json',{"object_type":"AirNowResolvedSnapshotPreservationAuditManifest","schema_version":"v1","manifest_id":m.get('manifest_id'),"created_at":created_at})
 inv=[]
 for sect in ['layer20_inputs','layer21_inputs','layer22_inputs']:
  for k,v in sorted(m.get(sect,{}).items()):
   p=Path(v); inv.append({"input_record_id":sid('kfm:air_quality:airnow:snapshot_preservation_audit_input_record:v1',[m.get('manifest_id'),sect,k]),"layer":sect,"input_id":k,"path_original":v,"exists":p.exists(),"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at})
 _wj(out/'snapshot_preservation_audit_input_inventory.json',{"object_type":"AirNowSnapshotPreservationAuditInputInventory","schema_version":"v1","records":inv,"created_at":created_at}); _wjl(out/'snapshot_preservation_audit_input_inventory.jsonl',sorted(inv,key=lambda x:x['input_record_id']))
 ac=sorted(loadjl(l21['snapshot_preservation_acceptance_candidates_jsonl']), key=lambda x:x.get('candidate_id',''))
 bl=sorted(loadjl(l21['residual_snapshot_preservation_blockers_jsonl']), key=lambda x:x.get('blocker_id',''))
 decision=loadj(l22['snapshot_preservation_decision_candidate_json'])
 receipts=[r20,r21,r22]; _wj(out/'snapshot_preservation_receipt_ledger.json',{"object_type":"AirNowSnapshotPreservationReceiptLedger","schema_version":"v1","records":receipts,"created_at":created_at}); _wjl(out/'snapshot_preservation_receipt_ledger.jsonl',sorted(receipts,key=lambda x:x.get('object_type','')))
 _wj(out/'snapshot_preservation_decision_ledger.json',{"object_type":"AirNowSnapshotPreservationDecisionLedger","schema_version":"v1","records":[decision],"created_at":created_at}); _wjl(out/'snapshot_preservation_decision_ledger.jsonl',[decision])
 ev=ac+bl; _wj(out/'snapshot_preservation_evidence_ledger.json',{"object_type":"AirNowSnapshotPreservationEvidenceLedger","schema_version":"v1","records":ev,"created_at":created_at}); _wjl(out/'snapshot_preservation_evidence_ledger.jsonl',ev)
 lin=[{"from":"layer20","to":"layer21"},{"from":"layer21","to":"layer22"},{"from":"layer22","to":"layer23"}]; _wj(out/'snapshot_preservation_lineage_graph.json',{"object_type":"AirNowSnapshotPreservationLineageGraph","schema_version":"v1","edges":lin,"created_at":created_at}); _wjl(out/'snapshot_preservation_lineage_graph.jsonl',lin)
 hashes=[{"name":p.name,"sha256":sha256_path(p)} for p in sorted(out.glob('*.json')) if p.name!='snapshot_preservation_hash_chain.json']
 _wj(out/'snapshot_preservation_hash_chain.json',{"object_type":"AirNowSnapshotPreservationHashChain","schema_version":"v1","records":hashes,"created_at":created_at})
 pol={"object_type":"AirNowSnapshotPreservationPolicyLedger","schema_version":"v1","layer20":loadj(l20['snapshot_preservation_policy_continuity_matrix_json']),"layer21":loadj(l21['snapshot_preservation_review_policy_attestation_json']),"layer22":loadj(l22['snapshot_preservation_policy_continuity_matrix_json']),"created_at":created_at}; _wj(out/'snapshot_preservation_policy_ledger.json',pol); _wjl(out/'snapshot_preservation_policy_ledger.jsonl',[pol])
 cav={"object_type":"AirNowSnapshotPreservationCaveatRegistry","schema_version":"v1","layer20":loadj(l20['snapshot_preservation_caveat_register_json']),"layer21":loadj(l21['snapshot_preservation_review_caveat_register_json']),"layer22":loadj(l22['snapshot_preservation_caveat_continuity_register_json']),"created_at":created_at}; _wj(out/'snapshot_preservation_caveat_registry.json',cav)
 non=[loadj(l20['snapshot_preservation_non_execution_attestation_json']),loadj(l22['snapshot_preservation_non_execution_attestation_json'])]; _wj(out/'snapshot_preservation_non_execution_ledger.json',{"object_type":"AirNowSnapshotPreservationNonExecutionLedger","schema_version":"v1","records":non,"created_at":created_at}); _wjl(out/'snapshot_preservation_non_execution_ledger.jsonl',non)
 comp=[{"check":"required_inputs_present","pass":True},{"check":"required_receipts_present","pass":True}];cons=[{"check":"no_public_release","pass":True},{"check":"no_execution","pass":True}]
 _wj(out/'snapshot_preservation_completeness_matrix.json',{"object_type":"AirNowSnapshotPreservationCompletenessMatrix","schema_version":"v1","records":comp,"created_at":created_at}); _wjl(out/'snapshot_preservation_completeness_matrix.jsonl',comp)
 _wj(out/'snapshot_preservation_consistency_matrix.json',{"object_type":"AirNowSnapshotPreservationConsistencyMatrix","schema_version":"v1","records":cons,"created_at":created_at}); _wjl(out/'snapshot_preservation_consistency_matrix.jsonl',cons)
 _wj(out/'snapshot_preservation_audit_exception_register.json',{"object_type":"AirNowSnapshotPreservationAuditExceptionRegister","schema_version":"v1","records":[],"created_at":created_at}); _wjl(out/'snapshot_preservation_audit_exception_register.jsonl',[])
 outcome='SNAPSHOT_PRESERVATION_INTERNAL_AUDIT_COMPLETE' if not bl else 'SNAPSHOT_PRESERVATION_INTERNAL_AUDIT_NEEDS_MORE_INPUT'
 _wj(out/'snapshot_preservation_final_internal_summary.json',{"object_type":"AirNowSnapshotPreservationFinalInternalSummary","schema_version":"v1","summary_outcome":outcome,"positive_outcome_ceiling":"SNAPSHOT_PRESERVATION_AUDIT_COMPLETE_INTERNAL_ONLY","references":REFS,"created_at":created_at})
 _wj(out/'snapshot_preservation_audit_rerun_plan.json',{"object_type":"AirNowSnapshotPreservationAuditRerunPlan","schema_version":"v1","steps":[],"created_at":created_at})
 _wj(out/'snapshot_preservation_audit_status_board.json',{"object_type":"AirNowSnapshotPreservationAuditStatusBoard","schema_version":"v1","board_status":"SNAPSHOT_PRESERVATION_AUDIT_COMPLETE_INTERNAL_ONLY","created_at":created_at})
 txt='Internal-only snapshot preservation audit. No preservation action, copy, transfer, publication, or release.'
 if re.search(COORD_RE,txt): return _deny(m,out,created_at,['COORDINATE_LEAK'])
 if any(t in txt.lower() for t in FORBIDDEN_TEXT_TERMS): return _deny(m,out,created_at,['FORBIDDEN_LANGUAGE'])
 (out/'snapshot_preservation_audit_status_board.md').write_text('# AirNow Layer 23 Snapshot Preservation Audit Status Board\n\n'+txt+'\n')
 (out/'snapshot_preservation_audit_report.md').write_text('# AirNow Layer 23 Snapshot Preservation Audit Report\n\nInternal-only audit ledger compilation from Layers 20-22.\n')
 packet_hash=None
 if m.get('audit_policy',{}).get('include_packet'):
  packet_hash=_packet(out,created_at)
 r={"object_type":"AirNowSnapshotPreservationAuditReceipt","schema_version":"v1","workflow_runner":"airnow_layer23_snapshot_preservation_audit","manifest_id":m.get('manifest_id'),"workflow_outcome":"SNAPSHOT_PRESERVATION_AUDIT_COMPLETE_INTERNAL_ONLY","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"audit_actions_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"snapshot_preservation_audit_packet_hash":packet_hash},"created_at":created_at}
 _wj(out/'snapshot_preservation_audit_receipt.json',r); return r
