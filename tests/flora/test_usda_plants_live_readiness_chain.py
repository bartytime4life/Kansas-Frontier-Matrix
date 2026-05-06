import json,subprocess

def test_chain(tmp_path):
 out=tmp_path/'out';d='2026-04-30';g='2026-04-30T00:00:00Z'
 subprocess.run(['python','tools/sources/flora/usda_plants_source_discovery.py','--downloads-html','tests/fixtures/flora/usda_plants/source_discovery/downloads_page_fixture.html','--snapshot-date',d,'--generated-at',g,'--out',str(out/f'work/flora/usda_plants/{d}/source_discovery.json')],check=True)
 subprocess.run(['python','tools/quality/flora/usda_plants_column_contract_builder.py','--generated-at',g,'--out',str(out/'work/flora/usda_plants/column_contract.json')],check=True)
 subprocess.run(['python','tools/intake/flora/usda_plants_snapshot_intake.py','--raw-dir','tests/fixtures/flora/usda_plants/operator_snapshot/good','--snapshot-date',d,'--generated-at',g,'--out-dir',str(out/f'raw/flora/usda_plants/{d}')],check=True)
