# Authority conflicts

## Schema homes (`contracts/` vs `schemas/` vs `jsonschema/`)
- **Status:** CONFLICTED
- **Observed:** All three homes exist and are populated.
- **Interim rule:** Keep semantic contracts in `contracts/`; machine validation schemas in `schemas/`; Python helper package in `jsonschema/`.
- **Prohibited:** Moving machine schema files between `contracts/` and `schemas/` without ADR authority.

## Policy homes (`policy/` vs `policies/`)
- **Status:** CONFLICTED
- **Observed:** Both homes exist and contain policy artifacts/readmes.
- **Interim rule:** `policy/` is canonical rule-pack home; `policies/` treated compatibility lane until ADR closure.
- **Prohibited:** Cross-home moves of Rego/rule files without ADR.
