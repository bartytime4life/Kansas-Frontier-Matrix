import pytest
pytest.importorskip("jsonschema", reason="jsonschema dependency unavailable in this environment")

import json
from pathlib import Path
from jsonschema import Draft202012Validator


def test_evidence_bundle_with_consent_validates_and_negative_case():
    schema = json.loads(Path("schemas/evidence/EvidenceBundle.v1.json").read_text())
    doc = json.loads(Path("tests/fixtures/consent/evidence_bundle.with_consent.valid.json").read_text())
    assert not list(Draft202012Validator(schema).iter_errors(doc))
    bad = json.loads(json.dumps(doc)); del bad["consent"]["consent_vc_id"]
    assert list(Draft202012Validator(schema).iter_errors(bad))
