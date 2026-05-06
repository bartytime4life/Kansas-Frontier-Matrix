from .ids import make_id

def make_quarantine(manifest,row_number,reason_code,reason_detail,raw_record,created_at,source_record_hash=""):
    seed={"m":manifest.get("manifest_id"),"p":manifest.get("product_type"),"r":row_number,"c":reason_code,"h":source_record_hash}
    return {"object_type":"AirNowFileProductQuarantineRecord","schema_version":"v1","quarantine_id":make_id("kfm:air_quality:airnow:file_product:quarantine:v1",seed),"source_id":"airnow","product_type":manifest.get("product_type"),"manifest_id":manifest.get("manifest_id"),"source_record_hash":source_record_hash,"row_number":row_number,"reason_code":reason_code,"reason_detail":reason_detail,"finite_outcome":"ABSTAIN","publication_allowed":False,"emergency_alert":False,"raw_record":raw_record,"created_at":created_at}
