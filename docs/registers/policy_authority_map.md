# Policy Authority Map
- current homes: `policy/`, `policies/`.
- likely authority: `policy/` primary (ADR-0013), `policies/` compatibility/legacy.
- allowed interim use: docs and examples may coexist.
- prohibited duplication: same policy package names in both homes.
- migration rule: no rego moves without explicit ADR update and tests.
- validator expectation: detect duplicate policy packages and untracked split.
- decision owner/status: CONFLICTED / pending.
- rollback risk: medium-high.
