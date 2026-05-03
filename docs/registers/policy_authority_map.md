# Policy Authority Map
- Current homes: `policy/`, `policies/`.
- Likely authority: `policy/` primary executable policy lane per ADR-0013; `policies/` compatibility/examples lane.
- Interim use: permitted only with explicit pointers from `policies/` back to canonical `policy/` modules.
- Prohibited: divergent policy packages with same intent in both homes.
- Migration rule: single-home consolidation with ADR and regression tests.
- Validator expectation: duplicate package-name detection across homes.
- Decision owner/status: CONFLICTED, owner TBD, status open.
- Rollback risk: medium-high (admission/promotion gate drift).
