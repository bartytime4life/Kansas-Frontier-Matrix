# Cosign attestation verification plan fixtures

Synthetic, public-safe fixtures for `CosignAttestationVerificationPlan`.

## Layout

```text
valid/
  valid_keyless_v3.json
  valid_keyed_v2.json
invalid/
  invalid_*.json                 # true JSON-Schema negatives
  semantic_invalid_*.json        # schema-valid semantic negatives
  expected_findings_manifest.json
```

The valid plans exercise patched Cosign 3.x keyless and 2.x keyed tracks. The negative corpus covers missing/unknown schema fields, vulnerable versions, disabled claim validation, subject mismatch, incomplete keyless identity, network and registry weakening, missing transparency requirements, unsupported command selection, governance overclaim, and `spec_hash` drift.

These fixtures contain no real signature, certificate, key, bundle, release artifact, source record, evidence, personal data, precise sensitive geometry, credential, or public-use authorization. Paths and digests are synthetic declarations.

Run:

```bash
python tools/validators/release/validate_cosign_attestation_verification_plan.py --fixtures
python -m unittest discover \
  --start-directory tests/release \
  --pattern 'test_cosign_attestation_verification_plan.py' \
  --verbose
```

A passing fixture is a plan-preflight result only. It is not cryptographic verification.
