import json, subprocess, tempfile
from pathlib import Path


def mk_release(tmp: Path):
    rel = tmp/'release_receipt.json'
    rel.write_text(json.dumps({'release_id':'rel1','run_id':'run1','kfm:spec_hash':'sha256:'+'a'*64,'suppression_min_n':10,'source_uri':'https://x?token=abc'})+'\n')
    pubroot = tmp/'published'; pubroot.mkdir()
    (pubroot/'ebird_agg_huc12.json').write_text(json.dumps({'kfm:spec_hash':'sha256:'+'a'*64,'public_safe':True,'exact_points':'restricted'})+'\n')
    return rel, pubroot


def test_scan_outputs_reports():
    with tempfile.TemporaryDirectory() as d:
        t=Path(d); rel,pub=mk_release(t); out=t/'out'
        subprocess.check_call(['python','tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_observe.py','--mode','scan','--aggregate','huc12','--release-receipt',str(rel),'--published-root',str(pub),'--out-dir',str(out)])
        assert (out/'observability_snapshot.json').exists()
        assert (out/'integrity_scan_report.json').exists()


def test_attest_hash_stable():
    with tempfile.TemporaryDirectory() as d:
        t=Path(d); rel,pub=mk_release(t)
        out1=t/'a1'; out2=t/'a2'
        cmd=['python','tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_observe.py','--mode','attest','--aggregate','huc12','--release-receipt',str(rel)]
        subprocess.check_call(cmd+['--out-dir',str(out1)])
        subprocess.check_call(cmd+['--out-dir',str(out2)])
        h1=json.loads((out1/'provenance_attestation.json').read_text())['attestation_hash']
        h2=json.loads((out2/'provenance_attestation.json').read_text())['attestation_hash']
        assert h1==h2
