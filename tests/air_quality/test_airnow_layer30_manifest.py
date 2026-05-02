from pathlib import Path
import json

def test_smoke_fixture_exists():
    p=Path('tests/fixtures/air_quality/airnow/layer30/manifests/closure_archive_index_finalization_valid_manifest.json')
    assert p.exists()
