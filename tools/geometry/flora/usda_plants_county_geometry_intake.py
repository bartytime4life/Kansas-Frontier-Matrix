from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file
p=argparse.ArgumentParser();p.add_argument('--geometry-source',type=Path,required=True);p.add_argument('--county-geojson',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
if not a.county_geojson.exists(): raise SystemExit('USDA_PLANTS_GEOMETRY_INTAKE_MISSING_FILE')
if a.county_geojson.suffix.lower() not in ['.geojson','.json']: raise SystemExit('USDA_PLANTS_GEOMETRY_INTAKE_UNSUPPORTED_MEDIA_TYPE')
o={"schema_version":"1.0.0","object_type":"usda_plants_county_geometry_intake","intake_id":f"kfm.geometry_intake.flora.usda_plants.counties.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","geometry_source_ref":str(a.geometry_source),"snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"input_files":[{"role":"county_geojson","path":str(a.county_geojson),"media_type":"application/geo+json","sha256":sha256_file(a.county_geojson),"size_bytes":a.county_geojson.stat().st_size,"status":"accepted"}],"required_roles":["county_geojson"],"missing_roles":[],"network_mode":"disabled","status":"pass","reason_codes":["USDA_PLANTS_GEOMETRY_INTAKE_PASS"]}
o['intake_hash']=canonical_hash(o,'intake_hash');validate(ROOT/'schemas/flora/usda_plants_county_geometry_intake.schema.json',o);write_json(a.out,o)
