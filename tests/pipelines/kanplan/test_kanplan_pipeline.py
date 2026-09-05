import copy
import dataclasses
import json
import math
import pytest
from connectors.kansas.kanplan import CaptureError, content_hash, SyntheticTransport
from packages.geo.src.geo.esri_polyline import GeometryError, polyline_to_geojson, intersects_bbox
import importlib
pipeline = importlib.import_module("pipelines.normalize.roads-rail-trade.kanplan_state_system")
compile_fixture = pipeline.compile_fixture
validate_candidate = pipeline.validate_candidate
resolve_fixture = pipeline.resolve_fixture
report_fixture = pipeline.report_fixture
candidate_refresh = pipeline.candidate_refresh
rollback_check = pipeline.rollback_check
aadt_observation = pipeline.aadt_observation
PUBLIC_KEYS = pipeline.PUBLIC_KEYS
build_fixture = pipeline.build_fixture
from test_kanplan_capture import setup_capture, run


def test_full_fixture_circle():
    c=build_fixture();validate_candidate(c)
    assert len(c.display['features'])==2
    assert c.display['features'][0]['geometry']['type']=='MultiLineString'
    assert len(c.analytical[0]['native_geometry']['paths'][0][0])==4
    assert len(c.display['features'][0]['geometry']['coordinates'][0][0])==2
    assert c.analytical[0]['native_attributes']['FromMeasure']==0
    assert c.analytical[0]['transform']['z_removed_for_display']
    assert c.analytical[0]['transform']['m_removed_for_display']
    assert c.analytical[0]['reported_adjusted_traveled_mileage'] is None
    selection=c.display['features'][0]['id']
    result=resolve_fixture(c,selection,context='private_fixture')
    assert result['outcome']=='ANSWER' and result['release_state']=='not_released'
    assert 'NOT KDOT' in result['bundle']['citations'][0]
    report=report_fixture(c,bbox=(0,0,.05,.05),context='private_fixture')
    assert report['unique_feature_count']==2 and report['aadt_total'] is None
    assert len(report['evidence_refs'])==2 and report['release_version'] is None
    body={k:v for k,v in report.items() if k!='report_sha256'}
    assert content_hash(body)==report['report_sha256']


def test_no_public_projection_of_internal_attributes():
    c=build_fixture()
    for feature in c.display['features']:
        assert set(feature['properties'])==PUBLIC_KEYS
    assert 'CreatedUser' not in json.dumps(c.display)
    assert 'synthetic-editor-never-public' not in json.dumps(c.bundles)


@pytest.mark.parametrize('context',['public','raw','work','quarantine','internal'])
def test_public_and_internal_store_delivery_denied(context):
    c=build_fixture()
    assert resolve_fixture(c,c.display['features'][0]['id'],context=context)['outcome']=='DENY'
    with pytest.raises(CaptureError):report_fixture(c,bbox=(0,0,.05,.05),context=context)


def test_unknown_feature_is_finite_abstention():
    assert resolve_fixture(build_fixture(),'does-not-exist',context='private_fixture')['outcome']=='ABSTAIN'


def test_report_uses_analytical_filter_and_scope():
    c=build_fixture()
    r=report_fixture(c,bbox=(0,0,.05,.05),route='FIXTURE-A',context='private_fixture')
    assert r['unique_feature_count']==1
    assert r['whole_feature_geometry_length_m']>2000
    assert report_fixture(c,bbox=(0,0,.05,.05),route='missing',context='private_fixture')['unique_feature_count']==0
    with pytest.raises(CaptureError,match='REPORT_SCOPE_NOT_COVERED'):
        report_fixture(c,bbox=(-1,-1,1,1),context='private_fixture')
    with pytest.raises(CaptureError,match='NO_SUPPORTED_COUNT_YEAR'):
        report_fixture(c,bbox=(0,0,.05,.05),year=2026,context='private_fixture')


@pytest.mark.parametrize('bad',[None,'','00000000-0000-0000-0000-000000000000','not-a-guid'])
def test_bad_business_identifier(bad):
    p,m,f=setup_capture();f[0]['attributes']['Id']=bad
    with pytest.raises(CaptureError):compile_fixture(run(p,SyntheticTransport(m,f)))


def test_duplicate_business_identifier():
    p,m,f=setup_capture();f[1]['attributes']['Id']=f[0]['attributes']['Id']
    with pytest.raises(CaptureError,match='BUSINESS_ID_ZERO_OR_DUPLICATE'):
        compile_fixture(run(p,SyntheticTransport(m,f)))


@pytest.mark.parametrize('value',[float('nan'),float('inf'),None,True])
def test_nonfinite_or_ambiguous_coordinate(value):
    g={'paths':[[[0,0],[1,value]]]}
    with pytest.raises(GeometryError):polyline_to_geojson(g,{'wkid':4326},has_z=False,has_m=False)


def test_curves_fail_closed_instead_of_flattening():
    with pytest.raises(GeometryError,match='UNSUPPORTED_CURVE'):
        polyline_to_geojson({'curvePaths':[[[0,0],{'c':[[1,1],[.5,.5]]}]]},{'wkid':4326},has_z=False,has_m=False)


