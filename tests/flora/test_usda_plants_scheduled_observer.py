import json,subprocess,sys
from pathlib import Path

def run(tmp_path,html):
 o=tmp_path/'work/flora/usda_plants/scheduled/2026-04-30'
 subprocess.check_call([sys.executable,'tools/watchers/flora/usda_plants_scheduled_observer.py','--mode','scheduled_mock','--downloads-html',str(html),'--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out-dir',str(o)])
 return json.loads((o/'scheduled_observation.json').read_text()),json.loads((o/'watch_state.json').read_text()),o

def test_mock_outputs(tmp_path):
 obs,st,o=run(tmp_path,Path('tests/fixtures/flora/usda_plants/source_discovery/downloads_page_fixture.html'))
 assert obs['mode']=='scheduled_mock' and st['object_type']=='usda_plants_watch_state'
 assert not (o/'raw').exists() and not (o/'published').exists()
