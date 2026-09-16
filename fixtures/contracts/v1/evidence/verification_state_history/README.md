# VerificationStateHistory fixtures

Synthetic, no-network fixtures for the [VerificationStateHistory contract](../../../../../contracts/evidence/verification_state_history.md) and its [JSON Schema](../../../../../schemas/contracts/v1/evidence/verification_state_history.schema.json).

The valid lane covers a late-recorded correction followed by re-verification and supersession, plus revocation followed by re-verification. The invalid lane covers missing conditional shape, broken chain linkage, an effective time after recorded time, an effective-time inversion that would orphan a successor during replay, an impossible UTC timestamp, hash mismatch, append-order drift, and a prohibited transition after supersession.

`valid_atlas_fixture_profile.json` adds the proposed `1.1.0` / Atlas fixture
profile with the exact original `overlay:synthetic-kansas-promotion-proof`
subject. Its events and supporting references are invented review fixtures,
not operational verification or approval. It covers late-recorded revocation,
re-verification, correction and terminal supersession. The two `invalid_atlas_`
cases reject a mixed legacy version and a different subject. The fixed Atlas
lookup never reads these histories and remains on review HOLD.

Files beginning with `invalid_` are schema-negative cases used by the generic schema harness. Files beginning with `semantic_` remain schema-valid and are rejected by the specialized validator. Every identifier and reference is visibly synthetic; these fixtures contain no source records, real releases, exact locations, personal data, evidence, policy decisions, or publication state.

```bash
KFM_NO_NETWORK=1 python tools/validators/validate_verification_state_history.py --fixtures
KFM_NO_NETWORK=1 python -m pytest -q tests/schemas/test_verification_state_history.py
KFM_NO_NETWORK=1 python -m pytest -q tests/schemas/test_atlas_verification_profile.py
```
