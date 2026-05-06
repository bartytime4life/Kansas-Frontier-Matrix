import json, subprocess, tempfile
from pathlib import Path

SCRIPT = Path('tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_aggregate.py')


def test_aggregate_and_suppression():
    with tempfile.TemporaryDirectory() as td:
        out=Path(td)/'out.jsonl'; man=Path(td)/'m.json'; rec=Path(td)/'r.json'
        proc = subprocess.run(['python3', str(SCRIPT), '--observations','tests/fixtures/fauna/ebird/restricted_observations.jsonl','--evidencebundle','tests/fixtures/fauna/ebird/evidencebundle.valid.json','--aggregate','huc12','--suppression','10','--out',str(out),'--manifest',str(man),'--suppression-receipt',str(rec)],capture_output=True,text=True)
        assert proc.returncode == 0, proc.stderr
        rows=[json.loads(x) for x in out.read_text().splitlines() if x.strip()]
        assert len(rows)==1
        assert rows[0]['checklist_count']==10
        assert 'decimalLatitude' not in rows[0]
        assert rows[0]['observation_count_unknown_count']==1
        receipt=json.loads(rec.read_text())
        assert receipt['policy_label']=='restricted'
        assert receipt['counts']['groups_suppressed']==1
        assert receipt['suppressed_groups'][0]['group_hash'].startswith('sha256:')


def test_suppression_receipt_under_published_fails():
    with tempfile.TemporaryDirectory() as td:
        proc = subprocess.run(['python3', str(SCRIPT), '--observations','tests/fixtures/fauna/ebird/restricted_observations.jsonl','--evidencebundle','tests/fixtures/fauna/ebird/evidencebundle.valid.json','--aggregate','huc12','--out',str(Path(td)/'o.jsonl'),'--manifest',str(Path(td)/'m.json'),'--suppression-receipt','data/published/foo.json'],capture_output=True,text=True)
        assert proc.returncode != 0
