import pytest
pytest.importorskip("jsonschema", reason="jsonschema dependency unavailable in this environment")

import json
from pathlib import Path
from jsonschema import Draft202012Validator


def test_run_receipt_with_consent_and_revoked_validate_and_negative_hash():
    schema = json.loads(Path("schemas/receipts/run_receipt.v1.json").read_text())
    doc1 = json.loads(Path("tests/fixtures/consent/run_receipt.with_consent.valid.json").read_text())
    doc2 = json.loads(Path("tests/fixtures/consent/run_receipt.revoked.valid.json").read_text())
    v = Draft202012Validator(schema)
    assert not list(v.iter_errors(doc1))
    assert not list(v.iter_errors(doc2))
    bad = json.loads(json.dumps(doc1)); bad["obligations_snapshot"]["obligations_snapshot_hash"] = "oops"
    assert list(v.iter_errors(bad))
