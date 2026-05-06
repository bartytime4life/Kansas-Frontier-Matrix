from .ids import make_id, sha256_text

def build_receipt(manifest, created_at, in_count, parsed, quarantined, warnings=None, errors=None, validation_outcome='PASS', finite_outcome='ABSTAIN'):
    warnings=warnings or []; errors=errors or []
    parsed_blob='\n'.join(parsed)
    quar_blob='\n'.join(quarantined)
    base={"object_type":"AirNowFileProductParseReceipt","schema_version":"v1","source_id":"airnow","product_type":manifest.get('product_type'),"manifest_id":manifest.get('manifest_id'),"parser":"airnow_layer3_file_products","parser_version":"v1","input_file":manifest.get('input_file'),"input_record_count":in_count,"parsed_record_count":len(parsed),"quarantined_record_count":len(quarantined),"warnings":warnings,"errors":errors,"validation_outcome":validation_outcome,"finite_outcome":finite_outcome,"input_hash":sha256_text(str(manifest.get('input_file'))),"parsed_output_hash":sha256_text(parsed_blob),"quarantine_output_hash":sha256_text(quar_blob),"outputs":{"parsed_jsonl":"parsed_records.jsonl","quarantine_jsonl":"quarantine.jsonl"},"created_at":created_at}
    base['receipt_id']=make_id('kfm:air_quality:airnow:file_product:parse_receipt:v1',[manifest.get('manifest_id'),base['input_hash'],base['parsed_output_hash'],base['quarantine_output_hash'],created_at])
    return base
