import copy
import dataclasses
import importlib
import json
import pytest
from connectors.kansas.kanplan import (CaptureProfile, CaptureError, Limits, SyntheticTransport, collect,
                           metadata_fingerprint, normalized_bytes, decode, DormantReadOnlyHTTP)
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]


def fixture_data():
    m = json.loads((ROOT/'fixtures/synthetic/kanplan/state-metadata.synthetic.json').read_text())
    f = json.loads((ROOT/'fixtures/synthetic/kanplan/state-features.synthetic.json').read_text())['features']
    return m, f


def setup_capture():
    m, f = fixture_data()
    p = CaptureProfile('src:fixture-kanplan-state','Transportation/State_System/FeatureServer/0',
          metadata_fingerprint(m),(0,0,.05,.05),tuple(x['name'] for x in m['fields']),
          {'OBJECTID':'esriFieldTypeOID','RouteId':'esriFieldTypeString','Id':'esriFieldTypeString'},True)
    return p, m, f


def run(p, t, limits=Limits(chunk_size=1)):
    return collect(p,t,limits,clock=lambda:'2026-09-05T00:00:00Z',sleep=lambda _:None)


def test_imports_do_not_access_network():
    for name in ['connectors.kansas.kanplan', 'packages.geo.src.geo.esri_polyline',
                 'pipelines.normalize.roads-rail-trade.kanplan_state_system']:
        importlib.import_module(name)


def test_count_ids_and_chunks_reconcile_native_bytes():
    p,m,f=setup_capture(); t=SyntheticTransport(m,f); c=run(p,t)
    assert c.receipt['returned_count']==2 and c.receipt['requests']==8
    assert c.receipt['atomic_snapshot'] is False
    assert len(c.raw_responses)==8
    assert all(x['params'].get('objectIds') in (None,'1','2') for x in t.calls)
    assert [x['attributes']['OBJECTID'] for x in c.features]==[1,2]
    import hashlib
    assert [hashlib.sha256(b).hexdigest() for b in c.raw_responses]==[x['sha256'] for x in c.receipt['trace']]


def test_deterministic_replay_and_id_order():
    p,m,f=setup_capture()
    a=run(p,SyntheticTransport(m,f)); b=run(p,SyntheticTransport(m,list(reversed(f))))
    assert a.receipt['normalized_content_sha256']==b.receipt['normalized_content_sha256']
    assert a.features==b.features
    assert a.receipt['trace'][2]['sha256']!=b.receipt['trace'][2]['sha256']


@pytest.mark.parametrize('mutation,code',[
    (lambda m:m.update(id=1),'LAYER_ID_DRIFT'),
    (lambda m:m.update(maxRecordCount=None),'RECORD_LIMIT_MISSING'),
    (lambda m:m.update(capabilities='Extract'),'QUERY_UNAVAILABLE'),
    (lambda m:m['fields'][1].update(type='esriFieldTypeDouble'),'FIELD_TYPE_DRIFT'),
    (lambda m:m['fields'].append({'name':'KDOTUseOnly','type':'esriFieldTypeString'}),'RESTRICTIVE_FIELD_NOT_ACQUIRED'),
    (lambda m:m['extent'].update(spatialReference={'wkid':4326}),'SCHEMA_DRIFT')])
def test_metadata_drift(mutation,code):
    p,m,f=setup_capture(); mutation(m)
    with pytest.raises(CaptureError,match=code): run(p,SyntheticTransport(m,f))


@pytest.mark.parametrize('bad_id',[None,0,-1,True,1.5,2**53])
def test_invalid_object_ids(bad_id):
    p,m,f=setup_capture(); f[0]['attributes']['OBJECTID']=bad_id
    with pytest.raises(CaptureError,match='INVALID_OBJECT_ID'): run(p,SyntheticTransport(m,f))


def test_duplicate_object_ids():
    p,m,f=setup_capture(); f[1]['attributes']['OBJECTID']=1
    with pytest.raises(CaptureError,match='DUPLICATE_OBJECT_ID'): run(p,SyntheticTransport(m,f))


class Altered(SyntheticTransport):
    def __init__(self,m,f,change): super().__init__(m,f); self.change=change
    def __call__(self,url,params,**kwargs):
        data=super().__call__(url,params,**kwargs)
        value=json.loads(data)
        return normalized_bytes(self.change(value,params,len(self.calls)))


