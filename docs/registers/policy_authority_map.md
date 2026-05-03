# Policy Authority Map

- Status: CONFLICTED
- Current homes: `policy/`, `policies/`.
- File families found: README, rego/json policy artifacts.
- Likely authority: `policy/` appears primary; `policies/` retained as compatibility lane pending ADR.
- Allowed interim use: docs-only indexing and explicit split disclosure.
- Prohibited duplication: duplicate policy package ownership across both homes.
- Migration rule: require ADR before relocating executable policy files.
- Validator expectation: detect unresolved split entry in authority map.
- Owner/status: UNKNOWN owner; OPEN.
- Rollback risk: medium/high if executable policy files are moved.
