# SourceEventEnvelopeCandidate Fixtures

These synthetic fixtures exercise the fixture-only `SourceEventEnvelopeCandidate` contract.

## Lanes

| Lane | Purpose | Naming rule |
|---|---|---|
| `valid/` | Shape-valid and semantically coherent candidates. | `valid_*.json` |
| `invalid/` | Intentionally JSON-Schema-invalid candidates. | `invalid_*.json` |
| `semantic_invalid/` | JSON-Schema-valid candidates denied by deterministic semantic checks. | `semantic_invalid_*.json` |

`expected_findings_manifest.json` binds every case to its exact finite outcome and stable finding codes. The generic repository contract test consumes only `invalid/invalid_*.json` as schema-negative vectors; semantic negatives remain separate so schema and semantic polarity cannot collapse.

## Synthetic-only boundary

The records use synthetic source references, evidence references, policy references, hashes, times, and payload attributes. They do not identify or activate a real source. They perform no network, queue, orchestration, policy, signing, lifecycle, release, or publication operation.

## Validation

```bash
python tools/validators/validate_source_event_envelope.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_source_event_envelope.py' \
  --verbose
```

A passing result proves only the bounded local profile. It is not CloudEvents conformance, source admission, source activation, policy approval, human review, release, or publication authority.
