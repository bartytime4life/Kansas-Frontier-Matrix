# VerificationStateHistory fixtures

Synthetic, no-network fixtures for the [VerificationStateHistory contract](../../../../../contracts/evidence/verification_state_history.md) and its [JSON Schema](../../../../../schemas/contracts/v1/evidence/verification_state_history.schema.json).

The valid lane covers a late-recorded correction followed by re-verification and supersession, plus revocation followed by re-verification. The invalid lane covers missing conditional shape, broken chain linkage, an effective time after recorded time, an effective-time inversion that would orphan a successor during replay, an impossible UTC timestamp, hash mismatch, append-order drift, and a prohibited transition after supersession.

Files beginning with `invalid_` are schema-negative cases used by the generic schema harness. Files beginning with `semantic_` remain schema-valid and are rejected by the specialized validator. Every identifier and reference is visibly synthetic; these fixtures contain no source records, real releases, exact locations, personal data, evidence, policy decisions, or publication state.

```bash
KFM_NO_NETWORK=1 python tools/validators/validate_verification_state_history.py --fixtures
KFM_NO_NETWORK=1 python -m pytest -q tests/schemas/test_verification_state_history.py
```
