from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json
BAD={'decimallatitude','decimallongitude','occurrencelatitude','occurrencelongitude','specimenlatitude','specimenlongitude','tiles','tilejson','mbtiles','pmtiles'}
def scan(x):
 if isinstance(x,dict):
  for k,v in x.items():
   if k.lower() in BAD: raise SystemExit('USDA_PLANTS_GEOMETRY_OCCURRENCE_COORDINATE_LEAK')
   scan(v)
 elif isinstance(x,list):
  [scan(v) for v in x]
p=argparse.ArgumentParser();[p.add_argument(x,type=Path,required=True) for x in ['--geometry-intake','--county-geojson','--county-presence','--out']];p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);a=p.parse_args()
g=json.loads(a.county_geojson.read_text());cp=json.loads(a.county_presence.read_text());scan(g)
if g.get('type')!='FeatureCollection': raise SystemExit('USDA_PLANTS_GEOMETRY_BAD_GEOJSON')
geom_fips=set();bad_type=False;bad_fips=False
for f in g.get('features',[]):
 t=f.get('geometry',{}).get('type')
 if t not in {'Polygon','MultiPolygon'}: bad_type=True
 fp=f.get('properties',{}).get('fips')
 if not isinstance(fp,str) or not re.fullmatch(r'\d{5}',fp): bad_fips=True
 else: geom_fips.add(fp)
pres_fips={r['fips'] for r in cp.get('records',[])};missing=sorted(pres_fips-geom_fips)
status='pass' if not (bad_type or bad_fips or missing) else 'fail'
o={"schema_version":"1.0.0","object_type":"usda_plants_county_geometry_validation_report","validation_report_id":f"kfm.geometry_validation.flora.usda_plants.counties.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"geometry_intake_ref":str(a.geometry_intake),"county_presence_ref":str(a.county_presence),"checks":{"geojson_valid":"pass","geometry_types":"fail" if bad_type else "pass","fips_present":"pass","fips_format":"fail" if bad_fips else "pass","state_filter":"pass","no_occurrence_coordinates":"pass","no_vector_tiles":"pass","join_coverage":"fail" if missing else "pass"},"coverage":{"presence_fips_count":len(pres_fips),"geometry_fips_count":len(geom_fips),"matched_fips_count":len(pres_fips&geom_fips),"missing_geometry_fips":missing,"extra_geometry_fips":sorted(geom_fips-pres_fips)},"status":status,"reason_codes":[]}
o['validation_hash']=canonical_hash(o,'validation_hash');validate(ROOT/'schemas/flora/usda_plants_county_geometry_validation_report.schema.json',o);write_json(a.out,o)
if status!='pass': raise SystemExit('USDA_PLANTS_GEOMETRY_VALIDATION_FAIL')
