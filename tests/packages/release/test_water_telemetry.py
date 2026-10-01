import json
from copy import deepcopy

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from tests.domains.hydrology.test_usgs_water_normalizer import acquired, ROOT, Clock, START, END
from connectors.usgs.water_data.pilot_capture import capture
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.validate import validate_candidate
from tools.generators.telemetry.water_operational_receipt import operational_receipt, source_health
from tools.local_data.manage import init_store
from tools.local_data.water_pilot import stage
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
        if value is None:
            assert health['result_class'] == 'PARSE_ERROR'
        assert validate_payload(health).ok


@pytest.mark.parametrize(('attempts', 'expected', 'reason'), [
    ([{'outcome': 'TIMEOUT'}, {'outcome': 'RETRY_EXHAUSTED'}], 'TIMEOUT', None),
    ([{'outcome': 'SUCCESS'}, {'outcome': 'RETRY_EXHAUSTED', 'code': 'RETRY_DEADLINE_REACHED'}], 'TIMEOUT', None),
    ([{'outcome': 'AUTH_REQUIRED'}], 'AUTH_ERROR', 'AUTH_FAILURE'),
    ([{'outcome': 'RATE_LIMITED'}], 'HTTP_ERROR', None),
    ([{'outcome': 'TRANSPORT_ERROR'}], 'ACQUISITION_ERROR', None),
    ([{'outcome': 'SUCCESS'}], 'ACQUISITION_ERROR', None),
])
def test_failed_capture_health_uses_recorded_attempt_class(attempts, expected, reason):
    manifest = deepcopy(acquired().manifest)
    manifest['complete'] = False
    manifest['attempts'] = attempts
    health = source_health(manifest, None, station_id='USGS-06892518')
    assert health['result_class'] == expected
    assert health['health_outcome'] == 'UNAVAILABLE'
    if reason:
        assert reason in health['reasons']
    else:
        assert 'SCHEMA_OR_PARSE_FAILURE' not in health['reasons']
    assert validate_payload(health).ok


def test_timeout_capture_persists_truthful_station_health(tmp_path):
    class TimeoutTransport:
        def send(self, _request, **_options):
            raise TimeoutError

    source = capture(START, END, transport=TimeoutTransport(), clock=Clock())
    assert source.manifest['complete'] is False
    assert source.manifest['attempts'][-1]['outcome'] == 'TIMEOUT'
    root = tmp_path / 'store'
    init_store(root)
    assert stage(root, source)['outcome'] == 'QUARANTINED'
    receipts = list(root.glob('data/receipts/ingest/usgs-nwis/*/health/*.json'))
    assert len(receipts) == 2
    assert {json.loads(path.read_text())['result_class'] for path in receipts} == {'TIMEOUT'}
