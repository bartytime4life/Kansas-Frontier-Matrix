"""Supplied OpenFEMA walk integrity, partial capture, administrative role and privacy."""
import copy
import json
import os
import socket
import subprocess
import sys

import pytest
from pipelines.domains.hazards import openfema_ingest as m


def packet(case='complete'):
    return json.loads((m.FIXTURE_ROOT/(case+'.json')).read_text())


def envelope(case='complete'):
    return json.loads(packet(case)['capture'])


def prepare(e=None):
    return m.prepare_capture(m.canonical_bytes(envelope() if e is None else e))


def change_body(e,index,mutate):
    b=json.loads(e['pages'][index]['body']);mutate(b);e['pages'][index]['body']=m.canonical_bytes(b).decode()


@pytest.mark.parametrize('case,kind,count',[('complete','CAPTURE_CANDIDATE',3),
    ('count-drift','INCOMPLETE_CAPTURE',3),('empty','CAPTURE_CANDIDATE',0)])
def test_full_golden_and_finite_holds(case,kind,count):
    result=m.replay_packet((m.FIXTURE_ROOT/(case+'.json')).read_bytes())
    assert result.candidate == packet(case)['expected']
    assert result.summary()['capture_outcome'] == kind
    assert result.summary()['record_count'] == count
    assert result.summary()['outcome'] == 'HOLD'
    assert result.candidate['capture']['coverage'] == 'NOT_ESTABLISHED'
    assert not any(result.candidate['authority'].values())
    assert 'DESIGNATION' not in repr(result)


def test_private_admin_context_preserves_distinct_times_flags_and_source_fields():
    c=prepare().candidate
    a,b,z=c['capture']['records']
    assert c['source_role']=='administrative'
    assert a['geography_semantics']=='DESIGNATED_JURISDICTION_NOT_HAZARD_FOOTPRINT'
    assert a['incident_end_date'] is None and 'INCIDENT_END_UNSET' in a['reasons']
    assert a['declaration_date']=='2020-05-01T00:00:00.123000Z'
    assert a['last_refresh']=='2026-01-01T00:00:00.789000Z'
    assert c['pages'][0]['retrieved_at']=='2026-09-27T12:00:00.123000Z'
    assert z['route']=='QUARANTINE_CANDIDATE'
    assert 'SCHEMA_DRIFT_ADDITIONAL_FIELD' in z['reasons']
    assert json.loads(z['raw_record_json'])['newSyntheticField']=={'retained':True}
    assert prepare().summary()['flagged']==2 and prepare().summary()['quarantined']==1


def test_reordering_input_pages_preserves_complete_candidate():
    e=envelope();e['pages'].reverse()
    assert prepare(e)==prepare()


def test_exact_byte_identity_is_separate_from_capture_time():
    e=envelope();e['pages'][0]['retrieved_at']='2026-09-27T07:00:00.123-05:00'
    assert prepare(e)==prepare()
    e['pages'][1]['retrieved_at']='2026-09-27T12:00:01Z'
    later=prepare(e).candidate;c=prepare().candidate
    assert later['candidate_id']==c['candidate_id'] and later['spec_hash']!=c['spec_hash']
    e=envelope();e['pages'][0]['body']=json.dumps(json.loads(e['pages'][0]['body']),indent=2)
    reformatted=prepare(e).candidate
    assert reformatted['capture']['records']==c['capture']['records']
    assert reformatted['candidate_id']!=c['candidate_id']


def test_walk_requires_terminal_short_page_even_when_count_matches():
    e=envelope();e['pages']=e['pages'][:1]
    change_body(e,0,lambda b:b['metadata'].update(count=2))
    assert 'END_NOT_REACHED' in prepare(e).candidate['capture']['reasons']
    last=copy.deepcopy(envelope('empty')['pages'][0]);last['retrieved_at']=e['pages'][0]['retrieved_at']
    cursor=json.loads(e['pages'][0]['body'])[m.of.ENTITY][-1]['id']
    last['source_url']=m.of.page_url(m.of.declaration_filter(),after_id=cursor,top=2)
    b=json.loads(last['body']);b['metadata']['filter']=m.of.declaration_filter()+f" and id gt '{cursor}'";last['body']=m.canonical_bytes(b).decode()
    e['pages'].append(last)
    assert prepare(e).candidate['capture']['outcome']=='CAPTURE_CANDIDATE'


