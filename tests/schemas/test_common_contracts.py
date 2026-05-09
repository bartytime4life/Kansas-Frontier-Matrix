import json
from pathlib import Path
import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]

SCHEMAS = [
    ('common/spec_hash','schemas/contracts/v1/common/spec_hash.schema.json'),
    ('source/source_descriptor','schemas/contracts/v1/source/source_descriptor.schema.json'),
    ('source/ingest_receipt','schemas/contracts/v1/source/ingest_receipt.schema.json'),
    ('evidence/evidence_ref','schemas/contracts/v1/evidence/evidence_ref.schema.json'),
    ('evidence/evidence_bundle','schemas/contracts/v1/evidence/evidence_bundle.schema.json'),
    ('runtime/runtime_response_envelope','schemas/contracts/v1/runtime/runtime_response_envelope.schema.json'),
    ('runtime/decision_envelope','schemas/contracts/v1/runtime/decision_envelope.schema.json'),
    ('runtime/run_receipt','schemas/contracts/v1/runtime/run_receipt.schema.json'),
    ('runtime/ai_receipt','schemas/contracts/v1/runtime/ai_receipt.schema.json'),
    ('policy/policy_decision','schemas/contracts/v1/policy/policy_decision.schema.json'),
    ('policy/sensitivity_label','schemas/contracts/v1/policy/sensitivity_label.schema.json'),
    ('governance/review_record','schemas/contracts/v1/governance/review_record.schema.json'),
]


def _validator(schema_rel):
    return Draft202012Validator(json.loads((ROOT / schema_rel).read_text()))


@pytest.mark.parametrize('family,schema_rel', SCHEMAS)
def test_valid_fixtures_validate(family, schema_rel):
    validator = _validator(schema_rel)
    for fp in (ROOT / 'fixtures/contracts/v1' / family / 'valid').glob('*.json'):
        errs = list(validator.iter_errors(json.loads(fp.read_text())))
        assert not errs, f'{family} valid fixture failed: {fp} {errs[0].message if errs else ""}'


@pytest.mark.parametrize('family,schema_rel', SCHEMAS)
def test_invalid_fixtures_fail(family, schema_rel):
    validator = _validator(schema_rel)
    for fp in (ROOT / 'fixtures/contracts/v1' / family / 'invalid').glob('invalid_*.json'):
        expected = fp.with_suffix('.expected_error.txt').read_text().strip()
        errs = list(validator.iter_errors(json.loads(fp.read_text())))
        assert errs, f'{family} invalid fixture passed: {fp}'
        msg = errs[0].message.lower()
        assert any(token in msg for token in expected.lower().split('|'))


def test_runtime_response_minimal_roundtrip_validates():
    schema_rel = 'schemas/contracts/v1/runtime/runtime_response_envelope.schema.json'
    validator = _validator(schema_rel)
    doc = {
        'id': 'resp-min', 'spec_hash': 'sha256:' + 'a' * 64, 'version': 'v1',
        'issued_at': '2026-05-09T00:00:00Z', 'outcome': 'ABSTAIN', 'reason_code': 'NOT_READY',
        'evidence_refs': [], 'policy_state': 'baseline', 'freshness': 'current', 'correction_state': 'none'
    }
    assert not list(validator.iter_errors(doc))
