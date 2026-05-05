import json
from pathlib import Path
o=json.loads(Path('release/dry_runs/hydrology_usgs_water_data_metadata_probe_gate.json').read_text())
ok=o['no_live_observation_ingestion'] and o['no_time_series_query'] and o['no_station_site_query']
print('PASS no observation ingestion assertions' if ok else 'FAIL no observation ingestion assertions')
raise SystemExit(0 if ok else 1)