def test_crs_and_z_m_rules():
    before={'paths':[[[0,0,30,1],[111319.49079327357,0,40,2]]]}
    original=copy.deepcopy(before)
    out,receipt=polyline_to_geojson(before,{'wkid':3857},has_z=True,has_m=True)
    assert out['coordinates'][1][0]==pytest.approx(1)
    assert before==original and receipt['native_z_m_preserved']
    with pytest.raises(GeometryError,match='AMBIGUOUS_DIMENSION'):
        polyline_to_geojson(before,{'wkid':3857},has_z=False,has_m=True)
    with pytest.raises(GeometryError,match='CRS_NOT_SUPPORTED'):
        polyline_to_geojson(before,{'wkid':999999},has_z=True,has_m=True)


def test_epsg_6923_projection_roundtrip_is_synthetic_not_source_validation():
    from pyproj import Transformer
    forward=Transformer.from_crs(4326,6923,always_xy=True,allow_ballpark=False,only_best=True)
    x0,y0=forward.transform(-98,38);x1,y1=forward.transform(-97.99,38.01)
    out,receipt=polyline_to_geojson({'paths':[[[x0,y0],[x1,y1]]]},{'wkid':6923},has_z=False,has_m=False)
    assert out['coordinates'][0]==pytest.approx([-98,38],abs=1e-7)
    assert receipt['input_horizontal_units']==['US survey foot','US survey foot']
    assert receipt['network_grids'] is False


def test_geometry_bounds_and_budget():
    with pytest.raises(GeometryError,match='VERTEX_BUDGET'):
        polyline_to_geojson({'paths':[[[0,0],[1,1],[2,2]]]},{'wkid':4326},has_z=False,has_m=False,maximum_vertices=2)
    # Geometry bbox overlaps rectangle, but the actual diagonal does not.
    assert not intersects_bbox({'type':'LineString','coordinates':[[0,0],[2,2]]},(0,1.5,.25,2))
    assert intersects_bbox({'type':'LineString','coordinates':[[0,0],[2,2]]},(.5,.5,1,1))


def test_malicious_text_remains_data_and_credentials_fail_closed():
    p,m,f=setup_capture();f[0]['attributes']['RouteId']='<img src=x onerror=alert(1)>'
    c=compile_fixture(run(p,SyntheticTransport(m,f)))
    assert c.display['features'][0]['properties']['route_id'].startswith('<img')
    f[0]['attributes']['RouteId']='token=not-to-be-leaked'
    with pytest.raises(CaptureError,match='CREDENTIAL_OR_CONTROL_TEXT'):
        compile_fixture(run(p,SyntheticTransport(m,f)))


def test_integrity_change_and_evidence_deletion_deny():
    c=build_fixture();c.display['features'][0]['properties']['route_id']='tampered'
    assert resolve_fixture(c,c.display['features'][0]['id'],context='private_fixture')['reason']=='INTEGRITY_FAILURE'
    c=build_fixture();c.bundles.clear()
    assert resolve_fixture(c,c.display['features'][0]['id'],context='private_fixture')['outcome']=='DENY'


def test_no_auto_publication_refresh_and_rights_aware_rollback():
    c=build_fixture()
    assert candidate_refresh(c,c)['reason']=='NO_MATERIAL_CONTENT_CHANGE'
    assert candidate_refresh(c,c,terms_changed=True)['outcome']=='DENY'
    assert candidate_refresh(c,c,source_withdrawn=True)['outcome']=='DENY'
    assert rollback_check(c,revoked_versions={c.dataset_version},context='private_fixture')['outcome']=='DENY'
    c.manifest['rights_revoked']=True
    assert resolve_fixture(c,c.display['features'][0]['id'],context='private_fixture')['outcome']=='DENY'
    assert rollback_check(c,revoked_versions=set(),context='private_fixture')['outcome']=='DENY'


def test_retrieval_receipts_and_bundle_ids_do_not_collapse_into_dataset_content_id():
    p,m,f=setup_capture()
    from connectors.kansas.kanplan import collect
    a=compile_fixture(collect(p,SyntheticTransport(m,f),clock=lambda:'2026-09-05T00:00:00Z',sleep=lambda _:None))
    b=compile_fixture(collect(p,SyntheticTransport(m,f),clock=lambda:'2026-09-05T01:00:00Z',sleep=lambda _:None))
    assert a.dataset_version==b.dataset_version
    assert set(a.bundles)!=set(b.bundles)
    assert a.manifest['display_sha256']!=b.manifest['display_sha256']


@pytest.mark.parametrize('attrs,expected_year',[
    ({'AADTCount':500,'AADTCountYear':2024,'LastEditedDate':1780000000000},2024),
    ({'AADTCount':500,'AADTCountYear':None,'AADTCountDate':1700000000000},None),
    ({'AADTCount':None},None)])
def test_aadt_year_is_not_edit_or_retrieval_year(attrs,expected_year):
    out=aadt_observation(attrs)
    assert out['count_year']==expected_year and out['live_traffic'] is False
    assert out['speed'] is None


@pytest.mark.parametrize('attrs',[{'AADTCount':-1},{'AADTCount':float('inf')},{'AADTCountYear':'2024'},
                                  {'AADTCountDate':'invalid-date'},{'AADTCountYear':True}])
def test_aadt_invalid_time_values(attrs):
    with pytest.raises(CaptureError):aadt_observation(attrs)