def test_count_drift_and_cursor_gap_remain_incomplete():
    assert 'COUNT_DRIFT' in m.replay_packet((m.FIXTURE_ROOT/'count-drift.json').read_bytes()).candidate['capture']['reasons']
    e=envelope();e['pages']=e['pages'][1:]
    assert 'CURSOR_NOT_FROM_START' in prepare(e).candidate['capture']['reasons']
    e=envelope();p=e['pages'][1];bad='00000000-0000-4000-8000-000000000001'
    p['source_url']=m.of.page_url(m.of.declaration_filter(),after_id=bad,top=2)
    change_body(e,1,lambda b:b['metadata'].update(filter=m.of.declaration_filter()+f" and id gt '{bad}'"))
    assert 'CURSOR_GAP_OR_OVERLAP' in prepare(e).candidate['capture']['reasons']


@pytest.mark.parametrize('status',[304,429,503,True,'200'])
def test_non200_and_noninteger_http_status_refused(status):
    e=envelope();e['pages'][0]['status']=status
    with pytest.raises(ValueError):prepare(e)


@pytest.mark.parametrize('bad',[b'',b'[]',b'{"pages":[],"pages":[]}',b'{"pages":NaN}',
    b'{"pages":1e999}',b'a'*(m.MAX_ENVELOPE+1)])
def test_bad_capture_json_and_envelope_bounds(bad):
    with pytest.raises(ValueError):m.prepare_capture(bad)


def test_page_count_size_and_combined_byte_bounds():
    for e in [{'pages':[]},{'pages':envelope()['pages']*(m.MAX_PAGES+1)}]:
        with pytest.raises(ValueError):prepare(e)
    e=envelope();e['pages'][0]['body']='x'*(m.MAX_PAGE+1)
    with pytest.raises(ValueError):prepare(e)
    # Use valid empty, uniquely cursored pages with inert metadata padding, so
    # aggregate bytes rather than parser failure hits the total capture bound.
    pages=[]
    for n in range(6):
        p=copy.deepcopy(envelope('empty')['pages'][0]);cursor=f'00000000-0000-4000-8000-{n:012d}'
        p['source_url']=m.of.page_url(m.of.declaration_filter(),after_id=cursor,top=2)
        b=json.loads(p['body']);b['metadata']['filter']=m.of.declaration_filter()+f" and id gt '{cursor}'";b['padding']='x'*200000;p['body']=m.canonical_bytes(b).decode();pages.append(p)
    with pytest.raises(ValueError,match='CAPTURE_BYTE_BOUND'):prepare({'pages':pages})


def test_record_count_and_page_size_profiles():
    e=envelope('empty');p=e['pages'][0]
    p['source_url']=m.of.page_url(m.of.declaration_filter(),top=m.MAX_TOP+1)
    change_body(e,0,lambda b:b['metadata'].update(top=m.MAX_TOP+1))
    with pytest.raises(ValueError,match='QUERY_PROFILE_BOUND'):prepare(e)
    e=envelope('empty');change_body(e,0,lambda b:b['metadata'].update(count=m.MAX_REPORTED+1))
    with pytest.raises(ValueError,match='QUERY_PROFILE_BOUND'):prepare(e)
    # A real parsed five-page sequence (257 rows) must fail, not truncate.
    template=json.loads(envelope()['pages'][0]['body'])[m.of.ENTITY][1];pages=[];cursor=None
    for start,size in [(1,64),(65,64),(129,64),(193,64),(257,1)]:
        p=copy.deepcopy(envelope('empty')['pages'][0]);p['source_url']=m.of.page_url(m.of.declaration_filter(),after_id=cursor,top=64)
        rows=[]
        for i in range(start,start+size):
            r=copy.deepcopy(template);r['id']=f'00000000-0000-4000-8000-{i:012d}';rows.append(r)
        b=json.loads(p['body']);b['metadata'].update(top=64,count=258-start,filter=m.of.declaration_filter()+(f" and id gt '{cursor}'" if cursor else ''));b[m.of.ENTITY]=rows;p['body']=m.canonical_bytes(b).decode();pages.append(p);cursor=rows[-1]['id']
    with pytest.raises(ValueError,match='RECORD_COUNT_BOUND'):prepare({'pages':pages})


