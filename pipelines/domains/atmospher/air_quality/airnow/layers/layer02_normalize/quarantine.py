from .ids import canonical_id

def make_quarantine(raw, rec_hash, manifest_id, reason_code, reason_detail, created_at):
    qid = canonical_id("kfm:air_quality:airnow:quarantine:v1", [rec_hash, reason_code, reason_detail])
    return {
      "object_type":"AirNowQuarantineRecord","schema_version":"v1","quarantine_id":qid,
      "source_id":"airnow","source_record_hash":rec_hash,"input_manifest_id":manifest_id,
      "reason_code":reason_code,"reason_detail":reason_detail,"finite_outcome":"ABSTAIN",
      "publication_allowed":False,"emergency_alert":False,"raw_record":raw,"created_at":created_at
    }
