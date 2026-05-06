import json
from pathlib import Path
from runtime.tiles.verified_runtime import process_tile_request


def _load(name: str):
    return json.loads((Path('fixtures/runtime') / name).read_text())


def test_missing_evidence_abstains():
    result = process_tile_request(
        pmtiles_uri='fixtures/runtime/pmtiles/sample.pmtiles',
        release_manifest=_load('release_manifest.valid.json'),
        evidence_bundle=None,
        decision_envelope=_load('decision.allow.json'),
        signature_bundle=_load('signature.valid.json'),
        request_tile=(0, 0, 0),
        runtime_policy_profile={'posture': 'strict'},
    )
    assert result['runtime_response_envelope']['outcome'] == 'ABSTAIN'
    assert result['runtime_response_envelope']['reason'] == 'missing_evidence_bundle'
