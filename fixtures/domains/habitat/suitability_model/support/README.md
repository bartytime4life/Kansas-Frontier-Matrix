# Support fixtures

Standalone ModelCardEnvelope documents used only to exercise
`validate_suitability_model.py`'s optional `model_card_ref` linkage check.

- `model_card_pass.json` is an exact copy of the real, committed
  `fixtures/contracts/v1/governance/model_card_envelope/base.json`, which
  independently passes `tools/validators/governance/validate_model_card_envelope.py`.
- `model_card_fail.json` is the same document with `spec_hash` replaced by an
  all-zero placeholder, so it independently fails that same validator with
  `SPEC_HASH_MISMATCH`.

Neither file is a SuitabilityModel candidate itself; both are pointed at by
`model_card_ref` in the sibling `valid/` and `invalid/` fixtures.
