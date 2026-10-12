# WithdrawalNotice validation fixtures

This fixture lane proves only the current PROPOSED Draft 2020-12 schema at `schemas/contracts/v1/release/withdrawal_notice.schema.json` and bounded JSON-input safety.

- `valid/minimal.json` demonstrates the schema's current `id`-only minimum.
- `invalid/missing_id.json` proves the current required-field boundary fails closed.
- `tools/validators/release/validate_withdrawal_notice.py --fixtures` runs deterministically without network access or repository mutation.

A passing fixture profile does **not** prove withdrawal completion, correction linkage, downstream cache/index/tile/API/map/AI invalidation, rights or sensitivity review, rollback execution, release authority, or publication state. The richer semantic fields described by `contracts/release/withdrawal_notice.md` remain proposal-level until separately governed and schema-backed.
