# Policy authority map

| Home | Family | Likely authority | Interim use | Prohibited duplication | Migration rule | Validator expectation | Owner/status | Rollback risk |
|---|---|---|---|---|---|---|---|---|
| `policy/` | rego bundles + policy docs | policy authority | canonical | duplicate package names in `policies/` | no cross-home move without ADR | conflict noted in reorg report | Policy owners / CONFLICTED | high |
| `policies/` | legacy/compat docs + rule files | compatibility lane | temporary | authoritative split | converge via ADR-0013 follow-up | ensure authority map present | Policy owners / CONFLICTED | medium |
