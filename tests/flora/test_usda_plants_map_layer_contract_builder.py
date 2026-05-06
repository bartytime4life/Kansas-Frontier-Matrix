import json, subprocess

def test_usda_plants_map_layer_contract_builder(tmp_path):
    out=tmp_path/"out"
    p=out/"maps/flora/usda_plants/county_presence.layer_contract.json"
    subprocess.run(["python","tools/maps/flora/usda_plants_map_layer_contract_builder.py","--snapshot-date","2026-04-30","--out",str(p)],check=True)
    o=json.loads(p.read_text()); assert o['publication_state']=="not_published" and o['source_contract']['currently_available'] is False
