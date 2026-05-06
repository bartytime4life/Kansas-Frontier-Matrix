import json,subprocess

def test_source_builder(tmp_path):
 o=tmp_path/'s.json';subprocess.run(['python','tools/geometry/flora/usda_plants_county_geometry_source_builder.py','--geometry-vintage','2024','--state','KS','--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out',str(o)],check=True)
 d=json.loads(o.read_text());assert d['network_mode']=='disabled';assert d['source_hash'].startswith('sha256:')
