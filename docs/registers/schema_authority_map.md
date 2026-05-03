# Schema Authority Map

- Status: CONFLICTED
- Current homes: `schemas/`, `contracts/`, `jsonschema/`.
- Likely authority: `schemas/` for machine validation schemas; `contracts/` for semantic contracts; `jsonschema/` library/runtime support.
- Allowed interim use: keep existing references, no cross-home machine-file moves.
- Prohibited duplication: duplicate schema IDs across homes.
- Migration rule: require ADR authorization before moving machine schema files.
- Validator expectation: detect duplicate `$id` and home divergence.
- Owner/status: UNKNOWN owner; PROPOSED for architecture review.
- Rollback risk: high if machine files moved without ADR.
