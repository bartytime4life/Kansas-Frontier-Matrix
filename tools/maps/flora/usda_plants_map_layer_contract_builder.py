from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; SCHEMA=ROOT/'schemas/flora/usda_plants_map_layer_contract.schema.json'
def main():
 p=argparse.ArgumentParser();p.add_argument('--snapshot-date',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 o={"schema_version":"1.0.0","object_type":"usda_plants_map_layer_contract","contract_id":"kfm.map_contract.flora.usda_plants.county_presence.v1","domain":"flora","status":"draft","publication_state":"not_published","join":{"dataset_key":"distributions.county[].fips","geometry_key":"fips","presence_property":"presence"},"source_contract":{"maplibre_source_id":"flora_usda_plants_county_presence","source_type":"geojson","future_data_ref":"published/flora/usda_plants/county_presence.geojson","currently_available":False},"layer_contract":{"maplibre_layer_id":"flora_usda_plants_county_presence_fill","layer_type":"fill","source":"flora_usda_plants_county_presence","paint_contract":{"fill_opacity":0.55,"fill_color_property":"presence"}},"evidence_drawer_binding":{"on_click_lookup_key":"fips","payload_ref_template":"ui/flora/usda_plants/evidence_drawer/<plants_symbol>.json"},"constraints":["No county geometry generated in this layer","No publication claim","No sensitive coordinates","Future geometry must join by 5-digit FIPS"]}
 from jsonschema import Draft202012Validator; errs=list(Draft202012Validator(json.loads(SCHEMA.read_text())).iter_errors(o));
 if errs: raise ValueError(str(errs[0]))
 a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
