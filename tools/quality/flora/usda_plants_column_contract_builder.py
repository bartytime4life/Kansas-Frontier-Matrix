from __future__ import annotations
import argparse
from pathlib import Path
from datetime import datetime,timezone
import sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate

def main():
 p=argparse.ArgumentParser();p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 o={"schema_version":"1.0.0","object_type":"usda_plants_column_contract","contract_id":"kfm.column_contract.flora.usda_plants.v1","domain":"flora","source_id":"usda_plants","tables":{"checklist":{"required_columns":["symbol","scientificName","nationalCommonName","family"],"optional_columns":["nativeStatus","growthHabit","wetlandStatus"]},"state_distribution":{"required_columns":["symbol","state","presence"],"optional_columns":[]},"county_distribution":{"required_columns":["symbol","fips","presence"],"optional_columns":[]}},"normalization_rules":["trim_whitespace","preserve_scientific_name_authorship","uppercase_symbol","uppercase_state","zero_pad_fips_to_5_digits"]}
 o['contract_hash']=canonical_hash(o,'contract_hash')
 validate(ROOT/'schemas/flora/usda_plants_column_contract.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
