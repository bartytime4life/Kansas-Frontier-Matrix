from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json
p=argparse.ArgumentParser();p.add_argument('--geometry-vintage',required=True);p.add_argument('--state',required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
o={"schema_version":"1.0.0","object_type":"usda_plants_county_geometry_source","geometry_source_id":f"kfm.geometry_source.flora.usda_plants.counties.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","geometry_authority":{"authority_id":"us_census_cartographic_boundary","authority_name":"U.S. Census Bureau Cartographic Boundary Files","authority_uri":"https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html","rights_status":"public","citation_required":True,"citation_text":"U.S. Census Bureau Cartographic Boundary Files, county boundaries."},"snapshot_date":a.snapshot_date,"geometry_vintage":a.geometry_vintage,"geometry_level":"county","geometry_generalization":"cartographic_boundary","allowed_geometry_types":["Polygon","MultiPolygon"],"join_key":"fips","state_filter":[a.state],"network_mode":"disabled","status":"registered","reason_codes":["USDA_PLANTS_GEOMETRY_SOURCE_REGISTERED"]}
o['source_hash']=canonical_hash(o,'source_hash');validate(ROOT/'schemas/flora/usda_plants_county_geometry_source.schema.json',o);write_json(a.out,o)
