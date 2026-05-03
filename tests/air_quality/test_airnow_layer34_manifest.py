from kfm.air_quality.airnow.closure_archive_index_preservation_finalization.manifest import validate_manifest
import json
from pathlib import Path

def test_manifest_valid():
 m=json.loads(Path('tests/fixtures/air_quality/airnow/layer34/manifests/closure_archive_index_preservation_finalization_valid_manifest.json').read_text())
 assert validate_manifest(m)==[]
