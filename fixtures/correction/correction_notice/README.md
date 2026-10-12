# CorrectionNotice validation fixtures

This fixture lane proves only the current PROPOSED Draft 2020-12 schema at `schemas/contracts/v1/correction/correction_notice.schema.json` and bounded JSON-input safety.

- `valid/minimal.json` demonstrates the schema's current `id`-only minimum.
- `invalid/missing_id.json` proves the current required-field boundary fails closed.
- `tools/validators/correction/validate_correction_notice.py --fixtures` runs deterministically without network access or repository mutation.
- `tools/validators/validate_correction_notice.py --fixtures` remains a compatibility entry point with the same result.

A passing fixture profile does **not** prove correction issuance, evidence closure, policy or human approval, supersession, withdrawal, downstream cache/index/tile/API/map/AI propagation, rollback execution, release authority, or publication state. Richer semantics described by `contracts/correction/correction_notice.md` and competing schema candidates remain unresolved until separately governed.
