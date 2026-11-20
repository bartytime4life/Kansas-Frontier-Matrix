"""NWS supplied-capture orchestration with explicit context, expiry and privacy proof."""
import copy
import json
import os
from pathlib import Path
import socket
import subprocess
import sys

import pytest
from pipelines.domains.hazards import nws_context_ingest as m


def packet(name='lineage'):
    return json.loads((m.FIXTURE_ROOT / (name + '.json')).read_text())


def prepare(body=None, *, name='lineage', **kw):
    p = packet(name)
    return m.prepare_capture(p['body'].encode() if body is None else body,
        retrieved_at=kw.pop('retrieved_at', p['retrieved_at']), as_of=kw.pop('as_of', p['as_of']), **kw)


@pytest.mark.parametrize('name', ['lineage', 'expired-partial', 'empty'])
def test_full_golden_context_and_denied_authority(name):
    p = packet(name)
    result = m.replay_packet((m.FIXTURE_ROOT/(name+'.json')).read_bytes())
    assert result.candidate == p['expected']
    assert result.candidate['context']['coverage'] == 'NOT_ESTABLISHED'
    assert result.summary()['outcome'] == 'HOLD'
    assert not any(result.candidate['authority'].values())
    assert 'INSTRUCTION' not in repr(result)


def test_source_faithful_instruction_and_unknown_fields_remain_private():
    c = prepare().candidate
    a = c['context']['alerts'][0]
    assert a['has_instruction'] is True
    assert 'SYNTHETIC SOURCE INSTRUCTION' in a['raw_feature_json']
    assert json.loads(a['raw_feature_json'])['properties']['unknown_field'] == {'preserved': True}
    assert 'instruction' not in a
    assert 'INSTRUCTION' not in json.dumps(prepare().summary())
    assert a['authority'] == 'NWS_ISSUED_CONTEXT_ONLY'
    assert a['life_safety_authority'] is False


def test_lineage_freshness_and_later_replay_never_become_current_claims():
    c = prepare().candidate
    assert [a['freshness_state'] for a in c['context']['alerts']] == [
        'SUPERSEDED_IN_COLLECTION', 'WITHIN_SOURCE_WINDOW_AT_AS_OF']
    later = prepare(as_of='2026-01-02T00:00:00Z').candidate
    assert [a['freshness_state'] for a in later['context']['alerts']] == ['SUPERSEDED_IN_COLLECTION', 'EXPIRED']
    assert c['candidate_id'] == later['candidate_id']
    assert c['spec_hash'] != later['spec_hash']
    assert 'CURRENT' not in json.dumps(later).upper()


def test_partial_capture_and_empty_are_not_absence_or_complete_coverage():
    partial = prepare(name='expired-partial')
    assert partial.summary()['capture_outcome'] == 'INCOMPLETE_CAPTURE'
    assert partial.summary()['quarantined'] == 1
    assert partial.summary()['freshness_counts'] == {'EXPIRED': 1}
    empty = prepare(name='empty')
    assert empty.summary()['message_count'] == 0
    assert empty.candidate['context']['coverage'] == 'NOT_ESTABLISHED'
    assert empty.summary()['outcome'] == 'HOLD'


def test_capture_timezone_normalizes_and_raw_byte_identity_is_separate():
    assert prepare(retrieved_at='2026-01-01T06:00:00-06:00', as_of='2026-01-01T06:00:00-06:00') == prepare()
    body = json.dumps(json.loads(packet()['body']), indent=2).encode()
    c = prepare(body).candidate
    assert c['context']['alerts'] == prepare().candidate['context']['alerts']
    assert c['candidate_id'] != prepare().candidate['candidate_id']


@pytest.mark.parametrize('status', [304,429,503,True,'200'])
def test_non200_responses_refused_without_fake_capture(status):
    with pytest.raises(ValueError, match='HTTP_STATUS'): prepare(status=status)


@pytest.mark.parametrize('bad', [b'', b'{"features":[],"features":[]}', b'{"x":NaN}',
    b'{"x":1e999}', b'[]', b'a'*(m.MAX_SOURCE+1), b'not-json'])
