# Generic ValidationReport validation fixtures

This fixture lane proves only the current PROPOSED Draft 2020-12 schema at `schemas/contracts/v1/data/validation_report.schema.json` and bounded JSON-input safety.

- `valid/minimal.json` demonstrates the schema's current `id`-only minimum.
- `invalid/missing_id.json` proves the current required-field boundary fails closed.
- `tools/validators/data/validate_validation_report.py --fixtures` runs deterministically without network access or repository mutation.

A passing fixture profile records shape conformance only. It does **not** prove the target is true, the validator is sufficient for a domain, evidence is resolved, policy allows use, review is complete, a proof pack closes, promotion or release is authorized, a correction is applied, or publication occurred. The generic family also does not replace the existing soil-specific `DomainValidationReport` extension; their relationship remains separately governed.
