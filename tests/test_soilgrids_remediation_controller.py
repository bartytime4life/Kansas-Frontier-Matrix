import json
from pathlib import Path
import pytest
import soilgrids_remediation_controller as m


def _write(p, o):
    p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(o))

def _base(tmp):
    dm={"distribution_id":"d1","distribution_spec_hash":"abc"}
    dr={"distribution_id":"d1","distribution_spec_hash":"abc","status":"success"}
    ms={"distribution_id":"d1","snapshot_id":"s1","monitor_spec_hash":"ms","observation_hash":"oh"}
    drift={"distribution_id":"d1","drifts":[],"status":"no_drift"}
    alert={"drift_ids":[]}
    paths={}
    for n,o in [("dm",dm),("dr",dr),("ms",ms),("df",drift),("al",alert)]:
        p=tmp/f"{n}.json"; _write(p,o); paths[n]=str(p)
    return paths

def test_rejects_missing_current_distribution_manifest(tmp_path):
    with pytest.raises(m.RemediationError): m._load_json(str(tmp_path/'missing.json'), required=True)

def test_rejects_malformed_distribution_manifest(tmp_path):
    p=tmp_path/'bad.json'; p.write_text('{')
    with pytest.raises(m.RemediationError): m._load_json(str(p), required=True)

def test_incident_fingerprint_stable(tmp_path):
    b=_base(tmp_path); dm=m._load_json(b['dm']); ms=m._load_json(b['ms']); dr=m._load_json(b['df'])
    assert m.compute_incident_fingerprint(dm,ms,dr)==m.compute_incident_fingerprint(dm,ms,dr)

def test_incident_classification_no_drift(): assert m.classify_incident({"drifts":[]})=="none"
def test_incident_classification_warning(): assert m.classify_incident({"drifts":[{"severity":"warning"}]})=="warning"
def test_incident_classification_critical(): assert m.classify_incident({"drifts":[{"severity":"critical"}]}, True)=="critical"
def test_incident_classification_emergency(): assert m.classify_incident({"drifts":[{"severity":"critical"}]}, False)=="emergency"

def test_selects_acknowledge_for_warning_drift():
    a=m.select_response_action({"drifts":[{"severity":"warning","class":"cache_header_drift"}]}, m.DEFAULT_POLICY)
    assert a=="acknowledge"

def test_selects_manual_approval_when_no_previous_good():
    a=m.select_response_action({"drifts":[{"severity":"critical","class":"checksum_mismatch"}]}, m.DEFAULT_POLICY)
    assert a=="request_manual_approval"

def test_selects_rollback_for_checksum_mismatch_with_previous_good():
    a=m.select_response_action({"drifts":[{"severity":"critical","class":"checksum_mismatch"}]}, m.DEFAULT_POLICY, previous_good={"distribution_id":"d0"})
    assert a=="rollback_latest_pointer"

def test_selects_quarantine_for_unsafe_redirect():
    a=m.select_response_action({"drifts":[{"severity":"critical","class":"unsafe_redirect"}]}, m.DEFAULT_POLICY)
    assert a=="quarantine"

def test_remediation_spec_hash_stable():
    h1=m.compute_remediation_spec_hash({"a":1},"acknowledge","plan-only")
    h2=m.compute_remediation_spec_hash({"a":1},"acknowledge","plan-only")
    assert h1==h2

def test_plan_only_does_not_mutate_remote(tmp_path):
    b=_base(tmp_path)
    class A: pass
    a=A(); a.current_distribution_manifest=b['dm']; a.current_distribution_receipt=b['dr']; a.monitor_snapshot=b['ms']; a.drift_report=b['df']; a.alert_envelope=b['al']; a.output_dir=str(tmp_path/'out'); a.mode='plan-only'; a.remote_access_validation_report=None; a.monitor_receipt=None; a.previous_good_distribution_manifest=None; a.previous_good_distribution_receipt=None; a.remediation_policy=None; a.force_action=None; a.approval_token=None; a.deterministic_run_id=True
    rp,code=m.handle_remote_drift(a)
    assert code==0 and Path(rp).exists()


def test_dry_run_does_not_mutate_remote(tmp_path):
    b=_base(tmp_path)
    class A: pass
    a=A(); a.current_distribution_manifest=b['dm']; a.current_distribution_receipt=b['dr']; a.monitor_snapshot=b['ms']; a.drift_report=b['df']; a.alert_envelope=b['al']; a.output_dir=str(tmp_path/'out'); a.mode='dry-run'; a.remote_access_validation_report=None; a.monitor_receipt=None; a.previous_good_distribution_manifest=None; a.previous_good_distribution_receipt=None; a.remediation_policy=None; a.force_action=None; a.approval_token=None; a.deterministic_run_id=True
    _,code=m.handle_remote_drift(a); assert code==5
