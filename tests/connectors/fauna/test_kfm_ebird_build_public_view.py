import json, subprocess, tempfile
from hashlib import sha256
from pathlib import Path

SCRIPT=Path('tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_build_public_view.py')
PROMOTE=Path('tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_promote.py')

def shafile(p:Path)->str: return 'sha256:'+sha256(p.read_bytes()).hexdigest()

def make_promoted(td:str, agg='huc12'):
    eb=Path('tests/fixtures/fauna/ebird/evidencebundle.valid.json')
    row={"schema_version":"v1","object_type":"AggregateOccurrence","domain":"fauna","source":"ebird","policy_label":"public_aggregate","aggregate":agg,"taxonKey":"sp1","occurrenceDate_month":"2025-01","checklist_count":10,"observation_count_sum":12,"observation_count_unknown_count":0,"species_count":1,"suppression_min_n":10,"kfm:spec_hash":"sha256:e2d03a9bbb06efed2bf6203fe04a35eba6fc11033d613a23fdbdcccd3c2e7fa7","evidence_bundle_uri":"file://eb.json"}
    row['huc12' if agg=='huc12' else 'county_fips']='123456789012' if agg=='huc12' else '20001'
    aggf=Path(td)/'agg.jsonl'; aggf.write_text(json.dumps(row)+'\n')
    manf=Path(td)/'man.json'; manf.write_text(json.dumps({"kfm:spec_hash":row['kfm:spec_hash'],"suppression_min_n":10,"output_sha256":shafile(aggf),"evidencebundle_sha256":shafile(eb)}))
    pub=Path(td)/'data/published/fauna/ebird'/agg
    subprocess.run(['python3',str(PROMOTE),'--aggregate-file',str(aggf),'--aggregate-manifest',str(manf),'--evidencebundle',str(eb),'--aggregate',agg,'--publish-dir',str(pub),'--catalog-dir',str(Path(td)/'cat'),'--layer-registry',f'data/published/fauna/layers/ebird_agg_{agg}.json'],check=True)
    return next(pub.iterdir())

def test_build_huc12_and_dryrun_deterministic():
    with tempfile.TemporaryDirectory() as td:
        promo=make_promoted(td,'huc12')
        cmd=['python3',str(SCRIPT),'--promotion-dir',str(promo),'--aggregate','huc12','--out-dir',str(promo/'api'),'--maplibre-out',str(promo/'maplibre.json'),'--format','jsonl']
        r=subprocess.run(cmd,capture_output=True,text=True); assert r.returncode==0, r.stderr
        f=(promo/'api'/'features.jsonl').read_text().splitlines(); assert len(f)==1
        feat=json.loads(f[0]); assert 'decimalLatitude' not in feat and 'geometry' not in feat
        d=json.loads((promo/'api'/'feature_evidence_drawers.jsonl').read_text().splitlines()[0]);
        for k in ['source_uri','query_predicate','evidence_bundle_uri','kfm:spec_hash']: assert k in d
        dry1=subprocess.run(cmd+['--dry-run'],capture_output=True,text=True); dry2=subprocess.run(cmd+['--dry-run'],capture_output=True,text=True)
        assert dry1.returncode==0 and dry2.returncode==0
        assert json.loads((promo/'api'/'features.jsonl').read_text().splitlines()[0])['feature_id']==feat['feature_id']

def test_fail_denied_and_overwrite():
    with tempfile.TemporaryDirectory() as td:
        promo=make_promoted(td,'huc12')
        p=subprocess.run(['python3',str(SCRIPT),'--promotion-dir',str(promo),'--aggregate','huc12'],capture_output=True,text=True); assert p.returncode==0
        p2=subprocess.run(['python3',str(SCRIPT),'--promotion-dir',str(promo),'--aggregate','huc12'],capture_output=True,text=True); assert p2.returncode!=0
        aggf=promo/'aggregates.jsonl'; r=json.loads(aggf.read_text().splitlines()[0]); r['geometry']='x'; aggf.write_text(json.dumps(r)+'\n')
        p3=subprocess.run(['python3',str(SCRIPT),'--promotion-dir',str(promo),'--aggregate','huc12','--overwrite'],capture_output=True,text=True); assert p3.returncode!=0
