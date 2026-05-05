# Schema Authority Map
Current homes: `contracts/`, `schemas/`, `jsonschema/`.
Likely authority: `schemas/` machine shapes, `contracts/` semantic contracts.
Prohibited duplication: same schema IDs across homes.
Migration rule: require ADR before moving machine schemas.
Validator expectation: detect duplicate schema IDs and unsupported homes (PROPOSED).
Owner/status: CONFLICTED / needs architecture owner decision.
Rollback risk: medium if moved without ADR.
