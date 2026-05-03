# Policy Authority Map
- Current homes: `policy/` and `policies/`.
- Likely authority: `policy/` as primary policy-as-code; `policies/` legacy/compatibility.
- Interim use: dual-home read-only compatibility.
- Prohibited duplication: duplicate policy package names across homes.
- Migration rule: consolidate only via ADR-authorized plan.
- Validator expectation: detect duplicate package names and unresolved split.
- Decision owner/status: CONFLICTED, open.
- Rollback risk: medium/high for gate behavior.

## 2026-05-03 reorg checkpoint
- Current homes: `policy/` (primary), `policies/` (compatibility lane).
- Allowed interim use: docs may reference both; executable policy migration requires ADR-0013 approval.
- Prohibited duplication: do not duplicate policy package names across homes.
- Validator expectation: authority conflicts must be listed in `docs/registers/reorg/authority_conflicts.md`.
