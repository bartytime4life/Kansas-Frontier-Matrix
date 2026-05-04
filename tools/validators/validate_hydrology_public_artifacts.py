import json,glob
bad=['data/raw/','data/work/','data/quarantine/','data/processed/','connectors/']
for p in glob.glob('fixtures/domains/hydrology/published_artifacts/*.json'):
 o=json.load(open(p))
 s=json.dumps(o)
 assert o['synthetic'] and o['public_display_allowed']
 assert not any(b in s and 'prohibited_source_paths' not in s for b in bad)
print('ok')
