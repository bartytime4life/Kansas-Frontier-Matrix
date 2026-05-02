import json
from pathlib import Path
from kfm.air_quality.airnow.file_products.manifest import validate_manifest
from kfm.air_quality.airnow.file_products.parse_common import parse_manifest_file

B=Path('tests/fixtures/air_quality/airnow/layer3')

def m(name): return json.loads((B/'manifests'/name).read_text())

def test_hourly_parses_and_negative_warning():
    pm=m('hourly_aq_obs_manifest.json'); p,q=parse_manifest_file(pm,Path(pm['input_file']),'2026-01-01T00:00:00Z')
    assert p and not q and 'NEGATIVE_CONCENTRATION:PM25' in p[0]['warnings'] and p[0]['reporting_areas']==['Clark County','Las Vegas']

def test_daily_sentinel_not_quarantine():
    pm=m('daily_data_manifest.json'); p,q=parse_manifest_file(pm,Path(pm['input_file']),'2026-01-01T00:00:00Z')
    assert len(p)==2 and not q and p[1]['aqi']['aqi_status']=='SOURCE_SENTINEL_NOT_APPLICABLE'

def test_site_non_aqi_allowed():
    pm=m('monitoring_site_locations_manifest.json'); p,q=parse_manifest_file(pm,Path(pm['input_file']),'2026-01-01T00:00:00Z')
    assert p[0]['parameter_role']=='meteorological_or_non_aqi'
