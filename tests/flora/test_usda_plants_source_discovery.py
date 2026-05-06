import json,subprocess

def test_source_discovery(tmp_path):
 out=tmp_path/'work/flora/usda_plants/2026-04-30/source_discovery.json'
 subprocess.run(['python','tools/sources/flora/usda_plants_source_discovery.py','--downloads-html','tests/fixtures/flora/usda_plants/source_discovery/downloads_page_fixture.html','--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out',str(out)],check=True)
 obj=json.loads(out.read_text())
 roles={r['resource_role'] for r in obj['discovered_resources']}
 assert {'checklist','state_distribution','county_distribution','unknown'}.issubset(roles)
 assert obj['discovery_hash'].startswith('sha256:')