def test_duplicate_page_requests_noncanonical_urls_and_mixed_queries_refused():
    e=envelope();e['pages'].append(copy.deepcopy(e['pages'][0]))
    with pytest.raises(ValueError,match='DUPLICATE_PAGE'):prepare(e)
    e=envelope();e['pages'][0]['source_url']+='&api_key=secret-marker'
    with pytest.raises(ValueError):prepare(e)
    e=envelope();p=e['pages'][1];cursor=json.loads(p['body'])['metadata']['filter'].split("'")[-2]
    p['source_url']=m.of.page_url(m.of.declaration_filter(),after_id=cursor,top=3)
    change_body(e,1,lambda b:b['metadata'].update(top=3))
    with pytest.raises(ValueError,match='MIXED_QUERY'):prepare(e)


def test_bad_metadata_state_and_record_order_are_refused():
    for key,value in [('top',True),('skip',False)]:
        e=envelope();change_body(e,0,lambda b:b['metadata'].update({key:value}))
        with pytest.raises(ValueError):prepare(e)
    e=envelope();change_body(e,0,lambda b:b[m.of.ENTITY][0].update(state='OK',fipsStateCode='40'))
    with pytest.raises(ValueError):prepare(e)
    e=envelope();change_body(e,0,lambda b:b[m.of.ENTITY].reverse())
    with pytest.raises(ValueError):prepare(e)


def test_temporal_inconsistency_is_not_silently_normalized():
    e=envelope();e['pages'][1]['retrieved_at']='2026-09-27T12:00:00Z'
    with pytest.raises(ValueError,match='CAPTURE_TIME_ORDER'):prepare(e)
    e=envelope();change_body(e,0,lambda b:b['metadata'].update(rundate='2027-01-01T00:00:00Z'))
    with pytest.raises(ValueError,match='SOURCE_TIME_AFTER_CAPTURE'):prepare(e)
    e=envelope();change_body(e,0,lambda b:b[m.of.ENTITY][0].update(lastRefresh='2027-01-01T00:00:00Z'))
    with pytest.raises(ValueError,match='SOURCE_TIME_AFTER_CAPTURE'):prepare(e)


@pytest.mark.parametrize('key,value',[('fixture_kind','PROVIDER_DATA'),('capture','{}'),
    ('capture_sha256','sha256:'+'0'*64),('expected',{}),('extra',True)])
def test_packet_tamper_refused(key,value):
    p=packet();p[key]=value
    with pytest.raises(ValueError):m.replay_packet(m.canonical_bytes(p))


def test_full_replay_rejects_rehashed_role_count_hash_or_authority_drift():
    for mutate in [lambda c:c['authority'].update(eligibility_determination_authorized=True),
        lambda c:c['capture'].update(outcome='INCOMPLETE_CAPTURE'),
        lambda c:c['capture']['records'][0].update(source_role='observed'),
        lambda c:c['pages'][0].update(body_sha256='sha256:'+'0'*64),
        lambda c:c['capture']['records'][0].update(designated_area='rewritten'),
        lambda c:c.update(candidate_id='openfema-ingest:sha256:'+'0'*64),
        lambda c:c.update(reason_codes=[]),lambda c:c.update(extra=True)]:
        c=copy.deepcopy(prepare().candidate);mutate(c);c['spec_hash']=m.spec_hash(c)
        with pytest.raises(ValueError):m.validate_candidate(c)
    result=prepare();result.candidate['authority']['public_use_allowed']=True
    with pytest.raises(ValueError):result.summary()


def test_no_socket_or_page_fetch_effects(monkeypatch):
    def denied(*a,**kw):raise AssertionError('NETWORK_FORBIDDEN')
    monkeypatch.setattr(socket,'socket',denied);monkeypatch.setattr(socket,'create_connection',denied)
    prepare()


@pytest.mark.parametrize('case',['complete','count-drift','empty'])
def test_cli_is_aggregate_only_and_writes_no_files(case,tmp_path):
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',KFM_NO_NETWORK='1')
    env['PYTHONPATH']=os.pathsep.join([str(m.ROOT/'tools/ci/kfm_no_network'),str(m.ROOT),str(m.ROOT/'packages/connectors-core/src'),env.get('PYTHONPATH','')])
    p=subprocess.run([sys.executable,'-B','-m',m.__name__,case],cwd=tmp_path,env=env,text=True,capture_output=True,check=True)
    s=json.loads(p.stdout);assert s['outcome']=='HOLD' and s['eligibility_determination_authorized'] is False
    assert all(t not in p.stdout for t in ['SYNTHETIC','9001','fema.gov','County','00000000','designatedArea'])
    assert list(tmp_path.iterdir())==[] and p.stderr==''
