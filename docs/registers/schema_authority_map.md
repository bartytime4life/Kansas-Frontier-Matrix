# Schema Authority Map
- Current homes: `contracts/`, `schemas/`, `jsonschema/`.
- Likely authority: semantic contracts in `contracts/`; machine validation in `schemas/`; compatibility/library helpers in `jsonschema/`.
- Interim use: allowed with ADR-0001/0012 compatibility posture.
- Prohibited duplication: same schema ID duplicated across homes.
- Migration rule: move only with ADR + validator update.
- Validator expectation: detect duplicate IDs and unsupported homes.
- Decision owner/status: CONFLICTED, open.
- Rollback risk: high for machine consumers.
