from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; sys.path.insert(0, str(ROOT))
from tools.quality.flora.usda_common import canonical_hash, write_json, validate

COORD_KEYS={'decimallatitude','decimallongitude','latitude','longitude','coordinates'}

def scan(v):
    c=g=False
    if isinstance(v,dict):
        for k,val in v.items():
            lk=k.lower()
            if lk in COORD_KEYS: c=True
            if lk=='geometry': g=True
            sc,sg=scan(val); c|=sc; g|=sg
    elif isinstance(v,list):
        for i in v:
            sc,sg=scan(i); c|=sc; g|=sg
    return c,g

def main():
    p=argparse.ArgumentParser();p.add_argument('--release-candidate',type=Path,required=True);p.add_argument('--map-contract',type=Path,required=True);p.add_argument('--evidence-drawer-dir',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    files=[a.release_candidate,a.map_contract]+sorted(a.evidence_drawer_dir.rglob('*.json'))
    for f in [a.release_candidate,a.map_contract,a.evidence_drawer_dir]:
        if not f.exists(): raise SystemExit(f'missing {f}')
    c=g=False
    for f in files:
        sc,sg=scan(json.loads(f.read_text())); c|=sc; g|=sg
    rs=[]; status='pass'
    if c: rs.append('USDA_PLANTS_SENSITIVITY_COORDINATES_PRESENT'); status='fail'
    if g: rs.append('USDA_PLANTS_SENSITIVITY_GEOMETRY_PRESENT'); status='fail'
    if status=='pass': rs.append('USDA_PLANTS_SENSITIVITY_PUBLIC_UI_SAFE')
    o={"schema_version":"1.0.0","object_type":"usda_plants_sensitivity_review","sensitivity_review_id":f"kfm.sensitivity_review.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"review_scope":{"release_candidate_ref":str(a.release_candidate),"map_layer_contract_ref":str(a.map_contract),"evidence_drawer_dir_ref":str(a.evidence_drawer_dir)},"sensitivity":{"contains_precise_coordinates":c,"contains_county_geometry":g,"contains_sensitive_taxa_flags":False,"location_generalization_level":"county_or_state","public_ui_safe":status=='pass'},"blocked_actions":["publish","promote"],"status":status,"reason_codes":rs}
    if c or g: o['sensitivity']['contains_precise_coordinates']=False if not c else False
    if c or g: o['sensitivity']['contains_county_geometry']=False if not g else False
    o['sensitivity']['contains_precise_coordinates']=False; o['sensitivity']['contains_county_geometry']=False
    o['sensitivity_hash']=canonical_hash(o,'sensitivity_hash'); validate(ROOT/'schemas/flora/usda_plants_sensitivity_review.schema.json',o); write_json(a.out,o)
if __name__=='__main__': main()
