# Policy Authority Map
- Current homes: `policy/` and `policies/`.
- Likely authority: `policy/` as primary policy-as-code; `policies/` legacy/compatibility.
- Interim use: dual-home read-only compatibility.
- Prohibited duplication: duplicate policy package names across homes.
- Migration rule: consolidate only via ADR-authorized plan.
- Validator expectation: detect duplicate package names and unresolved split.
- Decision owner/status: CONFLICTED, open.
- Rollback risk: medium/high for gate behavior.
