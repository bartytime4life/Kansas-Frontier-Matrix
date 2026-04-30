import json, subprocess
from pathlib import Path

BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def test_new_clis_help_and_version():
    for cli in ['kfm-ebird-doctor','kfm-ebird-conformance']:
        subprocess.check_call([str(BASE/cli),'--help'])
        out=subprocess.check_output([str(BASE/cli),'--version'], text=True)
        payload=json.loads(out)
        assert payload['adapter']=='kfm-ebird'

def test_doctor_json_passes():
    out=subprocess.check_output([str(BASE/'kfm-ebird-doctor'),'--json'], text=True)
    rep=json.loads(out)
    assert rep['object_type']=='EbirdDoctorReport'
    assert rep['status'] in {'pass','fail'}

def test_contract_hash_deterministic():
    import importlib.util
    spec=importlib.util.spec_from_file_location("kfm_ebird_contract", BASE/"kfm_ebird_contract.py")
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    lock=mod.load_contract_lock(BASE/"contract_lock.json")
    compute_contract_hash=mod.compute_contract_hash
    assert compute_contract_hash(lock)==compute_contract_hash(lock)