@pytest.mark.parametrize('change,code',[
    (lambda v,p,n:{**v,'exceededTransferLimit':True} if p.get('objectIds') else v,'TRANSFER_LIMIT'),
    (lambda v,p,n:{**v,'count':3} if p.get('returnCountOnly') else v,'COUNT_IDS_MISMATCH'),
    (lambda v,p,n:{**v,'features':[]} if p.get('objectIds') else v,'TRUNCATED_PAGE'),
    (lambda v,p,n:{**v,'objectIds':[1,3]} if n==7 else v,'CAPTURE_CHANGED_IDS'),
    (lambda v,p,n:{**v,'editingInfo':{'lastEditDate':1}} if n==8 else v,'CAPTURE_CHANGED_EDIT_METADATA'),
    (lambda v,p,n:{**v,'spatialReference':{'wkid':4326}} if p.get('objectIds') else v,'PAGE_CRS_DRIFT'),
    (lambda v,p,n:{**v,'hasM':False} if p.get('objectIds') else v,'PAGE_DIMENSION_DRIFT'),
    (lambda v,p,n:{'error':{'message':'secret=do-not-echo'}} if n==4 else v,'UPSTREAM_ERROR')])
def test_inconsistent_pages_and_changes(change,code):
    p,m,f=setup_capture()
    with pytest.raises(CaptureError,match=code) as e: run(p,Altered(m,f,change))
    assert 'do-not-echo' not in str(e.value)


@pytest.mark.parametrize('limits,code',[
    (Limits(max_requests=3),'REQUEST_BUDGET'),
    (Limits(max_features=1),'FEATURE_BUDGET'),
    (Limits(max_response_bytes=100),'RESPONSE_BYTE_BUDGET'),
    (Limits(max_total_bytes=1200),'RESPONSE_BYTE_BUDGET')])
def test_resource_budgets(limits,code):
    p,m,f=setup_capture()
    with pytest.raises(CaptureError,match=code): run(p,SyntheticTransport(m,f),limits)


def test_upstream_smaller_record_limit_controls_chunks():
    p,m,f=setup_capture(); m['maxRecordCount']=1
    p=dataclasses.replace(p,expected_metadata_hash=metadata_fingerprint(m))
    t=SyntheticTransport(m,f);run(p,t,Limits(chunk_size=200))
    assert [c['params']['objectIds'] for c in t.calls if 'objectIds' in c['params']]==['1','2']


def test_transient_retries_are_bounded():
    p,m,f=setup_capture()
    class Unavailable(SyntheticTransport):
        attempts=0
        def __call__(self,*args,**kwargs):
            self.attempts+=1
            raise CaptureError('HTTP_TRANSIENT')
    t=Unavailable(m,f)
    with pytest.raises(CaptureError,match='HTTP_TRANSIENT'): run(p,t,Limits(attempts=2))
    assert t.attempts==2


@pytest.mark.parametrize('payload',[b'{"a":1,"a":2}',b'{"a":NaN}',b'{"a":1e999}',b'[]',b'not json'])
def test_strict_json(payload):
    with pytest.raises(CaptureError): decode(payload,1000)


def test_no_real_source_activation_and_no_fixture_flag_bypass():
    p,m,f=setup_capture()
    with pytest.raises(CaptureError,match='ADMISSION_BINDING_REQUIRED'):
        run(dataclasses.replace(p,synthetic=False),SyntheticTransport(m,f))
    with pytest.raises(CaptureError,match='ADMISSION_BINDING_REQUIRED'):
        run(p,DormantReadOnlyHTTP())
    with pytest.raises(CaptureError,match='LIVE_SOURCE_NOT_ACTIVATED'):
        DormantReadOnlyHTTP()(p.url,{'f':'json'},timeout=1,maximum=1000)


@pytest.mark.parametrize('path',['Transportation/Functional_Classification/FeatureServer/0',
                               'https://evil.test/0','Transportation/State_System/FeatureServer/0/applyEdits'])
def test_unknown_layer_and_upstream_write_path_denied(path):
    p,m,f=setup_capture()
    with pytest.raises(CaptureError,match='LAYER_NOT_ALLOWLISTED'): dataclasses.replace(p,relative_layer=path)


@pytest.mark.parametrize('bbox',[(0,0,float('nan'),1),(1,0,0,1),(-180,-85,180,85)])
def test_invalid_scope(bbox):
    p,m,f=setup_capture()
    with pytest.raises(CaptureError):dataclasses.replace(p,bbox=bbox)
