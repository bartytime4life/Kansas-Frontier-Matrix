import json
from copy import deepcopy
from datetime import datetime, timedelta, timezone

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from tests.domains.hydrology.test_usgs_water_normalizer import acquired, FixtureTransport, ROOT, Clock, START, END
from connectors.usgs.water_data.pilot_capture import capture
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.validate import validate_candidate
from tools.generators.telemetry import water_operational_receipt as telemetry
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


def test_operational_code_ref_tracks_telemetry_producer_bytes(monkeypatch, tmp_path):
    for name in telemetry.BUILD_FILES:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b'original')
    monkeypatch.setattr(telemetry, 'ROOT', tmp_path)
    before = telemetry.build_identity()
    (tmp_path / 'tools/generators/telemetry/water_operational_receipt.py').write_bytes(b'changed')
    assert telemetry.build_identity() != before


def test_complete_capture_uses_each_station_success_attempt_time(tmp_path):
    class AdvancingClock(Clock):
        tick = 0

        def now(self):
            result = datetime(2026, 9, 30, 18, 1, tzinfo=timezone.utc) + timedelta(seconds=self.tick)
            self.tick += 1
            return result

    source = capture(START, END, transport=FixtureTransport(), clock=AdvancingClock())
    candidate = normalize_capture(source.manifest, source.objects)
    completion_time = source.manifest['captured_at']
    station_times = []
    for station_id in ('USGS-06892518', 'USGS-07156900'):
        expected = max(item['observed_at'] for item in source.manifest['attempts']
                       if item['station_id'] == station_id and item['outcome'] == 'SUCCESS')
        health = source_health(source.manifest, candidate, station_id=station_id)
        assert health['last_success_at'] == expected
        assert health['probed_at'] == completion_time
        assert validate_payload(health).ok
        station_times.append(expected)
    assert station_times[0] < station_times[1] < completion_time
    root = tmp_path / 'store'
    init_store(root)
    assert stage(root, source)['outcome'] == 'CANDIDATE_READY'
    stored = [json.loads(path.read_text()) for path in root.glob(
        'data/receipts/ingest/usgs-nwis/*/health/*.json')]
    assert {item['source_id']: item['last_success_at'] for item in stored} == {
        f'usgs-nwis:{station_id}': last_success
        for station_id, last_success in zip(
            ('USGS-06892518', 'USGS-07156900'), station_times)
    }


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
    ([{'outcome': 'SUCCESS'}], 'SUCCESS', 'CAPTURE_INCOMPLETE'),
])
def test_failed_capture_health_uses_recorded_attempt_class(attempts, expected, reason):
    manifest = deepcopy(acquired().manifest)
    manifest['complete'] = False
    manifest['attempts'] = [dict(item, station_id='USGS-06892518', observed_at=manifest['captured_at']) for item in attempts]
    health = source_health(manifest, None, station_id='USGS-06892518')
    assert health['result_class'] == expected
    assert health['health_outcome'] == ('UNKNOWN' if expected == 'SUCCESS' else 'UNAVAILABLE')
    assert (health['last_success_at'] is not None) == any(item['outcome'] == 'SUCCESS' for item in attempts)
    assert ('NO_PRIOR_SUCCESS' in health['reasons']) == all(item['outcome'] != 'SUCCESS' for item in attempts)
    if reason:
        assert reason in health['reasons']
    else:
        assert 'SCHEMA_OR_PARSE_FAILURE' not in health['reasons']
    assert validate_payload(health).outcome == ('ABSTAIN' if expected == 'SUCCESS' else 'PASS')


def test_second_station_failure_does_not_mislabel_first_station(tmp_path):
    class MixedTransport(FixtureTransport):
        def send(self, request, **options):
            if '07156900' in request.url:
                raise TimeoutError
            return super().send(request, **options)

    source = capture(START, END, transport=MixedTransport(), clock=Clock())
    assert source.manifest['complete'] is False
    assert [item['outcome'] for item in source.manifest['attempts'] if item['station_id'] == 'USGS-06892518'] == ['SUCCESS', 'SUCCESS']
    first = source_health(source.manifest, None, station_id='USGS-06892518')
    second = source_health(source.manifest, None, station_id='USGS-07156900')
    assert (first['result_class'], first['health_outcome'], first['reasons']) == ('SUCCESS', 'UNKNOWN', ['CAPTURE_INCOMPLETE'])
    assert first['last_success_at'] is not None
    assert (second['result_class'], second['health_outcome']) == ('TIMEOUT', 'UNAVAILABLE')
    assert second['last_success_at'] is None
    assert validate_payload(first).outcome == 'ABSTAIN'
    assert validate_payload(second).ok
    root = tmp_path / 'store'
    init_store(root)
    assert stage(root, source)['outcome'] == 'QUARANTINED'
    receipts = [json.loads(path.read_text()) for path in root.glob('data/receipts/ingest/usgs-nwis/*/health/*.json')]
    assert {item['source_id']: item['result_class'] for item in receipts} == {
        'usgs-nwis:USGS-06892518': 'SUCCESS', 'usgs-nwis:USGS-07156900': 'TIMEOUT'}


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
    assert {json.loads(path.read_text())['result_class'] for path in receipts} == {'TIMEOUT', 'NOT_PROBED'}
