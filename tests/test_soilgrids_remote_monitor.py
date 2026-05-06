import json
from pathlib import Path
import pytest
from tools.soilgrids import soilgrids_remote_monitor as m

@pytest.fixture
def valid_inputs(tmp_path):
    dm={"distribution_id":"d1","distribution_spec_hash":"abc","public_base_url":"https://example.com/base/","objects":[{"role":"cog","url":"https://example.com/a.tif","content_length":512},{"role":"viewer_html","url":"https://example.com/index.html","content_length":10}]}
    dr={"status":"success","distribution_spec_hash":"abc"}
    ravr={"checks":[{"severity":"required","status":"pass"}]}
    p=tmp_path
    (p/"dm.json").write_text(json.dumps(dm)); (p/"dr.json").write_text(json.dumps(dr)); (p/"ravr.json").write_text(json.dumps(ravr))
    return p

def test_rejects_missing_distribution_manifest(tmp_path):
    with pytest.raises(m.MonitorError): m.load_monitor_inputs(tmp_path/"x.json", tmp_path/"y.json", tmp_path/"z.json")

def test_rejects_malformed_distribution_manifest(tmp_path):
    f=tmp_path/"dm.json"; f.write_text("{")
    (tmp_path/"dr.json").write_text("{}")
    (tmp_path/"ravr.json").write_text("{}")
    with pytest.raises(m.MonitorError): m.load_monitor_inputs(f,tmp_path/"dr.json",tmp_path/"ravr.json")

def test_rejects_failed_distribution_receipt():
    with pytest.raises(m.MonitorError): m.validate_distribution_evidence({}, {"status":"failed"}, {"checks":[]})

def test_rejects_remote_access_report_required_failures():
    with pytest.raises(m.MonitorError): m.validate_distribution_evidence({}, {"status":"success"}, {"checks":[{"severity":"required","status":"fail"}]})

def test_monitor_spec_hash_stable():
    dm,dr,ra={"distribution_id":"d","distribution_spec_hash":"x"},{"status":"success"},{"checks":[]}
    p=m.load_monitor_policy(None)
    a=m.compute_monitor_spec_hash(dm,dr,ra,p,"dry-run",{})
    b=m.compute_monitor_spec_hash(dm,dr,ra,p,"dry-run",{})
    assert a==b

def test_dry_run_performs_no_probes(valid_inputs):
    dm,dr,ra,_=m.load_monitor_inputs(valid_inputs/"dm.json",valid_inputs/"dr.json",valid_inputs/"ravr.json")
    plan=m.build_monitor_plan(dm,m.load_monitor_policy(None),"dry-run","x")
    assert m.execute_monitor_plan(plan,m.MockHttpProbeClient({}),mode="dry-run")==[]

def test_existing_remote_requires_allow_remote_network(valid_inputs):
    dm,dr,ra,_=m.load_monitor_inputs(valid_inputs/"dm.json",valid_inputs/"dr.json",valid_inputs/"ravr.json")
    plan=m.build_monitor_plan(dm,m.load_monitor_policy(None),"existing-remote","x")
    with pytest.raises(m.MonitorError): m.execute_monitor_plan(plan,m.MockHttpProbeClient({}),mode="existing-remote",allow_remote_network=False)

def test_build_snapshot_statuses():
    plan={"distribution_id":"d","distribution_spec_hash":"x","monitor_spec_hash":"m","probes":[{"probe_id":"a"}]}
    s=m.build_monitor_snapshot(plan,[{"status":"pass"}],[],"r","one-shot","p","o")
    assert s["status"]=="healthy"

