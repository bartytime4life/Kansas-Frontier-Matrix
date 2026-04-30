import json, subprocess
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def test_layer14_help_and_version():
    subprocess.check_call([str(BASE/'kfm-ebird-portal'),'--help'])
    subprocess.check_call([str(BASE/'kfm-ebird-downloads'),'--help'])
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-portal'),'--version'], text=True))['adapter']=='kfm-ebird'
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-downloads'),'--version'], text=True))['adapter']=='kfm-ebird'

def test_layer14_build_smoke(tmp_path):
    outd=tmp_path/'downloads'; catd=tmp_path/'downloads-cat'
    rel=tmp_path/'latest.json'; rel.write_text(json.dumps({'release_id':'r1','run_id':'run1','kfm:spec_hash':'sha256:s'}),encoding='utf-8')
    subprocess.check_call([str(BASE/'kfm-ebird-downloads'),'--release-index',str(rel),'--out-dir',str(outd),'--catalog-out-dir',str(catd)])
    assert (outd/'public_download_manifest.json').exists()
    outp=tmp_path/'portal'; catp=tmp_path/'portal-cat'
    subprocess.check_call([str(BASE/'kfm-ebird-portal'),'--release-index',str(rel),'--download-manifest',str(outd/'public_download_manifest.json'),'--out-dir',str(outp),'--catalog-out-dir',str(catp),'--format','both'])
    assert (outp/'public_portal_manifest.json').exists()
