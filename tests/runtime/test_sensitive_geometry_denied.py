import json
import hashlib
from pathlib import Path

from runtime.tiles.verified_runtime import process_tile_request


def _load(name: str):
    return json.loads((Path('fixtures/runtime') / name).read_text())


def _manifest_hash(manifest: dict) -> str:
    canonical = json.dumps(manifest, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()


def test_sensitive_geometry_denied_without_transform():
    release_manifest = _load('release_manifest.valid.json')
    release_manifest['contains_sensitive_geometry'] = True
    release_manifest['sensitive_geometry_transformed'] = False

    result = process_tile_request(
        pmtiles_uri='fixtures/runtime/pmtiles/sample.pmtiles',
        release_manifest=release_manifest,
        evidence_bundle=_load('evidence_bundle.valid.json'),
        decision_envelope=_load('decision.allow.json'),
        signature_bundle={'status': 'valid', 'manifest_hash': _manifest_hash(release_manifest)},
        request_tile=(0, 0, 0),
        runtime_policy_profile={'posture': 'strict'},
    )
    assert result['runtime_response_envelope']['outcome'] == 'DENY'
    assert result['runtime_response_envelope']['reason'] == 'sensitive_geometry_without_transformation'


def test_policy_deny_path():
    deny = process_tile_request(
        pmtiles_uri='fixtures/runtime/pmtiles/sample.pmtiles',
        release_manifest=_load('release_manifest.valid.json'),
        evidence_bundle=_load('evidence_bundle.valid.json'),
        decision_envelope={'decision_ref': 'd2', 'decision': 'deny'},
        signature_bundle=_load('signature.valid.json'),
        request_tile=(0, 0, 0),
        runtime_policy_profile={'posture': 'strict'},
    )
    assert deny['runtime_response_envelope']['outcome'] == 'DENY'
