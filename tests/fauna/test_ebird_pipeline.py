import json, subprocess, tempfile, shutil
from pathlib import Path

def test_plan():
    cmd=['tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-run-pipeline','--ebd-file','tests/fixtures/fauna/ebird/sample_ebd.tsv','--plan']
    out=subprocess.check_output(cmd,text=True)
    j=json.loads(out)
    assert j['object_type']=='PipelinePlan'

def test_execute():
    with tempfile.TemporaryDirectory() as d:
        shutil.rmtree('data/published/fauna/ebird_test', ignore_errors=True)
        shutil.rmtree('data/catalog/fauna/ebird_test', ignore_errors=True)
        cmd=['tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-run-pipeline','--ebd-file','tests/fixtures/fauna/ebird/sample_ebd.tsv','--source-uri','https://ebird.org/data?token=abc&request_id=synthetic','--aggregate','both','--suppression','10','--work-dir',d+'/run','--publish-dir','data/published/fauna/ebird_test','--catalog-dir','data/catalog/fauna/ebird_test','--layer-registry-dir','data/published/fauna/layers','--run-id','testexec001','--no-maplibre','--execute']
        subprocess.check_call(cmd)
        subprocess.check_call(['python','tools/validators/fauna/validate_pipeline_run.py',d+'/run'])
        man=json.loads(Path(d+'/run/pipeline_manifest.json').read_text())
        assert man['object_type']=='PipelineManifest'
