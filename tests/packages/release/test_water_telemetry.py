import json
from jsonschema import Draft202012Validator, FormatChecker
from tests.domains.hydrology.test_usgs_water_normalizer import acquired, ROOT, observation
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.validate import validate_candidate
from tools.generators.telemetry.water_operational_receipt import operational_receipt, source_health
from tools.validators.source.validate_source_health_assessment import validate_payload


def test_local_receipt_matches_existing_contract_and_has_no_sensitive_content():
    source = acquired(); candidate = normalize_capture(source.manifest, source.objects)
    receipt = operational_receipt(source.manifest, candidate, validate_candidate(candidate))
    schema = json.loads((ROOT/'schemas/contracts/v1/runtime/run_receipt.schema.json').read_text())
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(receipt)
    text = json.dumps(receipt)
    for forbidden in ('coordinates', 'SYNTHETIC TEST STATION', '/home/', 'question', 'prompt', 'Authorization'):
        assert forbidden not in text
    assert receipt['operational']['release_authorized'] is False
    assert validate_payload(source_health(source.manifest, candidate, station_id='USGS-06892518')).ok


def test_empty_and_failed_capture_never_report_healthy():
    source = acquired(lambda _records: [])
    candidate = normalize_capture(source.manifest, source.objects)
    for value in (candidate, None):
        health = source_health(source.manifest, value, station_id='USGS-06892518')
        assert health['health_outcome'] != 'HEALTHY'
        assert validate_payload(health).ok
