import json, subprocess, tempfile
from pathlib import Path
from hashlib import sha256

SCRIPT=Path('tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_promote.py')


def shafile(p: Path)->str:
    return 'sha256:'+sha256(p.read_bytes()).hexdigest()

def make_row(agg='huc12'):
    r={"schema_version":"v1","object_type":"AggregateOccurrence","domain":"fauna","source":"ebird","policy_label":"public_aggregate","aggregate":agg,"taxonKey":"sp1","occurrenceDate_month":"2025-01","checklist_count":10,"observation_count_sum":12,"observation_count_unknown_count":0,"species_count":1,"suppression_min_n":10,"kfm:spec_hash":"sha256:e2d03a9bbb06efed2bf6203fe04a35eba6fc11033d613a23fdbdcccd3c2e7fa7","evidence_bundle_uri":"file://eb.json"}
    r['huc12' if agg=='huc12' else 'county_fips']='123456789012' if agg=='huc12' else '20001'
    return r

def run(td, agg='huc12', extra=None, dry=False):
    eb=Path('tests/fixtures/fauna/ebird/evidencebundle.valid.json')
    aggf=Path(td)/'agg.jsonl'; row=make_row(agg); aggf.write_text(json.dumps(row)+'\n')
    man={"kfm:spec_hash":row['kfm:spec_hash'],"suppression_min_n":10,"output_sha256":shafile(aggf),"evidencebundle_sha256":shafile(eb),"counts":{"groups_published":1}}
    manf=Path(td)/'man.json'; manf.write_text(json.dumps(man))
    pub=Path(td)/'data/published/fauna/ebird'/agg; cat=Path(td)/'catalog'; reg=Path('data/published/fauna/layers/ebird_agg_'+agg+'.json')
    cmd=['python3',str(SCRIPT),'--aggregate-file',str(aggf),'--aggregate-manifest',str(manf),'--evidencebundle',str(eb),'--aggregate',agg,'--publish-dir',str(pub),'--catalog-dir',str(cat),'--layer-registry',str(reg)]
    if dry: cmd.append('--dry-run')
    if extra: cmd.extend(extra)
    return subprocess.run(cmd,capture_output=True,text=True)


def test_promote_huc12_success_and_receipt_safety():
    with tempfile.TemporaryDirectory() as td:
        p=run(td); assert p.returncode==0, p.stderr
        run_dir=next((Path(td)/'data/published/fauna/ebird/huc12').iterdir())
        rec=json.loads((run_dir/'promotion_receipt.json').read_text())
        assert rec['public_safe'] is True
        assert 'suppressed_groups' not in rec
        assert 'suppressed_groups' not in rec.get('counts', {})


def test_promote_county_success():
    with tempfile.TemporaryDirectory() as td:
        p=run(td,agg='county'); assert p.returncode==0, p.stderr


def test_dry_run_no_writes_and_deterministic_run_id():
    with tempfile.TemporaryDirectory() as td:
        p1=run(td,dry=True); p2=run(td,dry=True)
        assert p1.returncode==0 and p2.returncode==0
        j1=json.loads(p1.stdout[p1.stdout.find('{'):]); j2=json.loads(p2.stdout[p2.stdout.find('{'):]); assert j1['run_id']==j2['run_id']
        assert not (Path(td)/'data/published/fauna/ebird/huc12').exists()


def test_failures():
    with tempfile.TemporaryDirectory() as td:
        p=run(td, extra=['--overwrite']); assert p.returncode==0
        p2=run(td); assert p2.returncode!=0
    with tempfile.TemporaryDirectory() as td:
        p=run(td, extra=['--evidencebundle','tests/fixtures/fauna/ebird/restricted_observations.jsonl']); assert p.returncode!=0
    with tempfile.TemporaryDirectory() as td:
        bad=Path(td)/'bad.jsonl'; r=make_row(); r['decimalLatitude']=1; bad.write_text(json.dumps(r)+'\n')
        eb=Path('tests/fixtures/fauna/ebird/evidencebundle.valid.json'); man=Path(td)/'m.json'; man.write_text(json.dumps({"kfm:spec_hash":r['kfm:spec_hash'],"suppression_min_n":10,"output_sha256":shafile(bad),"evidencebundle_sha256":shafile(eb)}))
        cmd=['python3',str(SCRIPT),'--aggregate-file',str(bad),'--aggregate-manifest',str(man),'--evidencebundle',str(eb),'--aggregate','huc12','--publish-dir',str(Path(td)/'data/published/x'),'--catalog-dir',str(Path(td)/'c')]
        assert subprocess.run(cmd,capture_output=True,text=True).returncode!=0