def test_malformed_or_oversized_captures_refused(bad):
    with pytest.raises(ValueError): prepare(bad)


def test_deep_and_too_many_features_refused():
    body = json.loads(packet()['body'])
    body['features'] *= m.MAX_FEATURES
    with pytest.raises(ValueError): prepare(m.canonical_bytes(body))
    with pytest.raises(ValueError): prepare(('{'+'"deep":'+'['*40+'0'+']'*40+'}').encode())


@pytest.mark.parametrize('kw', [{'as_of':'2025-12-31T00:00:00Z'}, {'as_of':'2026-01-01'},
    {'retrieved_at':'2025-12-31T00:00:00Z','as_of':'2026-01-01T12:00:00Z'}])
def test_invalid_time_and_future_source_message_refused(kw):
    with pytest.raises(ValueError): prepare(**kw)


def test_missing_lineage_duplicate_ids_and_wrong_area_are_explicit():
    b = json.loads(packet()['body'])
    b['features'][1]['properties']['references'] = []
    c = prepare(m.canonical_bytes(b)).candidate
    assert 'LINEAGE_REFERENCE_MISSING' in c['context']['alerts'][1]['reasons']
    assert 'MESSAGE_QUARANTINE_CANDIDATES' in c['reason_codes']
    b['features'][1] = copy.deepcopy(b['features'][0])
    with pytest.raises(ValueError): prepare(m.canonical_bytes(b))
    b['features'] = b['features'][:1]
    b['features'][0]['properties']['geocode']['UGC'] = ['OKZ001']
    assert 'OUTSIDE_REQUESTED_AREA' in prepare(m.canonical_bytes(b)).candidate['context']['alerts'][0]['reasons']


@pytest.mark.parametrize('key,value', [('body_sha256','sha256:'+'0'*64),('body','{}'),
    ('fixture_kind','PROVIDER_CAPTURE'),('extra',True),('expected',{})])
def test_packet_tamper_refused(key,value):
    p = packet();p[key] = value
    with pytest.raises(ValueError): m.replay_packet(m.canonical_bytes(p))


def test_schema_hash_and_rehashed_projection_drift_refused():
    mutations=[lambda c: c['authority'].update(alert_delivery_authorized=True),
        lambda c: c['context']['alerts'][0].update(freshness_state='WITHIN_SOURCE_WINDOW_AT_AS_OF'),
        lambda c: c['context']['alerts'][0].update(raw_feature_json='{}'),
        lambda c: c['context'].update(coverage='COMPLETE'),
        lambda c: c.update(extra=True),
        lambda c: c.update(reason_codes=[])]
    for mutate in mutations:
        c = copy.deepcopy(prepare().candidate);mutate(c);c['spec_hash'] = m.spec_hash(c)
        with pytest.raises(ValueError): m.validate_candidate(c)
    result = prepare();result.candidate['authority']['public_use_allowed'] = True
    with pytest.raises(ValueError): result.summary()


def test_no_socket_or_pagination_following(monkeypatch):
    def denied(*a, **kw): raise AssertionError('NETWORK_FORBIDDEN')
    monkeypatch.setattr(socket,'socket',denied)
    monkeypatch.setattr(socket,'create_connection',denied)
    prepare(name='expired-partial')


@pytest.mark.parametrize('name', ['lineage','expired-partial','empty'])
def test_cli_is_aggregate_only_and_has_no_filesystem_writes(name,tmp_path):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', KFM_NO_NETWORK='1')
    env['PYTHONPATH'] = os.pathsep.join([str(m.ROOT/'tools/ci/kfm_no_network'),str(m.ROOT),
        str(m.ROOT/'packages/connectors-core/src'),env.get('PYTHONPATH','')])
    p = subprocess.run([sys.executable,'-B','-m',m.__name__,name],cwd=tmp_path,env=env,
                       capture_output=True,text=True,check=True)
    summary = json.loads(p.stdout)
    assert summary['outcome'] == 'HOLD' and summary['alert_delivery_authorized'] is False
    assert all(t not in p.stdout for t in ['urn:oid','INSTRUCTION','synthetic.invalid','KSZ001','next','http'])
    assert list(tmp_path.iterdir()) == [] and p.stderr == ''
