# Schema Authority Map
- Current homes: `contracts/`, `schemas/`, `jsonschema/`.
- Likely authority: `contracts/` semantic contract meaning; `schemas/` machine validation authority; `jsonschema/` compatibility package.
- Interim use: allowed with explicit cross-reference and no duplicate IDs.
- Prohibited: duplicate canonical schema IDs across homes.
- Migration rule: ADR-0001 + ADR-0012 first, then validator-gated migrations.
- Validator expectation: detect duplicate `$id` and same logical object in multiple homes.
- Decision owner/status: CONFLICTED, owner TBD, status open.
- Rollback risk: high for runtime and CI consumers.
