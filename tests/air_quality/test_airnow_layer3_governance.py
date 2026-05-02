import json
from pathlib import Path
from kfm.air_quality.airnow.file_products.manifest import validate_manifest

def test_secret_key_denied():
    m=json.loads(Path('tests/fixtures/air_quality/airnow/layer3/manifests/hourly_aq_obs_manifest.json').read_text()); m['api_key']='x'
    assert 'SECRET_FIELD_DENIED' in validate_manifest(m)
